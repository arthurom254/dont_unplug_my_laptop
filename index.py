import psutil
import time
import pygame

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        time.sleep(1)  

def is_charging():
    battery = psutil.sensors_battery()
    if battery is not None:
        return battery.power_plugged
    return None

def main():
    last_status = is_charging()
    
    if last_status is None:
        print("Battery status not available.")
        return
    
    print("Monitoring charger status...")

    try:
        while True:
            current_status = is_charging()
            if current_status is not None and current_status != last_status:
                if current_status:
                    print("Charger plugged in.")
                else:
                    audio_file = "audio.mp3"  
                    play_audio(audio_file)
                last_status = current_status
            time.sleep(5)  
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()
