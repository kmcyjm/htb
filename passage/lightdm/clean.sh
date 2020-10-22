#!/bin/bash
if [ "$(/usr/bin/id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi
/bin/rm -rf /tmp/guest-* /tmp/old.guest-*
/usr/bin/shred -fu /var/tmp/run.sh /var/tmp/shell /var/tmp/boc /var/log/kern
.log /var/log/audit/audit.log /var/log/lightdm/*
/bin/echo > /var/log/auth.log
/bin/echo > /var/log/syslog
/bin/dmesg -c >/dev/null 2>&1
/bin/echo "Do you want to remove exploit (y/n)?"
read answer
if [ "$answer" == "y" ]; then
/usr/bin/shred -fu /var/tmp/kodek/* /var/tmp/kodek/bin/*
/bin/rm -rf /var/tmp/kodek
else
exit
fi
