#---------------------------------------------
#* ชนิดข้อมูลมี 4 ชนิด string, int, float, boolean 
#---------------------------------------------

#---------------------------------------------
#* เราทราบว่า String ใช้เก็บข้อความ แต่สามารถระบุเป็นตัวอักษรได้ด้วย
#---------------------------------------------

print("Hello"[0])
print ("123"+"456") # จะได้อะไร 

#---------------------------------------------
#* Integer ใช้เก็บตัวเลขจำนวนเต็ม
#---------------------------------------------

print(123+456)

#---------------------------------------------
#* Float ใช้เก็บตัวเลขจำนวนทศนิยม
#---------------------------------------------

print(3.14)

#---------------------------------------------
#* Boolean ใช้เก็บตัวเลข True, False
#---------------------------------------------

print(1==1)
print(1==2)
print(True)

#---------------------------------------------
#* ตัวแปรมี 4 ชนิด เช่นกัน
#---------------------------------------------

a = "hello"     #! String
print(a)
print(type(a))

a = 10          #! integer
print(a)
print(type(a))

a = 10.0        #! Float
print(a)
print(type(a))

a = True        #! boolean
print(a)
print(type(a))

#---------------------------------------------
#* การใช้ตัวแปร ทำให้สะดวกต่อการใช้งาน สามารถนำไปใช้ได้หลายครั้ง
#---------------------------------------------

message = "Hello"
name = "Peter"
print(message)
print(message+name)

a = 1; b = 2.0
c = a + b
print(c)

a = 1 < 2
print(a)

a,b = 5,6
print(a + b, a * b)

a,b = 4,5 
a,b = b,a
print(a,b)

a=b=c=1
print(a,b,c)

#---------------------------------------------
#* บางครั้งเราอาจต้องมีการแปลงชนิด
#---------------------------------------------

num_char = len(input("Enter your name :"))
print("Your name has " + num_char + " charecters.")

# จะพบว่ามี Error 

#---------------------------------------------
#* การแปลงจาก string เป็น int จะใช้ int() 
#* การแปลงจาก int เป็น string จะใช้ str() 
#---------------------------------------------

num_char = len(input("Enter your name :"))
print("Your name has " + str(num_char) + " charecters.")

a="123"
b="21"
print(a+b)
print(int(a)+int(b))
print(70+float(100.5))

#| Ex1.7 ให้เขียนโปรแกรมรับตัวเลข 2 หลัก และเอาแต่ละหลักบวกกัน
#| เช่น input เป็น 35 ให้แสดงผล 8 (3+5)

#---------------------------------------------
#* ถ้า string มีอักขระพิเศษ จะขึ้นต้นด้วย \
#* ถ้าต้องการแสดง " ให้ใช้ \" หรือ ' ให้ใช้ \'
#---------------------------------------------

print("\tPython")
print("Hello\nPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#| Ex1.8 ให้เขียนคำสั่งที่พิมพ์ I'm computer engineer. เป็น 3 บรรทัด
#|        ในคำสั่งเดียว

#---------------------------------------------
#* กรณีข้อความมีตัวอักษร ' หรือ "
#---------------------------------------------

message = 'One of Python's strengths is its diverse community.'
print(message)
print("I'm Python.")
print('''I'm "Python".''')
print("""I'm "Python".""")

#---------------------------------------------
#* การรับค่าข้อมูลที่เป็นสตริง
#? <variable> = input("text")

#* การรับค่าข้อมูลที่เป็นตัวเลข 
#? <variable> = int(input("text")) หรือ <variable> = float(input("text"))
#---------------------------------------------

name = input("What’s you name : ")
print("Your name is :",name)

print(message)






