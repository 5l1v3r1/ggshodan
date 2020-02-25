# ggshodan
ggshodan using shodan api to grab subdomains

## Requirements
python3 <= python3.7

*chromium driver (if you need a screenshoot module)
$ sudo apt install chromium-browser chromium-chromedriver

shodan api key, get one at <https://account.shodan.io/register>



put your shodan api key at the *config.ini*

## Install 
```bash
git clone https://github.com/t0gu/ggshodan.git
cd ggshodan
python3 -m pip install requirements.txt
```


## Usage options
```bash
# Output only subdomains
python3.7 main.py -d t0gu.com

# Output saving into a txt file
python3.7 main.py -d t0gu.com -st

# Verbose mode this include your api key status
python3.7 main.py -d t0gu.com -v

# Screenshoot module
python3.7 main.py -d t0gu.com -st -sv
```

* Screenshoot module using with -st -sc flag

![](https://raw.githubusercontent.com/t0gu/ggshodan/master/screen_t0gu.gif)


* the example bellow shows the output with -b flag that shows the banner you can get only the text ;) just remove the -b flag

![](https://raw.githubusercontent.com/t0gu/ggshodan/master/shodan-search.gif)


* Example of the verbose mode:

```python
>>> Verbose mode ON
>> Client call is: https://api.shodan.io/dns/domain/hackerone.com?key=<your_key>
subdomain:
type:A
value:104.16.99.52
last_seen:2020-02-24T19:31:48.470509+00:00
subdomain:
type:A
value:104.16.100.52
last_seen:2020-02-24T19:31:48.472942+00:00
subdomain:
type:AAAA
value:2606:4700::6810:6434
last_seen:2020-02-24T19:31:48.480402+00:00
subdomain:
type:AAAA
value:2606:4700::6810:6334
last_seen:2020-02-24T19:31:48.476111+00:00
subdomain:api

>> scan_credits:100
>> usage_limits:{'scan_credits': 100, 'query_credits': 100, 'monitored_ips': 16}
>> plan:dev
>> https:True
>> unlocked:True
>> query_credits:56
>> monitored_ips:None
>> unlocked_left:56
>> telnet:True

```
