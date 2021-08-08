import yaml
import json
import socket


def get_ip(dns):
    ip_addr = []
    for i in dns:
        ip_addr.append(socket.gethostbyname(i))
    return ip_addr

def check_ip_addr(dns, ip):
    current_ip_addr = []
    for i in dns:
        current_ip_addr.append(socket.gethostbyname(i))
    for k in range(len(ip)):
        if current_ip_addr[k] == ip[k]:
            print(f"http://{dns[k]} - {ip[k]}")
        else:
            print(f"[ERROR] http://{dns[k]} IP mismatch: {ip[k]} {current_ip_addr[k]}")

    return current_ip_addr

def create_json_yaml(dns, current_ip_addr):
    key = dns
    values = current_ip_addr
    my_dict = dict(zip(key, values))

    with open('ip_addres.json', 'w') as json_file:
        json.dump(my_dict, json_file)

    data = open('ip_addres.json', 'r')
    jsonData = json.load(data)
    data.close()

    with open('ip_addres.yml', 'w') as yml_file:
        yaml.dump(jsonData, yml_file)

if __name__ == '__main__':
    dns = ['drive.google.com', 'google.com', 'mail.google.com']
    ip = get_ip(dns)
    new_ip = check_ip_addr(dns, ip)
    create_json_yaml(dns, new_ip)
