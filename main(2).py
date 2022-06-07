import re
while True:
  input_code = input("Enter your country code : ")
  valid_code = False
  if (len(input_code)<2 or len(input_code)>3):
    print("Not valid ! Total digits should be betwwen 2-3 in country code")
    continue
  elif not re.search("[+]",input_code):
    print("Not valid !  [+] should exist in phone number")
    continue
  elif not re.search("[0-9]",input_code):
    print("Not valid ! Should contain only digits between [0-9]")
    continue
  else:
    valid_code = True
    break
if(valid_code==True):
  while True:
    num = input('Enter a mobile number to validate: ')
    Pattern = re.compile("[7-9][0-9]{9}")
    if Pattern.match(num):
      print('Valid Mobile Number')
      break
    else:
	    print("Invalid Mobile Number")