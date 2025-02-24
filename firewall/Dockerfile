FROM debian
RUN apt-get update && apt-get install -y iptables procps ulogd2 && apt-get clean
COPY firewall.sh /firewall.sh
RUN ls -l /
RUN chmod +x /firewall.sh
ENTRYPOINT ["/firewall.sh"]