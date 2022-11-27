#-------------------------------------------------
#* Blackjack Project
#*
#* เป็นการสร้างเกมไพ่ Blackjack 
#* ทดลองเล่นได้ที https://games.washingtonpost.com/games/blackjack/
#*
#* Blackjack House Rules:
#*      1. จำนวนไพ่มีไม่จำกัดชุด
#*      2. ไม่มี Joker
#*      3. Jack/Queen/King เท่ากับ 10
#*      4. Ace สามารถนับเป็น 1 หรือ 11 ก็ได้
#*
#* จะใช้ list ต่อไปนี้
#*      cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#*
#* การแจกไพ่จะมีโอกาสออกเท่าๆ กัน และไพ่ที่แจกแล้วจะไม่เอาออกจากกอง 
#* ให้คอมพิวเตอร์เป็นคนแจกไพ่

### Requirement 
# 1. สุ่มแจกไพ่ user และ computer ข้างละ 2 ใบ
# 2. ตรวจสอบว่าเป็น Blackjack หรือไม่ (A + ไพ่แต้ม 10)
# 3. ถ้า computer ได้ Blackjack ผู้เล่นจะแพ้ แม้ว่า user จะได้เหมือนกัน ถ้า user ได้ Blackjack ก็ชนะไปเลย 
# 4. คำนวณคะแนนของ user และ computer 
# 5. ถ้าแจกไพ่ A จะนับเป็น 11 แต่ถ้าคะแนนเกิน 21 จะนับเป็น 1 
# 6. เปิดไพ่ใบแรกของ computer ให้ user เห็น 
# 7. เกมจะจบเมื่อ user ได้คะแนน > 21 หรือได้ blackjack
# 8. ถามผู้ใช้ว่าจะเอาไพ่เพิ่มหรือไม่ 
# 9. เมื่อ user ไม่ต้องการไพ่เพิ่ม computer จะเอาไพ่เพิ่มหากได้คะแนน < 16
# 10. เปรียบเทียบคะแนนระหว่าง user กับ computer ว่าใครชนะ แพ้ หรือเสมอ
# 11. แสดงหน้าไพ่ของทั้ง 2 ข้าง 
# 12. ถามว่าจะเล่นต่อหรือไม่ 

### แนะนำฟังก์ชัน 
# 1. deal_card() สำหรับแจกไพ่
# 2. calculate_score(cards) คิดคะแนน
# 3. compare(user_score, computer_score)

# ### แนะนำส่วน main 
# 1. แจก user และ computer 2 ใบ โดยใช้ deal_card() และแสดงไพ่ของ computer 1 ใบ
# 2. ทุกครั้งที่แจกไพ่ ให้ตรวจสอบคะแนน โดยใช้ calculate_score() ถ้า computer หรือ user ได้ blackjack 
#    หรือคะแนน > 21 เกมจบ
# 3. ถ้าเกมยังไม่จบ ถาม user ต้องการไพ่เพิ่มหรือไม่ ถ้าต้องการให้เรียก deal_card() เพื่อเพิ่มไพ่ใน user list แต่ถ้าไม่ก็จบเกม
# 4. เมื่อผู้ใช้เสร็จ คอมพิวเตอร์เพิ่มไพ่ให้ตัวเอง ถ้าจนกว่าจะ > 16 
# 5. ตัดสินว่าใครชนะ 
# 6. ถามว่าจะกลับไปเล่นใหม่หรือไม่ 



### ตัวอย่างการทำงาน 
# Do you want to play a game of Blackjack? Type 'y' or 'n': y
#    Your cards: [10, 10], current score: 20
#    Computer's first card: 5
# Type 'y' to get another card, type 'n' to pass: n
#    Your final hand: [10, 10], final score: 20
#    Computer's final hand: [5, 4, 9], final score: 18
# You win 😃
# Do you want to play a game of Blackjack? Type 'y' or 'n': y
#    Your cards: [2, 7], current score: 9
#    Computer's first card: 8
# Type 'y' to get another card, type 'n' to pass: y
#    Your cards: [2, 7, 10], current score: 19
#    Computer's first card: 8
# Type 'y' to get another card, type 'n' to pass: n
#    Your final hand: [2, 7, 10], final score: 19
#    Computer's final hand: [8, 11], final score: 19
# Draw 🙃
# Do you want to play a game of Blackjack? Type 'y' or 'n': 


"Draw 🙃"
"Lose, opponent has Blackjack 😱"
"Win with a Blackjack 😎"
"You went over. You lose 😭"
"Opponent went over. You win 😁"
"You win 😃"
"You lose 😤"
