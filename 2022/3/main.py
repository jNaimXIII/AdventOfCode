with open('input.txt') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

compartments = []
priorities = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

accumulated_priority = 0

for line in lines:
    compartment_a = [*line[:len(line) // 2]]
    compartment_b = [*line[len(line) // 2:]]

    common_item = ""
    for i in compartment_a:
        if i in compartment_b:
            common_item = i
            break
    for j in compartment_b:
        if j in compartment_a:
            common_item = j
            break

    priority = priorities.index(common_item)
    accumulated_priority += priority


# ANSWER (PART 1)
print(accumulated_priority)


groups = [[] for _ in range(0, len(lines) // 3)]
groups_priority = 0

for i in range(0, len(lines)):
    elf = lines[i]
    groups[i // 3].append(elf)

for elves in groups:
    a, b, c = elves

    common_item = ""
    for i in a:
        if i in b:
            if i in c:
                common_item = i
                break

    priority = priorities.index(common_item)
    groups_priority += priority

# ANSWER (PART 2)
print(groups_priority)
