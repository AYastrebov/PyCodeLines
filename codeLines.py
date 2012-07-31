import os

total = 0
ext = (".h", ".m", ".mm", ".java", ".cpp", ".py")

def main() :
    directory = raw_input( "Provide your project path: " )
    prefix = raw_input("Provide your file prefix or leave it empty: ")
    for root, dirs, files in os.walk(directory.strip()):
        for filename in files:
            if filename.endswith(ext):
                if len(prefix) > 0:
                    if filename.startswith(prefix):
                        printOutputForFile("%s/%s" % (root, filename))
                else:        
                    printOutputForFile("%s/%s" % (root, filename))
    print 'Total lines of code: ', total

def printOutputForFile(filename):
    global total
    f = open(filename)
    le = len(f.readlines())
    total += le
    print '%(s)s file has %(l)d lines of code' % {'s': filename, 'l': le}



# Call the main routine which we difined as the first
# function in the file.
main()
