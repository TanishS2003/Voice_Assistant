This project creates a personal assistant named Jarvis using Python. It utilizes various libraries like pyttsx3, SpeechRecognition,
wikipedia, webbrowser, and PyQt5 for functionalities like text-to-speech, speech-to-text, web search, opening applications, and email/message
sending. Additionally, it incorporates a graphical user interface (GUI) using PyQt5 for a more interactive experience.

Before running the program, make sure you have the required Python libraries installed. You can install them using the following command:
pip install pyttsx3 speech_recognition requests wikipedia webbrowser pywhatkit smtplib pyjokes bs4 PyQt5 twilio


Features:
1. Voice Commands: Communicate with Jarvis using voice commands.
2. Open Applications: Open Notepad, Word, PowerPoint, Excel, and more.
3. Take Notes: Make and open notes using voice commands.
4. Play Music: Play random music from a specified directory.
5. Get IP Address: Fetch the public IP address.
6. Wikipedia Search: Search and retrieve information from Wikipedia.
7. Open Websites: Open YouTube, Google, and search Google.
8. Send Messages: Send WhatsApp messages to contacts.
9. YouTube Playback: Play videos on YouTube.
10. Send Emails: Send emails to contacts.
11. Tell Jokes: Jarvis can entertain you with jokes.
12. Read News: Get the latest news headlines.
13. Perform Calculations: Perform basic arithmetic calculations.
14. Check Weather: Retrieve the current temperature in a specified location.
15. Google Calendar Integration: Check your schedule for the day.
16. Make Calls: Make test calls using Twilio.


Customization:
1. Email Configuration: Set up your email credentials in the sendEmail function.
2. Contact Information: Add or modify contacts in the EMAIL_DIC and NUMBERS dictionaries.
3. Twilio Configuration: Set up your Twilio account SID, auth token, and phone numbers in the call function.
4. Google Calendar Integration: Update the GoogleCalendar module with your Google Calendar API credentials.


Usage:
1. Wake Commands: Use "Hey Jarvis" or "Hello Jarvis" to activate the voice assistant.
2. Command List: Refer to the code or documentation for a list of available voice commands.

Happy coding with Jarvis! 🚀
