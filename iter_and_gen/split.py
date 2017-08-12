from __future__ import print_function
from itertools import islice
from math import ceil

def read_n_lines(infile, i, n):
    ''' generates n lines from i to i + n '''
    return islice(open(infile), i, i+n)

def read_n_lines_packages(infile, n):
    ''' generates packages of n lines each '''
    nof_lines = sum(1 for line in open(infile))
    nof_files = int(ceil(float(nof_lines)/float(n)))
    for i in range(nof_files):
        yield read_n_lines(infile, i*n, n)

def split(infile, n):
    ''' splits the file into multiple files, up to n lines each '''
    lastindex = infile.rfind('/')
    lines = read_n_lines_packages(infile, n)
    for i, nlines in enumerate(lines):
        outfilename = infile[:lastindex]+'/out_'+ str(i) +'.py'
        outfile = open(outfilename,'w')
        for line in nlines:
            print(line, file = outfile, end = '')
