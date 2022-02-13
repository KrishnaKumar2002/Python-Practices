import sys,os,getopt
def main(argv):
opts, args = getopt.getopt(argv, "i:")
for o, a in opts:
if o in "-i":
run(a)
def run(a):
inp_file=a+'.cpp'
exe_file=a+'.exe'
if __name__=='__main__':
main(sys.argv[1:])