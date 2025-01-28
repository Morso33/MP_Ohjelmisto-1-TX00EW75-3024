import math
import random

circle_radius = 1
square_side_length = circle_radius * 2

def ray_cast_circle(pos_x, pos_y):
    if math.sqrt(pos_x**2 + pos_y**2) <= circle_radius:
        return True
    
iterations = int(input("Montako pistettä? "))
hits = 0
for i in range(iterations):
    pos_x = random.uniform(-1, 1)
    pos_y = random.uniform(-1, 1)
    hit_circle = ray_cast_circle(pos_x, pos_y)
    if hit_circle:
        hits += 1

pi_estimate = 4 * hits / iterations
print(f"Pi on noin {pi_estimate}")