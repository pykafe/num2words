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

        # Transforms "mil e cento e catorze" into "mil cento e catorze"
        # Transforms "cem milhões e duzentos mil e duzentos e dez" em "cem
        # milhões duzentos mil duzentos e dez" but "cem milhões e duzentos
        # mil e duzentos" in "cem milhões duzentos mil e duzentos" and not in
        # "cem milhões duzentos mil duzentos"
        for ext in (
                'rihun', 'miliaun','miliaun rihun',
                'biliaun', 'biliaun rihun'):
            if re.match('.*{} resin \\w*entus? (?=.*resin)'.format(ext), result):
                result = result.replace(
                    f'{ext} resin', f'{ext}'
                )

        return result

    # for the ordinal conversion the code is similar to pt_BR code,
    # although there are other rules that are probably more correct in
    # Portugal. Concerning numbers from 2000th on, saying "dois
    # milésimos" instead of "segundo milésimo" (the first number
    # would be used in the cardinal form instead of the ordinal) is better.
    # This was not implemented.
    # source:
    # https://ciberduvidas.iscte-iul.pt/consultorio/perguntas/a-forma-por-extenso-de-2000-e-de-outros-ordinais/16428
    '''
    def to_ordinal(self, value):
        # Before changing this function remember this is used by pt-BR
        # so act accordingly
        self.verify_ordinal(value)
        try:
            assert int(value) == value
        except (ValueError, TypeError, AssertionError):
            return self.to_cardinal_float(value)

        out = ""
        if value < 0:
            value = abs(value)
            out = "%s " % self.negword.strip()

        if value >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig % (value, self.MAXVAL))

        val = self.splitnum(value)
        outs = val
        while len(val) != 1:
            outs = []
            left, right = val[:2]
            if isinstance(left, tuple) and isinstance(right, tuple):
                outs.append(self.merge(left, right))
                if val[2:]:
                    outs.append(val[2:])
            else:
                for elem in val:
                    if isinstance(elem, list):
                        if len(elem) == 1:
                            outs.append(elem[0])
                        else:
                            outs.append(self.clean(elem))
                    else:
                        outs.append(elem)
            val = outs

        words, num = outs[0]

        if num in [900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 6, 7, 5, 4, 3, 2, 1]:
            words = 'wai'+words

        words_split = words.split()
        if len(words_split) >= 3 and num < 100:
            first_word = 'wai'+words_split[0]
            second_word = " ".join(words_split[1:])
            if 'aat' in second_word or 'neen' in second_word:
                words = first_word+" "+second_word
            else:
                words = first_word+" "+second_word

        word_first =  'dah'+words_split[0]
        if word_first == 'dahatus' and len(words_split) >=3:
            word_second = " ".join(words_split[1:])
            if 'haat' in word_second or 'neen' in word_second:
                words = word_first+" "+word_second
            else:
                words = word_first+" "+word_second+'k'

        if len(str(num)) > 3:
            if 'haat' in words_split[-1:] or 'neen' in words_split[-1:]:
                words = 'wai'+words
            else:
                words = 'wai'+words

        return self.title(out + words)

    def to_ordinal_num(self, value):
        # Before changing this function remember this is used by pt-BR
        # so act accordingly
        self.verify_ordinal(value)
        return "%sº" % (value)
    '''

    def to_year(self, val, longval=True):
        # Before changing this function remember this is used by pt-BR
        # so act accordingly
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

