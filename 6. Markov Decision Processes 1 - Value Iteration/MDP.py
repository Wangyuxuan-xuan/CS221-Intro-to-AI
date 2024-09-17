from enum import Enum
import os
import sys
from queue import PriorityQueue
from typing import Dict

sys.setrecursionlimit(100000)

Destination = 10

### Model (Search Problem)
class TransportationProblemMDP(object):

    WALK_REWARD = -1
    TRAM_REWARD = -2

    WALK = "walk"
    TRAM = "tram"

    TRAM_FAIL_PROB = 0.5
    def __init__(self, destination):
        # N number of blocks
        self.destination = destination

    def startState(self) -> int:
        return 1
    
    def isEnd(self, state):
        return state == self.destination
    
    def actions(self, state):
        '''
        Return a list of valid actions that we can take form the current state
        '''
        result = []
        if(state + 1 <= self.destination):
            result.append(self.WALK)
        
        if(state * 2 <= self.destination):
            result.append(self.TRAM)

        return result
    

    def succProbAndReward(self, state : int, action: str):
        '''
        Input: 
            current state
            Action that we gonna take
        Return a list of (newState, prob, rewards) triples
        Meaning return the a list of: 
            the new state we are gonna endup at, 
            what probability of it, 
            and the reward we get from it
        
        state = s, action = a, newState = s'
        prob = T(s, a, s'), reward = Reward(s, a, s')
        '''
        result = []
        if(action == self.WALK):
            # It is deterministic, so the prob is 1.
            result.append((state + 1, 1., self.WALK_REWARD))
        elif(action == self.TRAM):
            # There's a 50% chance that the tram could fail
            result.append((state, self.TRAM_FAIL_PROB, self.TRAM_REWARD))
            result.append((state * 2, 1. - self.TRAM_FAIL_PROB, self.TRAM_REWARD))
            
        return result

    def discountFactor(self):
        return 1.
    
    def states(self):
        return range(1, self.destination+1)

# Inference (Algorithms)
def valueIteration(mdp : TransportationProblemMDP):
    # Initialize
    valueOptDic: Dict[str, float] = {}  # state => Vopt[state]
    # Initialize all optimal value with 0
    for state in mdp.states():
        valueOptDic[state] = 0.
    
    def VQ(state, action):
        """Q value of chance node Q,
        If you take action a from state s.

        Returns:
            number: _description_
        """
        return sum(
            transProb * (reward + mdp.discountFactor() * valueOptDic[newState])
            for newState, transProb, reward in mdp.succProbAndReward(state, action)
        )

    def isConverged(valueDic, newValueDic):
        '''
        We want the maximum value difference of all states to be smaller than the treashold
        '''
        return max(abs(valueDic[state] - newValueDic[state])  for state in mdp.states()) < 1e-10
            

    while True:
        # Compute the new values (new V) with old values (V)
        newValueDic = {}

        for state in mdp.states():
            if mdp.isEnd(state):
                newValueDic[state] = 0
                break

            newValueDic[state] = max(
                VQ(state, action)   
                for action in mdp.actions(state)
            )

        # Check for convergence
        if (isConverged(valueOptDic, newValueDic)):
            break

        valueOptDic = newValueDic

        # Read out policy:
        pi = {}
        for state in mdp.states():
            if mdp.isEnd(state):
                for action in mdp.actions(state):
                    pi[(state, action)] = "none"
            else:
                # Otherwise it's gonna be the argmax of Q values
                # Which is the input that can maximize Q values
                # And how we gonna find the argmax?
                #  - We just gonna try out different actions and see

                for action in mdp.actions(state):
                    pi[(state, action)] = VQ(state, action)

                # pi[state] = max(
                #     (VQ(state, action), action) for action in mdp.actions(state)
                # )[1]

        # Print stuff out

        # print('{:25} {:25} {:25}'.format('state', 'valueOptDic[state]', 'pi[state])'))

        # for state in mdp.states():
        #     print('{:25} {:25} {:25}'.format(state, valueOptDic[state], pi[state]))

        print('{:25} {:25} {:25} {:25}'.format('state', 'action', 'valueOptDic[state]', 'pi[(state, action)])'))

        for state in mdp.states():
            for action in mdp.actions(state):
                print('{:25} {:25} {:25} {:25}'.format(state, action, valueOptDic[state], pi[(state, action)]))
        input()


mdp = TransportationProblemMDP(destination=10)
# print(mdp.actions(3))
# print(mdp.succProbAndReward(3, "tram"))
valueIteration(mdp)