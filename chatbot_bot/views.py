from django.shortcuts import render
import requests
import re
import random
from django.http import JsonResponse

def home(request):
    return render(request, 'chatbot_bot/html/index1.html')

def page(request):
    return render(request, 'chatbot_bot/html/page.html')

def input(request,input):
    print(input)
    chetbot_reply=get_response(input)
    print(chetbot_reply)
    return JsonResponse({'reply':chetbot_reply})

#imported long_responses.py
R_EATING = "I don't like eating anything because I'm a bot obviously!"

def unknown():
    response = ['Could you please re-phrase that?' ,
                '....',
                "Sorry i din't get it",
                'What does that mean?'][random.randrange(4)]
    return response


def messages_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    #Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty +=1

     #Calculate the percent of recognised words in a usee message
    percentage = float(message_certainty) / float(len(recognised_words))

    #Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0


def check_all_messages(message):

    highest_probe_list = {}

    # def major_responce(list_of_words):
    #     if major_responce('migraine'):
    #         return "migraines tend to be recurrent, and each attack may last up to 3 days.according to ayurveda if you are having migrane you can eat dairy products or sweets you will surely feel better.."

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_probe_list
        highest_probe_list[bot_response] = messages_probability(message, list_of_words, single_response, required_words)


    #Responses------------------------------------------------------------
    # greet
    response('Hello! How are you feeling today?',['hello','hi','hey','sup','heya'], single_response=True)
    # headache
    response("What kind of headache do you have :<br>    1. <b>Migraine headache</b> - Pain usually on one side of your head, but often on both sides.<br>     2.<b>Cluster headaches</b> - Cluster headaches include severe pain in or around one eye or on one side of your head they are characterized by severe burning and piercing pain.<br>     3.<b>Tension Headache</b> -  It is pain or discomfort in the head, scalp, or neck, and is often associated with muscle tightness in these areas.<br>     4.<b>Sinus headaches</b> - You may feel pressure around the eyes, cheeks and forehead", ['i','am','having','headache'], required_words=['headache'])

    response(' "<b>Migraines</b>" tend to be recurrent, and each attack may last up to 3 days.According to ayurveda if you are having migrane you can eat dairy products or sweets you will surely feel better..',['migraine'],single_response=True)
    response('Oxygen therapy is one of the main treatments.Getting extra oxygen into your bloodstream can calm your body and help you manage pain.According to ayurveda Camphor, jatasmansi, and sandalwood are also effective.',['cluster'],single_response=True)
    response('Apply heat to relieve tense neck and shoulder muscles. Use a heating pad set on low, a hot water bottle, a hot shower or bath, a warm compress, or a hot towel. Or apply ice or a cool washcloth to the forehead. Massage also can relieve muscle tension — and sometimes headache pain.According to ayurveda putting lukewarm salt water through Neti Pot in the nostrils may help clear clogged nose and relieve headache too.Apart from that, you can also eat half teaspoons of Sitopaladi powder with honey at least three times a day.',['tension'],single_response=True)
    response('Boil four glasses of water, add basil leaves, mint leaves, two cloves and a piece of ginger. Let it cool down and keep sipping this throughout the day or you can Grate a piece of ginger and take out its juice. Have this juice with honey two-four times a day.',['sinus'],single_response=True)



    response('Welcome, For proper diagnosis Please consult your nearest Medical Professional.',['thank','thank you'],single_response=True)

    # ERROR
    # if get_response("migraine"):
    #     return response('migraines tend to be recurrent, and each attack may last up to 3 days.according to ayurveda if you are having migrane you can eat dairy products or sweets you will surely feel better..')
    #
    # # elif get_response(".."):
    # #     return response('Migraines tend to be recurrent, and each attack may last up to 3 days.According to ayurveda if you are having migrane you can eat dairy products or sweets you will surely feel better..')
    #
    # else:





    response(R_EATING, ['what','you','eat'], required_words=['you','eat'])

    best_match = max(highest_probe_list, key=highest_probe_list.get)
    # print(highest_probe_list)

    return unknown() if highest_probe_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,:?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

#Testing the response system
print("Hello I'm a Healthcare BOT how can I help you")
