data = []
f = open("flo_gen_output.txt", "r")
for i in f:
	if "TIME (O.Flow Run-Time   ) (ms)" in i:
		data.append(float(i.split()[-1]))

print("Number of occurences found:",len(data))
print("Maximum number:", max(data))
print("Minimum number:", min(data))
print("Average:", (sum(data)/len(data)))