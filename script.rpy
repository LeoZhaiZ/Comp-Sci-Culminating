#This code is mainly dialogue. Uses Ren'py for dialogues.
#We used python commands to add the actual functions of the game (Ex. Name creating, Ordering at restaurant, Choosing dialogue options and choices)
#Python commands start with $

#Defines the characters
define me = Character("[me]")
define dad = Character("Dad")
define mom = Character("Mom")
define friend = Character("[friend]")
define teacher = Character("Mr. Khurram")
define bully = Character("Classroom Bully")
define kid = Character("Random Kid")
define thoughts = Character("*Thinking*")
define narrator  = Character("Narrator")
define arthur = Character("Arthur")
define s = Character("Stranger")
define r = Character("Random Dude")
define w = Character("Waiter")
define empty = Character("")

default ordered_items = []
default total_price = 0.0

#Beginning part of the story.
label start:

    scene black

    #Dialogue starts
    #Asks for name
    $ me = renpy.input("What is your name?", length=12)
    me "Urgh...."
    me "Man I'm so tired...."
    scene bg bedroom with fade:
        zoom 3.75
    me "It feels impossible to get out of bed right now..."
    scene black with fade
    me "5 more minutes..."
    mom "[me], WAKE UP ITS TIME FOR SCHOOL!!"
    scene bg bedroom with fade:
        zoom 3.75
    me "Nevermind then I guess."
    me "Time to start the day."
    
    menu:
        "What do you choose to do?"

        "Go downstairs":
            jump downstairs

label downstairs:
    scene bg kitchen with fade
    show mom happy with fade:
        zoom 2.6
    mom "Good morning [me]! You look awfully tired."
    me "Morning mom.. You look awfully happy today.."
    mom "Well of course! It's May 18th today! Do you know what day that is..?"
    me "No mom... What day is that?"
    mom "Wednesday!"
    me "Ok... and what day is wednesday?"
    mom "Wednesday!"
    me "..."
    me "I'll just have some breakfast..."
    hide mom happy wtih fade
    show dad reading at center with fade:
        zoom 2.5
    me "Good morning Dad."
    dad "Good morning [me], make sure not to be late for school!"
    me "Alright see you guys later."
    hide dad reading

#Fades into front of school
    scene bg schoolfront with fade:
        zoom 3.75

    pause 2

    scene bg hallway with fade
#Part 2 School
    $ friend = renpy.input("What is your friends name?", length=12)
    show friend talking with fade:
        zoom 2
    friend "Hey there [me], what you up to?"

    menu:
        me "Oh whats up [friend], "
        "I just got here, I was just relaxing":
            me "I just got here, I was just relaxing."
            jump school1
        "I was about to head to class.":
            me "I was about to head to class."
            jump school1
label school1:
    show friend happy:
        zoom 2
    friend "Nice. Want to head to class together?"
    me "Yeah sure, let's go."
    show friend questioning:
        zoom 2
    friend "Oh yeah, did you finish the comp sci culminating? Apparently it's worth 50 percent of our final mark."

    menu:
        "What will you say?"
        "Yeah I finished it (Lie)":
            me "Yeah I finished it."
            jump schoolsub1
        "We had a culminating?":
            jump school2

label schoolsub1:
    show friend talking:
        zoom 2
    friend "Yeah... you didn't do it did you?"
    me "Yeah.."
    jump school2

label school2:
    me "We had a culminating?"
    show friend worried:
        zoom 2
    friend "You're in so much trouble man, our teacher is going to be so mad at you."
    me "Pray for me I guess. I'm gonna have to hope Mr. Khurram doesn't get too mad."
    hide friend worried with fade
#Fade into classroom
    scene bg classroom with fade
    
    show khurram happy 
    teacher "Welcome class, here is a photo of the solar system right now in comparison to the solar system at the start of the school year!"
    show khurram talking
    teacher "This shows how we are constantly moving and how every day is different."
    show khurram happy
    teacher "Today's the due date for the culminating, is everybody ready to hand it in?"
    hide khurram happy
    show bully happy at left with fade:
        zoom 1.4
    bully "Yes sir I'm ready to hand it in!"
    me "Oh man, the classroom bully, I hate that guy."
    show bully talking at left:
        zoom 1.4
    bully "You know who isn't though? [me]! He doesn't even have his computer on his table! HAHA"
    bully "Looks like he thought he was too good to finish the culminating."
    hide bully talking
    show friend worried:
        zoom 2
    friend "Uh oh [me], you're screwed."
    me "Uh oh"
    hide friend worried
    show khurram mad with fade
    teacher "[me], come to my office after school."
    me "Yes sir.."
    hide khurram mad
    show bully talking at left with fade:
        zoom 1.4
    bully "heh, idiot."
    hide bully talking with fade
    #After class
    #Fade into office background.
    scene black with fade
    "At the end of school..."
    scene bg office with fade
    show khurram talking with fade
    teacher "Welcome, [me]."
    me "Hi Mr. Khurram..."
    show khurram happy 
    teacher "Do you mind explaining to me why your homework wasn't completed? This is a serious issue [me]. Is something bothering you at home or something?"
    
    menu:
        "What will you say?"
        "Sorry Mr. Khurram, I just forgot to do it.":
            jump schoolsub3
        "My dog ate my homework...":
            jump schoolsub2

