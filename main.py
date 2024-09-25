years = 2
investment = 100000
interest_rate = 0.14
months = 12
monthly_interest_rate = interest_rate / 12
total_interest = 0
balance = investment
print(f"Month \t Interest \t\t Accrued Interest \t Balance")

for i in range(1, (months * years) + 1):
    interest = investment * monthly_interest_rate
    balance = investment + interest
    investment = balance
    total_interest = total_interest + interest
    print(f"{i} \t\t {interest:.2f} \t\t {total_interest:.2f} \t\t\t {balance:.2f}")