import sys, os

def file_exists(path): return os.path.exists(path)

# get program args
args = sys.argv

# throw error if no path
if len(args) < 2:
    print('error: no file path given')
    sys.exit()

# get program path
path = args[1]

# throw error if path not valid
if not path.endswith('.onech') or not file_exists(path):
    print('error: file path invalid')
    sys.exit()

# read program from file
file = open(path, 'r')
program = file.read()
file.close()

# parse each character in program
for ch in program:
    parse(ch)
