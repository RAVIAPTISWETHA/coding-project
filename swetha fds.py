# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 22:37:32 2023

@author: swetha
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Step 1: Read the data from the CSV file
data = pd.read_csv('data5-1.csv')

# Extract the column name with leading spaces
salary_column = data.columns[0]

# Step 2: Create a probability density function (PDF) and plot it as a histogram
plt.hist(data[salary_column], bins=30, density=True, alpha=0.6, color='g', label='Histogram')

mu, std = norm.fit(data[salary_column])
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2, label='PDF')

# Step 3: Calculate and print the mean annual salary (W)
W = round(mu, 2)
plt.axvline(W, color='b', linestyle='dashed', linewidth=2, label=f'Mean Salary ($W={W}$)')

# Step 4: Calculate another value X using the distribution
# For example, choose X as the 75th percentile
X = round(np.percentile(data[salary_column], 75), 2)
plt.axvline(X, color='r', linestyle='dashed', linewidth=2, label=f'X ($X={X}$)')

# Step 5: Add labels, title, and legend
plt.xlabel('Salary')
plt.ylabel('Probability Density')
plt.title('Probability Density Function of Salaries')
plt.legend()

# Show the plot
plt.show()
