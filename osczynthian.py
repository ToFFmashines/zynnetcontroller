#!/bin/env python3

import liblo, sys

# send all messages to zynthian 
# on hostname or address 192.168.88.105
# and port 1370 UDP
hostname = 'zynthian.local'
port = 1370

osc_list = {
'b' : 'CHAIN_OPTIONS', # - option screen
'a' : 'SCREEN_AUDIO_MIXER', # - audio mixer screen
'c' : 'CHAIN_CONTROL', # - control screen
'd' : 'SCREEN_ZS3', # - subdsnapshot managment
'e' : 'SCREEN_ADMIN', # - admin screen
'f' : 'SCREEN_ALSA_MIXER', # - audio levels screen
'g' : 'SCREEN_PRESET', # - preset/banks screen
'h' : 'SCREEN_SNAPSHOT', # - snapshot managment
'i' : 'START_AUDIO_RECORD', # - audio record
'j' : 'STOP_AUDIO_RECORD', # - audio stop
'k' : 'START_AUDIO_PLAY', # - audio play
'l' : 'SCREEN_ARRANGER', # - tempo screen
'm' : 'ZYNPOT',
'n' : 'V5_ZYNPOT_SWITCH',
'o' : 'ZYNPOT',
'p' : 'ZYNPOT',
'q' : 'V5_ZYNPOT_SWITCH',
'r' : 'ZYNPOT',
'A' : 'START_MIDI_RECORD', # - midi records
'B' : 'STOP_MIDI_RECORD', # - midi stop
'C' : 'START_MIDI_PLAY', # - midi play
'D' : 'SCREEN_ZYNPAD', # - zynpad screen
'E' : 'BACK', # - back/no
'F' : 'ARROW_UP', # - up arrow
'G' : 'SELECT', # - sel/yes
'H' : 'SCREEN_PATTERN_EDITOR', # - pattern editor
'I' : 'ARROW_LEFT', # - left arrow
'J' : 'ARROW_DOWN', # - down arrow
'K' : 'ARROW_RIGHT', # - right arrow
'L' : 'ALL_SOUNDS_OFF', # - panic all
'M' : 'ZYNPOT',
'N' : 'V5_ZYNPOT_SWITCH',
'O' : 'ZYNPOT',
'P' : 'ZYNPOT',
'Q' : 'V5_ZYNPOT_SWITCH',
'R' : 'ZYNPOT',
}

arg1_list = {
'm' : 0,
'n' : 0,
'o' : 0,
'p' : 1,
'q' : 1,
'r' : 1,
'M' : 2,
'N' : 2,
'O' : 2,
'P' : 3,
'Q' : 3,
'R' : 3,
}


arg2_list = {
'm' : -1,
'n' : 'S',
'o' : 1,
'p' : -1,
'q' : 'S',
'r' : 1,
'M' : -1,
'N' : 'S',
'O' : 1,
'P' : -1,
'Q' : 'S',
'R' : 1,
}

# execute connection to zynthian
try:
    target = liblo.Address(hostname, port)
except liblo.AddressError(err):
    print(err)
    sys.exit()
# show start words
print('Ovládání Zynthianů')
print('Connected to ', hostname, ' Lets play')

# main cycle
run = True

while run:
    seq = input()
    #seq = inp.strip()
    if seq in osc_list:
        com = "/CUIA/" + osc_list[seq]
        arg1 = ''
        arg2 = ''
        if com == "/CUIA/V5_ZYNPOT_SWITCH":
            arg1 = int(arg1_list[seq])
            arg2 = str(arg2_list[seq])
        if com == "/CUIA/ZYNPOT":
            arg1 = int(arg1_list[seq])
            arg2 = int(arg2_list[seq])
        print(com, arg1, arg2)
        liblo.send(target, com, arg1, arg2)
    else:
        print('NonExisting input')


