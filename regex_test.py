import re

# Chaîne de caractères à analyser
texte = "Les numéros de téléphone sont: 123-456-7890, 234-773-9981 et 567-451-7865"

# Expression régulière pour rechercher un numéro de téléphone
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

# Recherche du motif dans le texte
resultat = pattern.findall(texte) # tous les numéros
# resultat = pattern.search(texte) le premier numéro puis print(resultat.group())

# Affichage du résultat
if resultat:
    print("Numéro de téléphone trouvé :", resultat)
else:
    print("Aucun numéro de téléphone trouvé.")
