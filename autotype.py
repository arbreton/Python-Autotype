from pynput.keyboard import Key, Controller
import random
import time


keyboard = Controller()

time.sleep(2)

for char in "A girl, in the Vacococha tribe of Peru, to prepare her for marriage at the age of 12, is placed in a basket in the hut of her prospective in-laws and must remain suspended over an open fire night and day for 3 months. The Spanish Inquisition once condemned the entire Netherlands to death for heresy. During the eighteenth century, books that were considered offensive were sometimes punished by being whipped.":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(random.uniform(0.05642,0.05644))
