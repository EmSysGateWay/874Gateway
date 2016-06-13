sudo echo 4 > /sys/class/gpio/unexport
sudo echo 17 > /sys/class/gpio/unexport
sudo echo 4 > /sys/class/gpio/export
sudo echo 17 > /sys/class/gpio/export

sudo echo out > /sys/class/gpio/gpio4/direction
sudo echo 1 > /sys/class/gpio/gpio4/value

sudo echo out > /sys/class/gpio/gpio17/direction
sudo echo 0 > /sys/class/gpio/gpio17/value