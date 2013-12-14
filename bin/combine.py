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
total=temp=0
noisyones=nonnoisy=0
remove=[]
keep=[] #stores a list of noisy and non noisy columns based on second criteria

try:
    seqs = []     #store the protein sequences
    seq_ids = []  #store the names of the protein sequences in seqs accordingly
    for seq_record in SeqIO.parse(sys.argv[1],'fasta'):
        seqs.append(seq_record.seq)
        seq_ids.append(seq_record.id)
    num_col = len(seqs[0])   #get the number of columns
    
#Check if all sequences have the same length
#If the don't have the same length, issue warning
    for i in range(1,len(seqs),1):
        if len(seqs[i]) != num_col:
            print "Warning: The sequences don't have the same length"
            break

    print 'number of alignments = ',len(seqs)
    print 'number of columns = ', num_col
    check= len(seqs)

 #go from first column to last column
    for col in range(0,num_col):
 #check if the column is noisy based on second criteria
        noisy = False
        for seq in seqs:
                    if seq[col] in 'ACDEFGHIKLMNPQRSTVWY':
                        each=seq[col]
                        if each in count:
                            count[each]=count[each]+1
                        else:
                            count[each]=1
                    if (seq[col]=='-'):
                       total+=1
    
        if((len(count)>=(check/2)) or (total>(check/2)) or (len(count)>=(check/2)) and (total>(check/2))):#checks first and second criteria
            noisy= True
        else:
            noisy= False
        
        if noisy:
            noisyones=noisyones+1
            temp=col+1
            remove.append(temp) #Appends each noisy column in the list
            temp=0
        else:
            nonnoisy=nonnoisy+1
            temp=col+1
            keep.append(temp) #Appends each non noisy column in the list
            temp=0
        noisy =False
        count={}
        total=0
    print 'Noisy columns:',noisyones,' Non noisy columns:',nonnoisy,'\n'
    print 'Remove: ',remove,'\n','\n'
    print 'Keep: ',keep


except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    sys.exit(-1)  

