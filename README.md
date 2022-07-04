# Tmux attach

Simple tmux session selector

## Installation

1. Clone repository

```shell
git clone https://github.com/gr3yknigh1/tmux-attach
```

2. Install it with pip

```shell
pip install tmux-attach
```

3. Try run

```shell
tmux-attach
```

## Hook with `fish` shell and `alacritty`:

> Note that this script force you to use terminal with tmux

```yaml
shell:
  program: /usr/bin/fish
  args:
    - --command=tmux-attach
```

