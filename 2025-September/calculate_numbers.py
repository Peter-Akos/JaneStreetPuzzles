def construct_possible_configurations():
    solutions = []
    for i in range(6):
        for j in range(6):
            for k in range(6):
                for l in range(6):
                    for m in range(6):
                        if i + j + k + l + m == 5:
                            s = j + (2*k) + (3*l) + (4*m)
                            if s % 5 ==0:
                                solutions.append([i, j, k, l, m])
                                print(f"{[i, j, k, l, m]} with s={s}")


    print(len(solutions))

def generate_lists(n, total, min_val=0, max_val=9):
    """
    Generate all lists of length n that sum to total, with each element between min_val and max_val.
    """
    if n == 0:
        if total == 0:
            yield []
        return
    for i in range(min_val, min(max_val, total) + 1):
        for lst in generate_lists(n-1, total - i, min_val, max_val):
            yield [i] + lst

if __name__ == "__main__":
    construct_possible_configurations()
    all_lists = list(generate_lists(26, 9))
    print(len(all_lists))

