import numpy as np

participants = []
name = " "
while name != "":
    name = input("Enter name: ")
    if name != "":
        participants.append(name)
num = len(participants)
index = np.random.choice(num, num, replace=False)
participants = np.asarray(participants)
print("\nOrder: ")
for i in index:
    print(participants[i])
