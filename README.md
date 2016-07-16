# simple-whois
Simple implementation of the whois server in python

IpTables rules:

iptables -A PREROUTING -t nat -p tcp --dport 43 -j REDIRECT --to-port 1043
iptables -A OUTPUT -t nat -p tcp --dport 43 -j REDIRECT --to-port 1043
