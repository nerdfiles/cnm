## Script (Python) "sendExpirationNotification"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=days
##title=
##


from Products.CMFCore.utils import getToolByName

ROLES_TO_NOTIFY = ('ACApprover', 'GroupManager', 'DivisionDirector')

plone_utils = getToolByName(context, 'plone_utils')
portal_groups = getToolByName(context, 'portal_groups')
portal_membership = getToolByName(context, 'portal_membership')
portal = getToolByName(context, 'portal_url').getPortalObject()
mail_host = portal.MailHost
encoding = portal.getProperty('email_charset')
from_address = portal.getProperty('email_from_address')
acquired_roles = plone_utils.getInheritedLocalRoles(context)
recipients = dict()
for name, roles, type, id in acquired_roles:
    for role in ROLES_TO_NOTIFY:
        if role in roles:
            if type == 'group':
                group = portal_groups.getGroupById(id)
                if group is not None:
                    for m in group.getGroupMembers():
                        recipients[m] = True
            else:
                recipients[id] = True
            break

recipient_emails = list()
for recipient in recipients:
    member = portal_membership.getMemberById(recipient)
    if member is not None:
        email = member.getProperty('email')
        if email:
            recipient_emails.append(email)

template = context.expiration_notification_template

subject = 'Content will expire in %s days.' % days
message = template(context, recipients=recipient_emails,
        from_address=from_address, days=days, subject=subject,
        charset=encoding)

mail_host.secureSend(message, recipient_emails, from_address, subject=subject,
        subtype='plain', charset=encoding, debug=False, From=from_address)

