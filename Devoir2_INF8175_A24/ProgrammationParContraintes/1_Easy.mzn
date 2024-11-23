% NOM_ETUDIANT_1 (MATRICULE_1)
% NOM_ETUDIANT_2 (MATRICULE_2)

include "globals.mzn";

%-----------------------------------------------------------------------------%
% Données
%-----------------------------------------------------------------------------%

% Nombre d'acteurs et de rôles
int: n;
% Couleurs des costumes
enum costumes; 
% Costume démandé pour un rôle i (première dimension) par un acteur j (seconde dimension)
array[1..n,1..n] of costumes: choix_costume;

%-----------------------------------------------------------------------------%
% Variables de décisions
%-----------------------------------------------------------------------------%

% Variables de décision pour assigner un acteur à un rôle
array [1..n] of var 1..n: assignation_role;

%-----------------------------------------------------------------------------%
% Partie étudiant
%-----------------------------------------------------------------------------%

<<<<<<< HEAD
% Contraintes vérifiant que tous les roles sont différents
constraint alldifferent(assignation_role);

% Contraintes vérifiant que deux acteurs voisins ne jouent pas un rôle adjacent
constraint forall(i in 1..n-1)(
              assignation_role[i] < assignation_role[i+1] - 1 \/ assignation_role[i] > assignation_role[i+1] + 1
              );
              
% Contrainte vérifiant que tous les constumes sont différents
constraint forall(i in 1..n)(not exists(j in 1..n where i != j)(
                      choix_costume[assignation_role[i], i] == choix_costume[assignation_role[j], j]
                      ));
solve satisfy;
=======


>>>>>>> d6bde5c1fce324ff3b890b2f8a8eebe99ee5c1c2
%-----------------------------------------------------------------------------%

output	
  ["L'acteur " ++ format(i) ++ 
   " prendra le rôle " ++ format(fix(assignation_role[i])) ++ 
   " (costume " ++ format(choix_costume[fix(assignation_role[i]), i]) ++ ")" ++"\n" 
  | i in 1..n];