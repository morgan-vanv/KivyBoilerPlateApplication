"""
http://jcalderone.livejournal.com/49707.html
http://labs.twistedmatrix.com/2008/02/simple-python-web-server.html

usage:
        $ twistd -y webserver.py
"""


from twisted.web.resource import Resource
from twisted.internet import protocol
from twisted.web import http
import json

#class SimpleHTTPListener(Resource):
#    isLeaf = True
#
#    def render_GET(self, request):
#        return ''
#
#    def render_POST(self, request):
#        #response = self.factory.app.handle_message(request)
#        return ''


class SimpleHTTPServerFactory(http.HTTPFactory):
    isLeaf = True
    #protocol = SimpleHTTPListener

    def __init__(self, app):
        self.app = app

    # TODO: add handling of other requests, and mapping based on URL/path in request
    def render(self, request):
        bytes_data = request.content.getvalue()
        json_data = bytes_data.decode('utf8').replace("'", '"')
        json_object = json.loads(json_data)
        self.app.handle_message(json_object)
        #print(json_object)
        return ''


