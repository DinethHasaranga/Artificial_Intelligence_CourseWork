import random as rand

# Creating the maze - Task 01
random_maze = []

maze_rows = 6
maze_columns = 6

for i in range(maze_rows):
    line = []
    for j in range(maze_columns):
        line.append(0)
    random_maze.append(line)

# Creating the start cell of the maze
start_cell_row = rand.randint(0, 1)
start_cell_column = rand.randint(0, 5)
random_maze[start_cell_column][start_cell_row] = 7

# Creating the goal cell of the maze
goal_cell_row = rand.randint(4, 5)
goal_cell_column = rand.randint(0, 5)
random_maze[goal_cell_column][goal_cell_row] = 8

# Creating the barrier cells of the maze
barrier_counter = 0
while barrier_counter < 4:
    barrier_row = rand.randint(0, 5)
    barrier_column = rand.randint(0, 5)

    if random_maze[barrier_column][barrier_row] != 0:
        continue
    random_maze[barrier_column][barrier_row] = 1
    barrier_counter = barrier_counter + 1

for i in random_maze:
    print(i)
print("\n")

# DSF SEARCH ALOGRITHM - Task 02
# Defining the directions allowed to move - up/down/left/right/diagonal

def valid_moves(x_cordinate, y_cordinate, maze):

    next_valid_move = []

#Search directions

    west_search = maze[y_cordinate][x_cordinate - 1]

    if y_cordinate < 5:
        north_search = maze[y_cordinate + 1][x_cordinate]

    if x_cordinate < 5:
        east_search = maze[y_cordinate][x_cordinate + 1]

    south_search = maze[y_cordinate - 1][x_cordinate]

    if y_cordinate < 5:
        northwest_search = maze[y_cordinate + 1][x_cordinate - 1]

    if y_cordinate < 5 and x_cordinate < 5:
        northeast_search = maze[y_cordinate + 1][x_cordinate + 1]

    if x_cordinate < 5:
        southeast_search = maze[y_cordinate - 1][x_cordinate + 1]

    southwest_search = maze[y_cordinate - 1][x_cordinate - 1]

#Search process

    if x_cordinate-1>=0 and west_search!=1:
        next_valid_move.append((y_cordinate,x_cordinate - 1))

    if y_cordinate+1<len(maze) and north_search!=1:
        next_valid_move.append((y_cordinate + 1,x_cordinate))

    if x_cordinate+1<len(maze) and east_search!=1:
        next_valid_move.append((y_cordinate,x_cordinate + 1))

    if y_cordinate-1>=0 and south_search!=1:
        next_valid_move.append((y_cordinate - 1,x_cordinate))

    if (x_cordinate - 1 >= 0 and y_cordinate + 1 < len(maze)) and northwest_search!=1:
        next_valid_move.append((y_cordinate + 1,x_cordinate - 1))

    if (x_cordinate + 1 < len(maze) and y_cordinate + 1 < len(maze)) and northeast_search!=1:
        next_valid_move.append((y_cordinate + 1,x_cordinate + 1))

    if (x_cordinate + 1 < len(maze) and y_cordinate - 1 >= 0) and southeast_search!=1:
        next_valid_move.append((y_cordinate - 1,x_cordinate + 1))

    if (x_cordinate - 1 >= 0 and y_cordinate - 1 >= 0) and southwest_search!=1:
        next_valid_move.append((y_cordinate - 1,x_cordinate - 1))


    return next_valid_move

# Apply DFS search to the maze to find the goal

def DFS_Process(maze, stack, visited_cells):

    start = (start_cell_column,start_cell_row)
    goal = (goal_cell_column,goal_cell_row)
    stack.append(start)

    while stack:
        currentExploreCell = stack.pop()
        # print("Popping", currentExploreCell)

        if currentExploreCell == goal:
            print("Goal found")
            print("This is the Final path", visited_cells)
            Total_Node = len(visited_cells)
            print("Time taken to find the goal: ", Total_Node, "minutes")
            return

        a = currentExploreCell[0]
        b = currentExploreCell[1]
        next_steps = valid_moves(a, b, maze)
        # print("Next steps is", next_steps)

        for next_cell in next_steps:
            if next_cell in visited_cells:
                # print(next_cell, ":visited cell")
                continue
            visited_cells.add(next_cell)
            stack.append(next_cell)

            # print("Visited nodes:", visited_cells)
            # print("Explore cells", stack)

# "explore_cells_stack" list work as a stack
explore_cells_stack = []
# visited set doesn't contain repeated cells.
visited = set()

valid_moves(start_cell_row, start_cell_column, random_maze)
DFS_Process(random_maze, explore_cells_stack, visited)

print("\n")
print("End of DFS Search Algorithm")
print("\n")
print("Start of A Star Search Algorithm")
print("\n")


# Heuristic cost calculation - Task 03
def Chebyshev_distance_calculation(goal_row_che, goal_col_che):
    chebyshev_value_list = []

    for row_node in range (maze_rows):
        for column_node in range (maze_columns):
            value = max(abs(row_node - goal_row_che), abs(column_node - goal_col_che))
            chebyshev_value_list.append(value)
            column_node += 1
        row_node += 1

    return chebyshev_value_list


