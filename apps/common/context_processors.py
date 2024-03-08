from apps.general.models import SiteDetail


def SiteDetailProcessor(request):
    site, created = SiteDetail.objects.get_or_create()

    site =  {
        "name": site.name,
        "email": site.email,
        "desc": site.desc,
        "fb": site.fb,
        "X": site.x,
        "ig": site.ig,
        "pt": site.pt,
        "website":site.website
    }

    return {"site":site}
