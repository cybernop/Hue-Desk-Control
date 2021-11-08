import json
from pathlib import Path

from phue import Bridge


class Hue_Control:
    bridge: Bridge = None

    def __init__(self, ip: str):
        self.bridge = Bridge(ip)
        self.bridge.connect()

    def turn_on(self, group: str):
        self.__switch(group, True)

    def turn_off(self, group: str):
        self.__switch(group, False)

    def __switch(self, group_name: str, on: bool):
        group = self.bridge.get_group(group_name)
        lights = self.bridge.get_light_objects('id')
        for light_id in group['lights']:
            lights[int(light_id)].on = on


if __name__ == "__main__":
    import sys

    config = json.loads(Path('config.json').read_text())
    ip = config['ip']
    group = config['group']

    control = Hue_Control(ip)

    if 'on' in sys.argv:
        control.turn_on(group)
    elif 'off' in sys.argv:
        control.turn_off(group)
