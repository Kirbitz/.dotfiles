from libqtile import widget
from WidgetWrapper import BatteryWrapper, VolumeWrapper, network

widgets_defaults = dict(font="Hack Nerd Font", fontsize=15)


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
        widget.Systray(background=colors["orange"]),
        widget.Sep(
            linewidth=10, background=colors["orange"], foreground=colors["orange"]
        ),
        create_left_bubble(colors["cyan"], colors["orange"]),
        widget.GenPollText(
            func=network,
            background=colors["cyan"],
            **widgets_defaults,
        ),
        create_left_bubble(colors["orange"], colors["cyan"]),
        widget.CPU(
            format=" {freq_current}GHz {load_percent}% ",
            background=colors["orange"],
            **widgets_defaults,
        ),
        widget.Memory(
            format=" {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm} ",
            measure_mem="G",
            background=colors["orange"],
            **widgets_defaults,
        ),
        widget.ThermalSensor(
            format=" {temp:.1f}{unit} ",
            background=colors["orange"],
            **widgets_defaults,
        ),
        create_left_bubble(colors["cyan"], colors["orange"]),
        widget.Backlight(
            brightness_file="/sys/class/backlight/intel_backlight/brightness",
            max_brightness_file="/sys/class/backlight/intel_backlight/max_brightness",
            fmt=" {} ",
            background=colors["cyan"],
            **widgets_defaults,
        ),
        VolumeWrapper(
            background=colors["cyan"],
            **widgets_defaults,
        ),
        BatteryWrapper(
            format="{char} {percent:2.0%} ",
            show_short_text=False,
            low_percentage=0.25,
            update_interval=15,
            background=colors["cyan"],
            **widgets_defaults,
        ),
        create_left_bubble(colors["orange"], colors["cyan"]),
        widget.Clock(
            format=" %Y-%m-%d %a %I:%M %p",
            background=colors["orange"],
            margin=3,
            **widgets_defaults,
        ),
        create_right_bubble(colors["orange"], "FF6600"),
    ]
