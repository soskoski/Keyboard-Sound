import os
from pynput import keyboard
from pynput import mouse
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUND_SHOT =  os.path.join(BASE_DIR, "audio/gunshot.mp3")
SOUND_RELOAD = os.path.join(BASE_DIR, "audio/reload.mp3")

pygame.mixer.init()
shot = pygame.mixer.Sound(SOUND_SHOT)
reload = pygame.mixer.Sound(SOUND_RELOAD)

ignored_keys = [keyboard.Key.space, keyboard.Key.backspace]

def on_press(key):
    if key in ignored_keys:
        return

    if key == keyboard.Key.enter:
        pygame.mixer.Sound.play(reload)
        return
    
    pygame.mixer.Sound.play(shot)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()