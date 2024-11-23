from schedule import Schedule
<<<<<<< HEAD

def solve(schedule: Schedule):
    """
    Your solution of the problem
    :param schedule: object describing the input
    :return: a list of tuples of the form (c,t) where c is a course and t a time slot. 
    """
    
    # Add here your agent
    theta = 2000
    solution = Local_Search(schedule, theta)
    return solution

def Local_Search(schedule: Schedule, theta):
    """
    Recherche la meilleure solution possible pour un horaire donné
    """
    solution = Generate_Initial_Solution(schedule)
    solutionStar = solution
    add = 1
    for k in range(theta):
        G = Voisinage(schedule, solution, add)
        V = Voisins_Valides(G, schedule, solution)
        s = Selection_Voisin(V, schedule)
        if len(s) == 0:
            add += 1
            continue
        else:
            add = 1
            solution = s
        if Nombre_conflits(schedule, solution) < Nombre_conflits(schedule, solutionStar):
            solutionStar = solution
    return solutionStar

def Generate_Initial_Solution(schedule: Schedule):
    """
    La solution initiale est que tous les cours ont le même créneau horaire
    """
    solution = dict()
    timeSlotId = 1
    for cours in schedule.course_list:
        solution[cours] = timeSlotId
    return solution

def Voisinage(schedule: Schedule, solution, add):
    """
    Retourne les voisins de l'état State sous forme de liste ou chaque élément est un dictionnaire
    avec comme clé les cours et comme valeur les créneaux horaires associés

    Principe : Modifier le créneau des cours en conflit avec un cours
    """
    voisins = list()
    for cours in schedule.course_list:
        voisin = solution.copy()
        set_conflits_init = schedule.get_node_conflicts(cours)
        nbr_conflits = 0
        for conflit in set_conflits_init:
            if voisin[cours] == voisin[conflit]:
                nbr_conflits += 1
        voisins.append((nbr_conflits, cours))

    max_conflits, cours_max_conflits = max(voisins)
    new_solution = solution.copy()
    new_solution[cours_max_conflits] += add
    return new_solution

def Voisins_Valides(G, schedule: Schedule, solution):
    """
    Retourne les voisins valide de l'état State selon tous les voisins G
    Sous forme de liste
    Un voisin valide est considéré comme un voisin qui diminue les conflits de la solution
    """
    ImprovedSol = list()
    nbr_conflits_solution = Nombre_conflits(schedule, solution)
    new_nbr_conflits = Nombre_conflits(schedule, G)
    if new_nbr_conflits <= nbr_conflits_solution:
        ImprovedSol.append(G)
    
    return ImprovedSol

def Selection_Voisin(V, schedule: Schedule):
    """
    Sélectionne un voisin possible de state parmis les états valides V
    Le meilleur voisin est celui qui a le moins de conflits
    """
    if len(V) == 0:
        return {}
    
    return V[0]

def Nombre_conflits(schedule: Schedule, solution):
    """
    Évalue l'état State 
    Retourne le nombre de conflits de la solution
    """
    somme = 0
    for conflit in schedule.conflict_list:
        if solution[conflit[0]] == solution[conflit[1]]:
            somme += 1
    
    return somme
=======
import random
import math

