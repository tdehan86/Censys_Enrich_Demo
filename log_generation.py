import random
import time
import logging
from datetime import datetime
import ipaddress
import requests

logging.basicConfig(filename='firewall.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

src_ips = [f'192.168.1.{i}' for i in range(1, 255)]
ports = [80, 443] + list(range(1, 65536))
protocols = ['TCP', 'UDP']

def generate_public_ip():
    while True:
        ip = ipaddress.IPv4Address(random.randint(1, 2**32 - 1))
        if not ip.is_private:
            return str(ip)

def get_country(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        return data['country']
    except:
        return 'Unknown'

def generate_log_entry():
    src_ip = random.choice(src_ips)
    dst_ip = generate_public_ip()
    src_port = random.randint(1024, 65535)
    
    if random.random() < 0.8:
        dst_port = random.choice([80, 443])
    else:
        dst_port = random.choice(ports)
    
    protocol = random.choice(protocols)
    action = random.choice(['ALLOW', 'BLOCK'])
    country = get_country(dst_ip)
    
    log_message = f"SRC={src_ip}:{src_port} DST={dst_ip}:{dst_port} PROTO={protocol} ACTION={action} COUNTRY={country}"
    logging.info(log_message)

while True:
    generate_log_entry()
    time.sleep(random.uniform(0.1, 1.0))
