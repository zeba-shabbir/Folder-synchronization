import os,shutil,logging,time
from datetime import datetime

def folder_synchronization(srcpath,destinationpath,logfile_path):
     
#  path = "C:/Users/zebashabbir/Desktop/source"
#  destinationpath="C:/Users/zebashabbir/Desktop/destination"

 logging.basicConfig(filename=logfile_path+"logfile.txt" , level=logging.INFO)
 logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
 destlist= os.listdir(destinationpath)

 fileList = os.listdir(srcpath)
 # list that contain files that need to be replaced from dst folder
 deletefiles_list= []

 # creating new files in dst from src
 for i in fileList:
     # check if any file of source is present in destination
     if any(i in destlist for x in fileList):
         deletefiles_list.append(i)
         continue    
    
     shutil.copy("C:/Users/zebashabbir/Desktop/source/"+i ,"C:/Users/zebashabbir/Desktop/destination/")
     logging.info("copying file..."+i)
     print("copying file... "+ i)

 # deleting extra files from dst
 for i in destlist:
     flag=0
     for j in fileList:
         if i==j:
             flag=1

     if flag==0:
            print("deleting file from dst folder...",i)
            logging.info("deleting file from destination folder... "+i)
            os.remove("C:/Users/zebashabbir/Desktop/destination/"+i)
            



    
 # delete file from destination and then recreate similar to src so that updated one is in dst folder

 for i in deletefiles_list:
     os.remove("C:/Users/zebashabbir/Desktop/destination/"+i)
     logging.info("deleting file from dst folder.. "+i)
     print("deleting file ..."+i)

 for i in deletefiles_list:
     shutil.copy("C:/Users/zebashabbir/Desktop/source/"+i ,"C:/Users/zebashabbir/Desktop/destination/")
     print("creating file..."+i)
     logging.info("creating file in dst folder.."+i)

##################################################

def myfunc(count):
 print(datetime.now())
 print(count)

srcpath=input("Please enter source folder path.. ")
dstpath=input("please enter destination folder path.. ")
logfile_path=input("Please enter log file path.. ")
interval=input("PLease enter time in seconds after which you want the synchronization to be performed")

# example folder path for log file : C:/Users/zebashabbir/Desktop/

interval=float(interval)

next=time.time()

count=1
while True: 
  next =next+interval
#   myfunc(count)
  folder_synchronization(srcpath,dstpath,logfile_path)
  time.sleep(max(0, next - time.time()))
  count=count+1
 




    
