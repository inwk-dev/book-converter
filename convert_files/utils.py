import os
from urllib.parse import urlparse
from pathlib import Path

def retrieveFilename(url) -> str:
        """
        Parse an url and retrieve a string with the filename.
        """
        a = urlparse(url)
        filename = os.path.basename(a.path)
        return filename
        
def checkChoice(choice,choices) -> bool:
      """
      docstring
      """
      if choice in choices.keys():
        return True
      else:
        return False


def isTxt(inputFile):
        suffix = ".txt"
        return inputFile.endswith(suffix)

def isPdf(inputFile):
        suffix = ".pdf"
        return inputFile.endswith(suffix)

def isUrl(inputFile):
        prefix = "http"
        return inputFile.start(prefix)

def isEpud(inputFile):
        suffix = ".epub"
        return inputFile.endswith(suffix)