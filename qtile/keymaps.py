from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


terminal = guess_terminal()


def init_keymaps(modKey):
    return [
        # Switch between windows
        Key([modKey], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([modKey], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([modKey], "j", lazy.layout.down(), desc="Move focus down"),
        Key([modKey], "k", lazy.layout.up(), desc="Move focus up"),
        Key(
            [modKey],
            "space",
            lazy.layout.next(),
            desc="Move window focus to other window",
        ),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key([modKey, "shift"], "h", lazy.layout.swap_left()),
        Key([modKey, "shift"], "l", lazy.layout.swap_right()),
        Key(
            [modKey, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"
        ),
        Key([modKey, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        # Adjust window sizes and orient layout
        Key([modKey], "i", lazy.layout.grow()),
        Key([modKey], "m", lazy.layout.shrink()),
        Key([modKey], "space", lazy.window.toggle_fullscreen()),
        Key([modKey], "f", lazy.layout.flip()),
        Key([modKey, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([modKey, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([modKey], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key(
            [modKey, "shift"],
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),
        Key([modKey], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        # Toggle between different layouts as defined below
        Key([modKey], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([modKey], "x", lazy.window.kill(), desc="Kill focused window"),
        Key([modKey, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([modKey, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        Key(
            [modKey],
            "d",
            lazy.spawn(
                "rofi -show-icons -theme /usr/share/rofi/themes/rounded-purple-dark.rasi -show drun"
            ),
            desc="Spawn a command using a prompt widget",
        ),
        # Brightness Keys
        Key([], "XF86MonBrightnessUp", lazy.spawn("amixer sset Master toggle")),
        Key([], "XF86MonBrightnessDown", lazy.spawn("amixer sset Master toggle")),
        # Volume Keys
        Key(
            [],
            "XF86AudioMute",
            lazy.spawn("amixer sset Master toggle"),
            desc="Unmutes the volume",
        ),
        Key(
            [],
            "XF86AudioLowerVolume",
            lazy.spawn("amixer sset Master 2%-"),
            desc="Decrease Volume by 2%",
        ),
        Key(
            [],
            "XF86AudioRaiseVolume",
            lazy.spawn("amixer sset Master 2%+"),
            desc="Increase Volume by 2%",
        ),
        # Print screen key
        Key(
            [modKey, "shift"],
            "p",
            lazy.spawn("gnome-screenshot -i"),
            desc="Opens Screenshot prompt",
        ),
    ]
