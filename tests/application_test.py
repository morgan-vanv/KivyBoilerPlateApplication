#
#   TODO: REFACTOR ALL TESTING. KIVY TESTING IS DONE IN AN ENTIRELY DIFFERENT WAY THAN ANTICIPATED
#       I WOULD READ THE DOCS AND FIX THIS RIGHT NOW BUT THE WEBSITE IS SEEMINGLY DOWN SO I GUESS THIS MUST BE RETURNED TO
#
# REFER TO: https://kivy.org/doc/stable/contribute-unittest.html


import time
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    # THIS IS OBVIOUSLY NOT CORRECT, BUT IS LEFT HERE FOR REFERENCE AND USE IN SCOPE TESTING
    #def test_build(self):
    #    from src.BoilerPlateApplication.main import KivyBoilerPlateApplication
    #    KivyBoilerPlateApplication.run()
    #    time.sleep(10)
    #    KivyBoilerPlateApplication.stop()


if __name__ == '__main__':
    unittest.main()
