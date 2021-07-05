from django.utils.translation import ugettext_lazy as _

# Permissions Bits List

only_system_admin_permissions_bits = {
    'delete_user': _('Delete user'),
    'add_role': _('Create role'),
    'change_role': _('Update role'),
    'delete_role': _('Delete role'),
    'view_role': _('View role'),
    'view_permission': _('View all permission bit'),
    'add_organization': _('Create organization'),
    'change_organization': _('Update organization'),
    'delete_organization': _('Delete organization'),
    'view_organization': _('View organization'),
    'change_license': _('Update license'),
    'change_interface': _('Update interface'),
    'change_setting': _('Update system setting'),
    'view_setting': _('View system setting'),
}

_org_admin_permissions_bits = {
    'add_user': _('Create user'),
    'change_user': _('Update user'),
    'remove_user': _('Remove user'),
    'view_user': _('View user'),
    'add_usergroup': _('Create user group'),
    'change_usergroup': _('Update user group'),
    'delete_usergroup': _('Delete user group'),
    'view_usergroup': _('View user group'),
    'add_accesskey': _('Add access key'),
    'delete_accesskey': _('Delete access key'),
    'view_accesskey': _('View access key'),
    'add_privatetoken': _('Create private token'),
    'add_ssotoken': _('Create SSO token'),
    'add_loginacl': _('Create user login rules'),
    'change_loginacl': _('Update user login rules'),
    'delete_loginacl': _('Delete user login rules'),
    'view_loginacl': _('View user login rules'),
    'add_loginassetacl': _('Create login asset access control'),
    'change_loginassetacl': _('Update login asset access control'),
    'delete_loginassetacl': _('Delete login asset access control'),
    'view_loginassetacl': _('View login asset access control'),
    'add_rolebinding': _('Create User role binding'),
    'change_rolebinding': _('Update user role binding'),
    'view_rolebinding': _('View user role binding'),
    'delete_rolebinding': _('Delete user role binding'),
    'add_organizationmember': _('Add organization member'),
    'remove_organizationmember': _('Remove organization member'),
    'view_organizationmember': _('View organization member'),
    'add_node': _('Create node'),
    'change_node': _('Update node'),
    'delete_node': _('Delete node'),
    'view_node': _('View node'),
    'add_asset': _('Create asset'),
    'change_asset': _('Update asset'),
    'delete_asset': _('Delete asset'),
    'view_asset': _('View asset'),
    'add_favoriteasset': _('Add favorite asset'),
    'add_assetuser': _('Create asset user'),
    'change_assetuser': _('Update asset user'),
    'delete_assetuser': _('Delete asset user'),
    'view_assetuser': _('View asset user'),
    'add_adminuser': _('Create admin user'),
    'change_adminuser': _('Update admin user'),
    'delete_adminuser': _('Delete admin user'),
    'view_adminuser': _('View admin user'),
    'add_systemuser': _('Create system user'),
    'change_systemuser': _('Update system user'),
    'delete_systemuser': _('Delete system user'),
    'view_systemuser': _('View system user'),
    'add_label': _('Create label'),
    'change_label': _('Update label'),
    'delete_label': _('Delete label'),
    'view_label': _('View label'),
    'add_domain': _('Create domain'),
    'change_domain': _('Update domain'),
    'delete_domain': _('Delete domain'),
    'view_domain': _('View domain'),
    'add_gateway': _('Create gateway'),
    'change_gateway': _('Update gateway'),
    'delete_gateway': _('Delete gateway'),
    'view_gateway': _('View gateway'),
    'add_commandfilter': _('Create command filter'),
    'change_commandfilter': _('Update command filter'),
    'delete_commandfilter': _('Delete command filter'),
    'view_commandfilter': _('View command filter'),
    'add_commandfilterrule': _('Create command filter rule'),
    'change_commandfilterrule': _('Update command filter rule'),
    'delete_commandfilterrule': _('Delete command filter rule'),
    'view_commandfilterrule': _('View command filter rule'),
    'add_platform': _('Create platform'),
    'change_platform': _('Update platform'),
    'delete_platform': _('Delete platform'),
    'view_platform': _('View platform'),
    'add_application': _('Create application'),
    'change_application': _('Update application'),
    'delete_application': _('Delete application'),
    'view_application': _('View application'),
    'add_assetpermission': _('Create asset permission'),
    'change_assetpermission': _('Update asset permission'),
    'delete_assetpermission': _('Delete asset permission'),
    'view_assetpermission': _('View asset permission'),
    'add_applicationpermission': _('Create application permission'),
    'change_applicationpermission': _('Update application permission'),
    'delete_applicationpermission': _('Delete application permission'),
    'view_applicationpermission': _('View application permission'),
    'add_session': _('Create session'),
    'change_session': _('Update session'),
    'delete_session': _('Delete session'),
    'view_session': _('View session'),
    'add_command': _('Create command'),
    'view_command': _('View command'),
    'add_status': _('Create system status'),
    'change_terminal': _('Update terminal'),
    'delete_terminal': _('Delete terminal'),
    'view_terminal': _('View terminal'),
    'add_commandstorage': _('Create command storage'),
    'change_commandstorage': _('Update command storage'),
    'delete_commandstorage': _('Delete command storage'),
    'view_commandstorage': _('View command storage'),
    'add_replaystorage': _('Create replay storage'),
    'change_replaystorage': _('Update replay storage'),
    'delete_replaystorage': _('Delete replay storage'),
    'view_replaystorage': _('View replay storage'),
    'terminate_session': _('Terminate session'),
    'add_commandexecution': _('Execute batch command'),
    'add_ticket': _('Create ticket'),
    'change_ticket': _('Update ticket'),
    'delete_ticket': _('Delete ticket'),
    'view_ticket': _('View ticket'),
    'add_comment': _('Create comment'),
    'view_comment': _('View comment'),
    'change_gathereduser': _('Update gathered user'),
    'delete_gathereduser': _('Delete gathered user'),
    'view_gathereduser': _('View gathered user'),
    'add_gatherusertask': _('Create gather user task'),
    'change_gatherusertask': _('Update gather user task'),
    'delete_gatherusertask': _('Delete gather user task'),
    'view_gatherusertask': _('View gather user task'),
    'add_account': _('Create account'),
    'change_account': _('Update account'),
    'delete_account': _('Delete account'),
    'view_account': _('View account'),
    'add_syncinstancetask': _('Create Synchronization instance task'),
    'change_syncinstancetask': _('Update Synchronization instance task'),
    'delete_syncinstancetask': _('Delete Synchronization instance task'),
    'view_syncinstancetask': _('View Synchronization instance task'),
    'view_syncinstancedetail': _('View Synchronization instance detail'),
    'add_changeauthplan': _('Create change authentication plan'),
    'change_changeauthplan': _('Update change authentication plan'),
    'delete_changeauthplan': _('Delete change authentication plan'),
    'view_changeauthplan': _('Update change authentication plan'),
}

