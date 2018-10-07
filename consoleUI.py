print ("Please Choose a Device" + 
       '\n'*1 +
       "1. Desktop"
       '\n'*1 +
       "2. RF Scangun"
       '\n'*1 + 
       "3. Receiving Tablet"
       '\n'*1 +
       "4. Forklift Mounted")
userinput = input()
if userinput == "4":
    print ("Please choose a warehouse" +'\n'*1 
           + "1. LV" + '\n'*1 + "2. HV")
    userinput = input()
    print ('\n'*100)
    if userinput == "1":
        print ("Please choose a job type")
        print ('\n'*1)
        print ("1. Cherry Picker")
        print ('\n'*1)
        print ("2. Motor Driver")
        print ('\n'*1)
        print ("3. Sanitation")
        print ('\n'*1)
        print ("4. Motor Driver")
userinput = input()
if userinput == "1":
        print('\n'*100 + "Next Cherrypick Assignment")
        print('\n'*100 + "1. Next  Assignment")
        print('\n'*1 + "2. Work Remaining")
        print('\n'*1 + "3. Percentage for Current Assignment")  
if userinput == "2":
        print('\n'*100 + "Next Motor Driver Assignment")
elif userinput == "2":
    print ("Please choose a job type")
    print ('\n'*1)
    print ("1. Cherry Picker")
    print ('\n'*1)
    print ("2. Motor Driver")
    userinput = input()
    if userinput == "2":
        print('\n'*100 + "Next  Assignment")
        print('\n'*1 + "Work Remaining")
        print('\n'*1 + "Percentage for Current Assignment")    
    if userinput == "2":
        print('\n'*100 + "Next Motor Driver Assignment")

#print (userinput)
#print (lv)