import os
from dotenv import load_dotenv
from censys.search import CensysHosts

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les credentials depuis les variables d'environnement
CENSYS_API_ID = os.getenv('CENSYS_API_ID')
CENSYS_API_SECRET = os.getenv('CENSYS_API_SECRET')

# Initialiser le client Censys
h = CensysHosts(api_id=CENSYS_API_ID, api_secret=CENSYS_API_SECRET)

# Le reste de votre code...


def check_ip(ip_address):
    try:
        host_data = h.view(ip_address)
        
        print(f"Informations pour {ip_address}:")
        print(f"Localisation: {host_data.get('location', {}).get('country', 'N/A')}")
        print(f"ASN: {host_data.get('autonomous_system', {}).get('name', 'N/A')}")
        
        # Récupérer et afficher les labels
        labels = host_data.get('labels', [])
        if labels:
            print("Labels associés:")
            for label in labels:
                print(f"  - {label}")
        else:
            print("Aucun label associé.")
        
        # Afficher les services ouverts
        print("Services ouverts:")
        for service in host_data.get('services', []):
            print(f"  - Port {service['port']}: {service['service_name']}")
        
    except Exception as e:
        print(f"Erreur lors de la vérification de {ip_address}: {str(e)}")

# Liste des adresses IP à vérifier
ip_list = ['8.8.8.8', '1.1.1.1']

for ip in ip_list:
    check_ip(ip)
    print("\n")
