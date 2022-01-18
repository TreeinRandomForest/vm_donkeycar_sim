import time

import gym
import gym_donkeycar
import matplotlib.pylab as plt
plt.ion()

import sys

SIM_HOST = None

port = 9091
if not SIM_HOST:
    exe_path = 'DonkeySimLinux/donkey_sim.x86_64'

    conf = {'exe_path': exe_path, 'port': port}
else:
    raise NotImplementedError("Needs to be done")


env = gym.make('donkey-generated-track-v0', conf=conf)

s = env.reset()
plt.imshow(s)

counter = 0
ilist = []
while counter <= 100:
    action = (1., 1.) #(angle \in [-1,1], throttle \in [-1,1])

    #if model, action would be:
    #action = model(s)

    s,r,d,i = env.step(action)
    time.sleep(0.1) #car runs at this setting for 0.1 seconds
    plt.imshow(s)

    counter += 1
    ilist.append(i)
