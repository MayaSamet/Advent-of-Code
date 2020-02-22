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

total_fuel_2 = 0
ind = 0

for mass in masses:
    
    fuel_mass = mass
    while fuel_mass > 0:
        fuel_mass = int(fuel_mass/3)-2
        total_fuel_2 += fuel_mass
        
