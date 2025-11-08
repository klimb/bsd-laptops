#!/usr/bin/env python3
#
# freebsd_laptop_compatibility_report.py 
# quick and dirty device checker (webcam, etc)
#

import os
import platform
import pprint
import subprocess

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
            "cores": psutil.cpu_count(logical=False),
            "threads": psutil.cpu_count(logical=True),
            "kernel": (
                subprocess.run(["sysctl", "kern.version"], capture_output=True, text=True)
                .stdout.split(":")[1].replace("\n", "").strip()
            )
        }

    def check_mem(self):
        self.report["memory"] = f"{(psutil.virtual_memory().total / (1024 * 1024 * 1024)):.0f} MB"


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

        self.report["webcam works?"] = attempt_video_capture()

    def check_disk(self):
        disk_name = (
            subprocess.run(["sysctl", "kern.disks"], capture_output=True, text=True)
            .stdout.split(":")[1]
            .replace("\n", "")
            .strip()
        )
        disk_info = (subprocess.run(["diskinfo", "-s", disk_name], capture_output=True, text=True).stdout
                     .replace("\n",""))
        self.report["disk"] = {
            'device': disk_name,
            'model': disk_info
        }

    def check_screen_resolution(self):
        self.report["screen"] = (next((l for l in __import__('subprocess').run(
                ['dmesg'], capture_output=True, text=True).stdout.splitlines() if 'VT' in l), '')
        ).split(" ")[-1]

    def run_checks(self):
        self.check_cpu()
        self.check_mem()
        self.check_disk()
        self.check_webcam()
        self.check_screen_resolution()

    def show_report(self):
        pp = pprint.PrettyPrinter(sort_dicts=False)
        pp.pprint(self.report)

if __name__ == "__main__":
    r = FreeBSDLaptopCompatibilityReport()
    r.run_checks()
    r.show_report()
