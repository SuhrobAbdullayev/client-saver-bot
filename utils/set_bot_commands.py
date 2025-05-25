from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("manual", "Qolda foydalanuvchi qo'shish"),
            types.BotCommand("file", "Excel file sifatida olish"),
        ]
    )
