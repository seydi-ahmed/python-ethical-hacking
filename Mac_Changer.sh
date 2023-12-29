# afficher l'actuelle adresse, changer puis réafficher
ifconfig eth0
ifconfig eth0 down
ifconfig hw ether "on met la nouvelle adresse MAC"
ifconfig eth0 up
ifconfig eth0