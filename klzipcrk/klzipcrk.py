import zipfile
import multiprocessing.dummy as mp


class Klzipcrk(object):

    def __init__(self, file_path, dict_path):

        self.zFile = zipfile.ZipFile(file_path)
        self.passFile = open(dict_path)

    def crack_password(self):
        for line in self.passFile.readlines():
            password = line.rstrip()
            print "attempting with:", password
            if(self.__extract_zip__(password)):
                raise SystemExit
        # p=mp.Pool(8)
        # p.map(extract_zip, zFile, passFile.readlines())
        # p.close()
        # p.join()

    def __extract_zip__(self, password):
        try:
            self.zFile.extractall(pwd=password)
            print "[+] Password Found: " + password + '\n'
            return True
        except:
            return False
