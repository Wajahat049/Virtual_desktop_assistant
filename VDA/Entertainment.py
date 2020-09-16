import random
import requests
from bs4 import BeautifulSoup
import os
from VDA.Engine import StartUp


class Entertainment:  # COMPOSITION
    """It randomly tell a joke and can play music of different genre . """
    sp = StartUp()

    def TellJokes(self):  # It scrap a joke from a particular website
        jokes_url = "https://icanhazdadjoke.com/"
        page = requests.get(jokes_url)
        soup = BeautifulSoup(page.content, "html.parser")
        jokes = soup.find("p", {"class": "subtitle"})
        print(jokes.text)
        self.sp.Speak(jokes.text)
        return None

    @staticmethod
    def Play_NAAT():  # Play naat which is already saved in a folder in same directory
        lst_naat = ["NAAT\\naat1.mp3", "NAAT\\naat2.mp3", "NAAT\\naat3.mp3"]
        os.system(random.choice(lst_naat))

    @staticmethod
    def Play_National_song():  # Play National song which is already saved in a folder in same directory
        lst_Nationalsong = ["National_song\\n1.mp3", "National_song\\n2.mp3"]
        os.system(random.choice(lst_Nationalsong))

    @staticmethod
    def Play_POP():  # Play pop which is already saved in a folder in same directory
        lst_POP = ["POP\\pop1.mp3", "POP\\pop2.mp3", "POP\\pop3.mp3"]
        os.system(random.choice(lst_POP))

    @staticmethod
    def Play_Sufi():  # Play sufi which is already saved in a folder in same directory
        lst_sufi = ["SUFI\\sufi1.mp3", "SUFI\\sufi2.mp3", "SUFI\\sufi3.mp3"]
        os.system(random.choice(lst_sufi))