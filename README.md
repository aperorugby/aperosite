# ApéroSite

Les entrailles de l'ApéroSite de l'ApéroRugby, le club qu'il vous faut.

## Licence

L'ApéroLicence de ce site devrait être accessible dans le fichier : LICENSE.md

## Installation

L'ApéroSite est codé en Python avec l'aide du framework de développement web Django. Les autres dépendances logicielles sont déclarées dans requirements.txt

### Environnement technique requis

Pour installer une version locale de ce site, il faut:
* git
* virtualenv
* pip

### Installation locale
    
Cloner le dépôt git depuis github

    $ git clone https://github.com/aperorugby/aperosite.git

Se déplacer dans le répertoire racine des sources clonées

    $ cd aperosite

Se créer un environnement virtuel Python nommé "venv"

    $ virtualenv venv
    
Activer l'environnement virtuel

    $ source venv/bin/activate
    
Installer les dépendances du projet avec pip

    (venv)$ pip install -r requirements.txt
    
Lancer le serveur local de Django

    (venv)$ python manage.py runserver
    
Visiter le site en local
* Lancer un navigateur
* Aller à l'URL : http://127.0.0.1:8000
