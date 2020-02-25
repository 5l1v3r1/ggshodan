import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from configparser import SafeConfigParser
from colorama import Fore, Back, Style

parser = SafeConfigParser()
parser.read("./config.ini")
API_KEY = parser.get('config','api_key')


class Client():

    def __init__(self, domain, verbose=False, text_subdomain=False):
        self.domain = domain
        self.base_url = "https://api.shodan.io/"
        self.verbose = verbose
        self.text_subdomain = text_subdomain


    def _get_only_subs(self, dict_domains):
        list_of_subdomains = dict_domains['subdomains']

        if self.verbose:
            for v in dict_domains['data']:
                for j,q in v.items():
                    print(Fore.YELLOW + f"{j}:{q}")
        else:
            if self.text_subdomain:
                for s in list_of_subdomains:
                    with open('subdomains.txt', 'a') as fh:
                        sub = s + "." + self.domain + '\n'
                        fh.write(sub)
            for s in list_of_subdomains:
                print(Fore.CYAN + f"{s+'.'+self.domain}")
    
        print(Fore.RESET)


    def Subdomain_search(self):
        client_call = self.base_url + 'dns/domain/' +self.domain  + "?key=" + API_KEY

        if self.verbose:
            print(f">> Client call is: {client_call}")
            try:
                client_request = requests.get(client_call, verify=False, timeout=10)
                resp = client_request.json()
                self._get_only_subs(resp)
            except (requests.exceptions.Timeout,requests.exceptions.HTTPError) as e:
                print(e)
        else:
            try:
                client_request = requests.get(client_call, verify=False, timeout=10)
                resp = client_request.json()
                self._get_only_subs(resp)
            except (requests.exceptions.Timeout,requests.exceptions.HTTPError) as e:
                print(Fore.RED + f"[+] Something went wrong at: {e}")


    def User_info(self):

        try:
            user_info = self.base_url + "api-info?key=" + API_KEY
            r = requests.get(user_info, verify=False, timeout=10)
            json_data = r.json()
            for k,v in json_data.items():
                print(Fore.YELLOW + f">> {k}:{v}")
            print(Fore.RESET)
        except (requests.exceptions.Timeout, requests.exceptions.HTTPError) as e:
            print(e)
