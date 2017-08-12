def printlines(lines):
    for line in lines:
        print line

def grep(lines, pattern):
    return (line for line in lines if pattern in line)

def over40(lines):
    return (line for line in lines if len(line)>40)

def readlines(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def main(filenames, pattern):
    # this is a generator reading one line at a time
    lines = readlines(filenames)
    # lines = grep(lines, pattern)
    lines = over40(lines)
    printlines(lines)
