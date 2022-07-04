# tmux session selector

Simple `tmux` session selector

## Installation

1. Clone repository

```shell
git clone https://github.com/gr3yknigh1/tmux-session-selector
```

2. Install it with `pip`

```shell
pip install tmux-session-selector
```

3. Try run

```shell
tmux-session-selector
```

## Hook with `fish` shell and `alacritty`:

> Note that this script force you to use terminal with `tmux`

```yaml
shell:
  program: /usr/bin/fish
  args:
    - --command=tmux-session-selector
```

If you want to quit selection and drop into `fish` without `tmux`, just add second command:

```yaml
    - --command=fish
```
