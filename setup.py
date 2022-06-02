from __future__ import annotations
import setuptools
import tmux_start

def get_install_requires() -> list[str]:
    with open("./requirements.txt") as f:
        raw_data = f.read()
    return raw_data.splitlines()

setuptools.setup(
    name="tmux-start",
    version=tmux_start.__version__,

    author="Akkuzin Ilya",
    author_email="gr3yknigh1@gmail.com",
    entry_points={
        "console_scripts": ["tmux-start = tmux_start:main"]
    },
    install_requires=get_install_requires()
)
