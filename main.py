import logging

import keyboard

from asr.asr_manager import ASR
from utils.audio_utils import save_audio

def print_menu():
    print("\n===== Whisper ASR CLI Menu =====")
    print("1. Record Audio")
    print("2. Set Recording Duration")
    print("3. Set Output File Path")
    print("4. Quit")

def main():
    try:
        logging.basicConfig(level=logging.INFO)
        asr = ASR()
        output_path = "output.wav"
        recording_duration = 30.0

        while True:
            print_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                try:
                    asr.record_audio(output_path, max_duration=recording_duration)
                except KeyboardInterrupt:
                    print("\nRecording interrupted. Press 'Ctrl+C' again to exit.")
                    try:
                        keyboard.wait("ctrl+c")
                    except KeyboardInterrupt:
                        print("\nExiting Whisper ASR CLI. Goodbye!")
                        break
            elif choice == "2":
                try:
                    recording_duration = float(input("Enter recording duration in seconds: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif choice == "3":
                output_path = input("Enter output file path: ")
            elif choice == "4":
                print("Exiting Whisper ASR CLI. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    except KeyboardInterrupt:
        print("\nQuitting Whisper ASR CLI. Goodbye!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
