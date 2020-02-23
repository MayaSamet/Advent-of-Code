# part 1
f = open('input.txt', 'r')
masses = f.readlines()
masses = list(map(int, masses)) 
f.close()

total_fuel = 0

for mass in masses:
    total_fuel += int(mass/3)-2

print("Day 1 part 1 solution: " + str(total_fuel))

# part 2

total_fuel_2 = []

for mass in masses:
    fuel_req = 0
    while int(mass/3)-2 > 0:
        mass = int(mass/3)-2
        fuel_req += mass
    total_fuel_2.append(fuel_req)

print("Day 1 part 2 solution: " + str(sum(total_fuel_2)))

        
