from django.contrib import admin

from .models import StartupProfile,stocks
#raman
#from .models import UserProfile

#admin.site.register(UserProfile)

#jogu
# admin.site.register(uid)
# admin.site.register(accounts)
# admin.site.register(InvestorProfile)
admin.site.register(StartupProfile)
# admin.site.register(holdings)
admin.site.register(stocks)
