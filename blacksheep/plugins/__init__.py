from blacksheep.plugins.json import JSONPlugin
from blacksheep.plugins.msgpack import MsgpackPlugin

json = JSONPlugin()
msgpack = MsgpackPlugin()

__all__ = [
    "json",
    "msgpack",
]
