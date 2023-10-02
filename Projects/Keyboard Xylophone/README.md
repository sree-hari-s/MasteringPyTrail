# Keyboard Xylophone

Play sounds based on value of key pressed.

## Description

Listen for key events and play a tone based on its value.

Listening for key events is handled by the `pynput` thread.
Playing sounds is handled by the `KeyboardXylophone` class.

Volume, duration and frequency of the tone can be changed by arguments passed at instantiation.

The keyboard listener thread exits if `Esc` is pressed.

## Libraries

- [pynput](https://pypi.org/project/pynput/) - key event listening
- [boombox](https://pypi.org/project/boombox/) - sound support