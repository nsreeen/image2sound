
from images import process_image
from sounds import get_audio_segment
from tune import get_sound

if __name__ == "__main__":
    sample_rate = 44100
    beats = 2
    photos = ["i1c.jpg", "i2c.jpg", "i3c.jpg"]
    processed = []
    for p in photos:
        image, labelled_image, blobs = process_image(p)
        sounds = [get_sound(b, beats, sample_rate) for b in blobs if b.width < 100]
        audio_segment = get_audio_segment(sounds, beats, sample_rate)
        processed.append([image, labelled_image, audio_segment, blobs, sounds])
