import subprocess
import os
text_to_find = raw_input('What do you want to find  :  ')
target_directory = raw_input('Please enter the path of the target directory  :  ')
for (dirpath, dirname, filename) in os.walk(target_directory):
	for file in filename:
		filepath = dirpath+file
		output = subprocess.check_output(['file', filepath])
		output = output.strip()
		if 'text' in output.split(':')[-1]:
			f1 = open(filepath)
			for line in f1:
				if text_to_find in line:
					print 'Text found in ', filepath
					break