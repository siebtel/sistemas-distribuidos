# Import libraries 
from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os, os.path

# import pathlib
# pathlib.Path().resolve()
# Path of the pdf 

''' 
Part #1 : Converting PDF to images 
'''
def pdf2image(file_name):
	file_name = file_name[0]
	file_name = file_name[2:]

	print("pdf to jpg: ", file_name)
	# Store all the pages of the PDF in a variable 
	pages = convert_from_path(file_name, 500) 

	file_name = file_name[5:-4] # retirando extensao e raiz da pasta do arquivo original
	# Counter to store images of each page of PDF to image 
	image_counter = 1

	# Iterate through all the pages stored above 
	for page in pages: 
		# Declaring filename for each page of PDF as JPG 
		# For each page, filename will be: 
		# PDF page 1 -> page_1.jpg 
		# PDF page 2 -> page_2.jpg 
		# PDF page 3 -> page_3.jpg 
		# .... 
		# PDF page n -> page_n.jpg 
		if os.path.isdir("./temp_images/"+str(file_name)+"/"):
			ouput_filename = "./temp_images/" +str(file_name)+"/page_"+str(image_counter)+".jpg"
		else:
			os.mkdir("./temp_images/"+str(file_name))
			ouput_filename = "./temp_images/" +str(file_name)+"/page_"+str(image_counter)+".jpg"

		# Save the image of the page in system 
		page.save(ouput_filename, 'JPEG') 

		# Increment the counter to update filename 
		image_counter = image_counter + 1

	''' 
	Part #2 - Recognizing text from the images using OCR 
	'''
def image2txt(filename):

	outfile = "./txt_from_pdf/" + file_name + ".txt"
	# Variable to get count of total number of pages 
	filelimit = image_counter-1

	# Creating a text file to write the output 

	# Open the file in append mode so that 
	# All contents of all images are added to the same file 
	f = open(outfile, "a") 

	# Iterate from 1 to total number of pages 
	for i in range(1, filelimit + 1): 
		print("jpg to txt: ", i)
		# Set filename to recognize text from 
		# Again, these files will be: 
		# page_1.jpg 
		# page_2.jpg 
		# .... 
		# page_n.jpg 
		filename = "./temp_images/page_"+str(i)+".jpg"
		
		# Recognize the text as string in image using pytesserct 
		text = str(((pytesseract.image_to_string(Image.open(filename))))) 

		# The recognized text is stored in variable text 
		# Any string processing may be applied on text 
		# Here, basic formatting has been done: 
		# In many PDFs, at line ending, if a word can't 
		# be written fully, a 'hyphen' is added. 
		# The rest of the word is written in the next line 
		# Eg: This is a sample text this word here GeeksF- 
		# orGeeks is half on first line, remaining on next. 
		# To remove this, we replace every '-\n' to ''. 
		text = text.replace('-\n', '')

		# Finally, write the processed text to the file. 
		f.write(text)


	# Close the file after writing all the text. 
	f.close() 