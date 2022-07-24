#!/usr/bin/env python3
from __future__ import annotations
import os
import subprocess
import psutil
import time
import string
import libtmux
import libtmux.server


__version__ = "1.0.2"


TMUX_SERVER_PS_NAME = "tmux: server"
TMUX_CLIENT_PS_NAME = "tmux: client"


def is_proc_running(proc_name: str) -> bool:
    for proc in psutil.process_iter():
        if proc.name() == proc_name:
            return True
    return False


def is_server_running() -> bool:
    return is_proc_running(TMUX_SERVER_PS_NAME)


def is_client_attached() -> bool:
    return is_proc_running(TMUX_CLIENT_PS_NAME)


# TODO: replace try-except with port check
def main() -> int:
    if is_client_attached():
        print("Can't select when you attached to session")
        return 1

    server = libtmux.Server()
    session_name: str = ""
    sessions = []

    print(f"[q]: Quit selection")
    print(f"[n]: Create new session")

    if is_server_running():
        sessions.extend(server.list_sessions())

        for idx, session in enumerate(sessions):
            session_name = session.get("session_name")
            print(f"[{idx}]: {session_name}")

    while True:
        selection = input("Select option: ")

        if selection not in string.digits and selection not in  "nq":
            print("You must enter digit or 'n' or 'q'")
            continue

        if selection not in 'nq' and int(selection) not in range(len(sessions)):
            print("Input digit must be in range of list")
            continue

        if selection == 'n':
            session_name = input("Name new session: ")
            server.new_session(session_name=session_name)
        elif selection == 'q':
            print("Quiting selection...")
            return 0
        else:
            session_name = sessions[int(selection)].get("session_name")
        break


    server.attach_session(session_name)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("Exiting after KeyboardInterrupt")
        raise SystemExit(1)

