from graph import Graph
from graph import Vertex
from queue2050 import Queue
import math
import unittest


class assignment6:

    def __init__(self):
        """Constructor for this class"""
        self.container_a = None
        self.container_b = None
        self.goal_amount = None
        self.rootNodeState = "0,0"
        self.graph = Graph()
        self.q = Queue()

    def findsolution(self, a, b, goal_amount):
        """Takes input of amount to store in container a and container b and the goal amount.
        Then it prints out the solution path"""
        self.container_a = Container(a)
        self.container_b = Container(b)
        self.goal_amount = str(goal_amount)
        if goal_amount % math.gcd(a, b) == 0:
            self.buildGraph2()
            return self.printResults(self.bfSearch())
        else:
            print("There is no solution")

    def getEligibleStates(self, a, b, curr_state):
        """Takes input of amount to store in container a and container b.  Takes the current state
        and prints out all of the possible states from the current state"""
        self.container_a = Container(a)
        self.container_b = Container(b)
        self.rootNodeState = curr_state
        self.buildGraph2()
        stateList = []
        for vertex in self.graph.getVertices():
            stateList.append(vertex)
            # print(vertex)
        return stateList

    def buildGraph2(self):
        """Builds the graph"""
        self.q.enqueue(self.establishRootVertex())
        while self.q.size() > 0:
            parentVertex = self.q.dequeue()
            parentStateString = parentVertex.getId()

            self.resetContainers(parentStateString)
            if not self.container_a.isFull():
                self.container_a.fill()
                self.addToQueue(self.addEdge(parentStateString, self.getStateString()))
                self.resetContainers(parentStateString)

            if not self.container_b.isFull():
                self.container_b.fill()
                self.addToQueue(self.addEdge(parentStateString, self.getStateString()))
                self.resetContainers(parentStateString)

            if self.canPour(self.container_a, self.container_b):
                self.pour(self.container_a, self.container_b)
                self.addToQueue(self.addEdge(parentStateString, self.getStateString()))
                self.resetContainers(parentStateString)

            if self.canPour(self.container_b, self.container_a):
                self.pour(self.container_b, self.container_a)
                self.addToQueue(self.addEdge(parentStateString, self.getStateString()))
                self.resetContainers(parentStateString)


    def resetContainers(self, containersState):
        """Resets the containers back to the container state"""
        # containerState is a two-element csv string.  e.g. "0,3"
        self.container_a.setCurrVolume(int(containersState.split(",")[0]))
        self.container_b.setCurrVolume(int(containersState.split(",")[1]))

    def establishRootVertex(self):
        """Creates the root vertwex"""
        self.graph.addVertex(self.rootNodeState)
        v = self.graph.getVertex(self.rootNodeState)
        v.setDistance(0)
        return v

    def getStateString(self):
        """Returns the container settings a string"""
        return str(self.container_a.getCurrVolume()) + "," + str(self.container_b.getCurrVolume())

    def addEdge(self, parent, child):
        """Connects two nodes/vertices"""
        # by design, the parent vertex will always exist on the graph
        # if the child exists already, return None
        parentVertex = self.graph.getVertex(parent)
        childVertex = Vertex(None)
        if self.graph.getVertex(child) is None:
            self.graph.addEdge(parent, child)
            childVertex = self.graph.getVertex(child)
            childVertex.setDistance(parentVertex.getDistance() + 1)
            childVertex.setPred(parentVertex)
            return childVertex

        return None

    def addToQueue(self, newVertex):
        """Adds the new vertex to the queue"""
        if newVertex is None:
            pass
        else:
            self.q.enqueue(newVertex)

    def bfSearch(self):
        """Performs a Breatdh First Search"""
        queue = Queue()
        rootVertex = self.graph.getVertex(self.rootNodeState)
        queue.enqueue(rootVertex)

        while not queue.isEmpty():
            currentVertex = queue.dequeue()
            if self.isSolutionVertex(currentVertex):
                return currentVertex
            else:
                childVertices = currentVertex.getConnections()
                for vertex in childVertices:
                    queue.enqueue(vertex)

        print("Solution not found")

    def pour(self, source, destination):
        """Pours from one container to another"""
        maxAmountToPour = destination.max_volume - int(destination.curr_volume)
        if source.curr_volume <= maxAmountToPour:
            destination.curr_volume = destination.curr_volume + source.curr_volume
            source.curr_volume = 0
        else:
            source.curr_volume = source.curr_volume - maxAmountToPour
            destination.curr_volume = destination.curr_volume + maxAmountToPour

    def canPour(self, source, destination):
        """Determines whether or not there is room to pour"""
        if source.isEmpty():
            return False
        elif destination.isFull():
            return False
        else:
            return True

    def isSolutionVertex(self, currentVertex):
        """Determines whether the current vertex is part of the solution"""
        if self.goal_amount in currentVertex.getId():
            return True
        else:
            return False

    def printResults(self, vertex):
        """Reverses the order of how the list is printed.  Prints from root node to bottom child node"""
        printList = []
        currentVertex = vertex
        printList.insert(0, currentVertex.getId())
        while currentVertex.getPred() is not None:
            currentVertex = currentVertex.getPred()
            printList.insert(0, currentVertex.getId())
        # for item in printList:
        #   print(item)
        return printList


