import numpy as numpy
from scipy.io import wavfile
from pydub import AudioSegment
from pydub.playback import play



def get_audio_segment(sounds, beats, sample_rate):
    combined = sine_wave_to_audio_segment(numpy.zeros(sample_rate*(beats)), sample_rate) # cuts off if dont add beat - why?
    for sound in sounds:
        sine_wave = get_sine_wave(sound.frequency, sound.duration, sample_rate, amplitude=sound.amplitude)
        offset_sine_wave = numpy.concatenate([numpy.zeros(sound.offset),sine_wave])
        audio_segment = sine_wave_to_audio_segment(offset_sine_wave, sample_rate)
        if sound.volume < 1:
            audio_segment = audio_segment - 15
        combined = combined.overlay(audio_segment)
    return combined

# this function and tuned frequency values are from: https://towardsdatascience.com/music-in-python-2f054deb41f4
def get_sine_wave(frequency, duration, sample_rate, amplitude=4096):
    theta = numpy.linspace(0, duration, int(sample_rate*duration))
    wave = amplitude*numpy.sin(2*numpy.pi*frequency*theta)
    return wave

def sine_wave_to_audio_segment(sine_wave, sample_rate):
    return AudioSegment(
        sine_wave.astype("float32").tobytes(),
        frame_rate=sample_rate,
        sample_width=4,
        channels=1
    )
