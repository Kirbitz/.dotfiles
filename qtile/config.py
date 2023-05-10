import os
import subprocess
from libqtile import bar, layout, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import keymaps
import Widgets


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
    layout.Floating(border_focus="#008ECC", border_normal="#000000"),
]


# Bar colors
def init_colors():
    return {
        "orange": "#DD5500",
        "cyan": "#29A8AB",
        "red": "#ED2939",
        "green": "#50C878",
        "black": "#000000",
    }


colors = init_colors()
widgets_list = Widgets.init_widgets(colors)

screens = [
    Screen(
        wallpaper="~/.config/qtile/zelda_background.jpg",
        wallpaper_mode="stretch",
        top=bar.Bar(
            widgets_list,
            30,
            margin=[4, 6, 4, 6],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [],
        "Button3",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
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
