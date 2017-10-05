
import optparse
import zipfile
from threading import Thread
#from concurrent.futures import ThreadPoolExecutor
import time
from time import time

def extract_zip(zfile, password):
    try:
        zfile.extractall(pwd=password)
        print "[+] Password Found: " + password + '\n'
    except:
        pass

def main():
    tiempo_inicial = time() 
    parser = optparse.OptionParser("usage %prog "+"-f <zipfile> -d <dicctionary>")
    parser.add_option('-f', dest='zname', type='string',help='specify zip file')
    parser.add_option('-d', dest='dname', type='string',help='specify dictionary file')
    (options, arg) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)

    #executor = ThreadPoolExecutor(max_workers=2)
    for line in passFile.readlines():
        password = line.rstrip()
	#executor.submit(extract_zip,(zFile),(password))
	extract_zip(zFile,password)
    #executor.shutdown()
    tiempo_final = time() 
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print 'El tiempo de ejecucion fue:',tiempo_ejecucion 

if __name__ == '__main__':
    main()

