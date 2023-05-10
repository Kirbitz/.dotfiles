from libqtile.widget.battery import Battery, BatteryState
from libqtile.widget.volume import Volume
import subprocess


battery_icon_list = ["", "", "", "", "", "", "", "", "", ""]


class BatteryWrapper(Battery):
    def build_string(self, status):
        if status.state == BatteryState.DISCHARGING:
            # updates battery icon based on position in array
            # battery percent is multiplied by 10 then converted to int
            # inorder to get position of icon
            char = battery_icon_list[int(status.percent * 10)]
        elif status.percent >= 1 or status.state == BatteryState.FULL:
            char = ""
        elif status.state == BatteryState.EMPTY or (
            status.state == BatteryState.UNKNOWN and status.percent == 0
        ):
            char = ""
        else:
            char = ""
        return self.format.format(char=char, percent=status.percent)


class VolumeWrapper(Volume):
    def _configure(self, qtile, bar):
        Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        char = ""
        if self.volume <= 0:
            char = "婢"
        elif self.volume <= 33:
            char = ""
        elif self.volume < 66:
            char = "墳"
        self.text = f"{char} {self.volume if self.volume > 0 else 'M'}% "

    def _update_drawer(self, wob=False):
        char = ""
        if self.volume <= 0:
            char = "婢"
        elif self.volume <= 33:
            char = ""
        elif self.volume < 66:
            char = "墳"
        self.text = f"{char} {self.volume if self.volume > 0 else 'M'}% "
        self.draw()


def network():
    command = "nmcli|grep interface|awk '{print $2}'"
    proc = subprocess.Popen(
        command, universal_newlines=True, shell=True, stdout=subprocess.PIPE
    )
    output = proc.stdout.read()

    if output != "":
        output = output.split()
        output = list(dict.fromkeys(output))

        if output[0] == "wlp5s0":
            command = (
                "nmcli|grep wlp5s0|head -1|awk '{ for (i=4; i<=NF; i++) printf $i }'"
            )
            output = subprocess.Popen(
                command, universal_newlines=True, shell=True, stdout=subprocess.PIPE
            ).stdout.read()
            output = output.rstrip("\n")
            output = "  " + output + " "
            return output

        else:
            command = "nmcli | grep {}".format(output[0])
            proc = subprocess.Popen(
                command, universal_newlines=True, shell=True, stdout=subprocess.PIPE
            )
            output = proc.stdout.read()
            output = " " + output[42:49]
            return output

    else:
        output = "睊 Not connected"
        return output
