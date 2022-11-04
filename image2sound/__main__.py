
from image_processor import process_image
from sound_generator import get_audio_segment
from tuner import get_sound

SAMPLE_RATE = 44100
BEATS = 2

if __name__ == "__main__":
    photos = ["images/i1c.jpg", "images/i2c.jpg", "images/i3c.jpg"]
    processed = []
    for p in photos:
        image, labelled_image, blobs = process_image(p)
        sounds = [get_sound(b, BEATS, SAMPLE_RATE) for b in blobs if b.width < 100]
        audio_segment = get_audio_segment(sounds, BEATS, SAMPLE_RATE)
        processed.append([image, labelled_image, audio_segment, blobs, sounds])
