
def choose_account():
    # print("enter your account type")
    account_type = input("enter account type")

def process_name():
    option = input("enter ")
    if option == withdrawal:
        amount = int(input("enter the ammount"))
        user_pin(pin)
        receipt(take_receipt)
    else:
        user_pin(pin)
        print("your balance is xxxxx")
        recept(take_recept)

def user_pin():
    pin = input("enter number")
    count = 0
    i = 0
    while i < len(pin):
        count = count+1
        i+=1
    if count == 4:
        print("we can move further")
    else:
        print("make sure you are entering the correct password")

def recept(take_recept):
    if take_recept == yes:
        print("wait for sometime time and collect the recept")
        print("thanks for using ATM service")
    else:
        print("thanks for using ATM service")
take_recept = input("would you like take the receipt")

    
def eng():
    print("welcome for the process")
    choose_account(account_type)
    process_name(option)

---------------------------------------------------------------

def khatha(khaate_ka_prakaar):
    khaate_ka_prakaar = input("apana khaata prakaar chunen")

def prakriya_naam(vikalp):
    if vikalp == vaapsi:
        rakam = int(input("pravesh karen"))
        upayogakarta_pin(pin)
        raseed(raseed)
    else:
        upayogakarta_pin(pin)
        print("aapka raashi hai xxxxx")
        raseed(raseed)

def upayogakarta_pin(pin):
    i = 0
    while i < len(pin):
        if pin[i] >= 0 or pin[i] <=9:
            i+=1
        else:
            print("sunishchi karen ki aapka sahee upayogakarta pin darj kar raha hai")
pin = input("apna pin darj karo")


def raseed(raseed):
    if raseed == "haan":
        print("kuch samay ke lie prateeksha karen aur apne rassed ko ikattha karen")
        print("ATM seva ka upayog karne ke lie dhanyavaad")
    else:
        print("ATM seva ka upayog karne ke lie dhanyavaad")
raseed = input("kya aap ek raseed lena chaahta hain ")


def hindi():
    print("swagat hai aapka process main")
    khatha(khaate_ka_prakaar)
    prakriya_naam(vikalp)

print("insert your card")
language = input("coose your language")
if language == english:
    eng()
else:
    hindi()
