#!/usr/bin/env python3
from __future__ import annotations
import libtmux
import libtmux.server




# TODO: replace try-except with port check
def main() -> int:
    server = libtmux.Server()
    session_name: str
    try:
        session = server.list_sessions()[0]
        session_name = session.get("session_name")
    except libtmux.exc.LibTmuxException as e:
        session_name = "0"
        server.new_session(session_name=session_name)
    server.attach_session(session_name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

