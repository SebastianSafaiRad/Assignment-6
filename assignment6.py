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
        curr_node = self.graph.addVertex(self.getContainerContents())
        done = False
        while not done:
            pass


    def getContainerContents(self):
        return self.container_a.getCurrVolume() + "," + self.container_b.getCurrVolume()

    def bfSearch(self, graph):
        pass

    def pour(self, a, b):
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


if __name__ == '__main__':

    g = Graph()
    node = g.addVertex("0,0")

    print(node.getId())
