import aiosqlite
from config import *
import os
from loguru import logger

async def create_db_if_not_exists():
    if not os.path.exists(DATABASE_PATH):
        async with aiosqlite.connect(DATABASE_PATH) as db:
            await db.execute('''CREATE TABLE users
                               (id INTEGER PRIMARY KEY, user TEXT, withdraw TEXT, deposit TEXT, upcash TEXT)''')
            await db.execute('''CREATE TABLE withdraw
                                           (id INTEGER PRIMARY KEY, user TEXT, amount TEXT, link TEXT, hash TEXT)''')
            await db.execute('''CREATE TABLE settings
                                                       (allcash TEXT, upcash TEXT, uncash TEXT, max_bet TEXT)''')
            logger.success("SUCCESS CREATE DATABASE")

async def create_giveaway(user, amount, link, hash):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("INSERT INTO withdraw(user, amount, link, hash) VALUES (?,?,?,?)", (user, amount, link, hash))
        await db.commit()

async def create_user(id, user_name, deposit, withdraws, uncash, upcash, allcash, ref, ref_balance, ref_procent, who_ref):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("INSERT INTO users(id, user_name, deposit, withdraws, uncash, upcash, allcash, ref, ref_balance, ref_procent, who_ref) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, user_name, deposit, withdraws, uncash, upcash, allcash, ref, ref_balance, ref_procent, who_ref))
        await db.commit()

async def get_user(**kwargs):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        db.row_factory = dict_factory
        queryy = "SELECT * FROM users"
        queryy, params = query_args(queryy, kwargs)
        result = await db.execute(queryy, params)
        return await result.fetchone()

async def get_all_users():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        db.row_factory = dict_factory
        result = await db.execute("SELECT * FROM users")
        return await result.fetchall()



async def search_giveaway(hash):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        result = await db.execute("SELECT * FROM withdraw WHERE hash = ?", (hash,))
        return await result.fetchone()

async def get_settings():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        db.row_factory = dict_factory
        result = await db.execute("SELECT * FROM settings")
        return await result.fetchone()

async def edit_user(user, **kwargs):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        db.row_factory = dict_factory
        queryy = f"UPDATE users SET"
        queryy, params = query(queryy, kwargs)
        params.append(user)
        await db.execute(queryy + "WHERE id = ?", params)
        await db.commit()

async def edit_settings(**kwargs):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        db.row_factory = dict_factory
        queryy = f"UPDATE settings SET"
        queryy, params = query(queryy, kwargs)
        await db.execute(queryy, params)
        await db.commit()

def dict_factory(cursor, row):
    save_dict = {}

    for idx, col in enumerate(cursor.description):
        save_dict[col[0]] = row[idx]

    return save_dict

def query(sql, parameters: dict):
    if "XXX" not in sql: sql += " XXX "
    values = ", ".join([
        f"{item} = ?" for item in parameters
    ])
    sql = sql.replace("XXX", values)

    return sql, list(parameters.values())

def query_args(sql, parameters: dict):
    sql = f"{sql} WHERE "

    sql += " AND ".join([
        f"{item} = ?" for item in parameters
    ])

    return sql, list(parameters.values())
