import aiosqlite
from pathlib import Path


db_path = Path(Path.cwd().parent,'order_helper\db.sqlite3')


async def get_customer(phone):
    '''Берём пользоваля из БД по никнейму'''
    async with aiosqlite.connect(db_path) as db:
        result = await db.execute(f"SELECT * FROM crm_customer WHERE phone='{phone}'")
        resultfetch = await result.fetchone()
        return(resultfetch)


async def add_customer(nickname,phone):
    '''Добавляем пользоваля в БД'''
    try:
        async with aiosqlite.connect(db_path) as db:
            await db.execute(f"INSERT INTO crm_customer (nickname, phone) VALUES (?,?)",(nickname,phone))
            await db.commit()
            return True
    except Exception as error:
        print("Ошибка при работе с SQLite", error)
        return False

