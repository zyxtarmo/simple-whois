# simple-whois
Simple implementation of the whois server in python

IpTables rules:

iptables -A PREROUTING -t nat -p tcp --dport 43 -j REDIRECT --to-port 1043
iptables -A OUTPUT -t nat -p tcp --dport 43 -j REDIRECT --to-port 1043
iptables -A INPUT -p tcp --dport 43 -m state --state NEW -m limit --limit 50/minute --limit-burst 200 -j ACCEPT
