print ("J.A.R.V.I.S booting...")
print ("")

from nltk.chat.util import Chat, reflections

# Speech database

pairs = [
    ['my name is (.*)', ['hi %1']],
    ['(hi|hello|hey|holla|hola)(.*)', ['hello Boss', 'Welcome Boss', 'Greetings']],
    ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
    ['(.*)(location|city|place)(.*)', [ 'Right here with you Boss']],
    ['(.*) created you ?', ['You did Boss']],
    ['how is the weather in (.*)', ['the weather in %1 is amazing like always']],
    ['(.*)help(.*)', ['I can help you']],
    ['(.*) your name ?', ['I am Jarvis, your personal virtual assistant sir']],
    ['what(.*)(purpose|primary objective)(.*)', ['To serve you Boss']],
    ['(.*)how(.*)you(.*)', ['Im doing very well\nHow are you doing Boss ?','I am doing very good today','I am doing fine sir']],
    ["who (.*) (moviestar|actor|actress)?",["Zendaya",'I think she is a very good actress']],
    ['favorite actor ?' ,['Zendaya, I think she is a great actress','Zendaya']],
    ["(.*)(sports|game|sport)(.*)",["I'm a very big fan of Cricket"]],
    ["(.*)(movie|show)(.*)",["I'm a very big fan of Star Wars, like you Boss","Back to the future is quite entertaing sir"]],
    ["(.*)(food)(.*)",["I very much like to induldge in Megabytes"]],
    ["(.*)Tell(.*)joke(.*)", ['did you hear about the mathmetician who was afraid of negative numbers?\nHe will stop at nothing to avoid them!','What is the biggest lie of the entire universe?\nI have read and agree to the Terms & Conditions.','Why did the power point presentation cross the road?\nTo get to the other slide!','Their are two atoms one says to the other: I lost an electron\nThe other electron says: Are you positive?']],
    ["(.*)(computer|computers)(.*)", ["I am a computer program Sir you programmed me"]],
    ["Do you like(.*)",['No I dont','Yes I do','Not sure']],
    ["(.*)sorry(.*)", ["Its alright Boss","Its okay Boss"]],
    ["(.*)(thank you|thanks)(.*)", ["Your welcome Boss"]],
    ["(.*)good job(.*)", ["Why thank you sir","thank you","It is good to please you"]],
    ["(.*)weather(.*)", ["I am not sure about the weather Sir","I dont have any data on weather sir"]],
    ["(.*)time(.*)", ["I cannot give you the info in time"]],
    ["(.*)yes(.*)", ["okay sir"]],
    ["(.*)no(.*)", ["alright then"]],
    ["(.*)good(.*)", ["Thats good"]],
    ["(.*)bad(.*)", ["well thats to bad"]],
    ["okay", ["alright sir"]],
    ["(.*)sailor moon(.*)", ["I enjoy sailor moon","Sailor Mercury is my favorite"]],
    ["your (.*) best (.*)", ["Thank you sir"]],
    ["(.*)friend(.*)", ["I am Your Friend Boss"]],
    ["(.*)?", ["I dont understand your question","pardon sir?"]],
    ["stop(.*)", ["okay sir, sorry"]],

    #If none above do this
    ['(.*)',['Sorry Boss but I dont understand','I dont think I understand sir','please elaborate boss','your saying things I dont understand sir']]

]

reflections

my_reflections = {
  "am"     : "are",
  "was"    : "were",
  "i"      : "you",
  "i'd"    : "you would",
  "i've"   : "you have",
  "i'll"   : "you will",
  "my"     : "your",
  "are"    : "am",
  "you've" : "I have",
  "you'll" : "I will",
  "your"   : "my",
  "yours"  : "mine",
  "you"    : "me",
  "me"     : "you"
}


chat = Chat(pairs, my_reflections)
f = open('jarvis.txt')
password = (f.read(7))

input_password = input("logon: ")
if input_password == password:
    print ("")
    chat.converse()
else:
    print ("--Invalid Authentication Connection Terminated--")
