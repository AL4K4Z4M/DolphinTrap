import os
import time
import platform
import random
import re
import webbrowser
from io import text_encoding
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

import customtkinter

root = customtkinter.CTk()
root.title("DolphinTrap GUI")
root.geometry("800x950")
root.title("DolphinTrap GUI")
root.iconbitmap("dolphin_trap_gui.ico")
root.resizable(False, False)


root.grid_columnconfigure(0, weight=1)

# Labels for messages (success and error)
message_label = customtkinter.CTkLabel(root, text="In progress. If you hit submit and it still says this, something is wrong", font=('Helvetica',20), text_color='red', fg_color=None)
message_label.grid(row=14, column=0, padx=20, pady=10, sticky="ew")

def callback(url):
   webbrowser.open_new_tab(url)

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


def create_html():
    # Read the HTML template
    with open('advanced_template.html', 'r') as file:
        template = file.read()

    # Use the format() method to substitute placeholders
    populated_html = template.format(**gui_data)

    file_name = output_file_name.get()
    # Save the populated HTML to a file
    with open(file_name, 'w') as file:
        file.write(populated_html)

    # Labels for messages (success and error)
    message_label = customtkinter.CTkLabel(root,text="HTML Generation Complete.",font=('Helvetica', 20), text_color='green', fg_color=None)
    message_label.grid(row=14, column=0, padx=20, pady=10, sticky="ew")


# Function to store data into the dictionary
def store_data(key, value):
    gui_data[key] = value
    print(f"Stored {key}: {value}")
    print("Current gui_data:", gui_data)


# Function to capture data from all entry fields
def submit_all_data():
    store_data('title_text', gui_title.get())
    store_data('company_logo', extract_and_modify_svg(gui_company_logo.get(), 200, 200))
    store_data('company_name', gui_company_name.get())
    store_data('welcome_text', gui_welcome_text.get())
    store_data('connect_button', gui_connect_button_text.get())
    store_data('address', gui_company_address.get())
    store_data('phone_number', gui_company_phone.get())
    store_data('connect_button_color', connect_button_color.get())
    store_data('connect_button_hover_color', connect_button_hover_color.get())
    store_data('output_file_name', output_file_name.get())
    create_html()
# Dictionary to store the data
gui_data = {
        'title_text': "",
        'welcome_text': "",
        'company_logo': "",
        'address': "",
        'phone_number': "",
        'connect_button': "",
        'background_color': '#f4f4f4',
        'form_color': '#fff',
        'button_color': "",
        'hover_color': "",
        'links_color': '#0000EE',
        'website': '',
        'website_text': ' Us',
        'footer_1_text': 'Terms of Service',
        'footer_1': 'tos',
        'footer_2_text': 'Privacy_Policy',
        'footer_2': 'privacy',
        'footer_3_text': 'Contact Us',
        'footer_3': 'contactus',
        'footer_4_text': 'FAQ',
        'footer_4' : 'faq',
        'output_file_name': ""
}

#Title of the APP
app_title = customtkinter.CTkLabel(root, font=('system',40, 'bold',), text_color='orange', text="D o l p i n   T r a p   G U I", wraplength=1200)
app_title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Entry 1: Title Bar
gui_title = customtkinter.CTkEntry(root, font=('system',20, 'bold'), text_color='orange', width=50, placeholder_text="What text do you want in the title bar? (Typically the company name): ")
gui_title.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

# Entry 2: Company Logo
gui_company_logo = customtkinter.CTkEntry(root, font=('system',20, 'bold'), text_color='orange', width=50, placeholder_text="Provide a .SVG file of the company logo. (Path to .SVG file no quotes or whitespace): ")
gui_company_logo.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

#Entry 3 Company Name
gui_company_name = customtkinter.CTkEntry(root, font=('system',20, 'bold'), text_color='orange', width=50, placeholder_text="What is the name of the company?")
gui_company_name.grid(row=5, column=0, padx=20, pady=20, sticky="ew")

#Entry 4 Welcome Text
gui_welcome_text = customtkinter.CTkEntry(root, font=('system',20, 'bold'), text_color='orange', width=50, placeholder_text='Enter the text you want to display. ("Enjoy our free WiFi!"): ')
gui_welcome_text.grid(row=6, column=0, padx=20, pady=20, sticky="ew")

#Entry 5 Connect Button Text
gui_connect_button_text = customtkinter.CTkEntry(root, font=('system',20, 'bold'), text_color='orange', width=50, placeholder_text='Enter the text you want to display on the connect button. ("Connect"): ')
gui_connect_button_text.grid(row=7, column=0, padx=20, pady=20, sticky="ew")

#Entry 6 Company Address
gui_company_address = customtkinter.CTkEntry(root, font=('system',20, 'bold'), text_color='orange', width=50, placeholder_text="Enter the address of the company: ")
gui_company_address.grid(row=8, column=0, padx=20, pady=20, sticky="ew")

#Entry 7 Company Phone Number
gui_company_phone = customtkinter.CTkEntry(root, font=('system',20, 'bold'), text_color='orange', width=50, placeholder_text="Enter the phone number of the company: ")
gui_company_phone.grid(row=9, column=0, padx=20, pady=20, sticky="ew")

#Entry 8 Connect Button Color
connect_button_color = customtkinter.CTkEntry(root, font=('system',20, 'bold'), text_color='orange', width=50, placeholder_text="Enter the color of the connect button: (HEX)")
connect_button_color.grid(row=10, column=0, padx=20, pady=20, sticky="ew")

#Entry 9 Connect Button Hover Color
connect_button_hover_color = customtkinter.CTkEntry(root, font=('system',20, 'bold'), text_color='orange', width=50, placeholder_text="Enter the hover color of the connect button: (HEX)")
connect_button_hover_color.grid(row=11, column=0, padx=20, pady=20, sticky="ew")

#Entry 10 Output File Name
output_file_name = customtkinter.CTkEntry(root, font=('system',20, 'bold'), text_color='orange', width=50, placeholder_text="Enter the name of the output file: ")
output_file_name.grid(row=12, column=0, padx=20, pady=20, sticky="ew")

# Single button to submit all entry data
submit_all_button = customtkinter.CTkButton(root, font=('system',30), text="Submit All", fg_color="#e88004", text_color='black', command=submit_all_data)
submit_all_button.grid(row=13, column=0, padx=20, pady=20, sticky="ew")

# Labels for messages (success and error)
message_label = customtkinter.CTkLabel(root, font=('Arial',15,'underline'), text="I am AL4K4Z4M, the developer of DolphinTrap. Please consider checking out my github.", fg_color=None)
message_label.bind("<Button-1>", lambda e: callback("https://github.com/AL4K4Z4M"))
message_label.grid(row=15, column=0, padx=20, pady=10, sticky="ew")


root.mainloop()