a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
nbre = a.count("i") # nombre de fois que le caractere i apparait dans la chaine a
haut = a.upper() # mise en majuscule
petit = a.lower() # mise en miniscule
test = a.islower() # verifie si tous les caracteres dans la chaine sont en miniscule
choix = a[2:10]
elimine = a.strip(" ") # elimine le charactere space avant et apres de la  chaine
print(a)
print(f"{nbre} fois pour le charactere  i dans la chaine de charactere")
print("majuscule : " + " " + haut)
print("miniscule : " + " " + petit)
print(test)
print(" apres elimination de i " + " " +elimine)
print("selection" + " " + choix)
