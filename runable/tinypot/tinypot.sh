#!/bin/bash
/sbin/iptables -t nat -A PREROUTING -p tcp --dport 1:65534 -j REDIRECT --to-ports 10000
screen -S test -d -m su - root /root/folder/folder/.program
/usr/bin/screen -S netcat -d -m /bin/netcat -l -k -p 10000 | tee -a /tmp/netcat.log
/usr/bin/screen -S tcpdump -d -m /sbin/tcpdump -i eth0 -w /tmp/tcpdump.pcap -C 1000 -W 10 -lenx -X -s 0 not port 655534
echo TinyPot running, use "screen -r [netcat|tcpdump] to access tools"