label schoolsub3:
    me "Sorry Mr. Khurram, I just forgot to do it."
    show khurram talking 
    teacher "At least you were honest about it. I'll let you off the hook for today. but make sure you hand it in by Friday."
    show khurram happy
    me "Thanks so much Mr. Khurram!"
    hide khurram happy with fade
    #Good ending with Mr. Khurram
    jump school3

label schoolsub2:
    me "My dog ate my homework..."
    show khurram talking
    teacher "Your dog ate your coding assignment...?"
    show khurram mad
    me "..."
    me "......"
    me "It took a couple bytes..."
    show khurram talking
    teacher "Get out."
    show khurram mad
    me "What about my mark-"
    show khurram talking
    teacher "Zero. Get out."
    show khurram mad
    me "Ok..."
    hide khurram mad with fade
    empty "BAD ENDING WITH MR. KHURRAM"
    scene black with fade
    narrator "What made you think that was going to work?"
    narrator "You head into the school hallways.."
    jump school3

label school3:
    scene bg hallway with fade
    me "Alright, now that I'm done with that, I guess I'll just start heading home."
    empty "WHAM" with vpunch
    me "Huh?"
    empty "POW! BAM!!" with vpunch
    me "Am I hearing things..?"
    empty "OWWW STOP PLEASE"
    me "What was that??"
    menu:
        "You choose to..."
        "Go check it out.":
            jump school4
        "Ignore it and go home.":
            jump schoolsub4

label schoolsub4:
    scene bg walking with fade:
        zoom 4
    me "Guess I'll just head home."
    me "Whoever that was yelling can figure it out himself I'm sure."
    me "Today sure felt uneventful."
    empty "GOOD ENDING (MISSED CONTENT)"
    return
label school4:
    me "I should go check that out."
    scene bg hallway2 with fade
    #Show bully
    show bully mad at left with fade:
        zoom 1.4
    me "Uh oh, it's the school bully..."
    me "Wait who's that in the corner though...?"
    show arthur talking at right with fade:
        zoom 2

    bully "You probably think you're all that just cause you get good grades but you're still just a loser you know that right?"
    show bully talking at left:
        zoom 1.4
    me "*whispering* What the hell?"
    bully "You think you can finally stand up for yourself? Loser."
    empty "BAM" with vpunch
    show arthur sad at right:
        zoom 1.4
    kid "Oww dude stop... I already did your homework for you.. What more do you want from me..?"
    me "*whispering* Oh man I can't just watch this happen, the poor kids getting bullied."
    hide arthur sad
    hide bully talking

    menu:
        "I should go help the kid":
            jump school5
        "Actually, nevermind I think I can just watch this happen.":
            jump schoolsub5
label schoolsub5:
    me "Yeah, no way am I going in there. The bully's gonna beat me up too"
    scene bg walking with fade:
        zoom 4
    me "Poor kid got beat up, not much I can do about that."
    me "I feel like I should've at least checked if he was okay..."
    me "Whatever, too late for that now."
    scene black with fade
    empty "BAD ENDING (MISSED CONTENT)"
    return

