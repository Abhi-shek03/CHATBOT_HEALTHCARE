from django.shortcuts import render
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

    response('"Migraines" tend to be recurrent, and each attack may last up to 3 days.According to ayurveda if you are having migrane you can eat dairy products or sweets you will surely feel better.<br><b>what else can i help you with?</b>',['migraine'],single_response=True)
    response('Oxygen therapy is one of the main treatments.Getting extra oxygen into your bloodstream can calm your body and help you manage pain.According to ayurveda Camphor, jatasmansi, and sandalwood are also effective. <br><b>what else can i help you with?</b>',['cluster'],single_response=True)
    response('Apply heat to relieve tense neck and shoulder muscles. Use a heating pad set on low, a hot water bottle, a hot shower or bath, a warm compress, or a hot towel. Or apply ice or a cool washcloth to the forehead. Massage also can relieve muscle tension — and sometimes headache pain.According to ayurveda putting lukewarm salt water through Neti Pot in the nostrils may help clear clogged nose and relieve headache too.Apart from that, you can also eat half teaspoons of Sitopaladi powder with honey at least three times a day. <br><b>what else can i help you with?</b>',['tension'],single_response=True)
    response('Boil four glasses of water, add basil leaves, mint leaves, two cloves and a piece of ginger. Let it cool down and keep sipping this throughout the day or you can Grate a piece of ginger and take out its juice. Have this juice with honey two-four times a day. <br><b>what else can i help you with?</b>',['sinus'],single_response=True)
    
      #stomachache 
    response("What kind of stomachache do you have:<br>  1.<b>Indigestion </b>:A burning sensation or discomfort in the upper abdomen, often after eating feeling full or bloated after eating<br>  2.<b>Gastritis</b>:Gastritis refers to inflammation of the stomach lining. Symptoms include stomach pain, nausea, vomiting, and bloating.<br>   3.<b>Peptic Ulcers</b>: Peptic ulcers are sores that develop in the lining of the stomach or the duodenum (the first part of the small intestine). Symptoms include stomach pain, nausea, vomiting, and bloating.<br> 4.<b>Gastroenteritis</b>: This type of stomach ache is caused by a viral or bacterial infection in the digestive system. Symptoms include stomach pain, diarrhea, vomiting, and fever.<br> 5.<b>Irritable Bowel Syndrome (IBS)</b>: IBS is a common digestive disorder that can cause stomach pain, bloating, constipation, and diarrhea.<br>  6.<b>Food Allergies </b>: Certain foods or ingredients may cause stomach pain, bloating, or diarrhea in people who have allergies or intolerances to them. <br> 7.<b>Inflammatory Bowel Disease (IBD)</b>: IBD is a chronic condition that causes inflammation in the digestive tract. Symptoms include abdominal pain, diarrhea, and rectal bleeding.<br>",['i','am','having','stomachache'], required_words=['stomachache'])
    #remedies

    response('<b>There are several Home remedies that can be used to treat Indigestion at home.Here are some suggestions</b>:<br>1.<b>Ginger</b>: Ginger is a natural digestive aid and can help alleviate indigestion symptoms. You can add fresh ginger to your meals, drink ginger tea, or chew on a piece of ginger root.</br> 2.<b>Turmeric</b>: Turmeric has anti-inflammatory properties and can help reduce inflammation in the digestive system. You can add turmeric powder to your meals or drink turmeric milk.<br> 3.<b>Fennel Seeds</b>: Fennel seeds can help improve digestion and reduce bloating. You can chew on fennel seeds after meals or drink fennel tea.<br><br> <b>what else can i help you with?</b>',['indigestion','Indigestion'],single_response=True)
    response('<b>Here are some Home remedies for gastritis</b>: <br> <b>1.Coconut Water</b>: Coconut water can help soothe the stomach lining and reduce inflammation. Drink coconut water regularly to alleviate gastritis symptoms.<br> <b>2.Aloe Vera</b>: Aloe vera has anti-inflammatory properties and can help soothe the stomach lining. Drink aloe vera juice or take it in supplement form.<br> <b>3.Chamomile Tea</b>: Chamomile tea can help reduce inflammation and alleviate gastritis symptoms. Drink chamomile tea regularly to help soothe the stomach lining.<br><br> <b>what else can i help you with?</b>',['gastritis','Gastritis'],single_response=True)
    response('<b>Here are some Home remedies for peptic ulcer</b>:<br> <b>1.Licorice Root</b>: Licorice root has anti-inflammatory properties and can help reduce inflammation in the stomach lining. It can also help protect the stomach lining from the damaging effects of stomach acid. You can drink licorice root tea or take it in supplement form.<br> <b>2.Amla</b>: Amla, also known as Indian gooseberry, is rich in vitamin C and has anti-inflammatory properties. It can help reduce inflammation and protect the stomach lining from the damaging effects of stomach acid. You can eat fresh amla or take it in supplement form. <br> <b>3.Coconut Water</b>: Coconut water can help soothe the stomach lining and reduce inflammation. Drink coconut water regularly to help alleviate peptic ulcer symptoms.<br> <b>4.Turmeric</b>: Turmeric has anti-inflammatory properties and can help reduce inflammation in the stomach lining. Add turmeric powder to your meals or drink turmeric milk.<br> <b>5.Coriander Seeds</b>: Coriander seeds can help improve digestion and reduce inflammation. You can chew on coriander seeds after meals or drink coriander tea.<br> <b>6.Triphala</b>: Triphala is an Ayurvedic herbal formula that can help improve digestion and reduce inflammation. You can take it in capsule form or mix it with water and drink it.<br><br> <b>what else can i help you with?</b>',['ulcer','Ulcer','Ulcers','ulcers'],single_response=True)
    response('<b>Here are some Home remedies for gastroenteritis</b>:<br> <b>1.Ginger</b>: Ginger has anti-inflammatory and antibacterial properties that can help alleviate gastroenteritis symptoms. You can add fresh ginger to your meals, drink ginger tea, or chew on a piece of ginger root.<br> <b>2.Cumin Seeds</b>: Cumin seeds can help improve digestion and reduce inflammation. You can chew on cumin seeds after meals or drink cumin tea.<br><b>Fennel Seeds</b>: Fennel seeds can help alleviate digestive symptoms such as bloating, gas, and abdominal pain. You can chew on fennel seeds after meals or drink fennel tea. <br><b>4.Coconut Water</b>: Coconut water can help replenish electrolytes lost due to diarrhea and vomiting, and can also help soothe the stomach lining. Drink coconut water regularly to help alleviate gastroenteritis symptoms.<br><b>5.Coriander Seeds</b>: Coriander seeds can help improve digestion and reduce inflammation. You can boil coriander seeds in water and drink the resulting tea.<br><b>6.Triphala</b>: Triphala is an Ayurvedic herbal formula that can help improve digestion and reduce inflammation. You can take it in capsule form or mix it with water and drink it.<br><br> <b>what else can i help you with?</b>',['gastroenteritis','Gastroenteritis'],single_response=True)
    response('<b>Here are some Home remedies for Irritable Bowel Syndrome (IBS)</b>:<br> <b>1.Triphala</b>: A combination of three fruits, Triphala is a popular Ayurvedic remedy that is known to improve digestion and relieve constipation. It can be taken in powder form, mixed with water, or as a supplement.<br> <b>2.Licorice</b>: Licorice is known to soothe the digestive tract and reduce inflammation. It can be taken in the form of tea, capsule, or extract.<br><b>2.Aloe Vera</b>: Aloe Vera is known to have a cooling effect on the body and can help relieve inflammation in the digestive tract. It can be taken in the form of juice or gel. <br><b>3.Ginger</b>: Ginger is a natural anti-inflammatory and can help relieve nausea and stomach discomfort. It can be taken in the form of tea or added to food. <br><b>5.Fennel</b>: Fennel seeds are known to relieve gas and bloating and can be taken in the form of tea or added to food.',['IBS','ibs','irritable','Irritable','Bowel','bowel','Syndrome','syndrome'],single_response=True)
    response('<b>Here are some home remedies for mild food allergy symptoms</b>:<br><b>1.Apple Cider Vinegar</b>: Apple cider vinegar has anti-inflammatory properties and can help alleviate itching and swelling. Mix one tablespoon of apple cider vinegar with a glass of water and drink it.<br><b>2.Aloe Vera</b>: Aloe vera has soothing and anti-inflammatory properties and can help alleviate itching and rash. Apply aloe vera gel to the affected area.<br><b>Baking Soda</b>: Baking soda can help reduce itching and swelling. Mix one teaspoon of baking soda with water to form a paste and apply it to the affected area.<br><b>3.Turmeric</b>: Turmeric has anti-inflammatory properties and can help alleviate itching and swelling. Mix turmeric powder with water to form a paste and apply it to the affected area.<br><b>4.Chamomile Tea</b>: Chamomile tea has anti-inflammatory and anti-allergenic properties and can help alleviate itching and swelling. Drink chamomile tea or apply a chamomile tea bag to the affected area.<br><b>5.Honey</b>: Honey has anti-inflammatory and anti-bacterial properties and can help alleviate itching and swelling. Apply honey to the affected area.<br><br> <b>what else can i help you with?</b>',['Food','Allergies','food','allergies'],single_response=True)
    response('<b>Here are some home remedies for Inflammatory Bowel Disease (IBD):</b><br> <b>1.Probiotics</b>: Probiotics are beneficial bacteria that can help improve gut health and reduce inflammation. You can take probiotic supplements or eat foods that are rich in probiotics, such as yogurt, kefir, sauerkraut, and kimchi.<br><b>2.Turmeric</b>: Turmeric has anti-inflammatory properties and can help reduce inflammation in the gut. You can add turmeric to your meals or take it in supplement form.<br><b>2.Fish Oil</b>: Fish oil supplements can help reduce inflammation in the gut and improve symptoms of IBD. You can take fish oil supplements or eat fatty fish, such as salmon, mackerel, and sardines.<br><b>3.Aloe Vera</b>: Aloe vera has anti-inflammatory and healing properties and can help soothe the gut lining. Drink aloe vera juice or take aloe vera supplements.<br><b>4.Exercise</b>: Exercise can help reduce inflammation and improve overall health. Aim for at least 30 minutes of moderate exercise, such as brisk walking or cycling, on most days of the week.<br><b>5.Stress Reduction</b>: Stress can exacerbate IBD symptoms, so it is important to manage stress through relaxation techniques, such as meditation, yoga, or deep breathing exercises.<br><br> <b>what else can i help you with?</b>',['IBD','ibd','Bowel','bowel'],single_response=True)
    
    #proresponse
    response('<b>Constant vomiting can be a symptom of several medical conditions, including</b>:<br><br><b>1.Gastrointestinal infections</b>: Viral or bacterial infections in the gastrointestinal tract can cause nausea and vomiting.<br><b>2.Food poisoning</b>: Consuming contaminated food or drink can lead to nausea, vomiting, and other gastrointestinal symptoms.<br><b>3.Migraines</b>: Some people experience vomiting as a symptom of a migraine headache.<br><b>4.Motion sickness</b>: Vomiting can be a symptom of motion sickness, which is caused by a disturbance in the inner ear.<br><b>5.Medications</b>: Certain medications can cause nausea and vomiting as a side effect.<br><b>6.Pregnancy</b>: Morning sickness, which is nausea and vomiting during pregnancy, is a common symptom in the first trimester.<br><b>7.Gallbladder disease</b>: Vomiting can be a symptom of gallbladder disease, which is caused by inflammation or blockage of the gallbladder.<br><b>8.Pancreatitis</b>: Inflammation of the pancreas can cause nausea and vomiting, as well as other gastrointestinal symptoms.<br><br><b>If you are experiencing constant vomiting, it is important to speak with a healthcare professional to determine the underlying cause and receive appropriate treatment</b>.',['Vomiting','vomiting','Vomit','vomit'],single_response=True)
   
    #friendlyresponse
    response('<b>I am sorry to hear that you are feeling stressed.Stress is a common issue that many people face, and it can have negative effects on both physical and mental health:) <br> Here are some tips that may help you manage your stress:</b><br><br> <b>1.Deep breathing exercises</b>: Take a few deep breaths, inhaling slowly through your nose and exhaling slowly through your mouth. Repeat several times until you feel more relaxed.<br><b>2.Exercise</b>: Physical activity can help reduce stress and improve mood. Try going for a walk, jog, or doing some yoga or stretching exercises.<br><b>3.Mindfulness meditation</b>: This practice involves focusing on the present moment and being aware of your thoughts and feelings without judgment. There are many apps and resources available to guide you through mindfulness meditation.<br><b>Talk to someone</b>: Sometimes talking to a friend, family member, or mental health professional can help you gain perspective and find solutions to your stressors.<br><b>Relaxation techniques</b>: Activities such as taking a warm bath, listening to calming music, or practicing progressive muscle relaxation can help reduce stress.<br><br><b>Remember, it is important to take care of yourself and prioritize your well-being. If your stress levels persist or interfere with your daily life, it may be helpful to seek professional support.</b>',['i','am','feeling','stressed'],required_words=['stressed'])
    response('<b>I am sorry, I am not authorized to prescribe medications. However, I can tell suggest you home remedies that you can follow to reduce your problem . It is important to talk to your doctor before starting or stopping any medications</b>',['medicine','medication','Medicine','Medication'],single_response=True)
    response('<b>I am sorry to hear that you are feeling depressed.Here are somethings you can do <br><br></b> 1.Talk to your family and friends.<br> 2.Think about th positive aspects of your life<br> 3.Get enough sleep and encourage in activities that you enjoy <br><br><b>Remember that everyones experience with depression is unique, and what works for one person may not work for another.Work with your mental health professional to develop a treatment plan that is tailored to your needs.',['depressed','Depressed','depression','Depression'],single_response=True)
    response('Welcome, For proper diagnosis Please consult your nearest Medical Professional.',['thanks','thankyou'],single_response=True)

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