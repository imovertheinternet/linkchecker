# -*- coding: iso-8859-1 -*-
# Copyright (C) 2008-2010 Bastian Kleineidam
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""
Test network functions.
"""

import unittest
from tests import need_posix
import linkcheck.network


class TestNetwork (unittest.TestCase):
    """Test network functions."""

    @need_posix
    def test_ifreq_size (self):
        self.assertTrue(linkcheck.network.ifreq_size() > 0)

    @need_posix
    def test_interfaces (self):
        ifc = linkcheck.network.IfConfig()
        ifc.getInterfaceList()
