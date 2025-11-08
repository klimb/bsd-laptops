Usage:
./freebsd_laptop_compatibility_report.py

Requires following packages:
pkg install python opencv pwcview

And python dependencies (pip is a package manager for python3):
pip install opencv-python
pwcview

Sample output (for thinkpad-classic-x230t):
{'platform': {'processor': 'amd64',
              'machine': 'amd64',
              'model': ' Intel(R) Core(TM) i5-3320M CPU @ 2.60GHz',
              'cores': 2,
              'threads': 4,
              'kernel': 'FreeBSD 14.3-RELEASE-p5 GENERIC'},
 'memory': '16 MB',
 'disk 1': '3.6T',
 'screen': {'max resolution': '1366x768', 'comment': 'sucks'},
 'wifi cards': 'rtwn1 rtwn0 iwn0',
 'webcam': {'max resolution': 'uxga', 'works?': True},
 'rtl-sdr?': True}
