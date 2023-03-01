# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    # CASO BASE HECHO EN CLASE
    def test_sell_in_decreases_by_one_every_day(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        gilded_rose = GildedRose([item])
        days = 3
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(7, item.sell_in)

    #CASES WITH +5 DEXTERITY VEST
    def test_decreases_twice_as_fast_when_sell_in_has_passed(self):
        item = Item(name="+5 Dexterity Vest", sell_in=0, quality=20)
        gilded_rose = GildedRose([item])
        days = 3
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(14, item.quality)

    def test_quality_cannot_be_negative(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=0)
        gilded_rose = GildedRose([item])
        days = 3
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(0, item.quality)

    #CASES AGED BRIE
    def test_quality_increases_as_it_ages(self):
        item = Item(name="Aged Brie", sell_in=10, quality=10)
        gilded_rose = GildedRose([item])
        days = 1
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(11, item.quality)

    def test_quality_increases_twice_as_fast_when_sell_in_has_passed(self):
        item = Item(name="Aged Brie", sell_in=0, quality=10)
        gilded_rose = GildedRose([item])
        days = 1
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(12, item.quality)

    def test_quality_cannot_exceed_50(self):
        item = Item(name="Aged Brie", sell_in=10, quality=50)
        gilded_rose = GildedRose([item])
        days = 1
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(50, item.quality)


    #CASES WITH SULFURAS, HAND OF RAGNAROS
    def test_quality_does_not_decrease(self):
        item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)
        gilded_rose = GildedRose([item])
        days = 3
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(80, item.quality)

    def test_sell_in_does_not_change(self):
        item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)
        gilded_rose = GildedRose([item])
        days = 3
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(10, item.sell_in)

    #CASES WITH ELIXIR
    def test_quality_decreases_by_1_each_day(self):
        item = Item(name="Elixir of the Mongoose", sell_in=10, quality=20)
        gilded_rose = GildedRose([item])
        days = 3
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(17, item.quality)

    def test_quality_decreases_twice_as_fast_when_sell_in_has_passed(self):
        item = Item(name="Elixir of the Mongoose", sell_in=0, quality=20)
        gilded_rose = GildedRose([item])
        days = 3
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(14, item.quality)

    def test_quality_cannot_be_negative(self):
        item = Item(name="Elixir of the Mongoose", sell_in=10, quality=0)
        gilded_rose = GildedRose([item])
        days = 3
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(0, item.quality)


    #CASES WITH BACKSTAGE
    def test_quality_increases_by_one_when_sell_in_is_greater_than_ten(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=20, quality=10)
        gilded_rose = GildedRose([item])
        days = 1
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(11, item.quality)

    def test_quality_increases_by_two_when_sell_in_is_between_ten_and_six(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=10)
        gilded_rose = GildedRose([item])
        days = 1
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(12, item.quality)

    def test_quality_increases_by_three_when_sell_in_is_between_five_and_zero(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=10)
        gilded_rose = GildedRose([item])
        days = 1
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(13, item.quality)

    def test_quality_is_zero_when_sell_in_is_zero_or_less(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=10)
        gilded_rose = GildedRose([item])
        days = 1
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(0, item.quality)

    
    #CASES WITH CONJURED
    #PRUEBA FALLIDA
    #def test_quality_decreases_four_times_as_fast_when_sell_in_negative(self):
        #item = Item(name="Conjured Mana Cake", sell_in=10, quality=20)
        #gilded_rose = GildedRose([item])
        #days = 1
        #for _ in range(days):
            #gilded_rose.update_quality()

        #self.assertEquals(8, item.quality)

    #PRUEBA FALLIDA
    #def test_conjured_mana_cake_quality_decreases_twice_as_fast(self):
        #item = Item(name="Conjured Mana Cake", sell_in=10, quality=20)
        #gilded_rose = GildedRose([item])
        #days = 3
        #for _ in range(days):
            #gilded_rose.update_quality()
        #self.assertEquals(14, item.quality)

    #PRUEBA FALLIDA
    #def test_conjured_mana_cake_quality_decreases_four_times_as_fast_after_sell_in(self):
        #item = Item(name="Conjured Mana Cake", sell_in=0, quality=20)
        #gilded_rose = GildedRose([item])
        #days = 3
        #for _ in range(days):
            #gilded_rose.update_quality()

        #self.assertEquals(8, item.quality)

    #PRUEBA ok
    def test_quality_never_negative(self):
        item = Item(name="Conjured Mana Cake", sell_in=10, quality=0)
        gilded_rose = GildedRose([item])
        days = 3
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(0, item.quality)

    
    #CASES WITH NORMAL
    def test_normal_item_quality_decreases_by_1_each_day(self):
        item = Item(name="Normal Item", sell_in=10, quality=20)
        gilded_rose = GildedRose([item])
        days = 3
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(17, item.quality)

    def test_normal_item_quality_decreases_twice_as_fast_when_sell_in_has_passed(self):
        item = Item(name="Normal Item", sell_in=0, quality=20)
        gilded_rose = GildedRose([item])
        days = 3
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(14, item.quality)

    def test_normal_item_quality_cannot_be_negative(self):
        item = Item(name="Normal Item", sell_in=10, quality=0)
        gilded_rose = GildedRose([item])
        days = 3
        for _ in range(days):
            gilded_rose.update_quality()

        self.assertEquals(0, item.quality)

   


if __name__ == '__main__':
    unittest.main()
