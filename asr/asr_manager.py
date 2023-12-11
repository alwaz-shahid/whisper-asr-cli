# whisper_asr_cli/asr/asr.py
import logging
import asyncio
import keyboard
import sounddevice as sd
import torchaudio
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from utils.audio_utils import save_audio

class ASR:
    def __init__(self):
        self.processor = WhisperProcessor.from_pretrained("openai/whisper-base")
        self.model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-base")
        self.model.config.forced_decoder_ids = None

    async def transcribe_audio(self, audio_path):
        try:
            logging.info("Transcribing audio...")
            waveform, sample_rate = torchaudio.load(audio_path)
            input_features = self.processor(waveform.numpy(), sampling_rate=sample_rate, return_tensors="pt").input_features
            predicted_ids = self.model.generate(input_features)
            transcription = self.processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
            logging.info("Audio transcription completed.")
            return transcription
        except Exception as e:
            logging.error(f"Error during transcription: {str(e)}")
            raise

    def record_audio(self, output_path, max_duration=30.0, sample_rate=16000):
        try:
            logging.info("Press 'R' to start recording. Press 'S' to stop recording. Press 'Q' to quit.")
            keyboard.wait("r")  # Wait for 'R' key press to start recording

            logging.info("Recording audio...")

            frames_to_record = int(sample_rate * max_duration)
            audio_data = sd.rec(frames_to_record, samplerate=sample_rate, channels=1, dtype='int16')

            logging.info("Press 'S' to stop recording. Press 'Q' to quit.")
            while True:
                if keyboard.is_pressed("s"):
                    break
                if keyboard.is_pressed("q"):
                    logging.info("Quitting Whisper ASR CLI. Goodbye!")
                    sd.stop()
                    return

            sd.stop()
            logging.info("Recording completed.")

            save_audio(output_path, audio_data, sample_rate)
            logging.info(f"Audio saved to: {output_path}")

            transcription = asyncio.run(self.transcribe_audio(output_path))
            print(f"Transcription: {transcription}")
        except Exception as e:
            logging.error(f"Error during recording: {str(e)}")
            raise
