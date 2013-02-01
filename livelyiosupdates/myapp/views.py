from django.http import HttpResponseRedirectBase

class LivelyHttpResponseRedirect(HttpResponseRedirectBase):
	allowed_schemes = ['http', 'https', 'ftp', 'itms-services']
	status_code = 302


def index(request):
	return LivelyHttpResponseRedirect("itms-services://?action=download-manifest&url=itms-services://?action=download-manifest&url=https://lively-enterprise.s3.amazonaws.com/lively.plist")
