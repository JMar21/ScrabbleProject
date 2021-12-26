#Given a mysql cursor and hand, find the maximum possible score for the given letters
def check_max_score(cursor, hand):
    regex="^["
    for val in hand:
        regex+=str(val)
    regex+="]+$"
    query="SELECT * from dictionary\n" \
          "WHERE Word RLIKE '{}'\n"\
          "ORDER BY Value DESC".format(regex)
    cursor.execute(query)
    result = cursor.fetchall()
    return