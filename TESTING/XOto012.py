"""
blag blag lbag

Code by: Kevin Moen Storvik
Version: 0
"""
from modbus_communication import ModbusClient
from gamechecker import GameChecker
import random
import cv2
import time


class translate(object):

    def XOto12(self, state):
        newstate = [0,0,0,0,0,0,0,0,0]

        index = 0
        if state[index] == "X":
            newstate.insert(1)
        elif state[index] == "0":
            newstate.insert(2)
        elif state[index] == "-":
            newstate.insert(0)
        index += 1
        if state[index] == "X":
            newstate.insert(1)
        elif state[index] == "0":
            newstate.insert(2)
        elif state[index] == "-":
            newstate.insert(0)
        index += 1
        if state[index] == "X":
            newstate.insert(1)
        elif state[index] == "0":
            newstate.insert(2)
        elif state[index] == "-":
            newstate.insert(0)
        index += 1
        if state[index] == "X":
            newstate.insert(1)
        elif state[index] == "0":
            newstate.insert(2)
        elif state[index] == "-":
            newstate.insert(0)
        index += 1
        if state[index] == "X":
            newstate.insert(1)
        elif state[index] == "0":
            newstate.insert(2)
        elif state[index] == "-":
            newstate.insert(0)
        index += 1
        if state[index] == "X":
            newstate.insert(1)
        elif state[index] == "0":
            newstate.insert(2)
        elif state[index] == "-":
            newstate.insert(0)
        index += 1
        if state[index] == "X":
            newstate.insert(1)
        elif state[index] == "0":
            newstate.insert(2)
        elif state[index] == "-":
            newstate.insert(0)
        index += 1
        if state[index] == "X":
            newstate.insert(1)
        elif state[index] == "0":
            newstate.insert(2)
        elif state[index] == "-":
            newstate.insert(0)
        index += 1
        if state[index] == "X":
            newstate.insert(1)
        elif state[index] == "0":
            newstate.insert(2)
        elif state[index] == "-":
            newstate.insert(0)


