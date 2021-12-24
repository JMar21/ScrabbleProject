import scrabbleBag
import wordCheck
import mysql.connector
import config
conn = mysql.connector.connect(
    host = config.host,user=config.user,password=config.password,database=config.database
)
cursor = conn.cursor()
hand={}
entered=False
if __name__ == '__main__':
    for i in range(1,6):
        letter = scrabbleBag.draw()
        hand[letter] = hand.get(letter , 0)+1
    print("Your hand is "+str(hand))
    response = input("Enter a word using the letters in your hand:").upper()
    cursor.execute("SELECT * FROM dictionary WHERE WORD = %s",(response,))
    result = cursor.fetchone()
    print(result)
    if wordCheck.wordCheck(response,hand):
        print("Valid word entered")
    else:
        print("Invalid word entered")
    conn.close()

