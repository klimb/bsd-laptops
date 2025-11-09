#!/usr/bin/env python3
#
# freebsd_laptop_compatibility_report.py 
#
# Design Goals:
# - be able to run this after OS install, from console without needing X or Wayland
# - try to get as much as possible from FreeBSD kernel (sysctl tree) and userland it ships with
# - only take dependencies on python modules and other apps if you have to, otherwise the number of dependencies
#   can get out of hand really quick
#

import os
import platform
import pprint
import subprocess
import screeninfo

import psutil

os.environ['OPENCV_LOG_LEVEL'] = 'OFF'
os.environ["OPENCV_FFMPEG_DEBUG"] = 'false'
os.environ['OPENCV_FFMPEG_LOGLEVEL'] = "0"
import cv2
import pyaudio


class FreeBSDLaptopCompatibilityReport:
    def __init__(self):
        self.report = dict()

    def check_cpu(self):
        self.report["platform"] = {
            "processor": platform.processor(),
            "machine": platform.machine(),
            "model":  (subprocess.run(["sysctl", "hw.model"], capture_output=True, text=True
                                    ).stdout).split(":")[-1].replace("\n", ""),
            "cores": psutil.cpu_count(logical=False),
            "threads": psutil.cpu_count(logical=True),
            "kernel": (
                subprocess.run(["sysctl", "kern.version"], capture_output=True, text=True)
                .stdout.split(":")[1].replace("\n", "").strip()
            )
        }

    def check_mem(self):
        self.report["memory"] = f"{(psutil.virtual_memory().total / (1024 * 1024 * 1024)):.0f} MB"

    def check_disks(self):
        try:
            disks = (subprocess.run(["sysctl", "kern.disks"], capture_output=True, text=True).stdout.split(":")[1]
                     .replace("\n", "").strip().split(" "))
            for i, disk in enumerate(disks):
                self.report[f"disk {i+1} ({disk})"] = (
                    (subprocess.run(["gpart", "show", disk], capture_output=True, text=True))
                    .stdout.splitlines()[0].split(" ")[-1].strip('()')
                )
        except:
            pass

    def check_screen_resolution(self):
        monitor = screeninfo.get_monitors()[0]
        self.report[f"display"] = {
            "max resolution": f"{monitor.width}x{monitor.height}",
            "name": monitor.name
        }

    def check_wifi_cards(self):
        self.report["wifi"] = subprocess.run(
            ['sysctl', "net.wlan.devices"], capture_output=True, text=True
            ).stdout.split(": ")[1].replace("\n", "")

    def check_webcam(self):
        def attempt_video_capture():
            capture = cv2.VideoCapture(0)
            if not capture.isOpened():
                return False
            else:
                ret, frame = capture.read()
                if ret:
                    return True
                else:
                    capture.release()
                    return False

        self.report["webcam"] = {
            "max resolution" : subprocess
               .run(['pwcview', "-h", "-s", "bogus"], capture_output=True, text=True)
               .stderr.replace("\n","").split(", ")[-1],
            "works?": attempt_video_capture()
        }

    def check_rtl_sdr(self):
        self.report["rtl-sdr?"] = True if (next((x for x in subprocess.run(
            ['dmesg'], capture_output=True, text=True).stdout.splitlines() if 'RTLSDR' in x), '')) else False

    def check_mic(self):
        p = pyaudio.PyAudio()
        for i in range(p.get_device_count()):
            device_info = p.get_device_info_by_index(i)
            is_mic = device_info['maxInputChannels'] > 0
            if is_mic:
                self.report["microphone"] = {
                    'sample rate': device_info['defaultSampleRate'],
                    'works?' : True
                }
                break
        p.terminate()

    def check_laptop_model(self):
        try:
            result = subprocess.run(['kenv', '|', 'grep', 'smbios.system.family'], capture_output=True, text=True,
                                    check=True, shell=True)
            output = result.stdout.strip()
            if 'smbios.system.family=' in output:
                model_name = output.split('smbios.system.family=')[1].strip().replace('"', '')
                self.report["laptop model"] = model_name.split("\n")[0]

            else:
                return "Model name not found using kenv."
        except:
            pass


    def run_checks(self):
        self.check_laptop_model()
        self.check_cpu()
        self.check_mem()
        self.check_disks()
        self.check_screen_resolution()
        self.check_wifi_cards()
        self.check_webcam()
        self.check_rtl_sdr()
        self.check_mic()

    def show_report(self):
        pp = pprint.PrettyPrinter(sort_dicts=False)
        pp.pprint(self.report)

if __name__ == "__main__":
    r = FreeBSDLaptopCompatibilityReport()
    r.run_checks()
    r.show_report()
