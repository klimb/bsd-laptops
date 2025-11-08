#!/usr/bin/env python3
#
# freebsd_laptop_compatibility_report.py 
# quick and dirty device checker (webcam, etc)
#

import os
import platform
import pprint
import subprocess
from idlelib.pyshell import capture_warnings

import psutil

os.environ['OPENCV_LOG_LEVEL'] = 'OFF'
os.environ["OPENCV_FFMPEG_DEBUG"] = 'false'
os.environ['OPENCV_FFMPEG_LOGLEVEL'] = "0"
import cv2


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
        disks = (subprocess.run(["sysctl", "kern.disks"], capture_output=True, text=True).stdout.split(":")[1]
                 .replace("\n", "").strip().split(" "))
        for i, disk in enumerate(disks):
            self.report[f"disk {i+1}"] = (
                (subprocess.run(["gpart", "show", disk], capture_output=True, text=True))
                .stdout.splitlines()[0].split(" ")[-1].strip('()')
            )

    def check_screen_resolution(self):
        screen_resolution = (next(
            (l for l in subprocess.run(['dmesg'], capture_output=True, text=True).stdout.splitlines() if
             'VT' in l), '')).split(" ")[-1]
        self.report["screen"] = {
            "max resolution": screen_resolution,
            "comment": "sucks" if bool(int(screen_resolution.split("x")[0]) < 2048) else "doable"
        }

    def check_wifi_cards(self):
        self.report["wifi cards"] = subprocess.run(
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

    def run_checks(self):
        self.check_cpu()
        self.check_mem()
        self.check_disks()
        self.check_screen_resolution()
        self.check_wifi_cards()
        self.check_webcam()
        self.check_rtl_sdr()

    def show_report(self):
        pp = pprint.PrettyPrinter(sort_dicts=False)
        pp.pprint(self.report)

if __name__ == "__main__":
    r = FreeBSDLaptopCompatibilityReport()
    r.run_checks()
    r.show_report()
