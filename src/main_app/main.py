""" This file is the primary execution point for the Kivy template application """
#   by Morgan Van V. (2022)

# Imports for Kivy & KivyMD
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.logger import Logger, LOG_LEVELS
from kivy.uix.screenmanager import ScreenManager, NoTransition
#from kivy.properties import *
from kivy.core.text import LabelBase

# Imports for Styling
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import FloatLayout

# Imports for Settings Screen
from kivy.uix.settings import SettingsWithSidebar

# Importing Screens
from screens.HomeScreen import HomeScreen
from screens.SecondScreen import SecondScreen
from screens.ThirdScreen import ThirdScreen


# Imports for Twisted Reactor Server
from server.twisted_listener import SimpleHTTPServerFactory
from kivy.support import install_twisted_reactor

install_twisted_reactor() # install_twisted_rector must be called before importing and using the reactor

from twisted.web import server
from twisted.internet import reactor


# Navbar
class ContentNavigationDrawer(MDBoxLayout):
    """This is for the drawer that pulls out from the left"""


#  MAIN CLASS HERE
class KivyBoilerPlateApplication(MDApp):
    """This is the main_app class for the application. Call .run() on this to do the obvious """

    # Initializes Application
    def __init__(self, **kwargs):
        Logger.info("   ! APPLICATION INITIALIZING !")
        Logger.setLevel(LOG_LEVELS["info"])     # TODO: add this as a selectable settings option
        super().__init__(**kwargs)  # Really should learn about this and why it is necessary

        # Set up Main Layout & Screen Manager
        self.main_layout = FloatLayout()
        self.nav_bar = Builder.load_file('screens/navbar.kv')
        self.screen_manager = ScreenManager()
        self.screen_manager.transition = NoTransition()
        self.main_layout.add_widget(self.nav_bar, 1)  # Adding Navigation Bar
        self.main_layout.add_widget(self.screen_manager, 10)  # Adding Screen Manager

        # Building Screens from File
        self.home_screen = Builder.load_file('screens/HomeScreen.kv')
        self.second_screen = Builder.load_file('screens/SecondScreen.kv')
        self.third_screen = Builder.load_file('screens/ThirdScreen.kv')

    # Builds Application
    def build(self):
        Logger.info("   ! APPLICATION BUILDING !")

        # Styling Configuration
        self.theme_cls.theme_style = "Dark"     # Theme Color
        self.theme_cls.material_style = "M3"    # Material Design Style
        LabelBase.register(name='osrs_font', fn_regular='static_assets/runescape-uf/runescape_uf.ttf')
        theme_font_styles.append('osrs_font')   # Custom OSRS Font Style

        # For Settings & Config
        self.settings_cls = SettingsWithSidebar
        self.config.read("./src/main_app/settings_config.ini")

        # Adding Screens to the Screen Manager
        self.screen_manager.add_widget(HomeScreen(name='HomeScreen'))
        self.screen_manager.add_widget(SecondScreen(name='SecondScreen'))
        self.screen_manager.add_widget(ThirdScreen(name='ThirdScreen'))
        self.screen_manager.current = 'HomeScreen'

        # Listener for Server that handles HTTP requests
        #site = server.Site(SimpleHTTPListener())
        site = server.Site(SimpleHTTPServerFactory(self))
        self.main_listener = reactor.listenTCP(9420, site)

        return self.main_layout

    # Builds Settings Menu
    def build_settings(self, settings):
        """Builds setting screen from settings_items.json and settings_config.ini"""
        Logger.info("   build_settings() called.")
        settings.add_json_panel('Settings Panel 1', self.config, './src/main_app/settings_items.json')

    # Page Navigation
    def show_screen(self, screen_name):
        """Passed screen_name, sets screen manager to display that screen"""
        Logger.info("   show_screen(%s) called.", screen_name)
        try:
            self.screen_manager.current = screen_name
        except RuntimeError:
            print(f"Error: {screen_name} is not in self.screen_manager!")

    # Twisted Reactor Server for Handling HTTP Requests
    def handle_message(self, msg):
        """ passed message from twisted reactor listener, then handles it """
        Logger.info("POST Received: %s", msg)
        #print(msg)


# MAIN EXECUTION LOOP
if __name__ == '__main__':
    print("Main Loop Executed. Starting...")

    # CODE GO HERE
    KivyBoilerPlateApplication().run()
    KivyBoilerPlateApplication().stop()

    print("Main Loop Closing...")
