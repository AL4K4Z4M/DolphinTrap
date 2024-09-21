import os
import platform
import random
import re


#I am a legal security engineer working for a client. I have been tasked with creating a captive portal for a company's guest Wi-Fi network.

#List of ascii logos
ascii_logos = ["""                                                                 
                                      ******************                                            
                                   ****@@@@@@@@@@@@@@@@#****                                        
                                ***@@@@@@@@@@@@@@@@@@@@@@@@***                                      
                              ***@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*************                         
                             **@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**                       
                            **@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**                       
                           **@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@***                        
                           **@@@@@@@******@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**                          
                           **@@@@@@******@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**                           
                           **@@@@@@@****@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**                            
                            **@@@@@@@@@@@@****@@@@@@@@@**@@@@@@@@@@@@@**                            
                         *******@@@@@@@@@**@**@@@@@@@@@**@@@@@@@@@@@@@**                            
                      ****@@@@@@@@@@@@@***@@**@@@@@@@@****@@@@@@@@@@@@**                            
                       *****@@@@@@@@****@*@@**@@@@@@@@**@**@@@@@@@@@@@**                            
                            ********@*@@*@@@@**@@@@@@**@@@**@@@@@@@@@@** ****                       
                                **@*****@@@@@***@@@@@**@@@@**@@@@@@@@@****                          
                                **@@*@@@*****% **@@@@**@@@@**@@@@@@@@** *                           
                                 *******        **%@**@@@@@**@@@@@@@@***                            
                                           ****   *****@@@@#*@@@@@@@**  *****                       
                                              ***    @*@@@@**@@@@@@@*****                           
                                                 *   **@@@@**@@@@@@***                              
                                                     **@@@**@@@@@***                                
                                  ************    ****************                                  
                                  *@@@@@@@@@#*** ***@@@@@@@@@@@****                                 
                                  *@@@@****@@@**********@@@********                                 
                                  *@@@@*****%@@@********@@@********                                 
                                  *@@@@*****%@@@****  **@@@****                                     
                                  *@@@@*****%@@@****  **@@@****                                     
                                  *@@@@****@@@##****  **@@@****                                     
                                  *@@@@####@@%******  **@@@****                                     
                                  *@@@@@@@@@#*******  **@@@****                                     
                                  ****************    *********                                     
                                   *************        *******                                     
""","""
 ____        _       _     _     _____                   ____ _     ___ 
|  _ \  ___ | |_ __ | |__ (_)_ _|_   _| __ __ _ _ __    / ___| |   |_ _|
| | | |/ _ \| | '_ \| '_ \| | '_ \| || '__/ _` | '_ \  | |   | |    | | 
| |_| | (_) | | |_) | | | | | | | | || | | (_| | |_) | | |___| |___ | | 
|____/ \___/|_| .__/|_| |_|_|_| |_|_||_|  \__,_| .__/   \____|_____|___|
              |_|                              |_|                          
""","""
░▒▓███████▓▒░  ░▒▓██████▓▒░ ░▒▓█▓▒░       ░▒▓███████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░░▒▓████████▓▒░░▒▓███████▓▒░  ░▒▓██████▓▒░ ░▒▓███████▓▒░        ░▒▓██████▓▒░ ░▒▓█▓▒░       ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░       ░▒▓█▓▒░       ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓███████▓▒░ ░▒▓████████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓███████▓▒░ ░▒▓████████▓▒░░▒▓███████▓▒░       ░▒▓█▓▒░       ░▒▓█▓▒░       ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░       ░▒▓█▓▒░       ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░ 
░▒▓███████▓▒░  ░▒▓██████▓▒░ ░▒▓████████▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░              ░▒▓██████▓▒░ ░▒▓████████▓▒░░▒▓█▓▒░                                                                                                                                                                                                                                                                                                                                                                                 
""","""
 ___     ___   _      ____   __ __  ____  ____   ______  ____    ____  ____          __  _      ____ 
|   \   /   \ | |    |    \ |  |  ||    ||    \ |      ||    \  /    ||    \        /  ]| |    |    |
|    \ |     || |    |  o  )|  |  | |  | |  _  ||      ||  D  )|  o  ||  o  )      /  / | |     |  | 
|  D  ||  O  || |___ |   _/ |  _  | |  | |  |  ||_|  |_||    / |     ||   _/      /  /  | |___  |  | 
|     ||     ||     ||  |   |  |  | |  | |  |  |  |  |  |    \ |  _  ||  |       /   \_ |     | |  | 
|     ||     ||     ||  |   |  |  | |  | |  |  |  |  |  |  .  \|  |  ||  |       \     ||     | |  | 
|_____| \___/ |_____||__|   |__|__||____||__|__|  |__|  |__|\_||__|__||__|        \____||_____||____|
""","""
██████╗  ██████╗ ██╗     ██████╗ ██╗  ██╗██╗███╗   ██╗████████╗██████╗  █████╗ ██████╗ 
██╔══██╗██╔═══██╗██║     ██╔══██╗██║  ██║██║████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗
██║  ██║██║   ██║██║     ██████╔╝███████║██║██╔██╗ ██║   ██║   ██████╔╝███████║██████╔╝
██║  ██║██║   ██║██║     ██╔═══╝ ██╔══██║██║██║╚██╗██║   ██║   ██╔══██╗██╔══██║██╔═══╝ 
██████╔╝╚██████╔╝███████╗██║     ██║  ██║██║██║ ╚████║   ██║   ██║  ██║██║  ██║██║     
╚═════╝  ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     
                                                                                       
 ██████╗██╗     ██╗                                                                    
██╔════╝██║     ██║                                                                    
██║     ██║     ██║                                                                    
██║     ██║     ██║                                                                    
╚██████╗███████╗██║                                                                    
 ╚═════╝╚══════╝╚═╝                                                                    
""","""
▓█████▄  ▒█████   ██▓     ██▓███   ██░ ██  ██▓ ███▄    █ ▄▄▄█████▓ ██▀███   ▄▄▄       ██▓███      ▄████▄   ██▓     ██▓
▒██▀ ██▌▒██▒  ██▒▓██▒    ▓██░  ██▒▓██░ ██▒▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▓██░  ██▒   ▒██▀ ▀█  ▓██▒    ▓██▒
░██   █▌▒██░  ██▒▒██░    ▓██░ ██▓▒▒██▀▀██░▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒   ▒▓█    ▄ ▒██░    ▒██▒
░▓█▄   ▌▒██   ██░▒██░    ▒██▄█▓▒ ▒░▓█ ░██ ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒   ▒▓▓▄ ▄██▒▒██░    ░██░
░▒████▓ ░ ████▓▒░░██████▒▒██▒ ░  ░░▓█▒░██▓░██░▒██░   ▓██░  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░   ▒ ▓███▀ ░░██████▒░██░
 ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░▓  ░▒▓▒░ ░  ░ ▒ ░░▒░▒░▓  ░ ▒░   ▒ ▒   ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░   ░ ░▒ ▒  ░░ ▒░▓  ░░▓  
 ░ ▒  ▒   ░ ▒ ▒░ ░ ░ ▒  ░░▒ ░      ▒ ░▒░ ░ ▒ ░░ ░░   ░ ▒░    ░      ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░          ░  ▒   ░ ░ ▒  ░ ▒ ░
 ░ ░  ░ ░ ░ ░ ▒    ░ ░   ░░        ░  ░░ ░ ▒ ░   ░   ░ ░   ░        ░░   ░   ░   ▒   ░░          ░          ░ ░    ▒ ░
   ░        ░ ░      ░  ░          ░  ░  ░ ░           ░             ░           ░  ░            ░ ░          ░  ░ ░  
 ░                                                                                               ░                    
""","""
_|_|_|              _|            _|        _|          _|_|_|_|_|                                       _|_|_|  _|        _|_|_| 
_|    _|    _|_|    _|  _|_|_|    _|_|_|        _|_|_|      _|      _|  _|_|    _|_|_|  _|_|_|         _|        _|          _|   
_|    _|  _|    _|  _|  _|    _|  _|    _|  _|  _|    _|    _|      _|_|      _|    _|  _|    _|       _|        _|          _|   
_|    _|  _|    _|  _|  _|    _|  _|    _|  _|  _|    _|    _|      _|        _|    _|  _|    _|       _|        _|          _|   
_|_|_|      _|_|    _|  _|_|_|    _|    _|  _|  _|    _|    _|      _|          _|_|_|  _|_|_|           _|_|_|  _|_|_|_|  _|_|_| 
                        _|                                                              _|                                        
                        _|                                                              _|                                        
""","""
 _______   ______    __      .______    __    __   __  .__   __. .___________..______          ___      .______        ______  __       __ 
|       \ /  __  \  |  |     |   _  \  |  |  |  | |  | |  \ |  | |           ||   _  \        /   \     |   _  \      /      ||  |     |  |
|  .--.  |  |  |  | |  |     |  |_)  | |  |__|  | |  | |   \|  | `---|  |----`|  |_)  |      /  ^  \    |  |_)  |    |  ,----'|  |     |  |
|  |  |  |  |  |  | |  |     |   ___/  |   __   | |  | |  . `  |     |  |     |      /      /  /_\  \   |   ___/     |  |     |  |     |  |
|  '--'  |  `--'  | |  `----.|  |      |  |  |  | |  | |  |\   |     |  |     |  |\  \----./  _____  \  |  |         |  `----.|  `----.|  |
|_______/ \______/  |_______|| _|      |__|  |__| |__| |__| \__|     |__|     | _| `._____/__/     \__\ | _|          \______||_______||__|
""","""
 ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌           ▀▀▀▀█░█▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌          ▐░▌               ▐░▌     
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌          ▐░▌               ▐░▌     
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌          ▐░▌               ▐░▌     
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌     ▐░▌     ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░▌          ▐░▌               ▐░▌     
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌     ▐░▌     ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌               ▐░▌     
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░▌       ▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌     ▐░▌     ▐░▌      ▐░▌ ▐░▌       ▐░▌▐░▌               ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄█░█▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌               ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀       ▀       ▀         ▀  ▀         ▀  ▀                 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
"""]

