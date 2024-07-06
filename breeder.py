import random

class Gecko:
  def __init__(self, name, sex, morph, can_breed = False, 
  is_hungry = True):
    self.name = name
    self.sex = sex
    self.morph = morph
    self.can_breed = can_breed
    self.is_hungry = is_hungry
    gecko_collection.append(self)
    player_1.add_xp()

  def __repr__(self):
    description = "{name} is a {sex} gecko and has the {morph} morphotype.".format(name = self.name, sex = self.sex, morph = self.morph)
    if self.can_breed:
      description += " It is ready to breed now."
    else:
      description += " It is not ready to breed yet."
    if self.is_hungry:
      description += " It is hungry and needs to be fed."
    else:
      description += " It's not hungry right now."
    return description

gecko_collection = []

sex = ["male", "female"]

names = "Max Bella Charlie Lucy Daisy Buddy Molly Rocky Bailey Sadie Cooper Chloe Jack Maggie Sophie Tucker Lola Duke Lily Oliver Zephyr Nimbus Cosmo Seraphina Apollo Juno Solstice Orion Echo Lyra Blaze Aurora Zenith Luna Phoenix Sable Amethyst Nova Zen Pixel Ember Orion Lyric Onyx Vega Nebula Comet Celeste Stardust Draco"

names_list = names.split(" ")

all_morph_list = ["diablo", "super red", "green galaxy", "blue headed", "granite", "leusistic", "platinum", "albino", "acid", "normal","reduced pattern", "powder blue", "patternless", "piebald", "candy dot",  "caramel", "striped", "zigzag"]

exotic_morph_list = ["diablo", "super red", "green galaxy", "blue headed", "granite", "leusistic", "platinum", "albino", "acid"]

exotic_morph_xp = []

for i in range(len(exotic_morph_list) + 1):
  exotic_morph_xp.append(10)
exotic_xp = dict(zip(exotic_morph_list, exotic_morph_xp))

basic_morph_list = ["normal","reduced pattern", "powder blue", "patternless", "piebald", "candy dot",  "caramel", "striped", "zigzag"]

basic_morph_xp = []

for i in range(len(basic_morph_list) + 1):
  basic_morph_xp.append(1)
basic_xp = dict(zip(basic_morph_list, basic_morph_xp))

class Player:
  def __init__(self, name, experience = 0):
    self.name = name
    self.experience = experience
    
  def __repr__(self):
    gecko_count = len(gecko_collection)
    player_desc = "{name} has {xp} XP and {count}".format(name = self.name, xp = self.experience, count = gecko_count)
    if gecko_count == 1:
      player_desc += " gecko.\n"
    else:
      player_desc += " geckos.\n"
    return player_desc

# I need to make the xp funtion work correctly
 
  def breed(self):
    print("Choose a female gecko: ")
    for gecko in gecko_collection:
      if gecko.sex == 'female':
        print(gecko.name)
    female_selection = input("Enter female gecko name: ")
    for gecko in gecko_collection:
        if female_selection == gecko.name and gecko.can_breed == False:
          print("This gecko isn't ready to breed right now. Please feed it or choose another.\n")
        elif female_selection == gecko.name and gecko.can_breed == True:
          print("Choose a male gecko: ")
          for gecko in gecko_collection:
            if gecko.sex == 'male':
              print(gecko.name)
          male_selection = input("Enter male gecko name: ")
          for gecko in gecko_collection:
            if male_selection == gecko.name and gecko.can_breed == False:
              print("This gecko isn't ready to breed right now. Please feed it or choose another.\n")
            elif male_selection == gecko.name and gecko.can_breed == True:
              new_gecko = Gecko(random.choice(names_list), random.choice(sex), random.choice(all_morph_list))
              print("Congratulations!!!!\n A new gecko hatched and was added to your collection!")
              gecko.can_breed == False
              gecko.is_hungry == True
        
# feed() is working    
  def feed(self):
    print("Who do you want to feed?")
    for gecko in gecko_collection:
      if gecko.is_hungry == True:
        print(gecko.name)
    needs_food = input("Enter gecko name: ")    
    for gecko in gecko_collection:
      if gecko.name == needs_food:
        gecko.is_hungry = False
        gecko.can_breed = True
        print("{name} has a full belly now\n".format(name = gecko.name))

  def show_collection(self):
    for gecko in gecko_collection:
      print(str(gecko) + "\n")
    menu()

# add_xp() is adding xp for every gecko in gecko_collection, not just the new gecko.
# I think I need to add this function to the breed function so it only add xp for the new gecko
  def add_xp(self):
    for gecko in gecko_collection:
      if gecko.morph in exotic_morph_list:
        player_1.experience += 10
      else:
        player_1.experience += 1


print("""     
 ██████╗ ███████╗ ██████╗██╗  ██╗ ██████╗ 
██╔════╝ ██╔════╝██╔════╝██║ ██╔╝██╔═══██╗
██║  ███╗█████╗  ██║     █████╔╝ ██║   ██║
██║   ██║██╔══╝  ██║     ██╔═██╗ ██║   ██║
╚██████╔╝███████╗╚██████╗██║  ██╗╚██████╔╝
 ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ \n\n\n""")

player_1 = Player(input("Hello! What is your name?: "))
print("\nHello, {name}!\n".format(name = player_1.name))
gecko1 = Gecko(input("Choose your male gecko's name: "), "male", random.choice(all_morph_list))
gecko2 = Gecko(input("Choose your female gecko's name: "), "female", random.choice(all_morph_list))

print("""\nWelcome to Gecko!\n
You have been given a pair of geckos to breed.
To get started, select from the following options:\n""")

def menu():
  option1 = " 1 - Breed Geckos\n"
  option2 = "2 - Feed Gecko\n"
  option3 = "3 - See Gecko Collection\n"
  option4 = "4 - See Player Stats\n"
  option5 = "5 - Quit Game\n"
  print(option1, option2, option3, option4, option5)
  selection = input("Select an option: ")
  if selection == "1":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    player_1.breed()
    menu()
  elif selection == "2":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    player_1.feed()
    menu()
  elif selection == "3":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    player_1.show_collection()
    menu()
  elif selection == "4":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(player_1)
    menu()
  elif selection == "5":
    quit()
  else:
    menu()

menu()


