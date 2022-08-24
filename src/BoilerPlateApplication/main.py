""" This file is the primary execution point for the Kivy template application """
#   by Morgan Van V. (2022)

# Imports for Kivy & KivyMD
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.properties import *
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


# from screens import HomeScreen, SecondScreen, ThirdScreen

# Navbar
class ContentNavigationDrawer(MDBoxLayout):
    """This is for the drawer that pulls out from the left"""


#  MAIN CLASS HERE
class KivyBoilerPlateApplication(MDApp):
    """This is the main class for the application. Call .run() on this to do the obvious """

    # Screens are stored as properties so they are updated dynamically
    screen_manager = ObjectProperty(None)
    home_screen = ObjectProperty(None)
    second_screen = ObjectProperty(None)
    third_screen = ObjectProperty(None)

    # Initializes Application
    def __init__(self, **kwargs):
        print("   __init__() executed for App.")
        super().__init__(**kwargs)  # Really should learn about this and why it is necessary

    # Builds Application
    def build(self):

        # Styling Configuration
        self.theme_cls.theme_style = "Dark"     # Theme Color
        self.theme_cls.material_style = "M3"    # Material Design Style
        LabelBase.register(name='osrs_font', fn_regular='static_assets/runescape-uf/runescape_uf.ttf')
        theme_font_styles.append('osrs_font')   # Custom OSRS Font Style

        # For Settings & Config
        self.settings_cls = SettingsWithSidebar
        self.config.read("./src/BoilerPlateApplication/kivyapp_config.ini")

        # Set up Main Layout & Screen Manager
        self.main_layout = FloatLayout()
        self.nav_bar = Builder.load_file('screens/navbar.kv')
        self.screen_manager = ScreenManager()
        self.screen_manager.transition = NoTransition()
        self.main_layout.add_widget(self.nav_bar, 1)  # Adding Navigation Bar
        self.main_layout.add_widget(self.screen_manager, 10)  # Adding Screen Manager

        # Building and Adding Screens to the Screen Manager
        self.home_screen = Builder.load_file('./screens/HomeScreen.kv')   # pay attention to these filepaths
        self.second_screen = Builder.load_file('./screens/SecondScreen.kv')
        self.third_screen = Builder.load_file('./screens/ThirdScreen.kv')
        self.screen_manager.add_widget(HomeScreen(name='HomeScreen'))
        self.screen_manager.add_widget(SecondScreen(name='SecondScreen'))
        self.screen_manager.add_widget(ThirdScreen(name='ThirdScreen'))
        self.screen_manager.current = 'HomeScreen'

        return self.main_layout

    # Builds Settings Menu
    def build_settings(self, settings):
        """Builds setting screen from settings_custom.json and kivyapp_config.ini"""
        #settings.add_json_panel('Settings Panel 1', self.config, 'settings_custom.json')
        settings.add_json_panel('Settings Panel 1', self.config, './src/BoilerPlateApplication/settings_custom.json')

    # Page Navigation
    def show_screen(self, screen_name):
        """Passed screen_name, will set screen manager to display that screen"""
        try:
            self.screen_manager.current = screen_name
        except Exception:
            print(f"Error: {screen_name} is not in self.screen_manager!")



# MAIN EXECUTION LOOP
if __name__ == '__main__':
    print("Main Loop Executed. Starting...")

    # CODE GO HERE
    KivyBoilerPlateApplication().run()

    print("Main Loop Closing...")