class Container:
    max_volume = 0
    curr_volume = 0

    def __init__(self, max_volume):
        """Constructor for Container class"""
        self.max_volume = max_volume

    def fill(self):
        """Fills the containers with the maximum amount possible"""
        self.curr_volume = self.max_volume

    def getCurrVolume(self):
        """returns the volume of the container"""
        return self.curr_volume

    def getMaxVolume(self):
        """Determines the maximum amount of volume in the container"""
        return self.max_volume

    def setCurrVolume(self, volume):
        """Setting the current volume of the container to the input"""
        self.curr_volume = volume

    def isFull(self):
        """Determines if the container is full and whether or not can be poured into"""
        if self.curr_volume == self.max_volume:
            return True
        else:
            return False

    def isEmpty(self):
        """Determines whether the container is empty and if it can be poured into"""
        if self.curr_volume == 0:
            return True
        else:
            return False


class TestHashTable(unittest.TestCase):
    """Test Class to test some methods"""

    def testFindSolution(self):
        """Tests the FindSolution method"""
        a1 = assignment6()
        a2 = assignment6()
        fsList = ['0,0', '3,0', '0,3', '3,3', '2,4']
        self.assertEqual(a1.findsolution(3, 4, 2), fsList)
        self.assertNotEqual(a2.findsolution(3, 4, 3), fsList)

    def testGetEligibleStates(self):
        """Tests the getEligibleStates method"""
        a3 = assignment6()
        a4 = assignment6()
        gesList = ['3,0', '3,4', '0,3', '3,3', '0,4', '2,4', '3,1']
        gesList2 = ['4,0', '3,0', '4,4', '0,4', '3,4', '0,3', '3,5', '3,1', '3,3', '2,4']
        self.assertEqual(a3.getEligibleStates(3, 4, "3,0"), gesList)
        self.assertNotEqual(a4.getEligibleStates(3, 4, "4,0"), gesList)
        self.assertEqual(a4.getEligibleStates(3, 4, "4,0"), gesList2)
        self.assertNotEqual(a4.getEligibleStates(3, 4, "5,3"), gesList2)


def main():
    """Main Method"""
    a6 = assignment6()
    print(a6.findsolution(3, 4, 2))
    print(a6.getEligibleStates(3, 4, "4,0"))
    # a6.findsolution(3, 4, 2)
    # g = Graph()
    # g.addVertex("0,0")
    # v0 = g.getVertex("0,0")
    # v0.setDistance(0)
    # g.addEdge("0,0", "3,0")
    # v = g.getVertex("3,0")
    # print(v.getId())
    # v.setDistance(1)
    # v.setPred(v0)
    # print(g.getVertices())


def unittest_main():
    unittest.main()


if __name__ == '__main__':
    main()
    unittest_main()

    # g = Graph()
    # g.addVertex("0,0")
    # v0 = g.getVertex("0,0")
    # v0.setDistance(0)
    # g.addEdge("0,0", "3,0")
    # v = g.getVertex("3,0")
    # print(v.getId())
    # v.setDistance(1)
    # v.setPred(v0)
    # print(g.getVertices())
