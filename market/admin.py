from django.contrib import admin

from .models import holdings,onSaleInvestor,onSaleStartup #
#raman
# from .models import UserProfile

# admin.site.register(UserProfile)

#jogu
admin.site.register(onSaleInvestor)
admin.site.register(onSaleStartup)
# admin.site.register(InvestorProfile)
# admin.site.register(StartupProfile)
admin.site.register(holdings)
# admin.site.register(stocks)