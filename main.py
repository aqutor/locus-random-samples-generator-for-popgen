import csv
import random
import os
import config

# Initialise
k = config.k
count = config.count
output_type = config.output_type
input_file_path = config.input_file_path


# Function
def write_locus_name(sample_size, opened_file):
    index_list = list(range(1, sample_size + 1))
    locus_name = 'Locus name:\n' + ', '.join(map(str, index_list)) + '\n'
    opened_file.write(locus_name)


# Calculate
with open(input_file_path) as f:
    data = [tuple(line) for line in csv.reader(f)]

size_of_sample = len(data[0])

i = 0
if output_type == 1:
    while i < count:
        samples = random.sample(data, k)
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, 'results', str(count), str(k),
                                     'sample_' + str(k) + '_' + str(i + 1) + '.csv')
        f = open(abs_file_path, 'w+')
        title = "/*Test Data Set I: Diploid */\n" \
                "number of populations = " + str(count) + "\n" \
                "number of loci = " + str(size_of_sample) + "\n"
        f.write(title)
        write_locus_name(size_of_sample, f)
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
    title = "/*Test Data Set I: Diploid */\n" \
            "number of populations = " + str(count)\
            + "\nnumber of loci = " + str(size_of_sample) + "\n"
    f.write(title)
    write_locus_name(size_of_sample, f)
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

print("INFO: File saved in " + abs_file_path + ". Run " + str(count)
      + " times with " + str(k) + " sets data.")
