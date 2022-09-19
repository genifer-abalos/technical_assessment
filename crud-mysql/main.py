import mysql.connector
from datetime import datetime, timedelta

db = mysql.connector.connect(
    host="localhost",
    user="root",
    database="mega"
)

my_cursor = db.cursor()

# print(my_cursor)
def age_verification(birthdate):
    # ver = birthdate + timedelta(days=7665)    # approx
    year_current = '{:%Y}'.format(datetime.now())
    # print(year_current)
    year_current_minus_21 = int(year_current) - 21
    # print(year_current_minus_21)
    # print(type(birthdate))
    birth_year = birthdate.split("-")[0]
    # print(birth_year)

    if int(birth_year) <= year_current_minus_21:
        print(">21")
        return True
    return False


# age_verification('1997-08-14')

def add_player(player_id, first_name, last_name, birthdate, gender, status):
    try:
        of_legal_age = age_verification(birthdate)
        print(of_legal_age)
        if of_legal_age:
            my_cursor.execute(" \
                              INSERT INTO `players`(`player_id`, `first_name`, `last_name`, `birthdate`, `gender`, `status`, `created_at`) VALUES (%s,%s,%s,%s,%s,%s,%s) \
                              ", (player_id, first_name, last_name, birthdate, gender, status, datetime.now()))
            db.commit()
            # print(my_cursor.fetchall())
            for x in my_cursor:
                print(x)
            print(f"Player {player_id} successfully added")
        else:
            print(f"Player is <21 years old")
    except mysql.connector.errors.IntegrityError as e:
        print(f"Duplicate value for player id {player_id}")


def update_player(player_id, first_name, last_name, birthdate, gender, status):
    my_cursor.execute(" \
    UPDATE `players` SET `player_id`=%s,`first_name`=%s,`last_name`=%s,`birthdate`=%s,`gender`=%s,`status`=%s,`created_at`=%s WHERE player_id=%s \
      ", (player_id, first_name, last_name, birthdate, gender, status, datetime.now(), player_id))
    db.commit()


def delete_player(player_id):
    my_cursor.execute(" \
                      DELETE FROM `players` WHERE player_id = %s \
                      ", (player_id,))
    db.commit()
    print(f"Deleted player id {player_id} successfully")


def view_players():
    my_cursor.execute("SELECT * FROM Players")
    for x in my_cursor:
        print(x)


# add_player('genifer','Genifer', 'Abalos', '2001-08-14', 'female', 'active')
# view_players()
# delete_player('genifer')
# view_players()
# update_player('genifer','Fer', 'Abalos', '1997-08-14', 'female', 'active')
# view_players()

def player_ui():
    print("-------------------")
    print("MENU")
    print(f"1 - Create New Player")
    print(f"2 - View Players")
    print(f"3 - Update a Player")
    print(f"4 - Delete a Player")
    print(f"5 - Exit")

    fnc = input("What do you want to do? ")
    match fnc:
        case '1':
            # player_id, first_name, last_name, birthdate, gender, status
            player_id = input("*Player id: ")
            first_name = input("*First name: ")
            last_name = input("*Last name: ")
            birthdate = input("*Birthdate [YYYY-MM-DD]: ")
            gender = input("*Gender['male', 'female']: ")
            status = input("*Status['active','inactive','banned']: ")
            add_player(player_id, first_name, last_name, birthdate, gender, status)
            return True
        case '2':
            view_players()
            return True
        case '3':
            player_id = input("*Player id: ")
            first_name = input("*First name: ")
            last_name = input("*Last name: ")
            birthdate = input("*Birthdate [YYYY-MM-DD]: ")
            gender = input("*Gender['male', 'female']: ")
            status = input("*Status['active','inactive','banned']: ")
            update_player(player_id, first_name, last_name, birthdate, gender, status)
            return True
        case '4':
            view_players()
            player_id = input("Delete which player id? ")
            delete_player(player_id)
            return True
        case '5':
            return False


if __name__ == '__main__':
    stat = True
    while stat is True:
        stat = player_ui()
        # print(stat)


