import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import random
# Example data: [center_x, center_y, center_z, length, width, height]

def plotULD(data,x,y,z):

    dim = {'x': x, 'y': y, 'z': z}

    packages = [lst[1] + lst[2] for lst in data]
    # Create the plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    colors = ["cyan"]
    # Function to create a cuboid at a specific center with length, width, and height
    def create_cuboid(center, length, width, height):
        # Calculate the 8 corners of the cuboid
        x, y, z = center
        l, w, h = length / 2, width / 2, height / 2  # Half sizes

        # Define the corners of the cuboid
        corners = [
            [x - l, y - w, z - h], [x + l, y - w, z - h], [x + l, y + w, z - h], [x - l, y + w, z - h],  # Bottom
            [x - l, y - w, z + h], [x + l, y - w, z + h], [x + l, y + w, z + h], [x - l, y + w, z + h]   # Top
        ]
        
        # List of sides of the cuboid
        faces = [
            [corners[0], corners[1], corners[2], corners[3]],  # Bottom
            [corners[4], corners[5], corners[6], corners[7]],  # Top
            [corners[0], corners[1], corners[5], corners[4]],  # Front
            [corners[2], corners[3], corners[7], corners[6]],  # Back
            [corners[0], corners[3], corners[7], corners[4]],  # Left
            [corners[1], corners[2], corners[6], corners[5]]   # Right
        ]
        
        # Create 3D polygons (faces) from the corners
        return Poly3DCollection(faces, facecolors=colors[random.randint(0,len(colors)-1)], linewidths=1, edgecolors='r', alpha=0.5)

    # Add each cuboid to the plot
    for package in packages:
        center, length, width, height = package[:3], package[3], package[4], package[5]
        cuboid = create_cuboid(center, length, width, height)
        ax.add_collection3d(cuboid)

    # Set the limits for the plot
    ax.set_xlim([0, dim['x']])
    ax.set_ylim([0, dim['y']])
    ax.set_zlim([0, dim['z']])

    plt.show()
