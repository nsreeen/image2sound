from sound_model import Sound

def get_sound(blob, beats, sample_rate):
    return Sound(
            frequency=tune(normalise((1000 - blob.area), 0, 1000, 150, 450)),
            amplitude=2048/2,
            duration=normalise(blob.width, 0, 200, 1, beats),
            offset=int(normalise(blob.x, 0, 250, 0, sample_rate*beats)),
            decreasing=blob.y < blob.center_y,
            volume=1 if blob.width < 500 else 0.5,
    )


def normalise(value, min_input, max_input, min_output, max_output):
    if value > max_input:
        value = max_input
    value = value if value <= max_input else max_input
    value = value if value >= min_input else min_input
    return ((value - min_input) / (max_input - min_input)) * (max_output - min_output) + min_output


def tune(frequency):
    tuned_frequencies = {
    "C2": 65.40639132514966,
    "C3": 130.8127826502993,
    "C4": 261.6255653005986,
    "D4": 293.6647679174076,
    "E4": 329.6275569128699,
    "F4": 349.2282314330039,
    "G4": 391.99543598174927,
    "A4": 440.0,
    "B4": 493.8833012561241,
    "C5": 523.2511306011972,
    }
    for f in tuned_frequencies.values():
        if frequency < f:
            return f
