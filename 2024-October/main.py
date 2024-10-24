from finder import find_equations
from pathfinder import Pathfinder
import marisa_trie
import optuna

TARGET_SCORE = 2024


def check_numbers(a, b, c):
    combinations = find_equations(a, b, c, TARGET_SCORE)
    if len(combinations) == 0:
        return 99999

    trie = marisa_trie.Trie(combinations)

    p = Pathfinder((0, 5), (5, 0), trie)
    p.find_all_paths()

    if len(p.all_paths) == 0:
        return 99999

    print(p.all_paths[0])

    p = Pathfinder((0, 0), (5, 5), trie)
    p.find_all_paths()

    if len(p.all_paths) == 0:
        return 99999

    print(p.all_paths[0])


    return a+b+c


# Optuna objective function
def objective(trial):
    a = trial.suggest_int('a', 1, 20)  # Adjust range as needed
    b = trial.suggest_int('b', 1, 20)
    c = trial.suggest_int('c', 1, 20)


    # Call the check_numbers function and return the result
    return check_numbers(a, b, c)


# Optuna optimization
if __name__ == '__main__':
    study = optuna.create_study(direction='minimize')
    study.optimize(objective, n_trials=125)

    # Output the best combination found
    print(f"Best parameters: {study.best_params}")
    print(f"Best value: {study.best_value}")
