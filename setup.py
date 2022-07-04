from __future__ import annotations
import setuptools

def get_install_requires() -> list[str]:
    with open("./requirements.txt") as f:
        raw_data = f.read()
    return raw_data.splitlines()

setuptools.setup(
    name="tmux-session-selector",
    version="0.1.0",

    author="Akkuzin Ilya",
    author_email="gr3yknigh1@gmail.com",
    url="https://github.com/gr3yknigh1/tmux-session-selector",

    py_modules=["tmux_session_selector"],

    entry_points={
        "console_scripts": ["tmux-session-selector = tmux_session_selector:main"]
    },

    install_requires=get_install_requires(),
    python_requires=">=3.10"
)
