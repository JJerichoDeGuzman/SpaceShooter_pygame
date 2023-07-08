import pygame 
import os 
import random
import time 

#Upload assets 
#Enemies assets
RedSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GreenSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BlueSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
RedLaser = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GreenLaser = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BlueLaser = pygame.image.load(os.path.join("assets","pixel_laser_blue.png"))

#Player Asset
PlayerPixelShip = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
YellowLaser = pygame.image.load(os.path.join("assets","pixel_laser_yellow.png"))

#upload background
BlackBackground = pygame.image.load(os.path.join("assets","background-black.png"))

