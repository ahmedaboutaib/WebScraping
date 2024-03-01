import requests
from bs4 import BeautifulSoup
import csv
import schedule
import time
from datetime import datetime

def main():
    try:
        # Récupère la page web
        page = requests.get("https://mobile.yallakora.com/match-center/?date=11/23/2022#matchesclipPrev")
        
        # Extrait le contenu HTML de la page
        src = page.content 
        
        # Initialise BeautifulSoup pour analyser le HTML
        soup = BeautifulSoup(src, "lxml")
        
        # Liste pour stocker les détails des matchs
        match_details = []
        
        # Trouve toutes les sections correspondant à chaque carte de match
        championships = soup.find_all("div", {"class": "matchCard"})
        
        # Fonction pour extraire les informations de chaque match
        def get_match_info(championships):
            # Récupère le titre de la compétition
            championship_title = championships.contents[1].find('h2').text.strip()
            
            # Récupère tous les éléments correspondant à chaque match dans la compétition
            all_matches = championships.find_all("div", {"class": "item"})
            number_of_match = len(all_matches)
            
            # Pour chaque match, extrait les détails
            for i in range(number_of_match):
                # Récupère les noms des équipes
                team = all_matches[i].find_all("p")
                teamA = team[0].text.strip()
                teamB = team[1].text.strip()
                
                # Récupère le score du match
                match_result = all_matches[i].find("div" , {"class": "MResult"}).find_all("span", {"class": "score"})
                score = f"{match_result[1].text.strip()} - {match_result[0].text.strip()}"
                
                # Récupère l'heure du match
                time =  all_matches[i].find("div" , {"class": "MResult"}).find('span', {"class": "time"}).text.strip()
                
                # Ajoute les détails du match à la liste
                match_details.append({"نوع البطولة": championship_title, "الفريق الأول": teamA, "الفريق الثاني": teamB, "نتيجة": score, "وقت": time})
        
        # Pour chaque section de match, appelle la fonction pour extraire les détails
        for i in range(len(championships)):
            get_match_info(championships[i])
        
        # Nom du fichier avec date et heure actuelle pour garantir l'unicité
        filename = f"match_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
        
        # Obtient les clés des dictionnaires pour les en-têtes CSV
        keys = match_details[0].keys()
        
        # Ouvre un fichier CSV en mode écriture avec UTF-8 encoding
        with open(filename, 'w', encoding='utf-8', newline='') as output_file:
            # Crée un écrivain de dictionnaire CSV
            dict_writer = csv.DictWriter(output_file, keys)
            
            # Écrit les en-têtes dans le fichier CSV
            dict_writer.writeheader()
            
            # Écrit les lignes de données dans le fichier CSV
            dict_writer.writerows(match_details)
            
            # Affiche un message de confirmation
            print(f"File created successfully: {filename}")
    except Exception as e:
        # En cas d'erreur, affiche un message d'erreur
        print(f"An error occurred: {str(e)}")

def job():
    # Fonction pour exécuter la tâche principale
    print("Running job...")
    main()

# Planifie l'exécution de la tâche toutes les 10 minutes
schedule.every(2).minutes.do(job)

# Exécute la tâche une fois au début
job()

# Boucle pour permettre l'automatisation en continu
while True:
    schedule.run_pending()
    time.sleep(1)
