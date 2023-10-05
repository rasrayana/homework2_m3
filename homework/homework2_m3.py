from aiogram import Bot, Dispatcher, types, executor
from config import token
from logging import basicConfig, INFO

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO) 

start_keyboards= [
    types.KeyboardButton("About us"),
    types.KeyboardButton("Objects"),
    types.KeyboardButton("Contacts"),
]
start_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_keyboards)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}", reply_markup=start_button)
    print(message)

@dp.message_handler(text="About us")
async def about(message:types.Message):
    await message.answer("""Мы - развивающаяся компания, которая предлагает своим клиентам широкий выбор квартир в объектах расположенных
во всех наиболее привлекательных районах городов Ош и Джалал-Абад. У нас максимально выгодные условия, гибкий (индивидуальный) подход при
реализации жилой и коммерческой недвижимости. Мы занимаем лидирующие позиции по количеству объектов по югу Кыргызстана.
Наша миссия: Мы обеспечиваем население удобным жильем для всей семьи, проявляя лояльность и индивидуальный подход и обеспечивая высокий
уровень обслуживания. Мы обеспечиваем бизнес подходящим коммерческим помещением, используя современные решения и опыт профессионалов своего дела.""")

@dp.message_handler(text="Objects")
async def about(message:types.Message):
    await message.answer("""
ЖК «Малина-Лайф»
ЖК «Томирис»
ЖК «Черемушки»
ЖК «Фрунзе»                
""")

@dp.message_handler(text="Contacts")
async def about(message:types.Message):
    await message.answer("""
Our contacts:
tel:+996709620088
tel:+996772620088
tel:+996550620088
""")

executor.start_polling(dp)