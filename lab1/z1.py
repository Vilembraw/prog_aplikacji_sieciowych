source = input("Give infile:\n> ")
dest = "lab1zad1.txt"

with open(source, 'r') as src, open(dest, 'w') as dst:
    for line in src:
        dst.write(line)