import linecache
r=10
n = 194
data = []
for i in range(n):
 riga = linecache.getline("flo_gen_output.txt", r) 
 data.append(float(riga.split()[-1]))
 r=r+12
 
print("Valore Max:%s"%max(data))
print("Valore Min: %s"%min(data))
print("Media: %f"%(sum(data)/len(data)))