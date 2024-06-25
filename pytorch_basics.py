# Importing PyTorch
import torch

# Creating a tensor
tensor = torch.tensor([1.0, 2.0, 3.0])
print("Tensor:", tensor)

# Basic operations with tensors
tensor_add = tensor + tensor
print("Addition:", tensor_add)

tensor_mul = tensor * tensor
print("Multiplication:", tensor_mul)

# Creating a random tensor
random_tensor = torch.rand(2, 3)
print("Random Tensor:", random_tensor)

# Creating a tensor with all elements set to zero
zeros_tensor = torch.zeros(2, 3)
print("Zeros Tensor:", zeros_tensor)

# Creating a tensor with all elements set to one
ones_tensor = torch.ones(2, 3)
print("Ones Tensor:", ones_tensor)

# Reshaping a tensor
reshaped_tensor = tensor.view(3, 1)
print("Reshaped Tensor:", reshaped_tensor)

# Computing the mean of a tensor
mean_value = tensor.mean()
print("Mean Value:", mean_value)

# Computing the sum of a tensor
sum_value = tensor.sum()
print("Sum Value:", sum_value)

# Creating a simple neural network
import torch.nn as nn
import torch.nn.functional as F

class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(3, 2)
        self.fc2 = nn.Linear(2, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Creating an instance of the network
net = SimpleNet()
print("Network Architecture:", net)

# Creating a loss function and optimizer
import torch.optim as optim

criterion = nn.MSELoss()
optimizer = optim.SGD(net.parameters(), lr=0.01)

# Training the network
input_data = torch.tensor([1.0, 2.0, 3.0])
target = torch.tensor([1.0])

for epoch in range(10):
    optimizer.zero_grad()
    output = net(input_data)
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item()}")
