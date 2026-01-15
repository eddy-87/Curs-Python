def filter_lines(input_file, output_file, keyword):
    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        for line in fin:
            if keyword in line:
                fout.write(line)

filter_lines("input.txt", "filtered.txt", "Python")
