with open("input.txt") as file:
    crates, moves = file.read().split("\n\n")

column_width = 3
columns = [
    int(i) for i in
    crates.split('\n')[-1].strip().split(" " * column_width)
]
crates = crates.split('\n')[:-1]

stack = [[] for _ in columns]

for column in columns:
    for crate in crates:
        column_start = (column - 1) * (column_width + 1)
        column_end = column_start + (column_width + 1)
        column_crate = crate[column_start:column_end][1:2]

        if column_crate != " " and column_crate != "":
            stack[column - 1].append(column_crate)

moves = moves.strip().split("\n")

crane9000_stack = [i.copy() for i in stack]
for move in moves:
    move = move.replace("move ", "").replace("from ", "").replace("to ", "")
    count, origin, destination = [int(i) for i in move.split(" ")]
    origin -= 1
    destination -= 1

    for i in range(0, count):
        origin_column = crane9000_stack[origin]
        container = origin_column.pop(0)

        destination_column = crane9000_stack[destination]
        destination_column.insert(0, container)

uppermost_containers = ""
for column in crane9000_stack:
    uppermost_containers += column[0]

# ANSWER (PART 1)
print(uppermost_containers)

crane9001_stack = [i.copy() for i in stack]

for move in moves:
    move = move.replace("move ", "").replace("from ", "").replace("to ", "")
    count, origin, destination = [int(i) for i in move.split(" ")]
    origin -= 1
    destination -= 1

    crates_to_move = []

    for i in range(0, count):
        origin_column = crane9001_stack[origin]
        container = origin_column.pop(0)

        crates_to_move.append(container)

    destination_column = crane9001_stack[destination]
    for i in range(0, count):
        destination_column.insert(0, crates_to_move.pop())

uppermost_containers = ""
for column in crane9001_stack:
    uppermost_containers += column[0]

# ANSWER (PART 2)
print(uppermost_containers)
