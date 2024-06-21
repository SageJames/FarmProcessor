"""
Title: UI Interface
Author: Alcinder Lewis
Version: 0.1
Description: Manages all the UI element of the application.
- Handles the Interface and optional logic for Image processing and Scanning
"""

import tkinter as tk


# User Interface Material 
def generate_main():
    pass

# Organized Component Logic
def image_processing(path):
    """
    Takes a pathway and determines if it is a folder or if it is a single image (Determine if batch processing is needed)
    """
    pass

def batch_processing(path):
    """
    Processes a collection of images with the folder
    """
    # TODO figure out the number of images with the folder and make sure to create a array of thier pathways
    # TODO Itterate over each pathway 
    # TODO Indciate the entire folder
    pass

def single_processing(path):
    """
    Processes the single image where the filepath specifies
    """
    # TODO Call a function from the ImageProcess.py
    # TODO Output some signal to say the job is complete
    pass