[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">MazeRunner</h3>

  <p align="center">
    An awesome game based on MazeRunner Trilogy!
  </p>
</p>

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
