import numpy as np
#NEW LINE ADDED IN MASTER BRANCH STABLE CODE
# Function for vector addition
def vector_addition(vector1, vector2):
    # Convert lists to numpy arrays (if they're not already)
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)
    
    # Add the vectors
    result = vector1 + vector2
    
    return result

# 4 Example vectors
vector1 = [3,4,5]
vector2 = [1, -1, 2]
vector3 = [7,8,9]
vector4 = [10,11,12,13]
# Perform vector addition
result = vector_addition(vector1, vector2)

# Print the result
print("Result of vector addition:", result)


#VERY GOOD CODE
#changes made by nice
