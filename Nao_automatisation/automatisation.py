# -*- coding: utf-8 -*-
import os
import re
import time
from docx import Document


class NaoScriptGenerator:
    def __init__(self, nom_fichier):
        self.nom_fichier = nom_fichier
        self.nao_talker = "Nao :"

    def lire_fichier_word(self):
        """Lit un fichier Word et retourne son contenu sous forme de texte."""
        contenu = ""
        try:
            doc = Document(self.nom_fichier)
            contenu = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        except Exception as e:
            print("Erreur lors de la lecture du fichier Word :", e)
        return contenu


    def lire_fichier_python(self, file_path):  # Add 'self' here
        """Lit un fichier Python et retourne son contenu sous forme de texte."""
        try:
            with open(file_path, 'r') as f:
                return f.read()
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier {file_path}: {e}")
            return ""

    def recuperer_phrases_nao(self, contenu):
        """Extrait les phrases de NAO et des autres interlocuteurs du texte."""
        phrases_nao, index_nao = [], []
        phrases_others, index_others = [], []

        lignes = contenu.split('\n')
        for i, ligne in enumerate(lignes):
            if ligne.strip().startswith(self.nao_talker):
                phrases_nao.append(ligne.strip())
                index_nao.append(i)
            else:
                phrases_others.append(ligne.strip())
                index_others.append(i)

        return phrases_nao, index_nao, phrases_others, index_others

    def discussion_to_sleep(self, discussion):
        """Calcule le temps de pause en fonction de la longueur de la phrase."""
        return [max(len(phrase) / 14, 1.5) for phrase in discussion]

    def generer_script_nao(self):
        """Génère le script Python pour NAO à partir du fichier Word."""
        contenu = self.lire_fichier_word()
        discussion_nao, index_nao, discussion_other, index_other = self.recuperer_phrases_nao(contenu)

        sleep_times = self.discussion_to_sleep(discussion_other)

        python_output = ""
        j, k = 0, 0
        lignes = contenu.split('\n')

        for i in range(len(lignes)):
            if j < len(index_nao) and i == index_nao[j]:
                sous_phrases = re.split(r'[:.!?]', discussion_nao[j])
                sous_phrases = [phrase.strip() for phrase in sous_phrases if phrase.strip()]
                python_output += '\n'.join([f'tts.say("{phrase}") \n time.sleep(0.5)' for phrase in sous_phrases[1:]]) + '\n'
                j += 1

            if k < len(index_other) and i == index_other[k]:
                python_output += f'\ntime.sleep({sleep_times[k]})\n'
                k += 1

        return python_output

    def sauvegarder_script(self):
        """Crée et enregistre le script généré pour NAO."""
        encodage = "# -*- coding: utf-8 -*- \n"
        introduction = self.lire_fichier_python("/home/gabriel/Documents/nao/nao_software_v4/Nao_automatisation/introduction_nao.py")
        script_nao = encodage + introduction + self.generer_script_nao() 

        fichier_nom = os.path.basename(self.nom_fichier)[:-5]  
        dossier_parent = os.path.dirname(os.getcwd())
        fichier_output = os.path.join(dossier_parent, "Nao_tasks/themes", f"{fichier_nom}.py")

        with open(fichier_output, 'w') as file:
            file.write(script_nao)

        return fichier_output


def text_to_nao(nom_fichier):
    generator = NaoScriptGenerator(nom_fichier)
    return generator.sauvegarder_script()
