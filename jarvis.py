import speech_recognition as sr
import subprocess
import time
import os
import pyttsx3
 # Initialize the pyttsx3 engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  
# def _speak(text):
#     print(f"Jarvis: {text}")
#     try:
#         engine.say(text)
#     except Exception as e:
#         print(f"[ERROR] Failed to speak. Reason: {e}")
#         engine.runAndWait()
def speak(text):
    print(f"Jarvis: {text}")
    try:
        command = f'edge-tts --voice "en-US-GuyNeural" --rate="+20%" --text "{text}" | mpg123 -q -'
        os.system(command)
    except Exception as e:
        print(f"[ERROR] Failed to speak. Reason: {e}")

def execute_welcome_back_routine():
    speak("Setting up your workspace now Sir.")

    try:
        # 1. Open the first window: Empty Brave browser
        print("Opening Brave Browser...")
        subprocess.Popen(["brave-browser", "--no-sandbox", "--new-window"])
        time.sleep(2)

        # 2. Open the second window: VS Code
        print("Opening VS Code...")
        # VS Code on Kali root needs both of these flags to launch
        subprocess.Popen(["code"]) 
        time.sleep(2)

        # 3. Open the third window: Brave with ChatGPT and YouTube Music tabs
        print("Opening ChatGPT and YouTube Music...")
        subprocess.Popen([
            "brave-browser", 
            "--no-sandbox",
            "--new-window", 
            "https://chatgpt.com", 
            "https://music.youtube.com"
        ])
        
        speak("Workspace is ready.")

    except FileNotFoundError as e:
        print(f"\n[ERROR] I couldn't find the application. Are you sure it's installed? Error: {e}")
        speak("Sir, I could not find one of the applications on your system.")
    except Exception as e:
        print(f"\n[ERROR] An error occurred: {e}")
        speak("I encountered an error while opening your applications, sir.")
        
# Opening you tube

def openYoutube():
    """The sequence of actions triggered by Open you tube'."""
    try:
        # 3. Open the third window: Brave with ChatGPT and YouTube Music tabs
        print("Opening YouTube ...")
        subprocess.Popen([
            "brave-browser", 
            "--no-sandbox",
            "https://youtube.com"
        ])
        

    except FileNotFoundError as e:
        print(f"\n[ERROR] I couldn't find the application. Are you sure it's installed? Error: {e}")
        speak("Sir, I could not find one of the applications on your system.")
    except Exception as e:
        print(f"\n[ERROR] An error occurred: {e}")
        speak("I encountered an error while opening your applications, sir.")
        
       
# Play music

def playMusic():
    """The sequence of actions triggered by Open you tube'."""
    try:
        # 3. Open the third window: Brave with play Music bandito
        print("play music...")
        subprocess.Popen([
            "brave-browser", 
            "--no-sandbox",
            "https://music.youtube.com/watch?v=ZB0amc1TZ3Y"
        ])
    except FileNotFoundError as e:
        print(f"\n[ERROR] I couldn't find the application. Are you sure it's installed? Error: {e}")
        speak("Sir, I could not find one of the applications on your system.")
    except Exception as e:
        print(f"\n[ERROR] An error occurred: {e}")
        speak("I encountered an error while opening your applications, sir.")
        
# open whatsapp

def openWhatsapp():
    """The sequence of actions triggered by Open you tube'."""
    try:
        # 3. Open the third window: Brave with play Music bandito
        print("Opening WhatsApp")
        subprocess.Popen([
            "brave-browser", 
            "--no-sandbox",
            "https://web.whatsapp.com/"
        ])
    except FileNotFoundError as e:
        print(f"\n[ERROR] I couldn't find the application. Are you sure it's installed? Error: {e}")
        speak("Sir, I could not find one of the applications on your system.")
    except Exception as e:
        print(f"\n[ERROR] An error occurred: {e}")
        speak("I encountered an error while opening your applications, sir.")

#opening telegram
def openTelegram():
    """The sequence of actions triggered by Open you tube'."""
    try:
        # 3. Open the third window: Brave with play Music bandito
        print("Opening Telegram")
        subprocess.Popen([
            "brave-browser", 
            "--no-sandbox",
            "https://web.telegram.org/a/"
        ])
    except FileNotFoundError as e:
        print(f"\n[ERROR] I couldn't find the application. Are you sure it's installed? Error: {e}")
        speak("Sir, I could not find one of the applications on your system.")
    except Exception as e:
        print(f"\n[ERROR] An error occurred: {e}")
        speak("I encountered an error while opening your applications, sir.")
      
# --- Main Loop ---
# ... (Keep your imports, speak(), execute_welcome_back_routine, etc. exactly the same up top) ...

if __name__ == "__main__":
    
    recognizer = sr.Recognizer()
    
    # Python opens the mic ONCE and holds onto it!
    with sr.Microphone(device_index=5) as source:
        
        print("\nCalibrating background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        speak("Jarvis is online. I am listening for your commands.")
        
        # The loop happens INSIDE the microphone block.
        # This forces Kali Linux to keep the microphone powered ON.
        while True:
            print("\nListening...")
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                user_command = recognizer.recognize_google(audio).lower()
                print(f"You said: '{user_command}'")
                
                # --- Command Processing ---
                if "workspace" in user_command or "set up" in user_command:
                    execute_welcome_back_routine()
                    
                elif "youtube" in user_command or "you tube" in user_command:
                    speak("Opening YouTube.")
                    openYoutube()
                elif "whatsapp" in user_command or "whatsapp" in user_command:
                    speak("Opening Whatsapp.")
                    openWhatsapp()
                elif "telegram" in user_command or "telegram" in user_command:
                    speak("Opening Telegram.")
                    openTelegram()
                elif "play music" in user_command:
                    speak("Starting Music.")
                    playMusic()
                elif "sleep" in user_command or "shut down" in user_command or "shutdown" in user_command:
                    speak("Powering down. Goodbye, sir.")
                    break # This breaks the loop, which safely closes the mic!
                    
            except sr.WaitTimeoutError:
                # If you don't speak, just loop back silently
                pass 
            except sr.UnknownValueError:
                # If it hears noise but no words, just loop back silently
                pass 
            except sr.RequestError:
                print("Network error. Cannot reach speech recognition service.")
