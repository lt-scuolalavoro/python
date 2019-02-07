import linecache
# Funzione che restituisce una lista contenente i valori analizzati.
def parser(filename, nImgs, firstLine, linesDifference):
	data = []
	i=firstLine
	while i<nImgs*linesDifference:
		data.append(float(linecache.getline(filename, i).split()[-1]))
		i+=linesDifference
	return data

# Funzione che restituisce il numero di immagini,
# la prima linea in cui si trova la frase passata e 
# la differenza di righe che c'è tra una frase e l'altra.
# Questi dati servono per velocizzare il parser
# e per farlo funzionare per qualsiasi riga che si voglia analizzare nel documento.

def rule(filename, phrase):
	f = open(filename, "r")
	firstLine=0
	firstLineFound=False
	nImgs=0
	nRows=0
	for i in f:
		nRows+=1
		if not firstLineFound:
			firstLine+=1
		if phrase in i:
			nImgs+=1
			if not firstLineFound:
				firstLineFound=True
		if (nImgs==1):
			linesDifference=nRows+1-firstLine
	return nImgs, firstLine, linesDifference
	
filename="flo_gen_output.txt"
# info: lista che contiene i risultati della funzione rule
info=rule(filename, "TIME (O.Flow Run-Time   )")
# data: lista che contiene i valori analizzati in base al risultato di rule
data=parser(filename, info[0], info[1], info[2])
print("Values scanned: %d" % len(data))
print("Maximum value: %s" % max(data))
print("Minimum value: %s" % min(data))
print("Average value: %.3f" % (sum(data)/len(data)))