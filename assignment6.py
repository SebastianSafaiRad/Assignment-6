from graph import Graph
from graph import Vertex
from queue2050 import Queue


class assignment6:

    def __init__(self, a_volume, b_volume, goal_amount):
        self.container_a = Container(a_volume)
        self.container_b = Container(b_volume)
        self.goal_amount = goal_amount
        self.graph = Graph()

    def findsolution(self, a, b, goal_amount):
        return self.bfSearch(self.buildGraph())

    def getEligibleStates(self, a, b, curr_state):
        pass

    def buildGraph(self):
        q = Queue
        q.enqueue(self.graph.addVertex("0,0"))
        while not q.isEmpty():
            curr_node = q.dequeue()
            nodeid = curr_node.getId()
            idList = nodeid.split(",")
            self.container_a.setCurrVolume(int(idList[0]))
            self.container_b.setCurrVolume(int(idList[1]))
            if not self.container_a.isFull():
                self.container_a.fill()
                newVertex = Vertex(self.container_a.getCurrVolume() + "," + idList[1])
                self.graph.addEdge(curr_node, newVertex)
                q.enqueue(newVertex)
                self.container_a.setCurrVolume(idList[0])
            if not self.container_b.isFull():
                self.container_b.fill()
                newVertex = Vertex(idList[0] + "," + self.container_b.getCurrVolume())
                self.graph.addEdge(curr_node, newVertex)
                q.enqueue(newVertex)
                self.container_b.setCurrVolume(idList[1])
            if self.canPour(self.container_a, self.container_b):




    def bfSearch(self, graph):
        pass

    def pour(self, source, destination):
        


    def canPour(self, source, destination):
        if source.isEmpty():
            return False
        elif destination.isFull():
            return False
        else:
            return True


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
        self.v = volume

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
    g = Graph()
    node = g.addVertex("0,0")

    print(node.getId())
