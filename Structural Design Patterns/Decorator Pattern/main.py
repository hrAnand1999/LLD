from notifierClass import Notifier
from slackNotifier import Slack
from facebookNotifier import Facebook
from smsNotifier import SMS

def main():
    fireAlarm = Notifier()
    fireAlarm.notify("Fire in the house")

    fireAlarm = Slack(Facebook(SMS(fireAlarm)))
    fireAlarm.notify("Fire in the company")

if __name__ == '__main__':
    main()