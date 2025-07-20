import sys
from dataclasses import dataclass, field
from typing import Dict
from .market import Market

@dataclass
class Player:
    cash: float = 1000.0
    portfolio: Dict[str, int] = field(default_factory=dict)

    def buy(self, stock: str, amount: int, market: Market) -> bool:
        price = market.get_price(stock) * amount
        if price <= self.cash and amount > 0:
            self.cash -= price
            self.portfolio[stock] = self.portfolio.get(stock, 0) + amount
            return True
        return False

    def sell(self, stock: str, amount: int, market: Market) -> bool:
        if self.portfolio.get(stock, 0) >= amount > 0:
            self.portfolio[stock] -= amount
            self.cash += market.get_price(stock) * amount
            return True
        return False

class Game:
    def __init__(self, turns: int = 10):
        self.market = Market()
        self.player = Player()
        self.turns = turns

    def display_state(self) -> None:
        print(f"Cash: ${self.player.cash:.2f}")
        print("Portfolio:")
        for stock, qty in self.player.portfolio.items():
            price = self.market.get_price(stock)
            print(f"  {stock}: {qty} shares @ ${price:.2f}")
        print("Market Prices:")
        for stock, price in self.market.prices.items():
            print(f"  {stock}: ${price:.2f}")

    def run(self) -> None:
        print("Welcome to the Stock Trading Game!")
        for turn in range(1, self.turns + 1):
            print(f"\n--- Day {turn} ---")
            self.display_state()
            cmd = input("Enter command (buy/sell/quit): ").strip().lower()
            if cmd == 'quit':
                print("Thanks for playing!")
                return
            parts = cmd.split()
            if len(parts) == 3 and parts[0] in {'buy', 'sell'}:
                action, stock, amt = parts
                try:
                    amount = int(amt)
                except ValueError:
                    print("Invalid amount")
                    continue
                if action == 'buy':
                    if not self.player.buy(stock.upper(), amount, self.market):
                        print("Could not complete purchase")
                else:
                    if not self.player.sell(stock.upper(), amount, self.market):
                        print("Could not complete sale")
            else:
                print("Invalid command")
            self.market.update_prices()
        print("Game over!")
        self.display_state()

def main():
    turns = 10
    if len(sys.argv) > 1:
        try:
            turns = int(sys.argv[1])
        except ValueError:
            pass
    Game(turns).run()

if __name__ == '__main__':
    main()
