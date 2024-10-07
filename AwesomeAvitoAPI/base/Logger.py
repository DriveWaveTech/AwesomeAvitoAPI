import atexit
import sys
import typing

from loguru._logger import Logger as _Logger, Core as _Core


class Logger(_Logger):
    def __init__(self):
        super().__init__(
            core=_Core(),
            exception=None,
            depth=0,
            record=False,
            lazy=False,
            colors=False,
            raw=False,
            capture=True,
            patchers=[],
            extra={},
        )

        self.add(sys.stderr)
        atexit.register(self.remove)

    def _trace(self, *messages):
        self._my_log(*messages, level="TRACE")

    def _debug(self, *messages):
        self._my_log(*messages, level="DEBUG")

    def _info(self, *messages):
        self._my_log(*messages, level="INFO")

    def _success(self, *messages):
        self._my_log(*messages, level="SUCCESS")

    def _warn(self, *messages):
        self._my_log(*messages, level="WARNING")

    def _err(self, *messages):
        self._my_log(*messages, level="ERROR")

    def _crit(self, *messages):
        self._my_log(*messages, level="CRITICAL")

    def _my_log(self, *messages, level: typing.Union[str, int] = "INFO"):
        self._log(
            level, False, self._options, self._format_messages(*messages), None, None
        )

    def _format_messages(self, *messages) -> str:
        return '\n'.join([f'[{self.__class__.__name__}] {msg}' for msg in messages])
