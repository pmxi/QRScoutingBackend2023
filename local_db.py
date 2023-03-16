import sqlite3
import datetime


def parse_qr_string(qr_string: str) -> list:
    """Parse a QR string into a list of values"""
    data_l = qr_string.split('\t')
    bool_indices = [4, 5, 7, 14, 15, 16, 25, 30, 31, 32]
    for i in bool_indices:
        if data_l[i] == 'true':
            data_l[i] = 1
        else:
            data_l[i] = 0
    integer_indices = [1, 3, 8, 9, 10, 11, 12, 13, 17, 18, 19, 20, 21, 22, 24, 27]
    for i in integer_indices:
        try:
            data_l[i] = int(data_l[i])
        except ValueError:
            print('ValueError: ' + data_l[i] + ' at index ' + str(i) + ' is not an integer')
            raise ValueError
    data_l.insert(0, datetime.datetime.now(datetime.timezone.utc).isoformat())
    return data_l


class ScoutDB:
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS match_scout(
                        time_submitted TEXT,
                        scouter_initials TEXT,
                        match_number INTEGER,
                        robot TEXT,
                        team_number INTEGER,
                        no_show INTEGER,
                        using_human_player INTEGER,
                        starting_location TEXT,
                        mobility INTEGER,
                        upper_cone_scored_auto INTEGER,
                        middle_cone_scored_auto INTEGER,
                        lower_cone_scored_auto INTEGER,
                        upper_cube_scored_auto INTEGER,
                        middle_cube_scored_auto INTEGER,
                        lower_cube_scored_auto INTEGER,
                        picked_up_more_cube_cone INTEGER,
                        docked INTEGER,
                        engaged INTEGER,
                        upper_cone_scored_teleop INTEGER,
                        middle_cone_scored_teleop INTEGER,
                        lower_cone_scored_teleop INTEGER,
                        upper_cube_scored_teleop INTEGER,
                        middle_cube_scored_teleop INTEGER,
                        lower_cube_scored_teleop INTEGER,
                        pick_up_cube_cone_where TEXT,
                        links INTEGER,
                        attempted_before_endgame INTEGER,
                        charge_station INTEGER,
                        num_alliance_bots_docked INTEGER,
                        driver_skill INTEGER,
                        defense_rating INTEGER,
                        died INTEGER,
                        tipped_over INTEGER,
                        yellow_red_card TEXT,
                        comments TEXT
                        )''')
        self.conn.commit()

    def add_match_from_qr_string(self, data: str):
        data_l = parse_qr_string(data)
        self.cur.execute('''INSERT INTO match_scout VALUES (
                        ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', data_l)
        self.conn.commit()

    def __del__(self):
        self.conn.close()
        print('DB connection closed')
