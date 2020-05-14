#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    d = {}
    route = []
    for x in tickets:
        d[x.source] = x.destination
    y = "NONE"
    for x in range(length):
        route.append(d[y])
        y = d[y]
            
    """
    YOUR CODE HERE

    need to take an array "tickets" and sort them in a linked list from start to finish. need to find the head node, which is source: None, Destination: LAX. Then find the ticket with source of LAX and make the next destination the next node and repeat. 
    """
    
    return route