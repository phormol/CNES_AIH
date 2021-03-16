from configparser import ConfigParser
import os.path
from pathlib import Path

def config(section='elk'):
    # create constant envfile
    file_env = Path(__file__).parent / "parameters.ini"
    ENVFILE = file_env
    #print(os.path.exists(ENVFILE))
    parser = ConfigParser()
    parser.read(ENVFILE)
    
    # get section, default to postgresql
    db = {}
    
    # Checks to see if section (postgresql) parser exists
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
         
    # Returns an error if a parameter is called that is not listed in the initialization file
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, ENVFILE))
 
    return db