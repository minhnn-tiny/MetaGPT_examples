## sounds.py
import pygame
import os

class Sounds:
    def __init__(self):
        # Initialize the pygame mixer module
        pygame.mixer.init()
        # Define the path to the sounds directory
        self.sounds_path = "sounds/"
        # Load sound files with default values
        self.sounds = {
            'flap': pygame.mixer.Sound(os.path.join(self.sounds_path, "flap.wav")),
            'hit': pygame.mixer.Sound(os.path.join(self.sounds_path, "hit.wav")),
            'point': pygame.mixer.Sound(os.path.join(self.sounds_path, "point.wav")),
            'swoosh': pygame.mixer.Sound(os.path.join(self.sounds_path, "swoosh.wav"))
        }
        # Set a default volume for all sounds
        for sound in self.sounds.values():
            sound.set_volume(0.5)

    def play_sound(self, sound_type: str) -> None:
        """
        Play a sound based on the sound_type argument.
        
        Args:
            sound_type (str): The type of sound to play. Must be one of 'flap', 'hit', 'point', or 'swoosh'.
        """
        if sound_type in self.sounds:
            self.sounds[sound_type].play()
        else:
            print(f"Warning: The sound type '{sound_type}' is not recognized.")
