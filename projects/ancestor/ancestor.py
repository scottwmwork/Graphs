


def earliest_ancestor(ancestors, starting_node):
    visited = set()
    ends = []
    depth = 0

    count = 0
    for pair in ancestors:
        if starting_node == pair[1] and pair not in visited:
            visited.add(pair)
            starting_node = pair
            count += 1
            depth += 1

    if count == 0:
