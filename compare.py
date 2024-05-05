from pydub import AudioSegment

# Load the original vocal file
original = AudioSegment.from_mp3(r'C:\Users\Saarthak\Desktop\datasets\songs\O Saathi Re Male - Muqaddar Ka Sikandar 320 Kbps\vocalsCorrect.mp3')

# Load the extracted vocal file
extracted = AudioSegment.from_mp3(r'C:\Users\Saarthak\Desktop\datasets\songs\O Saathi Re Male - Muqaddar Ka Sikandar 320 Kbps\vocals.wav')

# Invert the phase of the extracted vocal
inverted = extracted.invert_phase()

# Mix the original and inverted tracks together
mixed = original.overlay(original)

# Save the result
mixed.export(r'C:\Users\Saarthak\Desktop\datasets\songs\O Saathi Re Male - Muqaddar Ka Sikandar 320 Kbps\mixed2.mp3', format='mp3')
