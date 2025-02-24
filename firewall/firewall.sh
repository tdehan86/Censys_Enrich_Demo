#!/bin/bash
sysctl -w net.ipv4.ip_forward=1
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth0 -o eth0 -j ACCEPT
iptables -A FORWARD -s 10.10.10.0/24 -j ACCEPT
tail -f /dev/null  # Pour garder le conteneur actif
