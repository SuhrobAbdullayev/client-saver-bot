import pytz
from aiogram.dispatcher.filters.state import StatesGroup, State

tashkent_tz = pytz.timezone('Asia/Tashkent')
from loader import dp, db, bot
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.types import ContentType

class MessageSending(StatesGroup):
    count = State()

async def safe_finish(state: FSMContext):
    try:
        await state.finish()
    except KeyError:
        pass

from aiogram.dispatcher import FSMContext

@dp.channel_post_handler(content_types=ContentType.ANY)
async def handle_channel_post(message: types.Message):
    channel_data = await db.get_channel_info(message.chat.id)

    if channel_data is None:
        return

    isClient = await db.sent_false_clients(channel_data['tablename'])
    admin_id = channel_data['user_id']
    if not isClient:
        await bot.send_message(
            chat_id=admin_id,
            text="Hamma odamlarga yuborilgan ✅"
        )
        return
    await db.update_message_id(chat_id=admin_id, mid=message.message_id)
    state = dp.current_state(chat=admin_id, user=admin_id)
    await state.set_state(MessageSending.count.state)
    await bot.send_message(
        chat_id=admin_id,
        text="Nechta odamga yuboramiz? (20 donadan kam odamga yuborish kerak)"
    )


@dp.message_handler(state=MessageSending.count)
async def enter_count(message: types.Message, state: FSMContext):
    try:
        count = int(message.text)
        if count > 20:
            await message.answer("❌ Iltimos, 20 dan kam raqam kiriting.")
            return
        await db.set_count(chat_id=message.chat.id, count=count)
        await message.answer(f"{count} ta odamga yuboriladi ✅")
        await safe_finish(state)
    except ValueError:
        await message.answer("❌ Xato kiritildi. Iltimos, raqam kiriting.")