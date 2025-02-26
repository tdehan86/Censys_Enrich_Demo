import sqlite3
import random
import time
import logging
from datetime import datetime

# Configuration du logger
logging.basicConfig(filename='firewall.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Connexion à la base de données SQLite
conn = sqlite3.connect('censys_data.db')
cursor = conn.cursor()

def get_random_internal_ip():
    return f"192.168.1.{random.randint(1, 254)}"

def get_random_host():
    cursor.execute("SELECT * FROM hosts ORDER BY RANDOM() LIMIT 1")
    return cursor.fetchone()

def generate_log_entry():
    src_ip = get_random_internal_ip()
    host = get_random_host()
    if not host:
        return  # Si aucun hôte n'est trouvé dans la base de données

    dst_ip, country, ports = host
    ports_list = ports.split(',') if ports else []
    
    if ports_list:
        dst_port = random.choice(ports_list)
    else:
        dst_port = random.randint(1, 65535)
    
    src_port = random.randint(1024, 65535)
    protocol = random.choice(['TCP', 'UDP'])
    action = random.choice(['ALLOW', 'BLOCK'])
    
    log_message = f"SRC={src_ip}:{src_port} DST={dst_ip}:{dst_port} PROTO={protocol} ACTION={action} COUNTRY={country}"
    logging.info(log_message)

# Générer des logs
while True:
    generate_log_entry()
    time.sleep(random.uniform(0.1, 1.0))  # Pause aléatoire entre 0.1 et 1 seconde

conn.close()
