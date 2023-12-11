# Whisper ASR CLI

Whisper ASR CLI is a command-line interface for Automatic Speech Recognition (ASR) using OpenAI's Whisper ASR model. It allows users to record audio, save it to a file, and obtain transcriptions using the Whisper ASR model.

## Motivation

Speech recognition is a fundamental component of many applications, including voice assistants, transcription services, and more. The goal of this project is to provide a simple and user-friendly interface for leveraging the power of OpenAI's Whisper ASR model.

## Features

- Record audio from the command line.
- Save recorded audio to a specified file.
- Obtain transcriptions using the Whisper ASR model.

## How it Works

1. **Record Audio:**
   - Press 'R' to start recording.
   - Press 'S' to stop recording.
   - Press 'Q' to quit the recording process.

2. **Save Audio:**
   - The recorded audio is saved to a specified file using the [soundfile](https://pysoundfile.readthedocs.io/) library.

3. **Transcribe Audio:**
   - The recorded audio file is transcribed using the [Whisper ASR model](https://github.com/openai/whisper-api).

## Prerequisites

- Python 3.6 or higher
- Dependencies: See `requirements.txt`

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/alwaz-shahid/whisper-asr-cli.git
   cd whisper-asr-cli
