import asyncio
from telethon import TelegramClient
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

API_ID =   
API_HASH = ''  

async def main():
    client = TelegramClient('brother_session', API_ID, API_HASH)
    await client.start()  

    logging.info("Listing all accessible channels:")
    async for dialog in client.iter_dialogs():
        if dialog.is_channel:
            username = dialog.entity.username if hasattr(dialog.entity, 'username') else 'None (Private)'
            logging.info(f"Channel Name: {dialog.title}, ID: {dialog.id}, Username: @{username}")

    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
