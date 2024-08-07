#!/usr/bin/env python3
import speech_recognition as sr
import subprocess
import time
from pynput import keyboard
import os

def execute_command(command):
    if "1" in command or "one" in command:
        ros_command = "rosrun bot polygon_publisher.py _room_coordinates_file:=~/catkin_ws/src/bot/config/building_coordinates_room.yaml"
    elif "2" in command or "two" in command:
        ros_command = "rosrun bot polygon_publisher.py _room_coordinates_file:=~/catkin_ws/src/bot/config/building_coordinates_room1.yaml"
    elif "3" in command or "three" in command:
        ros_command = "rosrun bot polygon_publisher.py _room_coordinates_file:=~/catkin_ws/src/bot/config/building_coordinates_room2.yaml"
    elif "4" in command or "four" in command:
        ros_command = "rosrun bot polygon_publisher.py _room_coordinates_file:=~/catkin_ws/src/bot/config/building_coordinates_room3.yaml"
    elif "5" in command or "five" in command:
        ros_command = "rosrun bot polygon_publisher.py _room_coordinates_file:=~/catkin_ws/src/bot/config/building_coordinates_room4.yaml"
    elif "full house" in command or "entire house" in command:
        ros_command = "rosrun bot polygon_publisher.py _room_coordinates_file:=~/catkin_ws/src/bot/config/building_coordinates_room6.yaml"   
    elif "base" in command or "charging point" in command:
        ros_command = "rosrun bot polygon_publisher.py _room_coordinates_file:=~/catkin_ws/src/bot/config/building_coordinates_room5.yaml"
    else:
        print("Unknown command")
        return False
    
    try:
        print(f"Executing: {ros_command}")
        subprocess.run(ros_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Press 'space' to start listening...")

        # Wait for the space key press
        wait_for_space_key()

        print("Listening...")
        audio = recognizer.listen(source)
        print("Audio captured, processing...")

    print("Recognizing speech...")
    try:
        command = recognizer.recognize_google(audio)
        print(f"Recognized command: {command}")
        
        if "1" in command or "one" in command:
            os.system(f'pico2wave -w=/tmp/output.wav "Cleaning room one" && aplay /tmp/output.wav')
        elif "2" in command or "two" in command:
            os.system(f'pico2wave -w=/tmp/output.wav "Cleaning room two" && aplay /tmp/output.wav')
        elif "3" in command or "three" in command:
            os.system(f'pico2wave -w=/tmp/output.wav "Cleaning room three" && aplay /tmp/output.wav')
        elif "4" in command or "four" in command:
            os.system(f'pico2wave -w=/tmp/output.wav "Cleaning room four" && aplay /tmp/output.wav')
        elif "5" in command or "five" in command:
            os.system(f'pico2wave -w=/tmp/output.wav "Cleaning room five" && aplay /tmp/output.wav')
        elif "full house" in command or "entire house" in command:
            os.system(f'pico2wave -w=/tmp/output.wav "Cleaning entire house" && aplay /tmp/output.wav')
        elif "base" in command or "charging point" in command:
            os.system(f'pico2wave -w=/tmp/output.wav "Returning to charging point" && aplay /tmp/output.wav')
        else:
            os.system(f'pico2wave -w=/tmp/output.wav "Unknown command" && aplay /tmp/output.wav')

        return command
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def wait_for_space_key():
    space_pressed = False

    def on_press(key):
        nonlocal space_pressed
        if key == keyboard.Key.space:
            space_pressed = True
            return False  # Stop listener

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    return space_pressed

if __name__ == "__main__":
    try:
        while True:
            command = recognize_speech_from_mic()
            if command is not None:
                execute_command(command)
            else:
                print("No command recognized")
            time.sleep(3)
    except AttributeError as e:
        print(f"Error with microphone or PyAudio: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
