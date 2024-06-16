# Details of the home page
define config.name = _("Comp Sci Culminating")
define gui.show_name = True
define config.version = ""
define gui.about = _p("""
""")
define build.name = "Comp Sci Culminating"


#Controls sound of the project. Our project does not have sound.
define config.has_sound = False
define config.has_music = False
define config.has_voice = False


# Animation to enter and exit the game menu.
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None


# Animation for when the game ends
define config.end_game_transition = None


#This makes it so that in between dialogues, there is no placeholder name in between the seperate dialogues.
#For example when we were coding, we found the issue that it showed "Narrator" for like half a second before the next dialogue popped up.
define config.window = "hide"


#Basic settings for how long it takes to show and hide dialogue.
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


# Preference settings


#The time it takes for the words to show up. 0 would be instant and would ruin the flow of the game.
default preferences.text_cps = 35


# This controls how fast the game fast-forwards.
default preferences.afm_time = 15


## Save directory ##############################################################
#This part is in the game by default (We did not code this part)
define config.save_directory = "LearningProjec-1717081668"
define config.window_icon = "gui/window_icon.png"

init python:

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.documentation('*.html')
    build.documentation('*.txt')