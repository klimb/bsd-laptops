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
 'disk 1 (da0)': '920G',
 'disk 2 (nda0)': '954G',
 'display': {'max resolution': '2160x1350', 'name': 'eDP-1'},
 'wifi': 'rtwn1 rtwn0 iwlwifi0',
 'webcam': {'max resolution': 'uxga', 'works?': False},
 'rtl-sdr?': True,
 'microphone': {'sample rate': 44100.0, 'works?': True}}

Requires following packages:
pkg install python opencv pwcview

And python dependencies (pip is a package manager for python3):
pip install opencv-python psutil screeninfo pyaudio
