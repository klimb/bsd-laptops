## FreeBSD running perfect on laptops!!!

Please share a report for yours (by creating a folder structure for your laptop ^ here, by creating a pull request).
Its going to be like /usr/ports but for laptops. 

Fixing a particular problem / system tweak is a single point of change and we all benefit from it.

Usage:
```
./freebsd_laptop_compatibility_report.py
```

Sample output (for thinkpad x1 nano gen2):

```
{'laptop': 'ThinkPad X1 Nano Gen 2',
 'kernel': 'FreeBSD 14.3-RELEASE-p5 GENERIC',
 'processor': {'arch': 'amd64',
               'model': ' 12th Gen Intel(R) Core(TM) i7-1280P',
               'cores': 8,
               'threads': 20},
 'memory': '32 GB',
 'drives': [{'disk 1': {'size': '920G', 'name': 'da0'}},
            {'disk 2': {'size': '954G', 'name': 'nda0'}}],
 'display': {'resolution': '2160x1350'},
 'networking': [{'wifi card 0': 'rtwn1'},
                {'wifi card 1': 'rtwn0'},
                {'wifi card 2': 'iwlwifi0'}],
 'webcam': {'max resolution': 'uxga', 'works?': False},
 'rtl-sdr?': True,
 'microphone': {'sample rate': 44100.0, 'works?': True}}
```

Requires following packages:
```
pkg install python opencv pwcview
```

And python dependencies (pip is a package manager for python3):

```
pip install opencv-python psutil screeninfo pyaudio
```
