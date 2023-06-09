import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

# Muhim xabarlarni o'tkazib yubormaslik uchun loglarni sozlab, yoqib qo'yamiz
logging.basicConfig(level=logging.INFO)
# Bot obyekti
bot = Bot(token="6181573428:AAGFAgGRimL6qdBMyl8WWhl-pV6fjASMEdE")
# Bot uchun dispetcher
dp = Dispatcher(bot)


# Botga jo'natilgan /start buyrug'ini qabul qilib olish uchun handler
@dp.message_handler(commands='start')
async def start_cmd(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  # keyboard obyekti
    buttons = ['Bot zakas berish', 'Yaratuvchi bilan aloqa']
    keyboard.add(*buttons)  # yoki .add('Yaxshi','Yomon')
    await message.answer("Salom Botimizga xush kelibsiz", reply_markup=keyboard)
    buttons.delete()


@dp.message_handler(commands='Bot zakas berish')
async def url_tugma(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        # types.InlineKeyboardButton(text="Instagram",url="https://www.instagram.com/texnokun_uz/"),
        types.InlineKeyboardButton(text="Telegram kanal bot turlari", url="https://t.me/+hdP94Axk8zU2YWIy"),
        # types.InlineKeyboardButton(text="Yaratuvchi bilan aloqa", url="developertelegbotram"),
    ]
    keyboard.add(*buttons)
    await message.answer("Bulimlardan birini tanlang:", reply_markup=keyboard)


# @dp.message_handler(Text("Bot zakas berish"))  # yoki shunchaki text="Yaxshi"
# async def good(message: types.Message):
#     await message.reply("Kayfiyatingiz yaxshi ekanligidan xursandman :)")

# @dp.message_handler(Text("Yaratuvchi bilan aloqa"))  # yoki shunchaki text="Yomon"
# async def bad(message: types.Message):
#     await message.reply("Kayfiyatingiz yomonligidan afsusdaman :(\nSizga yaxshi kayfiyat tilab qo'laman!")

# @dp.message_handler(commands='Bot zakas berish')
# async def url_tugma(message: types.Message):
#     keyboard = types.InlineKeyboardMarkup(row_width=1)
#     buttons = [
#         # types.InlineKeyboardButton(text="Instagram",url="https://www.instagram.com/texnokun_uz/"),
#         types.InlineKeyboardButton(text="Telegram kanal bot turlari", url="https://t.me/+hdP94Axk8zU2YWIy"),
#         types.InlineKeyboardButton(text="Yaratuvchi bilan aloqa", url="developertelegbotram"),
#     ]
#     keyboard.add(*buttons)
#     await message.answer("TexnoKun.uz'ning ijtimoiy tarmoqlardagi sahifasi: ", reply_markup=keyboard)


# Foydalanuvchilardan kelgan matnni(textni) qabul qilib olish uchun handler
# @dp.message_handler(content_types=['text'])
# async def echo(message: types.Message):
# Foydalanuvchi jo'natgan matnga javoban jo'natgan matnini o'ziga yuboradi
# await message.reply(message.text)


if __name__ == '__main__':
    # Botimizni ishga tushiramiz
    executor.start_polling(dp, skip_updates=True)
