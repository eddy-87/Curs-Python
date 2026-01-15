def reverse_lines(input_file, output_file):
    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        for line in fin:
            fout.write(line.rstrip("\n")[::-1] + "\n")

reverse_lines("input.txt", "output.txt")
