import pyttsx3

text= "Let’s recap what we’ve learned today. First, we started off with installing the Python module and the language pack for the language we desired.\
We moved on to learn some of the available functions provided by the module. We learned to set and get the property of the object as well as the text-to-speech \
function. Besides, we also tried outputting the available voices present in the operating system.\
Other than that, I also linked a few examples I’ve tested out on four different domains for three languages.\
Have fun testing it on your own, and hope you enjoyed this article. See you again in the next article."

engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)
engine.save_to_file(text, "output.mp3")

engine.say("Testing")
engine.say('Welcome to Medium')
engine.runAndWait()


