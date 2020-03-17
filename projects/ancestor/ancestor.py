
def earliest_ancestor(ancestors, starting_node):
    visited = set()
    found_earliest = False
    depth = 0
    while found_earliest is False:
        count = 0
        for pair in ancestors:
            if pair not in visited:
                if starting_node == pair[1]:
                    visited.add(pair)
                    starting_node = pair[0]
                    count += 1
                    depth += 1
                    break

        if count == 0:
            if depth == 0:
                return -1
            else:
                found_earliest = True

    return starting_node
                
            

            
            


        
