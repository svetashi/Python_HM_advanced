YE= 50
balance = 0
count = 0

operating = True

while operating:
    operation = input("Напишите, что хотите: пополнить, снять, выйти: ")
    if operation != 'выйти':
        if balance > 5000000:
            balance -= ((balance/100) * 10)
            print('Произошёл вычет налога на богатство, баланс: ', balance)

        inp_sum = int(input("Введите сумму: "))
        valid = True if inp_sum%YE == 0 else False
        if not valid:
            print('Сумма не кратна 50!')
        else:
            if operation == "пополнить":
                balance += inp_sum
                count+=1
            elif operation == "снять":
                if inp_sum > balance:
                    print("Сумма снятия не может быть больше суммы на счете!")
                else:
                    proc = (inp_sum/100)*1.5
                    clamped_proc = sorted((30, proc, 600))[1]
                    if balance >= inp_sum + clamped_proc:
                        balance -= inp_sum + clamped_proc
                        count+=1
                    else:
                        print("Недостаточно средств!")
            else:
                print('Неверная операция!')
            if count == 3:
                to_pay = ((balance/100) * 3)
                if to_pay <= balance:
                    balance -= to_pay
                count=0
    else:
        operating = False
    print(balance)
        