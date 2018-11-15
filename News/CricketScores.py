import requests as req

URL = 'http://www.cricbuzz.com/match-api/livematches.json'
SERIES_KEYWORDS = ['IND', 'RSA', 'AUS', 'PAK', 'NZ', 'ENG', 'SL', 'SA', 'ZIM', 'BAN', 'IPL']  # short_name


def _fetch_and_parse():
    resp = req.get(URL)
    if resp.status_code == req.codes.ok:
        data = resp.json()
        if len(data['matches']) == 0:
            raise Exception('No scores to display.')
    else:
        raise Exception('No scores to display')

    return _process_data(data['matches'])


def _process_data(matches):
    matches = {id: match_data for id, match_data in matches.items() if _display_this_match(match_data)}
    if len(matches.keys()) == 0:
        raise Exception('no live matches')

    scores = []
    for match in matches.values():
        batting_score, bowling_score = _get_team_scores(match)
        individual_scores = _get_individual_scores(match)
        scores.append('{} | {} | {}'.format(batting_score, individual_scores, bowling_score))

    return scores


def _get_team_scores(match):
    if match['score']['batting']['id'] == match['team1']['id']:
        batting_team, bowling_team = (match['team1'], match['team2'])
    else:
        batting_team, bowling_team = (match['team2'], match['team1'])

    batting_score, bowling_score = match['score']['batting']['score'], match['score']['bowling']['score']
    batting_formatted_score = '{}: {}'.format(batting_team['s_name'], batting_score)
    bowling_formatted_score = '{}: {}'.format(bowling_team['s_name'], bowling_score)

    return batting_formatted_score, bowling_formatted_score


def _get_individual_scores(match):
    batsmen = {}
    for player in match['players']:
        batsmen[player['id']] = player['name']

    batsmen_scores = []
    for batsman in match['score']['batsman']:
        batsmen_scores.append('{}: {}'.format(batsmen[batsman['id']], batsman['r']))

    return ', '.join(batsmen_scores)


def _display_this_match(match):
    keys = filter(lambda key: key in match['series']['short_name'], SERIES_KEYWORDS)
    return bool(keys) and 'score' in match  # needs to be a live match


def beautify(num, msg):
    return '[{0}]\t{1}\n'.format(str(num), msg)


def print_cricket_scores():
    print "=================CRICKET SCORES=================================="
    try:
        parsed_scores = _fetch_and_parse()
        for i, score in enumerate(parsed_scores):
            print beautify(i+1, score)
    except:
        print beautify(0, 'No cricket scores to display.')
    print "***************************************************************"


if __name__ == '__main__':
    print_cricket_scores()
