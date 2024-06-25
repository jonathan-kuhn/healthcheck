#!/usr/bin/env python3
import socket
import requests as r
import ipaddress
import settings # type: ignore
import datetime
import json
import parser

#get environment variables
NUMBER = settings.NUMBER
API_KEY = settings.API_KEY
DOMAINS = settings.DOMAINS


def url_of(domain):
    return 'https://' + domain

def get_current_address() -> str:
    print('getting current address...')
    req = r.get('https://api.ipify.org')
    current_address = req.text
    print('current address: ' + current_address)
    return current_address

def get_dns_address(dns_name) -> str:
    print('getting address from dns server...')
    try:
        dns_address = socket.gethostbyname(dns_name)
        print('dns address: ' + dns_address)
        return dns_address
    except Exception as exception:
        print(f'Error resolving {dns_name}: {exception}')
        return None

def adresses_match(address1: str, address2: str) -> bool:
    print('matching current and dns adress...')
    if (is_valid_address(address1) and is_valid_address(address2)):
        if (address1 == address2):
            print('addresses match')
            return True
        else: 
            print('addresses don\'t match!')
    else: 
        ('at least one address is not valid')

def is_valid_address(address: str) -> bool:
    try:
        ipaddress.ip_address(address)
        return True
    except Exception:
        return False

def returns_status200(url:str) -> bool:
    print('checking http status code...')
    try:
        req = r.get(url)
        print('status code is ' + str(req.status_code))
        return req.status_code == 200
    except Exception as exception:
        print('the website did not return a valid response code!')
        return False

def domain_is_healthy(domain:str) -> bool:
    healthy = adresses_match(get_current_address(), get_dns_address(domain))
    healthy = healthy and returns_status200(url_of(domain))
    return healthy

def create_report():
    send_report = False
    report = {}
    for domain in DOMAINS:
        print('\nChecking domain: ' + domain)
        if domain_is_healthy(domain):
            report[domain] = 'Healthy'
        else:
            report[domain] = 'Not healthy'
            send_report = True
    if send_report:
        send()
        write_report(report)
    else:
        print('\n\nEvery domain is healthy!')

def write_report(report):
    report_file = 'report_' + str(datetime.datetime.now().date()) + '.json'
    report_json = json.dumps(report, indent=4)
    with open(report_file, "w") as file:
        file.write(report_json)

def send():
    message = 'One of your websites is not healthy.\nCheck the created status report for more info!' 
    res = r.post('https://textbelt.com/text', {
        'phone': NUMBER,
        'message': message,
        'key': API_KEY,
    })
    print('\n\nTextbelt info:\n' + str(res.json()))

def change_domains(domains):
    settings.DOMAIN = domains
def change_number(number):
    settings.NUMBER = number
def change_api_key(api_key):
    settings.API_KEY = api_key

parser.add_argument("-n", "--number", nargs=1, metavar="NUMBER",
                    help="change number in settings.py")
parser.add_argument("-a", "--api_key", nargs=1, metavar="API_KEY",
                    help="change api_key in settings.py")
parser.add_argument("-d", "--domain", nargs=1, metavar="DOMAIN",
                    help="change domains in settings.py")
args = parser.parse_args()

if __name__ == '__main__':
    if args.number:
        change_number(args.number[0])
    elif args.api_key:
        change_api_key(args.api_key[0])
    elif args.domain:
        change_domains(args.domain[0])
    else:
        create_report()