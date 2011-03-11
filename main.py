#!/usr/bin/env python   
import sys
from os.path import dirname, join as join_path
from wsgiref.handlers import CGIHandler
from google.appengine.api import urlfetch
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import RequestHandler, WSGIApplication
sys.path.insert(0, join_path(dirname(__file__), 'lib')) # extend sys.path
import feedparser

class Single(RequestHandler):

    def get(self):
    
        d = feedparser.parse('http://portal.ufes.br/rss.xml')
    
        feed = d.feed
        entries = d.entries
        entry = entries[2]
        
        id = self.request.get('id')
    
        template_values = {
            'feed': feed,
            'entries': entries,
            'entry': entry,
            'id': id,
        }
        
        path = join_path(dirname(__file__), 'templates/article.html')
        self.response.out.write(template.render(path, template_values))

class News(RequestHandler):

    def get(self):
        
        d = feedparser.parse('http://portal.ufes.br/rss.xml')
        
        feed = d.feed
        entries = d.entries
        
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
    
        version = "2.1 beta"
    
        template_values = {
            'version': version,
        }
        
        path = join_path(dirname(__file__), 'templates/about.html')
        self.response.out.write(template.render(path, template_values))


class Changelog(RequestHandler):

    def get(self):
    
        template_values = {}
        
        path = join_path(dirname(__file__), 'templates/changelog.html')
        self.response.out.write(template.render(path, template_values))

        
def main():
    application = WSGIApplication([('/', MainHandler),
                                    ('/sobre/', About),
                                    ('/changelog/', Changelog),
                                    ('/noticias/', News),
                                    ('/noticia/', Single)]
                                    ,debug=True)
    CGIHandler().run(application)


if __name__ == '__main__':
    main()