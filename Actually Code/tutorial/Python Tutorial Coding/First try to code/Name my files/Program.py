import os

os.listdir(r"C:\Users\aleja\Desktop")
os.listdir(r"C:\Users\aleja\Desktop/Vicio")
counter = 1
files = []
out = 0

for file in os.listdir(r"C:\Users\aleja\Desktop"):
    files.append(file)
    print(counter, file)
    counter = counter+1

for file in os.listdir(r"C:\Users\aleja\Desktop/Vicio"):
    files.append(file)
    print(counter, file)
    counter = counter+1


