"""
http://jcalderone.livejournal.com/49707.html
http://labs.twistedmatrix.com/2008/02/simple-python-web-server.html

usage:
        $ twistd -y webserver.py
"""


from pprint import pprint
from twisted.application.internet import TCPServer
from twisted.application.service import Application
#from twisted.web.resource import Resource
from twisted.web.server import Site

from twisted.web import server
from twisted.internet import reactor
from twisted.web.resource import Resource
import json

class Simple(Resource):
    isLeaf = True

    def render_GET(self, request):
        return ''

    def render_POST(self, request):
        bytes_data = request.content.getvalue()
        json_data = bytes_data.decode('utf8').replace("'", '"')
        json_object = json.loads(json_data)
        print(json_object)
        return ''


site = server.Site(Simple())
reactor.listenTCP(9420, site)
reactor.run()




#root = Resource()
##root.putChild(b'form', FormPage())
#application = Application("My Web Service")
#TCPServer(8880, Site(root)).setServiceParent(application)