# A star search algorithm - Task 04
def a_Serch(insert_Maze, start_row, start_column, goal_row, goal_column):
    cell_value_list = []

    # The below list works as a priority queue
    p_queue = []

    visited_nodes_list = []
    heuristic_value_dictionary = {} # Conatains a dictionary with heuristic values and respective cell

    startNode = (start_column, start_row)
    goalNode = (goal_column, goal_row)
    childNode = startNode

    # Dictionary to find the path from start to the goal node
    path_reverse_dic = {}

    # Updating heuristic cost to dictionary from heuristic_cost_calculation function
    heuristicValue = Chebyshev_distance_calculation(goal_row, goal_column)
    print("Heuristic Values")
    print(heuristicValue)
    print("\n")

    # Creating the heuristic value dictionary
    for i in range(6):
        for j in range(6):
            temp_cell = (j, i)
            cell_value_list.append(temp_cell)
    for i in range(36):
        value = cell_value_list[i]
        heuristic_value_dictionary[value] = heuristicValue[i]
    print("Heuristic value and the respective cell")
    print(heuristic_value_dictionary)
    print("\n")

    # Dictionary to hold g(n) values for each cell
    g_score_dict = {cell: float('inf') for cell in cell_value_list}
    g_score_dict[startNode] = 0

    # Dictionary to hold final value(g(n)+h(n)) for each cell
    f_score_dict = {cell: float('inf') for cell in cell_value_list}
    f_score_dict[startNode] = heuristic_value_dictionary[startNode]

    p_queue.append(startNode)

    while len(p_queue) != 0:
        curr_cell_node = p_queue.pop(0)
        start_column = curr_cell_node[0]
        start_row = curr_cell_node[1]
        visited_nodes_list.append(curr_cell_node)

        # Defining the directions allowed to move - up/down/left/right/diagonal
        west_search = insert_Maze[start_column][start_row - 1]

        if start_column < 5:
            north_search = insert_Maze[start_column + 1][start_row]

        if start_row < 5:
            east_search = insert_Maze[start_column][start_row + 1]

        south_search = insert_Maze[start_column - 1][start_row]

        if start_column < 5:
            L = insert_Maze[start_row - 1][start_column + 1] #northwest_search

        if start_column < 5 and start_row < 5:
            M = insert_Maze[start_row + 1][start_column + 1] #northeast_search

        if start_row < 5:
            P = insert_Maze[start_row + 1][start_column - 1] #southeast_search

        O = insert_Maze[start_row - 1][start_column - 1] #southwest_search

        if curr_cell_node == goalNode:
            print("Goal has found")
            # print("Visited nodes")
            print(visited_nodes_list)
            length_node_list = len(visited_nodes_list)
            print("Time taken to find the goal: ", length_node_list, "minutes")
            break
        else:
            for i in "ESNWLMPO": #Search process

                if i == "W":
                    if start_row - 1 >= 0 and west_search!=1:
                        childNode = (start_column, start_row - 1)

                elif i == "N":
                    if start_column + 1 <len(insert_Maze) and north_search!=1:
                        childNode = (start_column + 1, start_row)

                elif i == "S":
                    if start_column - 1 >0 and south_search!=1:
                        childNode = (start_column - 1, start_row)

                elif i == "E":
                    if start_row + 1 < len(insert_Maze) and east_search!=1:
                        childNode = (start_column, start_row + 1)

                elif i == "L":
                    if (start_row - 1 >= 0 and start_column + 1 < len(insert_Maze)) and L!=1:
                        childNode = (start_column + 1, start_row - 1)

                elif i == "M":
                    if (start_row + 1 < len(insert_Maze) and start_column + 1 < len(insert_Maze)) and M!=1:
                        childNode = (start_column + 1, start_row + 1)

                elif i == "P":
                    if (start_row + 1 < len(insert_Maze) and start_column - 1 >= 0) and P!=1:
                        childNode = (start_column - 1, start_row + 1)

                elif i == "O":
                    if (start_row - 1 >= 0 and start_column - 1 >= 0) and O!=1:
                        childNode = (start_column - 1, start_row - 1)

                temp_g_value = g_score_dict[curr_cell_node] + 1
                temp_final_value = temp_g_value + heuristic_value_dictionary[childNode]

                if temp_final_value < f_score_dict[childNode]:
                    g_score_dict[childNode] = temp_g_value
                    f_score_dict[childNode] = temp_final_value
                    p_queue.append(childNode)
                    path_reverse_dic[childNode] = curr_cell_node

    cell_temp = (goal_column, goal_row)
    path_forward = {}
    while cell_temp != startNode:
        path_forward[path_reverse_dic[cell_temp]] = cell_temp
        cell_temp = path_reverse_dic[cell_temp]

    print("\n")
    print("The final path :")
    print(path_forward.values())

Chebyshev_distance_calculation(goal_cell_row, goal_cell_column)
a_Serch(random_maze, start_cell_row, start_cell_column, goal_cell_row, goal_cell_column)



