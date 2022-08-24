import time
import unittest
# REFER TO: https://kivy.org/doc/stable/contribute-unittest.html
#   TODO: UNDERSTAND AND REFACTOR THE BUILDER.LOAD() STATEMENTS. THAT IS WHAT IS CAUSING ISSUES ON BUILD TEST

#from src.BoilerPlateApplication import *
from src.BoilerPlateApplication.main import KivyBoilerPlateApplication


class MyTestCase(unittest.TestCase):
    #def test_something(self):
    #    self.assertEqual(True, False)  # add assertion here

    def test_screenmanager(self):
        from kivy.lang import Builder
        from kivy.uix.screenmanager import ScreenManager
        self.screenmanager = ScreenManager()

        from src.BoilerPlateApplication.screens import HomeScreen, SecondScreen, ThirdScreen
        self.home_screen = Builder.load_file('src/BoilerPlateApplication/screens/HomeScreen.kv')
        self.second_screen = Builder.load_file('src/BoilerPlateApplication/screens/HomeScreen.kv')
        self.third_screen = Builder.load_file('src/BoilerPlateApplication/screens/HomeScreen.kv')
        self.screen_manager.add_widget(HomeScreen(name='HomeScreen'))
        self.screen_manager.add_widget(SecondScreen(name='SecondScreen'))
        self.screen_manager.add_widget(ThirdScreen(name='ThirdScreen'))
        self.screen_manager.current = 'HomeScreen'

        self.assertEqual(True, False)  # add assertion here

    #def test_build(self):
    #    KivyBoilerPlateApplication.run()
    #    time.sleep(10)
    #    KivyBoilerPlateApplication.stop()
    #    #self.assertIs(KivyBoilerPlateApplication)
    #
    #    #self.ass


if __name__ == '__main__':
    unittest.main()
