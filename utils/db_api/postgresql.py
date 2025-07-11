from typing import Union
import asyncpg
import pandas as pd
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config

class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
              CREATE TABLE IF NOT EXISTS admins (
                                                    id SERIAL PRIMARY KEY,
                                                    user_id BIGINT UNIQUE NOT NULL,
                                                    tablename VARCHAR(255) NOT NULL,
                                                      channel_id BIGINT NOT NULL,
                                                      message_id INT NOT NULL default 0,
                                                      counts int not null default 20,
                                                      status boolean not null default false
                  );
              """
        await self.execute(sql, execute=True)


    async def create_table_xorazm(self):
        sql = """
              CREATE TABLE IF NOT EXISTS xorazm (
                                                    id SERIAL PRIMARY KEY,
                                                    user_id BIGINT UNIQUE NOT NULL,
                                                    username varchar null,
                                                    phone varchar null,
                                                    fullname varchar null,
                                                    positions varchar null,
                                                    workplace varchar null,
                                                    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                                    last_sent TIMESTAMP,
                                                    sent boolean DEFAULT false,
                                                    reminder_count INTEGER DEFAULT 0
              );
              """
        await self.execute(sql, execute=True)

    async def create_table_xorazm2(self):
        sql = """
              CREATE TABLE IF NOT EXISTS xorazm_users (
                                                    id SERIAL PRIMARY KEY,
                                                    user_id BIGINT UNIQUE NOT NULL,
                                                    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                                    last_sent TIMESTAMP
              );
              """
        await self.execute(sql, execute=True)

    async def create_table_qashqadaryo(self):
        sql = """
              CREATE TABLE IF NOT EXISTS qashqadaryo (
                                                         id SERIAL PRIMARY KEY,
                                                         user_id BIGINT UNIQUE NOT NULL,
                                                         username varchar null,
                                                         phone varchar null,
                                                         fullname varchar null,
                                                         positions varchar null,
                                                         workplace varchar null,
                                                         saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                                         last_sent TIMESTAMP,
                                                         sent boolean DEFAULT false,
                                                         reminder_count INTEGER DEFAULT 0
              );
              """
        await self.execute(sql, execute=True)

    async def create_table_qashqadaryo2(self):
        sql = """
              CREATE TABLE IF NOT EXISTS qashqadaryo_users (
                                                          id SERIAL PRIMARY KEY,
                                                          user_id BIGINT UNIQUE NOT NULL,
                                                          saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                                          last_sent TIMESTAMP
              );
              """
        await self.execute(sql, execute=True)

    async def create_table_navoiy(self):
        sql = """
              CREATE TABLE IF NOT EXISTS navoiy (
                                                    id SERIAL PRIMARY KEY,
                                                    user_id BIGINT UNIQUE NOT NULL,
                                                    username varchar null,
                                                    phone varchar null,
                                                    fullname varchar null,
                                                    positions varchar null,
                                                    workplace varchar null,
                                                    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                                    last_sent TIMESTAMP,
                                                    sent boolean DEFAULT false,
                                                    reminder_count INTEGER DEFAULT 0
              );
              """
        await self.execute(sql, execute=True)

    async def create_table_navoiy2(self):
        sql = """
              CREATE TABLE IF NOT EXISTS navoiy_users (
                                                          id SERIAL PRIMARY KEY,
                                                          user_id BIGINT UNIQUE NOT NULL,
                                                          saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                                          last_sent TIMESTAMP
              );
              """
        await self.execute(sql, execute=True)

    async def create_table_samarqand(self):
        sql = """
              CREATE TABLE IF NOT EXISTS samarqand (
                                                       id SERIAL PRIMARY KEY,
                                                       user_id BIGINT UNIQUE NOT NULL,
                                                       username varchar null,
                                                       phone varchar null,
                                                       fullname varchar null,
                                                       positions varchar null,
                                                       workplace varchar null,
                                                       saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                                       last_sent TIMESTAMP,
                                                       sent boolean DEFAULT false,
                                                       reminder_count INTEGER DEFAULT 0
              );
              """
        await self.execute(sql, execute=True)

    async def create_table_samarqand2(self):
        sql = """
              CREATE TABLE IF NOT EXISTS samarqand_users (
                                                          id SERIAL PRIMARY KEY,
                                                          user_id BIGINT UNIQUE NOT NULL,
                                                          saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                                          last_sent TIMESTAMP
              );
              """
        await self.execute(sql, execute=True)

    async def create_table_fargona(self):
        sql = """
              CREATE TABLE IF NOT EXISTS fargona (
                                                     id SERIAL PRIMARY KEY,
                                                     user_id BIGINT UNIQUE NOT NULL,
                                                     username varchar null,
                                                     phone varchar null,
                                                     fullname varchar null,
                                                     positions varchar null,
                                                     workplace varchar null,
                                                     saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                                     last_sent TIMESTAMP,
                                                     sent boolean DEFAULT false,
                                                     reminder_count INTEGER DEFAULT 0
              );
              """
        await self.execute(sql, execute=True)

    async def create_table_fargona2(self):
        sql = """
              CREATE TABLE IF NOT EXISTS fargona_users (
                                                          id SERIAL PRIMARY KEY,
                                                          user_id BIGINT UNIQUE NOT NULL,
                                                          saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                                          last_sent TIMESTAMP
              );
              """
        await self.execute(sql, execute=True)

    async def create_table_jizzax(self):
        sql = """
              CREATE TABLE IF NOT EXISTS jizzax (
                                                    id SERIAL PRIMARY KEY,
                                                    user_id BIGINT UNIQUE NOT NULL,
                                                    username varchar null,
                                                    phone varchar null,
                                                    fullname varchar null,
                                                    positions varchar null,
                                                    workplace varchar null,
                                                    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                                    last_sent TIMESTAMP,
                                                    sent boolean DEFAULT false,
                                                    reminder_count INTEGER DEFAULT 0
              );
              """
        await self.execute(sql, execute=True)

    async def create_table_jizzax2(self):
        sql = """
              CREATE TABLE IF NOT EXISTS jizzax_users (
                                                          id SERIAL PRIMARY KEY,
                                                          user_id BIGINT UNIQUE NOT NULL,
                                                          saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                                          last_sent TIMESTAMP
              );
              """
        await self.execute(sql, execute=True)

    async def create_table_buxoro(self):
        sql = """
              CREATE TABLE IF NOT EXISTS buxoro (
                                                    id SERIAL PRIMARY KEY,
                                                    user_id BIGINT UNIQUE NOT NULL,
                                                    username varchar null,
                                                    phone varchar null,
                                                    fullname varchar null,
                                                    positions varchar null,
                                                    workplace varchar null,
                                                    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                                    last_sent TIMESTAMP,
                                                    sent boolean DEFAULT false,
                                                    reminder_count INTEGER DEFAULT 0
              ); \
              """
        await self.execute(sql, execute=True)

    async def create_table_buxoro2(self):
        sql = """
              CREATE TABLE IF NOT EXISTS buxoro_users (
                                                          id SERIAL PRIMARY KEY,
                                                          user_id BIGINT UNIQUE NOT NULL,
                                                          saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                                          last_sent TIMESTAMP
              );
              """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())


    async def get_info(self, user_id):
        sql = f"SELECT * FROM admins WHERE user_id = '{user_id}'"
        return await self.execute(sql, fetchrow=True)


    async def get_channel_info(self, channel_id):
        sql = f"SELECT * FROM admins WHERE channel_id = '{channel_id}'"
        return await self.execute(sql, fetchrow=True)

    async def add_full_client(self, user_id, username, phone, fullname, position, workplace, table_name):
        sql = f"""
            INSERT INTO {table_name} (user_id, username, phone, fullname, positions, workplace)
            VALUES ($1, $2, $3, $4, $5, $6)
            ON CONFLICT (user_id) DO NOTHING
            RETURNING *
        """
        return await self.execute(sql, user_id, username, phone, fullname, position, workplace, fetchrow=True)

    async def client_exists(self, user_id: int, table_name: str) -> bool:
        sql = f"SELECT 1 FROM {table_name} WHERE user_id = $1 LIMIT 1"
        result = await self.execute(sql, user_id, fetchrow=True)
        return result is not None


    async def sent_false_clients(self, table_name: str) -> bool:
        sql = f"SELECT * FROM {table_name} WHERE sent = false"
        result = await self.execute(sql,  fetchrow=True)
        return result is not None

    async def update_message_id(self, chat_id, mid):
        sql = f"UPDATE admins SET message_id = {mid} WHERE user_id='{chat_id}'"
        return await self.execute(sql, fetch=True)

    async def set_count(self, chat_id, count):
        sql = f"UPDATE admins SET counts='{count}', status = true WHERE user_id='{chat_id}'"
        return await self.execute(sql, fetch=True)

    async def export_to_excel(self, table_name: str, filename: str) -> bool:
        sql = f"""
        SELECT user_id, username, phone, fullname, positions, workplace, saved_at
        FROM {table_name}
        ORDER BY saved_at DESC
        """
        rows = await self.execute(sql, fetch=True)

        if not rows:
            return False

        df = pd.DataFrame(rows, columns=[
            "user_id", "username", "phone", "fullname", "positions", "workplace", "saved_at"
        ])
        df.to_excel(filename, index=False)
        return True
