from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []
traversal_graph = {}


def bfs(traversal_graph, start_room_id):
    """
    Return a list containing the shortest path from
    start_room_id to room with unexplored 
    connected rooms in breath-first order.
    """

    # Create a Queue
    q = Queue()
    # Enqueue a path to the starting
    q.enqueue([start_room_id])
    visited = set()
    while q.size() > 0:

        # dequeue the first path
        path = q.dequeue()
        if path[-1] != start_room_id:
            v = path[-1][1]
        else:
            v = path[-1]
        
        
        if v not in visited:
            visited.add(v)
        
        if v == "?":
            return path
        
        for connected_room in traversal_graph[v]:
            path_copy = path.copy()
            path_copy.append((connected_room,traversal_graph[v][connected_room]))
            q.enqueue(path_copy)


def make_dic(directions):
    """
    Returns framework for traversal_graph
    """

    dic = {}
    if 'n' in directions:
        dic['n'] = '?'
    if 's' in directions:
        dic['s'] = '?'
    if 'w' in directions:
        dic['w'] = '?'
    if 'e' in directions:
        dic['e'] = '?'
    return dic

# Global Variables
last_direction_moved = ''
bfs_return = False
last_room_id = None

while len(traversal_graph) < len(room_graph):
    
    # If the current_room does not have an ID then create one
    loop_detected = False
    if player.current_room.id not in traversal_graph:
        traversal_graph[player.current_room.id] = make_dic(player.current_room.get_exits())
    else:
        # If current room is already in traversal and we did not return from bfs
        loop_detected = True
        
    # Fill in entries
    if len(traversal_graph) > 1 and bfs_return == False:
        if loop_detected == False:
            if last_room_id != list(traversal_graph.keys())[-1]:
                last_room_id = last_room_id
            else:
                last_room_id = list(traversal_graph.keys())[-2]

            
        # Fill in the previous room's newly found information
        traversal_graph[last_room_id][last_direction_moved] = player.current_room.id
        # Fill in the current room information from the last room
        # Revert last_direction_moved to be the opposite
        if last_direction_moved == 'n':
            traversal_graph[player.current_room.id]['s'] = last_room_id
        elif last_direction_moved == 's':
            traversal_graph[player.current_room.id]['n'] = last_room_id
        elif last_direction_moved == 'e':
            traversal_graph[player.current_room.id]['w'] = last_room_id
        elif last_direction_moved == 'w':
            traversal_graph[player.current_room.id]['e'] = last_room_id

    if bfs_return == True:
        bfs_return = False

    # CHECK again after adding new current_room.id to traversal_graph
    # print(len(traversal_graph), " | ", len(room_graph))
    if len(traversal_graph) == len(room_graph):
        break

    # Create a list of rooms available with "?"
    exits = []
    for exit in traversal_graph[player.current_room.id]:
        if traversal_graph[player.current_room.id][exit] == "?":
            exits.append(exit)
    
    # If there are no rooms availiable with a "?"...
    if len(exits) == 0:
        # GO BACK
        # Use a BFS to find a path to a room with "?"
        path = bfs(traversal_graph, player.current_room.id)

        # remove first element
        path = path[1-len(path):]
        # remove last element
        path = path[:-1]
        # convert to "n","s","e","w"
        path_back = []
        for pair in path:
            path_back.append(pair[0])
        

        # Add to path
        traversal_path.extend(path_back)

        # Travel backwards to room with "?" with found path
        for exit in path_back:
            player.travel(exit)

        bfs_return = True

    else:
        
        # Prioritize going north then east then south then west
        if 'n' in exits:
            last_direction_moved = 'n'
        elif 'e' in exits:
            last_direction_moved = 'e'
        elif 's' in exits:
            last_direction_moved = 's'
        elif 'w' in exits:
            last_direction_moved = 'w'
        else:
            # Choose randomly from the list
            last_direction_moved = random.choice(exits)
        
        # Move to next room
        traversal_path.append(last_direction_moved)
        last_room_id = player.current_room.id
        player.travel(last_direction_moved)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
    print(traversal_path)
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
