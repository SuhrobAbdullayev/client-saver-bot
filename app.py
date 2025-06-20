from aiogram import executor

from loader import dp, db
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await db.create()
    await db.create_table_users()
    await db.create_table_xorazm()
    await db.create_table_xorazm2()
    await db.create_table_qashqadaryo()
    await db.create_table_qashqadaryo2()
    await db.create_table_navoiy()
    await db.create_table_navoiy2()
    await db.create_table_samarqand()
    await db.create_table_samarqand2()
    await db.create_table_jizzax()
    await db.create_table_jizzax2()
    await db.create_table_fargona()
    await db.create_table_fargona2()
    await db.create_table_buxoro()
    await db.create_table_buxoro2()

    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
