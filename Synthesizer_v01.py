import numpy as np
import sounddevice as sd
import time
from pynput.keyboard import Key, Listener


def sample(freq_hz=440.0):
    # Samples per second
    sps = 44100  # DONT CHANGE ?? 44100
    # Frequency / Pitch
    # freq_hz = 440.0
    # Rate
    rate = 2
    # Carrier Amplitude
    ac = 1.0
    # Sensitivity
    ka = 0.25
    # Modulator
    modulator_hz = 0.25
    # Duration
    duration_s = 0.5
    # Attenuation so the sound is reasonable
    atten = 0.3

    # NCalculate the sine wave
    t_samples = np.arange(duration_s * sps)
    waveform = np.sin(2 * np.pi * freq_hz * t_samples / sps)

    # Modulate the carrier
    modulator = np.sin(rate * np.pi * modulator_hz * t_samples / sps)
    envelope = ac * (1.0 + ka * modulator)
    modulated = waveform * envelope

    # Dampen
    waveform_quiet = modulated * atten
    modulated_ints = np.int16(waveform_quiet * 32767)  # 32767 is maximum value of an unsigned 16 bit integer

    sd.play(modulated_ints, sps)
    # time.sleep(duration_s)
    # sd.stop()


def on_press(key):
    # print('{0} release'.format(key))
    try:
        if key == Key.esc:
            # Stop listener
            return False
        if key.char == ('a'):
            sample(freq_hz=440.0)
        if key.char == ('s'):
            sample(freq_hz=480.0)
        if key.char == ('d'):
            sample(freq_hz=520.0)
        if key.char == ('f'):
            sample(freq_hz=560.0)
        if key.char == ('g'):
            sample(freq_hz=600.0)
        if key.char == ('h'):
            sample(freq_hz=640.0)
        if key.char == ('j'):
            sample(freq_hz=680.0)
        if key.char == ('k'):
            sample(freq_hz=720.0)
        if key.char == ('l'):
            sample(freq_hz=760.0)
    except:
        return


def on_release(key):
    # print('{0} pressed'.format(key))
    pass


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()




