source = input("Give infile:\n> ")
dest = "lab1zad1.png"

with open(source, 'rb') as src, open(dest, 'wb') as dst:
        dst.write(src.read())