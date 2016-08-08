# Debian Router
The following are notes on the process used to make Debian act as 
a router/ap for the purpose of web filtering / ids.

 Install Ubuntu 12.04 and all security updates on a separate system (we used a VM)
```
apt-get install build-essential python-pip python-dev libxml2 libxml2-dev libxslt1-dev
pip install mitmproxy
pip install pyasn1
pip install flask
pip install urwid
pip install lxml
pip install pyOpenSSL==0.13
```

i
sysctl -w 'net.ipv4.ip_forward=1'
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE;
iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT;
iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT;
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 80 -j REDIRECT --to-port 8080;
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j REDIRECT --to-port 8080;

iptables-save > /etc/iptables.ipv4.nat
echo "To restore:  "
echo "iptables-restore < /etc/iptables.ipv4.nat"
echo "-----------------------------------------"

# /etc/init.d/networking stop && /etc/init.d/networking start
#ifdown -a && ifup -a

/etc/init.d/udhcpd stop && /etc/init.d/udhcpd start
#/etc/init.d/isc-dhcp-server start

/etc/init.d/hostapd stop && /etc/init.d/hostapd start

update-rc.d hostapd enable
update-rc.d udhcpd enable
#update-rc.d isc-dhcp-server enable

return 0
