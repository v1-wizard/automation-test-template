import os

from pyhocon import ConfigFactory

conf = ConfigFactory.parse_file('reference.conf')


# THIS IS PROPERTY EXAMPLE REMOVE IT AND CREATE YOUR OWN.
DUMMY = os.environ.get('DUMMY', conf.get_string('conf.dummy'))

SETTINGS_TEXT = f'''Test configuration:
---------------------------------------------------------
DUMMY = {DUMMY}
---------------------------------------------------------'''
