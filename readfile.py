fr = open(r"ml-1m/movies.dat", "r")
fw = open("output.txt", "w")
'''
print fr
re = fr.readline()
print re
re = fr.readline()
print re
print "aa\n"
print "bb"
print "aa"
print "bb"
re = fr.read(1)
print re
re = fr.read(2)
print re
re = fr.read(23)
print re
'''
rlist = fr.readlines()
i = 0
while i < len(rlist):
	rec = rlist[i].strip("\n")
	m1 = rec.find("::")
	movieid = rec[:m1]
	m2 = rec.find("::", m1 + 2)
	ny = rec[m1 + 2 : m2]
	name = ny[: ny.rfind("(")]
	year = ny[-5 : -1]
	cates = rec[m2 + 2 :]
	lc = cates.split("|")
	c = ""
	k = 0
	while k < len(lc) - 1:
		c += "%-20s\t" % (lc[k])
		#print lc[k],
		k += 1
	c += "%-20s" % (lc[k])
	print ""
	outstr = "%4s\t%-50s\t%4s\t%-60s\n" % (movieid,name,year, c)
	fw.write(outstr)
	i += 1
fw.close()
fr.close()
