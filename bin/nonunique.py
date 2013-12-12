import sys
from Bio import SeqIO

#The program takes in a fasta file containing noisy alignments and 
#output noise-reduced alignments.
#A column is considered noisy if
# 1) there are more than 50% indels,
# 2) at least 50% of amino acids are unique,
# 3) no amino acid appears more than twice.
# 

if len(sys.argv)<2:
    sys.stderr.write("Syntax: python map.py input_file output_file \n" + "\n"+"Example: python map.py ..\data\appbio11\asymmetric_0.5\s001.align.1.msl output")
    sys.exit(-1)

#parameter list for checking noisy columns
count={} #stores each amino acid and its total occurence in the alignment
total=0
noisyones=nonnoisy=0
result=[] #stores a list of noisy and non noisy columns based on second criteria

try:
    seqs = []     #store the protein sequences
    seq_ids = []  #store the names of the protein sequences in seqs accordingly
    for seq_record in SeqIO.parse(sys.argv[1],'fasta'):
        seqs.append(seq_record.seq)
        seq_ids.append(seq_record.id)
    num_col = len(seqs[0])   #get the number of columns
    
#Check if all sequences have the same length
#If they don't have the same length, issue warning
    for i in range(1,len(seqs),1):
        if len(seqs[i]) != num_col:
            print "Warning: The sequences don't have the same length"
            break

    print 'number of alignments = ',len(seqs)
    print 'number of columns = ', num_col


 #go from first column to last column
    for col in range(0,num_col,1):
 #check if the column is noisy based on second criteria
        noisy = False
        for seq in seqs:
                    if seq[col] in 'ACDEFGHIKLMNPQRSTVWY':
                        total+=1
                        each=seq[col]
                        if each in count:
                            count[each]=count[each]+1
                        else:
                            count[each]=1
    
        if(len(count)>=(total/2)): #checks if atleast fifty percent of the amino acids are unique
            noisy= True
        else:
            noisy= False
        
        if noisy:
            noisyones=noisyones+1
            result.append(1) #Appends 1 for each noisy column in the list
        else:
            nonnoisy=nonnoisy+1
            result.append(0) #Appends 0 for each non noisy column in the list
    
    print 'Noisy columns:',noisyones,' Non noisy columns:',nonnoisy
    print result

except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    sys.exit(-1)  

