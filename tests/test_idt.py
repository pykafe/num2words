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
from num2words.lang_IDT import Num2Word_IDT


class Num2WordsIDTTest(TestCase):
    def setUp(self):
        super().setUp()
        self.n2w = Num2Word_IDT()

    def test_cardinal_integer(self):
        self.assertEqual(num2words(1, lang='idt'), 'isa')
        self.assertEqual(num2words(2, lang='idt'), 'rua')
        self.assertEqual(num2words(3, lang='idt'), 'telu')
        self.assertEqual(num2words(4, lang='idt'), 'aat')
        self.assertEqual(num2words(5, lang='idt'), 'lima')
        self.assertEqual(num2words(6, lang='idt'), 'neen')
        self.assertEqual(num2words(7, lang='idt'), 'hitu')
        self.assertEqual(num2words(8, lang='idt'), 'ualu')
        self.assertEqual(num2words(9, lang='idt'), 'sia')
        self.assertEqual(num2words(10, lang='idt'), 'sanulu')
        self.assertEqual(num2words(11, lang='idt'), 'sanulu resin isa')
        self.assertEqual(num2words(12, lang='idt'), 'sanulu resin rua')
        self.assertEqual(num2words(13, lang='idt'), 'sanulu resin telu')
        self.assertEqual(num2words(14, lang='idt'), 'sanulu resin aat')
        self.assertEqual(num2words(15, lang='idt'), 'sanulu resin lima')
        self.assertEqual(num2words(16, lang='idt'), 'sanulu resin neen')
        self.assertEqual(num2words(17, lang='idt'), 'sanulu resin hitu')
        self.assertEqual(num2words(18, lang='idt'), 'sanulu resin ualu')
        self.assertEqual(num2words(19, lang='idt'), 'sanulu resin sia')
        self.assertEqual(num2words(20, lang='idt'), 'ruanulu')

        self.assertEqual(num2words(21, lang='idt'), 'ruanulu resin isa')
        self.assertEqual(num2words(22, lang='idt'), 'ruanulu resin rua')
        self.assertEqual(num2words(35, lang='idt'), 'telunulu resin lima')
        self.assertEqual(num2words(99, lang='idt'), 'sianulu resin sia')

        self.assertEqual(num2words(100, lang='idt'), 'atus isa')
        self.assertEqual(num2words(101, lang='idt'), 'atus isa resin isa')
        self.assertEqual(num2words(107, lang='idt'), 'atus isa resin hitu')
        self.assertEqual(num2words(110, lang='idt'), 'atus isa sanulu')
        self.assertEqual(num2words(114, lang='idt'), 'atus isa sanulu resin aat')
        self.assertEqual(num2words(128, lang='idt'), 'atus isa ruanulu resin ualu')
        self.assertEqual(num2words(151, lang='idt'), 'atus isa limanulu resin isa')
        self.assertEqual(num2words(713, lang='idt'), 'atus hitu sanulu resin telu')
        self.assertEqual(num2words(999, lang='idt'), 'atus sia sianulu resin sia')

        self.assertEqual(num2words(1000, lang='idt'), 'rihun isa')
        self.assertEqual(num2words(1001, lang='idt'), 'rihun isa resin isa')
        self.assertEqual(num2words(1011, lang='idt'), 'rihun isa sanulu resin isa')
        self.assertEqual(num2words(1111, lang='idt'), 'rihun isa atus isa sanulu resin isa')
        self.assertEqual(num2words(2357, lang='idt'), 'rihun rua atus telu limanulu resin hitu')
        self.assertEqual(
            num2words(2200, lang='idt'),
            'rihun rua atus rua'
        )
        self.assertEqual(num2words(2230, lang='idt'), 'rihun rua atus rua telunulu')
        self.assertEqual(num2words(73400, lang='idt'), 'rihun hitunulu resin telu atus aat')
        self.assertEqual(num2words(73421, lang='idt'), 'rihun hitunulu resin telu atus aat ruanulu resin isa')
        self.assertEqual(num2words(100000, lang='idt'), 'rihun atus isa')
        self.assertEqual(num2words(250050, lang='idt'), 'rihun atus rua limanulu limanulu')
        self.assertEqual(
            num2words(6000000, lang='idt'), 'miliaun neen'
        )
        self.assertEqual(
            num2words(100000000, lang='idt'), 'miliaun atus isa'
        )
        self.assertEqual(
            num2words(19000000000, lang='idt'), 'miliaun rihun sanulu resin sia'
        )
        self.assertEqual(
            num2words(145000000002, lang='idt'),
            'miliaun rihun atus isa aatnulu resin lima resin rua'
        )
        self.assertEqual(
            num2words(4635102, lang='idt'),
            'miliaun aat rihun atus neen telunulu resin lima atus isa resin rua'
        )
        self.assertEqual(
            num2words(145254635102, lang='idt'),
            'miliaun rihun atus isa aatnulu resin lima atus rua limanulu resin aat rihun atus neen telunulu resin lima atus isa resin rua'
        )
        self.assertEqual(
            num2words(1000000000000, lang='idt'),
            'biliaun isa'
        )
        self.assertEqual(
            num2words(2000000000000, lang='idt'),
            'biliaun rua'
        )
        self.assertEqual(
            num2words(1000000000000000, lang='idt'),
            'biliaun rihun isa'
        )
        self.assertEqual(
            num2words(2000000000000000, lang='idt'),
            'biliaun rihun rua'
        )
        self.assertEqual(
            num2words(1000000000000000000, lang='idt'),
            'triliaun isa'
        )
        self.assertEqual(
            num2words(2000000000000000000, lang='idt'),
            'triliaun rua'
        )

    def test_cardinal_integer_negative(self):
        self.assertEqual(num2words(-1, lang='idt'), 'menus isa')
        self.assertEqual(
            num2words(-256, lang='idt'), 'menus atus rua limanulu resin neen'
        )
        self.assertEqual(num2words(-1000, lang='idt'), 'menus rihun isa')
        self.assertEqual(num2words(-1000000, lang='idt'), 'menus miliaun isa')
        self.assertEqual(
            num2words(-1234567, lang='idt'),
            'menus miliaun isa rihun atus rua telunulu resin aat atus lima neenulu resin hitu'
        )

    def test_cardinal_float(self):
        self.assertEqual(num2words(Decimal('1.00'), lang='idt'), 'isa')
        self.assertEqual(num2words(
            Decimal('1.01'), lang='idt'), 'isa vírgula maok isa')
        self.assertEqual(num2words(
            Decimal('1.035'), lang='idt'), 'isa vírgula maok telu lima'
        )
        self.assertEqual(num2words(
            Decimal('1.35'), lang='idt'), 'isa vírgula telu lima'
        )
        self.assertEqual(
            num2words(Decimal('3.14159'), lang='idt'),
            'telu vírgula isa aat isa lima sia'
        )
        self.assertEqual(
            num2words(Decimal('101.22'), lang='idt'),
            'atus isa resin isa vírgula rua rua'
        )
        self.assertEqual(
            num2words(Decimal('2345.75'), lang='idt'),
            'rihun rua atus telu aatnulu resin lima vírgula hitu lima'
        )


    def test_cardinal_float_negative(self):
        self.assertEqual(
            num2words(Decimal('-2.34'), lang='idt'),
            'menus rua vírgula telu aat'
        )
        self.assertEqual(
            num2words(Decimal('-9.99'), lang='idt'),
            'menus sia vírgula sia sia'
        )
        self.assertEqual(
            num2words(Decimal('-7.01'), lang='idt'),
            'menus hitu vírgula maok isa'
        )
        self.assertEqual(
            num2words(Decimal('-222.22'), lang='idt'),
            'menus atus rua ruanulu resin rua vírgula rua rua'
        )

    def test_currency_integer(self):
        self.assertEqual(self.n2w.to_currency(1.00), 'dolar isa')
        self.assertEqual(self.n2w.to_currency(2.00), 'dolar rua')
        self.assertEqual(self.n2w.to_currency(3.00), 'dolar telu')
        self.assertEqual(self.n2w.to_currency(4.00), 'dolar aat')
        self.assertEqual(self.n2w.to_currency(5.00), 'dolar lima')
        self.assertEqual(self.n2w.to_currency(6.00), 'dolar neen')
        self.assertEqual(self.n2w.to_currency(7.00), 'dolar hitu')
        self.assertEqual(self.n2w.to_currency(8.00), 'dolar ualu')
        self.assertEqual(self.n2w.to_currency(9.00), 'dolar sia')
        self.assertEqual(self.n2w.to_currency(10.00), 'dolar sanulu')
        self.assertEqual(self.n2w.to_currency(11.00), 'dolar sanulu resin isa')
        self.assertEqual(self.n2w.to_currency(12.00), 'dolar sanulu resin rua')
        self.assertEqual(self.n2w.to_currency(13.00), 'dolar sanulu resin telu')
        self.assertEqual(self.n2w.to_currency(14.00), 'dolar sanulu resin aat')
        self.assertEqual(self.n2w.to_currency(15.00), 'dolar sanulu resin lima')
        self.assertEqual(self.n2w.to_currency(16.00), 'dolar sanulu resin neen')
        self.assertEqual(self.n2w.to_currency(17.00), 'dolar sanulu resin hitu')
        self.assertEqual(self.n2w.to_currency(18.00), 'dolar sanulu resin ualu')
        self.assertEqual(self.n2w.to_currency(19.00), 'dolar sanulu resin sia')
        self.assertEqual(self.n2w.to_currency(20.00), 'dolar ruanulu')

        self.assertEqual(self.n2w.to_currency(21.00), 'dolar ruanulu resin isa')
        self.assertEqual(self.n2w.to_currency(22.00), 'dolar ruanulu resin rua')
        self.assertEqual(self.n2w.to_currency(35.00), 'dolar telunulu resin lima')
        self.assertEqual(self.n2w.to_currency(99.00), 'dolar sianulu resin sia')

        self.assertEqual(self.n2w.to_currency(100.00), 'dolar atus isa')
        self.assertEqual(self.n2w.to_currency(101.00), 'dolar atus isa resin isa')
        self.assertEqual(
            self.n2w.to_currency(128.00), 'dolar atus isa ruanulu resin ualu'
        )
        self.assertEqual(
            self.n2w.to_currency(713.00), 'dolar atus hitu sanulu resin telu')

        self.assertEqual(self.n2w.to_currency(1000.00), 'dolar rihun isa')
        self.assertEqual(self.n2w.to_currency(1001.00), 'dolar rihun isa resin isa')
        self.assertEqual(
            self.n2w.to_currency(1111.00), 'dolar rihun isa atus isa sanulu resin isa')
        self.assertEqual(
            self.n2w.to_currency(2114.00), 'dolar rihun rua atus isa sanulu resin aat'
        )
        self.assertEqual(
            self.n2w.to_currency(73421.00),
            'dolar rihun hitunulu resin telu atus aat ruanulu resin isa'
        )

        self.assertEqual(self.n2w.to_currency(100000.00), 'dolar rihun atus isa')
        self.assertEqual(
            self.n2w.to_currency(250050.00),
            'dolar rihun atus rua limanulu limanulu'
        )
        self.assertEqual(
            self.n2w.to_currency(6000000.00),
            'dolar miliaun neen'
        )
        self.assertEqual(
            self.n2w.to_currency(19000000000.00),
            'dolar miliaun rihun sanulu resin sia'
        )
        self.assertEqual(
            self.n2w.to_currency(145000000002.00),
            'dolar miliaun rihun atus isa aatnulu resin lima resin rua'
        )
        self.assertEqual(self.n2w.to_currency(1.00, currency='USD'),
                         'dolar isa')
        self.assertEqual(self.n2w.to_currency(1.50, currency='USD'),
                         'dolar isa sentavu limanulu')
        with self.assertRaises(NotImplementedError):
            self.n2w.to_currency(1.00, currency='CHF')

    def test_currency_integer_negative(self):
        self.assertEqual(self.n2w.to_currency(-1.00), 'menus dolar isa')
        self.assertEqual(
            self.n2w.to_currency(-256.00),
            'menus dolar atus rua limanulu resin neen'
        )
        self.assertEqual(self.n2w.to_currency(-1000.00), 'menus dolar rihun isa')
        self.assertEqual(
            self.n2w.to_currency(-1000000.00), 'menus dolar miliaun isa'
        )
        self.assertEqual(
            self.n2w.to_currency(-1234567.00),
            'menus dolar miliaun isa rihun atus rua telunulu resin aat atus lima neenulu resin hitu'
        )

    def test_currency_float(self):
        self.assertEqual(self.n2w.to_currency(Decimal('1.00')), 'dolar isa')
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.01')), 'dolar isa sentavu isa'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.03')), 'dolar isa sentavu telu'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.35')),
            'dolar isa sentavu telunulu resin lima'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('3.14')),
            'dolar telu sentavu sanulu resin aat'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('101.22')),
            'dolar atus isa resin isa sentavu ruanulu resin rua'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('2345.75')),
            'dolar rihun rua atus telu aatnulu resin lima sentavu hitunulu resin lima'
        )

    def test_currency_float_negative(self):
        self.assertEqual(
            self.n2w.to_currency(Decimal('-2.34')),
            'menus dolar rua sentavu telunulu resin aat'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-9.99')),
            'menus dolar sia sentavu sianulu resin sia'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-7.01')),
            'menus dolar hitu sentavu isa'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-222.22')),
            'menus dolar atus rua ruanulu resin rua sentavu ruanulu resin rua'
        )

    def test_year(self):
        self.assertEqual(self.n2w.to_year(1001), 'rihun isa resin isa')
        self.assertEqual(
            self.n2w.to_year(1789), 'rihun isa atus hitu ualunulu resin sia'
        )
        self.assertEqual(
            self.n2w.to_year(1942), 'rihun isa atus sia aatnulu resin rua'
        )
        self.assertEqual(
            self.n2w.to_year(1984), 'rihun isa atus sia ualunulu resin aat'
        )
        self.assertEqual(self.n2w.to_year(2000), 'rihun rua')
        self.assertEqual(self.n2w.to_year(2001), 'rihun rua resin isa')
        self.assertEqual(self.n2w.to_year(2016), 'rihun rua sanulu resin neen')

    def test_year_negative(self):
        self.assertEqual(self.n2w.to_year(-30), 'telunulu antes Kristu')
        self.assertEqual(
            self.n2w.to_year(-744),
            'atus hitu aatnulu resin aat antes Kristu'
        )
        self.assertEqual(
            self.n2w.to_year(-10000),
            'rihun sanulu antes Kristu'
        )
