import os
import matplotlib.pyplot as plt

currentDirectory = os.path.dirname(__file__)

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

def build(filePath):
    coordinates = readCoordinates(filePath)

    x, y = zip(*coordinates) if coordinates else ([], [])

    plt.figure(figsize=(9.6, 5.4))

    plt.axis('off') 
    plt.scatter(x, y, c='purple', marker='o')

    plt.show()

filePath = os.path.join(currentDirectory, "DS9.txt")
build(filePath)