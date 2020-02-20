f = open('input.txt', 'r')
masses = f.readlines()
masses = list(map(int, masses)) 
f.close()

total_fuel = int(0)

for mass in masses:
    total_fuel += int(mass/3)-2

print(total_fuel)
