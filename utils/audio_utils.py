# whisper_asr_cli/utils/audio_utils.py
import soundfile

def save_audio(output_path, audio_data, sample_rate):
    soundfile.write(output_path, audio_data, samplerate=sample_rate)
