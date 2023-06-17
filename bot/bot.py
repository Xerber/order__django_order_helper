from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from config_reader import config
import re
from dbwork import get_customer, add_customer



bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher(bot, storage=MemoryStorage())

class RegStateGroup(StatesGroup):
    phone = State()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await RegStateGroup.phone.set()
    await message.answer('Здравствуйте! Для того чтоб воспользоваться моими услугами нужно сперва зарегистрироваться!')
    await message.answer('Укажите Ваш действующий номер телефона и я зарегистрирую Вас не отнимая больше времени')

@dp.message_handler(commands=['reg'])
async def start_command(message: types.Message):
    await RegStateGroup.phone.set()
    await message.answer('Укажите Ваш действующий номер телефона и я зарегистрирую Вас не отнимая больше времени')

@dp.message_handler(state=RegStateGroup.phone)  
async def check_phone(message: types.Message, state: FSMContext):
    result = re.match(r'^[-+]?[78]?(\d{10}|\d{7})$', message.text) 
    if bool(result):
        if message.text in ['+79591234567', '79591234567']:
            await message.answer('Отличная мысль!, но введите корректный номер телефона. Пример: +79591234567')
        else:
            if bool(await get_customer(message.text)):
                await message.answer('Данный номер телефона уже зарегистрирован. Введите другой номер или свяжитесь с администратором')
            else:
                save = await add_customer(message.from_user.username,message.text)
                if save:
                    await message.answer('Учетная запись была зарегистрирована. Хороших покупок!')
                    await state.finish()
                else:
                    await message.answer('Ошибка при сохрании учетной записи. Свяжитесь с администратором или попробуйте снова прописав /reg')
    else:
        await message.answer('Введите корректный номер телефона. Пример: +79591234567')

if __name__=='__main__':
  executor.start_polling(dp)