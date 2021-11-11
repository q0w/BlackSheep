from typing import Any

import msgpack


class MsgpackPlugin:
    def __init__(self):
        self._loads = msgpack.loads
        self._dumps = msgpack.dumps

    def use(
        self,
        loads=msgpack.loads,
        dumps=msgpack.dumps,
    ):
        self._loads = loads
        self._dumps = dumps

    def loads(self, data: bytes) -> Any:
        return self._loads(data)

    def dumps(self, obj: Any) -> bytes:
        return self._dumps(obj)
