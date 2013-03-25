from django.http import HttpResponseRedirectBase
import logging 

logger = logging.getLogger(__name__)

class LivelyHttpResponseRedirect(HttpResponseRedirectBase):
	allowed_schemes = ['http', 'https', 'ftp', 'itms-services']
	status_code = 302


def index(request):
	plist_url = request.GET.get('plist_url', "https://lively-enterprise.s3.amazonaws.com/lively.plist")
	redirect_url = "itms-services://?action=download-manifest&url="+plist_url
	logger.debug("redirecting to "+redirect_url)
	return LivelyHttpResponseRedirect(redirect_url)
