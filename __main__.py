from klzipcrk.klzipcrk import Klzipcrk
from time import time
import optparse

if __name__ == "__main__":

    parser = optparse.OptionParser("usage %prog " + "-f <zipfile> -d <dicctionary>")
    parser.add_option('-f', dest='zip_path', type='string', help='specify zip file')
    parser.add_option('-d', dest='dict_path', type='string', help='specify dictionary file')
    (options, arg) = parser.parse_args()

    if (options.zip_path is None) | (options.dict_path is None):
        print parser.usage
        exit(1)
    else:
        tiempo_inicial = time()
        KL = Klzipcrk(options.zip_path, options.dict_path)
        KL.crack_password()
        tiempo_final = time()
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        print 'El tiempo de ejecucion fue:', tiempo_ejecucion, "segundos"
