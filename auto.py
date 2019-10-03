import time
import keyboard
from args_builder.args_builder import Args_Builder
from web_builder.web_builder import Web_Builder
###
#
# Basic Selenium Automation Script.
# Automate interval, maxInterval, WebsiteUrl, element
# Modes : Write / Click
#  
# Pass input with argparse: fx:
# python3 main.py -u 'https://google.com' -nm 'q' -i 0.5 -wri 'args ' -i_m 10 
# 
# use -h for help
#
# Requirements: 
# Chrome Version 77.0.3865.90 (Official Build) (64-bit) or later
# python3
# python3 get-pip.py
# pip3 install selenium
# pip3 install keyboard ############!!!
##
def run(mode):
    '''
    run("MODE") 
    MODE = "autostart" -> starts waiting for input
    MODE ="rerun" -> starts again with different promt
    MODE ="noautostart"
    ''' 
    if(mode=="noautostart"):
        print("noautostart enabled: wating for 'x' input...")
        keyboard.wait('x')
        
    elif(mode=="rerun"):
        print("Try Again? \nPress any Key to continue or CTRL-C to stop")
        keyboard.wait('x')

    elif(mode=="autostart"):
       print("starting automation...") 

    else:
        print("run exeption: no mode specified, exit()")
        exit() # exit when no mode is given
    automation()

def automation():
    # Get Webelement by either id or class
    
    if(args.el_id):
        print("get el_id")
        element = web_builder.getElement_byId(args.el_id)
    elif(args.el_class):
        print("get el_class")
        element = web_builder.getElement_byClass(args.el_class)
    elif(args.el_name):
        print("get el_name")
        element = web_builder.getElement_byName(args.el_name)
    elif(args.el_xpath):
        print("get el_xpath")
        element = web_builder.getElement_byXpath(args.el_xpath)

    # While maxRuntime is not reached, do
    # While Args:
    running = True          # stops loop
    run_for = 0             # time i seconds 
    while running:          # <- boolean gets turned False when maxRuntime is reached  
        
        #Check current args mode and do (click, write ..)
        if element:
            if(args.write):
                element.send_keys(args.write)
                if(args.debug):
                    print(f'write -> {element}')
            elif(args.click):
                element.click()
                if(args.debug):
                    print(f'click -> {element}')
        
            # Increase runtime & check if maxRuntime is reached -> stops the loop
            if(args.maxRuntime != None and run_for >= args.maxRuntime):
                print(f'ENDLOOP run:{run_for} && max:{args.maxRuntime}')
                running = False
            elif(args.maxRuntime != None and run_for < args.maxRuntime):
                run_for += args.interval
            
            # Sleep in interval between iterations
            time.sleep(args.interval)

        # if there is no element
        else: 
            running = False

    # while loop running = True after maxRuntime is reached or when not finding an element
    print(f'run for {run_for} seconds')
    run("rerun")

## Setup Args_Builder -> input when running script
args = Args_Builder().args

## Setup Web_Builder -> controls + driver initialization
web_builder = Web_Builder()
driver = web_builder.driver

## fetch the Page
driver.get(args.url)

# check if user enabled noautostart
# if not:
# loop to check if user starts Script
if(args.noautostart):
    run("noautostart")
else:
    run("autostart")









