from django.contrib import admin

from .models import accounts,uid,Inv,Sp,stocks,holdings

#raman
from .models import UserProfile

admin.site.register(UserProfile)

#jogu
admin.site.register(uid)
admin.site.register(accounts)
admin.site.register(Inv)
admin.site.register(Sp)
admin.site.register(holdings)
admin.site.register(stocks)
