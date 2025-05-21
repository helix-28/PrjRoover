# PrjRoover
Lepage, Luc-Antoine 2379439
Parent, Félix 2377074
Allawi, Roni 2393248
Morais, Victor 2378952


Groupe 03
Équipe # 1



Projet d’intégration en Sciences Informatiques et Mathématiques
420-204-RE


Roover






Collège Bois-De-Boulogne
Présenté à : Raouf Babari
21 mai 2025 
Consignes :
 
- Preuves d'exécution du projet  (captures d'écran, vidéos)
- Difficultés rencontrées  
- échéancier (plus de précision que la V1)
- UML (plus de précision que la V1)
- Perspectives ( Suite du projet si vous avez eu le double du temps et possibilités d'améliorations)
- Conclusion
Analyse Finale de Projet – Roover
Introduction
Ce document présente l'analyse finale détaillée du projet Roover, un robot capable de cartographier et naviguer dans un environnement grâce à l'utilisation d'un LiDAR.

1. Objectifs du projet
L'objectif principal du projet est de concevoir un robot autonome capable de cartographier un environnement inconnu et de s'y déplacer efficacement, en utilisant des technologies avancées comme ROS2, un LiDAR, SLAM, et NAV2.

2. Preuves d'exécution du projet
Cette section contient les preuves d'exécution du projet, incluant captures d'écran, photos et vidéos :
description	Vidéo
Premier test avec la manette, pas de batterie	https://youtube.com/shorts/LAB_bZLdY-M?feature=share 

Rotation qui ne fonctionne pas	https://youtube.com/shorts/ZpKIysOD0Yw?feature=share 

Mouvement difficile sans la rotation	https://youtube.com/shorts/6yK7ZddguFo?feature=share 

Rotation qui ne fonctionne pas	https://youtube.com/shorts/fmsqDtLCloo?feature=share 

Rotation qui fonctionne	https://youtube.com/shorts/iYt5px_BsIg?feature=share 


3. Difficultés rencontrées
Les principales difficultés rencontrées tout au long du projet sont les suivantes :

1)	Précision du mouvement
Des contraintes physiques ont mené à des problèmes de précision des mouvements. Voici les deux principales difficultés de ce type : 
- Erreurs liées aux déplacements du robot dues à un glissement des roues.
- Distribution du poids qui nuit à la précision du mouvement
-moteurs qui ne mesurent pas leur vitesse
	La batterie et le Raspberry pi sont beaucoup plus lourds que le reste des composantes sur le robot, donc mettre les deux dans la même zone sur le robot menait à des problèmes de précision de mouvement. Les roues d’avant avaient plus de traction et donc elles affectaient le mouvement plus que voulu. Pour résoudre ce problème, nous avons positionné ces deux composantes à des extrémités opposées du robot. De plus, les moteurs étant peu puissants pour la précision que nous avons besoin, nous avons adapté le robot pour que tout déplacement minime du joystick est annulé puisque les moteurs ne sont pas assez puissants pour faire que le Roover se déplace lorsque leur puissance transmise est inférieure à 25%. 
Puisque nous n’utilisions pas des moteurs intelligents qui communiquent leur vitesse à d’autres composantes, nous n’avions pas accès à des valeurs exactes de déplacement pour le robot. Nous avons donc dû faire un odomètre simulé pour pouvoir estimer les mouvements du robot, ce qui est nécessaire pour la cartographie.

2)	Communication entre les systèmes
-  Défis liés à la communication ROS2 entre les nœuds (moteurs, capteurs, navigation).
- Récupération et envoi de donnée (Manette à Pi) 
	La communication entre les différentes parties de ROS2 est une difficulté que nous avons rencontrée. Apprendre comment cela fonctionne a pris beaucoup de temps et c’est une manière de coder qui nous était nouvelle.

3)	Construction du robot
En travaillant sur un projet qui n’est pas totalement logiciel, nous avons eu plusieurs difficultés physiques dans la construction du robot. Les voici : 
- Branchements des fils électriques
- Construction du robot 
- Fixer les appareils sur le robot en s’assurant qu’ils ne cachent pas la vue du lidar :(Raspberry Pi, lidar, plaque électrique, distributeurs de courant, fils)
- Gestion des fils électriques
Premièrement, trouver les bons branchements à faire pour que les différentes pièces marchent bien ensemble fut difficile. Par exemple, nous avons eu de la difficulté à trouver un remplacement pour un port que nous avions besoin qui était déjà utilisé. De plus, nous avons dû faire une plaquette personnalisée à l’imprimante 3D pour pouvoir bien placer les pièces sur le robot et qu’aucune pièce ou aucun fil ne bloque la vue du Lidar. Finalement, la gestion générale des fils électriques pour obtenir un projet relativement propre fut difficile.

