from enum import Enum
import os

class UserLocalAppdata(Enum):
    
    LOCALAPPDATA = os.getenv('LOCALAPPDATA')
    DBFOLDER = 'ProjectBugCare'
    DBFILE = os.path.join(LOCALAPPDATA, DBFOLDER, 'bugcare.db')