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
from screens.home_screen import home_screen
from screens.second_screen import second_screen
from screens.third_screen import third_screen


# Navbar
class ContentNavigationDrawer(MDBoxLayout):
    """This is for the drawer that pulls out from the left"""


#  MAIN CLASS HERE
class KivyBoilerPlateApplication(MDApp):
    """This is the main_app class for the application. Call .run() on this to do the obvious """

    # Initializes Application
    def __init__(self, **kwargs):
        Logger.info("   __init__() called.")
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
        self.home_screen = Builder.load_file('screens/home_screen.kv')
        self.second_screen = Builder.load_file('screens/second_screen.kv')
        self.third_screen = Builder.load_file('screens/third_screen.kv')

    # Builds Application
    def build(self):
        Logger.info("   build() called.")
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
        self.screen_manager.add_widget(home_screen(name='home_screen'))
        self.screen_manager.add_widget(second_screen(name='second_screen'))
        self.screen_manager.add_widget(third_screen(name='third_screen'))
        self.screen_manager.current = 'home_screen'

        return self.main_layout

    # Builds Settings Menu
    def build_settings(self, settings):
        """Builds setting screen from settings_items.json and settings_config.ini"""
        Logger.info("   build_settings() called.")
        settings.add_json_panel('Settings Panel 1', self.config, './src/main_app/settings_items.json')

    # Page Navigation
    def show_screen(self, screen_name):
        """Passed screen_name, will set screen manager to display that screen"""
        Logger.info("   show_screen(%s) called.", screen_name)
        try:
            self.screen_manager.current = screen_name
        except RuntimeError:
            print(f"Error: {screen_name} is not in self.screen_manager!")



# MAIN EXECUTION LOOP
if __name__ == '__main__':
    print("Main Loop Executed. Starting...")

    # CODE GO HERE
    KivyBoilerPlateApplication().run()
    KivyBoilerPlateApplication().stop()

    print("Main Loop Closing...")
