def info_perso(nom, atk, def_val, pv):
    # Crée un dictionnaire pour un perso
    #On met les stats
    perso = {
        "nom": nom,
        "atk": atk,
        "def": def_val,
        "pv": pv,
        "pv_max": pv
    }
    
    # Message pour verifier
    print("--- Creation du personnage ---")
    print("Nom du heros : " + str(perso["nom"]))
    print("Force : " + str(perso["atk"]))
    print("Armure : " + str(perso["def"]))
    print("Vie : " + str(perso["pv"]))
    print("------------------------------")
    
    return perso

def info_monstre(nom, atk, def_val, pv):
    # Pareil pour les monstres
    monstre = {
        "nom": nom,
        "atk": atk,
        "def": def_val,
        "pv": pv
    }
    

    print("--- Nouveau monstre ---")
    print("Type : " + str(monstre["nom"]))
    print("Puissance : " + str(monstre["atk"]))
    print("Resistance : " + str(monstre["def"]))
    print("Sante : " + str(monstre["pv"]))
    
    return monstre

def preparer_score(joueur, score_vagues):
    # On prepare les donnees pour MongoDB
    donnees_score = {
        "nom": joueur,
        "score": score_vagues
    }
    # On renvoie juste le dico
    return donnees_score