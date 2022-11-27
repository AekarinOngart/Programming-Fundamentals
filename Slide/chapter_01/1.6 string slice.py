#---------------------------------------------
#* String slicing
#* String สามารถแยกออกเป็นตัวอักษรได้ โดยเริ่มจาก 0
#*
#* str1 = 'Hello World!'
#* str1[6] =  W
#* str1[1:5] = ello
#---------------------------------------------

str1 = 'Hello World!'
print (str1[6])
print (str1[1:5])

#---------------------------------------------
#* นอกจากนั้นยังอ้างจากท้ายได้ด้วย
#---------------------------------------------
word = 'Python'
word[-1] = 'n'
word[-2] = 'o'
#word[5] = ??

#---------------------------------------------
#* กรณีไม่ใส่หมายถึงที่เหลือ
#---------------------------------------------
s1 = "Python Programming"
print(s1[7:])
print(s1[-11:])


#---------------------------------------------
#* และอ้างแบบกระโดดได้ด้วย
#---------------------------------------------
s = '0123456789'
#* s[2:8:2] = '246'

#* s[:5] = '01234'
#* s[4:] = '456789'
#* s[::3] = '0369'
#*s[::-2] = '97531'


#| Ex.1.18 จงหา s[-1:2:-2] จากรหัสนักศึกษาของตัวเอง 

#| Ex.1.19 s = "ABCDEFG" จงหา
#| s[::-1]
#| s[-1::-1]
#| s[-1:-(len(s)+1):-1]

#---------------------------------------------
#* operator in กับ string
#* 'k' in "kmitl"
#---------------------------------------------

var1 = "hello world"
var2 = var1[:6] + 'Python language'

print (var2)

#* เราไม่สามารถแก้ไขข้อมูลใน String ได้ 
#* เช่น s[2] = 'a' ไม่ได้
#* แต่ถ้าเขียน s = s[:2] + 'a' + s[3:] สามารถทำได้

#| Ex.1.19 ให้เขียนโปรแกรมรับข้อมูลจาก Keyboard 2 ค่า คือ รหัสนักศึกษา และ ชื่อ 
#| จากนั้นแสดงผลในรูปแบบ 
#| "Student ID : [xx] Name : [nn] " ขึ้นบรรทัดใหม่ 
#| Year Entry : [แสดงปีที่รับเข้า] Last 4 Didit : [] Department : Computer Engineering 