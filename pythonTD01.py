#utilisateur va entrer un nombre et on va afficher la table de multiplication qui correspond au nombre
"""
pythonTD01.py
Récupérer ce que l'user va saisir
tester si c'est un nombre
afficher la table
demander s'il souhaite quitter
"""
continuer = True
while continuer == True:
	

	var = True
	while var == True:
		
		try:
			oSaisit = int(input("saississez un nombre pour avoir sa table de multiplication"))
			var = False
		except ValueError:
			print("Erreur veillez saisir un nombre")
			var = True

	print("nombre saisi : " + str(oSaisit))
	print("Sa table de multiplication est : ")
	for i in range(1,10):
		print(i*oSaisit)
	oQuitter = input("Voulez-vous quitter ?(tapper oui)")
	if oQuitter == 'oui' :
		continuer = False
	else :
		continuer = True