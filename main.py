import argparse
import sys
from core import client
from colorama import Fore, Back, Style
import banner

__AUTHOR__ = "t0gu"
__VERSION__ = "1.0"
__TWITTER__ = "@t0guu"


menu = argparse.ArgumentParser(description="[-] Domain analayser from shodan :)")
menu.add_argument("-d", "--domain", type=str, required=True, help="[-] Domain to scan")
menu.add_argument('-v','--verbose', help='Print more data', action='store_true')
menu.add_argument("-st", '--sub_txt', help="salve subdomains on txt", action='store_true')
menu.add_argument("--b", help='Shows the banner :D', action='store_true')
args = menu.parse_args()

if args.domain == "" or args.domain == None:
    print(f">> Domain is required...\n {sys.argv[0]} -h")

# arguments from command line
domain = args.domain
verbose = args.verbose
b = args.b
text_subdomain = args.sub_txt


if b:
    print(f":Author: {__AUTHOR__}:Version:{__VERSION__}:{__TWITTER__}:"+Fore.RED + banner.banner)
    print(Fore.RESET)

if verbose:
    print(f">> {verbose}")
    print(Fore.RED + f">>> Verbose mode ON")
    t = client.Client(domain,verbose)
    t.Subdomain_search()
    t.User_info()
else:
    if text_subdomain:
        t = client.Client(domain, text_subdomain=True)
        t.Subdomain_search()
    else:
        t = client.Client(domain)
        t.Subdomain_search()