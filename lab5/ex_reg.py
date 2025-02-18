import re

with open("lab5/row.txt", encoding="utf-8") as f:  
    data = f.read()
    
print("task1")
match = re.findall(r"ab*", data)  
print(match)

print("task2")
match = re.findall(r"ab{2,3}", data)
print(match)

print("task3")
match = re.findall(r"[a-z]+_[a-z]+", data)
print(match)

print("task4")
match = re.findall(r"[A-Z][a-z]+", data)
print(match)

print("task5")
match = re.findall(r"a.*b", data)
print(match)

print("task6")
match = re.sub(r"[ ,.]",":",data)
print(match)

print("task7")
match = re.sub(r"_","",data)
print(match)

print("task8")
match = re.findall(r"[A-Z][^A-Z]*",data)
print(match)

print("task9")
match = re.findall(r"[A-Z][a-z]*",data)
print(match)

print("task10")
match = re.sub(r"[A-Z]"," ",data)
print(match)