import urllib
import os
import sys

class GutClient:
    BASE_URL = "https://www.gutenberg.org/cache/epub/"
    def __init__(self, repo):       
        self.localRepo = os.path.abspath(repo)        
        
    def downloadBook(self, bookId):        
        bookUrl = GutClient.BASE_URL + bookId + "/pg" + bookId + ".txt"
        bookFile = self.localRepo + "/" + bookId + ".txt"
        print "Downloading " + bookUrl  + " to " +  bookFile
        urllib.urlretrieve(bookUrl, bookFile)
        
        

if __name__ == '__main__':
    if len(sys.argv) > 1:        
        bId = sys.argv[1]
    else:        
        sys.exit("bookid is required")
            
    if len(sys.argv) > 2:        
        repo = sys.argv[2]
    else:
        repo = "."
        
    cl = GutClient(repo)
    cl.downloadBook(bId)
