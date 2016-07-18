# Simple WHOIS server in Python

"WHOIS is a TCP-based transaction-oriented query/response protocol that is widely used to provide information services to Internet users."
Official specification can be found [here](https://tools.ietf.org/html/rfc3912)

Installation
-----
Since this is a python script Python of version 2.7 should be installed on a system.
* Place `whois.py` and `db/` folder in `/opt/` folder on your system
* Drop `simple-whois` bash script into `/etc/init.d/` folder 
* Run `chkconfig --add simple-whois`

Now simple-whois will automatically start on system boot. You can also start and stop the service manually by running `sudo service simple-whois start(stop)`.

Securing simple-whois service
-----
Whois service operates on the port 43 of TCP protocol. In order to start using this port the script has to run as root user. But this is potential issue if service gets compromised and hacker gets access to the system.

It is better to start a service with a non-root user that has limited rights to the system. One of the workarounds for this problem could be the use of Iptables.
Service starts on the 1043 port by a regular user and iptable rule is used to forward port 1043 -> 43:
``` 
    iptables -A PREROUTING -t nat -p tcp --dport 43 -j REDIRECT --to-port 1043
```

But now running whois from the localhost will not work for the default port 43. To fix this lets use another iptables rule:
```
    iptables -A OUTPUT -t nat -p tcp --dport 43 -j REDIRECT --to-port 1043
```

Simple way to prevent DoS attacks on the simple-whois service would be to use iptables to throttle down frequent requests:
```
    iptables -A INPUT -p tcp --dport 43 -m state --state NEW -m limit --limit 50/minute --limit-burst 200 -j ACCEPT
```

Audit
-----
Simple-whois service writes rotating logs to the `/var/log/simple-whois/` folder on the system. By default it's setup to write daily logs and it stores 7 logfiles. Example of the record in the logfile:
```
2016-07-16 22:46:53,214 WHOIS_SERVER INFO client_ip:104.172.239.44 requested_domain:test.com
2016-07-16 22:46:56,438 WHOIS_SERVER INFO client_ip:104.172.239.44 requested_domain:test.org
2016-07-16 22:46:59,848 WHOIS_SERVER INFO client_ip:104.172.239.44 requested_domain:test.com
```
