"""Play sounds based on value of key pressed."""

import os
from typing import Optional, Union

if os.name == "posix":
    from boombox import GstBoomBox as BoomBox
else:
    from boombox import BoomBox

from pynput import keyboard
from pynput.keyboard import Key, KeyCode


class KeyboardXylophone:
    """Listen for key events and play a tone based on its value."""

    def __init__(
        self, duration_ms: int = 250, volume: float = 0.1, freq_mul: int = 10
    ) -> None:
        """Initialise instance."""
        self._boombox = BoomBox("")
        self.duration_ms = duration_ms
        self.volume = volume
        self.freq_mul = freq_mul

    def play_sound(self, frequency: float) -> None:
        """Play sound at given frequency."""
        self._boombox.play_tone(frequency, self.duration_ms, self.volume)

    def on_press(self, key: Optional[Union[Key, KeyCode]]) -> None:
        """Play sound on key press."""
        try:
            self.play_sound(ord(key.char) * self.freq_mul)
        except AttributeError:
            pass

    def on_release(self, key: Optional[Union[Key, KeyCode]]) -> Optional[bool]:
        """Return False if Escape is released."""
        if key == keyboard.Key.esc:
            return False
        return None

    def run(self) -> None:
        """Start listening for key events."""
        with keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        ) as listener:
            listener.join()


if __name__ == "__main__":
    kbdxylo = KeyboardXylophone()
    kbdxylo.run()
