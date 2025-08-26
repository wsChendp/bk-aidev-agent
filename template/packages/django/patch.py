from django.utils.functional import cached_property

class PatchFeatures:
    @cached_property
    def minimum_database_version(self):
        if self.connection.mysql_is_mariadb:
            return (10, 4)
        else:
            return (5, 7)
