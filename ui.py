class Menu:

  def menu_choice(self):
    done = False
    print("0: Quit")
    print("1: Integer Set")
    print("2: Custom Set")

    while not done:
      choice = input("Choice > ")

      if not choice.isdigit():
        print("Invalid entry")
      else:
        done = True;

    return choice

  def start(self):
    nav = int(self.menu_choice())

    if nav == 1:
      new_set = IntSet()
      new_set.get_range()


    #integer_set():
    #custom_set():

class IntSet:
  lower = 0
  upper = 0

  def __init__(self):
    self.lower = lower
    self.upper = upper

  def get_range(self):
    lower = input("Provide integer range from: ")
    upper = input("to: ")

"""
  set_ret = set.create_set(start, end);

  cout << "\nNew set, cardinality " << set_ret << endl;
  set.display();
  cout << "\nPress ENTER to continue.";
  cin.ignore();
  return 1;
"""
