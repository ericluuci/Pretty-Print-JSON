file_in = "input.txt"
file_out = "output.txt"
indent_size = 2


def main():
    
    infile = open(file_in, 'r')
    outfile = open(file_out, 'w')
    
    counter = 0;
    for line in infile:
        for char in line:
            if (char == '[' or char == '{' or char == '('):
                counter += indent_size
                outfile.write(char + '\n' + ' '*counter)
            elif(char == ']' or char == '}' or char == ')'):
                counter -= indent_size
                outfile.write('\n' + ' '*counter + char)
            elif (char == ','):
                outfile.write(char + '\n' + ' '*counter)
            else:
                outfile.write(char)
            

if __name__ == "__main__":
    main()