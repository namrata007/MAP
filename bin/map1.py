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
        seqs = [] #store the protein sequences
        seq_ids = [] #store the names of the protein sequences in seqs accordingly
        for seq_record in SeqIO.parse(sys.argv[1],'fasta'):
                seqs.append(seq_record.seq)
                seq_ids.append(seq_record.id)
        
        num_col = len(seqs[0]) #get the number of columns
        
        print 'number of alignments = ',len(seqs)
        print 'number of columns = ', num_col
        
        #go from last column to first column
	final=[]
	for col in range(0,num_col,1):
		#check if the column is noisy
		p=0
		t=-1
		count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #count of 20 different types of aa
		noisy = False
		for seq in seqs:
		        #processing 3 criteria for the noise here
			print(seq[col])
			if(seq[col]=='A'):
						count[0]+=1
			if(seq[col]=='R'):
						count[1]+=1
			if(seq[col]=='N'):
						count[2]+=1
			if(seq[col]=='D'):
						count[3]+=1
			if(seq[col]=='C'):
						count[4]+=1
			if(seq[col]=='E'):
						count[5]+=1
			if(seq[col]=='Q'):
						count[6]+=1
			if(seq[col]=='G'):
						count[7]+=1
			if(seq[col]=='H'):
						count[8]+=1
			if(seq[col]=='I'):
						count[9]+=1
			if(seq[col]=='L'):
						count[10]+=1
			if(seq[col]=='K'):
						count[11]+=1
			if(seq[col]=='M'):
						count[12]+=1
			if(seq[col]=='F'):
						count[13]+=1
			if(seq[col]=='P'):
						count[14]+=1
			if(seq[col]=='S'):
						count[15]+=1
			if(seq[col]=='T'):
						count[16]+=1
			if(seq[col]=='W'):
						count[17]+=1
			if(seq[col]=='Y'):
						count[18]+=1
			if(seq[col]=='V'):
						count[19]+=1

		print count               #print count of all types of aa
		for k in range(0,20):
			if (count[k]<2):  # check for noise
				noisy = True
				t=col+1
			else:
				noisy = False
				p=1			
				break
	
			if(noisy == False and p==1):
				final.append(seq[col])
				break
		if(noisy == True and t!=-1):
			
			print "column ", t, "is noisy"
		
			
		
	print final
except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        sys.exit(-1)

