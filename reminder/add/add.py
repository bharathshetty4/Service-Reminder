import configparser


class AddService():
    def __init__(self):
        return None

    def add_service(self, service_data):
        print("called new class", service_data)
        Config = configparser.configparser()
        # TODO: create the file if not there
        config_file = open("/etc/reminder/reminder.conf", 'w')

        Config.add_section(service_data["name"])
        Config.set(service_data["name"], 'date', service_data["date"])
        Config.set(service_data["name"], 'interval', service_data["interval"])
        Config.set(service_data["name"], 'end_date', service_data["enddate"])
        Config.set(service_data["name"], 'time', service_data["time"])
        Config.set(service_data["name"], 'before', service_data["before"])

        # write to and close the conf file
        Config.write(cfgfile)
        cfgfile.close()
