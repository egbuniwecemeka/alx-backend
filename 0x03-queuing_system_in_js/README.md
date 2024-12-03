# 0x03. Queuing System in JS

Downloaded redis
wget http://download.redis.io/releases/redis-6.0.10.tar.gz

extract redis
tar xzf redis-6.0.10.tar.gz

Enter into extracted file and compile using `make`

cd redis-6.0.10

Run server
scr/redis-server & (where & can be user defined/configuration file)

Test if server is running (PING & PONG)
src/server-cli ping -> "pong"

Set and Retrieve Keys and values
Eg. Setting and retrieving key-value pair of Holberton: School
127.0.0.1:[Port]> set Holberton School (Setting value)
127.0.0.1:[Port]> get Holberton (Retrieving value)

Killing server process
ps aux | grep -i redis (Searches for processes with redis instances)
kill [PID-of-redis-server]
