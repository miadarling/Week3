def tryADifferentPath ():
  print "START AGAIN! JUST KEEP SWIMMING! GO!"
  
  startStory()

def askAgain():
  tryADifferentPath()

def tellStory():
  print "Start telling the story"

    #------octopus storyline------
def octopus ():
  print "You swim to the dark cave of wisdom where the wise octopus emerges from the deep."
  print "The wise octopus says that the waves have told him your story."
  print '                _,--._ '
  print '              ,/      \. '
  print '      |\     / ,-.  ,-. \     /| '
  print '      )o),/ ( ( o )( o ) ) \.(o( '
  print '     /o/// /|  `-+  `+-  |\ {\o\ '
  print '    / / |\ \(   .    ,   )/ /| \ \ '
  print '    | | \o`-/     \/    \-\o/ | | '
  print '    \ \  `,/              `.^  / / '
  print '  \.  \ `-^ /\|   /\  \`.  `- /  ,/ '
  print '   \`. `.__, `   /  \  \  \__.__,/ ///'
  print '    \o\     ,/  /    \  `.        /o/ '
  print '     \o`---`   "`     `.  `------/o/ '
  print '      `.____,/`         `.______,`/'

  playerChoice = raw_input ("Do you ask the wise octopus the secret to your happiness? Type yes or no.")
  
  print "You chose " + playerChoice
  
  if (playerChoice == "yes"):
    print "You've proven your generosity."
    print "The wise octopus tells you to continue to be good and to give your glittery scales to your friends. GLITTER ON!"
    print '              OOOOOOOOOOO '
    print '         OOOOOOOOOOOOOOOOOOO '
    print '       OOOOOO  OOOOOOOOO  OOOOOO'
    print '     OOOOOO      OOOOO      OOOOOO '
    print '   OOOOOOOO  #   OOOOO  #   OOOOOOOO '
    print '  OOOOOOOOOO    OOOOOOO    OOOOOOOOOO '
    print ' OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO '
    print 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO00'
    print 'OOOO  OOOOOOOOOOOOOOOOOOOOOOOOO  OOOO0 '
    print ' OOOO  OOOOOOOOOOOOOOOOOOOOOOO  OOOO0 '
    print '   OOOO   OOOOOOOOOOOOOOOOOOOO  OOOO'
    print '     OOOOO   OOOOOOOOOOOOOOO   OOOO '
    print '      OOOOOO   OOOOOOOOO   OOOOOO'
    print '         OOOOOO           OOOOOO '
    print '              OOOOOOOOOOOO'
    return 
    
  else:
    print "AH! Indigo ink!"
    print "You're lost in the cave!"
    print "A cloud of ink, black, and mystery!"
    print "Red eyes suddenly appear from the darkness!"
    print "The octopus strangles you! He tries to SWALLOW you WHOLE!"
    print "You blind the octopus with a flicker of light from your glittery scales and swim away!"
    tryADifferentPath()

#-----start of the story------
def startStory():
  print ' _____________ ______________'
  print ' \_    ____/__|___\__    ___/ '
  print '  |    | /    ~    \    __)_  '
  print '  |    | \    Y    /        \ '
  print '  |____|  \___|_  /_______  / '
  print '                \/        \/ '
  print '_________    _____  .___ _______ __________ ________  __      __  '
  print '\______   \  /  _  \ |   |\      (\______  )(____  \/  \    /  \ '
  print ' |       _/ /  /_\  \|   |/   |   \|    |  _/ /   |   \   \/\/   / '
  print ' |    |   \/    |    \   /    |    \    |   \/    |    \        / '
  print ' |____|_  /\____|__  /___\____|__  /______  /\_______  /\__/\  / ' 
  print '       \/         \/            \/       \/         \/      \/   '
  print '___________.___  _________ ___ ___  '
  print ' \_   _____/|   |/   _____//   |   \ '
  print ' |    __)  |   |\_____  \/    ~    \ '
  print ' |     \   |   |/        \    Y    / '
  print ' \___  /   |___/_______  /\___|_  / '
  print '     \/                \/       \/  '

  print '        /^^^^^7 '
  print '     ,oO))))))))Oo, '
  print '   ,/)))))))))))))), /{ '
  print ' ,/o  ))))))))))))))))={ ' 
  print ' >     ))))))))))))))))={ '
  print '  `,   ))))))\ \)))) ))={ '
  print '    ",))))))))\/)))))) \{ '
  print '      "*O))))))))O*'

  print "A calm sea, turquoise waters, and the enticement to swim."
  print '   ;--.   \ '
  print ' _/oo==\===| '
  print '(_ ___, \  | '
  print '   )_/  / / '
  print '   `--^^` '
  print '       /U/`--. '
  print '      ///,____) '
  print '     /// //  / '
  print '    ""  // <` '
  print '        \`\ \ '
  print '         _/_/__\_ '
  print '        \        | '
  print '            ===   -  (--. '
  print '              \         | '
  print '   ~^~^~^~^~^~[_________| '
  print '    ~^~^~^~^~^/////////// '
  print '  ~^~^~^~^~^~^////////// '

  print "You jump into the water and magic!"
  print "You become a beautiful rainbow fish with glittery scales that sparkle in the light."
  print "A little blue fish approaches from the coral reef."
  playerChoice = raw_input ("The little blue fish asks if please, can you spare a glittery scale? Type yes or no.")
  print "You chose " + playerChoice
  if (playerChoice == "yes"):
    print "You are happy with your colorful scales and play with your friends with happiness."
    starfish()
  elif(playerChoice == "no" ):
    print "You swim in the waves with no friends, sad and lonely, swimming in the vast ocean alone forever."
    starfish()
  else:
    print "I don't understand. Choose again."
    startStory()

#-------starfish storyline------
def starfish ():
  print "You meet a little red starfish in the coral reef."
  print  '    =\  ,  / '
  print  '   ,___/_\___, '
  print  '    \ /o o\ / '
  print  '-=   > \_/ <   =- '
  print  '    /_\___/_\ '
  print  ' . `   \ /   ` . '
  print  '      / ^  \ '
  print  '        .'

  playerChoice = raw_input ("Do you talk to the little red starfish? Type yes or no.")

  print "You chose " + playerChoice

  if (playerChoice == "yes"):
    print "The little red starfish says that the wise octopus knows why you are sad."
    octopus()
  elif (playerChoice == "no"):
    print "You swim away from the little red starfish and wonder why you have no friends."
    octopus()
  else:
    print "I don't understand. Choose again."
    starfish()
  
 
  #-----little blue fish------
  def littlebluefish ():
    print "You swim away and along your journey, you see a little blue fish playing in the colorful coral reef."
    print '  _///_ '
    print ' /o    \/ '
    print ' > ))_./\ '
    print '     <' 
    playerChoice == raw_input ("Do you give one of your glittery scales to the little blue fish? Type yes or no.")
    print "You chose " + playerChoice    
    if (playerChoice == "yes"):
      askAgain()
  
    else:
      print "I don't understand. Choose again."
    
def main():
  startStory()
  
main()
