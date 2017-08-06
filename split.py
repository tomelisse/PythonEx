from __future__ import print_function

def readlines(infile):
    ''' generates all the lines in the file '''
    return (line for line in open(infile))

def read_n_lines(infile, n):
    ''' generates n lines at a time '''
    i = 0
    n_lines = []
    for line in open(infile):
        n_lines.append(line)
        i += 1
        if i%n == 0:
            yield n_lines
            n_lines = []

def split(infile, n):
    ''' splits the file into multiple files, up to n lines each '''
    lastindex = infile.rfind('/')
    lines = read_n_lines(infile, n)
    for i, nlines in enumerate(lines):
        outfilename = infile[:lastindex]+'/out_'+ str(i) +'.py'
        outfile = open(outfilename,'w')
        for line in nlines:
            print(line, file = outfile, end = '')
