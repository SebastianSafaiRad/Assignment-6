from graph import Graph
from graph import Vertex
from queue2050 import Queue
import math


class assignment6:

    def __init__(self):
        self.container_a = None
        self.container_b = None
        self.goal_amount = None
        self.rootNodeState = "0,0"
        self.graph = Graph()
        self.q = Queue()

    def findsolution(self, a, b, goal_amount):
        self.container_a = Container(a)
        self.container_b = Container(b)
        self.goal_amount = str(goal_amount)
        if goal_amount % math.gcd(a, b) == 0:
            self.buildGraph2()
            self.printResults(self.bfSearch())
        else:
            print("There is no solution")

    def getEligibleStates(self, a, b, curr_state):
        pass

    def buildGraph2(self):
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

        #self.printGraph()

    def resetContainers(self, containersState):
        # containerState is a two-element csv string.  e.g. "0,3"
        self.container_a.setCurrVolume(int(containersState.split(",")[0]))
        self.container_b.setCurrVolume(int(containersState.split(",")[1]))

    def establishRootVertex(self):
        self.graph.addVertex(self.rootNodeState)
        v = self.graph.getVertex(self.rootNodeState)
        v.setDistance(0)
        return v

    def getStateString(self):
        return str(self.container_a.getCurrVolume()) + "," + str(self.container_b.getCurrVolume())

    def addEdge(self, parent, child):
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
        if newVertex is None:
            pass
        else:
            self.q.enqueue(newVertex)

    def bfSearch(self):
        queue = Queue()
        rootVertex = self.graph.getVertex(self.rootNodeState)
        queue.enqueue(rootVertex)

        while not queue.isEmpty():
            currentVertex = queue.dequeue()
            if self.isSolutionVertex(currentVertex):
                print("BFS Search Output: ", currentVertex)
                return currentVertex
            else:
                childVertices = currentVertex.getConnections()
                for vertex in childVertices:
                    queue.enqueue(vertex)

        print("Solution not found")

    def pour(self, source, destination):
        maxAmountToPour = destination.max_volume - int(destination.curr_volume)
        if source.curr_volume <= maxAmountToPour:
            destination.curr_volume = destination.curr_volume + source.curr_volume
            source.curr_volume = 0
        else:
            source.curr_volume = source.curr_volume - maxAmountToPour
            destination.curr_volume = destination.curr_volume + maxAmountToPour

    def canPour(self, source, destination):
        if source.isEmpty():
            return False
        elif destination.isFull():
            return False
        else:
            return True

    def isSolutionVertex(self, currentVertex):
        if self.goal_amount in currentVertex.getId():
            return True
        else:
            return False

    def printGraph(self):
        verts = self.graph.getVertices()
        print("all vertices : ", verts)
        for vid in verts:
            vert = self.graph.getVertex(vid)
            pred = "N/A" if vert.getPred() is None else vert.getPred().getId()
            print("vertex ID: ", vert.getId(), "   Parent : ", pred, "   Distance : ", vert.getDistance())

    def printResults(self, vertex):
        
        pass


class Container:
    max_volume = 0
    curr_volume = 0

    def __init__(self, max_volume):
        self.max_volume = max_volume

    def fill(self):
        self.curr_volume = self.max_volume

    def getCurrVolume(self):
        return self.curr_volume

    def getMaxVolume(self):
        return self.max_volume

    def setCurrVolume(self, volume):
        self.curr_volume = volume

    def isFull(self):
        if self.curr_volume == self.max_volume:
            return True
        else:
            return False

    def isEmpty(self):
        if self.curr_volume == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    a6 = assignment6()
    a6.findsolution(3, 4, 2)

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
