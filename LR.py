from matplotlib import pyplot
from pandas import DataFrame
import pandas as pd
import csv
import random
import matplotlib.pyplot as plt
import numpy as np

def Prediction(x):
  '''
  Test a random point with the model.
  '''
  print('\n PREDICTION OF A RANDOM POINT BY MODEL\n')
  m1 = 0.5
  c1 = 4
  d1 = random.uniform(-1, 1)
  y1 = m1 * x + c1 + d1
  print("Random Point: ", x)
  print("Actual Value:", y1)

  y2 = M[ind+1] * x + C[ind+1]
  print("Predicted Value by the model: ", y2)
  print("Loss: ", loss_function(M[ind+1],C[ind+1],x,y1),'\n')

def loss_function(m,c,x,t):
  '''
  Calculate Loss.
  '''
  return (t - ((m*x) + c))**2

def num_derivative(m,c,x,t,h):
  '''
  Calculate Numerical derivate w.r.t m and c.
  '''
  dlm = 0
  dlc = 0
  for i in range(x.shape[0]):
    dlmc = loss_function(m,c,x[i],t[i])
    dlmh = loss_function(m+h,c,x[i],t[i])
    dlch = loss_function(m,c+h,x[i],t[i])
    dlm += ((dlmh - dlmc) / h)
    dlc += ((dlch - dlmc) / h)
  return dlm,dlc


# Read data from the file
df = pd.read_csv('data.csv')
x = np.array(df['X'])
y = np.array(df['Y'])

# Initialize m and c with random values
alpha = 0.0001
h = 0.02
m = random.uniform(0,1)
c = random.randint(0,4)

# Calculate loss for 100 iterations
loss = []
M = [m]
C = [c]
for i in range(100):
  l = 0
  for j in range(x.shape[0]):
    l += loss_function(M[-1],C[-1],x[i],y[i])
  loss.append(l)

  m_d, c_d = num_derivative(M[-1],C[-1],x,y,h)

  m_new = M[-1] - (alpha * m_d)
  c_new = C[-1] - (alpha * c_d)

  if np.sign(M[-1]) != np.sign(m_new) or np.sign(C[-1]) != np.sign(c_new):
    alpha = alpha/2

  M.append(m_new)
  C.append(c_new)

# Get the parameters where loss in minimum.

ind = loss.index(min(loss))
y_new = (M[ind+1] * x) + C[ind+1]

# Plot the values predicted by model.

plt.scatter(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x,y_new)
plt.show()

# Test a random point with model.
input_val = input("Enter input value to Prediction function: ")
Prediction(float(input_val))
