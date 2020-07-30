import json
import math
import os

import requests


def millify(n):
    """Abbreviate a number to nearest thousand, million, etc.

    Adapted from: https://stackoverflow.com/a/3155023/10696164

    Parameters
    ----------
    n : int
        The number to abbreviate

    Returns
    -------
    millified : str
        The number abbreviated to the nearest thousand, million, etc.
    """
    millnames = ['', 'k', 'M', 'B', 'T']
    n = float(n)
    millidx = max(
        0,
        min(
            len(millnames) - 1,
            int(math.floor(0 if n == 0 else math.log10(abs(n)) / 3))
        )
    )
    final_num = float(n / 10 ** (3 * millidx))
    one_decimal = round(final_num, 1)

    # If the number is in the millions, and has a decimal, we want to show one
    # decimal. I.e.:
    #  - 967123  -> 967k
    #  - 1000123 -> 1M
    #  - 1100123 -> 1.1M
    final_output = one_decimal if n > 1e3 and not one_decimal.is_integer() else int(round(final_num, 1))

    return f'{final_output}{millnames[millidx]}'


# Dict of gh username to stack overflow ID
people_to_update = {
    'tgsmith61591': '3015734',
    'aaronreidsmith': '10696164'
}

# Open a session to save time
session = requests.Session()

new_data = {}
for gh_user, so_id in people_to_update.items():
    response = session.get(
        url=f'https://api.stackexchange.com/2.2/users/{so_id}?site=stackoverflow'
    ).json()
    new_reputation = millify(int(response['items'][0]['reputation']))
    new_data[gh_user] = new_reputation
    print(f'New reputation for {gh_user}: {new_reputation}')

request = session.post(
    url='https://store.zapier.com/api/records',
    headers={
        'X-Secret': os.getenv('ZAPIER_SHA')
    },
    data=json.dumps(new_data)
)
request.raise_for_status()
