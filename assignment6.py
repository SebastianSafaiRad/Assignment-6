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
        vertexValueDict = {}
        nextVertexId = 0
        self.graph.addVertex(0)
        vertexValueDict[0] = "0,0"
        q.enqueue(self.graph.getVertex(0))
        while not q.isEmpty():
            currVertex = q.dequeue()
            currVertexValue = vertexValueDict[currVertex.getId()]
            idList = currVertexValue.split(",")
            self.container_a.setCurrVolume(int(idList[0]))
            self.container_b.setCurrVolume(int(idList[1]))
            if not self.container_a.isFull():
                self.container_a.fill()
                newState = str(self.container_a.getCurrVolume()) + "," + idList[1]
                if newState not in vertexValueDict.values():
                    nextVertexId += 1
                    vertexValueDict[nextVertexId] = newState
                    self.graph.addEdge(currVertex.getId(), nextVertexId)
                    q.enqueue(self.graph.getVertex(nextVertexId))
                    self.container_a.setCurrVolume(int(idList[0]))
            if not self.container_b.isFull():
                self.container_b.fill()
                newState = idList[0] + "," + str(self.container_b.getCurrVolume())
                if newState not in vertexValueDict.values():
                    nextVertexId += 1
                    vertexValueDict[nextVertexId] = newState
                    self.graph.addEdge(currVertex.getId(), nextVertexId)
                    q.enqueue(self.graph.getVertex(nextVertexId))
                    self.container_b.setCurrVolume(int(idList[1]))
            if self.canPour(self.container_a, self.container_b):
                self.pour(self.container_a, self.container_b)
                newState = str(self.container_a.getCurrVolume()) + "," + str(self.container_b.getCurrVolume())
                if newState not in vertexValueDict.values():
                    nextVertexId += 1
                    vertexValueDict[nextVertexId] = newState
                    self.graph.addEdge(currVertex.getId(), nextVertexId)
                    q.enqueue(self.graph.getVertex(nextVertexId))
                    self.container_a.setCurrVolume(int(idList[0]))
            if self.canPour(self.container_b, self.container_a):
                self.pour(self.container_b, self.container_a)
                newState = str(self.container_a.getCurrVolume()) + "," + str(self.container_b.getCurrVolume())
                if newState not in vertexValueDict.values():
                    nextVertexId += 1
                    vertexValueDict[nextVertexId] = newState
                    self.graph.addEdge(currVertex.getId, nextVertexId)
                    q.enqueue(self.graph.getVertex(nextVertexId))
                    self.container_b.setCurrVolume(int(idList[1]))
                    
        print("Done with graph")

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

