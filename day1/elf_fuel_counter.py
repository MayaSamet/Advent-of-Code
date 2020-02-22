# part 1
f = open('input.txt', 'r')
masses = f.readlines()
masses = list(map(int, masses)) 
f.close()

total_fuel = 0

for mass in masses:
    total_fuel += int(mass/3)-2

# for solution:
# print(total_fuel)

# part 2

total_fuel_2 = []

for mass in masses:
    fuel_req = 0
    while mass > 0:
        mass = int(mass/3)-2
        fuel_req += mass
    total_fuel_2.append(fuel_req)

print(masses)
print(total_fuel_2)

        
