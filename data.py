from enum import Enum
import os

class UserLocalAppdata(Enum):
    
    LOCALAPPDATA = os.getenv('LOCALAPPDATA')
    DBFOLDER = 'ProjectBugCare'
    DBFILE = os.path.join(LOCALAPPDATA, DBFOLDER, 'bugcare.db')

class Colors(Enum):
    NAVIGATION = "#E1E0E1"
    MAIN = "#F8F4F4"
    NAVBUTTONS = "#D4D0C9"