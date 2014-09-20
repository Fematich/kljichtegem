from flask import Blueprint, redirect, request, flash, url_for
from flask.ext.principal import RoleNeed, Permission
from flask.ext.security import current_user
from flask.ext.security import url_for_security
admin = Blueprint('admin', __name__,
                        template_folder='templates')

@admin.before_request
def restrict_to_admins():
#    perm = Permission(RoleNeed('admin'))
    if not current_user.is_authenticated():
        flash("You have no admin-rights to access this page")
        return redirect(request.args.get('next') or url_for_security('login'))
from views import *
