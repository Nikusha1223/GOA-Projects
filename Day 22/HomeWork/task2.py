
vegetables = ["კომბოსტო", "სტაფილო", "კიტრი", "ბადრიჯანი", "პომიდორი"]

user_choice = int(input("შეიყვანეთ რიცხვი 0-იდან 4-მდე: "))

if 0 <= user_choice <= 4:
    print("თქვენ აირჩიეთ:", vegetables[user_choice])
else:
    print("არასწორი რიცხვი უნდა იყოს 0-დან 4-მდე.")
