## Hints to look for in questions to solve using graph theory:

| Question Mentions | Likely Tool |
| ---------------- | ------------ |
Shortest path | BFS
All possible transformations | BFS/DFS
Reachability| BFS/DFS
Islands, regions, grids | Graphs (DFS/BFS, Union-Find)
Build order / dependencies | Topological Sort (DAG)
Optimizing cost | Dijkstra / Bellman-Ford
Components, cycles | DFS, Union-Find
Transitions between valid states  | Graph


## Flowchart:
```
Start
 │
 ├── Is the problem about finding the shortest path?
 │    ├── Unweighted graph? → Use BFS
 │    └── Weighted graph?
 │         ├── All weights positive? → Dijkstra
 │         └── Some weights negative? → Bellman-Ford
 │
 ├── Do you need to check if one state can reach another?
 │    └── Use BFS or DFS
 │
 ├── Are you detecting cycles or traversing all paths?
 │    └── Use DFS (backtracking)
 │
 ├── Does the problem involve merging sets/groups?
 │    └── Use Union-Find
 │
 ├── Is it about ordering tasks with dependencies?
 │    └── Use Topological Sort
 │
 └── Is the input a grid or board (2D movement)?
      └── Treat as a graph → Use BFS or DFS

```