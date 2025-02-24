FROM alpine
RUN apk add --no-cache iproute2 iputils
CMD sh -c "ip route del default && ip route add default via 172.18.0.100; exec ping 8.8.8.8"