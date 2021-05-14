import sys, os

# attributes
vars = 256

# initialize varlist and pointer
varlist = []
for i in range(vars): varlist.append(0)
pointer = 0

# returns whether file exists at given path
def file_exists(path): return os.path.exists(path)

# parses given character
def parse(ch):
    global pointer
    if ch == '<': pointer = vars - 1 if pointer == 0 else pointer - 1
    elif ch == '>': pointer = 0 if pointer == vars - 1 else pointer + 1
    elif ch == '-': varlist[pointer] -= 1
    elif ch == '+': varlist[pointer] += 1
    elif ch == '.': print(chr(varlist[pointer]), end='')
    elif ch == ':': print(varlist[pointer])
    else: varlist[pointer] = ord(ch)

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
