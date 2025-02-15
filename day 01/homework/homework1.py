name = "luka"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშნელობის მიმნიჭებელი სიმბოლო
# "luka" ცვლადისთვის მნიშვნელობა 

surname = "roinishvili"

print(name)
#პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

name = "luka" #ეს არის str (string) ტიპის ცვლადი
age = 11 #ეს არის int (integer) მთელი რიცხვი
height = 147.5 #ეს არის float ტიპის ცვლადი (ათწილადი)
#boolean (boal) ტიპის ცვლადი

knows_programming = True  #true ან false
is_ugly = False  #snakecase(უბრალოდ წერის სტილი სტანდარტულად)

isugly = False # ჯავასკრიპტული camlecase


print(name + " " + surname)

#სტრინგი არის ბრჭყალებში მოცემული სიმბოლოები
#print(name + age)

#print(type(age))
#print(type(name))
#print(type (surname))
#print(type(height))
#print(type(knows_programming))

print(name + " " + str(age))