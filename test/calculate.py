file_name = ["pow_c.txt", "pow_sse.txt", "pow_cl.txt"]
output_name = "output.txt"

fout = open(output_name, "w")
fout.write("pow ")

for name in file_name:
    count = 0
    acc = 0.0
    
    with open(name, "r") as f:
        for line in f:
            _, _, time, _ = line.split()
            acc += float(time)
            count += 1

    avg = acc / count
    fout.write(str(round(avg, 3)) + " ")

fout.write("\n")
fout.close()
