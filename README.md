# roboc-lan

############################################################
            README : ROBOC
############################################################

I. LE JEU

1. Principe du jeu
L'objectif de ce développement est de créer un petit jeu en réseau.

Le jeu ne peut démarrer que si une instance sur un serveur est lancé.
Quand on lance cette instance il faut tout d'abord choisir le labyrinthe à afficher
Les labyrinthes que l'on peut lancer sont piochés dans un dossier spécifique ou tous
les labyrinthes sont présent au format txt. 

Une fois le serveur lancé le programme attend les connexions des joeurs

Les joueurs doivent lancer un programme pour se connecter au serveur
dès qu'un utilisateur indique que tous les joueurs sont connectés le jeu se lance.

Côté serveur 
Au lancement tous les utilisateurs reçoivent un état du labyrinthe. à la réception de cet état du labyrinthe
le premier jouer envoie sont instructions, tous les joueurs reçoivent le nouvel état et c'est au joueur suivant de jouer.

2. Design

Le jeu se joue uniquement avec du texte dans une console voici la codification :

O : C'est un mur, il doit bloquer la progression du joueur
X : Le joueur actuellement en train de jouer
x : Le joueur qui ne joue pas
. : C'est une porte le joueur peut la traverser en marchant
U : C'est la sortie l'objectif est de l'atteindre

Le labyrinthe sera toujours de forme rectangulaire sous format texte. Pas de limitation en terme de taille de labyrinthe

3. Les actions possibles

Le joueur peut réaliser plusieurs actions, il peut se déplacer dans les 4 directions. Il peut créer un mur ou percer un mur.
Il ne peut pas percer les murs d'enceinte du labyrinthe

II. Fonctionnement détaillé des mécaniques

1. la création du labyrinthe

Le labyrinthe est à la base un fichier txt avec sa représentation tel que le joueur le verra. La seule différence est qu'il n'y a pas de joueur positionnés sur le fichier source.
Les joueurs seront positionnés aléatoirement. 

Pour que le joueur puisse se déplacer dans le labyrinthe nous devons affecter des coordonés à chaque objet de ce labyrinthe. Pour cela il faut donc décomposer le labyrinthe en plusieurs objet. 

Nous avons donc deux types d'objet : Le labyrinthe dans sa globalité qui permet à l'utilisateur d'intéragir sur celui ci et l'objet case qui est contenu dans le labyrinthe.

Pour créer ce labyrinthe un objet à part entière sera créé dont l'objectif sera de créer un labyrinthe et ses cases à partir du fichier txt.

On peut tracer le fonctionnement suivant.

CARTE
Attribut
Méthode
Initialiser des cases
Initialiser un labyrinthe pour y renseigner ses cases

Labyrinthe
Attribut
Liste des cases dans un dictionnaires avec comme clé la position de la case
Liste des positions des joueurs
Longueur du labyrinthe
Méthode
repr : Le labyrinthe doit pouvoir reconstituer toutes cas 

Case 


Fonctionnement, on a donc une classe carte qui génère une instance labyrinthe qui génère des instances case
La question est comment est-ce que je nomme correctement ces éléments ?
