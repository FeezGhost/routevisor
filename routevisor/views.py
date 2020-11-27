from django.shortcuts import render,redirect
# from .forms import *
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from .models import *
# from django.contrib.auth.models import User
# import datetime
# from django.contrib import messages
# import re
# from django.contrib.auth.decorators import login_required
# from .decorators import  unauthenticated_user
# import pytz


# Create your views here.
# @login_required(login_url="homepage")
# def dashboard(request):
#     customer = request.user.customer
#     coins = customer.coins_set.all()
#     immcoins = customer.immaturecoins_set.all()
#     now = datetime.datetime.now().strftime("%m/%d/%Y")
    
#     now2 = datetime.datetime.now(pytz.utc)
#     hour = now.split('/')
    
#     now2 = now2.astimezone(pytz.timezone('Africa/Johannesburg'))
#     month =   int(hour[0])
#     day = int(hour[1])
#     for immcoin in immcoins:
#         monthcreated = int(immcoin.date_created.month)
#         daycreated = int(immcoin.date_created.day)
#         if(month == monthcreated):
#             diff = day - daycreated
#             if( (diff>=5) and (immcoin.days == 5) ):
#                 #add 130 per
#                 immcoin.coins += int(immcoin.coins*1.3) 
#                 totalup = coins[0].total
#                 remainingup = coins[0].remaining
#                 bidedup = coins[0].bided
#                 totalup +=int(immcoin.coins)
#                 remainingup +=int(immcoin.coins)
#                 coinform = CoinsForm({'customer':customer, 'total':totalup,'bided': bidedup, 'remaining': remainingup} ,instance=coins[0])
#                 if coinform.is_valid():
#                     userCoinForm = coinform.save()
#                     immcoin.delete()
#             elif( (diff>=2) and (immcoin.days == 2)):
#                 # add 60 per
#                 immcoin.coins += int(immcoin.coins*0.6) 
#                 totalup = coins[0].total
#                 remainingup = coins[0].remaining
#                 bidedup = coins[0].bided
#                 totalup +=int(immcoin.coins)
#                 remainingup +=int(immcoin.coins)
#                 coinform = CoinsForm({'customer':customer, 'total':totalup,'bided': bidedup, 'remaining': remainingup} ,instance=coins[0])
#                 if coinform.is_valid():
#                     userCoinForm = coinform.save()
#                     immcoin.delete()
#             else:
#                 pass

#         else:
#             daysincrement = 30-daycreated
#             daycreated = 1
#             if  (daysincrement<0):
#                 day += (abs(daysincrement))
#             else:
#                 day += (daysincrement+1)
#             diff = day - daycreated
#             if( (diff>=5) and (immcoin.days == 5) ):
#                 #add 130 per
#                 immcoin.coins += int(immcoin.coins*1.3) 
#                 totalup = coins[0].total
#                 remainingup = coins[0].remaining
#                 bidedup = coins[0].bided
#                 totalup +=int(immcoin.coins)
#                 remainingup +=int(immcoin.coins)
#                 coinform = CoinsForm({'customer':customer, 'total':totalup,'bided': bidedup, 'remaining': remainingup} ,instance=coins[0])
#                 if coinform.is_valid():
#                     userCoinForm = coinform.save()
#                     immcoin.delete()
#             elif( (diff>=2) and (immcoin.days == 2)):
#                 # add 60 per
#                 immcoin.coins += int(immcoin.coins*0.6) 
#                 totalup = coins[0].total
#                 remainingup = coins[0].remaining
#                 bidedup = coins[0].bided
#                 totalup +=int(immcoin.coins)
#                 remainingup +=int(immcoin.coins)
#                 coinform = CoinsForm({'customer':customer, 'total':totalup,'bided': bidedup, 'remaining': remainingup} ,instance=coins[0])
#                 if coinform.is_valid():
#                     userCoinForm = coinform.save()
#                     immcoin.delete()
#             else:
#                 pass
#     bids = customer.bids_set.all().order_by('-date_created')
#     now = now2.strftime('%H:%M:%S')
#     context = {
#         'customer': customer,
#         'coins':  coins,
#         'bids': bids,
#         'now': now,
#     }
#     return render(request, 'dashboard/dist/index.html', context)

def landingView(request):
    return render(request, 'routevisor/landingpage.html')