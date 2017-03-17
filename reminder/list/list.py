import configparser

class ListService():
    def __init__(self):
        return None

    def list_service(self):
        print("called list class ")
        Config = configparser.ConfigParser()

        cfg_file = open("/etc/reminder/reminder.conf", 'rb+')
        if (cfg_file):
            print ("opened config file here")

        Config.read_file(cfg_file)
        sections = Config.sections()

        for section in sections:
            print ("section : ",section)
            print ("options: ",Config.items(section))

        cfg_file.close()
