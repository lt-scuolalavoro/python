import linecache
values = []
i=10
while(i<=2326):
    values.append(float(linecache.getline("flo_gen_output.txt", i).split(":")[1]))
    i+=12

print(max(values))
print(min(values))
print("%.8s" %(sum(values)/len(values)))
print(len(values))