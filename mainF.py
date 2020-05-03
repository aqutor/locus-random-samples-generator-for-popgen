import csv
import random
import os

# Run
# Windows: python3 mainF.py
# Linux/macOs: python mainF.py

# Config
k = 15
count = 100
output_type = 2  # 1: separate output  2:

# Calculate

with open('macReversedSample.csv') as f:
    data = [tuple(line) for line in csv.reader(f)]

i = 0
if output_type == 1:
    while i < count:
        samples = random.sample(data, k)
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, 'results', str(count), str(k), 'sample_' + str(k) + '_' + str(i) + '.csv')
        f = open(abs_file_path, 'w+')
        title = "/*Test Data Set I: Diploid */\nnumber of populations = 1\nnumber of loci = 79\nlocus name:\n"
        f.write(title)

        for a in samples:
            for b in a:
                f.write(b)
                f.write(', ')
            f.write('\n')
        f.close()
        i = i + 1
else:
    samples = random.sample(data, k)
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, 'results',
                                 'sample_' + str(count) + '_' + str(k) + '.csv')
    f = open(abs_file_path, 'w+')
    title = "/*Test Data Set I: Diploid */\nnumber of populations = " + str(count) + "\nnumber of loci = 79\nlocus name:\n"
    f.write(title)
    f.close()
    f = open(abs_file_path, 'a')

    while i < count:
        f.write('name = ' + str(i + 1) + '\n')
        for a in samples:
            for b in a:
                f.write(b)
                f.write(', ')
            f.write('\n')
        i = i + 1
    f.write('\n')
    f.close()

print("INFO: File saved. Run " + str(count) + " times with " + str(k) + " sets data.")
