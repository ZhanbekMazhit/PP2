f = open("C:/Users/zhani/OneDrive/Рабочий стол/pp2/lab6/file/ALhABHET","r")
txt = f.read()
f.close()

p = open("C:/Users/zhani/OneDrive/Рабочий стол/pp2/lab6/file/e.txt","w")
p.write(txt)
p.close()