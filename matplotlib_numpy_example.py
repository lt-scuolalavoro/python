# Matplotlib is a Python 2D plotting library with which you can generate plots,
# histograms, power spectra, bar charts, errorcharts, scatterplots, etc., 
# with just a few lines of code.
import matplotlib

# The	matplotlib.pyplot module provides a MATLAB-like plotting framework
import matplotlib.pyplot as plt

# NumPy is the fundamental package for scientific computing with Python
# It contains, among other things, a powerful N-dimensional array object
import numpy as np

# Note that in the following code we are going to use 
# the arange() from the numpy module because Python's builtin
# range() function only accepts integer numbers as parameters.

# Data for plotting
# (t, s) are the arrays of coordinates
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# Get the Figure and Axes objects
fig, ax = plt.subplots()

# Plot the graph
ax.plot(t, s)

# Set descriptions for the graph
ax.set(title='Voltage', xlabel='time (s)', ylabel='voltage (mV)')

# Show the graph
plt.show()
