from djchoices import DjangoChoices, ChoiceItem

class GroupJoinExitConfig(DjangoChoices):

    join = ChoiceItem('join', 'Join')
    exit = ChoiceItem('exit', 'Exit')