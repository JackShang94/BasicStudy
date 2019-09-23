# 3)
def calculateTotalInterest(balance):
    anualInterest = 0
    if 0 <= balance <= 10000:
        anualInterest = balance * 0.015
    elif 10000<balance<= 30000:
        anualInterest = 10000 * 0.015 + (balance - 10000) * 0.02
    else:
        anualInterest = 10000 * 0.015 +20000 * 0.02 + (balance - 30000) * 0.01

    return anualInterest

balance = float(input('Enter the balance $:'))
print('Interest for that month is :{:.2f}'.format(calculateTotalInterest(balance)/12))