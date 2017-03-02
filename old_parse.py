f = open('new_debug5.log','r')

lines = f.readlines()
f.close()

usr = 'gekaragi'

for line in lines:
	i = line.find(usr)
	j = line.find('INAC to ACT')
	if ( j !=-1):
		w = line[j:].find('|')
		print (line[i-3:i-1], line[j: w+j])

print ('\n---------------\n')

for line in lines:
	i = line.find(usr)
	j = line.find('ACT to INAC')
	if ( j !=-1):
		w = line[j:].find('|')
		print (line[i-3:i-1], line[j: w+j])

print ('\n---------------\n')

for line in lines:
	i = line.find(usr)
	j = line.find('INAC to CACHE/FREE')
	if ( j !=-1):
		w = line[j:].find('|')
		print (line[i-3:i-1],line[j: w+j])

print ('\n---------------\n')

for line in lines:
	i = line.find(usr)
	j = line.find('FLUSHED')
	if ( j !=-1):
		w = line[j:].find('|')
		print (line[i-3:i-1],line[j: w+j])

print ('\n---------------\n')

for line in lines:
	i = line.find(usr)
	j = line.find('Pages in INACTIVE Queue')
	if ( j !=-1):
		w = line[j:].find('|')
		print (line[i-3:i-1],line[j: w+j])

print ('\n---------------\n')

for line in lines:
	i = line.find(usr)
	l = len(line)
	j = line.find('Pages in ACTIVE Queue')
	if ( j !=-1):
		print (line[i-3:i-1],line[j: l-1])


