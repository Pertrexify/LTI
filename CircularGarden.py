import math
rad = float(input("Enter your Radius for your Garden 👌: "))
area = rad*rad

circ = math.pi*rad

SR = math.sqrt(area)

ARD = math.floor(area)

ARU = math.ceil(area)

print("=========================")
print(f"Your area is: {area:.2f}")
print(f"Circ:, {circ:.2f}")
print(f"SR:, {SR:.2f}")
print("Area Rounded Down:", ARD)
print("Area Rounded Up:", ARU)
print("=========================")