% NOM_ETUDIANT_1 (MATRICULE_1)
% NOM_ETUDIANT_2 (MATRICULE_2)

include "globals.mzn"; 

%-----------------------------------------------------------------------------%
% Données
%-----------------------------------------------------------------------------%

% Nombre de tâches
int: n;
% Durée maximal du projet
int: m;
% Limite de ressources pouvant être partagées entre les tâches en cours
int: limite;

% Durée des tâches
array[1..n] of 1..m: duree_tache;
% Ressources requises par les tâches
array[1..n] of 1..m: ressource_tache;

%-----------------------------------------------------------------------------%
% Variables de décisions
%-----------------------------------------------------------------------------%

array[1..n] of var 1..m: debut_tache; % Début des tâches
array[1..n] of var 1..m: fin_tache; % Fin des tâches

%-----------------------------------------------------------------------------%
% Objectif
%-----------------------------------------------------------------------------%

% Fin du projet
var int: fin_projet;

%-----------------------------------------------------------------------------%
% Partie étudiant
%-----------------------------------------------------------------------------%
<<<<<<< HEAD
% Contrainte pour empecher que les tâches aient un cout supérieur à la limite d'énergie
constraint cumulative(debut_tache, duree_tache, ressource_tache, limite);

% Contrainte sur la durée des tâches
constraint forall(i in 1..n)(
              fin_tache[i] = debut_tache[i] + duree_tache[i]
              );

% Contrainte sur le nombre de tâches qui démarrent en meme temps
constraint forall(t in 0..m)(
              forall(i in 1..n)(
                at_most(2, [debut_tache[i] == t], true)
                )
              );
constraint               

fin_projet = max(fin_tache);

solve minimize fin_projet;
=======


>>>>>>> d6bde5c1fce324ff3b890b2f8a8eebe99ee5c1c2
%-----------------------------------------------------------------------------%

output [
  "Envergure du projet  : ", show(fin_projet), "\n",
  "Début des tâches     : ", show(debut_tache), "\n",
  "Fin des tâches       : ", show(fin_tache), "\n",
];