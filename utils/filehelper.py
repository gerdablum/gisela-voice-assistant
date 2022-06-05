from os import walk
import random

def getRandomFileFromDir(directory):
    filenames = []
    for (_, _, filename) in walk(directory):
        filenames.extend(filename)
        break
    randomNr = random.randint(0, len(filenames)-1)

    return directory + filenames[randomNr]