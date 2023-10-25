import os


def list_speakers():
    # This work if you know the name of the devices (There is other ways to get all devices, Google is your friend :P)
    return [
        "Headset HyperX",
        "Haut-parleurs Enceintes",
    ]


def select_speaker_device():
    speakers = list_speakers()

    print("Available speaker devices:")
    for i, speaker in enumerate(speakers):
        print(f"{i}. {speaker}")

    try:
        choice = int(input("\nEnter the number of the speaker device you want to switch to: "))
        device = speakers[choice]
        # See: https://www.nirsoft.net/utils/nircmd.html
        os.system(f'F:\\___PROJECTS___\\PyCharm\\SpeakerSwitcher\\nircmd.exe setdefaultsounddevice "{device}"')
        print(f"Device changed to {device}")
    except (ValueError, IndexError):
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    select_speaker_device()
