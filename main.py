import array as array
import numpy as np 

a = np.array([[1,2,3,5],
             [4,5,6,2],
             [7,8,9,1],
             [3,4,1,2]])
           
print(a)   

# Basic Info 

print(a.shape)     # Matrix rows x cols
print(a.ndim)      # Number of dimension 
print(a.size)      # Number of elements
print(a.dtype)     # Type of data 

# Slicing 

print(a[0,:])      # First row 
print(a[:,0])      # First column
print(a[1:3,1:3])  # Middle 2x2 block 

# Mathematic Operation 

print(np.sum(a))          # Total sum
print(np.mean(a))         # Average
print(np.max(a))          # Largest
print(np.sum(a, axis=0))  # Sum of each columns
print(np.sum(a, axis=1))  # Sum of each rows

# Transpose

print(a.T)
 
# Matrix arthematic operation 

b = np.array([[1,0,1,0],
             [0,1,0,1],
             [1,0,1,0],
             [0,1,0,1]])
             
    # addition
    
print(a + b)  # Adds each element 
print(a + 10) # Adds 10 to every element
print(a - b)  # Substract each element

     # multiplication
     
print(a * b)        # element wise multiplication
print(a * 2)        # multiply every elemnt by 2
print(np.dot(a,b))  # True matrix multiplication
