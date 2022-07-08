#!/usr/bin/env python3
from __future__ import annotations
import time
import string
import libtmux
import libtmux.server


__version__ = "1.0.0"


def create_new_session(server: libtmux.Server, session_name="0"):
    server.new_session(session_name=session_name)
    return session_name


# TODO: replace try-except with port check
def main() -> int:
    server = libtmux.Server()
    session_name: str = ""
    sessions = []

    print(f"[q]: Quit selection")
    print(f"[n]: Create new session")

    try:
        sessions.extend(server.list_sessions())

        for idx, session in enumerate(sessions):
            session_name = session.get("session_name")
            print(f"[{idx}]: {session_name}")

    except libtmux.exc.LibTmuxException as e:
        # NOTE(gr3yknigh1): Looks a little bit tricky
        # if no server is running (no session found), 
        # then `libtmux.exc.LibTmuxException` will raised. 
        # Then we just creating new session here.
        # session_name = create_new_session(server)
        pass

    while True:
        selection = input("Select option: ")

        if selection not in string.digits and selection not in  "nq":
            print("You must enter digit or 'n' or 'q'")
            continue
        
        if selection not in 'nq' and int(selection) not in range(len(sessions)):
            print("Input digit must be in range of list")
            continue

        if selection == 'n':
            session_name = create_new_session(server, session_name=input("Name new session: "))
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

