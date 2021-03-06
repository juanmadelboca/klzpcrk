from klzipcrk.klzipcrk import Klzipcrk
from time import time
import optparse
from dictionary.dictionary import create_dictionary

if __name__ == "__main__":

    parser = optparse.OptionParser("usage %prog " + "-f <zipfile> -w <word_length>")
    parser.add_option('-f', dest='zip_path', type='string', help='specify zip file')
    parser.add_option('-w', dest='word_length', type='int', help='specify word length')
    parser.add_option('-d', dest='dictionary_type', type='string', help='specify the dictionary you want to use')
    (options, arg) = parser.parse_args()

    if (options.zip_path is None) | (options.word_length is None):
        print parser.usage
        exit(1)
    else:    
        tiempo_inicial = time()
        if(options.dictionary_type is None):            
            create_dictionary(options.word_length, "dictionary_file.txt", "default")
        else:
            create_dictionary(options.word_length, "dictionary_file.txt", options.dictionary_type)
        KL = Klzipcrk(options.zip_path, "dictionary_file.txt")
        KL.crack_password()
        tiempo_final = time()
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        print 'El tiempo de ejecucion fue:', tiempo_ejecucion, "segundos"
