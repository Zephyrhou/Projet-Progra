import os

b_file = open("C:/Users/Aude/Desktop/board.txt", 'r')
lecture = []
lines = []
lines += b_file.readlines()

for line in lines:
    line = line.replace('\n', '')
    line = line.replace(':', '')
    line = line.split(' ')
    lecture += line
print(lecture)

b_file.close()
