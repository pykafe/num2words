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
from num2words.lang_MGM_NC import Num2Word_MGM_NC


class Num2WordsMGMTest(TestCase):
    def setUp(self):
        super().setUp()
        self.n2w = Num2Word_MGM_NC()

    def test_cardinal_integer(self):
        self.assertEqual(num2words(1, lang='mgm-NC'), 'iid')
        self.assertEqual(num2words(2, lang='mgm-NC'), 'ruu')
        self.assertEqual(num2words(3, lang='mgm-NC'), 'teul')
        self.assertEqual(num2words(4, lang='mgm-NC'), 'faat')
        self.assertEqual(num2words(5, lang='mgm-NC'), 'liim')
        self.assertEqual(num2words(6, lang='mgm-NC'), 'neen')
        self.assertEqual(num2words(7, lang='mgm-NC'), 'hitu')
        self.assertEqual(num2words(8, lang='mgm-NC'), 'ualu')
        self.assertEqual(num2words(9, lang='mgm-NC'), 'sia')
        self.assertEqual(num2words(10, lang='mgm-NC'), 'sakuul')
        self.assertEqual(num2words(11, lang='mgm-NC'), 'sakuul resi iid')
        self.assertEqual(num2words(12, lang='mgm-NC'), 'sakuul resi ruu')
        self.assertEqual(num2words(13, lang='mgm-NC'), 'sakuul resi teul')
        self.assertEqual(num2words(14, lang='mgm-NC'), 'sakuul resi faat')
        self.assertEqual(num2words(15, lang='mgm-NC'), 'sakuul resi liim')
        self.assertEqual(num2words(16, lang='mgm-NC'), 'sakuul resi neen')
        self.assertEqual(num2words(17, lang='mgm-NC'), 'sakuul resi hitu')
        self.assertEqual(num2words(18, lang='mgm-NC'), 'sakuul resi ualu')
        self.assertEqual(num2words(19, lang='mgm-NC'), 'sakuul resi sia')
        self.assertEqual(num2words(20, lang='mgm-NC'), 'rua nuul')

        self.assertEqual(num2words(21, lang='mgm-NC'), 'rua nuul resi iid')
        self.assertEqual(num2words(22, lang='mgm-NC'), 'rua nuul resi ruu')
        self.assertEqual(num2words(35, lang='mgm-NC'), 'teul nuul resi liim')
        self.assertEqual(num2words(99, lang='mgm-NC'), 'sia nuul resi sia')

        self.assertEqual(num2words(100, lang='mgm-NC'), 'atus iid')
        self.assertEqual(num2words(101, lang='mgm-NC'), 'atus iid resi iid')
        self.assertEqual(num2words(107, lang='mgm-NC'), 'atus iid resi hitu')
        self.assertEqual(num2words(110, lang='mgm-NC'), 'atus iid sakuul')
        self.assertEqual(num2words(114, lang='mgm-NC'), 'atus iid sakuul resi faat')
        self.assertEqual(num2words(128, lang='mgm-NC'), 'atus iid rua nuul resi ualu')
        self.assertEqual(num2words(151, lang='mgm-NC'), 'atus iid liim nuul resi iid')
        self.assertEqual(num2words(713, lang='mgm-NC'), 'atus hitu sakuul resi teul')
        self.assertEqual(num2words(999, lang='mgm-NC'), 'atus sia sia nuul resi sia')

        self.assertEqual(num2words(1000, lang='mgm-NC'), 'rihun iid')
        self.assertEqual(num2words(1001, lang='mgm-NC'), 'rihun iid resi iid')
        self.assertEqual(num2words(1011, lang='mgm-NC'), 'rihun iid sakuul resi iid')
        self.assertEqual(num2words(1111, lang='mgm-NC'), 'rihun iid atus iid sakuul resi iid')
        self.assertEqual(num2words(2357, lang='mgm-NC'), 'rihun ruu atus teul liim nuul resi hitu')
        self.assertEqual(
            num2words(2200, lang='mgm-NC'),
            'rihun ruu atus ruu'
        )
        self.assertEqual(num2words(2230, lang='mgm-NC'), 'rihun ruu atus ruu teul nuul')
        self.assertEqual(num2words(73400, lang='mgm-NC'), 'rihun hitu nuul resi teul atus faat')
        self.assertEqual(num2words(73421, lang='mgm-NC'), 'rihun hitu nuul resi teul atus faat rua nuul resi iid')
        self.assertEqual(num2words(100000, lang='mgm-NC'), 'rihun atus iid')
        self.assertEqual(num2words(250050, lang='mgm-NC'), 'rihun atus ruu liim nuul liim nuul')
        self.assertEqual(
            num2words(6000000, lang='mgm-NC'), 'miliaun neen'
        )
        self.assertEqual(
            num2words(100000000, lang='mgm-NC'), 'miliaun atus iid'
        )
        self.assertEqual(
            num2words(19000000000, lang='mgm-NC'), 'miliaun rihun sakuul resi sia'
        )
        self.assertEqual(
            num2words(145000000002, lang='mgm-NC'),
            'miliaun rihun atus iid faat nuul resi liim resi ruu'
        )
        self.assertEqual(
            num2words(4635102, lang='mgm-NC'),
            'miliaun faat rihun atus neen teul nuul resi liim atus iid resi ruu'
        )
        self.assertEqual(
            num2words(145254635102, lang='mgm-NC'),
            'miliaun rihun atus iid faat nuul resi liim atus ruu liim nuul resi faat rihun atus neen teul nuul resi liim atus iid resi ruu'
        )
        self.assertEqual(
            num2words(1000000000000, lang='mgm-NC'),
            'biliaun iid'
        )
        self.assertEqual(
            num2words(2000000000000, lang='mgm-NC'),
            'biliaun ruu'
        )
        self.assertEqual(
            num2words(1000000000000000, lang='mgm-NC'),
            'biliaun rihun iid'
        )
        self.assertEqual(
            num2words(2000000000000000, lang='mgm-NC'),
            'biliaun rihun ruu'
        )
        self.assertEqual(
            num2words(1000000000000000000, lang='mgm-NC'),
            'triliaun iid'
        )
        self.assertEqual(
            num2words(2000000000000000000, lang='mgm-NC'),
            'triliaun ruu'
        )

    def test_cardinal_integer_negative(self):
        self.assertEqual(num2words(-1, lang='mgm-NC'), 'menus iid')
        self.assertEqual(
            num2words(-256, lang='mgm-NC'), 'menus atus ruu liim nuul resi neen'
        )
        self.assertEqual(num2words(-1000, lang='mgm-NC'), 'menus rihun iid')
        self.assertEqual(num2words(-1000000, lang='mgm'), 'menus miliaun iid')
        self.assertEqual(
            num2words(-1234567, lang='mgm-NC'),
            'menus miliaun iid rihun atus ruu teul nuul resi faat atus liim neen nuul resi hitu'
        )

    def test_cardinal_float(self):
        self.assertEqual(num2words(Decimal('1.00'), lang='mgm-NC'), 'iid')
        self.assertEqual(num2words(
            Decimal('1.01'), lang='mgm-NC'), 'iid vírgula mamu iid')
        self.assertEqual(num2words(
            Decimal('1.035'), lang='mgm-NC'), 'iid vírgula mamu teul liim'
        )
        self.assertEqual(num2words(
            Decimal('1.35'), lang='mgm-NC'), 'iid vírgula teul liim'
        )
        self.assertEqual(
            num2words(Decimal('3.14159'), lang='mgm-NC'),
            'teul vírgula iid faat iid liim sia'
        )
        self.assertEqual(
            num2words(Decimal('101.22'), lang='mgm-NC'),
            'atus iid resi iid vírgula ruu ruu'
        )
        self.assertEqual(
            num2words(Decimal('2345.75'), lang='mgm-NC'),
            'rihun ruu atus teul faat nuul resi liim vírgula hitu liim'
        )


    def test_cardinal_float_negative(self):
        self.assertEqual(
            num2words(Decimal('-2.34'), lang='mgm-NC'),
            'menus ruu vírgula teul faat'
        )
        self.assertEqual(
            num2words(Decimal('-9.99'), lang='mgm-NC'),
            'menus sia vírgula sia sia'
        )
        self.assertEqual(
            num2words(Decimal('-7.01'), lang='mgm-NC'),
            'menus hitu vírgula mamu iid'
        )
        self.assertEqual(
            num2words(Decimal('-222.22'), lang='mgm-NC'),
            'menus atus ruu rua nuul resi ruu vírgula ruu ruu'
        )

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang='mgm-NC', ordinal=True), 'daiid')
        self.assertEqual(num2words(2, lang='mgm-NC', ordinal=True), 'daruu')
        self.assertEqual(num2words(3, lang='mgm-NC', ordinal=True), 'dateul')
        self.assertEqual(num2words(4, lang='mgm-NC', ordinal=True), 'dafaat')
        self.assertEqual(num2words(5, lang='mgm-NC', ordinal=True), 'daliim')
        self.assertEqual(num2words(6, lang='mgm-NC', ordinal=True), 'daneen')
        self.assertEqual(num2words(7, lang='mgm-NC', ordinal=True), 'dahitu')
        self.assertEqual(num2words(8, lang='mgm-NC', ordinal=True), 'daualu')
        self.assertEqual(num2words(9, lang='mgm-NC', ordinal=True), 'dasia')
        self.assertEqual(num2words(10, lang='mgm-NC', ordinal=True), 'dasakuul')
        self.assertEqual(
            num2words(11, lang='mgm-NC', ordinal=True), 'dasakuul resi iid'
        )
        self.assertEqual(
            num2words(12, lang='mgm-NC', ordinal=True), 'dasakuul resi ruu'
        )
        self.assertEqual(
            num2words(13, lang='mgm-NC', ordinal=True), 'dasakuul resi teul'
        )
        self.assertEqual(
            num2words(14, lang='mgm-NC', ordinal=True), 'dasakuul resi faat'
        )
        self.assertEqual(
            num2words(15, lang='mgm-NC', ordinal=True), 'dasakuul resi liim'
        )
        self.assertEqual(
            num2words(16, lang='mgm-NC', ordinal=True), 'dasakuul resi neen'
        )
        self.assertEqual(
            num2words(17, lang='mgm-NC', ordinal=True), 'dasakuul resi hitu'
        )
        self.assertEqual(
            num2words(18, lang='mgm-NC', ordinal=True), 'dasakuul resi ualu'
        )
        self.assertEqual(
            num2words(19, lang='mgm-NC', ordinal=True), 'dasakuul resi sia'
        )
        self.assertEqual(
            num2words(20, lang='mgm-NC', ordinal=True), 'darua nuul'
        )

        self.assertEqual(
            num2words(21, lang='mgm-NC', ordinal=True), 'darua nuul resi iid'
        )
        self.assertEqual(
            num2words(22, lang='mgm-NC', ordinal=True), 'darua nuul resi ruu'
        )
        self.assertEqual(
            num2words(35, lang='mgm-NC', ordinal=True), 'dateul nuul resi liim'
        )
        self.assertEqual(
            num2words(99, lang='mgm-NC', ordinal=True), 'dasia nuul resi sia'
        )

        self.assertEqual(
            num2words(100, lang='mgm-NC', ordinal=True), 'daatus iid'
        )
        self.assertEqual(
            num2words(101, lang='mgm-NC', ordinal=True), 'daatus iid resi iid'
        )
        self.assertEqual(
            num2words(128, lang='mgm-NC', ordinal=True),
            'daatus iid rua nuul resi ualu'
        )
        self.assertEqual(
            num2words(713, lang='mgm-NC', ordinal=True),
            'daatus hitu sakuul resi teul'
        )

        self.assertEqual(
            num2words(1000, lang='mgm-NC', ordinal=True), 'darihun iid'
        )
        self.assertEqual(
            num2words(1001, lang='mgm-NC', ordinal=True), 'darihun iid resi iid'
        )
        self.assertEqual(
            num2words(1111, lang='mgm-NC', ordinal=True),
            'darihun iid atus iid sakuul resi iid'
        )
        self.assertEqual(
            num2words(2114, lang='mgm-NC', ordinal=True),
            'darihun ruu atus iid sakuul resi faat'
        )
        self.assertEqual(
            num2words(73421, lang='mgm-NC', ordinal=True),
            'darihun hitu nuul resi teul atus faat rua nuul resi iid'
        )

        self.assertEqual(
            num2words(100000, lang='mgm-NC', ordinal=True),
            'darihun atus iid'
        )
        self.assertEqual(
            num2words(250050, lang='mgm-NC', ordinal=True),
            'darihun atus ruu liim nuul liim nuul'
        )
        self.assertEqual(
            num2words(6000000, lang='mgm-NC', ordinal=True), 'damiliaun neen'
        )
        self.assertEqual(
            num2words(19000000000, lang='mgm-NC', ordinal=True),
            'damiliaun rihun sakuul resi sia'
        )
        self.assertEqual(
            num2words(145000000002, lang='mgm-NC', ordinal=True),
            'damiliaun rihun atus iid faat nuul resi liim resi ruu'
        )

    def test_currency_integer(self):
        self.assertEqual(self.n2w.to_currency(1.00), 'dolar iid')
        self.assertEqual(self.n2w.to_currency(2.00), 'dolar ruu')
        self.assertEqual(self.n2w.to_currency(3.00), 'dolar teul')
        self.assertEqual(self.n2w.to_currency(4.00), 'dolar faat')
        self.assertEqual(self.n2w.to_currency(5.00), 'dolar liim')
        self.assertEqual(self.n2w.to_currency(6.00), 'dolar neen')
        self.assertEqual(self.n2w.to_currency(7.00), 'dolar hitu')
        self.assertEqual(self.n2w.to_currency(8.00), 'dolar ualu')
        self.assertEqual(self.n2w.to_currency(9.00), 'dolar sia')
        self.assertEqual(self.n2w.to_currency(10.00), 'dolar sakuul')
        self.assertEqual(self.n2w.to_currency(11.00), 'dolar sakuul resi iid')
        self.assertEqual(self.n2w.to_currency(12.00), 'dolar sakuul resi ruu')
        self.assertEqual(self.n2w.to_currency(13.00), 'dolar sakuul resi teul')
        self.assertEqual(self.n2w.to_currency(14.00), 'dolar sakuul resi faat')
        self.assertEqual(self.n2w.to_currency(15.00), 'dolar sakuul resi liim')
        self.assertEqual(self.n2w.to_currency(16.00), 'dolar sakuul resi neen')
        self.assertEqual(self.n2w.to_currency(17.00), 'dolar sakuul resi hitu')
        self.assertEqual(self.n2w.to_currency(18.00), 'dolar sakuul resi ualu')
        self.assertEqual(self.n2w.to_currency(19.00), 'dolar sakuul resi sia')
        self.assertEqual(self.n2w.to_currency(20.00), 'dolar rua nuul')

        self.assertEqual(self.n2w.to_currency(21.00), 'dolar rua nuul resi iid')
        self.assertEqual(self.n2w.to_currency(22.00), 'dolar rua nuul resi ruu')
        self.assertEqual(self.n2w.to_currency(35.00), 'dolar teul nuul resi liim')
        self.assertEqual(self.n2w.to_currency(99.00), 'dolar sia nuul resi sia')

        self.assertEqual(self.n2w.to_currency(100.00), 'dolar atus iid')
        self.assertEqual(self.n2w.to_currency(101.00), 'dolar atus iid resi iid')
        self.assertEqual(
            self.n2w.to_currency(128.00), 'dolar atus iid rua nuul resi ualu'
        )
        self.assertEqual(
            self.n2w.to_currency(713.00), 'dolar atus hitu sakuul resi teul')

        self.assertEqual(self.n2w.to_currency(1000.00), 'dolar rihun iid')
        self.assertEqual(self.n2w.to_currency(1001.00), 'dolar rihun iid resi iid')
        self.assertEqual(
            self.n2w.to_currency(1111.00), 'dolar rihun iid atus iid sakuul resi iid')
        self.assertEqual(
            self.n2w.to_currency(2114.00), 'dolar rihun ruu atus iid sakuul resi faat'
        )
        self.assertEqual(
            self.n2w.to_currency(73421.00),
            'dolar rihun hitu nuul resi teul atus faat rua nuul resi iid'
        )

        self.assertEqual(self.n2w.to_currency(100000.00), 'dolar rihun atus iid')
        self.assertEqual(
            self.n2w.to_currency(250050.00),
            'dolar rihun atus ruu liim nuul liim nuul'
        )
        self.assertEqual(
            self.n2w.to_currency(6000000.00),
            'dolar miliaun neen'
        )
        self.assertEqual(
            self.n2w.to_currency(19000000000.00),
            'dolar miliaun rihun sakuul resi sia'
        )
        self.assertEqual(
            self.n2w.to_currency(145000000002.00),
            'dolar miliaun rihun atus iid faat nuul resi liim resi ruu'
        )
        self.assertEqual(self.n2w.to_currency(1.00, currency='USD'),
                         'dolar iid')
        self.assertEqual(self.n2w.to_currency(1.50, currency='USD'),
                         'dolar iid sentavu liim nuul')
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
