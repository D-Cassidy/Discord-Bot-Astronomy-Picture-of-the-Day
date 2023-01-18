# Astronomy Picture of the Day: Discord Bot
A discord bot that posts the image, title, and explanation for the astronomy picture of the day every 24 hours.

# Instructions for Use
Create your own discord bot using the discord developer tools. (find instructions [here](https://realpython.com/how-to-make-a-discord-bot-python/))

Make a .env file in the same directory as bot.py with DISCORD_TOKEN={your bot's token}.

Change the channel id inside the code to the id of the specific text channel you want the bot to send messages in.

Run the bot from the console, leave it open and every 24 hours it will send the new APOD!

# Future Plans
Will try to allow interaction with the bod from within discord's channels so you can change which channel it sends messages in without editing the code. 

Possibly try to export the running of the bot to an external server, but that seems unnecessary for such a basic bot.
