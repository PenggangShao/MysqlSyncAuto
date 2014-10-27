import MySQLdb
import time
fr = open("ml-1m/movies.dat","r")
newfile = file("ml-1m/new.txt","a+")
conn = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="movie")
cur = conn.cursor()

'''
i = 0
while i < 10:
    r1 = fr.readline()
    print r1.strip("\n").split("::")
   # print "------------------------------"
   # print "%s%s%s"%(r1[0],r1[1],r1[2])
   # print r1.split("::")
    i+=1
'''
print "------------------------------"
rlist = fr.readlines()
'''
i = 0
while i <len(rlist):
    r = rlist[i].strip("\n")
    m1 = r.find("::")
    m2 = r.find("::",m1+2)
    print r[0:m1],r[m1+2:m2],r[m2+2:]
    i = i +1
'''
'''
for x in rlist:
     y = x.strip("\n").split("::")
    # print y
    # print y[0],y[1],y[2]
    # my = y[1].split("(")[1][0:4]
     my = y[1][y[1].rfind("(")+1:y[1].rfind(")")]
     mn = y[1][:y[1].rfind("(")]
    # mn = y[1].split("(")[0][0:y[1][0].rfind("(")]
    # print mn,"*",my,"*",
     #s = ""
     
     sql = 'insert into movie_info(movie_name,movie_year) values("%s","%s")'%(mn,my)
     cur.execute(sql)
     conn.commit()
     
     for t in y[2].split("|"):
      #   print t,
         #s = s+t+"\t"
         #newfile.write("%4s\t%-50s\t%4s\t%-60s\n"%(y[0],mn,my,s))
         sql1 = 'insert into category(movie_id,movie_category) values("%s","%s")'%(y[0],t)
         cur.execute(sql1)
         conn.commit()
'''
     sql2 = "select * from movie_info"
     sql3 = "select * from category"
     cur.execute(sql2)
     r = cur.fetchall()
     print r
     cur.execute(sql3)
     r1 = cur.fetchall()
     print r1
    # print ""
    # newfile.write("%4s\t%-50s\t%4s\t%-60s\n"%(y[0],mn,my,s))
newfile.close()
fr.close()
cur.close()
conn.close()
'''
