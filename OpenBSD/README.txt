Usage:
./open_laptop_compatibility_report.py

requires packages:
pkg_add py3-ifaddr py3-psutil

Sample output:
{'platform': {'processor': 'amd64',
              'machine': 'amd64',
              'model': 'Intel(R) Core(TM) i5-3320M CPU @ 2.60GHz',
              'cores': None,
              'threads': 4,
              'kernel': 'OpenBSD 7.8 GENERIC.MP#54'},
 'memory': '16 MB',
 'size of mount point /': '0.96 GB',
 'screen': {'max resolution': '1366x768'},
 'wifi': ['iwn0'],
 'webcam': {'max resolution': '1280x720', 'works?': True},
 'rtl-sdr?': False}

