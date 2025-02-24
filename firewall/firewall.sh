#!/bin/bash
#which sysctl || echo "sysctl introuvable"
# Activer le forwarding IP
sysctl -w net.ipv4.ip_forward=1

# Activer le NAT pour router le trafic vers l'extérieur
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# Loguer uniquement les paquets sortants vers Internet
iptables -A FORWARD -o eth0 -j ULOG --log-prefix "FW_OUT: " --log-level 4
dmesg -w
# Garder le conteneur actif
tail -f /dev/null
