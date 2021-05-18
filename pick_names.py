import numpy as np

participants = []
name = " "
while name != "":
    name = input("Enter name: ")
    if name != "":
        participants.append(name)
index = np.random.choice(len(participants), len(participants), replace=False)
participants = np.asarray(participants)
print("\nOrder: ")
for i in index:
    print(participants[i])
