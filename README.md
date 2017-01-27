# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Naked Twins technique of dealing with special case, it is a set of exactly two candidates that are in exactly two squares in a row, column, or block. The way to solve this problem with constant propagation approach is to introduce constrain that digits identified as naked twins can be removed out of consideration for any other box within the unit that contains naked twins. Implementation can viewed in a tree steps process:
 - identify presence of naked twins
 - remove digits that correspond to naked twins form any other box of the unit
 - return updated set of values  

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: As diagonal sudoku is a variation of regular sudoku, that among the two main diagonals may contain only single appearance of 1-9 number. The way solve this problem with constraint propagation is to define and introduce corresponding additional constraints. My implementation resulted in forming diag1 and diag2 units that represent two main diagonals and then adding both of them to already existing unitlist. Introduction of this extra constrain allowed existing algorithm to solve the problem. 


### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in function.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.