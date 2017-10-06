
import optparse
import zipfile
from time import time
import multiprocessing.dummy as mp


def extract_zip(zfile, password):
    try:
        zfile.extractall(pwd=password)
        print "[+] Password Found: " + password + '\n'
        exit(0)
    except:
        pass


def function(string):
    print string


def main():
    tiempo_inicial = time()
    parser = optparse.OptionParser("usage %prog " + "-f <zipfile> -d <dicctionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, arg) = parser.parse_args()
    if (options.zname is None) | (options.dname is None):
        print parser.usage
        exit(1)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)

    for line in passFile.readlines():
        password = line.rstrip()
        if(extract_zip(zFile, password)):
            break
    # p=mp.Pool(8)
    # p.map(extract_zip, zFile, passFile.readlines())
    # p.close()
    # p.join()

    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print 'El tiempo de ejecucion fue:', tiempo_ejecucion, "segundos"


if __name__ == '__main__':
    main()
