import bpy

from bpy.app.handlers import persistent

from . import functions
from .global_variables import handler_statement
from .addon_prefs import get_addon_preferences
from .update_module import check_addon_version


@persistent
def reload_startup(scene):

    wm = bpy.data.window_managers['WinMan']
    prefs = get_addon_preferences()

    # check for addon new version
    if prefs.update_check_launch:
        check_addon_version(wm)

    # images
    functions.check_images_startup()

    # libraries
    functions.check_libraries_startup()

    # launch timer on startup
    if prefs.startup_launch:
        wm.autoreload_properties.autoreload_is_timer = True

    print(handler_statement)


### REGISTER ---

def register():
    bpy.app.handlers.load_post.append(reload_startup)

def unregister():
    bpy.app.handlers.load_post.remove(reload_startup)