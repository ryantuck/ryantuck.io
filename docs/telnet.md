# telnet

Test open ports with `telnet`.

This will show the "Connected" message if the port is open.

Ctrl-C doesn't quit out, so Ctrl-] then "quit" is needed to exit.

```
$ telnet google.com 80
Trying 172.217.5.238...
Connected to google.com.
Escape character is '^]'.
^]
telnet> quit
Connection closed.
```
