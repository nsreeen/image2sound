import sys

from image_processor import process_image
from sound_generator import get_audio_segment
from tuner import get_sound

SAMPLE_RATE = 44100
BEATS = 2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Incorrect number of arguments.  Call like this: `python image2sound input_image_path.jpg output_file_name`")
    else:
        input_file = sys.argv[1]
        output_file_name = sys.argv[2]

        image, labelled_image, blobs = process_image(input_file)
        sounds = [get_sound(b, BEATS, SAMPLE_RATE) for b in blobs if b.width < 100]
        audio_segment = get_audio_segment(sounds, BEATS, SAMPLE_RATE)
        
        audio_segment.export(output_file_name, format="mp3")
