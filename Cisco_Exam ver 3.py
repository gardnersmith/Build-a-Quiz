'''This is a Cisco exam based on the the base code (madlibs generator) for the IPND course at UDACITY
'''
easy_exam = "This exam will test your basic knowledge about Cisco routing.\n______________________________________________________________\nGood Luck!\n\n___1___ protocol has 2 version open source\n distance vector based protocol.\n\n___2___ is a cisco proprietary protocol that is also considered to be distance vector.\n\nAn example of an open source link state protocol is ___3___ while ___4___ is considered to be Cisco's competing protocol which is propeitary."
answer_easy = ["RIP", "IGRP", "OSPF", "EIGRP"]

medium_exam = "This exam will test your knowledge about Cisco routers Hareware components.\n______________________________________________________________\nGood Luck!\n\nLike a computer, the cisco router has the following hardware components.\n\nThe Startup-configuration is stored in ___1___.\n\nThe Cisco operating System IOS is located on the routers ___2___.\n\nThe running configuration is stored in ___3___.\n\nIf the router cannot boot the IOS, it will default boot to ___4___ monitor mode."
answer_medium = ["NVRAM", "FLASH", "RAM", "ROM"]

hard_exam = "This exam is the more difficult exam, and will test your knowledge about BGP routing.\n______________________________________________________________\nGood Luck!\n\nIf a bgp peer is reachable, and is an internal peer, the first rule to assist in best path\n through the network is to determine the ___1___/PREFERENCE attribute.\n\nThe next tie breaker is the attribute known as the ___2___/PATH.\n\nThe 3rd tie breaker is the lowest value of their ___3___ attribute.\n\nNext tie breaker is the prefer routes with the lowest MULTI-___4___-DISC value.\n\nThere are other options as BGP is a very flexible open source routing protocol.\n\nYou can find more about BGP by follwing this link \n\nhttps://en.wikipedia.org/wiki/Border_Gateway_Protocol#Route_selection\n"
answer_hard = ["LOCAL", "AS", "WEIGHT", "EXIT"]

answers = ["___1___", "___2___", "___3___", "___4___"]

def answer_check(response,correct_answer):
    '''This procedure is to check the answer given against the correct answer key in answer_(easy,medium,hard)'''
    if response == correct_answer:
        return True
    else:
        return False

def choose_level():
    '''This procedure is to use the correct exam based on the user's input'''
    print "This exam will test your knowledge of networking in a Cisco environment.\n\nEach question will must be answered correctly within 3 tries.\n"
    level = raw_input("To make your choice of difficulty level:\nplease type easy, medium, or hard:\n").lower()
    if level == "easy":
        print "OK, you have chosen the easy exam.\n"
        return play_game(easy_exam, answer_easy, answers)
    if level == "medium":
        print "OK, you have chosen the medium exam.\n"
        return play_game(medium_exam, answer_medium, answers)
    if level == "hard":
        print "OK, you have chosen the hard exam.\n"
        return play_game(hard_exam, answer_hard, answers)
    else:
        return choose_level()

def play_game(exam_question, correct_answer, question):
    '''This procedure is the actual code for the game routine'''
    count = 0
    attempt = 1
    max_attempts = 3
    for fill_in_the_blank in question:
        while count < len(question) and attempt <= max_attempts:
            print exam_question
            answer = raw_input("****What is the correct answer for fill in the blank" + str(count +1) + '?***\n').upper()
            '''upper is used to convert the users raw_input into upper case'''
            if answer_check(answer, correct_answer[count]) == True :
                print "That is the correct answer!\n"
                exam_question = exam_question.replace(question[count], answer)
                '''This makes the exam question print using the user's correct answer'''
                count += 1
            else:
                print "Your answer was not correct.\n\n\n*****You may try again but this is was attempt number*****" + str(attempt)
                attempt += 1
        if count == len(question):
            print "You passed the test!\n"
            '''I used the raw_input to create a pause for the user to see the feedback on the screen when they pass or fail'''
        if attempt > max_attempts:
            print "This was your last attempt.  A good place to start learning more about Cisco Networking is by browsing to www.netacad.com.\nAfter that, come back and try again!  :)\n"
            '''I used the raw_input to create a pause for the user to see the feedback on the screen when they pass or fail'''
choose_level()