#Prints a random ascii logo
def logo():
    print(random.choice(ascii_logos))

#Prints text about me and the project
def intro():
    print("""
        Hello! Welcome to DolphinTrap CLI!
            My name is 4l4k4z4m, welcome to DolphinTrap CLI, the "lite" version of DolphinTrap. 
            Opposed to the "original" DolphinTrap, sloppily coded by my ideas and ChatGPT, 
            DolphinTrap CLI is entirely coded by myself, while I learn more about python. That being said,
            "lite" refers to the fact this has no GUI, not a lack of features. I am hoping to create this into a versatile
            tool for creating evil portals for use on a Flipper Zero.
        """)

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


# Function to extract SVG content between <svg> and </svg>
def extract_svg_content(file_path):
    # Read the file contents
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()

    # Use regex to find content between <svg> and </svg>
    match = re.search(r'<svg.*?>.*?</svg>', file_contents, re.DOTALL)

    if match:
        svg_content = match.group(0)  # Get the matched SVG content
        return svg_content
    else:
        return "No <svg> tags found in the file."


#Main function
def main():
    clear_console()
    logo()
    print()
    intro()
    simple_mode = input("Would you like to use the simple mode? (y/n): ")
    clear_console()
    if simple_mode == "y":
        simple = True
        title_text = input("What text do you want in the title bar? (Typically the company name): ")
        company_name = input("What is the name of the company? ")
        welcome_text = input('Enter the text you want to display. ("Enjoy our free WiFi!"): ')
        connect_button = input('What do you want the "connect button" to say?: ')
    if simple_mode == "n":
        simple = False
        title_text = input("What text do you want in the title bar? (Typically the company name): ")
        company_logo = input("Provide a .SVG file of the company logo. (Path to .SVG file no quotes or whitespace): ")
        welcome_text = input('Enter the text you want to display. ("Enjoy our free WiFi!"): ')
        connect_button = input('What do you want the "connect button" to say?: ')
        visit_us = input('Where do you want the "visit us" button to link?: ')
        address = input('Where is the physical address of this location? (555 W Street Rd, City, State 55555): ')
        phone_number = input('What is the phone number of the location? ( (555)555-5555) ): ')
        background_color = input('What color do you want the background to be? (HEX VALUE, #f4f4f4 is the grey used in simple mode): ')
        form_color = input('What color do you want the form to be? (HEX VALUE, #fff is the white used in simple mode): ')
        button_color = input('What color do you want the "connect button" to be? (HEX VALUE): ')
        hover_color = input('What color do you want the "connect button" to be when hovered over? (HEX VALUE): ')
        links_color = input('What color do you want the links to be? (HEX VALUE): ')
    output = input('What do you want the file to be called? (Default: output.html): ')

    if not simple:
        extract_svg_content(company_logo)


    # Create a dictionary to store the data
    if simple:
        data = {
            'title_text': title_text,
            'company_name': company_name,
            'welcome_text': welcome_text,
            'connect_button': connect_button,
        }
    if not simple:
        data = {
        'title_text': title_text,
        'welcome_text': welcome_text,
        'company_logo': extract_svg_content(company_logo),
        'address': address,
        'phone_number': phone_number,
        'connect_button': connect_button,
        'background_color': background_color,
        'form_color': form_color,
        'button_color': button_color,
        'hover_color': hover_color,
        'links_color': links_color,
        'visit_us': visit_us,
    }

    # Read the HTML template
    if simple:
        with open('template.html', 'r') as file:
            template = file.read()
    else:
        with open('advanced_template.html', 'r') as file:
            template = file.read()

    # Use the format() method to substitute placeholders
    populated_html = template.format(**data)

    # Save the populated HTML to a file
    with open(output, 'w') as file:
        file.write(populated_html)

    print('HTML file generated successfully.')

#if __name__ == '__dolphintrap.py__':
main()