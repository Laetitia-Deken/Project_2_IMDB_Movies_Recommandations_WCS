# Projet 2 : Système de recommandation de films

## Objectif :
Vous êtes un Data Analyst freelance. Un cinéma en perte de vitesse situé dans la Creuse vous contacte. Il a décidé de passer le cap du digital en créant un site Internet taillé pour les locaux. 

Pour aller encore plus loin, il vous demande de créer un moteur de recommandation de films qui à terme, enverra des notifications aux clients via Internet.

Pour l’instant, aucun client n’a renseigné ses préférences, vous êtes dans une situation de cold start. Mais heureusement, le client vous donne une base de données de films basée sur la plateforme IMDb.

 
<p align="center"> <img src="https://github.com/Laetitia-Deken/Project_2_Recommandation_de_films/blob/main/IMDB_Logo_2016.svg.png" alt="IMDB's logo"/> </p>


Vous allez commencer par proposer une analyse complète de la base de données (Quels sont les acteurs les plus présents ? À quelle période ? La durée moyenne des films s’allonge ou se raccourcit avec les années ? Les acteurs de série sont-ils les mêmes qu’au cinéma ? Les acteurs ont en moyenne quel âge ? Quels sont les films les mieux notés ? Partagent-ils des caractéristiques communes ? etc…) Suite à une première analyse, vous pouvez décider de spécialiser votre cinéma, par exemple sur la « période années 90 », ou alors sur « les films d’action et d’aventure », afin d'affiner votre exploration.

Après cette étape analytique, sur la fin du projet, vous utiliserez des algorithmes de machine learning pour recommander des films en fonction de films qui ont été appréciés par le spectateur.

## Missions :
Faire une présentation pour présenter votre travail, expliquer votre démarche, les outils utilisés, les difficultés rencontrées, et des pistes d’amélioration.
Présenter les indicateurs statistiques et KPI pertinents sur les films.
Créer un système de recommandation de film en utilisant des algorithmes de machine learning et faire une démonstration de ces recommandations sur des films proposés en séance par le client.

## Rendu final :
Le client aurait souhaité intégrer votre analyse et vos recommandations à son site pour pouvoir le tester, mais le timing est trop serré. Force de proposition, vous lui proposer de le rendre testable au moyen d’un outil de votre choix. 
Le client a 2 besoins, qui peuvent être dans 2 outils séparés :
- Obtenir quelques statistiques sur les films (type, durée), acteurs (nombre de films, type de films) et d’autres. Vous le ferez notamment à l’aide de visualisations. Vous pouvez utiliser un outil de business intelligence, ou des graphiques via Python. 
- Retourner une liste de films recommandés en fonction d'IDs ou de noms de films choisis par un utilisateur. Vous pouvez intégrer ces recommandations à un outil de dashboarding, ou bien faire ces recommandations directement depuis la ligne de commande (“input”).

L’objectif n’est pas d’arriver à un travail parfait, mais que le système fonctionne et que vous arriviez à déceler les points à améliorer.
