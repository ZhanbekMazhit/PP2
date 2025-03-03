import os

path = "C:/Users/zhani/OneDrive/Рабочий стол/pp2/h"

if os.path.exists(path):
    os.remove(path)
else:
    print("The file does not exist")