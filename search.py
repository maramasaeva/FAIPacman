# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    import pacman
    from util import Stack
    from searchAgents import PositionSearchProblem
    from pacman import GameState
    reached = []
    frontier = util.Stack()

    start_state = problem.getStartState()

    for s in problem.getSuccessors(start_state):
        new_state = (s[0], [s[1]])
        frontier.push(new_state)

    while not frontier.isEmpty():
        current_state = frontier.pop()
        solution_path = current_state[1]

        if current_state[0] not in reached:
            reached.append(current_state[0])

            if problem.isGoalState(current_state[0]):
                print("Goal found!")
                print(current_state[1])
                return current_state[1]

            else:
                # get the successors and add to frontier
                
                for s in problem.getSuccessors(current_state[0]):
                    node = s[0]
                    direction = [s[1]]
                    cost = s[2]
                    new_path = solution_path + direction
                    new_state = (node, new_path)

                    frontier.push(new_state)
    else:
        print('Frontier is empty!')
        

    #util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    import pacman
    from util import Stack
    from searchAgents import PositionSearchProblem
    from pacman import GameState
    reached = []
    frontier = util.Queue()

    start_state = problem.getStartState()
    reached.append(start_state)

    for s in problem.getSuccessors(start_state):
        new_state = (s[0], [s[1]])
        frontier.push(new_state)

    while not frontier.isEmpty():
        current_state = frontier.pop()
        solution_path = current_state[1]

        if current_state[0] not in reached: 
            reached.append(current_state[0])

            if problem.isGoalState(current_state[0]):
                print("Goal found!")
                print(current_state[1])
                return current_state[1]

            else:
                # get the successors and add to frontier
                
                for s in problem.getSuccessors(current_state[0]):
                    node = s[0]
                    direction = [s[1]]
                    cost = s[2]
                    new_path = solution_path + direction
                    new_state = (node, new_path)

                    frontier.push(new_state)
    else:
        print('Frontier is empty!')


    #util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    reached = []
    frontier = util.PriorityQueue()

    start_state = problem.getStartState()
    reached.append(start_state)

    for s in problem.getSuccessors(start_state):
        new_state = (s[0], [s[1]], s[2])
        frontier.push(new_state, s[2])

    while not frontier.isEmpty():
        current_state = frontier.pop()
        current_cost = current_state[2]
        solution_path = current_state[1]

        if current_state[0] not in reached:
            reached.append(current_state[0])

            if problem.isGoalState(current_state[0]):
                print("Goal found!")
                #print(current_state[1])
                return current_state[1]

            else:
                # get the successors and add to frontier
                
                for s in problem.getSuccessors(current_state[0]):
                    node = s[0]
                    direction = [s[1]]
                    cost = s[2]
                    new_path = solution_path + direction
                    new_cost =  current_cost + cost #here!
                    new_state = (node, new_path, new_cost)

                    frontier.update(new_state, new_cost) # the new cost is the priority
    else:
        print('Frontier is empty!')


    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    reached = []
    frontier = util.PriorityQueue()

    start_state = problem.getStartState()
    reached.append(start_state)

    for s in problem.getSuccessors(start_state):
        new_state = (s[0], [s[1]], s[2])
        
        frontier.push(new_state, s[2]+heuristic(s[0], problem))

    while not frontier.isEmpty():
        current_state = frontier.pop()
        current_cost = current_state[2]
        solution_path = current_state[1]

        if current_state[0] not in reached:
            reached.append(current_state[0])

            if problem.isGoalState(current_state[0]):
                print("Goal found!")
                print(current_state[1])
                return current_state[1]

            else:
                # get the successors and add to frontier
                
                for s in problem.getSuccessors(current_state[0]):
                    node = s[0]
                    direction = [s[1]]
                    cost = s[2]
                    new_path = solution_path + direction
                    new_cost =  current_cost + cost 
                    new_state = (node, new_path, new_cost)
                    frontier.push(new_state, new_cost + heuristic(node, problem)) # combining cost and heuristic here
    else:
        print('Frontier is empty!')

    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
