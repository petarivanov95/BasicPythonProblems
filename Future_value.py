# chapter 5/Problem 19
# F is the future value of the account after the specified time period
# P is the present value of the account
# i is the monthly interest rate
# t is the number of months
# Formula ---> F = P x (1+i)^t

present = 100 # current value of the account in dollars
interest_rate = 6 # interest rate in percent
time = 6 # in number of months


def future_value(present, interest_rate, time):
    end_value = present*((1+(interest_rate/100))**time)
    return round(end_value,2)

my_investment = future_value(present,interest_rate,time)
print(my_investment)
