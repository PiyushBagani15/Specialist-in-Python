import os
import pyttsx3 as ps
import subprocess as sb
ps.speak("WELCOME TO MY APPLICATION")
ps.speak("How Can I Help You")

while True:

    p=input('Tell Me about Your Requirements:')

    if ('notepad' in p.lower() or 'editor' in p.lower()) and ('run' in p.lower()  or  'open' in p.lower()):
        if("don't" not in p.lower()  or  'not' not in p.lower() or'dont' not in p.lower()):
            ps.speak("Opening Notepad")
            os.system('notepad') #we can also do it by sb.call("notepad.exe")
            
    elif('dont' in p.lower() or 'not' in p.lower()):
            print('You denied Me to open Application')

    elif ('chrome' in p.lower() or 'browser' in p.lower()) and ('run' in p.lower() or 'open' in p.lower()):
        if("don't" not in p.lower()  or  'not' not in p.lower() or 'dont' not in p.lower()):
            ps.speak("Opening Chrome")
            os.system('chrome')  #we can also do it by sb.call("chrome.exe")
            
    elif('dont' in p or 'not' in p):
            print('You Denied Me to open Application')
            
    elif ('wmplayer' in p.lower() or 'media player' in p.lower() or 'music player' in p.lower()) and ('run' in p.lower() or 'open' in p.lower()):
        if("don't" not in p.lower()  or  'not' not in p.lower() or 'dont' not in p.lower()):
            ps.speak("Opening Windows media player")
            os.system('wmplayer')
          
    elif('dont' in p or 'not' in p):
            print('You denied Me to open')
            
    elif ('zoom' in p.lower() or 'zoomapp' in p.lower() or 'video' in p.lower() or 'conferencing' in p.lower()) and ('run' in p.lower() or 'open' in p.lower()):
        if("don't" not in p.lower()  or  'not' not in p.lower() or 'dont' not in p.lower()):
            ps.speak("Opening Zoom")
            os.system('zoom')
          
    elif('dont' in p or 'not' in p):
            print('You denied Me to open')
            
    elif ('paint' in p.lower() or 'mspaint' in p.lower() or 'draw' in p.lower()) and ('run' in p.lower() or 'open' in p.lower()):
        if("don't" not in p.lower()  or  'not' not in p.lower() or 'dont' not in p.lower()):
            ps.speak("Opening Paint")
            os.system('mspaint')
          
    elif('dont' in p or 'not' in p):
            print('You denied Me to open')
    elif ('telegram' in p.lower() or 'telegram desktop' in p.lower() or 'telegram messenger' in p.lower()) and ('run' in p.lower() or 'open' in p.lower()):
        if("don't" not in p.lower()  or  'not' not in p.lower() or 'dont' not in p.lower()):
            ps.speak("Opening Telegram")
            os.system('Telegram')
          
    elif('dont' in p or 'not' in p):
            print('You denied Me to open')
    elif ('whatsapp' in p.lower() or 'whatapp desktop' in p.lower() or 'whatsapp messenger' in p.lower()) and ('run' in p.lower() or 'open' in p.lower()):
        if("don't" not in p.lower()  or  'not' not in p.lower() or 'dont' not in p.lower()):
            ps.speak("Opening WhatsApp")
            os.system('WhatsApp')
          
    elif('dont' in p or 'not' in p):
            print('You denied Me to open')
    elif ('firefox' in p.lower() or 'firefox browser' in p.lower() or 'mozilla' in p.lower() or 'mozilla firefox' in p.lower()) and ('run' in p.lower() or 'open' in p.lower()):
        if("don't" not in p.lower()  or  'not' not in p.lower() or 'dont' not in p.lower()):
            ps.speak("Opening Firefox")
            os.system('Firefox')
          
    elif('dont' in p or 'not' in p):
            print('You denied Me to open')
    elif ('cmd' in p.lower() or 'command' in p.lower() or 'command prompt' in p.lower() or 'terminal' in p.lower()) and ('run' in p.lower() or 'open' in p.lower()):
        if("don't" not in p.lower()  or  'not' not in p.lower() or 'dont' not in p.lower()):
            ps.speak("Opening Command prompt")
            os.system('cmd')
          
    elif('dont' in p or 'not' in p):
            print('You denied Me to open')
    elif ('control' in p.lower() or 'control panel' in p.lower() or 'settings' in p.lower()) and ('run' in p.lower() or 'open' in p.lower()):
        if("don't" not in p.lower()  or  'not' not in p.lower() or 'dont' not in p.lower()):
            ps.speak("Opening control panel")
            os.system('control')
          
    elif('dont' in p or 'not' in p):
            print('You denied Me to open')
    elif ('git' in p.lower() or 'git bash' in p.lower() or 'bash' in p.lower()) and ('run' in p.lower() or 'open' in p.lower()):
        if("don't" not in p.lower()  or  'not' not in p.lower() or 'dont' not in p.lower()):
            ps.speak("Opening Git Bash")
            os.system('git bash')
          
    elif('dont' in p or 'not' in p):
            print('You denied Me to open')


    elif ('this pc' in p.lower() or 'my computer' in p.lower()) and ('run' in p.lower() or 'open' in p.lower()):
        if("don't" not in p.lower()  or  'not' not in p.lower() or 'dont' not in p.lower()):
            ps.speak("Opening This PC")
            sb.call('explorer.exe')
            
    elif('dont' in p or 'not' in p):
            print('You denied Me to open The application') 
    elif ('quit' in p.lower() or 'exit' in p.lower()):
        ps.speak("Sorry To see You go")
        ps.speak("Thank You, Please Visit Again")
        exit()
    else :
        ps.speak("Sorry,Please enter a valid Choice")
