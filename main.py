from main_var import *


@bot.message_handler(commands=["start"])
def welcome(message):
    item = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("📍 Bizning manzilimiz", url=location)
    item2 = types.InlineKeyboardButton("👥 Bizning kanalimiz", url=group)
    item3 = types.InlineKeyboardButton("📲 Admin bilan boglanish", callback_data=admin)
    item4 = types.InlineKeyboardButton("⚙️ Shikoyatlar va takliflar", callback_data=complaints)
    item5 = types.InlineKeyboardButton("ℹ️ Kurslarimizdan malumot olish", callback_data=curse)
    item6 = types.InlineKeyboardButton("📝 Ro'yxatan otish", callback_data=test)

    item.row(item1, item2)
    item.row(item3, item4)
    item.row(item5)
    item.row(item6)
    bot.send_message(message.chat.id, f"😊 Assalomu aleykum {message.from_user.first_name}\n⚙️ Siz asosiy menyudasiz",
                     reply_markup=item)


@bot.callback_query_handler(func=lambda call: True)
def call_data(call):
    if call.data == admin:
        item = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("🔙 Back", callback_data=back)
        item.row(item1)
        bot.send_message(call.message.chat.id,
                         "😊 Ism - Elmar\n\n😊 Familiya - Izmailov\n\n✈️ Telegram akk - @E_l_m_a_r\n\n📱 Telefon raqam +998942584347",
                         reply_markup=item)

    elif call.data == complaints:
        item = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("🔙 Back", callback_data=back)
        item.row(item1)
        bot.send_message(call.message.chat.id,
                         f"Xurmatliy {call.from_user.first_name}\nShikoyat yoki takliflaringiz bolsa yozib qoldiring...",
                         reply_markup=item)
        bot.register_next_step_handler(call.message, get_func)

    elif call.data == curse:
        item = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("🖥 Kompyuter savodxonligi", callback_data=kompyter_sa)
        item2 = types.InlineKeyboardButton("📝 Frontend", callback_data=frondend)
        item3 = types.InlineKeyboardButton("🕸 Backend", callback_data=backend)
        item4 = types.InlineKeyboardButton("🐍 Python", callback_data=python)

        item.row(item1)
        item.row(item2, item3)
        item.row(item3, item4)
        bot.send_message(call.message.chat.id, "😊 Qaysi kursga qiziktingiz", reply_markup=item)

    elif call.data == back:
        item = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("📍 Bizning manzilimiz", url=location)
        item2 = types.InlineKeyboardButton("👥 Bizning kanalimiz", url=group)
        item3 = types.InlineKeyboardButton("📲 Admin bilan boglanish", callback_data=admin)
        item4 = types.InlineKeyboardButton("⚙️ Shikoyatlar va takliflar", callback_data=complaints)
        item5 = types.InlineKeyboardButton("ℹ️ Kurslarimizdan malumot olish", callback_data=curse)
        item6 = types.InlineKeyboardButton("📝 Ro'yxatan otish", callback_data=test)

        item.row(item1, item2)
        item.row(item3, item4)
        item.row(item5)
        item.row(item6)
        bot.send_message(call.message.chat.id,
                         f"😊 Assalomu aleykum {call.from_user.first_name}\n⚙️ Siz asosiy menyudasiz",
                         reply_markup=item)

    if call.data == kompyter_sa:
        item = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("🔙 Back", callback_data=back)
        item.row(item1)
        bot.send_message(call.message.chat.id, komp_info, reply_markup=item)
    elif call.data == frondend:
        item = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("🔙 Back", callback_data=back)
        item.row(item1)
        bot.send_message(call.message.chat.id, frondend_info, reply_markup=item)
    elif call.data == backend:
        item = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("🔙 Back", callback_data=back)
        item.row(item1)
        bot.send_message(call.message.chat.id, backend_info, reply_markup=item)
    elif call.data == python:
        item = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("🔙 Back", callback_data=back)
        item.row(item1)
        bot.send_message(call.message.chat.id, python_info, reply_markup=item)

    elif call.data == test:
        ism = bot.send_message(call.message.chat.id, "Ismizi yozib qoldiring")
        bot.register_next_step_handler(ism, get_name)


