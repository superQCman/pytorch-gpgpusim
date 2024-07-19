import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)  # Input channels, output channels, kernel size
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(64 * 7 * 7, 256)  # Adjust the dimensions according to your input image size
        self.fc2 = nn.Linear(256, 10)  # Assuming 10 classes

    def forward(self, x):
        # Convolution 1
        x = self.conv1(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)  # Pooling with kernel size 2

        # Convolution 2
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)

        # Flattening the layers
        x = x.view(x.size(0), -1)

        # Fully connected 1
        x = self.fc1(x)
        x = F.relu(x)

        # Fully connected 2
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output

# Set random seed for reproducibility
torch.manual_seed(42)

# Create random input data (batch size, number of color channels, height, width)
# Let's assume the input images are 28x28 grayscale images.
inputs = torch.randn(64, 1, 28, 28)  # Batch size of 64

# Create random target classes
targets = (torch.rand(64) * 10).floor().type(torch.LongTensor) # Assuming 10 classes
# Initialize the network
model = SimpleCNN()

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
num_epochs = 5
for epoch in range(num_epochs):
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()
    
    print('Epoch [{}/100], Loss: {:.4f}'.format(epoch + 1, loss.item()))
