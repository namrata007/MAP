import sys
import os

def batchfile(inputdirectory, extension):
	Total_files=[]
	try:
		for file in os.listdir(inputdirectory):
			if file.endswith(extension) and file.startswith('s'):
				Total_files.append(file)
	except:
		print 'The input directory does not exist'
		sys.exit(-1)
	return Total_files


if len(sys.argv)!= 7:
	print 'Syntax: python cal_diff_matrix.py indir inext intype outdir outext outtype \n' + \
		'indir, outdir: input and output directories containing input and output files\n' +\
		'inext, outext: extensions of input and output file\n' + \
		'intype, outtype: format of the files, only accept either "fasta" or "phylip"\n'
	sys.exit(-1)

indir = sys.argv[1]
inext = sys.argv[2]
intype = sys.argv[3]

outdir = sys.argv[4]
outext = sys.argv[5]
outtype = sys.argv[6]

#look for all files with extension inext in the directory indir
file_list = batchfile(indir, inext)
if len(file_list) == 0:
	print 'No files with the extension given found'
	sys.exit(-1)

for file_name in file_list:
	infile_path = indir + '/' + file_name
	outfile_path = outdir + '/' + file_name + '.' + outext

	command = "fnj -I " + intype + " " + infile_path + " -O " + outtype + " -o " + outfile_path
	os.system(command)
