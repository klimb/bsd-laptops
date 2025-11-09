Usage: as root on OpenBSD (it doesn't let python do much lol)
./open_laptop_compatibility_report.py

Sample output:
{'platform': {'processor': 'amd64',
              'machine': 'amd64',
              'model': 'Intel(R) Core(TM) i5-3320M CPU @ 2.60GHz',
              'cores': None,
              'threads': 4,
              'kernel': 'OpenBSD 7.8 GENERIC.MP#54'},
 'memory': '16 MB',
 'disk 1': '3726.0G',
 'disk 2': '920.4G',
 'screen': {'max resolution': '1366x768'},
 'webcam': {'max resolution': '1280x720', 'works?': True},
 'rtl-sdr?': False}
