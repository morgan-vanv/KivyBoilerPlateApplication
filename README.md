# KivyBoilerPlateApplication [TEMPLATE]
### by Morgan Van V.
This repo will store a clean example foundation for a Kivy App that can be easily forked for rapid application
prototyping and development

## Format / Foundation
Add images here to display what this application looks like when built. Basic Kivy & KivyMD Navigation Drawer
multipage layout.

## How to use:
1. install dependencies from requirements.txt 
2. run main.py file found in:
        
        ./src/BoilerPlateApplication/main.py

## TODO:
- fill out README with proper documentation and make it look real good
- set up proper packaging as well as test cases (FIX __INIT__.PY ISSUES FOR TESTING & RUNNING AS MAIN)
- requirements.txt (add to readme as well)
- set up all configuration options for ease of adjustment later (window size, logging level. etc.)
- use base pages to illustrate styling options and what can be done
- github actions into deployment pipeline? create official releases and other github features as learning opportunity

## A Crash Course / Reference on Kivy & KivyMD

Here are some notes for the user, (as well as for my later reference), regarding Kivy and KivyMD
Consider this a crash course of sorts.

#### Kivy App Lifecycle

      Python start, run() -> build() -> on_start() -> APP FUNCTIONS -> on_stop() -> KIVY WINDOW DESTROYED

   We can also use `on_pause()` and `on_resume()` to do self-explanatory things

