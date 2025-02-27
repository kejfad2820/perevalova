import os
import sys

sys.path.insert(1, 'il/MVP/')

from cogs.config import settings


class FindDB:
    def __init__(self, database_name = settings['database_name']):
        self.database_name = database_name

    def find_database_path(self, start_path = "."):
        dir = os.path.dirname(os.path.abspath(__file__))

        for root, _, files in os.walk(('..')):
            if self.database_name in files:
                print(os.path.join(root, self.database_name))
                return os.path.join(root, self.database_name)
        return None
