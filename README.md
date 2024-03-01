

### Automatisation du Scraping des Détails des Matchs de Football

Ce script Python, `scraping_schedule.py`, est conçu pour automatiser le processus de récupération des détails des matchs de football à partir d'un site web et les enregistrer dans un fichier CSV. Voici un aperçu de ce que fait chaque partie du script :

1. **Récupération des Données des Matchs :**
   - Le script utilise la bibliothèque `requests` pour envoyer une requête HTTP à une page web spécifique qui répertorie les matchs de football.
   - Ensuite, il utilise `BeautifulSoup` pour extraire les détails de chaque match, tels que les noms des équipes, les scores et l'heure des matchs.

2. **Création du Fichier CSV :**
   - Une fois les détails des matchs récupérés, le script crée un fichier CSV pour stocker ces données.
   - Chaque ligne du fichier CSV représente un match, avec des colonnes pour le type de compétition, les noms des équipes, les scores et l'heure du match.

3. **Planification de l'Exécution :**
   - Le script utilise la bibliothèque `schedule` pour planifier l'exécution du scraping à des intervalles spécifiques.
   - Par exemple, dans ce script, la fonction principale `main()` est exécutée une fois au début, puis chaque jour à 23h00 pour récupérer les détails des matchs de la journée.

4. **Gestion des Erreurs :**
   - Pour assurer une exécution fluide, le script est enveloppé dans un bloc `try-except` qui capture et gère les erreurs qui pourraient survenir lors du scraping des données.

5. **Affichage de Messages :**
   - Pendant l'exécution, le script affiche des messages à la console pour indiquer le bon déroulement du processus ou pour signaler toute erreur rencontrée.

En résumé, ce script permet de récupérer automatiquement les détails des matchs de football à partir d'un site web, de les enregistrer dans un fichier CSV et de planifier cette tâche pour s'exécuter quotidiennement à 23h00. Cela offre une solution pratique pour suivre les résultats des matchs de football de manière automatisée et régulière.
