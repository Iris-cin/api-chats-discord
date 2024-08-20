# API Flask d'Images de Chats Aléatoires

Ceci est une API simple construite avec Flask qui génère et sert des images de chats aléatoires. L'API inclut un endpoint pour générer une clé API, qui est nécessaire pour accéder à l'endpoint fournissant l'image de chat aléatoire.

## Fonctionnalités

- **/generate-key** : Génère une clé API unique pour accéder aux autres endpoints.
- **/random-cat** : Retourne une image de chat aléatoire si une clé API valide est fournie.

## Prérequis

- Python 3.x
- Pip (gestionnaire de paquets Python)
- Un compte [Heroku](https://www.heroku.com/) (si vous souhaitez déployer l'application)

## Installation Locale

1. Clonez ce dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/votre-utilisateur/nom-du-repo.git
   cd nom-du-repo
    ```

2. Créez un environnement virtuel et activez-le :
3. Installez les dépendances :
```py
pip install -r requirements.txt
```
4. Démarrez l'application localement :
```py
   python app.py
```
6. Accédez à l'application à l'adresse **http://127.0.0.1:5000/** dans votre navigateur.

 ## Tester Localement avec `test.py`

Le script `test.py` est conçu pour tester l'API localement depuis le terminal. Avant d'exécuter ce script, assurez-vous que l'application Flask est en cours d'exécution. Vous devez démarrer l'application Flask avec `app.py` en utilisant la commande suivante :

```bash
python app.py
```
Une fois que l'application Flask est démarrée et fonctionne, vous pouvez tester l'API en exécutant le script **test.py**. Ce script enverra des requêtes à l'API pour vérifier que les endpoints fonctionnent correctement. Exécutez le script avec la commande suivante :

```py
python test.py
```
