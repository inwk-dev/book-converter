import converter
import utils

class Route():
    """
    Routing class holding triggering the methods for conversion.
    """
    
    
    @staticmethod
    def txtToPdf(input):
        if utils.isTxt:
            try:
                fullpath = converter.ToPdfConverter.ConvertTextToPdf(input)
                print('The file has been created at: {}'.format(fullpath))

            except:
                print("There was an issue while processing the file.")
                

    @staticmethod
    def pdfToTxt(input):
        if utils.isPdf(input):
            try:
                fullpath = ''
                print('The file has been created at: {}'.format(fullpath))
            except:
                pass
        print("To be implemented")

    @staticmethod
    def htmlToPdf(input):
        if utils.isUrl(input):
            try:
                fullpath = converter.ToPdfConverter.ConvertHtmlToPdfUrl(input)
                print('The file has been created at: {}'.format(fullpath))
            except:
                print("There was an issue while processing the file.")
        elif utils.isHtml(input):
            try:
                fullpath = converter.ToPdfConverter.ConvertHtmlToPdfUrl(input)
                print('The file has been created at: {}'.format(fullpath))
            except:
                print("There was an issue while processing the file.")


    @staticmethod
    def htmlToTxt(input):
        print(input)

    @staticmethod
    def docToTxt(input):
        print("To be implemented")

    
    @staticmethod
    def docToPdf(input):
        print("To be implemented")

    
    @staticmethod
    def docxToTxt(input):
        print("To be implemented")


    @staticmethod
    def docxToPdf(input):
        print("text")
    
    @staticmethod
    def epubToTxt(input):
        print("text")
    
    @staticmethod
    def epubToPdf(input):
        print("text")
        
options = {
    "0": exit,
    "1": Route.txtToPdf,
    "2": Route.pdfToTxt,
    "3": Route.htmlToPdf,
    "4": Route.htmlToTxt,
    "5": Route.docToTxt,
    "6": Route.docToPdf,
    "7": Route.docxToTxt,
    "8": Route.docxToPdf,
    "9": Route.epubToTxt,
    "10": Route.epubToPdf,
}
