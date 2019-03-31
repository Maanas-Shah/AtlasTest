import os 
import speech_recognition as sr

use_audio_input = True

recognizer = sr.Recognizer()



def recognize_speech():
    # Record Audio

    with sr.Microphone() as source:
        print("Say something!")
        audio = recognizer.listen(source, phrase_time_limit=3)#, retry=None, timeout=3)

    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        recognized_text = recognizer.recognize_google(audio)#, retry=None, timeout=3)
        print("You said: " + recognized_text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        recognized_text = ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        recognized_text = ""
    except:
        recognized_text = ""

    return recognized_text

#Introduction Code
os.system("say 'Would you like to play a little game?' ")
print('Would you like to play a little game?')
if use_audio_input: True
  wanttoplay = recognize_speech()
else:
    wanttoplay = input("""Would you like to play a little game?\n""")
if not wanttoplay:
    wanttoplay = input("""Would you like to play a little game?\n""")
if (wanttoplay == "no"):
    os.system("say 'So sad to see you go. Come back another time!' ")
    print ("So sad to see you go. Come back another time!")
    exit()
else:
    if (wanttoplay == "yes"):
        os.system("say 'Great!' ")
        print ("Great!")
        os.system("say 'Do you know how to play Atlas?' ")
        if use_audio_input: True
            howtoplay = recognize_speech()
        else:
            howtoplay = input("""Do you know how to play Atlas?\n""")
        if not howtoplay:
            howtoplay = input("""Do you know how to play Atlas?\n""")
        #Gameplay Code if they don't know how to play
        if (howtoplay == "no"):
            os.system("""say "This is how you play: First, we start with any country. Let's say America. Since America ends with the letter A, you have to say a country starting with A. Then I will say a country starting with the last letter of the place you said. I know, it is a little confusing. Let's try it! I'll start!" """)
            print("This is how you play: First, we start with any country. Let's say America. Since America ends with the letter A, you have to say a country starting with A. Then I will say a country starting with the last letter of the place you said. I know, it is a little confusing. Let's try it! I'll start!") 
            print("")
            from random import choice
            countries = open("countrieslist.txt", "r")
            countries_list = countries.read().split("\n")
            final_choice = choice(countries_list)
            country_imput = input(final_choice)
            print (final_choice) 
        #Gameplay Code if they do know how to play
        if (howtoplay == "yes"):
            os.system("say 'Excellent! Today we will be playing the game using only countries. Let us begin! I can start!' ")
            print ("Excellent! Today we will be playing the game using only countries. Let's begin! I'll start!") 
            print("")
            from random import choice
            countries = open("countrieslist.txt", "r")
            countries_list = countries.read().split("\n")
            final_choice = choice(countries_list)
            country_imput = input(final_choice)
            print (final_choice) 
        else:
            os.system("say 'I'm sorry I cannot understand you. Can you please restart and type in yes or no next time?' ")
            print ("I'm sorry I cannot understand you. Can you please restart and type in yes or no next time?")
            quit()

    else:
        print ("I'm sorry I cannot understand you. Can you please restart and type in yes or no next time?")
        quit()

      
      
 