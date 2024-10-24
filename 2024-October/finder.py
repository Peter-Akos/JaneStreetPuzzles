from collections import deque


def find_equations(a, b, c, target=2024, max_depth=15):
    # A queue to perform BFS; each entry is (current_value, equation_string, last_used, current_depth)
    queue = deque([(a, 'a', 0)])

    # List to store all valid equations that end in 'c'
    results = []

    # Map to numbers for easier reference
    number_map = {'a': a, 'b': b, 'c': c}

    # Perform BFS
    while queue:
        current_value, path, current_depth = queue.popleft()

        last_used = path[-1]

        # Check if the target is reached and ends with 'c'
        if current_value == target and last_used == 'c':
            results.append(path)

        if current_value > target:
            continue

        # Check if maximum depth is reached
        if current_depth < max_depth:
            # Generate next possible values by adding or multiplying with a, b, or c
            for num_key, num in number_map.items():
                if num_key == last_used:
                    # Option 1: Addition (stay on the same number)
                    next_value = current_value + num
                    queue.append((next_value, f"{path}{num_key}", current_depth + 1))
                else:
                    # Option 2: Multiplication (move to a different number)
                    next_value = current_value * num
                    queue.append((next_value, f"{path}{num_key}", current_depth + 1))

    return results

def apply_operations(operation_string, a, b, c):
    # Map to values for easier lookup
    value_map = {'a': a, 'b': b, 'c': c}

    # Initialize the result with the value of the first character
    result = value_map[operation_string[0]]

    # Traverse the string and apply operations
    for i in range(1, len(operation_string)):
        current_char = operation_string[i]
        previous_char = operation_string[i - 1]

        if current_char == previous_char:
            # Add the value if it's the same character as before
            result += value_map[current_char]
        else:
            # Multiply the value if it's a different character
            result *= value_map[current_char]

    return result