label school5:
    show bully talking at left with fade:
        zoom 1.4
    show arthur sad at right with fade:
        zoom 1.4
    me "Yo! Dude!"
    show bully mad at center:
        zoom 1.4
    hide arthur sad with fade
    bully "Huh? You talkin to me [me]?"
 
    me "Yeah, who else?"
    show bully talking at center:
        zoom 1.6
    bully "Who do you think you're raising your tone to?"
    me "I'm raising my voice to YOU. What do you think you're doing bullying that poor kid in the school hallway?"
    show bully sad at center:
        zoom 1.6
    bully "Well, are you gonna do something about it? I'd like to see you try."
    thoughts "Ooh. I'm about to get beaten up"
    me "Maybe I will. Try me."
    show bully mad at center:
        zoom 1.6
    thoughts "Mom, Dad, thanks for always being there for me. I think today might be my last day."
    show bully mad at left:
        zoom 1.6
    show khurram mad with fade
    teacher "EXCUSE ME WHAT IS HAPPENING HERE?!" with vpunch
    show bully talking at left:
        zoom 1.6
    bully "Mr. khurram! What a pleasure to see you here!"
    me "MR KHURRAAM"
    show bully mad at left:
        zoom 1.6
    bully "Damn, you got lucky today [me]. Don't let me catch you in the hallways."
    hide bully mad with fade
    #bully leaves
    show khurram talking
    teacher "[me] just what exactly was happening here?"
    show khurram mad
    me "Uh, nothing. We were just having a conversation."
    show khurram talking
    teacher "Hm. Sure you were."
    show khurram mad
    me "I swear I was Mr. Khurram."
    show khurram talking
    teacher "Don't let me catch you doing this again."
    show khurram mad
    me "Yes sir."
    hide khurram mad with fade
    scene black with fade
    scene bg hallway2 with fade
    me "Yo, are you good man?"
    show arthur happy at center with fade:
        zoom 1.4
    kid "Yeah I am, thanks for helping me dude, he's been a real pain in the butt for me for like the past month."
    me "Has he been bullying you?"
    show arthur scared at center:
        zoom 1.4
    kid "Yeah.. He's been harassing me cause he caught me reading books in the library. Started calling me a nerd and stuff"
    me "Oh man, that must suck."
    me "By the way, what's your name?"
    show arthur talking at center:
        zoom 1.4
    kid "Oh, the name's Arthur. Nice to meet you man."
    me "I'm [me], it's nice to meet you too."
    show arthur happy at center:
        zoom 1.4
    arthur "Thanks so much for this again dude, you know what? How about I treat you to dinner?"

    menu:
        "What will you say?"
        "Sure why not let's go.":
            jump restaurant1
        "Uh I think I'm good thanks.":
            jump schoolsub6

label schoolsub6:
    me "Uh I think I'm good thanks."
    show arthur scared at center:
        zoom 1.4
    arthur "Aw man, that's alright. See you in school then!"
    me "Sounds good."
    hide arthur scared with fade
    scene bg walking with fade:
        zoom 4
    me "Today was a pretty okay day I guess. I stood up for Arthur, but now the bully's going to target me..."
    me "Maybe I should have gone to the restaurant with Arthur.."
    me "Too late for that now. I need to focus on my culminating."
    scene black with fade
    empty "GOOD ENDING (MISSED CONTENT)"
    return

label restaurant1:
    scene bg restaurantoutdoors with fade
    show arthur talking with fade:
        zoom 1.4
    arthur "Here we are, the new cafe in Markham."
    menu:
        "Let's go in.":
            jump restaurant2
        "Actually on second thought I don't really want to go...":
            jump restaurantsub1


label restaurantsub1:
    me "Actually on second thought I don't really want to go..."
    show arthur happy at center:
        zoom 1.4
    arthur "That's too bad.. Because we're already here and you don't have a choice anymore. Haha"
    me "Alright..."
    hide arthur happy
    jump restaurant2

label restaurant2:
    me "Let's go in."
scene bg restaurant with fade





label restaurantstart:
    scene bg restaurant
    show waiter happy:
        zoom 0.25
    w "Hello! Table for how many people?"
    hide waiter happy


    menu:
        "2 people":
            jump table_for_2
        "7 people":
            jump table_for_7
        "Can I have 3 tables please?":
            jump three_tables


label table_for_2:
    scene bg restaurant
    w "Alright, table for 2. Got it."
    jump restaurant_3


label table_for_7:
    scene bg restaurant
    show waiter happy:
        zoom 0.25
    w "Uh… Where’s the other 5 people?"
    hide waiter happy
    show arthur talking at center:
        zoom 1.4
    arthur "Oh sorry about that my friend means 2 people."
    me "Uh.."
    hide arthur talking
    show waiter happy:
        zoom 0.25
    w "Okay… So table for 2. Got it."
    jump restaurant_3


label three_tables:
    scene bg restaurant
    w "huh?"
    hide waiter happy 
    show arthur scared at center:
        zoom 1.4
    arthur "huh?"
    me "huh?"
    show arthur talking at center:
        zoom 1.4
    arthur "uhh table for 2 please."
    hide arthur talking
    show waiter happy:
        zoom 0.25
    w "sure.."
    hide waiter with fade
    jump restaurant_3


label restaurant_3:
    scene bg restaurant
    w "Alright here’s the menu, take your choice."
    jump show_menu


