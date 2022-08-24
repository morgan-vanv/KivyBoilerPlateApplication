# THIS IS THE HOMESCREEN CLASS. REFACTORED TO COME OFF MAIN.PY

# Imports for HomeScreen
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen


# HomeScreen class definition
class HomeScreen(MDScreen):

    def build(self, **kwargs):
        print('HomeScreen.build() executed')
        return
