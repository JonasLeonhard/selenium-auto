import argparse
from argparse import RawTextHelpFormatter  # allows for use of \n


class Args_Builder:
    def __init__(self, *args, **kwargs):
        print("Args_builder initialize...")


        # Setup argparse: python auto.py -u "https://google.com" -id "q" -i 30
        parser = argparse.ArgumentParser(
        description="Selenium - Bot. \npython3 auto.py -u 'https://google.com' -nm 'q' -i 0.5 -wri 'args ' -i_m 10 \npython3 auto.py -u 'https://tallycounterstore.com/online-counter' -i 1 -id 'addNewCounter' -cli -i_m 5 \npython3 auto.py -u 'https://countn.com' -xp '//*[@id=\u0022plus1\u0022]' -i 0.5 -cli -i_m 10",
        formatter_class=RawTextHelpFormatter)

        parser.add_argument('-u', '--url', type=str, required=True, metavar='URL',
                    help="Url to be loaded, copy & paste here -> fx (https://www.google.com)")
        parser.add_argument('-i', '--interval', type=float, required=True,
                    metavar='S', help="Interval in Seconds")
        parser.add_argument('-i_m', '--maxRuntime', type=float,
                    metavar='S_max', help="Interval maxRuntime in Seconds")
        parser.add_argument("-noauto", '--noautostart', action="store_true", help="Dont Autostart Script in Browser, start script upon pressing 'alt-x'")
        parser.add_argument("-deb", '--debug', action="store_true", help="Enables Debug logging in terminal when clicking'")
    
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-cl', '--el_class', type=str,
                   metavar='C', help="element class name in html")
        group.add_argument('-id', '--el_id', type=str, metavar='ID',
                   help="element id label in html")
        group.add_argument('-nm', '--el_name', type=str, metavar='NAME',
                   help="element name in html")
        group.add_argument('-xp', '--el_xpath', type=str, metavar='NAME',
                   help="element xpath in html")

        mode = parser.add_mutually_exclusive_group(required=True)
        mode.add_argument("-wri", '--write', type=str,
                  metavar='TXT', help="Writing mode")
        mode.add_argument("-cli", '--click', action="store_true", help="Click mode")

        self.args = parser.parse_args()
        print(f'\nArguments: \n {args} \n')
