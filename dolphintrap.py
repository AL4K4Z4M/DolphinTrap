import os
import subprocess
import time
import platform
import random
import re
import customtkinter
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

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
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║    ___              __              _       __            ____                                ___      _        __   ║
║   F __".    ____    LJ   _ ___     FJ___    LJ   _ ___   /_  _\  _ ___    ___ _    _ ___    ,"___".   FJ        FJ   ║
║  J |--\ L  F __ J   FJ  J '__ J   J  __ `.      J '__ J  [J  L] J '__ ", F __` L  J '__ J   FJ---L]  J |       J  L  ║
║  | |  J | | |--| | J  L | |--| |  | |--| |  FJ  | |__| |  |  |  | |__|-J| |--| |  | |--| | J |   LJ  | |       |  |  ║
║  F L__J | F L__J J J  L F L__J J  F L  J J J  L F L  J J  F  J  F L  `-'F L__J J  F L__J J | \___--. F L_____  F  J  ║
║ J______/FJ\______/FJ__LJ  _____/LJ__L  J__LJ__LJ__L  J__LJ____LJ__L    J\____,__LJ  _____/LJ\_____/FJ________LJ____L ║
║ |______F  J______F |__||_J_____F |__L  J__||__||__L  J__||____||__L     J____,__F|_J_____F  J_____F |________||____| ║
║                        L_J                                                       L_J                                 ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""","""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║      ____            ___            __                  ______                       ____     __     ______          ║
║     /\  _`\         /\_ \          /\ \      __        /\__  _\                     /\  _`\  /\ \   /\__  _\         ║
║     \ \ \/\ \    ___\//\ \    _____\ \ \___ /\_\    ___\/_/\ \/ _ __    __     _____\ \ \/\_1\ \ \  \/_/\ \/         ║
║      \ \ \ \ \  / __``\ \ \  /\ '__`\ \  _ `\/\ \ /' _ `\ \ \ \/\`'__\/'__`\  /\ '__`\ \ \/_/_\ \ \  __\ \ \         ║
║       \ \ \_\ \/\ \L\ `\_\ \_\ \ \L\ \ \ \ \ \ \ \/\ \/\ \ \ \ \ \ \//\ \L\.\_\ \ \L\ \ \ \L\ `\ \ \L\ `\_\ \__      ║
║        \ \____/\ \____//\____`\ \ ,__/\ \_\ \_\ \_\ \_\ \_\ \ \_\ \_1\ \__/.\_`\ \ ,__/\ \____/ \ \____//\_____\     ║
║         \/___/  \/___/ \/____/ \ \ \/  \/_/\/_/\/_/\/_/\/_/  \/_/\/_/ \/__/\/_/ \ \ \/  \/___/   \/___/ \/_____/     ║
║                                 \ \_\                                            \ \_\                               ║
║                                  \/_/                                             \/_/                               ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""","""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║      ██████╗  ██████╗ ██╗     ██████╗ ██╗  ██╗██╗███╗   ██╗████████╗██████╗  █████╗ ██████╗  ██████╗██╗     ██╗      ║
║      ██╔══██╗██╔═══██╗██║     ██╔══██╗██║  ██║██║████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██║     ██║      ║
║      ██║  ██║██║   ██║██║     ██████╔╝███████║██║██╔██╗ ██║   ██║   ██████╔╝███████║██████╔╝██║     ██║     ██║      ║
║      ██║  ██║██║   ██║██║     ██╔═══╝ ██╔══██║██║██║╚██╗██║   ██║   ██╔══██╗██╔══██║██╔═══╝ ██║     ██║     ██║      ║
║      ██████╔╝╚██████╔╝███████╗██║     ██║  ██║██║██║ ╚████║   ██║   ██║  ██║██║  ██║██║     ╚██████╗███████╗██║      ║
║      ╚═════╝  ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝      ╚═════╝╚══════╝╚═╝      ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""","""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ ▓█████▄  ▒█████   ██▓     ██▓███   ██░ ██  ██▓ ███▄    █ ▄▄▄█████▓ ██▀███   ▄▄▄       ██▓███   ▄████▄   ██▓     ██▓  ║
║ ▒██▀ ██▌▒██▒  ██▒▓██▒    ▓██░  ██▒▓██░ ██▒▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▓██░  ██▒▒██▀ ▀█  ▓██▒    ▓██▒  ║
║ ░██   █▌▒██░  ██▒▒██░    ▓██░ ██▓▒▒██▀▀██░▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒▒▓█    ▄ ▒██░    ▒██▒  ║
║ ░▓█▄   ▌▒██   ██░▒██░    ▒██▄█▓▒ ▒░▓█ ░██ ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓▓▄ ▄██▒▒██░    ░██░  ║
║ ░▒████▓ ░ ████▓▒░░██████▒▒██▒ ░  ░░▓█▒░██▓░██░▒██░   ▓██░  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░▒ ▓███▀ ░░██████▒░██░  ║
║  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░▓  ░▒▓▒░ ░  ░ ▒ ░░▒░▒░▓  ░ ▒░   ▒ ▒   ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░░ ░▒ ▒  ░░ ▒░▓  ░░▓    ║
║  ░ ▒  ▒   ░ ▒ ▒░ ░ ░ ▒  ░░▒ ░      ▒ ░▒░ ░ ▒ ░░ ░░   ░ ▒░    ░      ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░       ░  ▒   ░ ░ ▒  ░ ▒ ░  ║
║  ░ ░  ░ ░ ░ ░ ▒    ░ ░   ░░        ░  ░░ ░ ▒ ░   ░   ░ ░   ░        ░░   ░   ░   ▒   ░░       ░          ░ ░    ▒ ░  ║
║    ░        ░ ░      ░  ░          ░  ░  ░ ░           ░             ░           ░  ░         ░ ░          ░  ░ ░    ║
║  ░                                                                                            ░                      ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""","""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║   .%%%%%....%%%%...%%......%%%%%...%%..%%..%%%%%%..%%..%%..%%%%%%..%%%%%....%%%%...%%%%%....%%%%...%%......%%%%%%.   ║
║   .%%..%%..%%..%%..%%......%%..%%..%%..%%....%%....%%%.%%....%%....%%..%%..%%..%%..%%..%%..%%..%%..%%........%%...   ║
║   .%%..%%..%%..%%..%%......%%%%%...%%%%%%....%%....%%.%%%....%%....%%%%%...%%%%%%..%%%%%...%%......%%........%%...   ║
║   .%%..%%..%%..%%..%%......%%......%%..%%....%%....%%..%%....%%....%%..%%..%%..%%..%%......%%..%%..%%........%%...   ║
║   .%%%%%....%%%%...%%%%%%..%%......%%..%%..%%%%%%..%%..%%....%%....%%..%%..%%..%%..%%.......%%%%...%%%%%%..%%%%%%.   ║
║   ................................................................................................................   ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""","""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║       ______   _____          _____  _     _ _____ __   _ _______  ______ _______  _____  _______        _____       ║
║       |     \ |     | |      |_____] |_____|   |   | \  |    |    |_____/ |_____| |_____] |       |        |         ║
║       |_____/ |_____| |_____ |       |     | __|__ |  \_|    |    |    \_ |     | |       |_____  |_____ __|__       ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""","""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ d8888b.  .d88b.  db      d8888b. db   db d888888b d8b   db d888888b d8888b.  .d8b.  d8888b.  .o88b. db      d888888b ║
║ 88  `8D .8P  Y8. 88      88  `8D 88   88   `88'   888o  88 `~~88~~' 88  `8D d8' `8b 88  `8D d8P  Y8 88        `88'   ║
║ 88   88 88    88 88      88oodD' 88ooo88    88    88V8o 88    88    88oobY' 88ooo88 88oodD' 8P      88         88    ║
║ 88   88 88    88 88      88~~~   88~~~88    88    88 V8o88    88    88`8b   88~~~88 88~~~   8b      88         88    ║
║ 88  .8D `8b  d8' 88booo. 88      88   88   .88.   88  V888    88    88 `88. 88   88 88      Y8b  d8 88booo.   .88.   ║
║ Y8888D'  `Y88P'  Y88888P 88      YP   YP Y888888P VP   V8P    YP    88   YD YP   YP 88       `Y88P' Y88888P Y888888P ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""","""
      ╔════════════════════════════════════════════════════════════════════════════════════════════════════════╗
      ║      ___     ___   _      ____  __ __  ____  ____   ______  ____    ____  ____    __  _      ____      ║
      ║     |   \   /   \ | |    |    \|  |  ||    ||    \ |      ||    \  /    ||    \  /  ]| |    |    |     ║
      ║     |    \ |     || |    |  o  )  |  | |  | |  _  ||      ||  D  )|  o  ||  o  )/  / | |     |  |      ║
      ║     |  D  ||  O  || |___ |   _/|  _  | |  | |  |  ||_|  |_||    / |     ||   _//  /  | |___  |  |      ║
      ║     |     ||     ||     ||  |  |  |  | |  | |  |  |  |  |  |    \ |  _  ||  | /   \_ |     | |  |      ║
      ║     |     ||     ||     ||  |  |  |  | |  | |  |  |  |  |  |  .  \|  |  ||  | \     ||     | |  |      ║
      ║     |_____| \___/ |_____||__|  |__|__||____||__|__|  |__|  |__|\_||__|__||__|  \____||_____||____|     ║
      ╚════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""]

#Prints text about me and the project
def intro():
    print(Fore.WHITE + Style.BRIGHT + """
                                        Hello! Welcome to DolphinTrap CLI!
                                This is a tool to generate captive portal HTML files.
                            This tool
        """)

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def next():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    print(Fore.YELLOW + Style.BRIGHT + logo)

# Function to extract SVG content and modify height and width
def extract_and_modify_svg(file_path, new_width, new_height):
    # Read the file contents
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()

    # Use regex to find the opening <svg> tag and capture its attributes
    svg_tag_match = re.search(r'(<svg\s.*?>)', file_contents, re.DOTALL)

    if svg_tag_match:
        svg_tag = svg_tag_match.group(1)  # Get the <svg> tag

        # Modify the width and height in the <svg> tag
        updated_svg_tag = re.sub(r'width="[^"]+"', f'width="{new_width}"', svg_tag)
        updated_svg_tag = re.sub(r'height="[^"]+"', f'height="{new_height}"', updated_svg_tag)

        # Replace the original <svg> tag with the updated one
        updated_file_contents = file_contents.replace(svg_tag, updated_svg_tag)

        # Return the updated SVG content
        return updated_file_contents
    else:
        return "No <svg> tag found in the file."

def simple_mode():
    next()
    title_text = input("What text do you want in the title bar? (Typically the company name): ")
    company_name = input("What is the name of the company? ")
    welcome_text = input('Enter the text you want to display. ("Enjoy our free WiFi!"): ')
    connect_button = input('What do you want the "connect button" to say?: ')
    output = input('What do you want the file to be called? (Default: output.html): ')

    data = {
        'title_text': title_text,
        'company_name': company_name,
        'welcome_text': welcome_text,
        'connect_button': connect_button,
    }

    # Read the HTML template
    with open('template.html', 'r') as file:
        template = file.read()

    # Use the format() method to substitute placeholders
    populated_html = template.format(**data)

    # Save the populated HTML to a file
    with open(output, 'w') as file:
        file.write(populated_html)

    print('Simple HTML file generated successfully.')

def pretty_mode():
    next()
    title_text = input("What text do you want in the title bar? (Typically the company name): ")
    next()
    company_logo = input("Provide a .SVG file of the company logo. (Path to .SVG file no quotes or whitespace): ")
    next()
    welcome_text = input('Enter the text you want to display. ("Enjoy our free WiFi!"): ')
    next()
    connect_button = input('What do you want the "connect button" to say?: ')
    next()
    address = input('Where is the physical address of this location? (555 W Street Rd, City, State 55555): ')
    next()
    phone_number = input('What is the phone number of the location? ( (555)555-5555) ): ')
    next()
    button_color = input('What color do you want the "connect button" to be? (HEX VALUE): ')
    next()
    hover_color = input('What color do you want the "connect button" to be when hovered over? (HEX VALUE): ')
    next()
    output = input('What do you want the file to be called? (Default: output.html): ')

    data = {
        'title_text': title_text,
        'welcome_text': welcome_text,
        'company_logo': extract_and_modify_svg(company_logo,'200','200'),
        'address': address,
        'phone_number': phone_number,
        'connect_button': connect_button,
        'background_color': '#f4f4f4',
        'form_color': '#fff',
        'button_color': button_color,
        'hover_color': hover_color,
        'links_color': '#0000EE',
        'website': 'visit_us',
        'website_text': 'Visit Us',
        'footer_1_text': 'Terms of Service',
        'footer_1': 'tos',
        'footer_2_text': 'Privacy_Policy',
        'footer_2': 'privacy',
        'footer_3_text': 'Contact Us',
        'footer_3': 'contact_us',
        'footer_4_text': 'FAQ',
        'footer_4' : 'faq',
    }

    # Read the HTML template
    with open('advanced_template.html', 'r') as file:
        template = file.read()

    # Use the format() method to substitute placeholders
    populated_html = template.format(**data)

    # Save the populated HTML to a file
    with open(output, 'w') as file:
        file.write(populated_html)

    print('Advanced HTML file generated successfully.')

def pretty_connected():
    next()
    title_text = input("What text do you want in the title bar? (Typically the company name): ")
    next()
    company_logo = input("Provide a .SVG file of the company logo. (Path to .SVG file no quotes or whitespace): ")
    next()
    welcome_text = input('Enter the text you want to display. ("Enjoy our free WiFi!"): ')
    next()
    connect_button = input('What do you want the "connect button" to say?: ')
    next()
    address = input('Where is the physical address of this location? (555 W Street Rd, City, State 55555): ')
    next()
    phone_number = input('What is the phone number of the location? ( (555)555-5555) ): ')
    next()
    website = input('Where do you want the "visit us" button to link?: ')
    next()
    footer_1 = input('Where do you want the "Terms of Service" button to link?: ')
    next()
    footer_2 = input('Where do you want the "Privacy Policy" button to link?: ')
    next()
    footer_3 = input('Where do you want the "FAQ" button to link?: ')
    next()
    footer_4 = input('Where do you want the "Contact Us" button to link?: ')
    next()
    button_color = input('What color do you want the "connect button" to be? (HEX VALUE): ')
    next()
    hover_color = input('What color do you want the "connect button" to be when hovered over? (HEX VALUE): ')
    next()
    output = input('What do you want the file to be called? (Default: output.html): ')

    data = {
        'title_text': title_text,
        'welcome_text': welcome_text,
        'company_logo': extract_and_modify_svg(company_logo,'200','200'),
        'address': address,
        'phone_number': phone_number,
        'connect_button': connect_button,
        'background_color': '#f4f4f4',
        'form_color': '#fff',
        'button_color': button_color,
        'hover_color': hover_color,
        'links_color': '#0000EE',
        'website_text': 'Visit Us',
        'website': website,
        'footer_1_text': 'Terms of Service',
        'footer_1': footer_1,
        'footer_2_text': 'Privacy_Policy',
        'footer_2': footer_2,
        'footer_3_text': 'Contact Us',
        'footer_3': footer_3,
        'footer_4_text': 'FAQ',
        'footer_4': footer_4,
    }

    # Read the HTML template
    with open('advanced_template.html', 'r') as file:
        template = file.read()

    # Use the format() method to substitute placeholders
    populated_html = template.format(**data)

    # Save the populated HTML to a file
    with open(output, 'w') as file:
        file.write(populated_html)

    print('Advanced HTML file generated successfully.')

def advanced_mode():
    next()
    title_text = input("What text do you want in the title bar? (Typically the company name): ")
    next()
    company_logo = input("Provide a .SVG file of the company logo. (Path to .SVG file no quotes or whitespace): ")
    next()
    svg_width = input('What width do you want the SVG logo to be? (200px): ')
    next()
    svg_height = input('What height do you want the SVG logo to be? (200px): ')
    next()
    welcome_text = input('Enter the text you want to display. ("Enjoy our free WiFi!"): ')
    next()
    connect_button = input('What do you want the "connect button" to say?: ')
    next()
    address = input('Where is the physical address of this location? (555 W Street Rd, City, State 55555): ')
    next()
    phone_number = input('What is the phone number of the location? ( (555)555-5555) ): ')
    next()
    website_text = input('What do you want the "Visit us" button to say?: ')
    next()
    footer_1_text = input('What do you want "Footer 1" to say?: ')
    next()
    footer_2_text = input('What do you want "Footer 2" to say?: ')
    next()
    footer_3_text = input('What do you want "Footer 3" to say?: ')
    next()
    footer_4_text = input('What do you want "Footer 4" to say?: ')
    next()
    background_color = input(
        'What color do you want the background to be? (HEX VALUE, #f4f4f4 is the grey used in simple mode): ')
    next()
    form_color = input('What color do you want the form to be? (HEX VALUE, #fff is the white used in simple mode): ')
    next()
    button_color = input('What color do you want the "connect button" to be? (HEX VALUE): ')
    next()
    hover_color = input('What color do you want the "connect button" to be when hovered over? (HEX VALUE): ')
    next()
    links_color = input('What color do you want the links to be? (HEX VALUE): ')
    next()
    output = input('What do you want the file to be called? (Default: output.html): ')

    data = {
        'title_text': title_text,
        'welcome_text': welcome_text,
        'company_logo': extract_and_modify_svg(company_logo, svg_width, svg_height),
        'address': address,
        'phone_number': phone_number,
        'connect_button': connect_button,
        'background_color': background_color,
        'form_color': form_color,
        'button_color': button_color,
        'hover_color': hover_color,
        'links_color': links_color,
        'website_text': website_text,
        'website': 'website',
        'footer_1_text': footer_1_text,
        'footer_1': 'footer_1',
        'footer_2_text': footer_2_text,
        'footer_2': 'footer_2',
        'footer_3_text': footer_3_text,
        'footer_3': 'footer_3',
        'footer_4_text': footer_4_text,
        'footer_4' : 'footer_4',
    }



    # Read the HTML template
    with open('advanced_template.html', 'r') as file:
        template = file.read()

    # Use the format() method to substitute placeholders
    populated_html = template.format(**data)

    # Save the populated HTML to a file
    with open(output, 'w') as file:
        file.write(populated_html)

    print('Advanced HTML file generated successfully.')

def advanced_connected():
    next()
    title_text = input("What text do you want in the title bar? (Typically the company name): ")
    next()
    company_logo = input("Provide a .SVG file of the company logo. (Path to .SVG file no quotes or whitespace): ")
    next()
    svg_width = input('What width do you want the SVG logo to be? (200px): ')
    next()
    svg_height = input('What height do you want the SVG logo to be? (200px): ')
    next()
    welcome_text = input('Enter the text you want to display. ("Enjoy our free WiFi!"): ')
    next()
    connect_button = input('What do you want the "connect button" to say?: ')
    next()
    website_text = input('What do you want the "Visit us" button to say?: ')
    next()
    website = input('Where do you want the "Visit us" button to link?: ')
    next()
    address = input('Where is the physical address of this location? (555 W Street Rd, City, State 55555): ')
    next()
    phone_number = input('What is the phone number of the location? ( (555)555-5555) ): ')
    next()
    footer_1_text = input('What do you want "Footer 1" to say?: ')
    next()
    footer_1 = input('Where do you want the "Footer 1" button to link?: ')
    next()
    footer_2_text = input('What do you want "Footer 2" to say?: ')
    next()
    footer_2 = input('Where do you want the "Footer 2" button to link?: ')
    next()
    footer_3_text = input('What do you want "Footer 3" to say?: ')
    next()
    footer_3 = input('Where do you want the "Footer 3" button to link?: ')
    next()
    footer_4_text = input('What do you want "Footer 4" to say?: ')
    next()
    footer_4 = input('Where do you want the "Footer 4" button to link?: ')
    next()
    background_color = input(
        'What color do you want the background to be? (HEX VALUE, #f4f4f4 is the grey used in simple mode): ')
    next()
    form_color = input('What color do you want the form to be? (HEX VALUE, #fff is the white used in simple mode): ')
    next()
    button_color = input('What color do you want the "connect button" to be? (HEX VALUE): ')
    next()
    hover_color = input('What color do you want the "connect button" to be when hovered over? (HEX VALUE): ')
    next()
    links_color = input('What color do you want the links to be? (HEX VALUE): ')
    next()
    output = input('What do you want the file to be called? (Default: output.html): ')

    data = {
        'title_text': title_text,
        'welcome_text': welcome_text,
        'company_logo': extract_and_modify_svg(company_logo, svg_width, svg_height),
        'address': address,
        'phone_number': phone_number,
        'connect_button': connect_button,
        'background_color': background_color,
        'form_color': form_color,
        'button_color': button_color,
        'hover_color': hover_color,
        'links_color': links_color,
        'website_text': website_text,
        'website': website,
        'footer_1_text': footer_1_text,
        'footer_1': footer_1,
        'footer_2_text': footer_2_text,
        'footer_2': footer_2,
        'footer_3_text': footer_3_text,
        'footer_3': footer_3,
        'footer_4_text': footer_4_text,
        'footer_4': footer_4,
    }

    # Read the HTML template
    with open('advanced_template.html', 'r') as file:
        template = file.read()

    # Use the format() method to substitute placeholders
    populated_html = template.format(**data)

    # Save the populated HTML to a file
    with open(output, 'w') as file:
        file.write(populated_html)

    print('Advanced HTML file generated successfully.')

def art_mode():
    clear_console()
    for logo in ascii_logos:
        print(Fore.YELLOW + Style.BRIGHT + logo)
    return_from_art = input("Press enter to return to the main menu.")
    if return_from_art == "":
        clear_console()
        choose_trap_mode()
    else:
        clear_console()
        art_mode()

def choose_trap_mode():
    clear_console()
    global logo
    logo = random.choice(ascii_logos)
    print(Fore.YELLOW + Style.BRIGHT + logo)
    print("Choose a mode:")
    print()
    print(Fore.WHITE + Style.BRIGHT + "1. Basic Mode")
    print()
    print(Fore.MAGENTA + Style.BRIGHT + "2. Pretty Mode",Fore.MAGENTA + Style.BRIGHT +
          """       3. Pretty""",Fore.CYAN + Style.BRIGHT +"""Connected""")
    print()
    print(Fore.YELLOW + Style.BRIGHT + """4. Advanced Mode""",Fore.YELLOW + Style.BRIGHT +
          """     5. Advanced""",Fore.CYAN + Style.BRIGHT +"""Connected""")
    print()
    print(Fore.BLUE + Style.BRIGHT + "6. Art Mode")
    print()
    print(Fore.RED + Style.BRIGHT + "7. Exit")
    print()
    mode = input("Enter the number of the mode you would like to use: ")
    if mode == "1":
        simple_mode()
    elif mode == "2":
        pretty_mode()
    elif mode == "3":
        pretty_connected()
    elif mode == "4":
        advanced_mode()
    elif mode == "5":
        advanced_connected()
    elif mode == "6":
        art_mode()
    elif mode == "7":
        exit()
    elif mode == "":
        clear_console()
        choose_trap_mode()
    else:
        print(Fore.RED + Style.BRIGHT + "Invalid input. Please enter a valid number.")
        time.sleep(3)
        clear_console()
        choose_trap_mode()

#Main function
def main():
    clear_console()
    gui = input("Would you like to use the GUI? (Y/N): ")
    if gui.lower() == "y":
        print("Too bad! It's Still in development!")
        clear_console()
        intro()
        choose_trap_mode()
    elif gui.lower() == "n":
        clear_console()
        intro()
        choose_trap_mode()
    else :
        print(Fore.RED + Style.BRIGHT + "Invalid input. Please enter Y or N.")
        time.sleep(3)
        clear_console()
        main()

#if __name__ == '__dolphintrap.py__'
if __name__ == '__main__':
    main()
