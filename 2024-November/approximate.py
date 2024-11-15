import numpy as np
import sys
import time


def generate_random_point():
    """Generate a random point within the unit square."""
    return np.random.rand(2)


def perpendicular_bisector(p1, p2):
    """Calculate the perpendicular bisector of the line segment from p1 to p2."""
    midpoint = (p1 + p2) / 2
    if p1[0] != p2[0]:
        slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
        perp_slope = -1 / slope
        return midpoint, perp_slope
    else:
        return midpoint, None  # None slope indicates a vertical bisector


def closest_side(point):
    """Identify the closest side of the square to a given point."""
    x, y = point
    distances = {
        'left': x,  # Distance to x = 0
        'right': 1 - x,  # Distance to x = 1
        'bottom': y,  # Distance to y = 0
        'top': 1 - y  # Distance to y = 1
    }
    return min(distances, key=distances.get)


def intersects_side(midpoint, slope, side):
    """Check if the perpendicular bisector intersects the specified side of the unit square."""
    x, y = midpoint

    # Vertical bisector case
    if slope is None:
        return side in ['left', 'right'] and 0 <= x <= 1

    # Check for intersection based on the side
    if side == 'bottom':
        x_intersect = x + (-y) / slope
        return 0 <= x_intersect <= 1
    elif side == 'top':
        x_intersect = x + (1 - y) / slope
        return 0 <= x_intersect <= 1
    elif side == 'left':
        y_intersect = y + slope * (-x)
        return 0 <= y_intersect <= 1
    elif side == 'right':
        y_intersect = y + slope * (1 - x)
        return 0 <= y_intersect <= 1
    return False


def estimate_probability(n_trials):
    """Run n_trials and estimate the probability, updating the result continuously."""
    successful_trials = 0

    for i in range(1, n_trials + 1):
        # Generate random points
        red_point = generate_random_point()
        blue_point = generate_random_point()

        # Find the perpendicular bisector
        midpoint, slope = perpendicular_bisector(red_point, blue_point)

        # Identify the closest side to the blue point
        closest = closest_side(blue_point)

        # Check if the bisector intersects the closest side
        if intersects_side(midpoint, slope, closest):
            successful_trials += 1

        # Update probability estimate and print continuously
        probability = successful_trials / i
        # print(f"Trial {i}/{n_trials} - Current Estimated Probability: {probability:.10f}", end='\r')
        # time.sleep(0.01)  # Optional: slows down for visualization

    # Final output
    print(f"\nFinal Estimated Probability (after {n_trials} trials): {probability:.10f}")


estimate_probability(1000000)
# 0.4913305800
