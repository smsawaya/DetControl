""""Contains text to speech functions to play audio alerts during testing"""

import pyttsx3

#FUNCTIONS------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def vacuum_audio_indicator():
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)

    engine.say("Vacuum pressure of 0.5 Pascals reached")
    engine.runAndWait()


# Main used for manual testing from this file.
def main():
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)

    engine.say("Vacuum pressure of 0.5 Pascals reached")
    engine.runAndWait()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")