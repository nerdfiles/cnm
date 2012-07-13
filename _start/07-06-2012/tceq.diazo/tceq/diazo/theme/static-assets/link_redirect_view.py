"""
Redirect to the Link target URL, if and only if:
 - redirect_links property is enabled in portal_properties/site_properties
 - AND current user doesn't have permission to edit the Link
"""

from Products.CMFCore.utils import getToolByName

ptool = getToolByName(context, 'portal_properties')
mtool = getToolByName(context, 'portal_membership')

redirect_links = getattr(ptool.site_properties, 'redirect_links', False)
can_edit = mtool.checkPermission('Modify portal content', context)

ownerRoles = ('Owner', 'Manager', 'Editor')
if not can_edit:
    member = mtool.getAuthenticatedMember()
    for role in member.getRolesInContext(context):
        if role in ownerRoles:
            can_edit = True

if redirect_links and not can_edit:
    return context.REQUEST.RESPONSE.redirect(context.getRemoteUrl())
else:
    # link_view.pt is a template in the plone_content skin layer
    return context.link_view()