def solve(schedule:Schedule):
    """
    Algorithme de Simulated Annealing pour trouver la solution optimale.
    :param schedule: object describing the input.
    :return: a dictionnary where the keys are the list of the courses and the values are the time periods associated.
    """

    # Paramètres d'entrés pour l'algorithme de Simulated Annealing
    max_iterations = 30000  # Critère d'arrêt (Nombre d'itérations maximal)
    initial_temperature = 1000  # Température initiale
    min_temperature = 1e-4  # Critère d'arrêt sur la température (Température minimale)
    initial_cooling_rate = 0.99  # Taux de décroissance initial de la température

    courses = list(schedule.conflict_graph.nodes)  # Liste de tous les cours
    n_courses = len(courses)  # Nombre de cours
    max_slots = n_courses // 2  # Initialisation d'un nombre maximal de crénaux horaire égal à la moitié du nombre total de cours
    

    # Étape 1: Initialisation d'une solution initiale
    solution = greedy_initialization(schedule, max_slots) #Solution initale
    current_conflicts = evaluate_solution(solution, schedule)  # Nombre de conflits initial

    # Ajustement de la solution par une meilleure solution 
    solutionStar = solution.copy()
    conflictsStar, slotsStar = current_conflicts, count_unique_slots(solution)

    temperature = initial_temperature  # Initialisation de la température initiale comme première température

    # Boucle de l'algorithme de Simulated Annealing
    for k in range(max_iterations):
        # Étape 2 : Génération d'une solution du voisinage en échangeant 2 cours au hasard et en modifiant le crénaux horaire d'un cours au hasard
       
        new_solution = random_swap(solution.copy(), courses, max_slots) #Création de la nouvelle solution
        new_conflicts = evaluate_solution(new_solution, schedule)  # Évalutation de la nouvelle solution
        new_slots = count_unique_slots(new_solution)  # Nombre de crénaux horaire de la nouvelle solution

        # Attribution d'un score à la solution (Composé du nombre de conflit et du nombre de crénaux horaire)
        current_score = (current_conflicts, count_unique_slots(solution))
        new_score = (new_conflicts, new_slots)

        # Étape 3 : Critère d'acceptation de la nouvelle solution 
            #(Si le nombre de conflits est égal, on prend le nombre de crénaux comme critère)
        if (new_score < current_score or math.exp((current_conflicts - new_conflicts) / temperature) > random.random()):
                #On accepte la nouvelle solution si elle est meilleure. 
                #Si elle n'est pas meilleure, on peut quand même l'accepter pour échapper au minima locaux
            
            solution = new_solution
            current_conflicts = new_conflicts

            # Mise à jour de la meilleure solution trouvé jusqu'à présent
            if new_score < (conflictsStar, slotsStar):
                solutionStar = solution.copy()
                conflictsStar, slotsStar = new_conflicts, new_slots

        # On modifie la température en fonction du cooling_rate. On ajuste le cooloing rate en fonction du nombre d'itération.
        cooling_rate = (initial_cooling_rate - (k / max_iterations) * 0.01)
        temperature *= cooling_rate

        # Si la température descend sous la température minimale, on arrête l'algorithme. (Évite de compléter k itérations)
        if temperature < min_temperature:
            break
    
    return solutionStar

def greedy_initialization(schedule:Schedule, max_slots):
    """
    Initialize the solution using a greedy approach to minimize conflicts.
    :param schedule: Schedule object containing courses and conflict information.
    :param max_slots: Maximum number of time slots allowed.
    :return: a dictionnary where the keys are the list of the courses and the values are the time periods associated
    """
    solution = {}  # Initialisation d'une solution vide

    # On assigne chaque cours au premier crénaux horaire qui ne crée pas de conflits
    for course in schedule.conflict_graph.nodes:
        assigned = False  # Permet de vérifier si un crénaux est valide

        # On regarde chaque crénaux
        for slot in range(max_slots):
            solution[course] = slot  #On tente d'assigner le cours au crénaux

            # On vérifie si cette assignation entraîne un conflit
            if evaluate_solution(solution, schedule) == 0:
                assigned = True  # S'il n'y a pas de conflits, on confirme le crénaux 
                break  

        # Si aucun crénaux sans conflit est trouvé, on assigne un crénaux au hasard
        if not assigned:
            solution[course] = random.randint(0, max_slots - 1)

    return solution

def random_swap(solution, courses, max_slots):
    """
    Generate a neighboring solution by randomly swapping the slots of two courses.
    :param solution: a dictionnary where the keys are the list of the courses and the values are the time periods associated.
    :param courses: List of all courses.
    :param max_slots: Maximum number of time slots allowed.
    :return: A new neighboring solution.
    """
    # On échange les crénaux horaire de deux cours choisi au hasard
    course1, course2 = random.sample(courses, 2)  # Choix de deux cours au hasard
    solution[course1], solution[course2] = solution[course2], solution[course1] # Échange des crénaux de ces 2 cours

    # On change aussi le crénaux d'un cours au hasrd pour un crénaux au hasard
    random_course = random.choice(courses)
    new_slot = random.randint(0, max_slots - 1)
    solution[random_course] = new_slot

    return solution

def evaluate_solution(solution, schedule:Schedule):
    """
    Evaluate the solution by counting the number of conflicts.
    :param solution: a dictionnary where the keys are the list of the courses and the values are the time periods associated.
    :param schedule: object describing the input.
    :return: The total number of conflicts.
    """
    conflicts = 0  # Initialisation du nombre de conflits

    # On regarde chaque paire de cours dans la liste de conflits
    for course1, course2 in schedule.conflict_list:
        
        if course1 in solution and course2 in solution:
            # Si les deux cours ont le même crénaux horaire, on incrémente le compteur de 1
            if solution[course1] == solution[course2]:
                conflicts += 1

    return conflicts  # Retourne le nombre total de conflits trouvé

def count_unique_slots(solution):
    """
    Count the number of unique time slots used in the solution.
    :param solution: a dictionnary where the keys are the list of the courses and the v
    :return: The number of unique time slots.
    """
    
    return len(set(solution.values()))

>>>>>>> d6bde5c1fce324ff3b890b2f8a8eebe99ee5c1c2
