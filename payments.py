from aiocryptopay import AioCryptoPay, Networks
from config import *

class CryptoBotPay():
    def __init__(self):
        self.key = CRYPTOBOT_TOKEN
        self.pay = AioCryptoPay(self.key)

    async def balance(self):
        balance = await self.pay.get_balance()
        await self.pay.close()
        return balance[0].available

    async def create_pay(self, amount, currency):
        invoice = await self.pay.create_invoice(amount=amount, asset=currency, allow_anonymous=False)
        await self.pay.close()
        return invoice

    async def create_check(self, amount, currency):
        check = await self.pay.create_check(asset=currency, amount=amount)
        await self.pay.close()
        return check

    async def send_cash(self, user, amount, currency, hash):
        check = await self.pay.transfer(user, asset=currency, amount=amount, comment="Выплата за ставку.", spend_id=hash)
        await self.pay.close()
        return check

    async def check_pay(self, order_id):
        payment = await self.pay.get_invoices(invoice_ids=order_id)
        payment = payment[0].status
        await self.pay.close()
        return payment

    async def get_checks(self):
        payment = await self.pay.get_checks(status="active")
        await self.pay.close()
        return payment

    async def close_session(self):
        await self.pay.close()
