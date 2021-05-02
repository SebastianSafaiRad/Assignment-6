from graph import Graph
from graph import Vertex
from queue2050 import Queue
import math


class assignment6:

    def __init__(self, a_volume, b_volume, goal_amount):
        self.container_a = Container(a_volume)
        self.container_b = Container(b_volume)
        self.goal_amount = goal_amount
        self.graph = Graph()

    def findsolution(self, a, b, goal_amount):
        if goal_amount % math.gcd(a, b) == 0:
            self.buildGraph()
            return self.bfSearch()
        else:
            print("There is no solution")

    def getEligibleStates(self, a, b, curr_state):
        pass

    def buildGraph(self):
        q = Queue()
        visited = []
        # root = Vertex("0,0")
        graphVert = self.graph.addVertex("0,0")
        self.graph.addVertex(graphVert)
        # q.enqueue(root)
        q.enqueue(graphVert)
        while not q.isEmpty():
            curr_node = q.dequeue()
            nodeid = curr_node.getId()
            idList = nodeid.split(",")
            self.container_a.setCurrVolume(int(idList[0]))
            self.container_b.setCurrVolume(int(idList[1]))
            if not self.container_a.isFull():
                self.container_a.fill()
                newVertex = Vertex(str(self.container_a.getCurrVolume()) + "," + idList[1])
                if newVertex not in visited:
                    visited.append(newVertex)
                    self.graph.addEdge(curr_node, newVertex)
                    q.enqueue(newVertex)
                    self.container_a.setCurrVolume(int(idList[0]))
            if not self.container_b.isFull():
                self.container_b.fill()
                newVertex = Vertex(idList[0] + "," + str(self.container_b.getCurrVolume()))
                if newVertex not in visited:
                    visited.append(newVertex)
                    self.graph.addEdge(curr_node, newVertex)
                    q.enqueue(newVertex)
                    self.container_b.setCurrVolume(int(idList[1]))
            if self.canPour(self.container_a, self.container_b):
                self.pour(self.container_a, self.container_b)
                newVertex = Vertex(str(self.container_a.getCurrVolume()) + "," + str(self.container_b.getCurrVolume()))
                # if not self.vertexExists(newVertex):
                if newVertex not in visited:
                    visited.append(newVertex)
                    self.graph.addEdge(curr_node, newVertex)
                    q.enqueue(newVertex)
                    self.container_a.setCurrVolume(int(idList[0]))
            if self.canPour(self.container_b, self.container_a):
                self.pour(self.container_b, self.container_a)
                newVertex = Vertex(str(self.container_a.getCurrVolume()) + "," + str(self.container_b.getCurrVolume()))
                # if not self.vertexExists(newVertex):
                if newVertex not in visited:
                    visited.append(newVertex)
                    self.graph.addEdge(curr_node, newVertex)
                    q.enqueue(newVertex)
                    self.container_b.setCurrVolume(int(idList[1]))

    def bfSearch(self):
        queue = Queue()
        rootVertex = self.graph.getVertex("0,0")
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
    obj = assignment6(3, 4, 2)
    print(obj.buildGraph())
    # print(obj.graph)
    # print(obj)
    # print(obj.bfSearch())
    # print(obj.findsolution(3,4,2))

