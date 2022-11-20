# Graphics Playground

Boot.dev personal project this "graphics playground" will
incorporate the maze solver and then add other cool graphic
demos like strange attractors 

### Technologies:
- Python
- Poetry

### Dependencies:
- Pygame

### Dev Dependencies:
- mypy (linter)
- black (formatter)

## Demos

### Maze Solver

### Mandelbrot
    This application features a mandelbrot demo which can be customised using hotkeys
    to change the number of iterations and exponent used in the equation.

    ![Mandelbrot Set](https://github.com/Alextibtab/graphics-playground/raw/master/examples/mandelbrot/mandelbrot.jpg)

    #### Hotkeys
    You can use the - and + keys to decrease or increase the amount of iterations
    To swap between modifying the iterations or exponent press 'i' which will swap
    the value you are editing.
    To regenerate the mandelbrot with tweaked parameters press the enter key.
    To view the julia set for a certain point on the mandelbrot simply left
    click on the desired point and wait for the julia set to generate.

    ![Julia Set](https://github.com/Alextibtab/graphics-playground/raw/master/examples/mandelbrot/julia_set_1.png)

### Attractors

### Planned Features:
- Menu state system to support multiple windows and switching between them
- Start screen where you can select the different demos

### Advanced Goals:
- A* pathfinding implemented in the maze solver
- pretty start screen with random mini demo each time the app launches
