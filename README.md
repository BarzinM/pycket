# Pycket

## Functions

### my_ips
returns a list of device's IPs.

##### Returns
A list of IPs as strings.

### pingable
Returns a boolean to indicate if an IP is accessible in the network.

##### Args
- `ip`: IP of the device as a string.

##### Returns
`True` if accessible. `False` otherwise.

## Classes 

###`TCP`

A wrapper for python socket class configured for TCP connections.

#### `__init__`

`TCP(ip='localhost', port=8089, type=None, backlog=0)`

Constructs the TCP connection.

##### Args
- `ip`: IP of the server
- `port`: port of the server side of connection.
- `type`: Default is None. It checks the `ip` argument and see if it belongs to the local machine, then it sets the local machine as server. Otherwise, it sets the local machine as client. It can also be given the type of connection explicitly using `server` or `client` as arguments.
- `backlog`: Number of backlog for `socket.listen`.

#### `recv`

Receives a string through the connection.

##### Args
- `length`: Maximum length of the string.

##### Returns
A string that was received through TCP connection.

#### `send`

Sends a given string through the connection.

##### Args
- `data`: the string to be sent.

#### timeout

Sets the timeout for the connection.

##### Args
- `time`: a numerical value in seconds.
