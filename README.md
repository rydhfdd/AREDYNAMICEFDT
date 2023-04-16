### Introduction

Les bancs de poissons sont des phénomènes fascinants de la nature, où des milliers de poissons nagent ensemble de manière synchronisée pour échapper à leurs prédateurs. Ces comportements collectifs peuvent être étudiés et modélisés pour mieux comprendre les interactions entre les animaux et leur environnement.

Dans cette étude, nous nous intéressons aux comportements de bancs de poissons lorsqu'ils sont attaqués par un prédateur. Pour modéliser cette situation, nous avons utilisé un modèle Python basé sur la théorie de l'automate cellulaire. Ce modèle permet de simuler les mouvements individuels de chaque poisson ainsi que les interactions entre les poissons et leur prédateur.

L'objectif de cette étude est de mieux comprendre les mécanismes de défense des bancs de poissons face à un prédateur et d'analyser l'impact de différents facteurs tels que la densité du banc ou la vitesse du prédateur sur leur survie. Les résultats de cette étude pourraient avoir des implications importantes pour la conservation des espèces de poissons en danger et pour la gestion durable des ressources marines.


<img src="https://github.com/rydhfdd/AREDYNAMICEFDT/raw/main/image/poissonbanc.jpeg">



### Problématique

Comment les agents autonomes interagissent-ils et se coordonnent-ils pour manifester un comportement collectif efficace?

### L'équipe

**FOUDAD Ryadh**/
**TANG Ziyan**/
**DANET Aurelien**/
**EGUIZABAL Alexandre**


### Le modèle 

Le but de ce code est de simuler le comportement d'un banc de poissons et d'un prédateur dans un environnement 2D. Le code crée un certain nombre d'agents qui représentent les poissons et un agent qui représente le prédateur. Chaque poisson utilise un algorithme comportemental pour interagir avec ses voisins les plus proches, en évitant les collisions, en s'alignant avec les poissons de la même direction et en se rapprochant des poissons les plus proches. Le prédateur, quant à lui, suit un algorithme qui le guide à se rapprocher des poissons et à les chasser pour les manger.

La simulation est basée sur plusieurs paramètres tels que la vitesse des poissons, la distance de collision, le rayon d'alignement, le rayon d'attraction et le rayon de détection du prédateur. Ces paramètres peuvent être ajustés pour observer différents comportements et résultats de la simulation.

Le but de cette simulation est d'illustrer comment les poissons peuvent former des bancs en utilisant des règles simples et locales d'interaction avec leurs voisins. En outre, la simulation permet de visualiser comment les prédateurs peuvent chasser et se nourrir de poissons dans un environnement naturel.

<img src="https://github.com/rydhfdd/AREDYNAMICEFDT/raw/main/image/MODELE.png">

- Le prédateur est représenté en rouge 
- Les poissons en bleu
- Et en haut nous avons mis un compteur de poissons mangés




