def batchfile(extension, inputdirectory):
	import os
	Total_files=[]
	for file in os.listdir(inputdirectory):
		if file.endswith(extension) and file.startswith('s'):
			Total_files.append(file)
		else:
			continue

	print len(Total_files)
	print Total_files

import sys

batchfile(sys.argv[2], sys.argv[1])
