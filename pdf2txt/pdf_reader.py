# Import libraries 
from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os, os.path
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

	return ouput_filename