"""Creating a very simplified game of battleship using python"""

__author__ = "David Bottenberg"

import random

compChoice = random.randint(1, 4)
arr = [u'\U0001f7e9', u'\U0001f7e9', u'\U0001f7e9', u'\U0001f7e9']


def playerChoice():
  concat = ""
  val = input("choose a ship position (between 1-4): ")
  if val == "":
    print("you must make a choice")
    playerChoice()
  if int(val) > 4 or int(val) < 1:
    print("out of bounds")
    playerChoice()
  if int(val) == compChoice:
    hit = '\U0001f7e5'
    arr[int(val) - 1] = hit
    for elements in arr:
      concat += elements
    print(concat)
    print("Boom you hit their ship")
  elif int(val) != compChoice:
    print("You missed!")
    miss = '\U0001f7e6'
    arr[int(val) - 1] = miss
    for elements in arr:
      concat += elements
    print(concat)
    playerChoice()


playerChoice()