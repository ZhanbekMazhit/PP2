import os
k="C:/Users/zhani/OneDrive/Рабочий стол/pp2/h"
path = k
exist = os.access(path, os.F_OK)
if exist == True:
    print("Directory portion:",os.path.dirname(k))
    print("File name:",os.path.basename(k))
else:
    print("Path doesn't exist")