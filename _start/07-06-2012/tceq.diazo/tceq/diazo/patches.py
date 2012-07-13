
import logging
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.PythonScripts.standard import url_quote
from Products.TinyMCE.browser.style import TinyMCEStyle


logger = logging.getLogger('tceq.diazo.patches')

cssfmt = '<!-- @import url(%s/++theme++tceq.diazo/static-assets/tceq.css); -->'

def getStyle(self):
    """Returns a stylesheet with all content styles"""

    self.request.response.setHeader('Content-Type', 'text/css')

    registry = getToolByName(aq_inner(self.context), 'portal_css')
    portal_url = getToolByName(aq_inner(self.context), 'portal_url')
    registry_url = registry.absolute_url()
    context = aq_inner(self.context)

    styles = registry.getEvaluatedResources(context)
    skinname = url_quote(aq_inner(self.context).getCurrentSkinName())
    result = []

    for style in styles:
        if (style.getMedia() not in ('print', 'projection')
                and style.getRel() == 'stylesheet'):
            src = "<!-- @import url(%s/%s/%s); -->" % (registry_url,
                    skinname, style.getId())
            result.append(src)
    result.append(cssfmt % portal_url())
    return "\n".join(result)

TinyMCEStyle.getStyle = getStyle
logger.warn('Patching TinyMCEStyle.getStyle.')
