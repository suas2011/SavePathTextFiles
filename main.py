import Controls as con
con.DisplayMenu()
choice=int(input('enter your choice: '))
if choice==1:
    con.CreateFile()
elif choice==2:
    con.MembersList()
elif choice==3:
    con.RecordInformation()
    
else:
    print('Invalid Choice!')

# if __name__=="__DisplayMenu__":
#  DisplayMenu() 
