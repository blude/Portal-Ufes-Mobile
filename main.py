#!/usr/bin/env python   
import sys
from os.path import dirname, join as join_path
from wsgiref.handlers import CGIHandler
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import RequestHandler, WSGIApplication
sys.path.insert(0, join_path(dirname(__file__), 'lib')) # extend sys.path
import feedparser # universal feed parser
from datetime import datetime

d = feedparser.parse('http://portal.ufes.br/rss.xml') # our feed url
feed = d.feed
entries = d.entries

class Single(RequestHandler):

    def get(self):
    
        id = self.request.get('id')
        entry = entries[int(id) - 1]
        date = datetime.strptime(entry.date[:-6],'%a, %d %b %Y %H:%M:%S')
        
        template_values = {
            'feed': feed,
            'entries': entries,
            'entry': entry,
            'id': id,
            'date': date,
        }
        
        path = join_path(dirname(__file__), 'templates/article.html')
        self.response.out.write(template.render(path, template_values))

class List(RequestHandler):

    def get(self):
        
        template_values = {
            'feed': feed,
            'entries': entries,
        }
        
        path = join_path(dirname(__file__), 'templates/news.html')
        self.response.out.write(template.render(path, template_values))

        
class MainHandler(RequestHandler):

    def get(self):
        
        template_values = {}
        
        path = join_path(dirname(__file__), 'templates/index.html')
        self.response.out.write(template.render(path, template_values))
        
        
class About(RequestHandler):

    def get(self):
    
        version = "2.2"
    
        template_values = {
            'version': version,
        }
        
        path = join_path(dirname(__file__), 'templates/about.html')
        self.response.out.write(template.render(path, template_values))


class Changes(RequestHandler):

    def get(self):
    
        template_values = {}
        
        path = join_path(dirname(__file__), 'templates/changelog.html')
        self.response.out.write(template.render(path, template_values))

class Menu(RequestHandler):

    def get(self):
    
        template_values = {}
        
        path = join_path(dirname(__file__), 'templates/cardapio.html')
        self.response.out.write(template.render(path, template_values))
        
def main():
    application = WSGIApplication([('/', MainHandler),
                                    ('/sobre/', About),
                                    ('/sobre/changelog/', Changes),
                                    ('/cardapio/', Menu),
                                    ('/noticias/', List),
                                    ('/noticias/ler/', Single)]
                                    ,debug=True)
    CGIHandler().run(application)


if __name__ == '__main__':
    main()