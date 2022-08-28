"""
So this file is currently a bare-bones implementation of a listener in twisted
    Current Functionality: passes all request content to our handle_message() method in the Kivy App

This type of functionality should be expanded/refined if it is going to be core to the application,
as this currently does no routing or other more advanced behaviours.

This can also be reimplemented in other networking protocols, SSH, Tor, seemingly anything really
(Twisted seems like a pretty cool library)
Just try to modify this Factory implementation however you might need it,
because the use of factories is imperative so this functionality will play nice w/ the Kivy Event Loop.

-----
REFERENCES:
https://kivy.org/doc/stable/guide/other-frameworks.html
http://jcalderone.livejournal.com/49707.html
http://labs.twistedmatrix.com/2008/02/simple-python-web-server.html
"""

import json
from twisted.web import http

#from twisted.web.resource import Resource
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
    """This factory handles our HTTP requests"""
    isLeaf = True
    #protocol = SimpleHTTPListener

    def __init__(self, app):
        self.app = app

    # TODO: add handling of other requests, and mapping based on URL/path in request
    def render(self, request):
        """renders the request when received, passes content into Kivy app.handle_message()"""
        bytes_data = request.content.getvalue()
        json_data = bytes_data.decode('utf8').replace("'", '"')
        json_object = json.loads(json_data)
        self.app.handle_message(json_object)
        #print(json_object)
        return ''
