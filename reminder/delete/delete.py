import configparser


class DeleteService():
    def __init__(self):
        return None

    def delete_service(self, service_data):
        print("called delete class", service_data)
        Config = configparser.ConfigParser()

        cfg_file = open("/etc/reminder/reminder.conf", 'ab+')
        if (cfg_file):
            print ("opened config file here")

        Config.read_file(cfg_file)

        print(Config.sections())

        if(Config.has_section(service_data["name"])):
            cfg_file.close()
            cfg_file = open("/etc/reminder/reminder.conf", 'w')
            Config.remove_section(service_data["name"])
            Config.write(cfg_file)

        else:
            print("The given Name \"%s\" doesnot exist, please give the correct " \
                  "name and try again" % service_data["name"])
        print(Config.sections())
        #
        # write to and close the conf file
        #Config.clear()
        cfg_file.close()