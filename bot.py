import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import CommandStart, Command
from random import choice

TOKEN = "8035596290:AAF1c1NpO33oKQvNC8kq1cDz4P8FeK6hBpo"

dp = Dispatcher()
bot = Bot(token=TOKEN)

# Наш список слов
WORDS_LIST = [
    "Путешествие",
    "Радость",
    "Любовь",
    "Свобода",
    "Мир",
    "Счастье",
    "Красота",
    "Дружба",
    "Искусство",
    "Природа"
]

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Привет! Отправьте /word, чтобы увидеть случайное слово.")

@dp.message(Command(commands=["word"]))
async def send_random_word(message: types.Message):
    word = choice(WORDS_LIST)
    await message.reply(word)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())