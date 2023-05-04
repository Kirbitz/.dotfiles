from libqtile import widget
from BatteryWrapper import BatteryWrapper


def create_right_bubble(fg, bg=None):
    return widget.TextBox(
        text="",
        font="Hack Nerd Font",
        padding=0,
        fontsize=30,
        foreground=fg,
        background=bg,
    )


def create_left_bubble(fg, bg=None):
    return widget.TextBox(
        text="",
        font="Hack Nerd Font",
        padding=0,
        fontsize=30,
        foreground=fg,
        background=bg,
    )


def init_widgets(colors):
    return [
        create_left_bubble(colors["orange"], colors["orange"]),
        widget.TextBox(
            text="",
            font="Hack Nerd Font",
            padding=0,
            fontsize=40,
            background=colors["orange"],
        ),
        create_right_bubble(colors["orange"], colors["cyan"]),
        widget.GroupBox(
            highlight_method="block",
            this_current_screen_border=colors["orange"],
            background=colors["cyan"],
        ),
        create_right_bubble(colors["cyan"]),
        widget.WindowName(),
        create_left_bubble(colors["orange"]),
        widget.ThermalSensor(
            fontsize=15,
            format=" {temp:.1f}{unit}",
            background=colors["orange"],
        ),
        create_left_bubble(colors["cyan"], colors["orange"]),
        widget.CPU(
            fontsize=15,
            format=" {freq_current}GHz {load_percent}%",
            background=colors["cyan"],
        ),
        create_left_bubble(colors["orange"], colors["cyan"]),
        widget.Memory(
            fontsize=15,
            format=" {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}",
            measure_mem="G",
            background=colors["orange"],
        ),
        create_left_bubble(colors["cyan"], colors["orange"]),
        widget.Systray(background=colors["cyan"]),
        create_left_bubble(colors["orange"], colors["cyan"]),
        widget.Volume(fontsize=15, fmt=" {}", background=colors["orange"]),
        create_left_bubble(colors["cyan"], colors["orange"]),
        BatteryWrapper(
            format="{char} {percent:2.0%}",
            show_short_text=False,
            low_percentage=0.25,
            fontsize=17,
            update_interval=15,
            font="Hack Nerd Font",
            background=colors["cyan"],
        ),
        create_left_bubble(colors["orange"], colors["cyan"]),
        widget.Clock(
            fontsize=13,
            format="%Y-%m-%d %a %I:%M %p",
            background=colors["orange"],
            margin=3,
        ),
        create_right_bubble(colors["orange"], "FF6600"),
    ]