class FrontierStack:
    def __init__(self):
        self.mazeStack = []

    def addNode(self, addingNode):
        self.mazeStack.append(addingNode)

    def isMazeStackEmpty(self):
        return len(self.mazeStack) == 0

    def removeNode(self):
        if self.isMazeStackEmpty():
            print("Empty Maze Stack")
        else:
            node = self.mazeStack[-1]
            self.mazeStack = self.mazeStack[:-1]
            return node