label show_menu:
    scene bg restaurant


    menu:
        "Hamburger - $2.50":
            $ ordered_items.append("Hamburger")
            $ total_price += 2.50
            jump after_order
        "Cheese Burger - $2.75":
            $ ordered_items.append("Cheese Burger")
            $ total_price += 2.75
            jump after_order
        "Chicken Burger - $3.00":
            $ ordered_items.append("Chicken Burger")
            $ total_price += 3.00
            jump after_order
        "Medium Fries - $1.50":
            $ ordered_items.append("Medium Fries")
            $ total_price += 1.50
            jump after_order
        "Large Fries - $2.00":
            $ ordered_items.append("Large Fries")
            $ total_price += 2.00
            jump after_order
        "Poutine - $3.50":
            $ ordered_items.append("Poutine")
            $ total_price += 3.50
            jump after_order
        "Soda - $1.00":
            $ ordered_items.append("Soda")
            $ total_price += 1.00
            jump after_order


label after_order:
    scene bg restaurant


    menu:
        "That will be all thank you.":
            jump order_complete
        "Can I order some more?":
            w "Sure, what else would you like?"
            jump show_menu


label order_complete:
    scene bg restaurant
    show waiter happy with fade:
        zoom 0.25
    w "Alright, your total will be $[total_price:.2f]. Your order will consist of a [', a '.join(ordered_items)]."
    me "Sounds good."
    w "I will be back with your food shortly."
    hide waiter happy with fade
    jump restaurant_5


label restaurant_5:
    scene bg restaurant
    show arthur talking at center with fade:
        zoom 1.4
    arthur "I’m gonna go to the washroom really quickly."
    hide arthur talking
    me "Go for it."
    empty "..."
    empty "..."
    s "Psst. Hey, kid."
    empty "..."
    s "Hey KID."
    me "Are you talking to me?"
    s "Yeah bud I was just wondering if you could do me a little favor."


    menu:
        "Depends on what it is":
            jump stranger_favor
        "No, stop bothering me dude":
            s "Jeez dude, alright, no need to get angry."
            jump restaurant_bill
        "Uhhh I don’t know man you seem pretty sketchy":
            s "Whatever dude. That’s rude as hell."
            jump restaurant_bill


label stranger_favor:
    scene bg restaurant
    s "I was just wondering if you could pour some of this little powder into that person’s drink over there."


    menu:
        "Hell no":
            jump restaurant_bill
        "Sure I guess":
            me "*pours powder into random persons drink*"
            r "HEY I JUST SAW THIS GUY POUR SOMETHING INTO THAT GIRLS DRINK!"
            arthur "[me]??? What were you doing just now??"
            show arthur scared at center:
                zoom 1.4
            me "I swear I didn’t do anything you have to trust me! That guy over there told me to do it!"
            hide arthur scared
            s "I have no clue whats happening what do you mean me??"
            r "The cops are coming right now. You better stay still."
            me "You have to listen to me! I swear it wasn’t me!"
            show arthur scared at center:
                zoom 1.4
            arthur "I can’t believe you were someone like that [me]. I didn’t know these were your true colors."
            hide arthur scared
            scene black with fade
            "The cops have arrived and you have been arrested for spiking somebodies drink."
            "None of your friends trust you and your family began to distance themselves from you."
            "Maybe next time don’t trust sketchy strangers in public, idiot."
            "WORST ENDING."
            return


label restaurant_bill:
    scene bg restaurant
    "You’ve finished eating your food, and you had a great chat with Esmond about school and friends while eating"
    "The waiter has given great service while you were eating,"
    arthur "Man, I had a great time. Let’s get the bill now."
    arthur "Oh no, I only have enough money to pay for the food but not for the tip."
    arthur "You think you can pay the tip for me?"


    menu:
        "Sure yeah I’ve got you":
            jump best_ending
        "Let’s just not tip then":
            jump mediocre_ending


label best_ending:
    scene bg restaurant
    arthur "Alright, perfect, thanks so much man! I’m going to head home now. See you in school sometime dude!"
    me "It was nice meeting you too man!"
    scene bg walking with fade:
        zoom 4
    me "Wow, what a great day today was…"
    "BEST ENDING"
    return


label mediocre_ending:
    scene bg restaurant
    arthur "Uh.. I mean, if you really don’t want to pay the tip then theres not much we can do about it.."
    me "Whatever it’s fine, they get paid by the restaurant anyways."
    arthur "If you say so man.."
    w "Not tipping in a restaurant? What jerks."
    scene bg walking with fade:
        zoom 4
    me "Today was an okay day I guess.. It didn’t feel perfect."
    "MEDIOCRE ENDING"
    return
