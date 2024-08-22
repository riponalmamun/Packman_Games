# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    """
    stack = util.Stack()  # Initialize the stack for DFS
    visited = set()  # Set to track visited nodes
    start_state = problem.getStartState()  # Get the starting state
    stack.push((start_state, []))  # Push the start state and an empty path onto the stack
    print(f"Start State: {start_state}")
    while not stack.isEmpty():
        state, path = stack.pop()  # Pop the state and path from the stack

        if problem.isGoalState(state):  # Check if the state is the goal
            return path  # Return the path to the goal

        if state not in visited:  # If the state has not been visited
            visited.add(state)  # Mark it as visited
            for successor, action, _ in problem.getSuccessors(state):
                if successor not in visited:
                  stack.push((successor, path + [action]))  # Push the successor and updated path onto the stack

    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    queue = util.Queue()  # Initialize the queue for BFS
    visited = set()  # Set to track visited nodes
    start_state = problem.getStartState()  # Get the starting state
    queue.push((start_state, []))  # Push the start state and an empty path onto the queue

    while not queue.isEmpty():
        state, path = queue.pop()  # Pop the first state and path from the queue

        if problem.isGoalState(state):  # Check if the state is the goal
            return path  # Return the path to the goal

        if state not in visited:  # If the state has not been visited
            visited.add(state)  # Mark it as visited
            for successor, action, _ in problem.getSuccessors(state):
                if successor not in visited:
                    queue.push((successor, path + [action]))  # Push the successor and updated path onto the queue

    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    priority_queue = util.PriorityQueue()  # Initialize the priority queue for UCS
    visited = set()  # Set to track visited nodes
    start_state = problem.getStartState()  # Get the starting state
    priority_queue.push((start_state, []), 0)  # Push the start state with a priority of 0

    while not priority_queue.isEmpty():
        state, path = priority_queue.pop()  # Pop the node with the lowest cost

        if problem.isGoalState(state):  # Check if the state is the goal
            return path  # Return the path to the goal

        if state not in visited:  # If the state has not been visited
            visited.add(state)  # Mark it as visited
            for successor, action, step_cost in problem.getSuccessors(state):
                if successor not in visited:
                    total_cost = problem.getCostOfActions(path + [action])
                    priority_queue.push((successor, path + [action]), total_cost)  # Push the successor with its total cost

    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    priority_queue = util.PriorityQueue()  # Initialize the priority queue for A*
    visited = set()  # Set to track visited nodes
    start_state = problem.getStartState()  # Get the starting state
    priority_queue.push((start_state, []), 0)  # Push the start state with initial cost

    while not priority_queue.isEmpty():
        state, path = priority_queue.pop()  # Pop the node with the lowest combined cost

        if problem.isGoalState(state):  # Check if the state is the goal
            return path  # Return the path to the goal

        if state not in visited:  # If the state has not been visited
            visited.add(state)  # Mark it as visited
            for successor, action, step_cost in problem.getSuccessors(state):
                if successor not in visited:
                    total_cost = problem.getCostOfActions(path + [action]) + heuristic(successor, problem)
                    priority_queue.push((successor, path + [action]), total_cost)  # Push the successor with its total cost

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
