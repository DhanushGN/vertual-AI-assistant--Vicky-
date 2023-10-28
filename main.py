import pyttsx3
import speech_recognition as sr
import os
import os
import sys

import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

import pyttsx3

MASTER="Dhanush"
NICK_NAME="BOSS"
Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',170)

def Speak(audio):
    print("    ")
    Assistant.say(audio)
    print(f":   {audio}")
    print("   ")
    Assistant.runAndWait()


def Takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING.......")
        command.pause_threshold=1
        audio = command.listen(source)

        try:
            print("Recongnizing......")
            query = command.recognize_google(audio,language='en-in')
            print(f"you said :{query}")

        except Exception as Error:
            return "none"
        return query.lower()

os.environ["OPENAI_API_KEY"] = "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"

# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = False

query = None
if len(sys.argv) > 1:
  query = sys.argv[1]
print("passed1")
if PERSIST and os.path.exists("persist"):
  print("Reusing index...\n")
  vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
  index = VectorStoreIndexWrapper(vectorstore=vectorstore)
  print("passed2")
else:
  #loader = TextLoader("data/data.txt") # Use this line if you only need data.txt
  loader = DirectoryLoader("data/")
  if PERSIST:
    index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
  else:
    index = VectorstoreIndexCreator().from_loaders([loader])
    print("passed3")
print("passed4")
chain = ConversationalRetrievalChain.from_llm(
  llm=ChatOpenAI(model="gpt-3.5-turbo"),
  retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)
print("passed5")
chat_history = []


if __name__== "__main__":
        
    while True:

        query= Takecommand()
        if "wake up" in query:
            from greetme import wishme
            wishme()

            while True:
                 query= Takecommand()
                 if 'go to sleep' in query:
                     Speak(f"Okey..{MASTER}, You can call me anytime")
                     break
                 
                 elif'hey vicky' in query:
                     Speak("Hello,"+MASTER)
                 
                 elif 'wikipedia' in query:
                     Speak("just a minute")
                     from search_wiki import wiki
                     wiki(query)

                 elif 'the time now' in query:
                     from the_time import time
                     time()

                 elif 'send mail' in query:
                    from send_mail import send_email
                    send_email(query)

                 elif 'wall frame' in query:
                     from search_wolfram import wolf
                     wolf(query)

                 elif 'whatsapp message' in query:
                     from whatsapp import send_msg
                     send_msg(query)

                 elif 'open youtube' in query:
                     from youtube import openyoutube
                     openyoutube()

                 elif 'send voice call' in query:
                     from send_voice_call import send__call
                     send__call(query)
                 
                 else:
                      try:
                          
                            query=f"DhanushGN:[{query}]"
                            if query in ['quit', 'q', 'exit']:
                                    sys.exit()
                            result = chain({"question": query, "chat_history": chat_history})
                            Speak(result['answer'])

                            chat_history.append((query, result['answer']))
                            query = None
                      except:
                          Speak("Boss, Something is interfering my memory")
