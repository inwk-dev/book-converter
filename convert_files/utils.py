import os
from urllib.parse import urlparse
from pathlib import Path


## Show Menu
def showMenu(options):
        for key,value in options.items():
                print(key,value)


## Execute the method with the passed path or url
    
def make_choice(argument,inputFile,switcher):
        # Get the function from switch dictionary
        func = switcher.get(argument)
        # Execute the function
        return func(inputFile)



## Trim the filename from url or path
def retrieveFilename(url) -> str:
        """
        Parse an url and retrieve a string with the filename.
        """
        a = urlparse(url)
        filename = os.path.basename(a.path)
        return filename

def createFileDestination(basePath, filename) -> str:
        path = os.path.join(basePath,filename)
        return path
        
def checkChoice(choice,choices) -> bool:
      """
      MENU.
      Check if the selection exists in the dictionary with options.
      """
      if choice in choices.keys():
        return True
      else:
        return False


def isTxt(inputFile) -> bool:
        suffix = ".txt"
        return inputFile.endswith(suffix)

def isPdf(inputFile) -> bool:
        suffix = ".pdf"
        return inputFile.endswith(suffix)

def isEpud(inputFile)-> bool:
        suffix = ".epub"
        return inputFile.endswith(suffix)

def isUrl(inputFile)-> bool:
        prefix = "http"
        return inputFile.start(prefix)

def isHtml(inputFile) -> bool:
        suffix = ".html"
        return inputFile.endswith(suffix)

