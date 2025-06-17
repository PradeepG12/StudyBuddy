from djchoices import DjangoChoices, ChoiceItem

class GroupJoinExitConfig(DjangoChoices):

    join = ChoiceItem('join', 'Join')
    exit = ChoiceItem('exit', 'Exit')

class GroupRoleTypeChoices(DjangoChoices):

    admin = ChoiceItem("admin","Admin")
    member = ChoiceItem("member", "member")