ip_start = input('Please enter the first 3 octets (eg 192.168.0): ')
last_octet = input('Please enter the range of the last octet seperated by a comma (eg 1,254): ')

range_split = last_octet.split(',')
first = int(range_split[0])
last = int(range_split[1]) + 1

for i in range(first,last):
	count = i
	ip = ip_start + '.' + str(count)
	print(ip)
