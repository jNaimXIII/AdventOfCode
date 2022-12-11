with open("dummy.txt") as file:
    monkeys = file.read().strip().split("\n\n")


def _20_rounds():
    monkey_items = []
    monkey_operations = []
    monkey_tests = []
    monkey_if_true = []
    monkey_if_false = []
    monkey_inspections = []

    for monkey in monkeys:
        instructions = monkey.split("\n")

        items = [
            int(i) for i in

            instructions[1]
            .strip()
            .removeprefix("Starting items: ")
            .split(", ")
        ]
        monkey_items.append(items)

        operation = instructions[2].strip().removeprefix("Operation: new = ")
        monkey_operations.append(operation)

        test = instructions[3].strip().removeprefix("Test: divisible by ")
        monkey_tests.append(int(test))

        if_true = instructions[4].strip().removeprefix(
            "If true: throw to monkey"
        )
        monkey_if_true.append(int(if_true))

        if_false = instructions[5].strip().removeprefix(
            "If false: throw to monkey"
        )
        monkey_if_false.append(int(if_false))

        monkey_inspections.append(0)

    lcm = 1
    for i in monkey_tests:
        lcm *= i

    for round in range(20):
        for i in range(len(monkey_items)):
            monkey = monkey_items[i]

            items_thrown_to = [[] for _ in monkey_items]
            items_thrown_from = [[] for _ in monkey_items]

            for j in range(len(monkey)):
                monkey_inspections[i] += 1

                item = monkey[j]

                operation = monkey_operations[i]
                test = monkey_tests[i]

                old = item

                new = eval(operation)
                new = new // 3

                if new % test == 0:
                    throw = monkey_if_true[i]

                    items_thrown_from[i].append(old)
                    items_thrown_to[throw].append(new)
                else:
                    throw = monkey_if_false[i]

                    items_thrown_from[i].append(old)
                    items_thrown_to[throw].append(new)

            for j in range(len(items_thrown_from)):
                monkey = items_thrown_from[j]

                for item in monkey:
                    monkey_items[j].remove(item)

            for j in range(len(items_thrown_to)):
                monkey = items_thrown_to[j]

                for item in monkey:
                    monkey_items[j].append(item)

    _monkey_inspections = monkey_inspections.copy()

    highest_inspections = max(_monkey_inspections)
    _monkey_inspections.remove(highest_inspections)
    second_highest_inspections = max(_monkey_inspections)

    print(highest_inspections * second_highest_inspections)


def _10000_rounds():
    monkey_items = []
    monkey_operations = []
    monkey_tests = []
    monkey_if_true = []
    monkey_if_false = []
    monkey_inspections = []

    for monkey in monkeys:
        instructions = monkey.split("\n")

        items = [
            int(i) for i in

            instructions[1]
            .strip()
            .removeprefix("Starting items: ")
            .split(", ")
        ]
        monkey_items.append(items)

        operation = instructions[2].strip().removeprefix("Operation: new = ")
        monkey_operations.append(operation)

        test = instructions[3].strip().removeprefix("Test: divisible by ")
        monkey_tests.append(int(test))

        if_true = instructions[4].strip().removeprefix(
            "If true: throw to monkey"
        )
        monkey_if_true.append(int(if_true))

        if_false = instructions[5].strip().removeprefix(
            "If false: throw to monkey"
        )
        monkey_if_false.append(int(if_false))

        monkey_inspections.append(0)

    lcm = 1
    for i in monkey_tests:
        lcm *= i

    for round in range(10000):
        for i in range(len(monkey_items)):
            monkey = monkey_items[i]

            items_thrown_to = [[] for _ in monkey_items]
            items_thrown_from = [[] for _ in monkey_items]

            for j in range(len(monkey)):
                monkey_inspections[i] += 1

                item = monkey[j]

                operation = monkey_operations[i]
                test = monkey_tests[i]

                old = item

                new = eval(operation)
                new = new % lcm

                if new % test == 0:
                    throw = monkey_if_true[i]

                    items_thrown_from[i].append(old)
                    items_thrown_to[throw].append(new)
                else:
                    throw = monkey_if_false[i]

                    items_thrown_from[i].append(old)
                    items_thrown_to[throw].append(new)

            for j in range(len(items_thrown_from)):
                monkey = items_thrown_from[j]

                for item in monkey:
                    monkey_items[j].remove(item)

            for j in range(len(items_thrown_to)):
                monkey = items_thrown_to[j]

                for item in monkey:
                    monkey_items[j].append(item)

    _monkey_inspections = monkey_inspections.copy()

    highest_inspections = max(_monkey_inspections)
    _monkey_inspections.remove(highest_inspections)
    second_highest_inspections = max(_monkey_inspections)

    print(highest_inspections * second_highest_inspections)


# ANSWER (PART 1)
_20_rounds()

# ANSWER (PART 2)
_10000_rounds()
