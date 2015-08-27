import urllib
import os

class GutClient:
    BASE_URL = "https://www.gutenberg.org/cache/epub/"
    def __init__(self, repo):
        print "Initing"
        self.localRepo = os.path.abspath(repo)
        #self.getter = urllib.URLOpener()
        
    def downloadBook(self, bookId):        
        bookUrl = GutClient.BASE_URL + bookId + "/pg" + bookId + ".txt"
        bookFile = self.localRepo + "/" + bookId + ".txt"
        print "Downloading " + bookUrl  + " to " +  bookFile
        urllib.urlretrieve(bookUrl, bookFile)
        
        

if __name__ == '__main__':
    cl = GutClient(".")
    cl.downloadBook('45484')
