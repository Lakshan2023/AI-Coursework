from AstarSearchImplementor import AstarSearchImplementor
from DepthFirstSearchImplementor import DepthFirstSearchImplementor
from Maze import Maze

AStarMaze = []
originalMaze = Maze()
dfsSearch = DepthFirstSearchImplementor(originalMaze)
dfsSearch.DFSSearch()

AstarSearch = AstarSearchImplementor(originalMaze)
print("\n\n")
AstarSearch.AStarSearch()
