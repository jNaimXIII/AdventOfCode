with open('input.txt') as file:
    data = file.read().strip()

elves = data.split('\n\n')
calories = []

for i in range(len(elves)):
    elf = elves[i].split('\n')

    for j in range(len(elf)):
        calorie = int(elf[j])
        elf[j] = calorie

    elves[i] = elf
    calories.insert(i, sum(elf))

max_calorie = max(calories)

# ANSWER (PART 1)
print(max_calorie)


max_calories = []
while len(max_calories) < 3:
    max_calorie = max(calories)
    max_calories.append(max_calorie)
    calories.remove(max_calorie)

# ANSWER (PART 2)
print(sum(max_calories))
