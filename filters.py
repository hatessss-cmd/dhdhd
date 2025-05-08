from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from config import *


class IsGroup(BoundFilter):

    async def check(self, message: types.Message):
        return message.chat.type in (types.ChatType.GROUP,
                                     types.ChatType.SUPERGROUP)

class IsPrivate(BoundFilter):

    async def check(self, message: types.Message):
        return message.chat.type in (types.ChatType.PRIVATE)


class IsChannel(BoundFilter):
    async def check(self, message: types.Message):
        print(message.chat.id)
        return str(message.chat.id) in str(CHANNEL_ID)


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        return message.from_user.id in ALL_ADMINS
