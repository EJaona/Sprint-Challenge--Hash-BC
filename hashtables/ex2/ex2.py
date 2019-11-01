#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in range(length):
        # check to see if it's the it's the ticket with "NONE" source (First Ticket)
        if tickets[i].source == "NONE":
            
            route[0] = tickets[i].destination
        # else, add to hashtable with
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    # When all tickets are in, loop through and add the correct items to the route...
    for j in range(length):
        print(f"route j{route[j]}")
        print(f"route j - 1{route[j - 1]}")
        
        if route[j-1] is not None:
            route[j] = hash_table_retrieve(hashtable, route[j-1])

    return route