def get_name(message):
    global name
    name = message.text
    try:
        if message.text.isalpha():
            lname = bot.send_message(message.chat.id, "Familiyangizni yozib qoldiring")
            bot.register_next_step_handler(lname, get_lname)
        else:
            item = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("📍 Bizning manzilimiz", url=location)
            item2 = types.InlineKeyboardButton("👥 Bizning kanalimiz", url=group)
            item3 = types.InlineKeyboardButton("📲 Admin bilan boglanish", callback_data=admin)
            item4 = types.InlineKeyboardButton("⚙️ Shikoyatlar va takliflar", callback_data=complaints)
            item5 = types.InlineKeyboardButton("ℹ️ Kurslarimizdan malumot olish", callback_data=curse)
            item6 = types.InlineKeyboardButton("📝 Ro'yxatan otish", callback_data=test)

            item.row(item1, item2)
            item.row(item3, item4)
            item.row(item5)
            item.row(item6)
            bot.send_message(message.chat.id,
                             f"😊 Assalomu aleykum {message.from_user.first_name}\n⚙️ Siz malumotni noto'gri  kiritingiz",
                             reply_markup=item)

    except:
        item = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("📍 Bizning manzilimiz", url=location)
        item2 = types.InlineKeyboardButton("👥 Bizning kanalimiz", url=group)
        item3 = types.InlineKeyboardButton("📲 Admin bilan boglanish", callback_data=admin)
        item4 = types.InlineKeyboardButton("⚙️ Shikoyatlar va takliflar", callback_data=complaints)
        item5 = types.InlineKeyboardButton("ℹ️ Kurslarimizdan malumot olish", callback_data=curse)
        item6 = types.InlineKeyboardButton("📝 Ro'yxatan otish", callback_data=test)

        item.row(item1, item2)
        item.row(item3, item4)
        item.row(item5)
        item.row(item6)
        bot.send_message(message.chat.id,
                         f"😊 Assalomu aleykum {message.from_user.first_name}\n⚙️ Siz malumotni noto'gri  kiritingiz",
                         reply_markup=item)


def get_lname(message):
    global lname
    lname = message.text
    try:
        if message.text.isalpha():
            age = bot.send_message(message.chat.id, "Yoshizi yozib qoldiring")
            bot.register_next_step_handler(age, get_age)
        else:
            item = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("📍 Bizning manzilimiz", url=location)
            item2 = types.InlineKeyboardButton("👥 Bizning kanalimiz", url=group)
            item3 = types.InlineKeyboardButton("📲 Admin bilan boglanish", callback_data=admin)
            item4 = types.InlineKeyboardButton("⚙️ Shikoyatlar va takliflar", callback_data=complaints)
            item5 = types.InlineKeyboardButton("ℹ️ Kurslarimizdan malumot olish", callback_data=curse)
            item6 = types.InlineKeyboardButton("📝 Ro'yxatan otish", callback_data=test)

            item.row(item1, item2)
            item.row(item3, item4)
            item.row(item5)
            item.row(item6)
            bot.send_message(message.chat.id,
                             f"😊 Assalomu aleykum {message.from_user.first_name}\n⚙️ Siz malumotni noto'gri  kiritingiz",
                             reply_markup=item)

    except:
        item = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("📍 Bizning manzilimiz", url=location)
        item2 = types.InlineKeyboardButton("👥 Bizning kanalimiz", url=group)
        item3 = types.InlineKeyboardButton("📲 Admin bilan boglanish", callback_data=admin)
        item4 = types.InlineKeyboardButton("⚙️ Shikoyatlar va takliflar", callback_data=complaints)
        item5 = types.InlineKeyboardButton("ℹ️ Kurslarimizdan malumot olish", callback_data=curse)
        item6 = types.InlineKeyboardButton("📝 Ro'yxatan otish", callback_data=test)

        item.row(item1, item2)
        item.row(item3, item4)
        item.row(item5)
        item.row(item6)
        bot.send_message(message.chat.id,
                         f"😊 Assalomu aleykum {message.from_user.first_name}\n⚙️ Siz malumotni noto'gri  kiritingiz",
                         reply_markup=item)


