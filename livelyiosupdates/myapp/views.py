from django.shortcuts import redirect

def index(request):
    return redirect("itms-services://?action=download-manifest&url=itms-services://?action=download-manifest&url=https://lively-enterprise.s3.amazonaws.com/lively.plist")
    