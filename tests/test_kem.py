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
from num2words.lang_KEM import Num2Word_KEM


class Num2WordsKEMTest(TestCase):
    def setUp(self):
        super().setUp()
        self.n2w = Num2Word_KEM()

    def test_cardinal_integer(self):
        self.assertEqual(num2words(1, lang='kem'), 'sia')
        self.assertEqual(num2words(2, lang='kem'), 'rua')
        self.assertEqual(num2words(3, lang='kem'), 'telu')
        self.assertEqual(num2words(4, lang='kem'), 'paat')
        self.assertEqual(num2words(5, lang='kem'), 'lima')
        self.assertEqual(num2words(6, lang='kem'), 'neem')
        self.assertEqual(num2words(7, lang='kem'), 'itsu')
        self.assertEqual(num2words(8, lang='kem'), 'balu')
        self.assertEqual(num2words(9, lang='kem'), 'sibe')
        self.assertEqual(num2words(10, lang='kem'), 'sapulu')
        self.assertEqual(num2words(11, lang='kem'), 'sapulu resin sia')
        self.assertEqual(num2words(12, lang='kem'), 'sapulu resin rua')
        self.assertEqual(num2words(13, lang='kem'), 'sapulu resin telu')
        self.assertEqual(num2words(14, lang='kem'), 'sapulu resin paat')
        self.assertEqual(num2words(15, lang='kem'), 'sapulu resin lima')
        self.assertEqual(num2words(16, lang='kem'), 'sapulu resin neem')
        self.assertEqual(num2words(17, lang='kem'), 'sapulu resin itsu')
        self.assertEqual(num2words(18, lang='kem'), 'sapulu resin balu')
        self.assertEqual(num2words(19, lang='kem'), 'sapulu resin sibe')
        self.assertEqual(num2words(20, lang='kem'), 'gulurua')

        self.assertEqual(num2words(21, lang='kem'), 'gulurua resin sia')
        self.assertEqual(num2words(22, lang='kem'), 'gulurua resin rua')
        self.assertEqual(num2words(35, lang='kem'), 'gulutelu resin lima')
        self.assertEqual(num2words(99, lang='kem'), 'gulusibe resin sibe')

        self.assertEqual(num2words(100, lang='kem'), 'atsus sia')
        self.assertEqual(num2words(101, lang='kem'), 'atsus sia resin sia')
        self.assertEqual(num2words(107, lang='kem'), 'atsus sia resin itsu')
        self.assertEqual(num2words(110, lang='kem'), 'atsus sia sapulu')
        self.assertEqual(num2words(114, lang='kem'), 'atsus sia sapulu resin paat')
        self.assertEqual(num2words(128, lang='kem'), 'atsus sia gulurua resin balu')
        self.assertEqual(num2words(151, lang='kem'), 'atsus sia gululima resin sia')
        self.assertEqual(num2words(713, lang='kem'), 'atsus itsu sapulu resin telu')
        self.assertEqual(num2words(999, lang='kem'), 'atsus sibe gulusibe resin sibe')

        self.assertEqual(num2words(1000, lang='kem'), 'ribun sia')
        self.assertEqual(num2words(1001, lang='kem'), 'ribun sia resin sia')
        self.assertEqual(num2words(1011, lang='kem'), 'ribun sia sapulu resin sia')
        self.assertEqual(num2words(1111, lang='kem'), 'ribun sia atsus sia sapulu resin sia')
        self.assertEqual(num2words(2357, lang='kem'), 'ribun rua atsus telu gululima resin itsu')
        self.assertEqual(
            num2words(2200, lang='kem'),
            'ribun rua atsus rua'
        )
        self.assertEqual(num2words(2230, lang='kem'), 'ribun rua atsus rua gulutelu')
        self.assertEqual(num2words(73400, lang='kem'), 'ribun guluitsu resin telu atsus paat')
        self.assertEqual(num2words(73421, lang='kem'), 'ribun guluitsu resin telu atsus paat gulurua resin sia')
        self.assertEqual(num2words(100000, lang='kem'), 'ribun atsus sia')
        self.assertEqual(num2words(250050, lang='kem'), 'ribun atsus rua gululima gululima')
        self.assertEqual(
            num2words(6000000, lang='kem'), 'miliaun neem'
        )
        self.assertEqual(
            num2words(100000000, lang='kem'), 'miliaun atsus sia'
        )
        self.assertEqual(
            num2words(19000000000, lang='kem'), 'miliaun ribun sapulu resin sibe'
        )
        self.assertEqual(
            num2words(145000000002, lang='kem'),
            'miliaun ribun atsus sia gulupaat resin lima resin rua'
        )
        self.assertEqual(
            num2words(4635102, lang='kem'),
            'miliaun paat ribun atsus neem gulutelu resin lima atsus sia resin rua'
        )
        self.assertEqual(
            num2words(145254635102, lang='kem'),
            'miliaun ribun atsus sia gulupaat resin lima atsus rua gululima resin paat ribun atsus neem gulutelu resin lima atsus sia resin rua'
        )
        self.assertEqual(
            num2words(1000000000000, lang='kem'),
            'biliaun sia'
        )
        self.assertEqual(
            num2words(2000000000000, lang='kem'),
            'biliaun rua'
        )
        self.assertEqual(
            num2words(1000000000000000, lang='kem'),
            'biliaun ribun sia'
        )
        self.assertEqual(
            num2words(2000000000000000, lang='kem'),
            'biliaun ribun rua'
        )
        self.assertEqual(
            num2words(1000000000000000000, lang='kem'),
            'triliaun sia'
        )
        self.assertEqual(
            num2words(2000000000000000000, lang='kem'),
            'triliaun rua'
        )

    def test_cardinal_integer_negative(self):
        self.assertEqual(num2words(-1, lang='kem'), 'menus sia')
        self.assertEqual(
            num2words(-256, lang='kem'), 'menus atsus rua gululima resin neem'
        )
        self.assertEqual(num2words(-1000, lang='kem'), 'menus ribun sia')
        self.assertEqual(num2words(-1000000, lang='kem'), 'menus miliaun sia')
        self.assertEqual(
            num2words(-1234567, lang='kem'),
            'menus miliaun sia ribun atsus rua gulutelu resin paat atsus lima guluneem resin itsu'
        )

    def test_cardinal_float(self):
        self.assertEqual(num2words(Decimal('1.00'), lang='kem'), 'sia')
        self.assertEqual(num2words(
            Decimal('1.01'), lang='kem'), 'sia virgula bai sia')
        self.assertEqual(num2words(
            Decimal('1.035'), lang='kem'), 'sia virgula bai telu lima'
        )
        self.assertEqual(num2words(
            Decimal('1.35'), lang='kem'), 'sia virgula telu lima'
        )
        self.assertEqual(
            num2words(Decimal('3.14159'), lang='kem'),
            'telu virgula sia paat sia lima sibe'
        )
        self.assertEqual(
            num2words(Decimal('101.22'), lang='kem'),
            'atsus sia resin sia virgula rua rua'
        )
        self.assertEqual(
            num2words(Decimal('2345.75'), lang='kem'),
            'ribun rua atsus telu gulupaat resin lima virgula itsu lima'
        )

    def test_cardinal_float_negative(self):
        self.assertEqual(
            num2words(Decimal('-2.34'), lang='kem'),
            'menus rua virgula telu paat'
        )
        self.assertEqual(
            num2words(Decimal('-9.99'), lang='kem'),
            'menus sibe virgula sibe sibe'
        )
        self.assertEqual(
            num2words(Decimal('-7.01'), lang='kem'),
            'menus itsu virgula bai sia'
        )
        self.assertEqual(
            num2words(Decimal('-222.22'), lang='kem'),
            'menus atsus rua gulurua resin rua virgula rua rua'
        )

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang='kem', ordinal=True), 'saba')
        self.assertEqual(num2words(2, lang='kem', ordinal=True), 'abarua')
        self.assertEqual(num2words(3, lang='kem', ordinal=True), 'abatelu')
        self.assertEqual(num2words(4, lang='kem', ordinal=True), 'abapaat')
        self.assertEqual(num2words(5, lang='kem', ordinal=True), 'abalima')
        self.assertEqual(num2words(6, lang='kem', ordinal=True), 'abaneem')
        self.assertEqual(num2words(7, lang='kem', ordinal=True), 'abaitsu')
        self.assertEqual(num2words(8, lang='kem', ordinal=True), 'ababalu')
        self.assertEqual(num2words(9, lang='kem', ordinal=True), 'abasibe')
        self.assertEqual(num2words(10, lang='kem', ordinal=True), 'abasapulu')
        self.assertEqual(
            num2words(11, lang='kem', ordinal=True), 'décimu primeiru'
        )
        self.assertEqual(
            num2words(12, lang='kem', ordinal=True), 'décimu segundu'
        )
        self.assertEqual(
            num2words(13, lang='kem', ordinal=True), 'décimu terceiru'
        )
        self.assertEqual(
            num2words(14, lang='kem', ordinal=True), 'décimu quartu'
        )
        self.assertEqual(
            num2words(15, lang='kem', ordinal=True), 'décimu quintu'
        )
        self.assertEqual(
            num2words(16, lang='kem', ordinal=True), 'décimu sextu'
        )
        self.assertEqual(
            num2words(17, lang='kem', ordinal=True), 'décimu sétimu'
        )
        self.assertEqual(
            num2words(18, lang='kem', ordinal=True), 'décimu oitavu'
        )
        self.assertEqual(
            num2words(19, lang='kem', ordinal=True), 'décimu nonu'
        )
        self.assertEqual(
            num2words(20, lang='kem', ordinal=True), 'vigésimu'
        )

        self.assertEqual(
            num2words(21, lang='kem', ordinal=True), 'vigésimu primeiru'
        )
        self.assertEqual(
            num2words(22, lang='kem', ordinal=True), 'vigésimu segundu'
        )
        self.assertEqual(
            num2words(35, lang='kem', ordinal=True), 'trigésimu quintu'
        )
        self.assertEqual(
            num2words(99, lang='kem', ordinal=True), 'nonagésimu nonu'
        )

        self.assertEqual(
            num2words(100, lang='kem', ordinal=True), 'centésimu'
        )
        self.assertEqual(
            num2words(101, lang='kem', ordinal=True), 'centésimu primeiru'
        )
        self.assertEqual(
            num2words(128, lang='kem', ordinal=True),
            'centésimu vigésimu oitavu'
        )
        self.assertEqual(
            num2words(713, lang='kem', ordinal=True),
            'septigentésimu décimu terceiru'
        )

        self.assertEqual(
            num2words(1000, lang='kem', ordinal=True), 'milésimu'
        )
        self.assertEqual(
            num2words(1001, lang='kem', ordinal=True), 'milésimu primeiru'
        )
        self.assertEqual(
            num2words(1111, lang='kem', ordinal=True),
            'milésimu centésimu décimu primeiru'
        )
        self.assertEqual(
            num2words(2114, lang='kem', ordinal=True),
            'segundu milésimu centésimu décimu quartu'
        )
        self.assertEqual(
            num2words(73421, lang='kem', ordinal=True),
            'septuagésimu terceiru milésimu quadrigentésimu vigésimu primeiru'
        )

        self.assertEqual(
            num2words(100000, lang='kem', ordinal=True),
            'centésimu milésimu'
        )
        self.assertEqual(
            num2words(250050, lang='kem', ordinal=True),
            'ducentésimu quinquagésimu milésimu quinquagésimu'
        )
        self.assertEqual(
            num2words(6000000, lang='kem', ordinal=True), 'sextu milionésimu'
        )
        self.assertEqual(
            num2words(19000000000, lang='kem', ordinal=True),
            'décimu nonu milésimu milionésimu'
        )
        self.assertEqual(
            num2words(145000000002, lang='kem', ordinal=True),
            'centésimu quadragésimu quintu milésimu milionésimu segundu'
        )

    def test_currency_integer(self):
        self.assertEqual(self.n2w.to_currency(1.00), 'sia dolar')
        self.assertEqual(self.n2w.to_currency(2.00), 'rua dolares')
        self.assertEqual(self.n2w.to_currency(3.00), 'telu dolares')
        self.assertEqual(self.n2w.to_currency(4.00), 'paat dolares')
        self.assertEqual(self.n2w.to_currency(5.00), 'lima dolares')
        self.assertEqual(self.n2w.to_currency(6.00), 'neem dolares')
        self.assertEqual(self.n2w.to_currency(7.00), 'itsu dolares')
        self.assertEqual(self.n2w.to_currency(8.00), 'balu dolares')
        self.assertEqual(self.n2w.to_currency(9.00), 'sibe dolares')
        self.assertEqual(self.n2w.to_currency(10.00), 'sapulu dolares')
        self.assertEqual(self.n2w.to_currency(11.00), 'sapulu resin sia dolares')
        self.assertEqual(self.n2w.to_currency(12.00), 'sapulu resin rua dolares')
        self.assertEqual(self.n2w.to_currency(13.00), 'sapulu resin telu dolares')
        self.assertEqual(self.n2w.to_currency(14.00), 'sapulu resin paat dolares')
        self.assertEqual(self.n2w.to_currency(15.00), 'sapulu resin lima dolares')
        self.assertEqual(self.n2w.to_currency(16.00), 'sapulu resin neem dolares')
        self.assertEqual(self.n2w.to_currency(17.00), 'sapulu resin itsu dolares')
        self.assertEqual(self.n2w.to_currency(18.00), 'sapulu resin balu dolares')
        self.assertEqual(self.n2w.to_currency(19.00), 'sapulu resin sibe dolares')
        self.assertEqual(self.n2w.to_currency(20.00), 'gulurua dolares')

        self.assertEqual(self.n2w.to_currency(21.00), 'gulurua resin sia dolares')
        self.assertEqual(self.n2w.to_currency(22.00), 'gulurua resin rua dolares')
        self.assertEqual(self.n2w.to_currency(35.00), 'gulutelu resin lima dolares')
        self.assertEqual(self.n2w.to_currency(99.00), 'gulusibe resin sibe dolares')

        self.assertEqual(self.n2w.to_currency(100.00), 'atsus sia dolares')
        self.assertEqual(self.n2w.to_currency(101.00), 'atsus sia resin sia dolares')
        self.assertEqual(
            self.n2w.to_currency(128.00), 'atsus sia gulurua resin balu dolares'
        )
        self.assertEqual(
            self.n2w.to_currency(713.00), 'atsus itsu sapulu resin telu dolares')

        self.assertEqual(self.n2w.to_currency(1000.00), 'ribun sia dolares')
        self.assertEqual(self.n2w.to_currency(1001.00), 'ribun sia resin sia dolares')
        self.assertEqual(
            self.n2w.to_currency(1111.00), 'ribun sia atsus sia sapulu resin sia dolares')
        self.assertEqual(
            self.n2w.to_currency(2114.00), 'ribun rua atsus sia sapulu resin paat dolares'
        )
        self.assertEqual(
            self.n2w.to_currency(73421.00),
            'ribun guluitsu resin telu atsus paat gulurua resin sia dolares'
        )

        self.assertEqual(self.n2w.to_currency(100000.00), 'ribun atsus sia dolares')
        self.assertEqual(
            self.n2w.to_currency(250050.00),
            'ribun atsus rua gululima gululima dolares'
        )
        self.assertEqual(
            self.n2w.to_currency(6000000.00),
            'miliaun neem dolares'
        )
        self.assertEqual(
            self.n2w.to_currency(19000000000.00),
            'miliaun ribun sapulu resin sibe dolares'
        )
        self.assertEqual(
            self.n2w.to_currency(145000000002.00),
            'miliaun ribun atsus sia gulupaat resin lima resin rua dolares'
        )
        self.assertEqual(self.n2w.to_currency(1.00, currency='USD'),
                         'sia dolar')
        self.assertEqual(self.n2w.to_currency(1.50, currency='USD'),
                         'sia dolar resin gululima sentavus')
        with self.assertRaises(NotImplementedError):
            self.n2w.to_currency(1.00, currency='CHF')

    def test_currency_integer_negative(self):
        self.assertEqual(self.n2w.to_currency(-1.00), 'menus sia dolar')
        self.assertEqual(
            self.n2w.to_currency(-256.00),
            'menus atsus rua gululima resin neem dolares'
        )
        self.assertEqual(self.n2w.to_currency(-1000.00), 'menus ribun sia dolares')
        self.assertEqual(
            self.n2w.to_currency(-1000000.00), 'menus miliaun sia dolares'
        )
        self.assertEqual(
            self.n2w.to_currency(-1234567.00),
            'menus miliaun sia ribun atsus rua gulutelu resin paat atsus lima guluneem resin itsu dolares'
        )

    def test_currency_float(self):
        self.assertEqual(self.n2w.to_currency(Decimal('1.00')), 'sia dolar')
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.01')), 'sia dolar resin sia sentavu'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.03')), 'sia dolar resin telu sentavus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.35')),
            'sia dolar resin gulutelu resin lima sentavus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('3.14')),
            'telu dolares resin sapulu resin paat sentavus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('101.22')),
            'atsus sia resin sia dolares resin gulurua resin rua sentavus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('2345.75')),
            'ribun rua atsus telu gulupaat resin lima dolares resin guluitsu resin lima sentavus'

        )

    def test_currency_float_negative(self):
        self.assertEqual(
            self.n2w.to_currency(Decimal('-2.34')),
            'menus rua dolares resin gulutelu resin paat sentavus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-9.99')),
            'menus sibe dolares resin gulusibe resin sibe sentavus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-7.01')),
            'menus itsu dolares resin sia sentavu'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-222.22')),
            'menus atsus rua gulurua resin rua dolares resin gulurua resin rua sentavus'
        )

    def test_year(self):
        self.assertEqual(self.n2w.to_year(1001), 'ribun sia resin sia')
        self.assertEqual(
            self.n2w.to_year(1789), 'ribun sia atsus itsu gulubalu resin sibe'
        )
        self.assertEqual(
            self.n2w.to_year(1942), 'ribun sia atsus sibe gulupaat resin rua'
        )
        self.assertEqual(
            self.n2w.to_year(1984), 'ribun sia atsus sibe gulubalu resin paat'
        )
        self.assertEqual(self.n2w.to_year(2000), 'ribun rua')
        self.assertEqual(self.n2w.to_year(2001), 'ribun rua resin sia')
        self.assertEqual(self.n2w.to_year(2016), 'ribun rua sapulu resin neem')

    def test_year_negative(self):
        self.assertEqual(self.n2w.to_year(-30), 'gulutelu baipila eh Kristu')
        self.assertEqual(
            self.n2w.to_year(-744),
            'atsus itsu gulupaat resin paat baipila eh Kristu'
        )
        self.assertEqual(
            self.n2w.to_year(-10000),
            'ribun sapulu baipila eh Kristu'
        )

    def test_to_ordinal_num(self):
        self.assertEqual(self.n2w.to_ordinal_num(1), '1º')
        self.assertEqual(self.n2w.to_ordinal_num(100), '100º')
