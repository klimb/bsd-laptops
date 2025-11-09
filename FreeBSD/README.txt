Usage:
./freebsd_laptop_compatibility_report.py

Sample output (for thinkpad x1 nano gen2):
{'platform': {'processor': 'amd64',
              'machine': 'amd64',
              'model': ' 12th Gen Intel(R) Core(TM) i7-1280P',
              'cores': 8,
              'threads': 20,
              'kernel': 'FreeBSD 14.3-RELEASE-p5 GENERIC'},
 'memory': '32 MB',
 'disk 1': '920G',
 'disk 2': '954G',
 'screen': {'max resolution': '2160x1350', 'type': 'modern'},
 'wifi': 'rtwn1 rtwn0 iwlwifi0',
 'webcam': {'max resolution': 'uxga', 'works?': False},
 'rtl-sdr?': True}

Requires following packages:
pkg install python opencv pwcview

And python dependencies (pip is a package manager for python3):
pip install opencv-python psutil screeninfo pyaudio