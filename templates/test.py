print("Vacum Problem")
percept=[["clean"],["dirty"]      ,]
state=[["room A"],["room B",],]
rule={'aClean':'Move right','aDirty':'Suck','bClean':'Move left','bDirty':'suck'}



print("Vacum is in room A? 1 for yes 2 for no ")
x=int(input("enter choice"))
if x==1:
    print("is room dirty? 1 for yes 2 for no ")
    a=int(input("enter choice"))
    if a==1:
        print(rule['aClean'])
        b=int(input("Is vacum in room B?1 for yes 1 for no Enter choice"))
        if b==1:
             print("")
             c=int(input("enter choice"))
             if c==1:
                 print("do you have blood cp")
                 d=int(input("enter choice"))
                 if d==1:
                     print("is your tlc dlc ro tcr high?")
                     e=1
                     if e==1:
                         print(rule['appendictus'])
                     else:
                         print("you are fine and overreacting")
                 else:
                    print("please have blood cp")
             else:
                print("you are fine")