import os
path = "C:/Users/zhani/OneDrive/Рабочий стол/pp2/h"

existence = os.access(path, os.F_OK)
print("Does the path exists:", existence)

readability = os.access(path, os.R_OK)
print("Access to read the file:", readability)

writability = os.access(path, os.W_OK)
print("Access to write to file:", writability)

executability = os.access(path, os.X_OK)
print("Can path be executed:", executability)