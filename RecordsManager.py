def AddPersonalRecord():
    import os
    personalData=[]
    
    savedPath='F:\PYTHONGROUP-FSS\FileBaseRecordSystem\dat'
    pname=str(input('enter your FileName: '))
    pathFileName = os.path.join(savedPath, pname+".txt")             
    f=open(pathFileName,'a+')
    # f.writelines(personalData)
    print('\nYou can add 1 field at a time')
    print('\nYou can add: Float|Integer|String Data.\nType the Data Type Names for the Input.')
    fieldnamequestion=str(input('\nwhich field you want to add?').lower())
     
    if fieldnamequestion=='string':
      sfield=str(input('enter Field Name: '))
      sfield=str(input('enter your '+sfield+": "))
      personalData.append(sfield)
        
     
    elif fieldnamequestion=='float':
      ffield=str(input('enter Field Name: '))
      ffield=float(input('enter your '+ffield+": "))
      sffield=str(ffield)
      personalData.append(sffield)
    
    elif fieldnamequestion=='integer':
      ifield=str(input('enter Field Name: '))
      ifield=int(input('enter your '+ifield+": "))
      sifield=str(ifield)
      personalData.append(sifield)
    else:
      print('The data type you entered ',fieldnamequestion,' is not available')
    f.writelines(personalData)
    f.close()
    # print(personalData)     
    
def AddQualifications():
    pass
def AddExperience():
    pass
def AddFamilyInformation():
    pass
def ExitRecordManager():
    pass
