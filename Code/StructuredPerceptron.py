from enum import Enum
import sys
from queue import PriorityQueue

sys.setrecursionlimit(100000)

Destination = 10

### Model (Search Problem)
class TransportationProblem(object):

    WALK_COST: int
    TRAM_COST: int

    WALK = "walk"
    TRAM = "tram"

    def __init__(self, destination, weights):
        # N number of blocks
        self.destination = destination
        self.WALK_COST = weights["walk"]
        self.TRAM_COST = weights["tram"]

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

    return (minCost, history)


### Learning - learn the weights
#### Generate Training Examples

def predict(NumberOfBlocks, weights):
    ''' 
    F(x)
    Input (x): N number of blocks and weights
    Output (y): path (a sequence of actions)
    '''
    problem = TransportationProblem(NumberOfBlocks, weights)
    # Pridict using Dynamicprogramming or other Algo
    totalCost, history = dynamicProgramming(problem)
    return [action for action, newState, cost in history]

def generateExamples(numberOfExamples):
    trueWeights = {
        "walk": 1,
        "tram": 5
    }

    dataSet = []
    for n in range(1,numberOfExamples):
        path = predict(n, trueWeights)
        data = (n, path)
        dataSet.append(data)
     
    return dataSet

def structuredPerceptron(examples):
    weights = {
        "walk": 0,
        "tram": 0
    }

    for t in range(1,100):
        numberOfMistakes = 0
        for n, trueActions in examples:
            predictActions = predict(n ,weights)

            if(predictActions != trueActions):
                numberOfMistakes += 1

            # Update weights
            # In this case, we cancelled the change if two weights are the same
            # And decreased the cost that are the same with true actions
            # Increased the cost that are different from true actions
            for action in trueActions:
                weights[action] -= 1
            for action in predictActions:
                weights[action] += 1
        print('Itration {}, numMistakes = {}, weights = {}'.format(t, numberOfMistakes, weights))

        if(numberOfMistakes == 0):
            break




numOfExamples = 12
examples = generateExamples(numOfExamples)
print("Training Dataset:")
for example in examples:
    print('   ', example)

structuredPerceptron(examples)


### Inference
weights = {
    "walk": 1,
    "tram": 2
}
# problem = TransportationProblem(destination=Destination, weights=weights)
# solution = dynamicProgramming(problem)
# printSolution(solution)