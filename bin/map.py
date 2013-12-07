import sys
from Bio import SeqIO

#The program takes in a fasta file containing noisy alignments and 
#output noise-reduced alignments.
#a column is considered noisy if
# 1) there are more than 50% indels,
# 2) at least 50% of amino acids are unique,
# 3) no amino acid appears more than twice.
# 
if len(sys.argv)<3:
	sys.stderr.write("Syntax: python map.py input_file output_file \n" + \
		"Example: python map.py ..\data\appbio11\asymmetric_0.5\s001.align.1.msl output")
	sys.exit(-1)

try:
	seqs = []     #store the protein sequences
	seq_ids = []  #store the names of the protein sequences in seqs accordingly
	for seq_record in SeqIO.parse(sys.argv[1],'fasta'):
		seqs.append(seq_record.seq)
		seq_ids.append(seq_record.id)
	
	num_col = len(seqs[0])   #get the number of columns
	
	print 'number of alignments = ',len(seqs)
	print 'number of columns = ', num_col
	
	#go from last column to first column
	for col in range(num_col-1,-1,-1):
		#check if the column is noisy
		noisy = False
		for seq in seqs:
			#processing 3 criteria for the noise here
			temp = 0
		if noisy:
			for seq in seqs:
				#remove column col in seq
				temp = 0

except IOError as e:
	print "I/O error({0}): {1}".format(e.errno, e.strerror)
	sys.exit(-1)
	
