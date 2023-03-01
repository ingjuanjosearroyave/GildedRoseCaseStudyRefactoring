class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1

                if item.name == "Aged Brie":
                    self._update_aged_brie_quality(item)
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    self._update_backstage_pass_quality(item)
                elif item.name.startswith("Conjured"):
                    self._update_conjured_item_quality(item)
                else:
                    self._update_normal_item_quality(item)

    def _update_aged_brie_quality(self, item):
        item.quality = min(item.quality + 1, 50)

    def _update_backstage_pass_quality(self, item):
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            item.quality += 3
        elif item.sell_in < 10:
            item.quality += 2
        else:
            item.quality += 1
        item.quality = min(item.quality, 50)

    def _update_conjured_item_quality(self, item):
        item.quality = max(item.quality - 2, 0)

    def _update_normal_item_quality(self, item):
        if item.sell_in < 0:
            item.quality = max(item.quality - 2, 0)
        else:
            item.quality = max(item.quality - 1, 0)
