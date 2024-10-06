def DisplayMenu():
     f=open('F:\PYTHONGROUP-FSS\FileBaseRecordSystem\menu.txt','r')
     if f.mode=="r":
      menuItems=f.read()
      print(menuItems)
     else:
      # try:
       with open("menu.txt","a+") as f:
        f.write('1-Create File')
        f.write('2-Enter Data')
        f.write('3-Display Record')
        f.write('4-Exit System')
        f.close()
        print('Menu Created Successfully!')
        
    #  except:
    #   print('File was not found, now created successfully!')

def CreateFile():
     import os.path
     savedPath='F:\PYTHONGROUP-FSS\FileBaseRecordSystem\dat'
     fname=str(input('enter your name: '))
     pathFileName = os.path.join(savedPath, fname+".txt")         
     # filename=fname+".txt"
     with open(pathFileName,'a+') as fn:
          fn.write(fname) 
          fn.close()
          print('File/Record has been created successfully!')
     
def MembersList():
     import os.path
     savedPath='F:\PYTHONGROUP-FSS\FileBaseRecordSystem\dat'
     allfiles=os.listdir(savedPath)
     namelist=[names.split('.')[0] for names in allfiles]
     # print(os.listdir(savedPath))
     for i in range(len(namelist)):
      #printing list index and list contents below
      print(i,namelist[i],end="\n") 
      
def RecordInformation():
 import RecordsManager as rm
 rf=open('F:\\PYTHONGROUP-FSS\\FileBaseRecordSystem\\recmenu.txt','r')
 if rf.mode=="r":
  recordmenuItems=rf.read()
 print(recordmenuItems)   
 choice=int(input('enter your choice:'))  
 if choice==1:
     rm.AddPersonalRecord()
 else:
     print('Invalid Options, Under Construction!')
     
