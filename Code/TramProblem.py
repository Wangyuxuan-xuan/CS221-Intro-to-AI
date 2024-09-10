from enum import Enum
import sys
from queue import PriorityQueue

sys.setrecursionlimit(100000)

Destination = 10

### Model (Search Problem)
class TransportationProblem(object):

    WALK_COST = 1
    TRAM_COST = 2

    WALK = "walk"
    TRAM = "tram"

    def __init__(self, destination):
        # N number of blocks
        self.destination = destination

    def startState(self) -> int:
        return 1
    
    def isEnd(self, state):
        return state == self.destination
    
    def succAndCost(self, state : int):
        '''
        Return a list of (action, newState, cost) triples
        Meaning return the a list of: actions we can take, what new state we gonna endup at, and what the cost gonna be
        '''
        result = []
        if(state + 1 <= self.destination):
            result.append((self.WALK, state + 1, self.WALK_COST))
        
        if(state * 2 <= self.destination):
            result.append((self.TRAM, state * 2, self.TRAM_COST))

        return result


### Algorithms
def backtrackingSearch(self, problem):
        
    best = {
        "totalCost" : sys.maxsize,
        "history": None
    }

    memo = {}

    def recurse(currentState, history, totalCost):

        if(currentState in memo):
            for totalCost, history in memo[currentState]:
                best["totalCost"] = totalCost
                best["history"] = history
            return

        if(problem.isEnd(currentState)):
            #Update the best cost if we find a better solution
            if(totalCost < best["totalCost"]):
                best["totalCost"] = totalCost
                best["history"] = history
                memo[currentState] = (totalCost, history)

        for action, newState, cost in problem.succAndCost(currentState):
            recurse(newState, history + [(action, newState, cost)], totalCost + cost)

    recurse(problem.startState(), history=[], totalCost=0)

    return best

def printSolution(solution):
    totalCost = solution["totalCost"]
    history = solution["history"]
    print("minimum cost is {}".format(totalCost))

    for h in history:
        print(h)


# You just need to know the current state
def dynamicProgramming(problem):

    memo = {} # state -> futureCost(state) action, newState, cost
    def futureCost(state):

        if problem.isEnd(state):
            return 0
        
        if state in memo:
            return memo[state][0]
        
        minFutureCostWithAction = min(
            (curCost + futureCost(newState), action, newState, curCost)
            for action, newState, curCost in problem.succAndCost(state)
        ) 
            
        memo[state] = minFutureCostWithAction
        minFutureCost = minFutureCostWithAction[0]
        return minFutureCost

    
    state = problem.startState()
    minCost = futureCost(state)

    # Recover History
    history = []
    while not problem.isEnd(state):
        _, action, newState, cost= memo[state]
        history.append((action, newState, cost))
        state = newState

    return {
        "totalCost" : minCost,
        "history": history
    }




# searching method in a graph that visits nodes in order of their path cost from the start node. 
# It delves into the graph, visiting the node with the smallest cumulative path cost first.
def UniformCostSearch(problem):
    frontier = PriorityQueue()
    frontier.put((0, problem.startState()))
    
    while(True):
        # Move minumun cost from frontier to explored
        pastCost, state = frontier.get()

        # If the end state popped up, meaning we have already have the minumum cost to the end state
        # Everything else left in the queue would have a larger past cost.
        # If it's not (The end state may or may not in the queue yet), meaning there's other possible path
        # That may have a lower cost 
        if(problem.isEnd(state)):
            return {
                "totalCost" : pastCost,
                "history": []
            }
        
        # Add all the successors of current state to frontier
        for action, newState, cost in problem.succAndCost(state):
            frontier.put((pastCost + cost, newState))





### Inference
problem = TransportationProblem(destination=Destination)
# solution = problem.backtrackingSearch(problem)
solution = dynamicProgramming(problem)
printSolution(solution)

# solution = UniformCostSearch(problem)
# problem.printSolution(solution)
# print(problem.succAndCost(9))
