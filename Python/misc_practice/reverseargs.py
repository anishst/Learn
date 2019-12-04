import sys

# reversing and printing command-line arg

args = sys.argv[1:]
args.reverse()
print(' '.join(args))
