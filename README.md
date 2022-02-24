# Preventi
PREVENTI un système d’analyse d’image couplé avec une alarme périmétrique  dans le but de prévenir de la baignade dangereuse d’un jeune enfant.

Chaque année il y a plus de 372.000 noyés par an, les noyades infantiles représentent le plus fort taux d’après l’OMS.

Enjeu : 
Question de société - amélioration de la qualité de vie - amélioration de la sécurité

Deux types d’alarmes :

alarmes Immergées : Elles sont positionnées à l’intérieur de la piscine et prévienne toute chute dans la piscine.


Inconvénients :
- sur une grande surface de bassin il faut combiner plusieurs alarmes.
- Elle prévient seulement après la chute dans la piscine ce qui laisse un risque de noyade possible




Alarmes périmétriques : Positionné à l’extérieur de la piscine dans un périmètre précis et préviens de toute entrée dans celui-ci.



Inconvénients :
- beaucoup de faux positifs et négatifs possibles
- Imposant et pas forcément esthétique 

Type d’alarme choisi pour le projet . Alarme périmétrique, car le cahier des charges nous impose une alarme préventive donc l'alarme immergée n’a pas sa place.

Mise en place → Combiner un système d’alarme périmétrique avec une détection de mouvement pour éviter le plus possible de faux négatifs.


Différentes solutions pour l’analyse d’image :
- Opencv
- ESP32

L’ESP32 est utilisé avec des capteurs PIR en supplément ce qui rajoute une complication. De plus il ne permet pas une grande portée.

Détection de mouvement :
- PIR
- Caméra avec détection de mouvement intégré
- Open Cv

Choix → Ce qui nous importe le plus dans le projet est la fiabilité pour une question de sécurité, nous allons donc utiliser le module opencv et une caméra.
