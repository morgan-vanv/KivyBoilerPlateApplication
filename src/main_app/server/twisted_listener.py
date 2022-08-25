""" THIS IS A SCRIPT I ADAPTED FROM THE KIVY & TWISTED ECHO MESSAGING APP"""
# https://kivy.org/doc/stable/guide/other-frameworks.html

# install_twisted_rector must be called before importing and using the reactor
from kivy.support import install_twisted_reactor

install_twisted_reactor()

from twisted.internet import reactor
from twisted.internet import protocol
from twisted.web.http import Request


class LoggingServer(protocol.Protocol):
    def render_POST(self, request):
        return request

    def dataReceived(self, data):
        response = self.factory.app.handle_message(data)
        if response:
            self.transport.write(response)


class LoggingServerFactory(protocol.Factory):
    protocol = LoggingServer

    def __init__(self, app):
        self.app = app
