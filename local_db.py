import sqlite3
import datetime

from qr_str_parser import parse_qr_string


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
                        charge_station TEXT,
                        num_alliance_bots_docked INTEGER,
                        driver_skill TEXT,
                        defense_rating INTEGER,
                        died INTEGER,
                        tipped_over INTEGER,
                        yellow_red_card INTEGER,
                        comments TEXT,
                        UNIQUE(scouter_initials, match_number, robot, team_number, no_show, using_human_player,
                        starting_location, mobility, upper_cone_scored_auto, middle_cone_scored_auto,
                        lower_cone_scored_auto, upper_cube_scored_auto, middle_cube_scored_auto, lower_cube_scored_auto,
                        picked_up_more_cube_cone, docked, engaged, upper_cone_scored_teleop, middle_cone_scored_teleop,
                        lower_cone_scored_teleop, upper_cube_scored_teleop, middle_cube_scored_teleop,
                        lower_cube_scored_teleop, pick_up_cube_cone_where, links, attempted_before_endgame,
                        charge_station, num_alliance_bots_docked, driver_skill, defense_rating, died, tipped_over,
                        yellow_red_card, comments) ON CONFLICT IGNORE
                        );''')
        self.conn.commit()

    def add_match_from_qr_str(self, data: str):
        data_l = parse_qr_string(data)
        data_l.insert(0, datetime.datetime.now(datetime.timezone.utc).isoformat())
        self.cur.execute('''INSERT INTO match_scout VALUES (
                        ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', data_l)
        self.conn.commit()

    def __del__(self):
        self.conn.close()
        print('DB connection closed')
