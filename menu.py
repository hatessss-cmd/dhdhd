from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from config import *
def menu_gift(url):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🎁 Забрать выигрыш", url=url),
                InlineKeyboardButton(text="Сделать ставку 🎲", url=pinned_link)
            ]
        ]
    )
    return kb

def menu_non_gift():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Сделать ставку", url=pinned_link)
            ]
        ]
    )
    return kb

def sub_kb():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📌 Подписаться", url=casino_link)
            ]
        ]
    )
    return kb

def menu_kb():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🎲 Сделать ставку", url=casino_link)
            ],
            [
                InlineKeyboardButton(text="💳 Вывести реф. баланс", callback_data="ref_withdraw")
            ]
        ]
    )
    return kb

def withdraw_kb(user):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Выполнена", callback_data=f"withdraw_confirm:{user}")
            ]
        ]
    )
    return kb