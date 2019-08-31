from collections import namedtuple

UIM435 = namedtuple('UIM435',
    ['start','stop','move_right','move_left'])

def uim_right(velocity):
    print(f'uim right {velocity}')

def uim_left(velocity):
    print(f'uim left {velocity}')

def uim_start():
    print('uim start')

def uim_stop():
    print('uim stop')

uim = UIM435(start=uim_start,stop=uim_stop,move_right=uim_right,move_left=uim_left)

uim = UIM435(
    start=uim_start,
    stop=uim_stop,
    move_right=uim_right,
    move_left=uim_left
)