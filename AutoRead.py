from .. import loader 
from asyncio import sleep 
 
@loader.tds 
class AutoReadMod(loader.Module): 
    """Модуль, который показывает, что ты в сети. Сам читает все сообщения в чатах, каналах и лс.""" 
    strings = {'name': 'Auto read'} 
 
    async def client_ready(self, client, db): 
        self.db = db 
 
    async def autoreadcmd(self, message): 
        """Включить/выключить режим AutoRead.""" 
        if not self.db.get("Auto read", "status"): 
            self.db.set("Auto read", "status", True) 
            await message.edit("<b>[AutoRead]</b> Включён.") 
            while self.db.get("Auto read", "status"): 
                msg = await message.client.send_message("me", "Telegram best messenger!")
                await msg.delete()
                await sleep(60) 
 
        else: 
            self.db.set("Auto read", "status", False) 
            await message.edit("<b>[AutoRead]</b> Выключен.")

    async def watcher(self, message): 
        if self.db.get("Auto read", "status"):
            await message.client.send_read_acknowledge(message.chat_id, clear_mentions=True)
