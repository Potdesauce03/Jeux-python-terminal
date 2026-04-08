import pymongo

def afficher_classement(db):

    print("\n" + "!" * 40)
    print("CLASSEMENT")
    print("!" * 40)
    
    # On récupère les 3 meilleurs scores
    top_scores = db["scores"].find().sort("score", -1).limit(3)
    
    place = 1
    # On utilise un curseur MongoDB pour parcourir les résultats
    for resultat in top_scores:
        nom = resultat.get("nom", "Inconnu")
        score = resultat.get("score", 0)
        
        print(f" Rang {place} : {nom}")
        print(f" Score : {score} vagues survécues")
        print("-" * 20)
        place = place + 1
    
    # Si personne n'a encore joué
    if place == 1:
        print(" Le classement est vide pour le moment...")
        print(" Soyez le premier !")
        print("!" * 40)
    else:
        print(" Félicitations au vainqueur !")
        print("!" * 40)
    print("\n")

def recuperer_liste_persos(db):
    # On récupère les 10 persos qu'on a mis dans db_init
    curseur = db["personnages"].find()
    liste_complete = []
    
    for perso in curseur:
        liste_complete.append(perso)
        
    # On retourne la liste pour que le menu puisse l'afficher
    return liste_complete