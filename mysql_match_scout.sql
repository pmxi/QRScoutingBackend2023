CREATE TABLE IF NOT EXISTS match_scout
(
    time_submitted            TEXT,
    scouter_initials          TEXT,
    match_number              INTEGER,
    robot                     TEXT,
    team_number               INTEGER,
    no_show                   INTEGER,
    using_human_player        INTEGER,
    starting_location         TEXT,
    mobility                  INTEGER,
    upper_cone_scored_auto    INTEGER,
    middle_cone_scored_auto   INTEGER,
    lower_cone_scored_auto    INTEGER,
    upper_cube_scored_auto    INTEGER,
    middle_cube_scored_auto   INTEGER,
    lower_cube_scored_auto    INTEGER,
    picked_up_more_cube_cone  INTEGER,
    docked                    INTEGER,
    engaged                   INTEGER,
    upper_cone_scored_teleop  INTEGER,
    middle_cone_scored_teleop INTEGER,
    lower_cone_scored_teleop  INTEGER,
    upper_cube_scored_teleop  INTEGER,
    middle_cube_scored_teleop INTEGER,
    lower_cube_scored_teleop  INTEGER,
    pick_up_cube_cone_where   TEXT,
    links                     INTEGER,
    attempted_before_endgame  INTEGER,
    charge_station            TEXT,
    num_alliance_bots_docked  INTEGER,
    driver_skill              TEXT,
    defense_rating            INTEGER,
    died                      INTEGER,
    tipped_over               INTEGER,
    yellow_red_card           INTEGER,
    comments                  TEXT
);