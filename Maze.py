import random


class Maze:
    # Data structure that stores maze node related data
    mazeNodes = [[[y + x * 6, x, y, None, 0, 0] for x in range(6)] for y in range(6)]
    startPosition = []
    goalPosition = []

    def __init__(self):
        self.generateMaze()
        print(self.mazeNodes)

    def generateMaze(self):
        self.generateStartingNode()
        self.generateGoalNode()
        self.generateBarrierNode()

    def generateNode(self, startNode, endNode, nodeState):
        cellNumber = random.randint(startNode, endNode)
        X_Position = cellNumber // 6
        Y_Position = cellNumber % 6

        if nodeState == "Start":
            self.mazeNodes[Y_Position][X_Position][3] = "Start"
        elif nodeState == "Goal":
            self.mazeNodes[Y_Position][X_Position][3] = "Goal"
        else:
            self.mazeNodes[Y_Position][X_Position][3] = "Barrier"
        return [X_Position, Y_Position]

    def generateStartingNode(self):
        self.startPosition = self.generateNode(0, 11, "Start")

    def generateGoalNode(self):
        self.goalPosition = self.generateNode(24, 35, "Goal")

    def generateBarrierNode(self):
        for count in range(0, 4):
            while True:
                cellNumber = random.randint(0, 35)
                X_Position = cellNumber // 6
                Y_Position = cellNumber % 6
                if self.mazeNodes[Y_Position][X_Position][3] is None:
                    self.mazeNodes[Y_Position][X_Position][3] = "Barrier"
                    break
