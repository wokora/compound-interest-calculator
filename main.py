years = 3
months = 12
total_months = years * months
start_month = 1
investment = 1420000
interest_rate_percent = 14
interest_rate = interest_rate_percent / 100
monthly_interest_rate = interest_rate / 12
total_interest = 0
withdrawal = 0
total_withdrawal = 0

balance = investment
break_down = "Y"
break_down_string = "Year" if break_down == "Y" else "Month"

# def calculate_interest(investment):
#     interest = investment * monthly_interest_rate
#     balance = investment + interest
#     balance = balance - withdrawal
#     investment = balance
    
#     return  interest, investment, balance
    

print(f"{break_down_string} \t Interest \t\t Total Interest \t Balance \t Withdrawal")
print(f"----- \t -------- \t\t --------------- \t ------- \t -----------")


for i in range(total_months):
    month = (start_month + i - 1) % 12 + 1
    year = 1 + (start_month + i - 1) // 12

    if year > years:
        break

    interest = investment * monthly_interest_rate
    balance = investment + interest
    balance = balance - withdrawal
    investment = balance

    # interest, investment, balance = calculate_interest(investment)
    total_interest = total_interest + interest
    total_withdrawal = total_withdrawal + withdrawal

    if break_down == "Y" and month % 12 == 0:
        print(f"{year} \t {interest:.2f} \t\t {total_interest:.2f} \t\t {balance:.2f} \t {total_withdrawal:.2f} ")

    
    if break_down == "M":
        print(f"{month} \t {interest:.2f} \t\t {total_interest:.2f} \t\t {balance:.2f} \t {total_withdrawal:.2f} ")

    