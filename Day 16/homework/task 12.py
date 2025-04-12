"""შექმენით პროგრამა while ციკლით რომელიც მომხარებელს შეეკითხება pin კოდს (4 ციფრიანი კოდი) იქამდე სანამ არ შემოიყვანს სწორად, საბოლოოდ დაუბეჭდეთ რომ გაიარა ავტორიზაცია და გამოუტანეთ თუ რამდენი ცდა დასჭირდა""" 
counter = 0
password = "9876" 
a = input("enter your password")
while a != "9876" : 
    a = input("enter your password") 
    counter += 1 
print(counter)
