import tomllib
import sqlite3

with open('config.toml', 'rb') as f:
    config = tomllib.load(f)


def main():
    conn = sqlite3.connect(config['database_file'])
    cur = conn.cursor()
    cur.execute('''SELECT * FROM match_scout''')
    rows = cur.fetchall()
    with open(config['output_file'], 'w') as output_file:
        for row in rows:
            output_file.write(','.join([str(x) for x in row]) + '\n')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
