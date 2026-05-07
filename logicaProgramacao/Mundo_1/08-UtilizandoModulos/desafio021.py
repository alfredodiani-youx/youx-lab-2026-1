#Faça um programa em Pyton que abra e reproduza o audio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()