import sqlite3

class Database():
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_db()


    def create_db(self):
        try:
            query = ("CREATE TABLE IF NOT EXISTS users("
                     "id INTEGER PRIMARY KEY, "
                     "user_name TEXT,"
                     "user_phone TEXT,"
                     "telegram_id TEXT);"
                     "CREATE TABLE IF NOT EXISTS place("
                     "id INTEGER PRIMARY KEY,"
                     "name_place TEXT,"
                     "place_address TEXT);"
                     "CREATE TABLE IF NOT EXISTS games("
                     "id INTEGER PRIMARY KEY,"
                     "place_id TEXT,"
                     "date_game TEXT,"
                     "time_game TEXT,"
                     "min_player INTEGER,"
                     "max_player INTEGER,"
                     "price TEXT)")
            self.cursor.executescript(query)
            self.connection.commit()
        except sqlite3.Error as Error:
            print("Ошибка регистрации :", Error)

    def add_user(self, user_name, user_phone, telegram_id):
        self.cursor.execute(f'INSERT INTO users (user_name, user_phone, telegram_id) VALUES(?,?,?)', (user_name, user_phone, telegram_id))
        self.connection.commit()

    def add_game(self, place_id, date_game, time_game, min_player, max_player, price):
        self.cursor.execute(f'INSERT INTO games(place_id, date_game, time_game, min_player, max_player, price) VALUES (?,?,?,?,?,?)', (place_id, date_game, time_game, min_player, max_player, price))
        self.connection.commit()

    def select_user_id(self, telegram_id):
        users = self.cursor.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
        return users.fetchone()

    def db_select_column(self, table_name, column, item):
        result = self.cursor.execute("SELECT * FROM {} WHERE {} = {}".format(table_name, column, item))
        return result

    def db_select_all(self, table_name):
        result = self.cursor.execute("SELECT * FROM {}".format(table_name))
        return result.fetchall()

    def select_games(self, status, date_games):
        result = self.cursor.execute("SELECT * FROM `games` JOIN `place` ON place.id WHERE `status` = '{}' AND `date_game` = '{}'"
                                     .format(status, date_games))
        return result.fetchall()

    def select_game(self, status, game_id):
        result = self.cursor.execute("SELECT * FROM `games` JOIN `place` ON place.id WHERE `status` = '{}' AND `games`.`id` = '{}'"
                                     .format(status, game_id))
        return result.fetchone()

    def add_user_match(self, game_id, user_telegram_id):
        self.cursor.execute(f'INSERT INTO record_matches(game_id, user_telegram_id) VALUES (?,?)',
                            (game_id, user_telegram_id))
        self.connection.commit()

    def delete_user_match(self, game_id, user_telegram_id):
        self.cursor.execute(f'DELETE FROM `record_matches` WHERE game_id = ? AND user_telegram_id = ?',
                            (game_id, user_telegram_id))
        self.connection.commit()

    def select_player(self, game_id):
        result = self.cursor.execute("SELECT * FROM `record_matches` JOIN `users` ON `record_matches`. `user_telegram_id` = `users`.`telegram_id` WHERE `record_matches`.`game_id` = {}".format(game_id))
        return result.fetchall()

    def check_user(self, game_id, user_id):
        result = self.cursor.execute("SELECT * FROM `record_matches` WHERE `game_id` = {} AND `user_telegram_id` = {}".format(game_id, user_id))
        return result.fetchall()


    def __del__(self):
        self.cursor.close()
        self.connection.close()