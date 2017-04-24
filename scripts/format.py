f=open("countries.txt", "r+")
curw=f.readline()
l=""
while curw!="":
	curw=curw.rstrip("\r\n")
	curw="\""+curw+"\", "
	l=l+curw
	curw=f.readline()
f.write(l)
f.close()
