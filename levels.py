from player import Player
from platforms import Platform
from spikes import Spike
from key import Key
from door import Door

def load_level(level,platforms,keys,doors,spikes,all_sprites,platform_height,platform_width,display_height,display_width,spike_width,spike_height):
    platforms.empty()
    spikes.empty()
    keys.empty()
    doors.empty()

    if level == 1:
        platform1 = Platform(0,10*platform_height,platform_width,platform_height)
        platform2 = Platform(2*platform_width,6*platform_height,platform_width/2,platform_height)
        platform3 = Platform(2*platform_width,14*platform_height,platform_width*1.5,platform_height)
        platform4 = Platform(4*platform_width,11*platform_height,platform_width,platform_height)
        platform5 = Platform(4*platform_width,20*platform_height,platform_width*2,platform_height)
        platform6 = Platform(5*platform_width,8*platform_height,platform_width*3,platform_height)
        platform7 = Platform(6*platform_width,17*platform_height,platform_width*2,platform_height)
        platform8 = Platform(8*platform_width,14*platform_height,platform_width*2,platform_height)
        platform9 = Platform(9*platform_width,11*platform_height,platform_width,platform_height)
        platform10 = Platform(10*platform_width,18*platform_height,platform_width,platform_height)
        platform11 = Platform(11*platform_width,7*platform_height,platform_width,platform_height)
        platform_ground = Platform(0,display_height-platform_height,display_width,platform_height)
        platforms.add(platform1,platform_ground,platform2,platform3,platform4,platform5,platform6,platform7,platform8,platform9,
                platform10,platform11)

        spike1 = Spike(4*platform_width,10*platform_height,spike_width,spike_height)
        spike2 = Spike(5*platform_width,19*platform_height,spike_width,spike_height)
        spike3 = Spike(6*platform_width,7*platform_height,spike_width,spike_height)
        spike4 = Spike(7*platform_width,16*platform_height,spike_width,spike_height)
        spike5 = Spike(8.5*platform_width,13*platform_height,spike_width,spike_height)
        spike6 = Spike(10*platform_width,17*platform_height,spike_width,spike_height)
        spike7 = Spike(11*platform_width,6*platform_height,spike_width,spike_height)
        spike8 = Spike(3*platform_width,22*platform_height,spike_width,spike_height)
        spikes.add(spike1,spike2,spike3,spike4,spike5,spike6,spike7,spike8)

        key1=Key(2.5*platform_width,13*platform_height)
        keys.add(key1)

        door1 = Door(14.5*platform_width,19*platform_height)
        doors.add(door1)

        all_sprites.add(platform1,platform_ground,platform2,platform3,platform4,platform5,platform6,platform7,platform8,platform9,
                    platform10,platform11)
        all_sprites.add(spike1,spike2,spike3,spike4,spike5,spike6,spike7,spike8)
    elif level == 2:
        pass
    return key1,door1