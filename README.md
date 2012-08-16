cube_python
===========

A library for using Cube in Python


Usage
-----

```python
import cube_python as Cube
emitter = Cube.Emitter('udp://example.com:1081')
emitter.send({ 'hello': 'world' })
emitter.close()
``1