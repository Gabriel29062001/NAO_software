def text_to_nao(nom_fichier, nursery_choices):

    # -*- coding: utf-8 -*-

    import os
    import re
    import time
    from docx import Document


    def lire_fichier_word(chemin_fichier):
        contenu = ""
        try:
            # Ouvrir le fichier Word
            doc = Document(chemin_fichier)
            
            # Parcourir les paragraphes et ajouter leur contenu à la variable
            for paragraph in doc.paragraphs:
                contenu += paragraph.text + "\n"
        except Exception as e:
            print("Erreur lors de la lecture du fichier Word :", e)
        
        return contenu
    
    def lire_fichier_python(file_name):
        print(file_name)
        with open(file_name, 'r') as f:
            # Lire le contenu du fichier
            contenu = f.read()
        return contenu


    contenu = lire_fichier_word(nom_fichier)
    lignes = contenu.split('\n')
    #print(contenu)

    def recuperer_phrases_nao(contenu, talker):

        phrases_nao = []
        index_nao = []
        phrases_others = []
        index_others = []

        lignes = contenu.split('\n')
        for i, ligne in enumerate(lignes):
            if ligne.strip().startswith(talker):
                phrases_nao.append(ligne.strip())
                index_nao.append(i)  # Utilisation de la fonction append pour ajouter l'index de la ligne
            else :
                phrases_others.append(ligne.strip())
                index_others.append(i)  # Utilisation de la fonction append pour ajouter l'index de la ligne

        return phrases_nao, index_nao, phrases_others, index_others


    def discussion_to_sleep(discussion):
        sleep_time = []
        

        for i in range(len(discussion)):
            sleep_time.append(max((len(discussion[i]))/14,1.5))

        
        return sleep_time

    nao_talker = "Nao:"

    discussion_nao, index_nao, discussion_other, index_other = recuperer_phrases_nao(contenu,nao_talker)



    sleep_time = discussion_to_sleep(discussion_other)
   

    j= 0
    k = 0
    python_ouput = ""


    for i in range(len(lignes)):
        #print(i,index_nao[j], index_other[k])

        print(i,j)
        if i == index_nao[j] :
            
            sous_phrases = re.split(r'[:.!?]', discussion_nao[j])
            sous_phrases = [discussion.strip() for discussion in sous_phrases if discussion.strip()]
            
            python_ouput += '\n'
            for l in range(len(sous_phrases)-1):
                python_ouput += 'tts.say("' + sous_phrases[l+1] + '") \n' + 'time.sleep(0.5) \n'
            if j == len(discussion_nao)-1:
                j = j
            else: 
                j = j+ 1

        if i == index_other[k]:
        
            python_ouput += '\ntime.sleep(' + str(sleep_time[k])+ ')\n'
            k = k + 1


    creches = ["La_Nanosphère","Les_Petits_Acrobates", "Les_6_sens", "Le_Microcosme", "HOME"]
    ROBOTS_IP = ['192.168.90.236', "192.168.55.60","11.10.10.10", "12.10.10.10", "10.101.0.183"]
    ROBOT_IP = ROBOTS_IP[nursery_choices]

    encodage = "# -*- coding: utf-8 -*- \n"
    current_directory = os.getcwd()
    print("Current directory:", current_directory)
    introduction = lire_fichier_python("/home/gabriel/Documents/nao/nao_softwarev3/Nao_automatisation/introduction_nao.py") + "\n"
    conclusion = lire_fichier_python("/home/gabriel/Documents/nao/nao_softwarev3/Nao_automatisation/conclusion_nao.py") + "\n"




    fichier_automatise = encodage +introduction+ python_ouput + conclusion
   

    fichier = os.path.basename(nom_fichier)
    nom_themes =fichier[:-5]

    dossier_actuel = os.getcwd()
    dossier_parent = os.path.dirname(dossier_actuel)

    fichier_output = dossier_parent + "/nao_softwarev3/Nao_tasks/themes"  +   "/" + nom_themes + ".py"
    #print(fichier_output)

    with open(fichier_output, 'w') as file:
        # Write the entire file content
        file.write(fichier_automatise)

    return fichier_output

    