# Simple WHOIS server in Python

"WHOIS is a TCP-based transaction-oriented query/response protocol that is widely used to provide information services to Internet users."
Official specification can be found [here](https://tools.ietf.org/html/rfc3912)

Installation
-----
Since this is a python script Python of version 2.7 should be installed on a system.
* Place `whois.py` and `db/` folder in `/opt/` folder on your system
* Drop `simple-whois` bash script into `/etc/init.d/` folder 
* Run `chkconfig --add simple-whois`
* Now you can start the service by running `sudo service simple-whois start`; run `sudo service simple-whois stop` to stop the service

Securing simple-whois service
-----
Whois service operates on the port 43 of TCP protocol. In order to start using this port the script has to run as root user. But this is potential issue if service gets compromised and hacker gets access to the system.

It is better to start a service with a non-root user that has limited rights to the system. One of the workarounds for this problem could be the use of Iptables.
Service starts on the 1043 port by a regular user nad iptable rule is used to forward port 1043 -> 43:
``` 
    iptables -A PREROUTING -t nat -p tcp --dport 43 -j REDIRECT --to-port 1043
```

iptables -A PREROUTING -t nat -p tcp --dport 43 -j REDIRECT --to-port 1043
iptables -A OUTPUT -t nat -p tcp --dport 43 -j REDIRECT --to-port 1043
iptables -A INPUT -p tcp --dport 43 -m state --state NEW -m limit --limit 50/minute --limit-burst 200 -j ACCEPT
