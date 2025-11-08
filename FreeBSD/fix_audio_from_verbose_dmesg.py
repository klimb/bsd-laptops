#!/usr/bin/env python
#
# Example: ./fix_audio_from_verbose_dmesg.py thinkpad-x1-nano-gen2_dvk/dmesg-verbose.txt
# 
# Creates a sample output:
# hint.hdaa.0.nid29.config="as=0 seq=0"
# hint.hdaa.0.nid18.config="as=3 seq=0"
# hint.hdaa.0.nid25.config="as=3 seq=14"
# hint.hdaa.0.nid33.config="as=1 seq=15"
#
# append it to /boot/device.hints to fix headphones
#

import re
import sys


def generate_hint_lines(log_text):
    patch_re = re.compile(r"nid=(\d+)\s+0x[0-9a-fA-F]+\s+->\s+0x([0-9a-fA-F]+)")

    results = []

    for nid, hexval in patch_re.findall(log_text):
        val = int(hexval, 16)
        asn = (val >> 4) & 0xF
        seq = val & 0xF
        hint_line = f'hint.hdaa.0.nid{nid}.config="as={asn} seq={seq}"'
        results.append(hint_line)

    return "\n".join(results)


def main():
    if len(sys.argv) != 2:
        print("Example: ./fix_audio_from_verbose_dmesg.py thinkpad-x1-nano-gen2_dvk/dmesg-verbose.txt")
        print("To get dmesg-verbose.txt")
        print(" * boot FreeBSD in verbose mode (press 7 at boot loader)")
        print(" * dmesg > dmesg-verbose.txt")
        sys.exit(1)

    dmesg_verbose_file = sys.argv[1]

    try:
        with open(dmesg_verbose_file, "r") as file:
            content = file.read()
            print("add this to /boot/device.hints:")
            print(generate_hint_lines(content))
    except FileNotFoundError:
        print("Error: need dmesg-verbose.txt (and not just a normal dmesg)")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
