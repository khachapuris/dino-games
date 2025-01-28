def hello(msg1=" Let's play a game!", msg2=""):
    print(r")-               __,                        ")
    print(r"`         O   <( o o                       ")
    print(r"           \</     ..) __________________   ")
    print(r"          </____ `--<   Hello! I'm Dino.  \ ")
    print(r"      _^^/    U  U   \ " + msg1)
    print(r" <==^^/       L_ i_   " + msg2)
    print(r"-----------------------------------------------")


def the_rules(rules):
    print(r")-               __,                          ")
    print(r"`             <( o o                          ")
    print(r"            </___r ..) _______________________")
    print(r"          </____ `-- =\   T H E   R U L E S   \ ")
    print(fr"      _^^/    U  U    / {rules[0]} / ")
    print(fr" <==^^/       L_ i_   \ {rules[1]} \ ")
    print(fr"----------------------/ {rules[2]} /--")
    print(fr"                      \ {rules[3]} \ ")
    print(fr"                      / {rules[4]} / ")
    print(fr"                      \ {rules[5]} \ ")
    print(fr"                      / {rules[6]} / ")
    print(r"                       ------------------------ ")


def pick(obj, title, objs):
    print(fr")-               __,  ( Pick a{obj} you like ")
    print(r"`             <( o o   \/-------------------- ")
    print(r"            </___r ..) _____________________  ")
    print(fr"          </____ `-- =\ {title} \ ")
    print(fr"      _^^/    U  U    /  {objs[0]}/ ")
    print(fr" <==^^/       L_ i_   \  {objs[1]}\ ")
    print(fr"----------------------/  {objs[2]}/----")
    print(fr"                      \  {objs[3]}\ ")
    print(r"                       ----------------------  ")
    return input()


def something_went_wrong(msg1="Something went wrong! ", msg2=None):
    if msg2:
        print()
        print(r")-               __,                         ")
        print(r"`         ?   <( o o   p                     ")
        print(r"           \</     ..)/____________________  ")
        print(fr"          </_____ ~~< {msg1}\ ")
        print(r"      _^^/    U  U   \ " + msg2)
        print(r" <==^^/       L_ i_                          ")
        print(r"-----------------------------------------------")
    else:
        print()
        print(r")-               __,                         ")
        print(r"`         ?   <( o o   p                     ")
        print(r"           \</     ..)/____________________  ")
        print(fr"          </_____ ~~< {msg1}) ")
        print(r"      _^^/    U  U                           ")
        print(r" <==^^/       L_ i_                          ")
        print(r"-----------------------------------------------")


def you_lost():
    print()
    print(r" ~~~~            __,            ")
    print(r" ' '          <( -,-;           ")
    print(r"  ' '       </\   '..)_________ ")
    print(r" ' '      </___\_~~< You lost! )")
    print(r"  '   _^^/   U  T               ")
    print(r" <==^^/      L_ i_              ")
    print(r"-----------------------------------------------")


def i_win():
    print(r")-               __,             ")
    print(r"`             <( o o             ")
    print(r"            </\    ..)_________  ")
    print(r"          </___\_`--<  I win!  \ ")
    print(r"      _^^/    U  T               ")
    print(r" <==^^/       L_ i_              ")
    print(r"-----------------------------------------------")


def you_win(msg1="       You win!       ", msg2="   Congradulations!"):
    print()
    print(r")-               __,                          ")
    print(r"`         n|  <( - o                         ")
    print(r"           \</     ..) ____________________   ")
    print(fr"          </____ `--< {msg1}\ ")
    print(r"       _^^/   U  U    \ " + msg2)
    print(r" <==^^/       L_ i_                            ")
    print(r"-----------------------------------------------")


def give_up():
    print(r")-               __,                     ")
    print(r"`         ?   <( o o   p                 ")
    print(r"           \</     ..)/_____________     ")
    print(r"          </____ `--<   I give up!  \    ")
    print(r"      _^^/    U  U   \  What is it?      ")
    print(r" <==^^/       L_ i_                      ")
    print(r"-----------------------------------------------")


def draw():
    print(r")-               __,                       ")
    print(r"`         ?   <( o o   p                   ")
    print(r"           \</     ..)/________________    ")
    print(r"          </____ `--<   It's a draw!   )   ")
    print(r"      _^^/    U  U                         ")
    print(r" <==^^/       L_ i_                        ")
    print(r"-----------------------------------------------")


def print_scoreboard(scoreboard, msg1, msg2):
    scoreboard = [str(score) for score in scoreboard]
    for a in [0, 1]:
        if len(scoreboard[a]) == 1:
            scoreboard[a] = ' ' + scoreboard[a]
        if scoreboard[a].strip().endswith('1') and scoreboard[a] != '11':
            scoreboard[a] += " time "
        else:
            scoreboard[a] += " times"
    print(r")-               __,  ( Thank you for playing! )")
    print(r"`             <( o o   \/---------------------  ")
    print(r"            </___r ..) ___________________      ")
    print(fr"          </____ `-- =| {msg1} {scoreboard[0]} | ")
    print(fr"      _^</    U  U    | {msg2} {scoreboard[1]} | ")
    print(r" <==^^/       L_ i_    -------------------      ")
    print(r"------------------------------------------------")


def print_greetings(greetings="Congradulations"):
    print(fr")-                 ( {greetings}!!!")
    print(r"`                __, \/--------------------- ")
    print(r"              <( o o .--(\__/)──.. ")
    print(r"            </\    ..)  //--\\\\  || ")
    print(r"          </___\_`== |   |  |   || ")
    print(r"      _^^/    U  T   |   |  |   || ")
    print(r" <==^^/       L_ i_  `----------`` ")
    print(r"-----------------------------------------------")

