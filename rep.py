# -*- coding: UTF-8 -*-

#newtest
#add newtest
#testing
#add testing

import sys,getopt,time,re
 
startNumber=1
seq=0

def appnum(matched):
    global seq, startNumber
    value=matched.group('value')+str(seq+startNumber)
    seq=seq+1
    return value

def main(argv):
    searchStr=""
    inputfile=""
    outputfile="output.txt"
    global seq,startNumber
    
    try:
      opts, args = getopt.getopt(argv,"hi:o:s:r:n:")
    except getopt.GetoptError:
      print("replace search-str in <inputfile> with search-str and sequence number format as search-str%d")
      print("usage: rep -i <inputfile> -o <outputfile> -s <search-str> -n <startNumber=1>")
      sys.exit(2)
      
    for opt, arg in opts:
      if opt == '-h':
        print("replace search-str in <inputfile> with search-str and sequence number format as search-str%d")
        print("usage: rep -i <inputfile> -o <outputfile> -s <search-str> -n <startNumber=1>")
        sys.exit()
      elif opt =="-i":
         inputfile = arg
      elif opt =="-o":
         outputfile = arg
      elif opt =="-s":
         searchStr = arg
      elif opt =="-n":
         startNumber = int(arg)
    if searchStr=="" or inputfile=="":
        print("usage: rep -i <inputfile> -o <outputfile=output.txt> -s <search-str> -r <replace-str> -n <startNumber=1>")
        sys.exit()
    print ('Search str is：', searchStr)
    print ('Sequence number starts from：', startNumber)

    try:
        fi = open(inputfile, "r",encoding='utf-8')
        fo = open(outputfile,"w",encoding='utf-8')
    except:
        print ("Fail to open files")
        print ('inputfile is：', inputfile)
        print ('outputfile is：', outputfile)
        sys.exit(3)
    
    i=0
    while True:
        line = fi.readline()
        if not line: break
        
        fo.write(re.sub(r'(?P<value>'+searchStr+')',appnum,line))
        i=i+1
        sys.stdout.write("\r"+str(i)+" lines processed, "+str(seq)+" replaced")
        sys.stdout.flush()
        #time.sleep(0.1)
        
    print ("")
    fi.close()
    fo.close()
    print ("Saved in",outputfile)
    
if __name__ == "__main__":
   main(sys.argv[1:])
