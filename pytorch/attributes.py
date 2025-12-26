import torch
import numpy as np

data = [[1, 2],[3, 4]]
x_data = torch.tensor(data)

# initialization of a tensor from an array
print(x_data)

# from numpy
np_array = np.array(data)
x_np = torch.from_numpy(np_array)

# from another tensor: 
x_ones = torch.ones_like(x_data) # retains the properties of x_data
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float) # overrides the datatype of x_data
print(f"Random Tensor: \n {x_rand} \n")


# attrinubtes of a tensor: 


tensor = torch.rand(3,4) # 3 rows, 4 columns

print(tensor)
print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}") # stored on CPU