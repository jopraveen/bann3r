# importing modules
from pyfiglet import Figlet
from termcolor import colored

# colors
gr = 'green'
rd = 'red'
bl = 'blue'
cn = 'cyan'
wt = 'white'
mn = 'magenta'

# Banner
print("")
print(colored(" __________                      ________   Creator Tool",cn))
print(colored(" \______   \_____    ____   ____ \_____  \______  ",cn))
print(colored("  |    |  _/\__  \  /    \ /    \  _(__  <_  __ \ By Jopraveen",cn))
print(colored("  |    |   \ / __ \|   |  \   |  \/       \  | \/ ",cn))
print(colored("  |______  /(____  /___|  /___|  /______  /__|   ",cn))
print(colored("         \/      \/     \/     \/       \/         ",cn))


def ban():
	# Getting Input
	banner = input(colored("\nType your Banner's text: ",gr))

	# Generating banner
	custom_fig = Figlet(font='./graffiti')
	print(colored("\n\n==========<( Your Banner\n",cn))
	print(custom_fig.renderText(banner))
	print(colored("\n==========<( Thankyou For Using :D\n",cn))
ban()
# multiple times
mult = input("\n\n\nDo you want to run again and again? ( y / n ) ")

if mult == "y":
	while True:
		ban()
else:
	print("")
	print("  ___________.__                   __                        ")
	print("  \__    ___/|  |__ _____    ____ |  | _____.__. ____  __ __ ")
	print("    |    |   |  |  \\__  \  /    \|  |/ <   |  |/  _ \|  |  \ ")
	print("    |    |   |   Y  \/ __ \|   |  \    < \___  (  <_> )  |  /")
	print("    |____|   |___|  (____  /___|  /__|_ \/ ____|\____/|____/ ")
	print("                  \/     \/     \/     \/\/                  ")
	print("       FOLLOW [ J O P R A V E E N ] FOR MORE COOL STUFFS")
	
