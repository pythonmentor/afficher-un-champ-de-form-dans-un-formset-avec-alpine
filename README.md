# Example utilisant Alpine.js pour afficher cacher un champ de formulaire dans un formset

Ce projet utilise l'outil pipenv pour gérer ses dépendances back-end. S'il n'est pas
déjà installé sur votre ordinateur, vous pouvez l'installer à l'aide de la commande
`pip install pipenv`.

Une fois pipenv installé, il vous suffit de suivre les instructions suivantes:
- Si vous avez décidé d'utiliser Postgresql, lancer la base de donnée à l'aide de `docker-compose up -d`
- Exécuter les migrations avec `pipenv run python manage.py migrate`
- Lancer le server de dev avec `pipenv run python manage.py runserver` et se rendre sur la [page d'accueil](http://localhost:8000).