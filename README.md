# GAME OF LIFE
- Played in 2D
- Run computations on a set of cells on a grid to generate a new generation
- Each cell has a state, alive or dead, 0 or 1
- For each generation, evaluate each cell one by one and get a new state based on previous state and it's neighbours (8 cells surrounding it)
- Decide whether cell should stay as a 0 or 1 and turn into the other

## Rules
- Any live cell with fewer than 2 live neighbours dies
- Any live cell with 2 or 3 live neighbours lives on to the next generation
- Any live cell with more than 3 live neighbours dies
- Any dead cell with exactly 3 live neighbours becomes a live cell