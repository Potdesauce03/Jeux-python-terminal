def info_perso(nom, atk, def_val, pv):
    #crée un dictionnaire pour un perso
    #On met les stats
    perso = {
        "nom": nom,
        "atk": atk,
        "def": def_val,
        "pv": pv,
        "pv_max": pv
    }
    
    #message pour dire que c'est ok
    print("--- Creation du personnage ---")
    print("Nom du heros : " + str(perso["nom"]))
    print("Force : " + str(perso["atk"]))
    print("Armure : " + str(perso["def"]))
    print("Vie : " + str(perso["pv"]))
    print("------------------------------")
    
    return perso

def info_monstre(nom, atk, def_val, pv):
    # Pareil pour les monstres mais sans le pv_max
    # On regroupe tout dans un dictionnaire simple
    monstre = {
        "nom": nom,
        "atk": atk,
        "def": def_val,
        "pv": pv
    }
    
    # On rajoute des print
    print("--- Nouveau monstre detecte ---")
    print("Type : " + str(monstre["nom"]))
    print("Puissance : " + str(monstre["atk"]))
    print("Resistance : " + str(monstre["def"]))
    print("Sante : " + str(monstre["pv"]))
    
    return monstre

def preparer_score(joueur, score_vagues):
    # On prepare le petit pack de donnees pour MongoDB
    donnees_score = {
        "nom": joueur,
        "score": score_vagues
    }
    # On renvoie juste le dico
    return donnees_score