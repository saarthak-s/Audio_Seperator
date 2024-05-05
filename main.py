from spleeter.separator import Separator

if __name__ == '__main__':
    # Initialize Spleeter with 'spleeter:2stems' model (vocals/accompaniment separation)
    separator = Separator('spleeter:2stems')

    # Provide the path to the input song file
    input_song = r'C:\Users\Saarthak\Desktop\datasets\O Saathi Re Male - Muqaddar Ka Sikandar 320 Kbps.mp3'

    # Perform vocal extraction
    separator.separate_to_file(input_song, r'C:\Users\Saarthak\Desktop\datasets\songs')

