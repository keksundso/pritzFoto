import os
import glob


def scanFotoFolder(fotoFolderPath,sufix):
    for file in os.listdir(fotoFolderPath):
        if file.endswith("."+str(sufix)):
            print file



fotoFolderPath =  os.path.join(os.path.dirname(os.getcwd()), "newFotos")

scanFotoFolder(fotoFolderPath,"png")
