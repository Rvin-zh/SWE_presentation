# Programmer A's changes (loyalty_feature.py)
class ShopManager:
    def __init__(self, data_dir="shop_data"):
        # Existing initialization code...
        self.discounts_file = self.data_dir / "discounts.json"
        self.discounts = self._load_json(self.discounts_file)

    def add_discount(self, product_name, percentage, start_date, end_date):
        self.discounts[product_name] = {
            "percentage": percentage,
            "start_date": start_date,
            "end_date": end_date,
        }
        self._save_json(self.discounts, self.discounts_file)

    def sell_product(self, name, quantity, customer_id=None):
        success = super().sell_product(name, quantity)
        if success and customer_id:
            points = int(self.inventory[name]["price"] * quantity)
            self.customers[customer_id]["points"] += points
            self._update_customer_tier(customer_id)
        return success
