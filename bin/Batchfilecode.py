#The program takes in input directory, extension of files to be read
#output is files with noise-reduced alignments in results folder.

# Column is considered noisy if
# 1) there are more than 50% indels,
# 2) at least 50% of amino acids are unique,
# 3) no amino acid appears more than twice.
#

#Syntax: >>python Batchfilecode.py input_directory extension_of_file output_dir 
#E.g. >>python Batchfilecode.py asymmetric_0.5/ msl results

import sys
import os
from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment
from Bio.Alphabet import generic_protein
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

#Function to read all the msl files in specified folder

def batchfile(inputdirectory, extension): 		      #Arguments are input directory and extension
	if len(sys.argv)<4:
		sys.stderr.write("Syntax: >>python Batchfilecode.py input_directory extension_of_file output_dir \n E.g. >>python Batchfilecode.py asymmetric_0.5/ msl results")
		sys.exit(-1)
        
	try:
		import os
		Total_files=[]     			       #files are appended into a list Total_files
		for file in os.listdir(inputdirectory):        #Files in the folder
		        if file.endswith(extension) and file.startswith('s'): # Specified extension is read and duplicates are removed
		                Total_files.append(file)       #Files are appended
		        else:
		                continue

		return(Total_files)

	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		sys.exit(-1)

#Three conditions for noise reduction are processed

def processing(seqs, num_col):				       #Argument is the sequences in a file and number of columns
	
	check= len(seqs)
	total= 0        
							       #Check if all sequences have the same length
							       #If the don't have the same length, issue warning
        for i in range(0,len(seqs),1):
                if len(seqs[i]) != num_col:
                        print "Warning: The sequences don't have the same length"
                        break

        #go from last column to first column
        for col in range(num_col-1,-1,-1):
                						#check if the column is noisy
                count = {}                                 	#count of 20 different types of aa
                for seq in seqs:                 	   	#go through all the sequences
                        
                        if seq[col] in 'ARNDCEQGHILKMFPSTWYV':
                                if seq[col] in count:
                                        count[seq[col]] += 1
                                else:
                                        count[seq[col]] = 1
				if (seq[col]=='-'):
                     			total+=1
 		noisy2 = False
		if((len(count)>=(check/2)) or (total>(check/2)) or (len(count)>=(check/2)) and (total>(check/2))):#checks first and second criteria
            		noisy2= True
        	else:
            		noisy2= False

                         
                noisy3 = True
                for k in count:
		         if (count[k]>2):                 	#check for no amino acid appears more than twice
                                noisy3 = False
				break
		seqs = delete(noisy2, noisy3, seqs,col)
		
	return(seqs)

#Delete the noisy columns

def delete(noisy2, noisy3, seqs, col): 	#Arguments are the true/false value of both noisy conditions, sequence and column 
	
	if noisy3 or noisy2:
                        for i in range(len(seqs)):
			        				#remove column col in seq
                                seqs[i] = seqs[i][:col] + seqs[i][col+1:]
                                				#del seq[col]
	return(seqs)

#Writing the non noisy columns to the output file in output folder
			
def writing(seqs,seq_descs,seq_ids, filename): #Arguments are sequence, description, ids, filename

	
	outdir = sys.argv[3] 					#Output directory
	if os.path.isdir(outdir):				#Checks the presence of directory
		print "Directory exists. New directory not created"
	else: 
		command= "mkdir "+ outdir 
		os.system(command)
								#outpath defines path of the subfolder we want to store results in 
			        
	outpath = outdir + '/' + sys.argv[1]
	command = "mkdir " + outpath
	os.system(command)

								#write the result to output
        align = MultipleSeqAlignment([])
	output_file = outpath + '/' + filename + '.' + 'output'
	#print output_file
								#path = outdir + '/'+ output_file
        
	for i in range(len(seqs)):
                align.append(SeqRecord(Seq(seqs[i],generic_protein),id=seq_ids[i],description=seq_descs[i]))
                
        AlignIO.write(align, output_file ,"fasta")

#Read files from input directory one by one	

def readfile(inputdirectory,Total_files):
		
		for i in range(0, len(Total_files)):
			
			path_to_file = inputdirectory+'/'+ Total_files[i]
			seqs = [] 				#store the protein sequences
			seq_ids = [] 				#store the names of the protein sequences in seqs accordingly
			seq_descs = [] 				#store the descriptions of the protein sequences
			
			for record in AlignIO.read(path_to_file,'fasta'):
				seqs.append(str(record.seq))
				seq_descs.append(record.description)
				seq_ids.append(record.id)
		
			num_col = len(seqs[0]) 			#get the number of columns
			#print 'number of columns = ', num_col
			#print 'number of sequences = ', len(seqs)
			
			seqs=processing(seqs, num_col) 		#processing function is called to check for3conditions			
			       
			writing(seqs,seq_descs,seq_ids,Total_files[i]) #writing function is called to write non noisy sequences in ouputfile 


        
Total_files=[] 							#list to append all file names
Total_files = batchfile(sys.argv[1], sys.argv[2]) 		#Calling batchfile function
#print (len(Total_files))					#Printing length of total files

readfile(sys.argv[1],Total_files) 				#Calling readfile function








