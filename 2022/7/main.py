class Node:
    def __init__(self, data):
        self.data = data

        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self

        self.children.append(child)

    def get_size(self):
        size = 0

        if self.data["type"] == "file":
            size += self.data["size"]

        for child in self.children:
            if child.data["type"] == "dir":
                size += child.get_size()

            if child.data["type"] == "file":
                size += child.data["size"]

        return size

    def get_level(self):
        level = 0

        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent

        return level

    def print_child(self):
        spaces = " " * self.get_level() * 2
        print(spaces + self.data["name"])

        for child in self.children:
            child.print_child()


with open("input.txt") as file:
    output = file.read().strip().split("\n")

path = []
current_node = Node({
    "name": "/",
    "type": "dir"
})


for line in output:
    if line.startswith("$ cd"):
        directory = line.removeprefix("$ cd ")

        if directory == "/":
            continue

        if directory == "..":
            path.pop()

            current_node = current_node.parent

        else:
            path.append(directory)

            child_node = Node({
                "name": directory,
                "type": "dir"
            })

            current_node.add_child(child_node)
            current_node = child_node

    elif line.split(" ")[0].isdigit():
        size, name = line.split(" ")

        child_node = Node({
            "name": name,
            "type": "file",
            "size": int(size)
        })
        current_node.add_child(child_node)

while current_node.parent:
    current_node = current_node.parent


def get_large_dirs(large_dir_limit):
    large_dirs = []

    def get_large_dirs_recursively(parent):
        for node in parent.children:
            if node.data["type"] == "dir":
                if node.get_size() <= large_dir_limit:
                    large_dirs.append(node.get_size())

                get_large_dirs_recursively(node)

    get_large_dirs_recursively(current_node)

    return large_dirs


# ANSWER (PART 1)
print(sum(get_large_dirs(100000)))


system_space = 70000000
update_space = 30000000
occupied_space = current_node.get_size()
available_space = system_space - occupied_space
required_space = update_space - available_space

large_dirs = get_large_dirs(70000000)
large_dirs.sort()

def get_update_space_removal_dir():
    for dir in large_dirs:
        if dir >= required_space:
            return dir

# ANSWER (PART 2)
print(get_update_space_removal_dir())
