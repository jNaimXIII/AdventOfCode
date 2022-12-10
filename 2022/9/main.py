"""
    Only been able to solve the first one with minor help. Will be back. ;)
"""

with open("input.txt") as file:
    steps = file.read().strip().split("\n")


places_visited = set()
headX = headY = tailX = tailY = 0

for step in steps:
    dir, count = step.split(" ")
    count = int(count)

    for _ in range(0, count):

        places_visited.add((tailX, tailY))

        if dir == "L":
            headX -= 1
        elif dir == "R":
            headX += 1

        if dir == "U":
            headY += 1
        elif dir == "D":
            headY -= 1

        diffX = abs(headX - tailX)
        diffY = abs(headY - tailY)

        if diffX >= 2:
            tailX = headX - 1 if tailX < headX else headX + 1
            tailY = headY

        elif diffY >= 2:
            tailX = headX
            tailY = headY - 1 if tailY < headY else headY + 1

        places_visited.add((tailX, tailY))


# ANSWER (PART 1)
print(len(places_visited))
