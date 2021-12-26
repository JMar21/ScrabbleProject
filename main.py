import scrabbleBag
import wordCheck
import mysql.connector
import config
import check_max_score
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
    if result is not None:
        score = result[1]
        print(result)
    check_max_score.check_max_score(cursor,hand)
    if wordCheck.word_check(response, hand) and result:
        print("Valid word entered with score "+str(score))
        for val in response:
            hand[val]-=1
    else:
        print("Invalid word entered")
    conn.close()

