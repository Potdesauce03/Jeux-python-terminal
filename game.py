import random

def lancer_partie(db, nom_joueur, equipe):
    # On initialise le compteur de vagues
    vagues_survecues = 0
    equipe_est_vivante = True
    
    print(f"\n--- DEBUT POUR {nom_joueur} ---")
    
    # Boucle principale : tant que l'équipe n'est pas KO
    while equipe_est_vivante == True:
        # On récupère tous les monstres pour en choisir un au hasard
        liste_monstres = list(db["monstres"].find())
        monstre_actuel = random.choice(liste_monstres)
        
        # On extrait les stats du monstre
        m_nom = monstre_actuel['nom']
        m_atk = monstre_actuel['atk']
        m_def = monstre_actuel['def']
        m_pv = monstre_actuel['pv']
        
        print(f"\n[VAGUE {vagues_survecues + 1}]")
        print(f"Stats du monstre -> PV: {m_pv} | ATK: {m_atk} | DEF: {m_def}")
        
        # Boucle de combat contre le monstre précis
        while m_pv > 0 and equipe_est_vivante == True:
            print("\n>> TOUR DES HEROS")
            # Chaque personnage de l'équipe attaque
            for heros in equipe:
                if heros['pv'] > 0:
                    # Formule
                    degats_heros = heros['atk'] - m_def
                    if degats_heros < 0:
                        degats_heros = 0
                    
                    m_pv = m_pv - degats_heros
                    print(f"{heros['nom']} attaque et inflige {degats_heros} dégâts au {m_nom}.")
            
            # Vérification si le monstre est mort ?
            if m_pv <= 0:
                print(f"BRAVO ! Le {m_nom} a été vaincu !")
                vagues_survecues = vagues_survecues + 1
            else:
                # Si le monstre est vivant, il attaque un héros au hasard
                print(f"\n>> TOUR DU {m_nom}")
                heros_vivants = []
                for h in equipe:
                    if h['pv'] > 0:
                        heros_vivants.append(h)
                
                if len(heros_vivants) > 0:
                    cible = random.choice(heros_vivants)
                    # Formule : Dégâts = ATK monstre - DEF heros
                    degats_monstre = m_atk - cible['def']
                    if degats_monstre < 0:
                        degats_monstre = 0
                        
                    cible['pv'] = cible['pv'] - degats_monstre
                    print(f"Le {m_nom} frappe {cible['nom']} ! {degats_monstre} dégâts encaissés.")
                    
                    if cible['pv'] <= 0:
                        print(f"{cible['nom']} à été éliminé.")

                # On vérifie si toute l'équipe est morte
                pv_totaux_equipe = 0
                for h in equipe:
                    if h['pv'] > 0:
                        pv_totaux_equipe = pv_totaux_equipe + h['pv']
                
                if pv_totaux_equipe <= 0:
                    print("\nGAME OVER : Votre équipe a perdu")
                    equipe_est_vivante = False
    
    # Fin de la boucle on enregistre le score
    print(f"\nSCORE FINAL : {vagues_survecues} vagues.")
    score_final = {"nom": nom_joueur, "score": vagues_survecues}
    db["scores"].insert_one(score_final)
    print("Votre score a été sauvegardé dans le classement.")