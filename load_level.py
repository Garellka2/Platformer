from platforms import Platform
from spikes import Spike
from key import Key
from door import Door

def load_level(level, platforms, keys, doors, spikes, all_sprites, platform_height, platform_width, display_height, display_width, spike_width, spike_height):
    if level == 1:
        platform1 = Platform(0, display_height - platform_height, platform_width * 10, platform_height)
        platform2 = Platform(display_width / 2, display_height / 2, platform_width * 2, platform_height)
        spike1 = Spike(display_width / 2 - spike_width, display_height / 2 - spike_height, spike_width, spike_height)
        key1 = Key(display_width / 2 + 50, display_height / 2 - 50)
        door1 = Door(display_width - 50, display_height - 100)

        platforms.add(platform1, platform2)
        spikes.add(spike1)
        keys.add(key1)
        doors.add(door1)
        all_sprites.add(platform1, platform2, spike1, key1, door1)

        return key1, door1