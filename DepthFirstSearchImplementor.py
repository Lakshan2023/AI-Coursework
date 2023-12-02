from FrontierStack import FrontierStack


class DepthFirstSearchImplementor:
    visited = []
    fullVisitedList = []
    finalPath = []

    def __init__(self, maze):
        self.maze = maze
        self.Stack = FrontierStack()
        self.GoalNode = self.maze.mazeNodes[self.maze.goalPosition[1]][self.maze.goalPosition[0]]

    def DFSSearch(self):
        self.Stack.addNode(self.maze.mazeNodes[self.maze.startPosition[1]][self.maze.startPosition[0]])
        self.traverseNodes()
        print(self.visited)
        self.printAllVisitedNodeList()
        self.calculateTime()
        self.displayFinalPath()

    def traverseNodes(self):
        while not self.Stack.isMazeStackEmpty():
            print(self.Stack.mazeStack)
            popNode = self.Stack.removeNode()
            self.fullVisitedList.append(popNode[0])
            if self.maze.mazeNodes[popNode[2]][popNode[1]][3] not in ["Start", "Goal", "Blocked"]:
                self.maze.mazeNodes[popNode[2]][popNode[1]][3] = "Visited"
            if self.stateExistCondition(popNode):
                self.visited.append(popNode)
                return self.visited
            if popNode not in self.visited:
                self.visited.append(popNode)
            self.getNeighbourNodes(popNode[1], popNode[2], "Traverse")

        print("There is no solution !!!")
        return None

    def getNeighbourNodes(self, X_position, Y_position, status):
        neighbourDirections = [[1, 0], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1], [-1, 0], [0, -1]]
        achievableNeighbours = []
        for index in neighbourDirections:
            newXPosition = X_position + index[0]
            newYPosition = Y_position + index[1]

            if newXPosition not in [-1, 6] and newYPosition not in [-1, 6]:
                if self.maze.mazeNodes[newYPosition][newXPosition][3] not in ["Barrier", "Blocked"]:
                    achievableNeighbours.append(self.maze.mazeNodes[newYPosition][newXPosition])
        sortedNeighborList = self.sortNeighborNodeList(achievableNeighbours)

        if status == "Traverse":
            if self.checkAllNeighboursVisited(sortedNeighborList):
                self.backTrackMaze()

            else:
                for value in sortedNeighborList:
                    if value not in self.visited:
                        self.Stack.addNode(value)
            return None
        else:
            return sortedNeighborList

    def backTrackMaze(self):
        for index in range(len(self.visited) - 1, -1, -1):
            poppedNode = self.visited[index]
            previousNode = self.visited[index - 1]
            if poppedNode[3] == "Visited" and poppedNode != self.GoalNode:
                self.maze.mazeNodes[poppedNode[2]][poppedNode[1]][3] = "Blocked"
                self.fullVisitedList.append(poppedNode[0])
                previousNodeNeighbours = self.getNeighbourNodes(previousNode[1], previousNode[2], "Backtrack")
                filteredPreviousNodeNeighbours = [node for node in previousNodeNeighbours if node[3] in ["Start", "Goal","Start"]]

                if len(filteredPreviousNodeNeighbours) != 0:
                    print(previousNode, "fp", filteredPreviousNodeNeighbours)
                    self.Stack.addNode(filteredPreviousNodeNeighbours[-1])
                    break

    def checkAllNeighboursVisited(self, neighbor_list):
        for index in neighbor_list:
            if index[3] not in ["Visited", "Start"]:
                return False
        return True

    def sortNeighborNodeList(self, ListToBeSorted):
        for count in range(0, len(ListToBeSorted) - 1):
            for index in range(len(ListToBeSorted) - 1):
                if ListToBeSorted[index][0] < ListToBeSorted[index + 1][0]:
                    temp = ListToBeSorted[index]
                    ListToBeSorted[index] = ListToBeSorted[index + 1]
                    ListToBeSorted[index + 1] = temp
        return ListToBeSorted

    def stateExistCondition(self, state):
        if state == self.GoalNode:
            return True
        else:
            return False

    def printAllVisitedNodeList(self):
        index = 0
        while index < len(self.fullVisitedList) - 1:
            if self.fullVisitedList[index] == self.fullVisitedList[index + 1]:
                self.fullVisitedList.pop(index)
            else:
                index += 1

        print(self.fullVisitedList)

    def displayFinalPath(self):
        for index in self.visited:
            if index[3] != "Blocked":
                self.finalPath.append(index[0])
        print("final Path :", self.finalPath)

    def calculateTime(self):
        spentTime = (len(self.visited) - 1) * 1
        print("Spent time = {} minutes".format(spentTime))
