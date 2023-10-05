from aiogram import Bot, Dispatcher, types, executor
from homework.config import token
from logging import basicConfig, INFO

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO) 

start_keyboards= [
    types.KeyboardButton("About us"),
    types.KeyboardButton("Courses"),
    types.KeyboardButton("Schedule"),
    types.KeyboardButton("Adress")
]
start_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_keyboards)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Helo, {message.from_user.full_name}", reply_markup=start_button)
    print(message)

@dp.message_handler(text="About us")
async def about(message:types.Message):
    await message.answer("""Образовательный центр Geeks (Гикс) был основан Fullstack-разработчиком Айдаром Бакировым 
и Android-разработчиком Нургазы Сулаймановым в 2018-ом году в Бишкеке с целью дать возможность каждому человеку, даже без опыта в технологиях,
гарантированно освоить IT-профессию. На сегодняшний день более 1200 студентов в возрасте от 12 до 45 лет изучают здесь самые популярные
и востребованные IT-профессии. Филиальная сеть образовательного центра представлена в таких городах, как Бишкек, Ош и Кара-Балта.""")
    
@dp.message_handler(text="Schedule")
async def about(message:types.Message):
    await message.answer(f"{message.from_user.username}\nOur schedule: Mon-Sat 10:00 AM-22:00 PM")

@dp.message_handler(text="Adress")
async def about(message:types.Message):
    await message.answer(f"{message.from_user.username}\nOur adress: Mirzaly Amatova 1B(BC Tomiris)")
    await message.answer_location(40.51927293359835, 72.80298008693217)

executor.start_polling(dp)