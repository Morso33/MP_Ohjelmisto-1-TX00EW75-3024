import math

def pizza_price_per_square_meter(diameter_centimeters, price):
    radius = diameter_centimeters / 2
    area_cm2 = math.pi * radius ** 2
    area_m2 = area_cm2 / 10_000  # Convert to m²
    price_per_square_meter = price / area_m2
    return price_per_square_meter


pizza_1_price = float(input("Give the price of the first pizza: "))
pizza_1_diameter = float(input("Give the diameter of the first pizza: "))
pizza_2_price = float(input("Give the price of the second pizza: "))
pizza_2_diameter = float(input("Give the diameter of the second pizza: "))

pizza_1_price_per_square_meter = pizza_price_per_square_meter(pizza_1_diameter, pizza_1_price)
pizza_2_price_per_square_meter = pizza_price_per_square_meter(pizza_2_diameter, pizza_2_price)

print (f"{pizza_1_price_per_square_meter:.2f} euros.")
print (f"{pizza_2_price_per_square_meter:.2f} euros.")

if pizza_1_price_per_square_meter < pizza_2_price_per_square_meter:
    print("The first pizza is cheaper.")
else:
    print("The second pizza is cheaper.")
