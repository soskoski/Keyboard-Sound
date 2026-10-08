import os
from pynput import keyboard
from pynput import mouse
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUND_SHOT =  os.path.join(BASE_DIR, "audio/gunshot.mp3")
SOUND_RELOAD = os.path.join(BASE_DIR, "audio/reload.mp3")

SOUND_TYPEWRITER = os.path.join(BASE_DIR, "audio/typing_sound.mp3")
SOUND_TYPEWRITER_BELL = os.path.join(BASE_DIR, "audio/typewritter_bell.mp3")

pygame.mixer.init()
shot_sound = pygame.mixer.Sound(SOUND_SHOT)
reload_sound = pygame.mixer.Sound(SOUND_RELOAD)
typewriter_sound = pygame.mixer.Sound(SOUND_TYPEWRITER)
typewriter_bell_sound = pygame.mixer.Sound(SOUND_TYPEWRITER_BELL)

ignored_keys = [keyboard.Key.space, keyboard.Key.backspace]

is_muted = False

print("<ctrl+1> is to toggle mute")
print("<ctrl+2> is to switch to gunshot")
print("<ctrl+3> is to switch to typewriter")

def toggle_mute():
    global is_muted
    if not is_muted:
        pygame.mixer.stop()
        is_muted = True
        print("muted\n")

    else:
        is_muted = False
        print("unmuted\n")

toggle_key = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+1'), toggle_mute)


sound_state = "gunshot"
def set_gunshot_mode():
    global sound_state
    sound_state = "gunshot"
    print("Switched to gunshot mode\n")

def set_typewriter_mode():
    global sound_state
    sound_state = "typewriter"
    print("Switched to typewriter mode\n")

def gunshot_sound_func(key):
    if key == keyboard.Key.enter:
        pygame.mixer.Sound.play(reload_sound)
    else:
        pygame.mixer.Sound.play(shot_sound)

def typewriter_sound_func(key):
    if key == keyboard.Key.enter:
        pygame.mixer.Sound.play(typewriter_bell_sound)

    else:
        pygame.mixer.Sound.play(typewriter_sound)

gunshot_key = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+2'), set_gunshot_mode)
type_key = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+3'), set_typewriter_mode)

is_ctrl_pressed = False

def handle_press(key):

    global is_ctrl_pressed

    if key in (keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        is_ctrl_pressed = True

    canonical_key = listener.canonical(key)
    toggle_key.press(canonical_key)
    gunshot_key.press(canonical_key)
    type_key.press(canonical_key)

    if is_ctrl_pressed or key in ignored_keys:
        return

    if is_muted:
        return

    if sound_state == "gunshot":
        gunshot_sound_func(key)
    elif sound_state == "typewriter":
        typewriter_sound_func(key)


def handle_release(key):
    global is_ctrl_pressed

    if key in (keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        is_ctrl_pressed=False

    canonical_key = listener.canonical(key)
    toggle_key.release(canonical_key)
    gunshot_key.release(canonical_key)
    type_key.release(canonical_key)

listener = keyboard.Listener(on_press=handle_press, on_release=handle_release)

with listener:
    listener.join()