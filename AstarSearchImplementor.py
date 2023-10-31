class AstarSearchImplementor:

    def __init__(self, maze):
        self.maze = maze
        self.AstarMaze = self.getTheInitialMaze()

    def AStarSearch(self):
        print(self.AstarMaze)

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
