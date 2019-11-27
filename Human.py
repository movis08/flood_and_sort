class Human(dict):
    """
    Человек с возрастом ))
    """

    def __init__(self, age, **kwargs):
        super().__init__()

        self['age'] = age
        for index, value in kwargs.items():
            self[index] = value

    def __eq__(self, other):
        return self['age'] == other['age']

    def __ne__(self, other):
        return self['age'] != other['age']

    def __lt__(self, other):
        return self['age'] < other['age']

    def __le__(self, other):
        return self['age'] <= other['age']

    def __gt__(self, other):
        return self['age'] > other['age']

    def __ge__(self, other):
        return self['age'] >= other['age']
