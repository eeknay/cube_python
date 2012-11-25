cube_python
===========

A library for using Cube in Python


Example using UDP
-----------------

```python
import cube_python as Cube
emitter = Cube.Emitter('udp://example.com:1081')
emitter.send({ 'hello': 'world' })
emitter.close()
```

Example of using Websockets
---------------------------
requires websocket-client (pip install websocket-client)

```python
import cube_python as Cube

emitter = Cube.Emitter('ws://localhost:1080/1.0/event/put')
emitter.send({"data": {
                      "mem": {
                          "total": 4036177920,
                          "free": 147902464},
                      "network": {
                          "eth0": {
                              "rxp": 2584118,
                              "rxb": 2234161298,
                              "txb": 3120755872,
                              "txp": 2830949}}},
                      "type": "ws_test"
              })
emitter.close()
```
