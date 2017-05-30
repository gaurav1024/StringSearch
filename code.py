import subprocess
import os
text_to_find = raw_input('What do yoy want to find  :  ')
for (dirpath, dirname, filename) in os.walk('./'):
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