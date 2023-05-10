from libqtile import widget
from WidgetWrapper import BatteryWrapper, VolumeWrapper, network

widgets_defaults = dict(font="Hack Nerd Font", fontsize=13)


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
        widget.Sep(linewidth=5, background=colors["black"], foreground=colors["black"]),
        widget.Image(
            filename="~/.config/qtile/python-logo.png",
            background=colors["black"],
            margin=3,
        ),
        widget.Sep(linewidth=5, background=colors["black"], foreground=colors["black"]),
        widget.GroupBox(
            highlight_method="block",
            this_current_screen_border=colors["orange"],
            fontsize=12,
        ),
        widget.Sep(linewidth=5, background=colors["black"], foreground=colors["black"]),
        widget.WindowName(),
        create_left_bubble(colors["cyan"]),
        widget.CheckUpdates(
            background=colors["cyan"],
            custom_command="apt-show-versions -u -b",
            distro="debian",
            display_format="痢 {updates} pkgs ",
            **widgets_defaults,
        ),
        create_left_bubble(colors["orange"], colors["cyan"]),
        widget.GenPollText(
            func=network,
            background=colors["orange"],
            **widgets_defaults,
        ),
        create_left_bubble(colors["cyan"], colors["orange"]),
        widget.CPU(
            format=" {load_percent}% ",
            background=colors["cyan"],
            **widgets_defaults,
        ),
        widget.Memory(
            format=" {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm} ",
            measure_mem="G",
            background=colors["cyan"],
            **widgets_defaults,
        ),
        widget.ThermalSensor(
            format=" {temp:.1f}{unit} ",
            background=colors["cyan"],
            **widgets_defaults,
        ),
        create_left_bubble(colors["orange"], colors["cyan"]),
        widget.Backlight(
            brightness_file="/sys/class/backlight/intel_backlight/brightness",
            max_brightness_file="/sys/class/backlight/intel_backlight/max_brightness",
            fmt=" {} ",
            background=colors["orange"],
            **widgets_defaults,
        ),
        VolumeWrapper(
            background=colors["orange"],
            **widgets_defaults,
        ),
        BatteryWrapper(
            format="{char} {percent:2.0%} ",
            show_short_text=False,
            low_percentage=0.25,
            update_interval=15,
            background=colors["orange"],
            **widgets_defaults,
        ),
        create_left_bubble(colors["cyan"], colors["orange"]),
        widget.Systray(background=colors["cyan"]),
        widget.Sep(linewidth=10, background=colors["cyan"], foreground=colors["cyan"]),
        create_left_bubble(colors["orange"], colors["cyan"]),
        widget.Clock(
            format=" %Y-%m-%d %a %I:%M %p",
            background=colors["orange"],
            margin=3,
            **widgets_defaults,
        ),
        create_right_bubble(colors["orange"], "FF6600"),
    ]
