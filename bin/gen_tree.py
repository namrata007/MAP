import sys
import os

def getfilenames(inputdirectory, extension):
	Total_files=[]
	try:
		for file in os.listdir(inputdirectory):
			if file.endswith(extension) and file.startswith('s'):
				Total_files.append(file)
	except:
		print 'The input directory does not exist'
		sys.exit(-1)
	return Total_files


if len(sys.argv)!= 5:
	print 'Syntax: python gen_tree.py indir inext outdir outext\n' + \
		'indir, outdir: input and output directories containing input and output files\n' +\
		'inext, outext: extensions of input and output file\n'
	sys.exit(-1)

subfolders = ['asymmetric_0.5','asymmetric_1.0','asymmetric_2.0',\
				'symmetric_0.5','symmetric_1.0','symmetric_2.0',]
indir = sys.argv[1]
inext = sys.argv[2]
outdir = sys.argv[3]
outext = sys.argv[4]

#create all the subfolders in outdir
for subfolder_name in subfolders:
	inpath = indir + '/' + subfolder_name
	filename_list = getfilenames(inpath,inext)
	if len(filename_list) == 0:
		print "No files with the extension ." + inext + " are found in " + inpath
		continue
	
	#create a folder with the same subfolders' names in outpath
	outpath = outdir + '/' + subfolder_name
	command = "mkdir " + outpath
	os.system(command)
	for filename in filename_list:
		infile_path = inpath + '/' + filename
		outfile_path = outpath + '/' + filename + '.' + outext
		command = "fastprot -I fasta " + infile_path + " -O phylip |fnj -I phylip -O newick  -o " + outfile_path
		os.system(command)
