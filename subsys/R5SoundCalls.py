import os
import random

RES_DIR = os.path.dirname(os.path.abspath("R5-G4.py")) + "/res/"

#sound resources
channelSounds = ['vc1.mp3', 'vc2.mp3', 'vc3.mp3']
randomSounds = ['r1.mp3', 'r2.mp3', 'r3.mp3', 'r4.mp3', 'r5.mp3', 'r6.mp3', 'r7.mp3', 'r8.mp3']
err = 'err.mp3'


def returnChannelSound():
    return RES_DIR + 'vcSounds/' + channelSounds[random.randint(0, 2)]


def returnRandomSound():
    return RES_DIR + 'rSounds/' + randomSounds[random.randint(0, 7)]


def returnAtmosphericSound(arg: str):
    return RES_DIR + 'atmosSounds/' + arg + '.mp3'