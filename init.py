import csv
def init(file):
    with open(file,'r') as f:
        content = f.read().split('\n')
    maxpoint = content[-2][1]
    edge = [[0]*int(maxpoint)]*int(maxpoint)
    print edge
    for i in content:
        print i.split(',')
        if len(i.split(','))!=4:
            continue
        else:
            edge[int(i.split(',')[1])][int(i.split(',')[2])] = i.split(',')[3]
            print edge
    return edge
reader = csv.reader(file('topo.csv', 'rb'))
print reader.line_num
print dir(reader)
for line in reader:
    print line
# print init(r'topo.csv')