from __future__ import annotations
import setuptools

def get_install_requires() -> list[str]:
    with open("./requirements.txt") as f:
        raw_data = f.read()
    return raw_data.splitlines()

setuptools.setup(
    name="tmux-start",
    version="0.1.0",

    author="Akkuzin Ilya",
    author_email="gr3yknigh1@gmail.com",
    url="https://github.com/gr3yknigh1/tmux-start",

    py_modules=["tmux_start"],

    entry_points={
        "console_scripts": ["tmux-start = tmux_start:main"]
    },

    install_requires=get_install_requires(),
    python_requires=">=3.10"
)
