from copyreg import constructor


class Html:

    def __init__(self):
        pass
    
    def loadFile(self,persistence):
        return persistence.load("html")
    
    def loadUrl(self,request,url):
        #Faz Download da pagina 
        html = request.downloadHTML(url)
        return html
        
    def dumpHTML(self,persistence,html):
        #Persiste a pagina 
        persistence.persistFile(html, "html")
        
       