#!/usr/bin/python3
'''
   Copyright 2017 Mirko Brombin (brombinmirko@gmail.com)

   This file is part of Kangaroo.

    Kangaroo is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Kangaroo is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Kangaroo.  If not, see <http://www.gnu.org/licenses/>.
'''
import gi
import os
import locale
import gettext
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

try:
    current_locale, encoding = locale.getdefaultlocale()
    locale_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
    translate = gettext.translation ('kangaroo', locale_path, [current_locale] )
    _ = translate.gettext
except FileNotFoundError:
    _ = str

class App:
    application_shortname = "kangaroo"
    application_id = "com.github.mirkobrombin.kangaroo"
    application_name = _('Kangaroo')
    application_description = _('Easily manage your Wine kangaroo')
    application_version ="0.1.2"
    app_years = "2017-2018"
    main_url = "https://github.com/mirkobrombin/kangaroo"
    bug_url = "https://github.com/mirkobrombin/kangaroo/issues/labels/bug"
    help_url = "https://github.com/mirkobrombin/kangaroo/wiki"
    translate_url = "https://github.com/mirkobrombin/kangaroo/blob/master/CONTRIBUTING.md"
    about_authors = None # Mirko Brombin <brombinmirko@gmail.com>
    about_documenters = None
    about_comments = application_description
    about_license_type = Gtk.License.GPL_3_0

class Colors:
    primary_color = "#302a2d"
    primary_text_color = "#f0e7e7"
    primary_text_shadow_color = "#160404"
