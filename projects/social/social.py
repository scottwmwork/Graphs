import random 

import os
os.chdir('../graph')
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # Write a for loop that calls create user the right amount of times
        for i in range(num_users):
            self.add_user(f"User {self.i+1}")

        # Create friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        visited = {}
        queue = Queue()
        
        # Create a Queue
        q = Queue()
        # Enqueue a path to the starting user_id
        q.enqueue([user_id])
        # While the queue is not empty...
        while q.size > 0
            #dequeue the first path
            path = q.dequeue()
            # grab the last id from the path
            current_id = path[-1]
            # check if it's been visited
            # if not...
            if current_id not in visited:
                #   add it to visited along with the path
                visited[current_id] = path
                # Enqueue the path to each friend to the queue
                for friend_id in self.friendships[current_id]:
                    # copy the path
                    path_copy = path.copy()
                    # append each neighbor
                    path_copy.append(friend_id)
                    # enqueue
                    q.enqueue(path_copy)
            
        return visited


    
            


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
