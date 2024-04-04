has_high_income =True
has_good_credit = True
has_criminal_record = False
# logical and operatorn for bith condition to be true 
if has_high_income and has_good_credit:
    print("ëligible for loan")

# logical OR operator for one condition to be true 
if has_high_income or has_good_credit: 
      print("ëligible for loan")

# logical NOt it inverse the boolean vlaue True t0 false
if  has_good_credit and not  has_criminal_record :
      print("Eligible for loan")