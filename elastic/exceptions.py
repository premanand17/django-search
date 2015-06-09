''' Exceptions used in querying. '''


class SettingsError(Exception):
    ''' Query error  '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class QueryError(Exception):
    ''' Query error  '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class FilterError(Exception):
    ''' Filter error  '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class AggregationError(Exception):
    ''' Aggregation error  '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
