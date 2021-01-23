import random
from art import logo, vs
from game_data import data

def random_acount():
  random_entry = random.choice(data)
  return random_entry


  print (random_entry["name"])

  print (random_entry["follower_count"])

def acount_data(acount):
  name = acount["name"]
  description = acount["description"]
  country = acount["country"]
  follow = acount["follower_count"]
  return f"{name}, a {description}, from {country}, {follow}"



#compare
def game():
  print(logo)
  count = 0
  a = random_acount()
  b = random_acount()

  should_continue = True

  while should_continue:
    a = b
    b = random_acount()

    while a == b:
      b = random_acount()

    print(f"Compare A: {acount_data(a)}.")
    print(vs)
    print(f"Against B: {acount_data(b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers_count = a["follower_count"]
    b_followers_count = b["follower_count"]

    if guess == "a":
      if a_followers_count > b_followers_count:
        count += 1
        print(f"You're right! Current score: {count}.")
      else:
        should_continue = False
    else:
      if b_followers_count > a_followers_count:
        count += 1
        print(f"You're right! Current score: {count}.")
      else:
        should_continue = False


game()

