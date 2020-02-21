input = open("d.txt", "r")
output = open("01.txt", "w")
for line in input:
    datalist = line.strip().split("\t")
    sno,country,points,price,province = datalist
    if len(country) != 0:
        if len(price) != 0:
            output.write(country + "\t" + price + "\n")

input.close()
output.close()