4) Autres difficultés
- Connection Wifi dans la classe rend la communication difficile car le wifi de l’école n’atteint pas et à chaque fois qu’on veut configurer le wifi sur le rasberryPi, il faut le connecter sur un moniteur puis chercher son adresse IP.  
- Défaut de fabrication d’un des moteurs, les polarités sont inversées, le code a donc été adapté pour inverser les actions que le robot doit réellement faire
- Librairies incompatibles : Certaines librairies, comme celle initialement choisie pour recevoir les données de la manette, ne sont pas compatibles avec le Raspberry Pi. Nous avons donc dû changer de librairie pour pouvoir continuer le projet.
- Les librairies installés comme GPIO et PI rendent le test impossible à faire sur le PC. Il faut brancher le tout au robot et faire le test ce qui prenait environ 30 minutes d’installation pour faire un seul test. Si le code ne fonctionnait pas, il fallait le changer sur l’ordi puis le push sur discord et le pull sur le raspberry Pi et remettre le Pi sur le robot. 
- Équipement pas assez performant
La batterie portative utilisée au début pour alimenter le Raspberry Pi et le Lidar était trop grosse/lourde. Elle débalançait trop le Roover et les déplacements n’étaient pas précis. Nous avons utilisé une autre batterie, plus petite, mais elle ne fournissait pas assez de courant, ce qui nuisait aux performances de l’équipement. Nous avons donc dû passer d’une batterie de 5V 2A à une nouvelle batterie portative de 5V 3A pour répondre aux demandes énergétiques du projet.


4. Échéancier détaillé
L'échéancier ci-dessous détaille précisément les phases du projet :

Semaine	Tâches prévues	Tâches réalisées

1	  Planification initiale et choix technologiques  	Complété

2  	Commande et réception du matériel	  Complété

3	  Montage initial du robot	  Complété

4   Assemblage détaillé du robot et tests préliminaires	  Complété

5  	Tests moteurs et intégration des capteurs initiaux	  Complété avec ajustements

6	  Installation et configuration de ROS2	  Complété

7	  Premiers essais de communication ROS2  	Complété

8	  Intégration et calibration du LiDAR  	Complété avec difficultés

9	  Développement initial SLAM Toolbox	  Complété 

10	 Optimisation SLAM Toolbox et tests avancés	  complété

11	  Développement initial NAV2 (navigation autonome)	  incomplet

12	  Finalisation NAV2 et optimisation navigation	  Incomplet

13	  Développement interface Web HTML (localhost)	  Complété

14  	Optimisation interface Web et tests finaux	  Partiellement complété


 
5. Diagrammes UML
![Diagramme classes](PrjRoover/Diagramme%20classes.png)

 
6. Perspectives d'amélioration
Avec davantage de temps et de ressources, plusieurs améliorations seraient envisageables :

- Développement d'une application mobile pour contrôler le robot à distance.
À la place d’utiliser une manette et un ordinateur, une application mobile serait une manière plus simple d’utiliser ce projet.

- La navigation autonome
La navigation autonome était un des objectifs de ce projet, mais nous n’avons pas eu le temps de le faire fonctionner, donc si nous avions plus de temps, nous pourrions perfectionner cette portion du projet.

- Améliorer l’interface graphique 
L’interface graphique pourrait être rendue plus complète et avancée. Par exemple, on pourrait rendre le site plus beau visuellement. On pourrait aussi améliorer la carte qui est présentée sur le site.

- Intégration de l’algorithme AMCL pour se repérer dans l’espace
L’intégration de cet algorithme est un autre objectif que nous avions avant de commencer, mais que nous n’avons pas eu le temps de compléter. Avec plus de temps, nous pourrions perfectionner cette fonctionnalité et améliorer notre projet.

- Amélioration de l’apparence du robot
Il serait possible de remplacer une grande partie du ruban adhésif utilisé sur le robot par des vis pour rendre l’organisation des pièces plus propre et organisée. De plus, la gestion des fils pourrait être meilleure pour qu’il y ait moins de doute sur quel fil se rend à quel endroit et cela rendrait aussi au robot une apparence plus propre. 
 
7. Collaboration d'équipe
La collaboration au sein de l'équipe a été efficace, avec une répartition claire des rôles :

- Roni Allawi : Gestion des tests et optimisation matérielle ainsi que le développement de l'interface utilisateur et web. Début des mouvements simples.
- Félix Parent : Gestion des tests, optimisation matérielle, gestion fils électriques, gestions des mouvements simples.
- Luc-Antoine Lepage : Développement de l'interface utilisateur et web et lien entre manette-moteurs-interface graphique, mouvements
- Victor Morais : intégration ROS2 et gestion des algorithmes SLAM et Lidar. 

Conclusion
Le projet Roover fut une opportunité enrichissante qui a permis de concrétiser des connaissances théoriques en une application pratique complète. Malgré les défis rencontrés, les résultats obtenus sont satisfaisants et démontrent la viabilité de la solution pour des applications réelles. Ce projet a permis à chacun des membres de l'équipe de renforcer ses compétences en gestion de projet, programmation, et intégration de systèmes complexes. Malgré le fait que nous n’avons pas atteint tous les objectifs initiaux, le résulat final est quand-même satisfaisant et il reste plusieurs perspectives d’amélioration réalistes. 

