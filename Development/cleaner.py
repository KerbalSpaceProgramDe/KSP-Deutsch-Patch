# cleaner.py - Removes doubled lines from the Logfiles
# Copyright (c) 2016 Thomas P.
# Do what you want

# Imports
import glob
import re

# The unique lines
lines = []
            
# Remove the logger prefix            
def no_prefix(l):
    return re.sub(r'\[LOG \d\d:\d\d:\d\d\]: ', '', l)

# Go through all log files
for filename in glob.glob("Logs/*.log"):
    # Log the file
    print('[CLEANER] Parsing file ' + filename)
    
    # Open the file and get all lines
    file = open(filename, 'r+', encoding='utf8')
    lines_ = file.readlines()
    file.seek(0)
    
    # Check all lines
    for line in lines_:
        if no_prefix(line) in lines and line.startswith('[LOG'): continue
        lines.append(no_prefix(line))
        line = line.replace('\n', '\\n')
        if (line.startswith('[LOG') or line.startswith('//')) and not file.tell() == 0:
            file.seek(file.tell() - 2)
            file.write('\n' + line)
        else:
            file.write(line)
    
    # Log
    print('[CLEANER] Removed ' + str(len(lines_) - len(lines)) + ' lines from ' + filename)
    lines = []
    
    # Close the file
    file.truncate()
    file.close()
    