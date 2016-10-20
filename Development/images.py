# images.py - Generates an image config for KDP
# Copyright (c) 2016 Thomas P.
# Do what you want

# Imports
import glob
import sys
import os
import os.path

# The final config
config = """// **************
// KSP-Deutsch-Patch: Übersetzt KSP ins Deutsche
// Copyright (c) 2016 kerbalspaceprogram.de
// 
// Images.cfg: Ersetzt die Spielgrafiken die Texte enthalten
// Autor: Von image.py generiert
// **************

LANGUAGEPATCHES
{
"""

# Go through all image files
for filename in glob.glob(sys.argv[1] + '/*'):
	# Log the file
	print('[IMAGE] Found image ' + filename)
	
	# add config
	name = os.path.basename(filename).split('.')[0]
	config += """	IMAGE
	{
		name = """ + name + """
		file = """ + sys.argv[2] + name + """
	}
"""

# Finish the file and save it
config += '}'

if os.path.exists("Images.cfg"):
	file = open("Images.cfg", "r+")	
else:
	file = open("Images.cfg", "w")
file.seek(0)
file.write(config)
file.close()