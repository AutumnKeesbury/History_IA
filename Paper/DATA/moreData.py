import numpy as np

path = 'output.dat'

yrs = []
pcntgs = []

with open(path, 'r') as file:
    next(file)
    for line in file:
        parts = line.strip().split()
        yrs.append(float(parts[0]))
        pcntgs.append(float(parts[1]))

pcntgs = np.array(pcntgs)

print(pcntgs[36])
print(pcntgs.max())

for i in range(pcntgs.size):
    if pcntgs[i] == pcntgs.max():
        print(yrs[i])


def get_percent(year: float):
    return pcntgs[yrs.index(year)]

def get_year(percent: float):
    if pcntgs.index(percent) is None:
        return 0
    else:
        return yrs[pcntgs.index(percent)]

print("In 1851, cotton made up", get_percent(1851), "% of the total value of exports in the United States.")
print("In 1860, cotton made up", get_percent(1860), "% of the total value of exports in the United States.")