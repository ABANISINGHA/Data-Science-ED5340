#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# # 2.Using steepest gradient descent, find all the local minima for the function  J(x1, x2) = (x1^2+x2−11)^2+(x1+x2^2−7)^2. While applying gradient descent, do the following (a) Fixing the value for alpha (b) use line search to determine the value for alpha. Plot the intermediate steps in the iteration to show one of the minimal point.
# 
# 

# In[59]:


import numpy as np
import matplotlib.pyplot as plt
def J(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

def grad_J(x):
    b = np.zeros(2)
    b[0] = 4*x[0]*(x[0]**2 + x[1] - 11) + 2*(x[0] + x[1]**2 - 7)
    b[1] = 2*(x[0]**2 + x[1] - 11) + 4*x[1]*(x[0] + x[1]**2 - 7)
    return b

def norm(x):
    norm = np.linalg.norm(x)
    return norm

# steepest gradient descent for constant value of alpha
def gradient_decent(J,grad_J,x0,alpha,eps):
    x = np.zeros(2)
    itrs = [x0]
    while norm(grad_J(x0))>eps:
        x0 = x0 - alpha*grad_J(x0)
        itrs.append(x0)
    plt.figure(figsize=(10, 6))
    x_vals = np.linspace(-5, 5, 400)
    y_vals = np.linspace(-5, 5, 400)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = J([X, Y])

    plt.contour(X, Y, Z, levels=50, cmap='viridis')
    plt.plot([p[0] for p in itrs], [p[1] for p in itrs], 'ro-')
    plt.title('Gradient Descent Search Directions')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.colorbar(label='J(x1, x2)')
    plt.grid(True)
    plt.pause(0.1)
    plt.clf()
    return x0
        
x0 = np.array([4,-2])  
alpha = 0.01
eps = 0.001
gradient_decent(J,grad_J,x0,alpha,eps)


# In[38]:


def interval_halving(J,a,b,n,eps):
    c = a
    d = b
    l = d-c
    while abs(l)>eps:
        w1 = c+(l/4)
        w3 = d-(l/4)
        w2 = (c+d)/2
        if J(w1)< J(w2):
            d = w2
            w2 = w1
        elif J(w3)< J(w2):
            c = w2
            w2 = w3
        else:
            c = w1
            d = w3
        l = d-c
    return c


# In[ ]:





# In[ ]:





# In[64]:


import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm

def gradient_decent(J, grad_J, x0, eps):
    itrs = [x0]

    while norm(grad_J(x0)) > eps:
        dJ = grad_J(x0)
        phi = lambda alpha: J(x0 - alpha * dJ)
        alp = interval_halving(phi, 0, 4, 100, eps)
        x0 = x0 - alp * dJ
        itrs.append(x0)

    plt.figure(figsize=(10, 6))
    x_vals = np.linspace(-5, 5, 400)
    y_vals = np.linspace(-5, 5, 400)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = J([X, Y])

    plt.contour(X, Y, Z, levels=50, cmap='viridis')
    plt.plot([p[0] for p in itrs], [p[1] for p in itrs], 'ro-')
    plt.title('Gradient Descent Search Directions')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.colorbar(label='J(x1, x2)')
    plt.grid(True)
    plt.pause(0.1)
    plt.clf()

    return x0


x0 = np.array([0, 0])  # Initial guess
eps = 1e-6  # Tolerance for stopping criterion
result = gradient_decent(J, grad_J, x0, eps)
print(f"Initial point: {x0}")
print(f"Minimal point found: {result}")
print(f"Minimal value found: {J(result)}")


# In[67]:


x0 = np.array([-4, 2])  # Initial guess
eps = 1e-6  # Tolerance for stopping criterion
result = gradient_decent(J, grad_J, x0, eps)
print(f"Initial point: {x0}")
print(f"Minimal point found: {result}")
print(f"Minimal value found: {J(result)}")



# In[66]:


x0 = np.array([-2, 4])  # Initial guess
eps = 1e-6  # Tolerance for stopping criterion
result = gradient_decent(J, grad_J, x0, eps)
print(f"Initial point: {x0}")
print(f"Minimal point found: {result}")
print(f"Minimal value found: {J(result)}")


# In[69]:


x0 = np.array([2, -2])  # Initial guess
eps = 1e-6  # Tolerance for stopping criterion
result = gradient_decent(J, grad_J, x0, eps)
print(f"Initial point: {x0}")
print(f"Minimal point found: {result}")
print(f"Minimal value found: {J(result)}")


# In[ ]:




