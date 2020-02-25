# ggshodan
ggshodan using shodan api to grab subdomains

## Requirements
python3 <= python3.7
shodan api key, get one at <https://account.shodan.io/register>

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
```

* the example bellow shows the output with -b flag that shows the banner you can get only the text ;) just remove the -b flag

![](https://raw.githubusercontent.com/t0gu/ggshodan/master/shodan-search.gif)
