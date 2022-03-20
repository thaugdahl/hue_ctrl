#!/bin/python3
import requests
import json

from light import Light
from group import Group
from config import *
from time import sleep
from random import randint
import math

def get_light(id):
    global api_url

    response = requests.get(api_url + "lights/" + id)

    print(response)

def get_groups():
    global api_url

    response = requests.get(api_url + "groups").json()

    groups = {}
    for k in response.keys():
        new_group = Group()
        new_group.name = response[k]['name']
        new_group.id = k

        new_group.action_url = api_url + "groups/" + str(k) + "/action"

        lights = response[k]['lights']


        for i in lights:
            instance = Light.construct_from_id(int(i))
            new_group.lights.append(instance)

        groups[k] = new_group

    return groups


groups = get_groups()

lights_to_change = []

for k in groups.keys():
    # print(groups[k])

    for i in groups[k].lights:
        if i.id == 9:
            lights_to_change.append(i)


for i in range(0, 101, 1):
    light = lights_to_change[0]

    # current_ct = math.sin(i / math.pi) * 50 + 50
    # current_bri = math.cos(i / (0.5*math.pi)) * 50 + 50

    light.set_hue(math.cos(i/(2*math.pi))*50 + 50)

    sleep(1)

