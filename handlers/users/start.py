import os

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ContentType
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from loader import dp, db
import re


class ManualEntry(StatesGroup):
    user_id = State()
    username = State()
    phone = State()
    full_name = State()
    position = State()
    workplace = State()

async def safe_finish(state: FSMContext):
    try:
        await state.finish()
    except KeyError:
        pass

def normalize_phone(text: str) -> str or None:
    digits = re.sub(r'\D', '', text)

    if digits.startswith('998') and len(digits) == 12:
        return '+{}'.format(digits)

    elif len(digits) == 9:
        return '+998{}'.format(digits)

    else:
        return None

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    info = await db.get_info(str(message.chat.id))
    if info is None:
        await message.answer("❌ Siz botdan foydalana olmaysiz.")
        return
    await message.answer(f"Salom, menga forward habar yuboring, yoki /manual yordamida foydalanuvchi qo'shing.")
    await safe_finish(state)

@dp.message_handler(commands="file")
async def export_to_excel_cmd(message: types.Message, state: FSMContext):
    info = await db.get_info(str(message.chat.id))
    if info is None:
        await message.answer("❌ Siz botdan foydalana olmaysiz.")
        return
    table_name = info['tablename']
    filename = f"{table_name}.xlsx"
    success = await db.export_to_excel(table_name, filename)
    if not success:
        await message.answer("ℹ️ Jadvalda hech qanday ma'lumot yo‘q.")
        return
    await message.answer_document(types.InputFile(filename))
    os.remove(filename)
    await safe_finish(state)

@dp.message_handler(commands="manual")
async def start_manual(message: types.Message, state: FSMContext):
    info = await db.get_info(str(message.chat.id))
    if info is None:
        await message.answer("❌ Siz botdan foydalana olmaysiz.")
        return
    await state.update_data(table_name=info['tablename'])
    await message.answer("1. Foydalanuvchi ID raqamini kiriting:")
    await ManualEntry.user_id.set()

@dp.message_handler(state=ManualEntry.user_id)
async def manual_user_id(message: types.Message, state: FSMContext):
    if not message.text.strip().isdigit() or message.text.strip().startswith('-'):
        await message.reply("❌ Noto‘g‘ri ID. Musbat raqam kiriting.")
        return
    user_id = int(message.text.strip())
    data = await state.get_data()
    table_name = data.get("table_name")
    exists = await db.client_exists(user_id=user_id, table_name=table_name)
    if exists:
        await message.reply("⚠️ Bu foydalanuvchi avvalroq bazaga qo‘shilgan.")
        await safe_finish(state)
        return
    await state.update_data(user_id=int(message.text.strip()))
    await ManualEntry.next()
    await message.answer("2. Username kiriting yoki `-` belgisi yuboring:")

@dp.message_handler(state=ManualEntry.username)
async def manual_username(message: types.Message, state: FSMContext):
    username = message.text.strip()
    if username == '-':
        username = None
    await state.update_data(username=username)
    await ManualEntry.next()
    await message.answer("3. Telefon raqamini kiriting yoki `-` belgisi yuboring (misol: +998901234567):")

@dp.message_handler(state=ManualEntry.phone)
async def manual_phone(message: types.Message, state: FSMContext):
    raw_phone = message.text.strip()

    if raw_phone == '-':
        phone = None
    else:
        phone = normalize_phone(raw_phone)
        if not phone:
            await message.reply(
                "❌ Telefon raqami noto‘g‘ri. Tog'ri yuboring\n"
                "Yoki `-` agar mavjud bo‘lmasa."
            )
            return

    await state.update_data(phone=phone)
    await ManualEntry.next()
    await message.answer("4. Ismni kiriting:")


@dp.message_handler(state=ManualEntry.full_name)
async def manual_full_name(message: types.Message, state: FSMContext):
    full_name = message.text.strip()
    await state.update_data(full_name=full_name)
    await ManualEntry.next()
    await message.answer("5. Lavozimni kiriting yoki `-` yuboring:")

@dp.message_handler(state=ManualEntry.position)
async def manual_position(message: types.Message, state: FSMContext):
    position = message.text.strip()
    if position == '-':
        position = None
    await state.update_data(position=position)
    await ManualEntry.next()
    await message.answer("6. Ish joyini kiriting yoki `-` yuboring:")

@dp.message_handler(state=ManualEntry.workplace)
async def manual_workplace(message: types.Message, state: FSMContext):
    workplace = message.text.strip()
    if workplace == '-':
        workplace = None

    data = await state.get_data()

    await db.add_full_client(
        user_id=data['user_id'],
        username=data['username'],
        phone=data['phone'],  # ✅ telefon ham bazaga yuboriladi
        fullname=data['full_name'],
        position=data['position'],
        workplace=workplace,
        table_name=data['table_name']
    )
    await message.answer("✅ Ma'lumotlar saqlandi.")
    await safe_finish(state)


@dp.message_handler(content_types=ContentType.ANY)
async def handle_ads(message: types.Message, state: FSMContext):
    info = await db.get_info(str(message.chat.id))
    if info is None:
        await message.answer("❌ Siz botdan foydalana olmaysiz.")
        return

    if not message.forward_from:
        await message.reply("Iltimos, faqat foydalanuvchidan forward qilingan habar yuboring.")
        return

    user_id = message.forward_from.id
    username = f"@{message.forward_from.username}"

    exists = await db.client_exists(user_id=user_id, table_name=info['tablename'])
    if exists:
        await message.answer("⚠️ Bu foydalanuvchi allaqachon bazaga qo‘shilgan.")
        return

    await state.update_data(user_id=user_id, username=username, table_name=info['tablename'])
    await message.answer("3. Telefon raqamini kiriting yoki `-` belgisi yuboring (misol: +998901234567):")
    await ManualEntry.phone.set()


