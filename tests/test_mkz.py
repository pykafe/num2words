# -*- coding: utf-8 -*-
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

from __future__ import unicode_literals

from decimal import Decimal
from unittest import TestCase, skip

from num2words import num2words
from num2words.lang_MKZ import Num2Word_MKZ


class Num2WordsMKZTest(TestCase):
    def setUp(self):
        super().setUp()
        self.n2w = Num2Word_MKZ()

    def test_cardinal_integer(self):
        self.assertEqual(num2words(1, lang='mkz'), 'u')
        self.assertEqual(num2words(2, lang='mkz'), 'lolae')
        self.assertEqual(num2words(3, lang='mkz'), 'lolitu')
        self.assertEqual(num2words(4, lang='mkz'), 'loloha')
        self.assertEqual(num2words(5, lang='mkz'), 'lima')
        self.assertEqual(num2words(6, lang='mkz'), 'daha')
        self.assertEqual(num2words(7, lang='mkz'), 'pitu')
        self.assertEqual(num2words(8, lang='mkz'), 'apo')
        self.assertEqual(num2words(9, lang='mkz'), 'siwa')
        self.assertEqual(num2words(10, lang='mkz'), 'ruru')
        self.assertEqual(num2words(11, lang='mkz'), 'ruru resi u')
        self.assertEqual(num2words(12, lang='mkz'), 'ruru resi lolae')
        self.assertEqual(num2words(13, lang='mkz'), 'ruru resi lolitu')
        self.assertEqual(num2words(14, lang='mkz'), 'ruru resi loloha')
        self.assertEqual(num2words(15, lang='mkz'), 'ruru resi lima')
        self.assertEqual(num2words(16, lang='mkz'), 'ruru resi daha')
        self.assertEqual(num2words(17, lang='mkz'), 'ruru resi pitu')
        self.assertEqual(num2words(18, lang='mkz'), 'ruru resi apo')
        self.assertEqual(num2words(19, lang='mkz'), 'ruru resi siwa')
        self.assertEqual(num2words(20, lang='mkz'), 'ruru lolae')

        self.assertEqual(num2words(21, lang='mkz'), 'ruru lolae resi u')
        self.assertEqual(num2words(22, lang='mkz'), 'ruru lolae resi lolae')
        self.assertEqual(num2words(35, lang='mkz'), 'ruru lolitu resi lima')
        self.assertEqual(num2words(99, lang='mkz'), 'ruru siwa resi siwa')

        self.assertEqual(num2words(100, lang='mkz'), 'rasa u')
        self.assertEqual(num2words(101, lang='mkz'), 'rasa u resi u')
        self.assertEqual(num2words(107, lang='mkz'), 'rasa u resi pitu')
        self.assertEqual(num2words(110, lang='mkz'), 'rasa u ruru')
        self.assertEqual(num2words(114, lang='mkz'), 'rasa u ruru resi loloha')
        self.assertEqual(num2words(128, lang='mkz'), 'rasa u ruru lolae resi apo')
        self.assertEqual(num2words(151, lang='mkz'), 'rasa u ruru lima resi u')
        self.assertEqual(num2words(713, lang='mkz'), 'rasa pitu ruru resi lolitu')
        self.assertEqual(num2words(999, lang='mkz'), 'rasa siwa ruru siwa resi siwa')

        self.assertEqual(num2words(1000, lang='mkz'), 'rihun u')
        self.assertEqual(num2words(1001, lang='mkz'), 'rihun u resi u')
        self.assertEqual(num2words(1011, lang='mkz'), 'rihun u ruru resi u')
        self.assertEqual(num2words(1111, lang='mkz'), 'rihun u rasa u ruru resi u')
        self.assertEqual(num2words(2357, lang='mkz'), 'rihun lolae rasa lolitu ruru lima resi pitu')
        self.assertEqual(
            num2words(2200, lang='mkz'),
            'rihun lolae rasa lolae'
        )
        self.assertEqual(num2words(2230, lang='mkz'), 'rihun lolae rasa lolae ruru lolitu')
        self.assertEqual(num2words(73400, lang='mkz'), 'rihun ruru pitu resi lolitu rasa loloha')
        self.assertEqual(num2words(73421, lang='mkz'), 'rihun ruru pitu resi lolitu rasa loloha ruru lolae resi u')
        self.assertEqual(num2words(100000, lang='mkz'), 'rihun rasa u')
        self.assertEqual(num2words(250050, lang='mkz'), 'rihun rasa lolae ruru lima ruru lima')
        self.assertEqual(
            num2words(6000000, lang='mkz'), 'miliaun daha'
        )
        self.assertEqual(
            num2words(100000000, lang='mkz'), 'miliaun rasa u'
        )
        self.assertEqual(
            num2words(19000000000, lang='mkz'), 'miliaun rihun ruru resi siwa'
        )
        self.assertEqual(
            num2words(145000000002, lang='mkz'),
            'miliaun rihun rasa u ruru loloha resi lima resi lolae'
        )
        self.assertEqual(
            num2words(4635102, lang='mkz'),
            'miliaun loloha rihun rasa daha ruru lolitu resi lima rasa u resi lolae'
        )
        self.assertEqual(
            num2words(145254635102, lang='mkz'),
            'miliaun rihun rasa u ruru loloha resi lima rasa lolae ruru lima resi loloha rihun rasa daha ruru lolitu resi lima rasa u resi lolae'
        )
        self.assertEqual(
            num2words(1000000000000, lang='mkz'),
            'biliaun u'
        )
        self.assertEqual(
            num2words(2000000000000, lang='mkz'),
            'biliaun lolae'
        )
        self.assertEqual(
            num2words(1000000000000000, lang='mkz'),
            'biliaun rihun u'
        )
        self.assertEqual(
            num2words(2000000000000000, lang='mkz'),
            'biliaun rihun lolae'
        )
        self.assertEqual(
            num2words(1000000000000000000, lang='mkz'),
            'triliaun u'
        )
        self.assertEqual(
            num2words(2000000000000000000, lang='mkz'),
            'triliaun lolae'
        )

    def test_cardinal_integer_negative(self):
        self.assertEqual(num2words(-1, lang='mkz'), 'hau hasai u')
        self.assertEqual(
            num2words(-256, lang='mkz'), 'hau hasai rasa lolae ruru lima resi daha'
        )
        self.assertEqual(num2words(-1000, lang='mkz'), 'hau hasai rihun u')
        self.assertEqual(num2words(-1000000, lang='mkz'), 'hau hasai miliaun u')
        self.assertEqual(
            num2words(-1234567, lang='mkz'),
            'hau hasai miliaun u rihun rasa lolae ruru lolitu resi loloha rasa lima ruru daha resi pitu'
        )

    def test_cardinal_float(self):
        self.assertEqual(num2words(Decimal('1.00'), lang='mkz'), 'u')
        self.assertEqual(num2words(
            Decimal('1.01'), lang='mkz'), 'u virgula gi losa u')
        self.assertEqual(num2words(
            Decimal('1.035'), lang='mkz'), 'u virgula gi losa lolitu lima'
        )
        self.assertEqual(num2words(
            Decimal('1.35'), lang='mkz'), 'u virgula lolitu lima'
        )
        self.assertEqual(
            num2words(Decimal('3.14159'), lang='mkz'),
            'lolitu virgula u loloha u lima siwa'
        )
        self.assertEqual(
            num2words(Decimal('101.22'), lang='mkz'),
            'rasa u resi u virgula lolae lolae'
        )
        self.assertEqual(
            num2words(Decimal('2345.75'), lang='mkz'),
            'rihun lolae rasa lolitu ruru loloha resi lima virgula pitu lima'
        )


    def test_cardinal_float_negative(self):
        self.assertEqual(
            num2words(Decimal('-2.34'), lang='mkz'),
            'hau hasai lolae virgula lolitu loloha'
        )
        self.assertEqual(
            num2words(Decimal('-9.99'), lang='mkz'),
            'hau hasai siwa virgula siwa siwa'
        )
        self.assertEqual(
            num2words(Decimal('-7.01'), lang='mkz'),
            'hau hasai pitu virgula gi losa u'
        )
        self.assertEqual(
            num2words(Decimal('-222.22'), lang='mkz'),
            'hau hasai rasa lolae ruru lolae resi lolae virgula lolae lolae'
        )

    @skip('not implement yet')
    def test_ordinal(self):
        self.assertEqual(num2words(1, lang='tet', ordinal=True), 'dahuluk')
        self.assertEqual(num2words(2, lang='tet', ordinal=True), 'daruak')
        self.assertEqual(num2words(3, lang='tet', ordinal=True), 'datoluk')
        self.assertEqual(num2words(4, lang='tet', ordinal=True), 'dahaat')
        self.assertEqual(num2words(5, lang='tet', ordinal=True), 'dalimak')
        self.assertEqual(num2words(6, lang='tet', ordinal=True), 'daneen')
        self.assertEqual(num2words(7, lang='tet', ordinal=True), 'dahituk')
        self.assertEqual(num2words(8, lang='tet', ordinal=True), 'daualuk')
        self.assertEqual(num2words(9, lang='tet', ordinal=True), 'dasiak')
        self.assertEqual(num2words(10, lang='tet', ordinal=True), 'dasanuluk')
        self.assertEqual(
            num2words(11, lang='tet', ordinal=True), 'dasanulu resin idak'
        )
        self.assertEqual(
            num2words(12, lang='tet', ordinal=True), 'dasanulu resin ruak'
        )
        self.assertEqual(
            num2words(13, lang='tet', ordinal=True), 'dasanulu resin toluk'
        )
        self.assertEqual(
            num2words(14, lang='tet', ordinal=True), 'dasanulu resin haat'
        )
        self.assertEqual(
            num2words(15, lang='tet', ordinal=True), 'dasanulu resin limak'
        )
        self.assertEqual(
            num2words(16, lang='tet', ordinal=True), 'dasanulu resin neen'
        )
        self.assertEqual(
            num2words(17, lang='tet', ordinal=True), 'dasanulu resin hituk'
        )
        self.assertEqual(
            num2words(18, lang='tet', ordinal=True), 'dasanulu resin ualuk'
        )
        self.assertEqual(
            num2words(19, lang='tet', ordinal=True), 'dasanulu resin siak'
        )
        self.assertEqual(
            num2words(20, lang='tet', ordinal=True), 'daruanuluk'
        )

        self.assertEqual(
            num2words(21, lang='tet', ordinal=True), 'daruanulu resin idak'
        )
        self.assertEqual(
            num2words(22, lang='tet', ordinal=True), 'daruanulu resin ruak'
        )
        self.assertEqual(
            num2words(35, lang='tet', ordinal=True), 'datolunulu resin limak'
        )
        self.assertEqual(
            num2words(99, lang='tet', ordinal=True), 'dasianulu resin siak'
        )

        self.assertEqual(
            num2words(100, lang='tet', ordinal=True), 'dahatus idak'
        )
        self.assertEqual(
            num2words(101, lang='tet', ordinal=True), 'dahatus ida resin idak'
        )
        self.assertEqual(
            num2words(128, lang='tet', ordinal=True),
            'dahatus ida ruanulu resin ualuk'
        )
        self.assertEqual(
            num2words(713, lang='tet', ordinal=True),
            'dahatus hitu sanulu resin toluk'
        )

        self.assertEqual(
            num2words(1000, lang='tet', ordinal=True), 'darihun idak'
        )
        self.assertEqual(
            num2words(1001, lang='tet', ordinal=True), 'darihun ida resin idak'
        )
        self.assertEqual(
            num2words(1111, lang='tet', ordinal=True),
            'darihun ida atus ida sanulu resin idak'
        )
        self.assertEqual(
            num2words(2114, lang='tet', ordinal=True),
            'darihun rua atus ida sanulu resin haat'
        )
        self.assertEqual(
            num2words(73421, lang='tet', ordinal=True),
            'darihun hitunulu resin tolu atus haat ruanulu resin idak'
        )

        self.assertEqual(
            num2words(100000, lang='tet', ordinal=True),
            'darihun atus idak'
        )
        self.assertEqual(
            num2words(250050, lang='tet', ordinal=True),
            'darihun atus rua limanulu limanuluk'
        )
        self.assertEqual(
            num2words(6000000, lang='tet', ordinal=True), 'damiliaun neen'
        )
        self.assertEqual(
            num2words(19000000000, lang='tet', ordinal=True),
            'damiliaun rihun sanulu resin siak'
        )
        self.assertEqual(
            num2words(145000000002, lang='tet', ordinal=True),
            'damiliaun rihun atus ida haatnulu resin lima resin ruak'
        )

    def test_currency_integer(self):
        self.assertEqual(self.n2w.to_currency(1.00), 'dolar u')
        self.assertEqual(self.n2w.to_currency(2.00), 'dolar lolae')
        self.assertEqual(self.n2w.to_currency(3.00), 'dolar lolitu')
        self.assertEqual(self.n2w.to_currency(4.00), 'dolar loloha')
        self.assertEqual(self.n2w.to_currency(5.00), 'dolar lima')
        self.assertEqual(self.n2w.to_currency(6.00), 'dolar daha')
        self.assertEqual(self.n2w.to_currency(7.00), 'dolar pitu')
        self.assertEqual(self.n2w.to_currency(8.00), 'dolar apo')
        self.assertEqual(self.n2w.to_currency(9.00), 'dolar siwa')
        self.assertEqual(self.n2w.to_currency(10.00), 'dolar ruru')
        self.assertEqual(self.n2w.to_currency(11.00), 'dolar ruru resi u')
        self.assertEqual(self.n2w.to_currency(12.00), 'dolar ruru resi lolae')
        self.assertEqual(self.n2w.to_currency(13.00), 'dolar ruru resi lolitu')
        self.assertEqual(self.n2w.to_currency(14.00), 'dolar ruru resi loloha')
        self.assertEqual(self.n2w.to_currency(15.00), 'dolar ruru resi lima')
        self.assertEqual(self.n2w.to_currency(16.00), 'dolar ruru resi daha')
        self.assertEqual(self.n2w.to_currency(17.00), 'dolar ruru resi pitu')
        self.assertEqual(self.n2w.to_currency(18.00), 'dolar ruru resi apo')
        self.assertEqual(self.n2w.to_currency(19.00), 'dolar ruru resi siwa')
        self.assertEqual(self.n2w.to_currency(20.00), 'dolar ruru lolae')

        self.assertEqual(self.n2w.to_currency(21.00), 'dolar ruru lolae resi u')
        self.assertEqual(self.n2w.to_currency(22.00), 'dolar ruru lolae resi lolae')
        self.assertEqual(self.n2w.to_currency(35.00), 'dolar ruru lolitu resi lima')
        self.assertEqual(self.n2w.to_currency(99.00), 'dolar ruru siwa resi siwa')

        self.assertEqual(self.n2w.to_currency(100.00), 'dolar rasa u')
        self.assertEqual(self.n2w.to_currency(101.00), 'dolar rasa u resi u')
        self.assertEqual(
            self.n2w.to_currency(128.00), 'dolar rasa u ruru lolae resi apo'
        )
        self.assertEqual(
            self.n2w.to_currency(713.00), 'dolar rasa pitu ruru resi lolitu')

        self.assertEqual(self.n2w.to_currency(1000.00), 'dolar rihun u')
        self.assertEqual(self.n2w.to_currency(1001.00), 'dolar rihun u resi u')
        self.assertEqual(
            self.n2w.to_currency(1111.00), 'dolar rihun u rasa u ruru resi u')
        self.assertEqual(
            self.n2w.to_currency(2114.00), 'dolar rihun lolae rasa u ruru resi loloha'
        )
        self.assertEqual(
            self.n2w.to_currency(73421.00),
            'dolar rihun ruru pitu resi lolitu rasa loloha ruru lolae resi u'
        )

        self.assertEqual(self.n2w.to_currency(100000.00), 'dolar rihun rasa u')
        self.assertEqual(
            self.n2w.to_currency(250050.00),
            'dolar rihun rasa lolae ruru lima ruru lima'
        )
        self.assertEqual(
            self.n2w.to_currency(6000000.00),
            'dolar miliaun daha'
        )
        self.assertEqual(
            self.n2w.to_currency(19000000000.00),
            'dolar miliaun rihun ruru resi siwa'
        )
        self.assertEqual(
            self.n2w.to_currency(145000000002.00),
            'dolar miliaun rihun rasa u ruru loloha resi lima resi lolae'
        )
        self.assertEqual(self.n2w.to_currency(1.00, currency='USD'),
                         'dolar u')
        self.assertEqual(self.n2w.to_currency(1.50, currency='USD'),
                         'dolar u sentavu ruru lima')
        with self.assertRaises(NotImplementedError):
            self.n2w.to_currency(1.00, currency='CHF')

    def test_currency_integer_negative(self):
        self.assertEqual(self.n2w.to_currency(-1.00), 'hau hasai dolar u')
        self.assertEqual(
            self.n2w.to_currency(-256.00),
            'hau hasai dolar rasa lolae ruru lima resi daha'
        )
        self.assertEqual(self.n2w.to_currency(-1000.00), 'hau hasai dolar rihun u')
        self.assertEqual(
            self.n2w.to_currency(-1000000.00), 'hau hasai dolar miliaun u'
        )
        self.assertEqual(
            self.n2w.to_currency(-1234567.00),
            'hau hasai dolar miliaun u rihun rasa lolae ruru lolitu resi loloha rasa lima ruru daha resi pitu'
        )

    def test_currency_float(self):
        self.assertEqual(self.n2w.to_currency(Decimal('1.00')), 'dolar u')
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.01')), 'dolar u sentavu u'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.03')), 'dolar u sentavu lolitu'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.35')),
            'dolar u sentavu ruru lolitu resi lima'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('3.14')),
            'dolar lolitu sentavu ruru resi loloha'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('101.22')),
            'dolar rasa u resi u sentavu ruru lolae resi lolae'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('2345.75')),
            'dolar rihun lolae rasa lolitu ruru loloha resi lima sentavu ruru pitu resi lima'
        )

    def test_currency_float_negative(self):
        self.assertEqual(
            self.n2w.to_currency(Decimal('-2.34')),
            'hau hasai dolar lolae sentavu ruru lolitu resi loloha'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-9.99')),
            'hau hasai dolar siwa sentavu ruru siwa resi siwa'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-7.01')),
            'hau hasai dolar pitu sentavu u'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-222.22')),
            'hau hasai dolar rasa lolae ruru lolae resi lolae sentavu ruru lolae resi lolae'
        )

    def test_year(self):
        self.assertEqual(self.n2w.to_year(1001), 'rihun u resi u')
        self.assertEqual(
            self.n2w.to_year(1789), 'rihun u rasa pitu ruru apo resi siwa'
        )
        self.assertEqual(
            self.n2w.to_year(1942), 'rihun u rasa siwa ruru loloha resi lolae'
        )
        self.assertEqual(
            self.n2w.to_year(1984), 'rihun u rasa siwa ruru apo resi loloha'
        )
        self.assertEqual(self.n2w.to_year(2000), 'rihun lolae')
        self.assertEqual(self.n2w.to_year(2001), 'rihun lolae resi u')
        self.assertEqual(self.n2w.to_year(2016), 'rihun lolae ruru resi daha')

    def test_year_negative(self):
        self.assertEqual(self.n2w.to_year(-30), 'ruru lolitu Kristu neegu lafu')
        self.assertEqual(
            self.n2w.to_year(-744),
            'rasa pitu ruru loloha resi loloha Kristu neegu lafu'
        )
        self.assertEqual(
            self.n2w.to_year(-10000),
            'rihun ruru Kristu neegu lafu'
        )

    def test_to_ordinal_num(self):
        self.assertEqual(self.n2w.to_ordinal_num(1), '1º')
        self.assertEqual(self.n2w.to_ordinal_num(100), '100º')
