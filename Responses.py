from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi","sup","hii"):
        return "Hey! How's it going"

    if user_message in ("who are you","Who are you?",):
        return "I'm Garullus Bot!"

    if user_message in ("how are you",):
        return "I am Great.What about you"

    if user_message in ("Who created you","who created you",):
        return "Alok Shakya, Amit Sharma and Akshat Thakur Created me!"

    if user_message in ("What Garullus means", "why your name is Garullus", "why your name is garullus ","Meaning of Garullus","meaning of garullus"):
        return "It is latin word of Chatterbox"

    if user_message in ("time","time?",):
        now  = datetime.now()
        date_time = now.strftime("%d/%m/%y,%H:%M:%S")

        return str(date_time)

    return "I dont'understand you."