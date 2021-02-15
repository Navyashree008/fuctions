def choose_account():
    a = "enter your account type either SAVING or CURRENT"
    account_type = input("enter account type:-")
    return a
# ----------------------------------------------------
def process_name():
    print("you can withdraw or check balance")
    option = input("enter the type of transaction:-")
    if option == "withdrawal":
        amount = int(input("enter the ammount:-"))
        print(user_pin())
        receipt()
    else:
        print(user_pin())
        print("your balance is xxxxx")
        receipt()

# ---------------------------------------------------
def user_pin():
    pin = input("enter your pin:-")
    count = 0
    i = 0
    while i < len(pin):
        count = count+1
        i+=1
    if count == 4:
        return "we can move further"
    else:
        return "make sure you are entering the correct password"

#-------------------------------------------------------
def receipt():
    take_recept = input("would you like take the receipt:-")
    if take_recept == "yes":
        print("wait for sometime time and collect the recept")
        print("thanks for using ATM service")
    else:
        print("thanks for using ATM service")

#-------------------------------------------------------- 
def eng():
    print("welcome for the process")
    print(choose_account())
    process_name()

#=======================================================

def khatha():
    a = "aap SAVING YA CURRENT account choose kar sakte hai"
    khaate = input("apana khaata prakaar chunen:-")
    return a
# -----------------------------------------------------------
def prakriya_naam():
    print("aap withdraw ya balance check kar sakte hai")
    vikalp = input("tansaction ki tharika chuniye:-")
    if vikalp == "withdrawal":
        rakam = int(input("rakam pravesh karen:-"))
        upayogakarta_pin()
        raseed()
    else:
        upayogakarta_pin()
        print("aapka raashi hai xxxxx")
        raseed()
# ------------------------------------------------------
def upayogakarta_pin():
    pin = input("pin enter kijiye")
    count = 0
    i = 0
    while i < len(pin):
        count = count+1
        i+=1
    if count == 4:
        return "aage ki prakriya kar sakte hai"
    else:
        return "sahi pin enter karein"
    

# -----------------------------------------------------------
def raseed():
    raseed = input("kya aap ek raseed lena chaahta hain:- ")
    if raseed == "haan":
        print("kuch samay ke lie prateeksha karen aur apne rassed ko ikattha karen")
        print("ATM seva ka upayog karne ke lie dhanyavaad")
    else:
        print("ATM seva ka upayog karne ke lie dhanyavaad")


# -----------------------------------------------
def hindi():
    print("swagat hai aapka process main")
    print(khatha())
    prakriya_naam()
    
# -----------------------------------------------
print("insert your card")
print("you can coose english or hindi for the further process")
language = input("choose your language:-")
if language == "english":
    eng()
else:
    hindi()
