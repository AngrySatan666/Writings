#!/bin/python

## <!-- [SS-0]: Imports ----->
import tkinter as tk
import numpy as np
import sqlite3
import os, sys
import datetime
import time
import configparser
import threading
import json
from dataclasses import dataclass
from typing import Tuple, List, Dict, Optional
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

## <!-- [SS-1]: Global Variables ----->
# /1.1/ Pathing
_dir = os.path.dirname(os.path.abspath(__file__))
dat_dir = os.path.join(_dir, "..", "data")
setf = os.path.join(dat_dir, "settings.ini")

## <!-- [SS-2]: Snippetype Functions ----->
def Info (*args) :
    '''Inform User of Current Task/Status'''
    for txt in args :
        print (f"[INFO] {txt}")
        print ("   ")

def Ok (*args) :
    '''Inform User of Successful Task Completion'''
    for txt in args :
        print (f"[OK] {txt}")

def Warn (*args) :
    '''Inform User of Potential Issues'''
    for txt in args :
        print (f"[WARN] {txt}")
        print ("   ")

def Error (*args) :
    '''Inform User of Fatal Errors'''
    for txt in args :
        print (f"[ERROR] {txt}")
        print ("   ")

def Stamp () :
    '''Return Current Date/Time Stamp'''
    return datetime.datetime.now().strftime ("%Y-%m-%d %H:%M:%S")

## <!-- [SS-3]: Classes ----->
# /3.1/ Qu-Voxels
@dataclass
class QuVoxel:
    amplitude: complex = 0.0 + 0.0j
    probability: float = 0.0
    collapse_state: str = "superposition"
    anchor_score: float = 0.0
    last_updated: float = 0.0

# /3.2/ 3D Quantum Space
class Grid:
    def __init__(self, size_x: int = None, size_y: int = None, size_z: int = None):
        self.Sett()
        self.total_voxels = self.size_x * self.size_y * self.size_z
        self.initialize_grid()
        self.tick = 0

    def Sett (self):
        config = configparser.ConfigParser()
        config.read(setf)
        self.size_x = config.getint('Grid', 'X', fallback=64)
        self.size_y = config.getint('Grid', 'Y', fallback=64)
        self.size_z = config.getint('Grid', 'Z', fallback=64)
        self.vox = config.getfloat('Grid', 'vox', fallback=1.616e-35)

    def initialize_grid(self):
        """Initialize all voxels in the 3D space"""
        Info("Initializing 3D quantum grid...")
        for x in range(self.size_x):
            for y in range(self.size_y):
                for z in range(self.size_z):
                    # Initialize each voxel with random quantum superposition
                    real_part = np.random.normal(0, 0.5)
                    imag_part = np.random.normal(0, 0.5)
                    amplitude = complex(real_part, imag_part)

                    voxel = QuVoxel(
                        amplitude=amplitude,
                        probability=abs(amplitude)**2,
                        collapse_state="superposition",
                        anchor_score=0.0,
                        last_updated=0.0
                    )
                    self.voxel_grid[(x, y, z)] = voxel

        Ok(f"Grid initialized with {len(self.voxel_grid):,} quantum voxels")
