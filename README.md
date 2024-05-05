# Music Source Separation with Spleeter

This project utilizes the Spleeter library for source separation, specifically to separate vocals and accompaniment from music tracks.

## Introduction

This project aims to provide a simple implementation of source separation for music tracks. By using Spleeter, a pre-trained deep learning model, it separates vocals and accompaniment from input songs. This can be useful for various applications such as remixing, karaoke generation, and music analysis.

## Requirements

- Python 3.x
- Spleeter library

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/downloads/)
2. Install Spleeter library by running:


## Usage

1. Place your music files (in supported formats like MP3) in the input directory.
2. Run the provided Python script (`separate_music.py`).
3. Separated vocal and accompaniment tracks will be saved in the output directory.


## Configuration

- You can adjust the separation model and parameters in the Python script according to your requirements.
- Ensure correct paths for input and output directories in the script.

## Credits

- Spleeter: [Github Repository](https://github.com/deezer/spleeter)
- Created by [Your Name]
