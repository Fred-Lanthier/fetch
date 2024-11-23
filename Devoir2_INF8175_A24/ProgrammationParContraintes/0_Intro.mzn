% NOM_ETUDIANT_1 (MATRICULE_1)
% NOM_ETUDIANT_2 (MATRICULE_2)

include "globals.mzn";

%-----------------------------------------------------------------------------%
% Variables de décisions
%-----------------------------------------------------------------------------%

% Nombre devant satisfaire les critères
var 1000..9999: nombre;

% Décomposition du nombre en un ensemble de chiffres
array[1..4] of var 1..9: chiffres;

%-----------------------------------------------------------------------------%
% Objectif
%-----------------------------------------------------------------------------%

% Variable à minimiser
var int: p;

%-----------------------------------------------------------------------------%
% Partie étudiant
%-----------------------------------------------------------------------------%

<<<<<<< HEAD
constraint chiffres[4] mod 2 == 0;
constraint count(chiffres, 0, 0);
constraint alldifferent(chiffres);
constraint chiffres[1] > chiffres[2];
constraint chiffres[3] < chiffres[4];
constraint chiffres[2] > chiffres[4];
constraint sum(i in 1..4)(chiffres[i]) > 15;

solve minimize chiffres[2]*chiffres[3]*chiffres[4];

nombre = chiffres[1]*1000 + chiffres[2]*100 + chiffres[3]*10 + chiffres[4];
=======

>>>>>>> d6bde5c1fce324ff3b890b2f8a8eebe99ee5c1c2
%-----------------------------------------------------------------------------%

output [
  show(nombre)
];

