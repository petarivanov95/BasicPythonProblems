# Software Sales
# Problem #12 from Chapter 3 from Starting out with Python by Gaddis

# packages = int(input("How many packages do you intend to buy? "))

packages = 24
original_price_package = 99

if packages >= 100:
    new_price = round(original_price_package*0.4,2)
    total_new = round(packages * new_price,2)
    print("The new reduced price will be {} and the total for this number of packages is {}.".format(new_price, total_new))
elif packages >=50:
    new_price = round(original_price_package*0.3,2)
    total_new = round(packages * new_price,2)
    print("The new reduced price will be {} and the total for this number of packages is {}.".format(new_price, total_new))
elif packages >=20:
    new_price = round(original_price_package*0.2,2)
    total_new = round(packages * new_price,2)
    print("The new reduced price will be {} and the total for this number of packages is {}.".format(new_price, total_new))
elif packages >=10:
    new_price = round(original_price_package*0.1,2)
    total_new = round(packages * new_price,2)
    print("The new reduced price will be {} and the total for this number of packages is {}.".format(new_price, total_new))
else:
    new_price = original_price_package
    total_new = packages * new_price
    print("The quantity of {} packages does not warrant a reduction. The Price will be {}. Total price will be {}".format(packages,new_price,total_new))
