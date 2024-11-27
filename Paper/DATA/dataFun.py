path = 'C:\Users\Autum\Desktop\History_IA\Paper\DATA\cotton_v_total_exports.dat'

with open(path, 'r') as file:
    for line in file:
        print(line.strip())