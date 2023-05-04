from libqtile.widget.battery import Battery, BatteryState


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
