# Documentation

Maze Runner is a maze game based on `Turtle` module.

# General concept

The algorithm used in this game is `Recursive Backtracker Maze Generation`.

It's implementation goes like:

	We start at a random cell, mark the current cell as visited, and get a list of its neighbors.
    For each neighbor, starting with a randomly selected neighbor,
    if that neighbor hasn't been visited, we remove the wall between this cell and that neighbor, 
    and then recurse with that neighbor as the current cell.

# Authors

1) Aakash Khanal
2) Bibek Chand
3) Bigyan Dahal
4) Manish Gyawali