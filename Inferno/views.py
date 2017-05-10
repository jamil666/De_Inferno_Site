import requests
from django.shortcuts import render
from Inferno_Site.settings import STATIC_URL
from .models import WFAccount

def main(request):
    wfaccounts = WFAccount.objects.all()


    context = {"wfaccounts": wfaccounts}
    return render(request, "main.html", context)


def profile(request, userinfo):
    AccountURL = 'http://api.warface.ru/user/stat/?name=%s&server=2' %userinfo
    AccountData = requests.get(AccountURL)
    AccountDataJson = AccountData.json()

    wfaccounts = WFAccount.objects.all()

    DB_search = wfaccounts.get(Name=AccountDataJson["nickname"])
    DB_search.RankImage = "%simages/Ranks/Rank%s.png" %(STATIC_URL, AccountDataJson["rank_id"])
    DB_search.save()

    context = {"AccountName": AccountDataJson["nickname"],
               "AccountRank": AccountDataJson["rank_id"],
               "AccountRankIcon": "%simages/Ranks/Rank%s.png" %(STATIC_URL, AccountDataJson["rank_id"]),
               "AccountFavoritePVP": AccountDataJson["favoritPVP"],
               "AccountFavoritePVE": AccountDataJson["favoritPVE"],
               "AccountPVEwins": AccountDataJson["pve_wins"],
               "AccountPVPwins": AccountDataJson["pvp_wins"],
               "AccountStat": AccountDataJson["pvp"],
               "AccountExpirience": AccountDataJson["experience"],
               "AccountPVPKills": AccountDataJson["kill"],
               "AccountPVPdeath": AccountDataJson["death"],
               "AccountURL": "https://wfts.su/profile/%s" %userinfo,
               "AccountPVPURL": "https://wfts.su/pvp/%s" % userinfo,
               "AccountPVEURL": "https://wfts.su/pve/%s" % userinfo,
               }

    return render(request, 'profile.html', context)

def clan(request):
        wfaccounts = WFAccount.objects.all()

        context = {"wfaccounts": wfaccounts}
        return render(request, 'clan.html', context)