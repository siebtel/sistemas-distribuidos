import pdf_reader
import sys, os

# sys.path.append(os.environ['PYDFHOME'])
sys.path.append('../')

from pyDF import *

path = './pdfs/'

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
	return fname



if __name__ == '__main__':
	nprocs = int(sys.argv[1]) # number of processors
	file_list = list_pdfs(sys.argv[2])[:2] # list of files to convert

	graph = DFGraph()
	sched = Scheduler(graph, nprocs, mpi_enabled = False)


	feed_files = Source(file_list)

	convert_file = FilterTagged(pdf_reader.pdf2image, 1)  

	pname = Serializer(print_name, 1)


	graph.add(feed_files)
	graph.add(convert_file)
	graph.add(pname)


	feed_files.add_edge(convert_file, 0)
	convert_file.add_edge(pname, 0)


	sched.start()

