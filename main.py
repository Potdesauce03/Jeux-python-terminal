import pymongo
import random



def afficher_classement(db):
    print("\n" + "="*30)
    print("      CLASSEMENT TOP 3")
    print("="*30)
    # On cherche les scores, triés du plus grand au plus petit
    scores = db["scores"].find().sort("score", -1).limit(3)
    
    rang = 1
    for s in scores:
        print(f"{rang}. {s['nom']} : {s['score']} vagues survécues")
        rang = rang + 1
    
    if rang == 1:
        print("Aucun score pour le moment. Soyez le premier !")
    print("="*30)

def recuperer_liste_persos(db):
    # On récupère tous les persos de la collection
    curseur = db["personnages"].find()
    liste = []
    for p in curseur:
        liste.append(p)
    return list(liste)

# Fonction de combat

def lancer_partie(db, nom_joueur, equipe):
    nb_vagues = 0
    equipe_en_vie = True
    
    while equipe_en_vie == True:
        # On pioche un monstre au hasard
        tous_les_monstres = list(db["monstres"].find())
        monstre = random.choice(tous_les_monstres)
        m_pv = monstre['pv']
        
        print(f"\n>>> VAGUE {nb_vagues + 1} <<<")
        print(f"Un {monstre['nom']} surgit ! (PV: {m_pv}, ATK: {monstre['atk']}, DEF: {monstre['def']})")
        
        # Boucle de combat contre le monstre
        while m_pv > 0 and equipe_en_vie == True:
            print("\n--- Tour des Héros ---")
            for hero in equipe:
                if hero['pv'] > 0:
                    # Calcul dégâts : Attaque - Défense
                    degats = hero['atk'] - monstre['def']
                    if degats < 0:
                        degats = 0
                    m_pv = m_pv - degats
                    print(f"{hero['nom']} frappe le {monstre['nom']} et retire {degats} PV.")
            
            if m_pv <= 0:
                print(f"Victoire ! Le {monstre['nom']} est terrassé.")
                nb_vagues = nb_vagues + 1
            else:
                # Tour du monstre
                print(f"\n--- Tour du {monstre['nom']} ---")
                # Il attaque quelqu'un qui a encore des PV
                cibles = []
                for h in equipe:
                    if h['pv'] > 0:
                        cibles.append(h)
                
                if len(cibles) > 0:
                    cible = random.choice(cibles)
                    degats_m = monstre['atk'] - cible['def']
                    if degats_m < 0:
                        degats_m = 0
                    cible['pv'] = cible['pv'] - degats_m
                    print(f"Le {monstre['nom']} attaque {cible['nom']} et lui inflige {degats_m} dégâts.")
                
                # Vérification si l'équipe est KO
                total_pv = 0
                for h in equipe:
                    if h['pv'] > 0:
                        total_pv = total_pv + h['pv']
                
                if total_pv <= 0:
                    print("\n--- DEFAITE ---")
                    print("Tous vos héros sont tombés au combat...")
                    equipe_en_vie = False
                    
    # Fin de partie et sauvegarde
    print(f"Score final : {nb_vagues} vagues.")
    db["scores"].insert_one({"nom": nom_joueur, "score": nb_vagues})

# MENU PRINCIPAL

def menu_principal():
    # Connexion MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["jeu_combat"]
    
    choix = ""
    while choix != "3":
        print("\n--- MENU JEU ---")
        print("1. Jouer")
        print("2. Classement")
        print("3. Quitter")
        choix = input("Votre choix : ")
        
        if choix == "1":
            pseudo = input("Votre nom de joueur : ")
            disponibles = recuperer_liste_persos(db)
            ma_team = []
            
            print("\nChoisissez 3 héros (un par un) :")
            while len(ma_team) < 3:
                compteur = 0
                while compteur < len(disponibles):
                    p = disponibles[compteur]
                    print(f"{compteur} : {p['nom']} (ATK:{p['atk']} DEF:{p['def']} PV:{p['pv']})")
                    compteur = compteur + 1
                
                try:
                    num = int(input("Numéro du héros : "))
                    if 0 <= num < len(disponibles):
                        perso = disponibles.pop(num)
                        ma_team.append(perso)
                        print(f"{perso['nom']} ajouté !")
                    else:
                        print("Mauvais numéro.")
                except:
                    print("Entre un chiffre valide !")
            
            lancer_partie(db, pseudo, ma_team)
            
        elif choix == "2":
            afficher_classement(db)
            
    print("A bientot !")

if __name__ == "__main__":
    menu_principal()