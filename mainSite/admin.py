from django.contrib import admin
from mainSite.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Candidates)
admin.site.register(Votes)
admin.site.register(ChallengeStrings)
admin.site.register(PublicKeys)

