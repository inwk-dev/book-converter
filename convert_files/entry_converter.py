import sys, getopt
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


choices = {
   "0": ". Exit",
   "1": ". Convert HTML to PDF from URL",
   "2": ". Convert HTML to PDF from file",
   "3": ". Convert PDF to TXT",
   "4": ". Convert TXT to PDF",
   "5": ". Convert DOC to TXT",
   "6": ". Convert DOC to PDF",
   "7": ". Convert DOCX to TXT",
   "8": ". Convert DOCX to PDF",
   "9": ". Convert EPUB to TXT",
   "10": ". Convert EPUB to PDF"
}

if __name__ == "__main__":
   correctChoice = False
   print("\n\n\n\n")
   print("Select from one of the following options:")
   print("=========================================")
   print("\n\n")

   #Display Menu
   for key,value in choices.items():
      print(key,value)
   
   #Make selection
   choice = input("Your selection is: ")      
   while utils.checkChoice(choice,choices) == False:
      print("Invalid choice.")
      choice = input("Your selection is: ")      
   else: 
      if choice == "0":
         quit()
      inputFile = input("Type the filepath to the file: ")
      print("\n\n")
      try:
         Route.make_choice(choice,inputFile)      
      finally:
         return
      
   print("")
   
   