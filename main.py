import argparse,sys,os
from core import client,screenshoots
from colorama import Fore, Back, Style
import banner

__AUTHOR__ = "t0gu"
__VERSION__ = "1.0"
__TWITTER__ = "@t0guu"

menu = argparse.ArgumentParser(description="[-] Domain analayser from shodan :)")
menu.add_argument("-d", "--domain", type=str, required=True, help="[-] Domain to scan")
menu.add_argument('-v','--verbose', help='Print more data', action='store_true')
menu.add_argument("-st", '--sub_txt', help="salve subdomains on txt", action='store_true')
menu.add_argument("-sc", "--screenshot", help="Take screen shoot of all subdomains", action='store_true')
menu.add_argument("-pd", "--path_driver", type=str ,help="Path for your custom chromedriver default is [/usr/bin/chromedriver]")
menu.add_argument("--b", help='Shows the banner :D', action='store_true')
args = menu.parse_args()


# arguments from command line
domain = args.domain
verbose = args.verbose
b = args.b
text_subdomain = args.sub_txt
screen = args.screenshot
pt = args.path_driver


if domain == "" or domain == None:
    print(f">> Domain is required...\n {sys.argv[0]} -h")

if screen and not text_subdomain:
    print(Fore.CYAN + f">> Screenshoot need the flat -st to work")
    print(Fore.CYAN + f">> {sys.argv[0]} -d t0gu.com -st -sc")

if b:
    print(f":Author: {__AUTHOR__}:Version:{__VERSION__}:Twitter:{__TWITTER__}:"+Fore.RED + banner.banner)
    print(Fore.RESET)

if verbose:
    print(f">> {verbose}")
    print(Fore.RED + f">>> Verbose mode ON")
    t = client.Client(domain,verbose)
    t.Subdomain_search()
    t.User_info()
else:
    if text_subdomain:
        if screen:
            if pt != None:
                t = client.Client(domain, text_subdomain=True)
                t.Subdomain_search()
                s = screenshoots.Screen(path=pt)
                s.Start()
            else:
                t = client.Client(domain, text_subdomain=True)
                t.Subdomain_search()
                s = screenshoots.Screen()
                s.Start()
        else:
            t = client.Client(domain, text_subdomain=True)
            t.Subdomain_search()
    else:
        t = client.Client(domain)
        t.Subdomain_search()
