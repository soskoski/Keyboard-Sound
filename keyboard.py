import os
from pynput import keyboard
from pynput import mouse
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUND_SHOT =  os.path.join(BASE_DIR, "audio/gunshot.mp3")
SOUND_RELOAD = os.path.join(BASE_DIR, "audio/reload.mp3")

pygame.mixer.init()
shot_sound = pygame.mixer.Sound(SOUND_SHOT)
reload_sound = pygame.mixer.Sound(SOUND_RELOAD)

ignored_keys = [keyboard.Key.space, keyboard.Key.backspace]

def mute():
    pygame.mixer.pause()
    print("Muted!\n")

def unmute():
    pygame.mixer.unpause()
    print("Unmute!\n")

pause = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+1'), mute)
unpause = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+1'), unmute)
is_ctrl_pressed = False

def handle_press(key):

    global is_ctrl_pressed

    if key in (keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        is_ctrl_pressed = True

    canonical_key = listener.canonical(key)
    pause.press(canonical_key)

    if is_ctrl_pressed:
        return

    if key in ignored_keys:
        return

    if key == keyboard.Key.enter:
        pygame.mixer.Sound.play(reload_sound)
        return
    
    pygame.mixer.Sound.play(shot_sound)

def handle_release(key):
    canonical_key = listener.canonical(key)
    pause.release(canonical_key)

listener = keyboard.Listener(on_press=handle_press, on_release=handle_release)

with listener:
    listener.join()