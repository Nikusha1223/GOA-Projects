"""4) შექმენით 5 ცვლადი, რომლებშიც შეინახავთ განსხვავებულ ლოგიკურ და შედარების ოპერაციათა შედეგებს (უნდა იყოს შედარების და ლოგიკური ოპერატორები ერთად მაგალითად temperature > 30 and not cloudy), გვერდზე კომენტარის საშვალებით მიუწერეთ ეს შედეგი (boolean მნიშვნელობა) აიღეთ მრავალფეროვანი კომბინაციები""" 

temperature = 25 
cloudy = 4 
op1 = 5 
op2 = 10 
op3 = 11 

print(temperature > 10 and cloudy < op1) #true
print(temperature < 10 or cloudy > op1) #false
print(op3 > op1 and temperature > cloudy) #true 
print(temperature == cloudy or op2 > op1) #true 
print(cloudy < temperature != op1) #true 
print(not temperature) #false 
print(not cloudy and op2 > op3) #false
