
---

# Scripts Python pour la récupération de données de matchs sportifs

Ce dépôt GitHub contient deux scripts Python qui permettent de récupérer des données de matchs sportifs à partir de différents sites web.

## 1. Script 1 - `match_scraper.py`

Ce script utilise les bibliothèques `requests`, `BeautifulSoup`, `csv`, `schedule`, et `datetime` pour récupérer les détails des matchs sportifs à partir du site web YallaKora.

### Fonctionnalités :
- Récupère les informations sur les matchs en direct pour une date donnée.
- Extrait les détails tels que les noms des équipes, les scores, les horaires, et le type de compétition.
- Stocke les données dans un fichier CSV avec un nom unique basé sur la date et l'heure.

### Utilisation :
1. Assurez-vous d'avoir les bibliothèques requises installées (`requests`, `BeautifulSoup`, `schedule`).
2. Exécutez le script `match_scraper.py`.
3. Le script va récupérer les données des matchs en direct et les stocker dans un fichier CSV.

### Exemple d'exécution :
```bash
python match_scraper.py
```

## 2. Script 2 - `goal_scraper.py`

Ce script utilise `Selenium` avec `WebDriver` pour récupérer les détails des matchs de football à partir du site web Adam Choi Team Goals.

### Fonctionnalités :
- Sélectionne le pays et récupère les données des matchs de football.
- Exporte les détails des matchs dans un fichier CSV.

### Utilisation :
1. Assurez-vous d'avoir `Selenium` installé ainsi que le pilote nécessaire (par exemple, pour Firefox).
2. Exécutez le script `goal_scraper.py`.
3. Le script va ouvrir le navigateur, sélectionner les matchs pour un pays spécifique, puis exporter les données dans un fichier CSV.

### Exemple d'exécution :
```bash
python goal_scraper.py
```

---

