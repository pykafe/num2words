# -*- coding: utf-8 -*-Num2Word_IDT
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import division, unicode_literals
from num2words.currency import parse_currency_parts, prefix_currency

import re

from .lang_EU import Num2Word_EU

DOLLAR = ('dolar', 'dolar')
CENTS = ('sentavu', 'sentavu')


class Num2Word_IDT(Num2Word_EU):

    CURRENCY_FORMS = {
        'AUD': (DOLLAR, CENTS),
        'CAD': (DOLLAR, CENTS),
        'EUR': (('euro', 'euros'), CENTS),
        'GBP': (('pound sterling', 'pound sterling'), ('pence', 'pence')),
        'USD': (DOLLAR, CENTS),
    }

    GIGA_SUFFIX = None
    MEGA_SUFFIX = "iliaun"

    def setup(self):
        super().setup()
        lows = ["quatr", "tr", "b", "m"]
        self.high_numwords = self.gen_high_numwords([], [], lows)
        self.negword = "menus "
        self.pointword = "vírgula"
        self.exclude_title = ["resin", "vírgula", "menus"]

        self.mid_numwords = [
            (1000, "rihun"), (100, "atus"), (90, "sianulu"),
            (80, "ualunulu"), (70, "hitunulu"), (60, "neenulu"),
            (50, "limanulu"), (40, "aatnulu"), (30, "telunulu"),
            (20, "ruanulu")
        ]
        self.low_numwords = [
            "sanulu",
            "sia", "ualu", "hitu", "neen", "lima", "aat", "telu", "rua",
            "isa", "maok"
        ]
        self.ords = [
            {
                0: "",
                1: "waiisa",
                2: "wairua",
                3: "waitelu",
                4: "waiaat",
                5: "wailima",
                6: "waineen",
                7: "waihitu",
                8: "waiualu",
                9: "waisia",
            },
            {
                0: "",
                1: "waisanulu",
                2: "wairuanulu",
                3: "waitelunulu",
                4: "waiaatnulu",
                5: "wailimanulu",
                6: "waineenulu",
                7: "waihitunulu",
                8: "waiualunulu",
                9: "waisianulu",
            },
            {
                0: "",
                1: "waiatus isa",
                2: "waiatus rua",
                3: "waiatus telu",
                4: "waiatus aat",
                5: "waiatus lima",
                6: "waiatus neen",
                7: "waiatus hitu",
                8: "waiatus ualu",
                9: "waiatus sia",
            },
        ]
        self.thousand_separators = {
            3: "wairihun",
            6: "waimiliaun",
            9: "wairihun waimiliaun",
            12: "waibiliaun",
            15: "wairihun waibiliaun"
        }
        self.hundreds = {
            1: "atus",
            2: "atus rua",
            3: "atus telu",
            4: "atus aat",
            5: "atus lima",
            6: "atus neen",
            7: "atus hitu",
            8: "atus ualu",
            9: "atus sia",
        }

    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1 and nnum < 100:
            return next

        if nnum < cnum:
            if nnum < 10:
                return ("%s resin %s" % (ctext, ntext), cnum + nnum)
            else:
                return ("%s %s" % (ctext, ntext), cnum + nnum)

        return (ntext + " " + ctext, cnum * nnum)

    def to_cardinal(self, value):
        result = super().to_cardinal(value)

        for ext in (
                'rihun', 'miliaun','miliaun rihun',
                'biliaun', 'biliaun rihun'):
            if re.match('.*{} resin \\w*entus? (?=.*resin)'.format(ext), result):
                result = result.replace(
                    f'{ext} resin', f'{ext}'
                )

        return result


    def to_year(self, val, longval=True):
        if val < 0:
            return self.to_cardinal(abs(val)) + ' antes Kristu'
        return self.to_cardinal(val)

    def to_currency(self, val, currency='USD', cents=True,
                    adjective=False):
        """
        Args:
            val: Numeric value
            currency (str): Currency code
            cents (bool): Verbose cents
            adjective (bool): Prefix currency name with adjective
        Returns:
            str: Formatted string

        """
        left, right, is_negative = parse_currency_parts(val)

        try:
            cr1, cr2 = self.CURRENCY_FORMS[currency]

        except KeyError:
            raise NotImplementedError(
                'Currency code "%s" not implemented for "%s"' %
                (currency, self.__class__.__name__))

        if adjective and currency in self.CURRENCY_ADJECTIVES:
            cr1 = prefix_currency(self.CURRENCY_ADJECTIVES[currency], cr1)

        minus_str = "%s " % self.negword.strip() if is_negative else ""
        money_str = self._money_verbose(left, currency)
        cents_str = self._cents_verbose(right, currency) \
            if cents else self._cents_terse(right, currency)

        if right == 0:
            return u'%s%s %s' % (
                minus_str,
                self.pluralize(left, cr1),
                money_str
            )
        else:
            return u'%s%s %s %s %s' % (
                minus_str,
                self.pluralize(left, cr1),
                money_str,
                self.pluralize(right, cr2),
                cents_str
            )

