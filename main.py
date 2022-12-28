from aiogram.utils import executor
from handlers import dp


async def bot_start(_):
    print('Вот запущен')



if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True, on_startup=bot_start)