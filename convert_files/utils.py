import os
from urllib.parse import urlparse
from pathlib import Path


#region Menu
## Show intro
def showIntro():
        """
        Show intro message - title + separator.
        """
        print("\n\n\n\n")
        print("Select from the following options:")
        print("=========================================")
        print("\n\n")

## Show Menu
def showMenu(options):
        """
        Display options menu.
        """
        for key,value in options.items():
                print(key,value)

## Execute the method with the passed path or url
def make_choice(argument,inputFile,switcher):
        """
        Trigger the execution of the method 
        based on the choice and dictionary with options.
        """
        # Get the function from switch dictionary
        func = switcher.get(argument)
        # Execute the function
        return func(inputFile)

## Check if the selected option is present in the dict of available options        
def checkChoice(choice,choices) -> bool:
      """
      Check if the selection exists in the dictionary with options.
      """
      if choice in choices.keys():
        return True
      else:
        return False
#endregion


#region File
## Retrieve the filename from url or path
def retrieveFilename(url) -> str:
        """
        Parse an url/filepath and retrieve a string with the filename.
        """
        a = urlparse(url)
        filename = os.path.basename(a.path)
        return filename

## Create the full destination path for the file
def createFileDestination(basePath, filename) -> str:
        path = os.path.join(basePath,filename)
        return path
#endregion


#region Fileformats.
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
#endregion