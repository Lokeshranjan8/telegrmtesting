from telethon.sync import TelegramClient
import gitignore as gi 

api_id = gi.api_id
api_hash = gi.api_hash
phone_number = gi.phone_number


client=TelegramClient('present', api_id, api_hash)

async def connect_telegram():
    await client.start(phone=phone_number)
    print('Connected to Telegram')
    

with client:
    client.loop.run_until_complete(connect_telegram())



# users data specific friends
async def fetch_user_info(username):
    user = await client.get_entity(username)
    print(f"User details: {user.first_name} {user.last_name}, Username: {user.username}")

username = "Its_altR" 
with client:
    client.loop.run_until_complete(fetch_user_info(username))



# fetch messages
async def fetch_messages(username):
    async for message in client.iter_messages(username, limit=100):  # Fetch last 100 messages
        print(f"[{message.date}] {message.sender_id}: {message.text}")

with client:
    client.loop.run_until_complete(fetch_messages(username))




# //groups fetch
async def fetch_user_groups():
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if dialog.is_group or dialog.is_channel:
            print(f"Group/Channel: {dialog.name} (ID: {dialog.id})")

with client:
    client.loop.run_until_complete(fetch_user_groups())



# media
async def download_media(username):
    async for message in client.iter_messages(username):
        if message.media:
            print(f"Downloading media from message {message.id}")
            await message.download_media(file=f"media_{message.id}")

# Example usage
with client:
    client.loop.run_until_complete(download_media(username))
