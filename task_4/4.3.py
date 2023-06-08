# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
import decimal


class ATM:
    _BALANCE = 0
    _MIN = 50
    _COMMISSION = 0.015
    _BONUS = 0.03
    _TAX = 0.1
    _OPERATION = int
    _WEALTH = 5_000_000
    _WEALTH_TAX = 0.1
    _list_operation = []

    def __init__(self):
        self._OPERATION = 0

    def _in(self, cash: int) -> tuple[int, int]:

        if cash % self._MIN == 0:
            self._BALANCE += cash
            self._OPERATION += 1
            return self._BALANCE, self._OPERATION
        else:
            None

    def _out(self, cash: int, commission: int) -> tuple[int, int] | bool:
        if cash % self._MIN == 0 and self._BALANCE - (cash + commission) >= 0:
            self._BALANCE -= cash + commission
            self._OPERATION += 1
            return self._BALANCE, self._OPERATION
        else:
            None

    def _check_commission(self, cash: decimal, ) -> decimal:

        MIN = 30
        MAX = 600
        sum_commission = cash * self._COMMISSION
        if sum_commission < MIN:
            return MIN
        elif sum_commission > MAX:
            return MAX
        else:
            return sum_commission

    def _check_operation(self):
        state = self._OPERATION
        if state % 3 == 0:
            return True
        else:
            return False

    def exit(self):
        return f"Спасибо, что воспользовались услугами банка. Ждем Вас снова! Баланс: {self._BALANCE}"

    def start(self, mode: str, cash: decimal = 0) -> str:

        match mode:
            case "_in":
                if self._BALANCE > self._WEALTH:
                    self._BALANCE = self._BALANCE * self._WEALTH_TAX
                    print(f'Вы очень богаты! С вас был взят налог. Баланс: {self._BALANCE}')
                data = self._in(cash=cash)
                if data:
                    check_operation = self._check_operation()
                    self._list_operation.append(['Внесено', cash])
                    if check_operation:
                        self._BALANCE += self._BALANCE * self._BONUS
                        return f'Операция пополнения на {cash} выполнена успешно. Вам зачислены бонусы на остаток. ' \
                               f' Ваш баланс: {self._BALANCE}'
                    return f'Операция пополнения на {cash} выполнена успешно. Ваш баланс: {self._BALANCE}.'
                else:
                    return f"Ошибка. Внесите сумму кратную 50 y.e. Повторите попытку. Баланс: {self._BALANCE}"
            case "_out":
                if self._BALANCE > self._WEALTH:
                    self._BALANCE = self._BALANCE * self._WEALTH_TAX
                    print(f'Вы очень богаты! С вас был снят налог. Баланс: {self._BALANCE}')
                com_data = self._check_commission(cash=cash)
                data = self._out(cash=cash, commission=com_data)
                if data:
                    check_operation = self._check_operation()
                    self._list_operation.append(['Снятие', cash])
                    if check_operation:
                        self._BALANCE += self._BALANCE * self._BONUS
                        return f'Операция снятия {cash} выполнена успешно, комиссия {com_data}. ' \
                               f'Вам зачислены бонусы на остаток. Ваш баланс: {self._BALANCE}'
                    return f'Операция снятия {cash} выполнена успешно, комиссия {com_data}. Ваш баланс: {self._BALANCE}'
                else:
                    return f'Ошибка. На счете недостаточно средств или сумма не кратна 50. Повторите попытку.' \
                            f'Ваш баланс: {self._BALANCE}'
            case "exit":
                print('Ваши операции за сессию: ' f'{self._list_operation}')
                return self.exit()

        check_operation = self._check_operation()
        if check_operation:
            self._BALANCE += self._BALANCE * self._BONUS
            return f'Вам зачислены бонусы на остаток. Ваш баланс: {self._BALANCE}'


client = ATM()
# print(client.start(mode="_in", cash=200))
# print(client.start(mode="_out", cash=100))
# print(client.start(mode="_in", cash=300))
# print(client.start(mode="_in", cash=200))
# print(client.start(mode="_out", cash=100))
# print(client.start(mode="_out", cash=100))
# print(client.start(mode="_out", cash=400))
# print(client.start(mode="_in", cash=220))
# print(client.start(mode="_in", cash=200))
# print(client.start(mode="_in", cash=5_000_000))
# print(client.start(mode="_out", cash=50))
# print(client.start(mode="_out", cash=70))
# print(client.start(mode="_in", cash=5000000))
# print(client.start(mode="_out", cash=70))
# print(client.start(mode="exit"))
print(client.start(mode="_in", cash=1000000))
print(client.start(mode="_out", cash=10000))
print(client.start(mode="_out", cash=150000))
print(client.start(mode="exit"))