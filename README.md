![](https://www.freebsd.org/images/banner-red.png)
![](https://www.openbsd.org/images/puffy78.gif)

## FreeBSD and OpenBSD on laptops!!!

Goals: 
* to get all hardware working perfect on specific laptops
* this is like /usr/ports .. but for laptops, and so you know what to buy and what works for sure :)
* What is the best laptop for FreeBSD or OpenBSD? run *_laptop_compatibility_report.py

Friends, would you please share your system configs and dmesg (by making some commits here) so we can get all hardware working perfect on specific laptop models? Suspend/resume, webcam, audio, headphones, built-in & external mic, fingerprint reader, WIFI cards, etc. I'll make you admin/collaborator if you'd like to help out. Ideally, a laptop would be just an empty directory. But its not the case in 2025.

## how to add your laptop to this repo (FreeBSD example)
Please read: [How to contribute to someone's repository](https://kbroman.org/github_tutorial/pages/fork.html)
* fork this repo (click Fork ^ .. naming: "bsd-laptops-your-laptop-you")
* clone your forked repo to your computer
* add your laptop
  * copy your system files .. tweaks you had to do to get stuff working, organize it just like the OS does.
  * add your dmesg output + compatibility report. 
  * write a little readme of what works to some_laptop_model_you/README.md (optional)
* make sure you're not leaking any sensitive info (like wifi passwords if you're sharing /etc/wpa_supplicant.conf .. remove/redact them)
* commit and push 
* On github website, go to your forked repo and click on "Create Pull Request" button


```
# setup your forked repo
mkdir ~/src
cd ~/src
git clone https://github.com/you/bsd-laptops-your-laptop-you.git

cd bsd-laptops
git remote add bsdlaptops git://github.com/klimb/bsd-laptops
git remote -v

# add your laptop to FreeBSD directory
mkdir FreeBSD/some_laptop_model_you
./freebsd_laptop_compatibility_report.py > FreeBSD/some_laptop_model_you/compatibility-report.json
dmesg > FreeBSD/some_laptop_model_you/dmesg.txt

mkdir FreeBSD/some_laptop_model_you/etc
cp /etc/rc.conf FreeBSD/some_laptop_model_you/etc
...

# commit your changes to your forked repo
cd ~/src/bsd-laptops
git add .
git commit -m "adding your_laptop_model_you to FreeBSD"
git push
# and click on "create pull request" on github website (in your forked repo)
```

I know its a pain to work with git and github. But the laptop thing needs to be a repo (with proven configs, structured), not some webapp or write-ups. With verifiable reports. Laptops are expensive. Buy stuff that works for sure. Also, its almost 2026 -- we want 2k+ screens and every piece of hardware working. 

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

PS. If you're running NetBSD please contribute :)
![](https://www.netbsd.org/images/NetBSD-smaller-tb.png)
