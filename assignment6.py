from graph import Graph
import queue2050


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
        self.graph.addVertex(self.getContainerContents())


    def getContainerContents(self):
        return self.container_a.getCurrVolume() + "," + self.container_b.getCurrVolume()


    def bfSearch(self, graph):
        pass

    def fill():
        pass

    def pour(a, b):
        pass


class Container:
    max_volume = 0
    curr_volume = 0

    def __init__(self, max_volume):
        self.max_volume = max_volume

    def fill(self):
        pass

    def pour(self):
        pass

    def getCurrVolume(self):
        return self.curr_volume

    def getMaxVolume(self):
        return self.max_volume

if __name__ == '__main__':
 pass

