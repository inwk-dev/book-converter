import os
from fpdf import FPDF 
import pdfkit
from urllib.parse import urlparse
from pathlib import Path
import utils
import constants


class ToPdfConverter():
    """
    The class will handle the conversion to pdf format by given input file and output file.
    """
    @staticmethod
    def ConvertTextToPdf(inputpath):
        """
        Convert text to pdf.
        """
        try:
            print("Starting the conversion...")
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
            
            baseName = utils.retrieveFilename(inputpath)
            outputfilename= baseName + ".pdf"
            fullpath = utils.createFileDestination(constants.DOWNLOAD_LOCATION, outputfilename)
            pdf.output(fullpath) 
            return fullpath  
        except:
            print("There was an issue with the conversion.") 
        


    @staticmethod
    def ConvertHtmlToPdfUrl(urls):
        """
        Convert HTML url/urls to pdf.
        """
        if isinstance(urls, (list,tuple)):
            for url in urls:
                try:
                    filename = utils.retrieveFilename(url)
                    outputfilename= filename + ".pdf"
                    fullpath = utils.createFileDestination(constants.DOWNLOAD_LOCATION, outputfilename)
                    pdfkit.from_url(url,fullpath)
                    return fullpath
                except:
                    print("There was an issue with the conversion.") 
        elif isinstance(urls, str):
            try:
                filename = utils.retrieveFilename(url)
                outputfilename= filename + ".pdf"
                fullpath = utils.createFileDestination(constants.DOWNLOAD_LOCATION, outputfilename)
                pdfkit.from_url(url,fullpath)
                return fullpath
            except:
                print("There was an issue with the conversion.")
    
    @staticmethod
    def ConvertHtmlToPdfFile(files):
        """
        docstring
        """
        if isinstance(files, (list,tuple)):
            for file in files:
                try:
                    filename = utils.retrieveFilename(file)
                    outputfilename= filename + ".pdf"
                    fullpath = utils.createFileDestination(constants.DOWNLOAD_LOCATION, outputfilename)
                    pdfkit.from_file(file, fullpath)
                    return fullpath
                except:
                    print("There was an issue with the conversion.")
        elif isinstance(files, str):
            try:
                filename = utils.retrieveFilename(file)
                outputfilename= filename + ".pdf"
                fullpath = utils.createFileDestination(constants.DOWNLOAD_LOCATION, outputfilename)
                pdfkit.from_file(file, fullpath)
                return fullpath
            except:
                print("There was an issue with the conversion.")

    
    
class ToTxtConverter():
    """
    docstring
    """
    @staticmethod
    def ConvertPdfToTxt(inputpath):
        """
        Convert text to pdf.
        """
        if utils.isPdf(inputpath):
            try:
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
                
                baseName = utils.retrieveFilename(inputpath)
                outputfilename= baseName + ".pdf"
                fullpath = utils.createFileDestination(constants.DOWNLOAD_LOCATION, outputfilename)
                pdf.output(fullpath) 
                return fullpath  
            except:
                print("There was an issue with the conversion") 
        else:
            print("")