def get_age(message):
    global age
    age = message.text
    try:
        if int(message.text) <= 50:
            phone_number = bot.send_message(message.chat.id, "Telefon raqamingizni yozib qoldiring")
            bot.register_next_step_handler(phone_number, get_numbers)
        else:
            item = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("📍 Bizning manzilimiz", url=location)
            item2 = types.InlineKeyboardButton("👥 Bizning kanalimiz", url=group)
            item3 = types.InlineKeyboardButton("📲 Admin bilan boglanish", callback_data=admin)
            item4 = types.InlineKeyboardButton("⚙️ Shikoyatlar va takliflar", callback_data=complaints)
            item5 = types.InlineKeyboardButton("ℹ️ Kurslarimizdan malumot olish", callback_data=curse)
            item6 = types.InlineKeyboardButton("📝 Ro'yxatan otish", callback_data=test)

            item.row(item1, item2)
            item.row(item3, item4)
            item.row(item5)
            item.row(item6)
            bot.send_message(message.chat.id,
                             f"😊 Assalomu aleykum {message.from_user.first_name}\n⚙️ Siz malumotni noto'gri  kiritingiz",
                             reply_markup=item)

    except ValueError:
        item = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("📍 Bizning manzilimiz", url=location)
        item2 = types.InlineKeyboardButton("👥 Bizning kanalimiz", url=group)
        item3 = types.InlineKeyboardButton("📲 Admin bilan boglanish", callback_data=admin)
        item4 = types.InlineKeyboardButton("⚙️ Shikoyatlar va takliflar", callback_data=complaints)
        item5 = types.InlineKeyboardButton("ℹ️ Kurslarimizdan malumot olish", callback_data=curse)
        item6 = types.InlineKeyboardButton("📝 Ro'yxatan otish", callback_data=test)

        item.row(item1, item2)
        item.row(item3, item4)
        item.row(item5)
        item.row(item6)
        bot.send_message(message.chat.id,
                         f"😊 Assalomu aleykum {message.from_user.first_name}\n⚙️ Siz malumotni noto'gri  kiritingiz",
                         reply_markup=item)


def get_numbers(message):
    global phone_numbers
    phone_numbers = message.text
    try:
        if int(message.text):
            item = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Python")
            item2 = types.KeyboardButton("Frontend")
            item3 = types.KeyboardButton("Backend")
            item4 = types.KeyboardButton("Kompyuter savodxonlig")
            item.row(item1, item2)
            item.row(item3, item4)

            curse = bot.send_message(message.chat.id, "Qaysi kursga kiziktingiz", reply_markup=item)
            bot.register_next_step_handler(curse, get_curse)

        else:
            item = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("📍 Bizning manzilimiz", url=location)
            item2 = types.InlineKeyboardButton("👥 Bizning kanalimiz", url=group)
            item3 = types.InlineKeyboardButton("📲 Admin bilan boglanish", callback_data=admin)
            item4 = types.InlineKeyboardButton("⚙️ Shikoyatlar va takliflar", callback_data=complaints)
            item5 = types.InlineKeyboardButton("ℹ️ Kurslarimizdan malumot olish", callback_data=curse)
            item6 = types.InlineKeyboardButton("📝 Ro'yxatan otish", callback_data=test)

            item.row(item1, item2)
            item.row(item3, item4)
            item.row(item5)
            item.row(item6)
            bot.send_message(message.chat.id,
                             f"😊 Assalomu aleykum {message.from_user.first_name}\n⚙️ Siz malumotni noto'gri  kiritingiz",
                             reply_markup=item)
    except ValueError:
        item = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("📍 Bizning manzilimiz", url=location)
        item2 = types.InlineKeyboardButton("👥 Bizning kanalimiz", url=group)
        item3 = types.InlineKeyboardButton("📲 Admin bilan boglanish", callback_data=admin)
        item4 = types.InlineKeyboardButton("⚙️ Shikoyatlar va takliflar", callback_data=complaints)
        item5 = types.InlineKeyboardButton("ℹ️ Kurslarimizdan malumot olish", callback_data=curse)
        item6 = types.InlineKeyboardButton("📝 Ro'yxatan otish", callback_data=test)

        item.row(item1, item2)
        item.row(item3, item4)
        item.row(item5)
        item.row(item6)
        bot.send_message(message.chat.id,
                         f"😊 Assalomu aleykum {message.from_user.first_name}\n⚙️ Siz malumotni noto'gri  kiritingiz",
                         reply_markup=item)


