import numpy as np



def possible_states_space(node: np.ndarray) -> list: 

    result = []

    if np.sum(node) == 1: 
        player =  -1
    else: 
        player = 1
    
    for x_index in range(3): 
        for y_index in range(3): 
            if node[x_index, y_index] == 0: 
                copy_node = np.copy(node)
                copy_node[x_index, y_index] = player
                result.append(copy_node)
    
    return result



def cost(node: np.ndarray) -> int: 

    def transform_matrix(mat: np.ndarray): 
            transposed_matrix = np.transpose(mat)
            col_0 = transposed_matrix[:, 0].reshape((3, 1))
            col_1 = transposed_matrix[:, 1].reshape((3, 1))
            col_2 = transposed_matrix[:, 2].reshape((3, 1))

            return np.hstack([col_2, col_1, col_0])
        
    vec = np.ones(shape = (3, 1))
    transformed_grid = transform_matrix(node)

    horizontals_sum_array = node @ vec 
    vertical_sum_array = transformed_grid @ vec

    for i in range(3): 
        if horizontals_sum_array[i] == 3 or vertical_sum_array[i] == 3: 
            return 10
        elif horizontals_sum_array[i] == -3 or vertical_sum_array[i] == -3: 
            return -10
        

    if np.trace(transformed_grid) == 3 or np.trace(node) == 3: 
        return 10

    elif np.trace(transformed_grid) == -3 or np.trace(node) == -3: 
        return -10

    else: 
        return 0 
    

def stop(node: np.ndarray)\
      -> bool:
    
    def transform_matrix(mat: np.ndarray): 
            transposed_matrix = np.transpose(mat)
            col_0 = transposed_matrix[:, 0].reshape((3, 1))
            col_1 = transposed_matrix[:, 1].reshape((3, 1))
            col_2 = transposed_matrix[:, 2].reshape((3, 1))

            return np.hstack([col_2, col_1, col_0])
        
    vec = np.ones(shape = (3, 1))
    transformed_grid = transform_matrix(node)

    horizontals_sum_array = node @ vec 
    vertical_sum_array = transformed_grid @ vec

    for i in range(3): 
        if horizontals_sum_array[i] == 3 or vertical_sum_array[i] == 3: 
            return True
        elif horizontals_sum_array[i] == -3 or vertical_sum_array[i] == -3: 
            return True
        

    if np.trace(transformed_grid) == 3 or np.trace(node) == 3: 
        return True

    elif np.trace(transformed_grid) == -3 or np.trace(node) == -3: 
        return True

    else: 
        return False

    
def Minimax(node: np.ndarray, 
            player : int,
            depth: int, 
            cost, 
            f, 
            stop):
 
    if (stop(node)==True or depth == 0):
        return cost(node)
    
    else:

        EEP = f(node)

        if (player==1):
            return max([Minimax(n, -1, depth-1, cost, f, stop) for n in EEP])
     
        else:
            player = 1
            return min([Minimax(n, 1, depth-1, cost, f, stop) for n in EEP])
        




