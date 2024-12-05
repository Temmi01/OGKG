import os
import numpy as np
import matplotlib.pyplot as plt

currentDirectory = os.path.dirname(__file__)

rotationCenter = (480, 480)
angle = np.radians(100) 

def readCoordinates(filePath):
    coordinates = []
    with open(filePath, 'r') as file:
        for line in file:
            try:
                x, y = map(int, line.strip().split())
                coordinates.append((x, y))
            except ValueError:
                print("Wrong file format")
    return coordinates

coordinates = readCoordinates(os.path.join(currentDirectory, "DS9.txt"))

def rotate(point, center, angle):
    x, y = point
    xc, yc = center
    
    xs = x - xc
    ys = y - yc

    xr = np.cos(angle) * xs - np.sin(angle) * ys
    yr = np.sin(angle) * xs + np.cos(angle) * ys

    xRes = xr + xc
    yRes = yr + yc

    return xRes, yRes


transformedCoordinates = [rotate(point, rotationCenter, angle) for point in coordinates]

def build(coordinates, transformedCoordinates):
  plt.figure(figsize=(9.6, 9.6)) 

  x, y = zip(*coordinates)
  plt.scatter(x, y, color='purple', marker='o')

  xRes, yRes = zip(*transformedCoordinates)
  plt.scatter(xRes, yRes, color='blue', marker='o')

  plt.axis('off')
  plt.show()

build(coordinates, transformedCoordinates)