# -*- coding: utf-8 -*-Num2Word_TET
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

import re

from .lang_EU import Num2Word_EU

DOLLAR = ('dólar', 'dólares')
CENTS = ('cêntimo', 'cêntimos')


class Num2Word_TET(Num2Word_EU):

    CURRENCY_FORMS = {
        'AUD': (DOLLAR, CENTS),
        'CAD': (DOLLAR, CENTS),
        'EUR': (('euro', 'euros'), CENTS),
        'GBP': (('libra', 'libras'), ('péni', 'pence')),
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
            (80, "walunulu"), (70, "hitunulu"), (60, "neenulu"),
            (50, "limanulu"), (40, "haatnulu"), (30, "tolunulu"),
            (20, "ruanulu")
        ]
        self.low_numwords = [
            "sanulu",
            "sia", "walu", "hitu", "neen", "lima", "haat", "tolu", "rua",
            "ida", "zero"
        ]
        self.ords = [
            {
                0: "",
                1: "primeiro",
                2: "segundo",
                3: "terceiro",
                4: "quarto",
                5: "quinto",
                6: "sexto",
                7: "sétimo",
                8: "oitavo",
                9: "nono",
            },
            {
                0: "",
                1: "décimo",
                2: "vigésimo",
                3: "trigésimo",
                4: "quadragésimo",
                5: "quinquagésimo",
                6: "sexagésimo",
                7: "septuagésimo",
                8: "octogésimo",
                9: "nonagésimo",
            },
            {
                0: "",
                1: "centésimo",
                2: "ducentésimo",
                3: "tricentésimo",
                4: "quadrigentésimo",
                5: "quingentésimo",
                6: "seiscentésimo",
                7: "septigentésimo",
                8: "octigentésimo",
                9: "nongentésimo",
            },
        ]
        self.thousand_separators = {
            3: "milésimo",
            6: "milionésimo",
            9: "milésimo milionésimo",
            12: "bilionésimo",
            15: "milésimo bilionésimo"
        }
        self.hundreds = {
            1: "cento",
            2: "duzentos",
            3: "trezentos",
            4: "quatrocentos",
            5: "quinhentos",
            6: "seiscentos",
            7: "setecentos",
            8: "oitocentos",
            9: "novecentos",
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
            if re.match('.*{} e \\w*entos? (?=.*e)'.format(ext), result):
                result = result.replace(
                    '{} e'.format(ext), '{}'.format(ext)
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
    def to_ordinal(self, value):
        # Before changing this function remember this is used by pt-BR
        # so act accordingly
        self.verify_ordinal(value)

        result = []
        value = str(value)
        thousand_separator = ''

        for idx, char in enumerate(value[::-1]):
            if idx and idx % 3 == 0:
                thousand_separator = self.thousand_separators[idx]

            if char != '0' and thousand_separator:
                # avoiding "segundo milionésimo milésimo" for 6000000,
                # for instance
                result.append(thousand_separator)
                thousand_separator = ''

            result.append(self.ords[idx % 3][int(char)])

        result = ' '.join(result[::-1])
        result = result.strip()
        result = re.sub('\\s+', ' ', result)

        if result.startswith('primeiro') and value != '1':
            # avoiding "primeiro milésimo", "primeiro milionésimo" and so on
            result = result[9:]

        return result

    def to_ordinal_num(self, value):
        # Before changing this function remember this is used by pt-BR
        # so act accordingly
        self.verify_ordinal(value)
        return "%sº" % (value)

    def to_year(self, val, longval=True):
        # Before changing this function remember this is used by pt-BR
        # so act accordingly
        if val < 0:
            return self.to_cardinal(abs(val)) + ' antes de Cristo'
        return self.to_cardinal(val)

    def to_currency(self, val, currency='EUR', cents=True, separator=' e',
                    adjective=False):
        # change negword because base.to_currency() does not need space after
        backup_negword = self.negword
        self.negword = self.negword[:-1]
        result = super().to_currency(
            val, currency=currency, cents=cents, separator=separator,
            adjective=adjective)
        # undo the change on negword
        self.negword = backup_negword

        # transforms "milhões euros" em "milhões de euros"
        cr1, _ = self.CURRENCY_FORMS[currency]

        for ext in (
                'miliaun','biliaun','triliaun'):
            if re.match('.*{} (?={})'.format(ext, cr1[1]), result):
                result = result.replace(
                    '{}'.format(ext), '{} de'.format(ext), 1
                )
        # do not print "e zero cêntimos"
        result = result.replace(' e zero cêntimos', '')
        return result
