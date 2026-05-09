#calculate the hipotenuse of a Triangle (c = sqrt(a^2 + b^2 ))

import math 

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {round(hypotenuse, 2)}")