auditor_permissions_bits = {
    'add_ftplog': _('Create FTP log'),
    'view_ftplog': _('View FTP log'),
    'view_operatelog': _('View operate log'),
    'add_passwordchangelog': _('Create password change log'),
    'view_passwordchangelog': _('View password change log'),
    'add_userloginlog': _('Create user login log'),
    'view_userloginlog': _('View user login log'),
}

user_permissions_bits = {
    'view_my_asset': _('View my asset'),
    'view_my_application': _('View my application'),
    'execute_batch_command': _('Execute batch command'),
}

other_only_system_admin_permissions_bits = {

}
_other_org_admin_permissions_bits = {

}
other_auditor_permissions_bits = {

}
other_user_permissions_bits = {

}

other_org_admin_permissions_bits = {}
other_org_admin_permissions_bits.update(_other_org_admin_permissions_bits)
other_org_admin_permissions_bits.update(other_auditor_permissions_bits)
other_org_admin_permissions_bits.update(other_user_permissions_bits)

org_admin_permissions_bits = {}
org_admin_permissions_bits.update(_org_admin_permissions_bits)
org_admin_permissions_bits.update(other_org_admin_permissions_bits)
org_admin_permissions_bits.update(auditor_permissions_bits)
org_admin_permissions_bits.update(user_permissions_bits)


system_admin_permissions_bits = {}
system_admin_permissions_bits.update(only_system_admin_permissions_bits)
system_admin_permissions_bits.update(other_only_system_admin_permissions_bits)
system_admin_permissions_bits.update(org_admin_permissions_bits)


permissions_bits_map = {
    'system_admin': list(system_admin_permissions_bits.keys()),
    'org_admin': list(org_admin_permissions_bits.keys()),
    'system_auditor': list(auditor_permissions_bits.keys()),
    'org_auditor': list(auditor_permissions_bits.keys()),
    'user': list(user_permissions_bits.keys()),
}

scope_system_permissions_bits = permissions_bits_map['system_admin']
scope_org_permissions_bits = permissions_bits_map['org_admin']
