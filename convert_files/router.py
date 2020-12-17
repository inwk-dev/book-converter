import converter
import utils

class Route():
    """
    Routing class holding triggering the methods for conversion.
    """
    
    ## Execute the method with the passed path or url
    @staticmethod
    def make_choice(argument,inputFile):
        # Get the function from switch dictionary
        func = switcher.get(argument)
        # Execute the function
        return func(inputFile)

    @staticmethod
    def txtToPdf(input):

        if utils.isTxt:
            converter.ToPdfConverter.ConvertTextToPdf(input)

        print(input)

    @staticmethod
    def htmlToPdf(input):
        print("text")

    @staticmethod
    def htmlToTxt(input):
        print(input)

    @staticmethod
    def docToTxt(input):
        print("text")
    
    @staticmethod
    def docToPdf(input):
        print("text")
    
    @staticmethod
    def docxToTxt(input):
        print("text")

    @staticmethod
    def docxToPdf(input):
        print("text")
    
    @staticmethod
    def epubToTxt(input):
        print("text")
    
    @staticmethod
    def epubToPdf(input):
        print("text")

switcher = {
    "0": exit,
    "1": Route.txtToPdf,
    "2": Route.htmlToPdf,
    "3": Route.htmlToTxt,
    "4": Route.docToTxt,
    "5": Route.docToPdf,
    "6": Route.docxToTxt,
    "7": Route.docxToPdf,
    "8": Route.epubToTxt,
    "9": Route.epubToPdf
}
