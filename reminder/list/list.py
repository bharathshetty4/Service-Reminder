import configparser

class ListService():
    def __init__(self):
        return None

    def list_service(self):
        Config = configparser.ConfigParser()

        cfg_file = open("/etc/reminder/reminder.conf", 'rb+')
        if (not cfg_file):
            print "Unable to open the conf file, /etc/reminder/reminder.conf"

        Config.read_file(cfg_file)
        sections = Config.sections()
        print "Added Services are:"
        for section in sections:
            #do not show email info while listing the service list
            if (section == "EMAIL"):
                continue
            print "\n   Name: "+ section
            options = Config.items(section=section)
            for i in options:
                print "   "+ i[0] + ": " +i[1]


        cfg_file.close()
