import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import keymaps
import psutil


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])


mod = "mod4"

keys = keymaps.init_keymaps(mod)


def init_group_names():
    return [
        ("DEV", {"layout": "monadtall"}),
        ("WWW", {"layout": "monadtall", "matches": [Match(wm_class=["firefox"])]}),
        ("CHAT", {"layout": "monadtall", "matches": [Match(wm_class=["discord"])]}),
    ]


def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]


group_names = init_group_names()
groups = init_groups()

for index, (name, kwargs) in enumerate(group_names, 1):
    keys.extend(
        [
            # Change current group with mod + number
            Key(
                [mod],
                str(index),
                lazy.group[name].toscreen(),
                desc="Switch to group {}".format(name),
            ),
            # Move window to new group with mod + shift + number
            Key(
                [mod, "shift"],
                str(index),
                lazy.window.togroup(name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(name),
            ),
        ]
    )

layouts = [
    layout.MonadTall(border_focus="#008ECC", border_normal="#000000", margin=8),
    layout.Max(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


# Bar colors
def init_colors():
    return [
        ["#282a36", "#282a36"],
        ["#FF0000", "#FF0000"],
        ["#ffffff", "#ffffff"],
        ["#000000", "#000000"],
        ["#000000", "#000000"],
    ]


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


def batter_discharge_icon():
    battery = psutil.sensors_battery()
    if battery.percent < 13:
        return ""
    if battery.percent < 80:
        return ""


colors = init_colors()

screens = [
    Screen(
        wallpaper="~/.config/qtile/zelda_background.jpg",
        wallpaper_mode="stretch",
        top=bar.Bar(
            [
                create_left_bubble("#DD5500", "#DD5500"),
                widget.TextBox(
                    text="",
                    font="Hack Nerd Font",
                    padding=0,
                    fontsize=40,
                    background="#DD5500",
                ),
                create_right_bubble("#DD5500", "#29A8AB"),
                widget.GroupBox(
                    highlight_method="block",
                    this_current_screen_border="#DD5500",
                    background="#29A8AB",
                ),
                create_right_bubble("#29A8AB"),
                widget.WindowName(),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                create_left_bubble("#DD5500"),
                widget.ThermalSensor(
                    fontsize=15, format=" {temp:.1f}{unit}", background="#DD5500"
                ),
                create_left_bubble("#29A8AB", "#DD5500"),
                widget.CPU(
                    fontsize=15,
                    format=" {freq_current}GHz {load_percent}%",
                    background="#29A8AB",
                ),
                create_left_bubble("#DD5500", "#29A8AB"),
                widget.Memory(
                    fontsize=15,
                    format=" {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}",
                    measure_mem="G",
                    background="#DD5500",
                ),
                create_left_bubble("#29A8AB", "#DD5500"),
                widget.Systray(background="#29A8AB"),
                create_left_bubble("#DD5500", "#29A8AB"),
                widget.Volume(fontsize=15, fmt=" {}", background="#DD5500"),
                create_left_bubble("#29A8AB", "#DD5500"),
                widget.Battery(
                    fontsize=15,
                    background="#29A8AB",
                    full_char="",
                    discharge_char=batter_discharge_icon(),
                    charge_char="",
                    empty_char="",
                    unknown_char="",
                    format="{char} {percent:2.0%}",
                    notify_below=20,
                ),
                create_left_bubble("#DD5500", "#29A8AB"),
                widget.Clock(
                    fontsize=13,
                    format="%Y-%m-%d %a %I:%M %p",
                    background="#DD5500",
                    margin=3,
                ),
                create_right_bubble("#DD5500", "FF6600"),
            ],
            30,
            margin=[4, 6, 4, 6],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"
