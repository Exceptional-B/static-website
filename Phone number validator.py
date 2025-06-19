# define network code for each provider
networks= {
"MTN":{"703","706" ,"803" ,"806","810","813","814","816","903","906"},

 "Airtel":{"701","708","802","808","812","902","907"},
 "Glo":{"705","805","807","811","815","905"}, 
 "9mobile":{"809","817","818","908","909"},     }
def get_network(phone):
#check if the phone number stat with 0 and is of the correct lenght
 if phone.startswith("0") and len(phone)==11 and phone.isdigit():
     code =phone[1:4]
 else:
   return "invalid phone number lenght"
# check if  the network code is valid

 for name, codes in networks.items():
  if code in codes:   
    return f"Valid number.Network:{name}" 
  # If the code doesn't match any network

  return "Invalid network code."
  #get input and check

 number=input("enter number:").strip()
print(get_network(number))