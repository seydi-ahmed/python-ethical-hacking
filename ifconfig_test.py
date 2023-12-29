import subprocess
import re

# exécuter la commande ifconfig
result = subprocess.run(["ifconfig"], capture_output=True, text=True)
ifconfig_output = result.stdout
print(ifconfig_output)

# Lire l'adresse MAC à partir de la sortie
mac_address_pattern = re.compile(r"([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}")
mac_address_match = mac_address_pattern.search(ifconfig_output)
if mac_address_match:
    current_mac = mac_address_match.group(0)
    print(current_mac)
else:
    print("Impossible de trouver l'adresse MAC dans la sortie d'ifconfig.")
