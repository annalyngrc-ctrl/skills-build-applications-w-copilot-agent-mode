from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Team')
        dc = Team.objects.create(name='DC', description='DC Team')

        # Create Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel)
        bruce = User.objects.create(email='bruce@banner.com', name='Bruce Banner', team=marvel)
        natasha = User.objects.create(email='natasha@romanoff.com', name='Natasha Romanoff', team=marvel)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc)
        bruce_dc = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc)
        diana = User.objects.create(email='diana@prince.com', name='Diana Prince', team=dc)

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        running = Workout.objects.create(name='Running', description='Cardio', difficulty='Medium')
        squats = Workout.objects.create(name='Squats', description='Lower body', difficulty='Easy')

        # Create Activities
        Activity.objects.create(user=tony, type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='Pushups', duration=15, date=timezone.now().date())
        Activity.objects.create(user=natasha, type='Squats', duration=20, date=timezone.now().date())
        Activity.objects.create(user=clark, type='Running', duration=40, date=timezone.now().date())
        Activity.objects.create(user=bruce_dc, type='Pushups', duration=25, date=timezone.now().date())
        Activity.objects.create(user=diana, type='Squats', duration=35, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=120)
        Leaderboard.objects.create(user=bruce, score=110)
        Leaderboard.objects.create(user=natasha, score=130)
        Leaderboard.objects.create(user=clark, score=140)
        Leaderboard.objects.create(user=bruce_dc, score=125)
        Leaderboard.objects.create(user=diana, score=135)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
