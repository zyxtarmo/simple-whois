# Simple WHOIS server in Python

"WHOIS is a TCP-based transaction-oriented query/response protocol that is widely used to provide information services to Internet users."
Official specification can be found [here](https://tools.ietf.org/html/rfc3912)

Installation
-----
Since this is a python script Python of version 2.7 should be installed on a system.
* Place `whois.py` and `db/` folder in `/opt/` folder on your system
* Drop `simple-whois` bash script into `/etc/init.d/` folder 
* Run `chkconfig --add simple-whois` 


iptables -A PREROUTING -t nat -p tcp --dport 43 -j REDIRECT --to-port 1043
iptables -A OUTPUT -t nat -p tcp --dport 43 -j REDIRECT --to-port 1043
iptables -A INPUT -p tcp --dport 43 -m state --state NEW -m limit --limit 50/minute --limit-burst 200 -j ACCEPT
