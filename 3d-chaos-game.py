import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

N = 3  # Number of points on the unit circle

# Create points on the unit circle
r = np.arange(0, N)
points = np.exp(2.0 * np.pi * 1j * r / N)
points_3d = np.zeros((N, 3))
points_3d[:, 0] = np.real(points)
points_3d[:, 1] = np.imag(points)

# Add a fourth point above the center of the unit circle
z_height = 1.0  # Change this value as needed to adjust the height of the fourth point
fourth_point = np.array([0, 0, z_height])
points_3d = np.vstack([points_3d, fourth_point])

# Compute resolution for the unit circle display
res = 100
w = np.arange(0, res)
unit_circle = np.exp(2.0 * np.pi * w * 1j / res)
unit_circle_3d = np.zeros((res, 3))
unit_circle_3d[:, 0] = np.real(unit_circle)
unit_circle_3d[:, 1] = np.imag(unit_circle)

# Start point
start = np.array([0.1, 0.5, 0])  # Start in the plane

def compute_new_rand_location(startLoc):
    rand_location = np.random.randint(0, N + 1)
    vector = (points_3d[rand_location] - startLoc) / 2.0
    new_point = startLoc + vector
    return new_point

# Set up the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(unit_circle_3d[:, 0], unit_circle_3d[:, 1], unit_circle_3d[:, 2], 'b-')
ax.plot(points_3d[:, 0], points_3d[:, 1], points_3d[:, 2], 'ro')

# Iterate and plot points
next_point = start
for iteration in range(2000):
    next_point = compute_new_rand_location(next_point)
    ax.plot([next_point[0]], [next_point[1]], [next_point[2]], "b.")

# Final plot adjustments
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
print("End")