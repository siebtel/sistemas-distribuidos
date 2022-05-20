import sys, os
import time
from pdf2image import convert_from_path 

sys.path.append(os.environ['PYDFHOME'])
sys.path.append('../')

from pyDF import *


def list_pdfs(rootdir):
    fnames = []

    for current, directories, files in os.walk(rootdir):
        for f in files:
            fnames.append(current + '/' + f)

    fnames.sort()
    return fnames

def print_name(args):
	fname = args[0]
	print("args", args)
	print("Converted %s" %fname)

def pdf2image(file_name):
	file_name = file_name[0]
	file_name = file_name[2:]

	print("pdf to jpg: ", file_name)
	# Store all the pages of the PDF in a variable 
	pages = convert_from_path(file_name, timeout=1000) 

	file_name = file_name[5:-5] # retirando extensao e raiz da pasta do arquivo original
	# Counter to store images of each page of PDF to image 
	image_counter = 1
	ouput_filename = ""
	# Iterate through all the pages stored above 
	for page in pages:
		print("Page: ", image_counter)
		# Declaring filename for each page of PDF as JPG 
		# For each page, filename will be: 
		# PDF page 1 -> page_1.jpg 
		# PDF page 2 -> page_2.jpg 
		# PDF page 3 -> page_3.jpg 
		# .... 
		# PDF page n -> page_n.jpg 
		ouput_filename = ".\\temp_images\\" +str(file_name)+"_page_"+str(image_counter)+".jpeg"

		# Save the image of the page in system 
		page.save(ouput_filename, 'JPEG') 

		# Increment the counter to update filename 
		image_counter = image_counter + 1

	return ouput_filename

if __name__ == '__main__':
	start = time.time()
	nprocs = int(sys.argv[1]) # number of processors
	file_list = list_pdfs(sys.argv[2])[:6] # list of files to convert
	print("file_list: ", file_list)
	graph = DFGraph()
	sched = Scheduler(graph, nprocs, mpi_enabled = False)


	feed_files = Source(file_list)

	convert_file = FilterTagged(pdf2image, 1)  

	pname = Serializer(print_name, 1)


	graph.add(feed_files)
	graph.add(convert_file)
	graph.add(pname)


	feed_files.add_edge(convert_file, 0)
	convert_file.add_edge(pname, 0)


	sched.start()
	end = time.time()
	print(str(end - start) + ' time elapsed')