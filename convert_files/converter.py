import os
from fpdf import FPDF 
import pdfkit
from urllib.parse import urlparse
from pathlib import Path
import utils


class ToPdfConverter():
    """
    The class will handle the conversion from text to pdf format by given input file and output file.
    """
    @staticmethod
    def ConvertTextToPdf(inputpath,outputpath):
        """
        Convert text to pdf.
        """
        pdf = FPDF()    
        # Add a page 
        pdf.add_page() 
        # set style and size of font  
        # that you want in the pdf 
        pdf.set_font("Arial", size = 15) 
        # open the text file in read mode 
        f = open(inputpath, "r") 
        # insert the texts in pdf 
        for x in f: 
            pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
        # save the pdf with name .pdf 

        
        pdf.output(outputpath)    

    @staticmethod
    def ConvertHtmlToPdfUrl(urls):
        """
        Convert HTML url/urls to pdf.
        """
        if isinstance(urls, (list,tuple)):
            for url in urls:
                filename = utils.retrieveFilename(url)
                pdfkit.from_url(url,filename)
                print('')
                
        elif isinstance(urls, str):
            filename = utils.retrieveFilename(url)
            pdfkit.from_url(urls,filename)
            print('')
    
    @staticmethod
    def ConvertHtmlToPdfFile(files):
        """
        docstring
        """
        if isinstance(files, (list,tuple)):
            for file in files:
                filename = utils.retrieveFilename(file)
                pdfkit.from_url(file,filename)
                print('')
                
        elif isinstance(files, str):
            filename = utils.retrieveFilename(files)
            pdfkit.from_url(files,filename)
            print('')

    
    
class ToTxtConverter():
    """
    docstring
    """
    pass