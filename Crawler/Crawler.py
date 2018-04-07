import urllib
import PubgStats

class webParser():
    self.url = ""
    self.html

    def __init__(self):
        pass

    def __init__(self, website):
        self.url = website

    def setWebsite(self, website):
        self.url = website

    def getHTML(self):
        self.html = urllib.urlopen(self.url).read()
        return self.html

    def saveToFile(self):
        f = open('latestCrawlerText.txt','w')
        f.write(self.html)
        f.close()

class Crawler():
    self.queuedUrls = "bot/queue.txt"
    self.parsedUrls = "bot/parsed.txt"
    self.parser = webParser()

    def __init__(self, website):
        #If the website has already been parsed by the bot, return from the function.
        if(self.isParsed(website)):
            return

        #If the link has not been parsed, add it to the queue.
        f = open('bot/queue.txt','w')
        #Write the new website to the file containing queued urls.
        f.write('\n' + website)
        f.close()        

    def addLinksToQueue():
        #ToDo, tag on all <a></a> tags to grab links and parse them for more links.
        #Ensure links that are obtained are the format of http://pubg.op.pp/user/{user}?server={server}
        #Ensure links added have not been parsed.
        pass

    def isParsed(self, url):
        f = open('bot/parsed.txt','r')
        #Write the new website to the file containing queued urls.
        for line in f.readlines():
            if website == line:
                return True
        
        f.close()
        return False

    def getHTML(self):
        #Get the first line from the queue text file and remove it.
        f = open('bot/queue.txt','r')
        self.parser.setWebsite(f.readLine())
        lines = f.readlines()
        lines = lines[1:-1]
        f.close()
        f = open('bot/queue.txt','w')
        for line in lines:
            f.write(line)
        f.close()
        return self.parser.getHTML()

class PubgOpGgCrawler(Crawler):

    soloStats = PubgStats()
    duoStats = PubgStats()
    squadStats = PubgStats()
    
    def __init__(self, username):
        Crawler.__init__(self, "https://pubg.op.gg/user/" + username)
        soloStats.playerName = username
        duoStats.playerName = username
        squadStats.playerName = username

        soloStats.server = "na"
        duoStats.server = "na"
        squadStats.server = "na"

        soloStats.gameMode = 'Solo'
        duoStats.gameMode = 'Duo'
        squadStats.gameMode = 'Squad'        

    def __init__(self, username, server):
        Crawler.__init__(self, "https://pubg.op.gg/user/" + username + "?server=" + server)
        soloStats.playerName = username
        duoStats.playerName = username
        squadStats.playerName = username

        soloStats.server = server
        duoStats.server = server
        squadStats.server = server

        soloStats.gameMode = 'Solo'
        duoStats.gameMode = 'Duo'
        squadStats.gameMode = 'Squad'

    def crawlPage():
        #Get the html from the frist url in the queue.
        html = self.parser.getHTML()
        
        #Wesite uses javascript/ajax to load new information!
        #Need to install Selenium to control a browser before gathering the information required.
        #https://pypi.python.org/pypi/selenium

        soloRating = html.find('<div class="ranked-stats__rating-point">')
        duoRating = html.find('<div class="ranked-stats__rating-point">', soloRating + len('<div class="ranked-stats__rating-point">') + 4)
        squadRating = html.find('<div class="ranked-stats__rating-point">', duoRating + len('<div class="ranked-stats__rating-point">') + 4)

        soloStats.rating = html[soloRating + len('<div class="ranked-stats__rating-point">'):soloRating + len('<div class="ranked-stats__rating-point">') + 4]        f = open('bot/queue.txt','r')
        self.parser.setWebsite(f.readLine())
        lines = f.readlines()
        f.close()
        duoStats.rating = html[duoRating + len('<div class="ranked-stats__rating-point">'):duoRating + len('<div class="ranked-stats__rating-point">') + 4]
        squadStats.rating = html[squadRating + len('<div class="ranked-stats__rating-point">'):squadRating + len('<div class="ranked-stats__rating-point">') + 4]
        #ToDo: Use the parser to get a url from the queue to parse.
        #Save any data that is found to a database model.
        pass
