import configparser
import re
import sys

class SendInvite():
    def __init__(self):
        return None

    def validate_mail(self, mail_address):
        if not re.match(pattern=r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$",string=mail_address):
            return 0
        return 1

    def send_invite(self):
        print "Called send invite"
        Config = configparser.ConfigParser()
        cfg_file = open("/etc/reminder/reminder.conf", 'rb+')
        if (not cfg_file):
            print "Unable to open the conf file, /etc/reminder/reminder.conf"

        Config.read_file(cfg_file)
        options = Config.items(section="EMAIL")
        for i in options:
            if (i[0] == 'username'):
                if (not self.validate_mail(i[1])):
                    print "Inavlid mail address is given in the conf file, " + i[1]
                    sys.exit(2)
                mail_address = i[1]
            elif (i[0] == 'password'):
                mail_password = i[1]
        if (not mail_address or not mail_password):
            print "Email address or password which will be used to send the invite is missing, \n" \
                  "Please Update it in /etc/reminder/reminder.conf under [EMAIL] section as given in sample conf file"

        print "mail address is: " + mail_address
        print "password is: " + mail_password
        #split the string at '@' and call the appropraite provider