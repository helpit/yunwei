#! /bin/bash
#！/usr/bin/expect
spawn ssh [name]@[host_ip]
expect "*assword:*"
send "123456\r"
expect eof
