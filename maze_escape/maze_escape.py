# Create a Maze Escape game, where the 'robot' finds the exit on its own
# Make a 5x5 maze
# O will mark the goal, $ = player

maze_grid: list = [
    ['X', ' ', 'X', 'O', ' '],
    [' ', 'X', 'X', ' ', 'X'],
    [' ', 'X', 'X', ' ', 'X'],
    [' ', ' ', ' ', ' ', 'X'],
    [' ', 'X', ' ', 'X', 'X'],
]
# Hardcode for testing
start_coords_x: int = 4
start_coords_y: int = 2


# Print like this to make the layout look correct in terminal
def display_maze():
    for maze in maze_grid:
        print(maze)


# Add the player icon to the start position
def initialize_player():
    maze_grid[start_coords_x][start_coords_y] = "$"
    print("Player Added")


initialize_player()
display_maze()
