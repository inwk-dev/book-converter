import sys, getopt
import router
from router import Route
import utils

def main(argv):
   inputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
   print('Input file is "', inputfile)

# html to pdf
# html to txt
# txt to pdf
# doc to txt
# doc to pdf
# docx to txt
# docx to pdf
# epub to txt
# epud to pdf


options = {
   "0": ". Exit",
   "1": ". Convert TXT to PDF",
   "2": ". Convert PDF to TXT",
   "3": ". Convert HTML to PDF from URL",
   "4": ". Convert HTML to PDF from .HTML",
   "5": ". Convert DOC to TXT",
   "6": ". Convert DOC to PDF",
   "7": ". Convert DOCX to TXT",
   "8": ". Convert DOCX to PDF",
   "9": ". Convert EPUB to TXT",
   "10": ". Convert EPUB to PDF"
}

if __name__ == "__main__":
   print("\n\n\n\n")
   print("Select from one of the following options:")
   print("=========================================")
   print("\n\n")

   #Display Menu
   utils.showMenu(options)
   
   #Make selection
   choice = input("Your selection is: ").strip()      
   while utils.checkChoice(choice,options) == False:
      print("Invalid choice.")
      print("\n\n")
      choice = input("Your selection is: ")
      print("\n\n")
   else: 
      if choice == "0":
         quit()
      inputFile = input("Type the filepath to the file: ").strip()
      print("\n\n")
      try:
         utils.make_choice(choice,inputFile,router.options)      
      finally:
         utils.showMenu(options)
      
   
   