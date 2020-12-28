import os

path_Input = input()
os.chdir(path_Input)
f_list = os.listdir(path_Input)
f_data = []

for i in range(len(f_list)):
    f_stat = os.stat(f_list[i])
    data = [f_list[i], f_stat.st_size]
    f_data.append(data)

for i in range(0, len(f_data)-1):
    for j in range(0, len(f_data)-i-1):
        if f_data[j][1] < f_data[j+1][1]:
            f_data[j], f_data[j+1] = f_data[j+1], f_data[j]
print('\n', f_data)




