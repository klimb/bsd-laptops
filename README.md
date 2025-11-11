![](https://www.freebsd.org/images/banner-red.png)
![](https://www.openbsd.org/images/puffy78.gif)

## FreeBSD and OpenBSD on laptops!!!


Purpose: 
* to get all hardware working perfect on specific laptops
* this is like /usr/ports .. but for laptops, and so you know what to buy :)
* What is the best laptop for FreeBSD or OpenBSD? (run freebsd_laptop_compatibility_report.py (feel free to modify it) and submit your system)

Friends, would you please share your system configs and dmesg (by making some commits here) so we can get all hardware working perfect on specific laptop models? Suspend/resume, webcam, audio, headphones, built-in & external mic, fingerprint reader, WIFI cards, etc. I'll make you admin/collaborator if you'd like to help out. 

## how to add your laptop to this repo (FreeBSD example)
```
mkdir ~/src
cd ~/src
git clone https://github.com/klimb/bsd-laptops.git

cd bsd-laptops/FreeBSD
mkdir some_laptop_model_you
./freebsd_laptop_compatibility_report.py > some_laptop_model_you/compatibility-report.json
dmesg > some_laptop_model_you/dmesg.txt

mkdir some_laptop_model_you/etc
cp /etc/rc.conf some_laptop_model_you/etc
...
```

* clone this repo
* create a directory for your laptop using similar naming convention as others here
* copy your system files .. tweaks you had to do to get stuff working, organize it just like the OS does.
* add your dmesg output + compatibility report. 
* write a little readme of what works to some_laptop_model_you/REAMDE.md 
* create a pull request "adding some_laptop_model_you". [How to contribute to someone's repository](https://kbroman.org/github_tutorial/pages/fork.html)

We're going to automate getting hardware to work 100% perfect, but for now .. collecting system configs.

Some related articles:
- [FreeBSD on a thinkpad x230 tablet](https://www.linkedin.com/pulse/freebsd-thinkpad-x230t-dmitry-kalashnikov-3ya5c)
- [OpenBSD on a laptop](https://www.linkedin.com/pulse/openbsd-laptop-dmitry-kalashnikov-innmc)
- [Recording a failed login using a Webcam, and securing OS boot, biometric auth with PAM](https://www.linkedin.com/pulse/security-recording-videopics-failed-login-pam-dmitry-kalashnikov-ifuoc)
- [Linux is not an operating system: part 2](https://www.linkedin.com/pulse/linux-operating-system-part-2-dmitry-kalashnikov-9lpdc)
- [Linux is not an operating system: part 1](https://www.linkedin.com/pulse/linux-operating-system-dmitry-kalashnikov-uyfgc)
- [UNIX userland was always as mess, you're just used to it](https://www.linkedin.com/pulse/unix-userland-always-mess-youre-just-used-dmitry-kalashnikov-2k6sc)

Links:
- [OpenBSD Laptops](https://jcs.org/openbsd-laptops)
- [FreeBSD Foundation Project Laptop Repo](https://github.com/FreeBSDFoundation/proj-laptop)
