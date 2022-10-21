import configparser
from typepen import config

class CreateConfig:
    def __init__(self):
        self.config_file = configparser.ConfigParser()
    
    def create_config_file(self, section_name:str, section_settings:dict) -> None:
        ''' Create sections and add settings from a dict object '''

        self.config_file.add_section(section_name)
        
        for skey, svalue in section_settings.items():
            self.config_file.set(section_name, skey, svalue)

        # Save the settings
        with open(config.CF_NAME, "w") as config_object:
            self.config_file.write(config_object)
            config_object.flush()
            config_object.close()
    
    def update_config_file(self, section_name:str, section_settings:dict):
        ''' Update the config file; if one of the keys is not part of it,
            ConfigParser.update method is called
        '''
        self.config_file.read(config.CF_NAME)

        if not self.config_file[section_name]:
            return False
        
        for skey, svalue in section_settings.items():
            k = self.config_file[section_name]
            for sk, sv in k.items():
                if skey == sk:
                    k[sk] = svalue
            else:
                self.config_file[section_name].update({f"{skey}": f"{svalue}"})

        # Save updated version

        with open(config.CF_NAME, "w") as config_object:
            self.config_file.write(config_object)
            
        return True

