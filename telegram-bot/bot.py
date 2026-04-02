import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message


async def echo(message: Message) -> None:
    await message.answer(message.text)


async def my_command(message: Message) -> None:
    await message.answer("my command handler")


async def main() -> None:
    dp = Dispatcher()
    dp.message.register(my_command, Command("my_command"))
    dp.message.register(echo, F.text)

    bot = Bot(token="TELEGRAM_BOT_TOKEN")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
