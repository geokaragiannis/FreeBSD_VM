import sys

# Usage: python parse.py file.log

usage = "Usage: python parse.py file.log"
numArgs = len(sys.argv) -1
# Make sure to start from 1 not 0

# Check arguments
print ('\n---------------\n')
print('Number of Arguments:', numArgs, 'arguments.')

if numArgs is 0:
	print("\nNo log file specified\n")
	print(usage)
	print("Exiting ...\n")
	exit(1);
elif numArgs > 1:
	print("\nToo many log files specified\n")
	print(usage)
	print("Exiting ...\n")
	exit(1);

print('Log File:', sys.argv[1])
print ('\n---------------\n')

# Open file specified by argument
f = open(sys.argv[1],'r')

lines = f.readlines()
f.close()

print('INAC to ACT')
for line in lines:							#					       vv We use these for line numbers (i+4:i+6) 
	i = line.find(':')						# Goes to time stamp ##:##:##
	j = line.find('INAC to ACT')			#                 Here ^    
	if ( j !=-1):
		w = line[j:].find('|')
		print (line[j+12: w+j])

print ('\n---------------\n')
print('ACT to INAC')

for line in lines:
	i = line.find(':')
	j = line.find('ACT to INAC')
	if ( j !=-1):
		w = line[j:].find('|')
		print (line[j+12: w+j])

print ('\n---------------\n')

print('INAC to CACHE/FREE')
for line in lines:
	i = line.find(':')
	j = line.find('INAC to CACHE/FREE')
	if ( j !=-1):
		w = line[j:].find('|')
		print (line[j+20: w+j])

print ('\n---------------\n')

print('FLUSHED')
for line in lines:
	i = line.find(':')
	j = line.find('FLUSHED')
	if ( j !=-1):
		w = line[j:].find('|')
		print (line[j+8: w+j])

print ('\n---------------\n')

print('Pages in INACTIVE Queue')
for line in lines:
	i = line.find(':')
	j = line.find('Pages in INACTIVE Queue')
	if ( j !=-1):
		w = line[j:].find('|')
		print (line[j+25: w+j])

print ('\n---------------\n')

print('Pages in ACTIVE Queue')
for line in lines:
	i = line.find(':')
	l = len(line)
	j = line.find('Pages in ACTIVE Queue')
	if ( j !=-1):
		print (line[j+23: l-1])

print ('\n---------------\n')
print('Active scanned')
m = 0
for line in lines:
	i = line.find(':')
	l = len(line)
	j = line.find('Active Scanned')
	if ( m%2 == 0 and j !=-1):
		print (1)
	elif ( m%2 == 0 and j ==-1):
		print (0)
	m = m+1

print ('\n---------------\n')
print('Inactive scanned')
m = 0
for line in lines:
	i = line.find(':')
	l = len(line)
	j = line.find('Inactive Scanned')
	
	if ( m%2 == 0 and j !=-1):
		print (1)
	elif ( m%2 == 0 and j ==-1):
		print (0)
	m = m+1


