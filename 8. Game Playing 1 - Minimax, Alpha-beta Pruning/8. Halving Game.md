class HalvingGame(object):

    def __init__(self, N) -> None:
        self.N = N

    # player {+1, -1}
    # state -> (player, number)
    def startState(self):
        return (+1, self.N)
    
    def isEnd(self, state):
        player, number = state
        return number == 0
    
    def utility(self, endState):
        player, number = endState
        assert number == 0
        # I am player +1, the opponent is -1
        # If I win I get +inf
        # If the opponent wins, I get -inf
        return player * float('inf')
    
    def actions(self, state):
        '''
        For any state the actions we can do is to substract or devide by 2
        '''
        return ['-', '/']
    
    def player(self, state):
        player, number = state
        return player
    
    def succ(self, state, action):
        '''
        The successor function takes a state, and an action
        and tells u (returns) what state u gonna end up at
        '''
        player, number = state
        if action == '-':
            # Shifting player and minus number by 1
            return (-player, number - 1)
        elif action == '/':
            # Shifting player and divide the number by 2
            # The / operator is used for float division, while the // operator is used for integer division
            return (-player, number // 2)
        
# General code

def humanPolicy(game : HalvingGame, state):
    while True:
        action = input('Input action:')
        if action in game.actions(state):
            return action

def minimaxPolicy(game : HalvingGame, state) -> str:

    def recurse(state):
        '''
        return a tuple of (
            value, action
        )
        '''
        if game.isEnd(state):
            return (game.utility(state), "none")
        
        # If ur not at the end state, ur either maximizing or minimizing 
        # over a set of choices
        # Which is gonna recurse over succsessor states
        # Array of tuple (value, action)
        choices = []
        for action in game.actions(state):
            value = recurse(game.succ(state, action))[0]
            choices.append((value, action))

        player, number = state
        
        # If the player is the agent => try to maximize the choices
        if player == +1:
            return max(choices)
        
        # If the player is the opponent => try to minimize the choices
        if player == -1:
            return min(choices)
            
    value, action = recurse(state)
    print('minimax says action = {}, value = {}'.format(action, value))

    return action
    


# Controller
policies = {+1: humanPolicy, -1:minimaxPolicy}
startNumber = 15
game = HalvingGame(N = startNumber)
state = game.startState()

while not game.isEnd(state):
    print('='*10, state)

    player = game.player(state)
    policy = policies[player]

    action  = policy(game, state)
    newState = game.succ(state, action)
    state = newState

print('utility = {}'.format(game.utility(state)))