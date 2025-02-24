FROM debian:latest
RUN apt-get update && apt-get install -y iptables iproute2
COPY firewall.sh /firewall.sh
RUN chmod +x /firewall.sh
ENTRYPOINT ["/firewall.sh"]
