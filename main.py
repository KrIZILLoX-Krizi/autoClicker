

import autoclicker_class
from sys import argv

timer_duration = argv[1]
sleep_duration = argv[2]

print('timer_duration: ' + timer_duration)
print('sleep_duration: ' + sleep_duration)

ac_obj = autoclicker_class.AutoClicker(int(timer_duration), int(sleep_duration))
ac_obj.clickFor()