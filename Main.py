from AstarSearchImplementor import AstarSearchImplementor
from DepthFirstSearchImplementor import DepthFirstSearchImplementor
from Maze import Maze

AStarMaze = []
originalMaze = Maze()
dfsSearch = DepthFirstSearchImplementor(originalMaze)
dfsSearch.DFSSearch()

print("\n\n")
AstarSearch = AstarSearchImplementor(originalMaze)
AstarSearch.AStarSearch()
