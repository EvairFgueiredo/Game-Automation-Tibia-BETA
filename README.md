# Game-Automation-Tibia-BETA
Code Description This project consists of a Python script intended to automate interactions in Tibia, apparently using the PyAutoGUI and PySimpleGUI libraries to create a simple graphical interface.

# Main Components and Features

# Graphical Interface:

The script uses the PySimpleGUI library to create three distinct graphical windows: one for login, another for bot options, and a third for the main bot settings. Each window features buttons and input fields to configure various options, such as hotkeys for attacks, mana regeneration, rings, food, among others.

# Automation of Actions:

The script incorporates automations for various in-game actions, including attacking enemies, using rings and food, regenerating mana and health, and a "Cavebot" for automatic exploration.

# Screen Operations:

It utilizes the PyAutoGUI library to perform computer vision-based operations, such as clicking on specific areas of the screen and checking for the presence of specific images.

# Threads for Parallel Operations:

The code employs threads to execute multiple operations simultaneously, such as mana regeneration, health regeneration, attack, item collection, among others.

# configuration and Image Paths:

It defines paths for images used in the script for visual recognition. It configures directories for images and uses lists of paths for different actions.

# Control of Tibia Window Opacity:

It implements a function to adjust the opacity of the Tibia game window using the PyGetWindow and ctypes libraries.

How to Use

Users can interact with the graphical interface to configure game options, hotkeys, and enable/disable different bot functionalities. Pressing the "Play!" button initiates threads to automatically perform the configured actions.

Notes

Ensure correct configuration of hotkeys and other parameters before running the script. The code is structured to allow easy expansion and modification of functionalities.

Requirements and Dependencies

The script requires the installation of Python libraries, such as PyAutoGUI, PySimpleGUI, PyGetWindow, and keyboard.

# Additional Note to Description:

Using with OBS Studio for Broadcasting

# Opacity for Integration with OBS Studio:

A key feature of this script is the ability to adjust the opacity of the Tibia game window. This functionality is designed to be used in conjunction with OBS Studio for live broadcasts. By configuring opacity, the Tibia window can be made nearly transparent, showing only the mirrored screen of OBS Studio during the broadcast. This is particularly useful for creating a more appealing and professional layout for your audience. Ensure careful adjustment of opacity settings to meet your specific needs during broadcasts.

# How to Set Up for OBS Studio:

# Run the Script:

Start the script and access the options window.
Use the "Opacity" function to adjust the transparency of the Tibia window.
# OBS Studio Settings:

In OBS Studio, add a "Window Capture" source and select the Tibia window.
Organize your sources and adjust transparency to overlay the mirrored Tibia screen onto the original Tibia screen.
# Final Adjustments:

Experiment with different opacity levels to achieve the desired effect.
Test the settings before starting a live broadcast to ensure a smooth experience for viewers.
# Important Notes:

# System Performance:

Consider your system's performance when using these settings, especially if broadcasting in high quality.
Monitor resource usage to ensure a stable broadcasting experience.
# Copyrights and Terms of Use:

Always respect the Terms of Service of Tibia and OBS Studio when using these settings for live broadcasts.
# Important Disclaimer:

Legal and Ethical Warning

This project is provided solely for educational and study purposes. The use of this script in online gaming environments may violate the Terms of Service of those games. The practice of using bots or automated scripts in online games may be considered illegal and result in penalties, including account bans.

Warning:

# Educational Purposes:

This script was developed as an educational project to explore concepts of automation and interaction with graphical interfaces. It should not be used to circumvent or violate rules of online games.
# Responsibility:

The author of this script is not responsible for any misuse or illegal use of this code. Users are entirely responsible for understanding and obeying the Terms of Service of the relevant online games.
# Ethics and Compliance:

The practice of using bots in online games can harm the gaming experience of other users and violate ethical principles. We encourage compliance with the rules and regulations established by game developers.
# Legal Consequences:

The use of bots in online games may result in legal actions by the game developers. We strongly recommend that users consider legal consequences before using this script in online gaming environments. By downloading and using this code, you agree to abide by all laws, regulations, and policies associated with the use of automated scripts in online games.
