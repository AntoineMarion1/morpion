import numpy as np


from minimax import Minimax, cost, possible_states_space, stop

class Board: 

    def __init__(self, grid =np.zeros(shape = (3, 3))): 

        self.grid: np.ndarray = np.zeros(shape = (3, 3))
        self.player = 1 
        self.winner = 0 


    def compute_player(self)\
                        -> int: 

        if np.sum(self.grid) == 1: 
            return -1
        else: 
            return 1

    def play_a_move(self, 
                    coo: tuple)\
                    -> bool: 
        
        try: 
            coo_x = int(coo[0])
            coo_y = int(coo[1])

        except ValueError: 
            return False 
        
        if (coo_x >= 0)\
                and (coo_x <= 3)\
                and (coo_y >= 0)\
                and (coo_y <= 3)\
                and (self.grid[coo_x, coo_y] == 0): 
            
            self.grid[coo_x, coo_y] = self.player
            return True
        
        else: 
            return False

    def compute_winner(self)\
                       -> int: 
        def transform_matrix(mat: np.ndarray): 
            transposed_matrix = np.transpose(mat)
            col_0 = transposed_matrix[:, 0].reshape((3, 1))
            col_1 = transposed_matrix[:, 1].reshape((3, 1))
            col_2 = transposed_matrix[:, 2].reshape((3, 1))

            return np.hstack([col_2, col_1, col_0])
        
        vec = np.ones(shape = (3, 1))
        transformed_grid = transform_matrix(self.grid)
        
        horizontals_sum_array = self.grid @ vec 
        vertical_sum_array = transformed_grid @ vec

        for i in range(3): 
            if horizontals_sum_array[i] == 3 or vertical_sum_array[i] == 3: 
                self.winner = 1
            elif horizontals_sum_array[i] == -3 or vertical_sum_array[i] == -3: 
                self.winner = -1
            

        if np.trace(transformed_grid) == 3 or np.trace(self.grid) == 3: 
            self.winner = 1 
        
        elif np.trace(transformed_grid) == -3 or np.trace(self.grid) == -3: 
            self.winner = -1 

    def compute_player(self) -> int: 

        if np.sum(self.grid) == 1: 
            self.player = -1
        else: 
            self.player = 1

    def terminal_display(self): 
        
        def convert_to_icon(x: float) -> str: 
            if x == 0.: 
                return "-"
            elif x == 1.: 
                return "X"
            else: 
                return "O"
            
        print("\n" + convert_to_icon(self.grid[0, 0]) + " | " + convert_to_icon(self.grid[0, 1]) + " | " + convert_to_icon(self.grid[0, 2]))
        print(convert_to_icon(self.grid[1, 0]) + " | " + convert_to_icon(self.grid[1, 1]) + " | " + convert_to_icon(self.grid[1, 2]))
        print(convert_to_icon(self.grid[2, 0]) + " | " + convert_to_icon(self.grid[2, 1]) + " | " + convert_to_icon(self.grid[2, 2]))
        print(" ")
    

    def compute_best_move(self) -> tuple: 

        depth = 0 

        if np.any(self.grid) == False:
            return (0, 0) 
        
        #compute the depth 
        for x_index in range(3): 
            for y_index in range(3): 
                if self.grid[x_index, y_index] == 0: 
                    depth += 1

        #if the AI is the player 1, the algorithm need to find the maximal value 
        if self.player == 1: 
            best_cost =  -1000
            best_cost_index = (0, 0)

            for x_index in range(3): 
                for y_index in range(3): 
                    if self.grid[x_index, y_index] == 0: 
                        copy_grid = np.copy(self.grid)
                        copy_grid[x_index, y_index] = 1

                        evaluation = Minimax(copy_grid, -1, depth-1, cost, possible_states_space, stop)
                        if best_cost < evaluation: 
                            best_cost = evaluation
                            best_cost_index = (x_index, y_index)

        #if the AI is the player -1, the algorithm need to find the minimal value 
        else: 
            best_cost = 1000
            best_cost_index = (0, 0)

            for x_index in range(3): 
                for y_index in range(3): 
                    if self.grid[x_index, y_index] == 0: 
                        copy_grid = np.copy(self.grid)
                        copy_grid[x_index, y_index] = -1

                        evaluation = Minimax(copy_grid, 1, depth-1, cost, possible_states_space, stop)

                        if best_cost > evaluation: 
                            best_cost = evaluation
                            best_cost_index = (x_index, y_index)
    
        return best_cost_index
    





# def possible_states_space(node: np.ndarray) -> list: 

#     result = []

#     if np.sum(node) == 1: 
#         player =  -1
#     else: 
#         player = 1
    
#     for x_index in range(3): 
#         for y_index in range(3): 
#             if node[x_index, y_index] == 0: 
#                 copy_node = np.copy(node)
#                 copy_node[x_index, y_index] = player
#                 result.append(copy_node)
    
#     return result



# def cost(node: np.ndarray) -> int: 

#     def transform_matrix(mat: np.ndarray): 
#             transposed_matrix = np.transpose(mat)
#             col_0 = transposed_matrix[:, 0].reshape((3, 1))
#             col_1 = transposed_matrix[:, 1].reshape((3, 1))
#             col_2 = transposed_matrix[:, 2].reshape((3, 1))

#             return np.hstack([col_2, col_1, col_0])
        
#     vec = np.ones(shape = (3, 1))
#     transformed_grid = transform_matrix(node)

#     horizontals_sum_array = node @ vec 
#     vertical_sum_array = transformed_grid @ vec

#     for i in range(3): 
#         if horizontals_sum_array[i] == 3 or vertical_sum_array[i] == 3: 
#             return 10
#         elif horizontals_sum_array[i] == -3 or vertical_sum_array[i] == -3: 
#             return -10
        

#     if np.trace(transformed_grid) == 3 or np.trace(node) == 3: 
#         return 10

#     elif np.trace(transformed_grid) == -3 or np.trace(node) == -3: 
#         return -10

#     else: 
#         return 0 
    

# def stop(node: np.ndarray)\
#       -> bool:
    
#     def transform_matrix(mat: np.ndarray): 
#             transposed_matrix = np.transpose(mat)
#             col_0 = transposed_matrix[:, 0].reshape((3, 1))
#             col_1 = transposed_matrix[:, 1].reshape((3, 1))
#             col_2 = transposed_matrix[:, 2].reshape((3, 1))

#             return np.hstack([col_2, col_1, col_0])
        
#     vec = np.ones(shape = (3, 1))
#     transformed_grid = transform_matrix(node)

#     horizontals_sum_array = node @ vec 
#     vertical_sum_array = transformed_grid @ vec

#     for i in range(3): 
#         if horizontals_sum_array[i] == 3 or vertical_sum_array[i] == 3: 
#             return True
#         elif horizontals_sum_array[i] == -3 or vertical_sum_array[i] == -3: 
#             return True
        

#     if np.trace(transformed_grid) == 3 or np.trace(node) == 3: 
#         return True

#     elif np.trace(transformed_grid) == -3 or np.trace(node) == -3: 
#         return True

#     else: 
#         return False

    
# def Minimax(node: np.ndarray, 
#             player : int,
#             depth: int, 
#             cost, 
#             f, 
#             stop):
 
#     if (stop(node)==True or depth == 0):
#         return cost(node)
    
#     else:

#         EEP = f(node)

#         if (player==1):
#             return max([Minimax(n, -1, depth-1, cost, f, stop) for n in EEP])
     
#         else:
#             player = 1
#             return min([Minimax(n, 1, depth-1, cost, f, stop) for n in EEP])
        




