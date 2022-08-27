"""
http://jcalderone.livejournal.com/49707.html
http://labs.twistedmatrix.com/2008/02/simple-python-web-server.html

usage:
        $ twistd -y webserver.py
"""


from twisted.web.resource import Resource
import json

class SimpleHTTPListener(Resource):
    isLeaf = True

    def render_GET(self, request):
        return ''

    def render_POST(self, request):
        bytes_data = request.content.getvalue()
        json_data = bytes_data.decode('utf8').replace("'", '"')
        json_object = json.loads(json_data)
        print(json_object)
        return ''
