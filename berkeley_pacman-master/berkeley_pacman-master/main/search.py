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

from builtins import object
from concurrent.futures import process
from re import L
import util


class SearchProblem(object):
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
    return [s, s, w, s, w, w, s, w]


                
            # if not visitedQueue.check(succState[0]):
            #     pathStack.push(succState[0])
            #     visitedQueue.push(succState[0])
            #     recursiveFunction(problem, visitedQueue, pathStack, succState[0])
    

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    pathStack = util.Stack()
    visitedNodes = []
    
    startNode = problem.getStartState()
    pathStack.push((startNode, []))
    visitedNodes.append(startNode)

    if pathStack.isEmpty() or problem.isGoalState(startNode):
        return []
    currNode, currPath = pathStack.pop()
    while not problem.isGoalState(currNode):
        for succNode, action, cost in problem.getSuccessors(currNode):
            if succNode not in visitedNodes:
                visitedNodes.append(succNode)
                pathStack.push((succNode, currPath + [action]))
        currNode, currPath = pathStack.pop()
    
    return currPath

   
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    pathQueue = util.Queue()
    visitedNodes = []

    startNode = problem.getStartState()
    pathQueue.push((startNode, []))
    visitedNodes.append(startNode)

    if pathQueue.isEmpty() or problem.isGoalState(startNode):
        return []
    
    currNode, currPath = pathQueue.pop()
    while not problem.isGoalState(currNode):
        for succNode, action, cost in problem.getSuccessors(currNode):
            if succNode not in visitedNodes:
                visitedNodes.append(succNode)
                pathQueue.push((succNode, currPath + [action]))
        currNode, currPath = pathQueue.pop()

    return currPath

    "*** YOUR CODE HERE ***"

    # util.raiseNotDefined()

def remove(list, currNode):
    for node, path in list:
        if node == currNode:
            list.remove((node, path))
            
def get(list, currNode):
    for node, path in list:
        if node == currNode:
            return path



def uniformCostSearch(problem, heuristic=None):
    """Search the node of least total cost first."""
    
    
    pathPriorityQueue = util.PriorityQueue()
    visitedNodes = []
    pathList = []
    startNode = problem.getStartState()
    priority = 0
    pathPriorityQueue.push(startNode, priority)
    visitedNodes.append(startNode)
    pathList.append((startNode, []))
    if pathPriorityQueue.isEmpty() or problem.isGoalState(startNode):
        return []
    
    priority, _, currNode = pathPriorityQueue.pop()
    currPath = []
    for node, path in pathList:
        if node == currNode:
            currPath = path

    while not problem.isGoalState(currNode):
        for succNode, action, cost in problem.getSuccessors(currNode):
            if succNode not in visitedNodes:
                visitedNodes.append(succNode)
                pathPriorityQueue.push(succNode, priority + cost)
                pathList.append((succNode, currPath + [action]))
            else:
                pathPriorityQueue.update(succNode, priority + cost)
                for node, path in pathList:
                    if node == succNode:
                        pathList.remove((node, path))
                pathList.append((succNode, currPath + [action]))
        priority, _, currNode = pathPriorityQueue.pop() 
        currPath = get(pathList, currNode)
    return currPath
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
