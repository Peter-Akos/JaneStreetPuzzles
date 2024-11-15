import numpy as np
from scipy.integrate import dblquad


def integrate_over_triangle(function):
    result_left, error_left = dblquad(function, 0, 1 / 2, lambda x: 0, lambda x: x)

    result_right, error_right = dblquad(function, 1 / 2, 1, lambda x: 0, lambda x: 1 - x)

    print(result_left, result_right, error_left, error_right)

    return 4 * (result_left + result_right)


# Define the function to integrate
def area_left_sector(y, x):
    return (x ** 2 + y ** 2) * np.arctan(y / x) / 2


def area_right_sector(y, x):
    return ((1 - x) ** 2 + y ** 2) * np.arctan(y / (1 - x)) / 2


def area_triangle_middle(y, x):
    return y / 2


def area_left_quarter_circle(y, x):
    return (x ** 2 + y ** 2) * np.pi / 4


def area_right_quarter_circle(y, x):
    return ((1 - x) ** 2 + y ** 2) * np.pi / 4


if __name__ == "__main__":
    expected_left_sector = integrate_over_triangle(area_left_sector)
    print(expected_left_sector)

    expected_right_sector = integrate_over_triangle(area_right_sector)
    print(expected_right_sector)

    expected_area_middle_triangle = integrate_over_triangle(area_triangle_middle)
    print(expected_area_middle_triangle)

    expected_area_left_quarter_circle = integrate_over_triangle(area_left_quarter_circle)
    print(expected_area_left_quarter_circle)

    expected_area_right_quarter_circle = integrate_over_triangle(area_right_quarter_circle)
    print(expected_area_right_quarter_circle)

    total_quarters = expected_area_left_quarter_circle + expected_area_right_quarter_circle
    print(f"Total area of quarter circles:{total_quarters}")

    intersection = expected_left_sector + expected_right_sector - expected_area_middle_triangle
    print(f"Intersection area: {intersection}")

    print(f"Result: {total_quarters - intersection - intersection}")

    total_quarters_exact = np.pi / 6
    print(f"Total area of quarter circles exactly:{total_quarters_exact}")
    intersection_exact = (np.log(4) + (2 * np.log(2)) - 2) / 48

    print(f"Exact Intersection area of circles: {intersection_exact}")

    print(f"Exact Result: {total_quarters_exact - intersection_exact - intersection_exact}")

    # 0.4914075788383081  Approximated
    # 0.491407578838308   Exact
