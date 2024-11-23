
% FRÉDÉRICK LANTHIER (2087752)
% MATHIEU BERNIER (2086468)

include "globals.mzn"; 

%-----------------------------------------------------------------------------
% Données
%-----------------------------------------------------------------------------

% Nombre de villes à visiter + point de départ de la tournée
int: n;
% Distance entre chaque villes (symmétrique)
array[1..n,1..n] of int: distance;
% Distance minimale possible entre deux villes différentes
int: min_val = min([distance[i,j] | i,j in 1..n where distance[i,j] > 0]);
% Distance maximale possible entre deux villes différentes
int: max_val = max([distance[i,j] | i,j in 1..n]);

% Fenêtre de temps (1 = début, 2 = fin) durant laquelle il est possible de jouer pour chaque ville
array[1..n,1..2] of int: fenetre_arrivee;
% Temps maximum pour tout le trajet
int: max_trajet = max([fenetre_arrivee[i,2] | i in 1..n]);
% Fenêtre de temps la plus grande du trajet
int: max_fenetre = max([fenetre_arrivee[i,2] - fenetre_arrivee[i,1]| i in 2..n]);

%-----------------------------------------------------------------------------
% Variables de décisions
%-----------------------------------------------------------------------------

% Ordre des villes visitées par la tournée
array[1..n] of var 1..n: chemin_tournee;
% Circuit de la tournée, circuit_tournee[i] = j => j est le successeur de i
array[1..n] of var 1..n: circuit_tournee;
% Temps cumulé lors de l'arrivé au point i de la tournée
array[1..n] of var 0..max_trajet: cumul_temps;
% Temps d'attente avant le spectacle en ville i
array[1..n] of var 0..max_fenetre: temps_attente;
% Temps d'attente total 
var 0..max_trajet: total_temps_attentes = sum(temps_attente);

%-----------------------------------------------------------------------------
% Objectif
%-----------------------------------------------------------------------------

% Temps de trajet à minimiser
var int: temps_trajet;

%-----------------------------------------------------------------------------
% Partie étudiant
%-----------------------------------------------------------------------------

% Contrainte sur la différence entre toutes les villes
constraint alldifferent(chemin_tournee);
constraint alldifferent(circuit_tournee);

% Contrainte pour le circuit de la tournée
constraint forall(i in 1..n-1)(
              circuit_tournee[chemin_tournee[i]] = chemin_tournee[i+1]
);
constraint chemin_tournee [n] = 1;

% Contrainte sur le temps de trajet cumulé
constraint cumul_temps[1] = distance[chemin_tournee[1], chemin_tournee[2]];
constraint forall(i in 1..n-1)(
              cumul_temps[i+1] = cumul_temps[i] + distance[chemin_tournee[i], chemin_tournee[i+1]] + temps_attente[i]
);

% Contrainte sur les fenêtres de temps
constraint forall(i in 1..n)(
              cumul_temps[i] <= fenetre_arrivee[chemin_tournee[i],2] /\
              cumul_temps[i] >= fenetre_arrivee[chemin_tournee[i],1]
);

% Contraintes sur les temps d'attente
constraint temps_attente [2] = max(0, fenetre_arrivee[chemin_tournee[2],1] - distance[chemin_tournee[1], chemin_tournee[2]]);
constraint forall(i in 2..n)(
              temps_attente[chemin_tournee[i]] = max(0, fenetre_arrivee[chemin_tournee[i],1] - cumul_temps[i-1] - distance[chemin_tournee[i-1], chemin_tournee[i]])
);

% Calcul du temps total de trajet
constraint temps_trajet = cumul_temps[n];

% Résoudre pour minimiser le temps du trajet
solve :: int_search(chemin_tournee, first_fail, indomain_min, complete) minimize temps_trajet;
%solve minimize temps_trajet;
%-----------------------------------------------------------------------------
% Output
%-----------------------------------------------------------------------------

output [
  "Chemin de la tournée                   : \(chemin_tournee)\n",
  "Circuit de la tournée                  : \(circuit_tournee)\n",
  "Temps cumulés avant d'entrer en ville  : \(cumul_temps)\n",
  "Temps d'attente avant l'entrée en ville: \(temps_attente)\n",
  "Temps d'attente total                  : \(total_temps_attentes)\n",
  "Temps de trajet total                  : \(temps_trajet)\n",
];