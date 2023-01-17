


from pyautogui import click
from time import sleep


class AutoClicker:

    def clickOnce(self):
        print('clickOnce()')
        click(10, 10)
        return

    def clickFor(self):
        i = 0
        print('clickFor()')
        while i < self.timer_duration:
            print('i: ' + str(i))
            for count in range(self.sleep_duration):
                sleep(1)
                print(i + count + 1)
            self.clickOnce()
            i = i + self.sleep_duration

        return

    def __init__(self, timer_duration, sleep_duration):
        print('AutoClicker object created.')
        self.timer_duration = timer_duration
        self.sleep_duration = sleep_duration
        print('self.timer_duration: ' + str(self.timer_duration))
        print('self.sleep_duration: ' + str(self.sleep_duration))
