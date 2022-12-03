import os
import sys
from datetime import date

import browser_cookie3
import requests

#Get cookies from the browser
# cj = browser_cookie3.firefox()
# if not (".adventofcode.com" in str(cj)):
cj = browser_cookie3.chrome()

#Get today number of day
day_today = date.today().strftime("%d").lstrip("0")

#If we provide an argument, use it as the desired day. Ex: ./startDay.py 5. Otherwise use day_today
if len(sys.argv) > 1:
    day = int(sys.argv[1])
    if day<0 or day>31 or day>int(day_today):
        exit("Day is not valid")
else:
    day = day_today


print(f"Initializing day {day}")

# download inputs
if not os.path.exists(f"day{day}"):
    os.mkdir(f"day{day}")

    # copy template
    os.system(f"cp ./solution_template.py day{day}/solution.py")

    os.chdir(f"day{day}")

    headers = {'User-Agent': 'Mozilla/5.0'}

    r = requests.get(f"https://adventofcode.com/2022/day/{day}/input", cookies = cj, headers=headers)
    with open(f"inputs.txt","w") as f:
        f.write(r.text)

else:
    print(f"day{day} already initialized, aborting")
