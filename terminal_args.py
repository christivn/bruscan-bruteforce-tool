import sys,getopt
from os import path

def main(argv):
    scanType="none"
    try:
        opts, args = getopt.getopt(argv,"hml")
        
        if(opts!=0):
            for opt, arg in opts:
                if opt == "-h":
                    raise Exception
                elif opt in ("-l", "--iplist"):
                    scanType="list"
                elif opt in ("-m", "--mysql"):
                    scanType="mysql"
                else:
                    raise Exception
            return scanType
        
    except:
        print ("HELP MENU")
        print ("----------------------------------------------------------")
        print ("bruscan.py -l [--list]\tGet ip list from file 'ip_list.txt'")
        print ("bruscan.py -m [--mysql]\tGet ip list from mysql")
        sys.exit(2)