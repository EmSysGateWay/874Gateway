sudo ifconfig eth0 down
sudo ifconfig eth0 down hw ether 08:9E:01:D1:0A:FC
sudo ifconfig eth0 up
sudo ip addr flush dev eth0
sudo ip addr add dev eth0 192.168.1.8/24
sudo ip route replace default via 192.168.1.1

