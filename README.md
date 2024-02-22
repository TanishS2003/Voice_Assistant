This project creates a personal assistant named Jarvis using Python. It utilizes various libraries like pyttsx3, SpeechRecognition,
wikipedia, webbrowser, and PyQt5 for functionalities like text-to-speech, speech-to-text, web search, opening applications, and email/message
sending. Additionally, it incorporates a graphical user interface (GUI) using PyQt5 for a more interactive experience.

Before running the program, make sure you have the required Python libraries installed. You can install them using the following command:
pip install pyttsx3 speech_recognition requests wikipedia webbrowser pywhatkit smtplib pyjokes bs4 PyQt5 twilio


Features:
Voice Commands: Communicate with Jarvis using voice commands.
Open Applications: Open Notepad, Word, PowerPoint, Excel, and more.
Take Notes: Make and open notes using voice commands.
Play Music: Play random music from a specified directory.
Get IP Address: Fetch the public IP address.
Wikipedia Search: Search and retrieve information from Wikipedia.
Open Websites: Open YouTube, Google, and search Google.
Send Messages: Send WhatsApp messages to contacts.
YouTube Playback: Play videos on YouTube.
Send Emails: Send emails to contacts.
Tell Jokes: Jarvis can entertain you with jokes.
Read News: Get the latest news headlines.
Perform Calculations: Perform basic arithmetic calculations.
Check Weather: Retrieve the current temperature in a specified location.
Google Calendar Integration: Check your schedule for the day.
Make Calls: Make test calls using Twilio.


Customization:
Email Configuration: Set up your email credentials in the sendEmail function.
Contact Information: Add or modify contacts in the EMAIL_DIC and NUMBERS dictionaries.
Twilio Configuration: Set up your Twilio account SID, auth token, and phone numbers in the call function.
Google Calendar Integration: Update the GoogleCalendar module with your Google Calendar API credentials.


Usage:
Wake Commands: Use "Hey Jarvis" or "Hello Jarvis" to activate the voice assistant.
Command List: Refer to the code or documentation for a list of available voice commands.

Happy coding with Jarvis! 🚀
