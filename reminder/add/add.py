import configparser
import sys

class AddService():
    def __init__(self):
        return None

    def add_service(self, service_data):
        print("called add class", service_data)
        Config =  configparser.ConfigParser()

        # TODO: check the file in home directory as well


        """
        code to check file in many dirs
        refer: http://stackoverflow.com/questions/7567642/where-to-put-a-configuration-file-in-python
        for loc in os.curdir, os.path.expanduser("~"), "/etc/myproject", os.environ.get("MYPROJECT_CONF"):
            try:
                with open(os.path.join(loc,"myproject.conf")) as source:
                config.readfp( source )
            except IOError:
                pass

        """


        cfg_file = open("/etc/reminder/reminder.conf", 'ab+')

        Config.read_file(cfg_file)
        if(service_data["name"] in Config.sections()):
            print("The given Name \"%s\" already exist, please give some other " \
                  "name and try again"% service_data["name"])
            sys.exit(2)

        Config.clear()

        print(Config.sections())

        Config.add_section(service_data["name"])
        Config.set(service_data["name"], 'date', service_data["date"])
        Config.set(service_data["name"], 'interval', service_data["interval"])
        Config.set(service_data["name"], 'end_date', service_data["enddate"])
        Config.set(service_data["name"], 'time', service_data["time"])
        Config.set(service_data["name"], 'before', service_data["before"])
        print(Config.sections())
        # write to and close the conf file

        Config.write(cfg_file)

        print(Config.sections())
        cfg_file.close()
