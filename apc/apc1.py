import sys
import telnetlib
import time

# Program un-tested thus far
#######################################
# Telnet responses
#received (see IANA assigned telnet options):
#255 253 1    IAC DO ECHO
#255 253 31   IAC DO NAWS
#255 251 1    IAC WILL ECHO
#255 251 3    IAC WILL SUPPRESS-GO-AHEAD
#So you should respond:
#255 252 1    IAC WONT ECHO
#255 252 31   IAC WONT NAWS
#255 254 1    IAC DONT ECHO
#255 254 3    IAC DONT SUPPRESS-GO-AHEAD
#Note that you don't have to know what 1, 3, or 31 mean. 
# You can refuse those options, You default to the network virtual terminal.
#Telnet(10.200.1.26,23): recv '\xff\xfb\x01\n\rUser Name : '
#Telnet(10.200.1.26,23): IAC WILL 1
#Telnet(10.200.1.26,23): send 'apc\n'
#Telnet(10.200.1.26,23): recv '\xff\xfc\x01apc'
#Telnet(10.200.1.26,23): IAC WONT 1
#Telnet(10.200.1.26,23): recv '\r\n'
#Telnet(10.200.1.26,23): recv 'Connection Closed - Bye\r\n'
#Telnet(10.200.1.26,23): recv ''
#Telnet(10.200.1.26,23): send 'apc\n'
#Telnet(10.200.1.26,23): send 'enable\n'
#Traceback (most recent call last):
# File "apc1.py", line 38, in <module>
#   tn.write(cmd1.encode('ascii') + b"\n")
# File "/usr/lib/python2.7/telnetlib.py", line 283, in write
#   self.sock.sendall(buffer)
# File "/usr/lib/python2.7/socket.py", line 228, in meth
#   return getattr(self._sock,name)(*args)
#socket.error: [Errno 32] Broken pipe
#######################################

user = "apc"
password = "apc"
command = "sh ver"
term = "term len 0"

data = open("telnet.txt")
for line in data:
    cmd1 = "enable"
    tn = telnetlib.Telnet(line.rstrip())
    tn.set_debuglevel(1)
    time.sleep(2)
    tn.read_until(b"User Name : ")
    tn.write(user.encode('ascii') + b"\n")
    time.sleep(2)
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    time.sleep(2)
    tn.write(cmd1.encode('ascii') + b"\n")
    time.sleep(2)
    tn.write(password.encode('ascii') + b"\n")
    time.sleep(2)
    tn.write(b"exit\n")
    lastpost = tn.read_all().decode('ascii')
    print(lastpost)
    tn.close()
