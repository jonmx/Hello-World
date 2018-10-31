import os
import os.path
import datetime
import re
import csv
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# need modify 
gpufrac="0.5"
refdir="~/facenet/datasets/lfw/raw/Adam_Sandler"
target="~/facenet/datasets/lfw/raw/Abdul_Majeed_Shobokshi/Abdul_Majeed_Shobokshi_0001.jpg"
compare_py="~/facenet/facenet-master/src/compare.py"
MODELS="~/facenet/20180402-114759"

restr=r'0\s+0.0000\s+(.*)'

date=datetime.datetime.now()
log=date.strftime('%Y%m%d-%H%M%S')+".log"
excel=date.strftime('%Y%m%d-%H%M%S')+".csv"
  
reflist=os.listdir(refdir)
for i in range(0,len(reflist)):
    print(refdir+"/"+reflist[i]+" compared to "+target)
    os.system("python "+compare_py+" "+MODELS+" "+refdir+"/"+reflist[i]+" "+target+" --gpu_memory_fraction="+ gpufrac +" >>"+log) 


distance =[];    
with open(log) as flog:
    for line in flog:
#        print(line)
        so=re.search(restr,line)
        if so:
             print(so.group(1))
             distance.append(so.group(1))

rows=[]
for i in range(0,len(reflist)):
    rows.append([reflist[i],distance[i]])

os.mknod(excel)
with open(excel,"w") as fexcel:
    writer = csv.writer(fexcel)
    writer.writerows(rows) 
             
