"""
Title: Main
Author: Alcinder Lewis
Version: 0.1
Description: Comprises the main operations of the application
"""
from UI import generate_main
import sys

# TODO Displays Options menu
def help():
    """
    Options Menu display
    - 1: Dubug Mode
    - 2: Developer Mode 
    - 3: Data Summary
    """
    print("Help Menu:")
    print("-Debug or -debug: Debug Mode")
    print("-Dev or -dev: Developer Mode ")
    print("-Data or -data: Data Summary")

# TODO Warm up display
def warm_up():
    """
    My personal sanity check to help me free less scared
    """
    pass

# TODO Functionality Testing from Test.py
def test():
    """
    Wrapper for all the other things for system I can VSCode test
    """
    pass

# TODO Debug Protocol
def debug_protocol():
    """
    Wrapper for standard operations in the Debug Protocol python file. 
    
    Protocol:
    - Print to the user another menu to determine if they want to validate some form of functionanlity or Warm up simulation 
    """
    print("Debug Mode Activated")
    pass

# TODO Dev Mode
def dev_protocol():
    """
    Wrapper for standard operations in the Developer Protocol python file. 
    
    Protocol:
    - 
    """
    print("Developer Mode Activated")
    pass

# TODO Data Summary 
def data_summary():
    """
    Wrapper for standard operations in the Data Summary python file. 

    Protocol:
    - 
    """
    print("Data Summary Generating...")
    pass

# TODO start protocol
def start():
    """
    Wrapper for standard operations in the Start Protocol. 
    
    Protocol:
    - 
    """
    #generate_main()
    print("Start Protocol")
    pass


# Main method 
if __name__ == "__main__":

    # Determine is a argument is provided on call
    if len(sys.argv) < 2:
        print("Deflult Option")
        start()
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-help':
            help()
        elif sys.argv[1] == '-Dev' or sys.argv[1] == '-dev':
            dev_protocol()
        elif sys.argv[1] == '-Debug' or sys.argv[1] == '-debug':
            debug_protocol()
        elif sys.argv[1] == '-data' or sys.argv[1] == '-Data':
            data_summary()
        else:
            print("Unknown Commmand")
            help()
    else:
        print("To many arguments")
        help()
        start()
    
    

