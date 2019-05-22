filenames = ['Letters.txt', 'Letters_ч.txt']
with open('Output.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)