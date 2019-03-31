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
imputcorrector = True
while (imputcorrector):
    os.system("say 'Would you like to play a game?' ")
    print('Would you like to play a game?')
    if use_audio_input: 
        wanttoplay = recognize_speech()
    else:
        wanttoplay = input("""Would you like to play a game?\n""")
    if not wanttoplay:
        wanttoplay = input("""Would you like to play a game?\n""")
    if (wanttoplay == "yes" or wanttoplay == "no"):
        imputcorrector = False
    else:
        os.system("""say "I'm sorry I cannot understand you. Can you please type in yes or no?" """)
        print ("I'm sorry I cannot understand you. Can you please type in yes or no?\n")
    if (wanttoplay == "no"):
        os.system("say 'So sad to see you go. Come back another time!' ")
        print ("So sad to see you go. Come back another time!")
        exit()
    else:
        if (wanttoplay == "yes"):
            os.system("say 'Great!' ")
            print ("Great!")
            imputcorrector2 = True
            while (imputcorrector2):
                os.system("say 'Do you know how to play Atlas?' ")
                print ("Do you know how to play Atlas?")
                if use_audio_input:
                    howtoplay = recognize_speech()
                else:
                    howtoplay = input("""Do you know how to play Atlas?\n""")
                if not howtoplay:
                    howtoplay = input("""Do you know how to play Atlas?\n""")
                if (howtoplay == "yes" or howtoplay == "no"):
                    imputcorrector2 = False
                else:
                    os.system("say 'I'm sorry I cannot understand you. Can you please type in yes or no?' ")
                    print("I'm sorry I cannot understand you. Can you please type in yes or no?\n")
                if (howtoplay == "no"):
                    print ("Well this is how you play: \nFirst, we start with any country. Let's say America. Since America ends with the letter A, you have to say a country starting with the letter A. Then I will say a country starting with the last letter of the place you said. I know, it is a little confusing. Let's try it! Make sure you spell them correctly and remember, NO REPEATS! Let's begin!")
                    os.system("""say "This is how you play: First, we start with any country. Let's say America. Since America ends with the letter A, you have to say a country starting with A. Then I will say a country starting with the last letter of the place you said. I know, it is a little confusing. Let's try it! Make sure you spell them correctly and remember, NO REPEATS! Let's begin! " """)
                    print ("")
                    gaming = True
                    from random import choice
                    countries = open("countrieslist.txt","r")
                    countries_list = [country.lower() for country in countries.read().split("\n")]
                    final_choice = choice(countries_list)
                    player_previous = []
                    while (gaming):
                        player_input = input(final_choice + "\n")
                        if player_input in player_previous:
                            os.system("say 'Hey! You used the same country twice! You lose! Game over!!' ")
                            print ("Hey! You used the same country twice! You lose! Game over!")
                            exit()
                        player_previous.append(player_input)
                        if (player_input[0].lower() == final_choice[-1]):
                            if player_input.lower() in countries_list:
                                os.system("say 'Good Job!' ")
                                print ("Good job!")
                                user_final_letter = player_input[-1]
                                vaild_computer = []
                                for country in countries_list:
                                    if country[0] == user_final_letter:
                                        vaild_computer.append(country)
                                final_choice = choice(vaild_computer)
                                player_previous.append(final_choice)
                            else:
                                gaming = False
                        else:
                            gaming = False
                    os.system("""say "Incorrect that's not a country! You lose! Game over!" """)
                    print ("Incorrect that's not a country! You lose! Game over!")
                    exit()
                if (howtoplay == "yes"):
                    print ("Excellent! Today we will be playing the game using only countries. Make sure you spell them correctly! Let's begin!")
                    os.system("""say "Excellent! Today we will be playing the game using only countries. Make sure you spell them correctly and remember, NO REPEATS. Let's begin!" """)
                    print ("")
                    gaming = True
                    from random import choice
                    countries = open("countrieslist.txt","r")
                    countries_list = [country.lower() for country in countries.read().split("\n")]
                    final_choice = choice(countries_list)
                    player_previous = []
                    while (gaming):
                        player_input = input(final_choice + "\n")
                        if player_input in player_previous:
                            os.system("say 'Hey! You used the same country twice! You lose! Game over!!' ")
                            print ("Hey! You used the same country twice! You lose! Game over!")
                            exit()
                        player_previous.append(player_input)
                        if (player_input[0].lower() == final_choice[-1]):
                            if player_input.lower() in countries_list:
                                os.system("say 'Good Job!' ")
                                print ("Good job!")
                                user_final_letter = player_input[-1]
                                vaild_computer = []
                                for country in countries_list:
                                    if country[0] == user_final_letter:
                                        vaild_computer.append(country)
                                final_choice = choice(vaild_computer)
                                player_previous.append(final_choice)
                            else:
                                gaming = False
                        else:
                            gaming = False
                    print ("Incorrect that's not a country! You lose! Game over!")
                    os.system("say 'Incorrect that's not a country! You lose! Game over!' ")
                    exit()
