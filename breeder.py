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

  # this method will start a cooldown period after a female has been
  # bred. After the female breeds, can_breed = False. 
  # After 3 breeding attempts, can_breed = True.
  def cooldown(self, other_gecko):
    pass

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

#print(exotic_xp)

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

  # breed() will display a list of the female and male geckos in the player's collection. 
  # Then player will select one male and one female from the collection. 
  # The function will take an input for the geckos name and search gecko_collection for the name. 
  # If in the list, breed() will check if can_breed = True. 
  # If both male and female can_breed = True, breed() will create a new instance of Gecko() with a random generated name, sex, and morph.
  #  Depending on the morph generated, morph xp will be added to player xp. After the geckos successfully breed, the can_breed = False. 
  # If a gecko has not been fed since instantiation, the gecko will need to fed to be breedable. 
  def breed(self):
    print("Choose a female gecko: ")
    for gecko in gecko_collection:
      if gecko.sex == 'female':
        print(gecko.name)
    female_selection = input("Enter female gecko name: ")
    for gecko in gecko_collection:
        if female_selection == gecko.name and gecko.can_breed == False:
          print("This gecko isn't ready to breed right now. Please choose another.\n")
        elif female_selection == gecko.name and gecko.can_breed == True:
          print("Choose a male gecko: ")
          for gecko in gecko_collection:
            if gecko.sex == 'male':
              print(gecko.name)
          male_selection = input("Enter male gecko name: ")
          for gecko in gecko_collection:
            if male_selection == gecko.name and gecko.can_breed == False:
              print("This gecko isn't ready to breed right now. Please choose another.\n")
            elif male_selection == gecko.name and gecko.can_breed == True:
              Gecko(random.choice(names_list), random.choice(sex), random.choice(all_morph_list))
              print("""Congratulations!!!!
                    2 new geckos hatched and were added to your collection!""")
        
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
        print("{name} has a full belly now/n".format(name = gecko.name))


# show_collection() is working

  def show_collection(self):
    for gecko in gecko_collection:
      print(str(gecko) + "\n")
    menu()

player_1 = Player("Ethan")
#print(player_1)

print("""     
 ██████╗ ███████╗ ██████╗██╗  ██╗ ██████╗ 
██╔════╝ ██╔════╝██╔════╝██║ ██╔╝██╔═══██╗
██║  ███╗█████╗  ██║     █████╔╝ ██║   ██║
██║   ██║██╔══╝  ██║     ██╔═██╗ ██║   ██║
╚██████╔╝███████╗╚██████╗██║  ██╗╚██████╔╝
 ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ """)

gecko_1 = Gecko(random.choice(names_list), "male", random.choice(all_morph_list))
gecko_1 = Gecko(random.choice(names_list), "female", random.choice(all_morph_list))

print("""Welcome to Gecko!\n
You have been given a pair of geckos to breed.
To get started, select from the following options:\n""")

def menu():
  option1 = "1 - Breed geckos\n"
  option2 = "2 - Feed gecko\n"
  option3 = "3 - See gecko collection\n"
  option4 = "4 - See player points\n"
  print(option1, option2, option3, option4)
  selection = input("Select an option: ")
  if selection == "1":
    player_1.breed()
    menu()
  elif selection == "2":
    player_1.feed()
    menu()
  elif selection == "3":
    player_1.show_collection()
    menu()
  elif selection == "4":
    print(player_1)
    menu()


gecko1 = Gecko(random.choice(names_list), "male", random.choice(all_morph_list))
gecko2 = Gecko(random.choice(names_list), "female", random.choice(all_morph_list))
gecko3 = Gecko(random.choice(names_list), "male", random.choice(all_morph_list))
gecko4 = Gecko(random.choice(names_list), "female", random.choice(all_morph_list))

menu()


