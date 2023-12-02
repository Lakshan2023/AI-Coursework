class AstarSearchImplementor:
    visited = []

    def __init__(self, maze):
        self.maze = maze
        self.maze.mazeNodes = self.getTheInitialMaze()
        self.GoalNode = self.maze.mazeNodes[self.maze.goalPosition[1]][self.maze.goalPosition[0]]
        self.calculateHeuristicCost()
        startingPoint = self.maze.mazeNodes[self.maze.startPosition[1]][self.maze.startPosition[0]]
        startingPoint[5] = startingPoint[4]
        self.visited.append(startingPoint)

    def AStarSearch(self):
        print(self.maze.mazeNodes)
        self.AStarTraverse()
        print("\n\n", self.visited)

    def AStarTraverse(self):
        cost = 0
        while not (self.stateExistCondition(self.visited[-1])):
            cost += 1
            self.getNeighbourNodes(self.visited[-1][1], self.visited[-1][2], cost)

    def getNeighbourNodes(self, X_position, Y_position, cost):
        neighbourDirections = [[1, 0], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1], [-1, 0], [0, -1]]
        achievableNeighbours = []
        for index in neighbourDirections:
            newXPosition = X_position + index[0]
            newYPosition = Y_position + index[1]

            if newXPosition not in [-1, 6] and newYPosition not in [-1, 6]:
                newNode = self.maze.mazeNodes[newYPosition][newXPosition]
                if newNode not in self.visited:
                    if newNode[3] not in ["Barrier"]:
                        newNode[5] = newNode[4] + cost
                        achievableNeighbours.append(newNode)
        sortedNeighborList = self.sortNeighbourList(achievableNeighbours)
        self.visited.append(sortedNeighborList[0])
        print(sortedNeighborList)

    def sortNeighbourList(self, ListToBeSorted):
        for count in range(0, len(ListToBeSorted) - 1):
            for index in range(len(ListToBeSorted) - 1):
                if ListToBeSorted[index][5] > ListToBeSorted[index + 1][5]:
                    temp = ListToBeSorted[index]
                    ListToBeSorted[index] = ListToBeSorted[index + 1]
                    ListToBeSorted[index + 1] = temp
                if ListToBeSorted[index][5] == ListToBeSorted[index + 1][5]:
                    if ListToBeSorted[index][1] > ListToBeSorted[index + 1][1]:
                        temp = ListToBeSorted[index]
                        ListToBeSorted[index] = ListToBeSorted[index + 1]
                        ListToBeSorted[index + 1] = temp

        return ListToBeSorted

    def calculateHeuristicCost(self):
        for index in self.maze.mazeNodes:
            for value in index:
                value[4] = abs(value[1] - self.GoalNode[1]) + abs(value[2] - self.GoalNode[2])

    def getTheInitialMaze(self):
        initialMaze = []
        for index in self.maze.mazeNodes:
            innerNodes = []
            for values in index:
                if values[3] in ["Visited", "Blocked"]:
                    values[3] = None
                innerNodes.append(values)
            initialMaze.append(innerNodes)
        return initialMaze

    def stateExistCondition(self, state):
        if state == self.GoalNode:
            return True
        else:
            return False
