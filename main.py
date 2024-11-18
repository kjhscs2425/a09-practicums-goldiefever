'''In the theatre department at UC San Diego, there's a requirement that all theatre majors and minors take a class where they learn a practical backstage skill. Here are the choices for skills:

* Costumes
* Scenery
* Lighting
* Sound

You will make a script that implements a sign up process for practicums.

You will write two functions:

1. The `choose_practicum` function.
   * Ask the user to sign up for a practicum
   * If they choose a valid practicum, return their choice
   * Otherwise, call the function `choose_practicum` again (recursive call) and return the result of that.
2. The main function for the signup process. This will:
  * Ask for the user's name and save it to a variable
  * Call the `choose_practicum` function and save the result to a variable.
  * Print out a confirmation that says, "Congratulations, NAME, you are signed up for PRACTICUM" using an f-string so whatever the user gave as input'''

signup = input("Choose a theatre course to sign up for: ")

def choose_practicum():
    print(signup)
    if signup in ["Costumes" , "costumes" , "Costume" , "costume" , "Scenery" , "scenery" , "Lighting" , "lighting" , "Sound" , "sound"]:
        return signup
    else:
        choose_practicum()

def theatre_signup():
    choose_practicum()
    name = input("Enter your full name: ")
    confirm = (f"Congratulations, {name}, you are signed up for {signup}!")
    print(confirm)

theatre_signup()
