from plogin_server.models import Team, Contest, User

swords_usernames = ['obevan', 'leonardo', 'aragorn', 'jake']
tmnt_usernames = ['leonardo', 'rafael', 'michelangelo', 'donatello']
test_usernames = ['test1', 'test2', 'test3', 'test4']

teams_name = ['Sword masters', 'TMNT', 'Test']

def get_user(username):
    return User.objects.get(username=username)

def get_team(name):
    return Team.objects.get(name=name)

# tmnt = Team(name='TMNT', captain=User.objects.get(username='leonardo'))
# swords = Team(name='Sword masters', captain=User.objects.get(username='obevan'))
# test = Team(name='Test', captain=User.objects.get(username='test1'))

# tmnt.save()
# swords.save()
# test.save()

# for un in tmnt_usernames:
#     tmnt.members.add(User.objects.get(username=un))

# for un in swords_usernames:
#     swords.members.add(User.objects.get(username=un))

# for un in test_usernames:
#     test.members.add(User.objects.get(username=un))

# tmnt.save()
# swords.save()
# test.save()

# c1 = Contest(name='TMNT Test', start_timestamp=1529060400, end_timestamp=1529074800)
# c2 = Contest(name='Swords Test', start_timestamp=1529492400, end_timestamp=1529506800)

c1 = Contest.objects.get(name='TMNT Test')
c2 = Contest.objects.get(name='Swords Test')

# c1.save()
# c2.save()

c1.teams.add(Team.objects.get(name='TMNT'))
c1.teams.add(Team.objects.get(name='Test'))
c2.teams.add(Team.objects.get(name='Sword masters'))
c2.teams.add(Team.objects.get(name='Test'))

c1.save()
c2.save()
