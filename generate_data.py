import sqlite3
from censys.search import CensysHosts
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Récupérer les credentials depuis les variables d'environnement
CENSYS_API_ID = os.getenv('CENSYS_API_ID')
CENSYS_API_SECRET = os.getenv('CENSYS_API_SECRET')

# Initialiser le client Censys
h = CensysHosts(api_id=CENSYS_API_ID, api_secret=CENSYS_API_SECRET)
print("Début du script")

# Connexion à la base de données SQLite
conn = sqlite3.connect('censys_data.db')
cursor = conn.cursor()

# Créer la table si elle n'existe pas
cursor.execute('''
CREATE TABLE IF NOT EXISTS hosts (
    ip TEXT PRIMARY KEY,
    country TEXT,
    ports TEXT
    )
''')

def fetch_and_store_data(query, max_results):
    for result in h.search(query, per_page=100, pages=max_results//100):
        for host in result:
            ip = host.get('ip', 'Unknown')
            country = host.get('location', {}).get('country', 'Unknown')
            #asn = host.get('autonomous_system', {}).get('name', 'Unknown')
            ports = ','.join(str(service.get('port', '')) for service in host.get('services', []))
            #services = ','.join(service.get('service_name', '') for service in host.get('services', []))

            cursor.execute('''
            INSERT OR REPLACE INTO hosts (ip, country, ports)
            VALUES (?, ?, ?)
            ''', (ip, country, ports))

    conn.commit()



# Exemple de requête pour obtenir des hôtes avec des ports ouverts
fetch_and_store_data("services.port: 80 OR services.port: 443",1000)
fetch_and_store_data("labels:c2",1)

# Fermer la connexion à la base de données
conn.close()

print("Données récupérées et stockées avec succès.")
