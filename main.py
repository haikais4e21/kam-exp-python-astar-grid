import sys
from astar import a_star_search

def read_map(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def main():
    if len(sys.argv) != 2:
        print('Usage: python3.12 main.py <path_to_ascii_map_file>')
        sys.exit(1)
    map_file = sys.argv[1]
    grid = read_map(map_file)
    start = (0, 0)
    goal = (len(grid) - 1, len(grid[0]) - 1)
    path = a_star_search(grid, start, goal)
    if path:
        print('Path found:', path)
    else:
        print('No path found.')

if __name__ == '__main__':
    main()