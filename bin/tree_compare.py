#Syntax: python tree_compare.py reftree compdir treeext
#Generating a file 'tree_compare_results.txt' in compdir folder
#storing the comparison of each tree in compdir folder against reftree
#the result in 'tree_compare_results.txt' contain 3 values for 
#each comparison from three different comparison methods provided
#by Dendropy: symmetric difference, euclidean distance and Robinson-Foulds distance

import dendropy
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

def tree_compare(treefile1,treefile2):
	tree1 = dendropy.Tree.get_from_path(treefile1,"newick")
	tree2 = dendropy.Tree.get_from_path(treefile2,"newick")
	return tree1.symmetric_difference(tree2)

if len(sys.argv)!= 4:
	print 'Syntax: python tree_compare.py reftree compdir treeext\n' + \
		'reftree the file containing the reference tree\n' +\
		'compdir: directory containing files of compared trees\n' +\
		'extesion of the files which contain trees in compdir\n'
	sys.exit(-1)

reftree = sys.argv[1]   #the file containing the reference tree
compdir = sys.argv[2]   #directory containing files of compared trees
treeext = sys.argv[3]   #extesion of the files which contain trees in compdir

treefilenames = getfilenames(compdir, treeext)

outputfile = compdir + '/' + 'tree_compare_results.txt'
outfile = open(outputfile,'w')
outfile.write('Reference tree: '+reftree+'\n')
outfile.write('treefilename\t\t\tSymmetric_difference\n')
for treefilename in treefilenames:
	treefilepath = compdir + '/' + treefilename
	symdist = tree_compare(reftree,treefilepath)
	outfile.write(treefilename + '\t' + str(symdist) + '\n')
outfile.close()


