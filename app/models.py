from tortoise import fields, models


class BTCPrice(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=50)
    price = fields.DecimalField(max_digits=20, decimal_places=5)
    max_price = fields.DecimalField(max_digits=20, decimal_places=5)
    min_price = fields.DecimalField(max_digits=20, decimal_places=5)
    difference = fields.DecimalField(max_digits=15, decimal_places=4)
    total_amount = fields.DecimalField(max_digits=20, decimal_places=5)
    date = fields.DatetimeField(auto_now_add=True)



