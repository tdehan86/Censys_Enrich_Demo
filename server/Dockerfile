FROM alpine
RUN apk add --no-cache curl iproute2
CMD ["sh", "-c", "ip route add default via 192.168.1.1"]
