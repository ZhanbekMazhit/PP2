import json

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")  
print("-------------------------------------------------- --------------------  ------  ------")

with open("lab4/sample-data.json") as file:
    a = json.load(file)

i = 0

while i != 3:
    topology = a["imdata"][i]["l1PhysIf"]["attributes"]["dn"]
    speed = a["imdata"][i]["l1PhysIf"]["attributes"]["speed"]
    MTU = a["imdata"][i]["l1PhysIf"]["attributes"]["mtu"]
    print(topology,"                            ", speed ," ", MTU)
    i+=1