def get_curse(message):
    global curses
    curses = message.text
    try:
        if message.text in "Python Frontend Backend Kompyuter savodxonlig":
            item = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Xa")
            item2 = types.KeyboardButton("Yo'q")
            item.row(item1, item2)
            k = bot.send_message(message.chat.id,
                                 f"Ismiz {name}\n\nFamiliyangiz {lname}\n\nYoshiz {age}\n\nTelefon raqamingiz {phone_numbers}\n\nTanlagan  kursiz {curses}",
                                 reply_markup=item)
            bot.register_next_step_handler(k, yes_or_no)
        else:
            item = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("📍 Bizning manzilimiz", url=location)
            item2 = types.InlineKeyboardButton("👥 Bizning kanalimiz", url=group)
            item3 = types.InlineKeyboardButton("📲 Admin bilan boglanish", callback_data=admin)
            item4 = types.InlineKeyboardButton("⚙️ Shikoyatlar va takliflar", callback_data=complaints)
            item5 = types.InlineKeyboardButton("ℹ️ Kurslarimizdan malumot olish", callback_data=curse)
            item6 = types.InlineKeyboardButton("📝 Ro'yxatan otish", callback_data=test)

            item.row(item1, item2)
            item.row(item3, item4)
            item.row(item5)
            item.row(item6)
            bot.send_message(message.chat.id,
                             f"😊 Assalomu aleykum {message.from_user.first_name}\n⚙️ Siz malumotni noto'gri  kiritingiz",
                             reply_markup=item)
    except:
        item = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("📍 Bizning manzilimiz", url=location)
        item2 = types.InlineKeyboardButton("👥 Bizning kanalimiz", url=group)
        item3 = types.InlineKeyboardButton("📲 Admin bilan boglanish", callback_data=admin)
        item4 = types.InlineKeyboardButton("⚙️ Shikoyatlar va takliflar", callback_data=complaints)
        item5 = types.InlineKeyboardButton("ℹ️ Kurslarimizdan malumot olish", callback_data=curse)
        item6 = types.InlineKeyboardButton("📝 Ro'yxatan otish", callback_data=test)

        item.row(item1, item2)
        item.row(item3, item4)
        item.row(item5)
        item.row(item6)
        bot.send_message(message.chat.id,
                         f"😊 Assalomu aleykum {message.from_user.first_name}\n⚙️ Siz malumotni noto'gri  kiritingiz",
                         reply_markup=item)


def yes_or_no(message):
    global son
    if message.text == "Xa" or message.text == "xa":
        bot.send_message(5371294058,
                         f"Ismiz {name}\n\nFamiliyangiz {lname}\n\nYoshiz {age}\n\nTelefon raqamingiz {phone_numbers}\n\nTanlagan  kursiz {curses}")
        son  += 1

    elif message.text == "Yo'q" or message.text == "yo'q":
        item = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("📍 Bizning manzilimiz", url=location)
        item2 = types.InlineKeyboardButton("👥 Bizning kanalimiz", url=group)
        item3 = types.InlineKeyboardButton("📲 Admin bilan boglanish", callback_data=admin)
        item4 = types.InlineKeyboardButton("⚙️ Shikoyatlar va takliflar", callback_data=complaints)
        item5 = types.InlineKeyboardButton("ℹ️ Kurslarimizdan malumot olish", callback_data=curse)
        item6 = types.InlineKeyboardButton("📝 Ro'yxatan otish", callback_data=test)

        item.row(item1, item2)
        item.row(item3, item4)
        item.row(item5)
        item.row(item6)
        bot.send_message(message.chat.id,
                         f"😊 Assalomu aleykum {message.from_user.first_name}\n⚙️ Siz asosiy menyudasiz",
                         reply_markup=item)
    else:
        item = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("📍 Bizning manzilimiz", url=location)
        item2 = types.InlineKeyboardButton("👥 Bizning kanalimiz", url=group)
        item3 = types.InlineKeyboardButton("📲 Admin bilan boglanish", callback_data=admin)
        item4 = types.InlineKeyboardButton("⚙️ Shikoyatlar va takliflar", callback_data=complaints)
        item5 = types.InlineKeyboardButton("ℹ️ Kurslarimizdan malumot olish", callback_data=curse)
        item6 = types.InlineKeyboardButton("📝 Ro'yxatan otish", callback_data=test)

        item.row(item1, item2)
        item.row(item3, item4)
        item.row(item5)
        item.row(item6)
        bot.send_message(message.chat.id,
                         f"😊 Assalomu aleykum {message.from_user.first_name}\n⚙️ Siz malumotni noto'gri  kiritingiz",
                         reply_markup=item)


def get_func(message):
    bot.send_message(message.chat.id, "📲 Adminga xabaringiz jonatildi")
    bot.send_message(5371294058, message.text)


@bot.message_handler(content_types=["text"])
def get_info(message):
    global son
    if message.text == "/help":
             bot.send_message(message.chat.id, son)

bot.polling(none_stop=True)
