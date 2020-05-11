# a=50
# b=a/0
#
# print(b)
# zerodivisionError

import sys
randomlist=['a',0,2]

for entry in randomlist:
    try:
        print('The entry is',entry)
        aaa=1/int(entry)
        break
    except:
        print("Oss",sys.exc_info()[0],"occured")
        print("Next")
        print()
print("Teh recip of",entry,"is",aaa)
