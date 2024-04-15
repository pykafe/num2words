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
from num2words.lang_MGM_S import Num2Word_MGM_S


class Num2WordsMGMTest(TestCase):
    def setUp(self):
        super().setUp()
        self.n2w = Num2Word_MGM_S()

    def test_cardinal_integer(self):
        self.assertEqual(num2words(1, lang='mgm-S'), 'iid')
        self.assertEqual(num2words(2, lang='mgm-S'), 'ruu')
        self.assertEqual(num2words(3, lang='mgm-S'), 'teul')
        self.assertEqual(num2words(4, lang='mgm-S'), 'faat')
        self.assertEqual(num2words(5, lang='mgm-S'), 'liim')
        self.assertEqual(num2words(6, lang='mgm-S'), 'liim nai-ida')
        self.assertEqual(num2words(7, lang='mgm-S'), 'liim nai-rua')
        self.assertEqual(num2words(8, lang='mgm-S'), 'liim nai-telu')
        self.assertEqual(num2words(9, lang='mgm-S'), 'liim nai-fata')
        self.assertEqual(num2words(10, lang='mgm-S'), 'saguul')
        self.assertEqual(num2words(11, lang='mgm-S'), 'saguul resi iid')
        self.assertEqual(num2words(12, lang='mgm-S'), 'saguul resi ruu')
        self.assertEqual(num2words(13, lang='mgm-S'), 'saguul resi teul')
        self.assertEqual(num2words(14, lang='mgm-S'), 'saguul resi faat')
        self.assertEqual(num2words(15, lang='mgm-S'), 'saguul resi liim')
        self.assertEqual(num2words(16, lang='mgm-S'), 'saguul resi liim nai-ida')
        self.assertEqual(num2words(17, lang='mgm-S'), 'saguul resi liim nai-rua')
        self.assertEqual(num2words(18, lang='mgm-S'), 'saguul resi liim nai-telu')
        self.assertEqual(num2words(19, lang='mgm-S'), 'saguul resi liim nai-fata')
        self.assertEqual(num2words(20, lang='mgm-S'), 'saguul haet rua')

        self.assertEqual(num2words(21, lang='mgm-S'), 'saguul haet rua resi iid')
        self.assertEqual(num2words(22, lang='mgm-S'), 'saguul haet rua resi ruu')
        self.assertEqual(num2words(35, lang='mgm-S'), 'saguul haet teul resi liim')
        self.assertEqual(num2words(99, lang='mgm-S'), 'saguul haet liim nai-fata resi liim nai-fata')

        self.assertEqual(num2words(100, lang='mgm-S'), 'atus iid')
        self.assertEqual(num2words(101, lang='mgm-S'), 'atus iid resi iid')
        self.assertEqual(num2words(107, lang='mgm-S'), 'atus iid resi liim nai-rua')
        self.assertEqual(num2words(110, lang='mgm-S'), 'atus iid saguul')
        self.assertEqual(num2words(114, lang='mgm-S'), 'atus iid saguul resi faat')
        self.assertEqual(num2words(128, lang='mgm-S'), 'atus iid saguul haet rua resi liim nai-telu')
        self.assertEqual(num2words(151, lang='mgm-S'), 'atus iid saguul haet liim resi iid')
        self.assertEqual(num2words(713, lang='mgm-S'), 'atus liim nai-rua saguul resi teul')
        self.assertEqual(num2words(999, lang='mgm-S'), 'atus liim nai-fata saguul haet liim nai-fata resi liim nai-fata')

        self.assertEqual(num2words(1000, lang='mgm-S'), 'rihun iid')
        self.assertEqual(num2words(1001, lang='mgm-S'), 'rihun iid resi iid')
        self.assertEqual(num2words(1011, lang='mgm-S'), 'rihun iid saguul resi iid')
        self.assertEqual(num2words(1111, lang='mgm-S'), 'rihun iid atus iid saguul resi iid')
        self.assertEqual(num2words(2357, lang='mgm-S'), 'rihun ruu atus teul saguul haet liim resi liim nai-rua')
        self.assertEqual(
            num2words(2200, lang='mgm-S'),
            'rihun ruu atus ruu'
        )
        self.assertEqual(num2words(2230, lang='mgm-S'), 'rihun ruu atus ruu saguul haet teul')
        self.assertEqual(num2words(73400, lang='mgm-S'), 'rihun saguul haet liim nai-rua resi teul atus faat')
        self.assertEqual(num2words(73421, lang='mgm-S'), 'rihun saguul haet liim nai-rua resi teul atus faat saguul haet rua resi iid')
        self.assertEqual(num2words(100000, lang='mgm-S'), 'rihun atus iid')
        self.assertEqual(num2words(250050, lang='mgm-S'), 'rihun atus ruu saguul haet liim saguul haet liim')
        self.assertEqual(
            num2words(6000000, lang='mgm-S'), 'miliaun liim nai-ida'
        )
        self.assertEqual(
            num2words(100000000, lang='mgm-S'), 'miliaun atus iid'
        )
        self.assertEqual(
            num2words(19000000000, lang='mgm-S'), 'miliaun rihun saguul resi liim nai-fata'
        )
        self.assertEqual(
            num2words(145000000002, lang='mgm-S'),
            'miliaun rihun atus iid saguul haet faat resi liim resi ruu'
        )
        self.assertEqual(
            num2words(4635102, lang='mgm-S'),
            'miliaun faat rihun atus liim nai-ida saguul haet teul resi liim atus iid resi ruu'
        )
        self.assertEqual(
            num2words(145254635102, lang='mgm-S'),
            'miliaun rihun atus iid saguul haet faat resi liim atus ruu saguul haet liim resi faat rihun atus liim nai-ida saguul haet teul resi liim atus iid resi ruu'
        )
        self.assertEqual(
            num2words(1000000000000, lang='mgm-S'),
            'biliaun iid'
        )
        self.assertEqual(
            num2words(2000000000000, lang='mgm-S'),
            'biliaun ruu'
        )
        self.assertEqual(
            num2words(1000000000000000, lang='mgm-S'),
            'biliaun rihun iid'
        )
        self.assertEqual(
            num2words(2000000000000000, lang='mgm-S'),
            'biliaun rihun ruu'
        )
        self.assertEqual(
            num2words(1000000000000000000, lang='mgm-S'),
            'triliaun iid'
        )
        self.assertEqual(
            num2words(2000000000000000000, lang='mgm-S'),
            'triliaun ruu'
        )

    def test_cardinal_integer_negative(self):
        self.assertEqual(num2words(-1, lang='mgm-S'), 'menus iid')
        self.assertEqual(
            num2words(-256, lang='mgm-S'), 'menus atus ruu saguul haet liim resi liim nai-ida'
        )
        self.assertEqual(num2words(-1000, lang='mgm-S'), 'menus rihun iid')
        self.assertEqual(num2words(-1000000, lang='mgm-S'), 'menus miliaun iid')
        self.assertEqual(
            num2words(-1234567, lang='mgm-S'),
            'menus miliaun iid rihun atus ruu saguul haet teul resi faat atus liim saguul haet liim nai-ida resi liim nai-rua'
        )

    def test_cardinal_float(self):
        self.assertEqual(num2words(Decimal('1.00'), lang='mgm-S'), 'iid')
        self.assertEqual(num2words(
            Decimal('1.01'), lang='mgm-S'), 'iid vírgula mamu iid')
        self.assertEqual(num2words(
            Decimal('1.035'), lang='mgm-S'), 'iid vírgula mamu teul liim'
        )
        self.assertEqual(num2words(
            Decimal('1.35'), lang='mgm-S'), 'iid vírgula teul liim'
        )
        self.assertEqual(
            num2words(Decimal('3.14159'), lang='mgm-S'),
            'teul vírgula iid faat iid liim liim nai-fata'
        )
        self.assertEqual(
            num2words(Decimal('101.22'), lang='mgm-S'),
            'atus iid resi iid vírgula ruu ruu'
        )
        self.assertEqual(
            num2words(Decimal('2345.75'), lang='mgm-S'),
            'rihun ruu atus teul saguul haet faat resi liim vírgula liim nai-rua liim'
        )


    def test_cardinal_float_negative(self):
        self.assertEqual(
            num2words(Decimal('-2.34'), lang='mgm-S'),
            'menus ruu vírgula teul faat'
        )
        self.assertEqual(
            num2words(Decimal('-9.99'), lang='mgm-S'),
            'menus liim nai-fata vírgula liim nai-fata liim nai-fata'
        )
        self.assertEqual(
            num2words(Decimal('-7.01'), lang='mgm-S'),
            'menus liim nai-rua vírgula mamu iid'
        )
        self.assertEqual(
            num2words(Decimal('-222.22'), lang='mgm-S'),
            'menus atus ruu saguul haet rua resi ruu vírgula ruu ruu'
        )

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang='mgm-S', ordinal=True), 'daiid')
        self.assertEqual(num2words(2, lang='mgm-S', ordinal=True), 'daruu')
        self.assertEqual(num2words(3, lang='mgm-S', ordinal=True), 'dateul')
        self.assertEqual(num2words(4, lang='mgm-S', ordinal=True), 'dafaat')
        self.assertEqual(num2words(5, lang='mgm-S', ordinal=True), 'daliim')
        self.assertEqual(num2words(6, lang='mgm-S', ordinal=True), 'daliim nai-ida')
        self.assertEqual(num2words(7, lang='mgm-S', ordinal=True), 'daliim nai-rua')
        self.assertEqual(num2words(8, lang='mgm-S', ordinal=True), 'daliim nai-telu')
        self.assertEqual(num2words(9, lang='mgm-S', ordinal=True), 'daliim nai-fata')
        self.assertEqual(num2words(10, lang='mgm-S', ordinal=True), 'dasaguul')
        self.assertEqual(
            num2words(11, lang='mgm-S', ordinal=True), 'dasaguul resi iid'
        )
        self.assertEqual(
            num2words(12, lang='mgm-S', ordinal=True), 'dasaguul resi ruu'
        )
        self.assertEqual(
            num2words(13, lang='mgm-S', ordinal=True), 'dasaguul resi teul'
        )
        self.assertEqual(
            num2words(14, lang='mgm-S', ordinal=True), 'dasaguul resi faat'
        )
        self.assertEqual(
            num2words(15, lang='mgm-S', ordinal=True), 'dasaguul resi liim'
        )
        self.assertEqual(
            num2words(16, lang='mgm-S', ordinal=True), 'dasaguul resi liim nai-ida'
        )
        self.assertEqual(
            num2words(17, lang='mgm-S', ordinal=True), 'dasaguul resi liim nai-rua'
        )
        self.assertEqual(
            num2words(18, lang='mgm-S', ordinal=True), 'dasaguul resi liim nai-telu'
        )
        self.assertEqual(
            num2words(19, lang='mgm-S', ordinal=True), 'dasaguul resi liim nai-fata'
        )
        self.assertEqual(
            num2words(20, lang='mgm-S', ordinal=True), 'dasaguul haet rua'
        )

        self.assertEqual(
            num2words(21, lang='mgm-S', ordinal=True), 'dasaguul haet rua resi iid'
        )
        self.assertEqual(
            num2words(22, lang='mgm-S', ordinal=True), 'dasaguul haet rua resi ruu'
        )
        self.assertEqual(
            num2words(35, lang='mgm-S', ordinal=True), 'dasaguul haet teul resi liim'
        )
        self.assertEqual(
            num2words(99, lang='mgm-S', ordinal=True), 'dasaguul haet liim nai-fata resi liim nai-fata'
        )

        self.assertEqual(
            num2words(100, lang='mgm-S', ordinal=True), 'daatus iid'
        )
        self.assertEqual(
            num2words(101, lang='mgm-S', ordinal=True), 'daatus iid resi iid'
        )
        self.assertEqual(
            num2words(128, lang='mgm-S', ordinal=True),
            'daatus iid saguul haet rua resi liim nai-telu'
        )
        self.assertEqual(
            num2words(713, lang='mgm-S', ordinal=True),
            'daatus liim nai-rua saguul resi teul'
        )

        self.assertEqual(
            num2words(1000, lang='mgm-S', ordinal=True), 'darihun iid'
        )
        self.assertEqual(
            num2words(1001, lang='mgm-S', ordinal=True), 'darihun iid resi iid'
        )
        self.assertEqual(
            num2words(1111, lang='mgm-S', ordinal=True),
            'darihun iid atus iid saguul resi iid'
        )
        self.assertEqual(
            num2words(2114, lang='mgm-S', ordinal=True),
            'darihun ruu atus iid saguul resi faat'
        )
        self.assertEqual(
            num2words(73421, lang='mgm-S', ordinal=True),
            'darihun saguul haet liim nai-rua resi teul atus faat saguul haet rua resi iid'
        )

        self.assertEqual(
            num2words(100000, lang='mgm-S', ordinal=True),
            'darihun atus iid'
        )
        self.assertEqual(
            num2words(250050, lang='mgm-S', ordinal=True),
            'darihun atus ruu saguul haet liim saguul haet liim'
        )
        self.assertEqual(
            num2words(6000000, lang='mgm-S', ordinal=True), 'damiliaun liim nai-ida'
        )
        self.assertEqual(
            num2words(19000000000, lang='mgm-S', ordinal=True),
            'damiliaun rihun saguul resi liim nai-fata'
        )
        self.assertEqual(
            num2words(145000000002, lang='mgm-S', ordinal=True),
            'damiliaun rihun atus iid saguul haet faat resi liim resi ruu'
        )

    def test_currency_integer(self):
        self.assertEqual(self.n2w.to_currency(1.00), 'dolar iid')
        self.assertEqual(self.n2w.to_currency(2.00), 'dolar ruu')
        self.assertEqual(self.n2w.to_currency(3.00), 'dolar teul')
        self.assertEqual(self.n2w.to_currency(4.00), 'dolar faat')
        self.assertEqual(self.n2w.to_currency(5.00), 'dolar liim')
        self.assertEqual(self.n2w.to_currency(6.00), 'dolar liim nai-ida')
        self.assertEqual(self.n2w.to_currency(7.00), 'dolar liim nai-rua')
        self.assertEqual(self.n2w.to_currency(8.00), 'dolar liim nai-telu')
        self.assertEqual(self.n2w.to_currency(9.00), 'dolar liim nai-fata')
        self.assertEqual(self.n2w.to_currency(10.00), 'dolar saguul')
        self.assertEqual(self.n2w.to_currency(11.00), 'dolar saguul resi iid')
        self.assertEqual(self.n2w.to_currency(12.00), 'dolar saguul resi ruu')
        self.assertEqual(self.n2w.to_currency(13.00), 'dolar saguul resi teul')
        self.assertEqual(self.n2w.to_currency(14.00), 'dolar saguul resi faat')
        self.assertEqual(self.n2w.to_currency(15.00), 'dolar saguul resi liim')
        self.assertEqual(self.n2w.to_currency(16.00), 'dolar saguul resi liim nai-ida')
        self.assertEqual(self.n2w.to_currency(17.00), 'dolar saguul resi liim nai-rua')
        self.assertEqual(self.n2w.to_currency(18.00), 'dolar saguul resi liim nai-telu')
        self.assertEqual(self.n2w.to_currency(19.00), 'dolar saguul resi liim nai-fata')
        self.assertEqual(self.n2w.to_currency(20.00), 'dolar saguul haet rua')

        self.assertEqual(self.n2w.to_currency(21.00), 'dolar saguul haet rua resi iid')
        self.assertEqual(self.n2w.to_currency(22.00), 'dolar saguul haet rua resi ruu')
        self.assertEqual(self.n2w.to_currency(35.00), 'dolar saguul haet teul resi liim')
        self.assertEqual(self.n2w.to_currency(99.00), 'dolar saguul haet liim nai-fata resi liim nai-fata')

        self.assertEqual(self.n2w.to_currency(100.00), 'dolar atus iid')
        self.assertEqual(self.n2w.to_currency(101.00), 'dolar atus iid resi iid')
        self.assertEqual(
            self.n2w.to_currency(128.00), 'dolar atus iid saguul haet rua resi liim nai-telu'
        )
        self.assertEqual(
            self.n2w.to_currency(713.00), 'dolar atus liim nai-rua saguul resi teul')

        self.assertEqual(self.n2w.to_currency(1000.00), 'dolar rihun iid')
        self.assertEqual(self.n2w.to_currency(1001.00), 'dolar rihun iid resi iid')
        self.assertEqual(
            self.n2w.to_currency(1111.00), 'dolar rihun iid atus iid saguul resi iid')
        self.assertEqual(
            self.n2w.to_currency(2114.00), 'dolar rihun ruu atus iid saguul resi faat'
        )
        self.assertEqual(
            self.n2w.to_currency(73421.00),
            'dolar rihun saguul haet liim nai-rua resi teul atus faat saguul haet rua resi iid'
        )

        self.assertEqual(self.n2w.to_currency(100000.00), 'dolar rihun atus iid')
        self.assertEqual(
            self.n2w.to_currency(250050.00),
            'dolar rihun atus ruu saguul haet liim saguul haet liim'
        )
        self.assertEqual(
            self.n2w.to_currency(6000000.00),
            'dolar miliaun liim nai-ida'
        )
        self.assertEqual(
            self.n2w.to_currency(19000000000.00),
            'dolar miliaun rihun saguul resi liim nai-fata'
        )
        self.assertEqual(
            self.n2w.to_currency(145000000002.00),
            'dolar miliaun rihun atus iid saguul haet faat resi liim resi ruu'
        )
        self.assertEqual(self.n2w.to_currency(1.00, currency='USD'),
                         'dolar iid')
        self.assertEqual(self.n2w.to_currency(1.50, currency='USD'),
                         'dolar iid sentavu saguul haet liim')
        with self.assertRaises(NotImplementedError):
            self.n2w.to_currency(1.00, currency='CHF')

    def test_currency_integer_negative(self):
        self.assertEqual(self.n2w.to_currency(-1.00), 'menus id dólar')
        self.assertEqual(
            self.n2w.to_currency(-256.00),
            'menus atusid ru gullim resi hohonid dólares'
        )
        self.assertEqual(self.n2w.to_currency(-1000.00), 'menus rihunid id dólares')
        self.assertEqual(
            self.n2w.to_currency(-1000000.00), 'menus miliaunid id dólares'
        )
        self.assertEqual(
            self.n2w.to_currency(-1234567.00),
            'menus miliaunid id rihunid atusid ru gulteil resi pat atusid lim gulhohonid resi hohoru dólares'
        )

    def test_currency_float(self):
        self.assertEqual(self.n2w.to_currency(Decimal('1.00')), 'id dólar')
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.01')), 'id dólar resi id cêntimu'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.03')), 'id dólar resi teil cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.35')),
            'id dólar resi gulteil resi lim cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('3.14')),
            'teil dólares resi sagul resi pat cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('101.22')),
            'atusid id resi id dólares resi gulru resi ru cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('2345.75')),
            'rihunid ru atusid teil gulpat resi lim dólares resi gulhohoru resi lim cêntimus'

        )

    def test_currency_float_negative(self):
        self.assertEqual(
            self.n2w.to_currency(Decimal('-2.34')),
            'menus ru dólares resi gulteil resi pat cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-9.99')),
            'menus hohopat dólares resi gulhohopat resi hohopat cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-7.01')),
            'menus hohoru dólares resi id cêntimu'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-222.22')),
            'menus atusid ru gulru resi ru dólares resi gulru resi ru cêntimus'
        )

    def test_year(self):
        self.assertEqual(self.n2w.to_year(1001), 'rihunid id resi id')
        self.assertEqual(
            self.n2w.to_year(1789), 'rihunid id atusid hohoru gulhohoteil resi hohopat'
        )
        self.assertEqual(
            self.n2w.to_year(1942), 'rihunid id atusid hohopat gulpat resi ru'
        )
        self.assertEqual(
            self.n2w.to_year(1984), 'rihunid id atusid hohopat gulhohoteil resi pat'
        )
        self.assertEqual(self.n2w.to_year(2000), 'rihunid ru')
        self.assertEqual(self.n2w.to_year(2001), 'rihunid ru resi id')
        self.assertEqual(self.n2w.to_year(2016), 'rihunid ru sagul resi hohonid')

    def test_year_negative(self):
        self.assertEqual(self.n2w.to_year(-30), 'gulteil muna Kristu')
        self.assertEqual(
            self.n2w.to_year(-744),
            'atusid hohoru gulpat resi pat muna Kristu'
        )
        self.assertEqual(
            self.n2w.to_year(-10000),
            'rihunid sagul muna Kristu'
        )

    def test_to_ordinal_num(self):
        self.assertEqual(self.n2w.to_ordinal_num(1), '1º')
        self.assertEqual(self.n2w.to_ordinal_num(100), '100º')
