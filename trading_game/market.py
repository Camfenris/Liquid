import random
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Market:
    prices: Dict[str, float] = field(default_factory=lambda: {
        'AAPL': 100.0,
        'GOOG': 150.0,
        'AMZN': 200.0,
    })

    def update_prices(self) -> None:
        """Randomly update stock prices."""
        for stock, price in self.prices.items():
            change = random.uniform(0.95, 1.05)
            self.prices[stock] = round(price * change, 2)

    def get_price(self, stock: str) -> float:
        return self.prices.get(stock, 0.0)
