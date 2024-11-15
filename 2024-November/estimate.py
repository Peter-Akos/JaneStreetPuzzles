import numpy as np


# Function to check if the point (x, y) lies inside the triangle with vertices A(0, 0), B(1, 0), C(0.5, 0.5)
def is_point_inside_triangle(x, y):
    # Check if the point (x, y) is inside the triangle
    if 0 <= x <= 0.5:  # For the left half of the triangle (0 <= x <= 0.5)
        return 0 <= y <= x
    elif 0.5 < x <= 1:  # For the right half of the triangle (0.5 < x <= 1)
        return 0 <= y <= (-x + 1)
    return False  # If x is outside the range [0, 1], return False


# Function to simulate choosing random points and calculating the mean distance from the x-axis
def simulate_random_points(num_points):
    points_x = []
    points_y = []
    metrics = []

    for _ in range(num_points):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        if is_point_inside_triangle(x, y):
            points_x.append(x)
            points_y.append(y)

            # # Calculate distance from (0,0)
            # distance = np.sqrt(x ** 2 + y ** 2)
            # metrics.append(distance)

            # # Area of circle with center in (0,0)
            # radius_2 = (1 - x) ** 2 + y ** 2
            # metrics.append(np.pi * radius_2 / 4)

            # Area of split circle
            radius_2 = x ** 2 + y ** 2
            metrics.append(np.arctan(y / x) * radius_2 / 2)

    # Return the mean of the distances
    return points_x, points_y, np.mean(metrics)


num_points = 10000000
points_x, points_y, mean_distance = simulate_random_points(num_points)
print(f"Mean metric : {mean_distance}")
