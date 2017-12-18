file_name = ["pow_c.txt", "pow_sse.txt"]
output_name = "output.txt"

SAMPLES = 30
THREADS = 9

fout = open(output_name, "w")

flist = []

for name in file_name:
    count = 0
    acc = 0.0
    
    fin = open(name, "r");
    
    temp = []

    for i in range(THREADS):
        acc = 0.0
        for j in range(SAMPLES):
            line = fin.readline()
            _, _, time, _ = line.split()
            acc += float(time)

        temp.append(acc / SAMPLES)

    flist.append(temp)

for i in range(THREADS):
    fout.write(str(2 ** i) + " ")
    fout.write(str(round(flist[0][i], 3)) + " ")
    fout.write(str(round(flist[1][i], 3)) + "\n")

fout.close()
