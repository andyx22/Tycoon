import time
from threading import Thread

#add getters and setters before upload
class Tycoon:
    #create instance with a name. The Tycoon's generated amount per second is defaulted to 0, along with default worth.
    #self.assets is a list with all created assets, formatted in: {"name": name, "cost": cost, "gen": gen}. Gen is the asset's amount generated per second. 
    #self.inventory is a list containing the asset's names and number the Tycoon owns.
    def __init__(self, name, gen=0, worth=0):
        self.name = name
        self.worth = worth
        self.gen_per_sec = gen
        self.assets = []
        self.inventory = []

    #Takes 3 args to form dict, which is appended to self.assets. A separate dict is created with name
    #and 0 amount and appended into self.inventory. Name must be unique. 
    def add_asset(self, name: str, cost: int, gen: int):
        if name in self.assets:
            return Exception("Asset name must not already exist in self.asset")
        asset = {"name": str(name), "cost": int(cost), "gen": int(gen)}
        self.assets.append(asset)
        self.inventory.append({name: 0})

    #adds an int amount to self.worth
    def add(self, amount: int):
        self.worth = self.worth + int(amount)

    #subtracts an int amount from self.worth
    def sub(self, amount: int):
        self.worth = self.worth - int(amount)

    #Takes 2 args, asset name, and amount. Buying an asset decreases respective amount from self.worth,
    #increases self.gen_per_sec, and increases asset amount in self.inventory
    def buy(self, asset, amount: int):
        #search through self.assets to find asset name, and assign the dictionary's values to variables
        for i in self.assets: 
            if i["name"] == asset:
                asset_price = i["cost"]
                asset_gen = i["gen"]
                print(asset_price)
                total_price = asset_price * int(amount)
                self.worth = self.worth - total_price
                self.gen_per_sec = self.gen_per_sec + asset_gen
        for j in self.inventory:
            if asset in j:
                j[asset] += amount

    #same as buy, but subtracts
    def sell(self, asset, amount: int):
        for i in self.assets:
            if i["name"] == asset:
                asset_price = i["cost"]
                asset_gen = i["gen"]
                total_price = asset_price * int(amount)
                self.worth = self.worth + total_price
                self.gen_per_sec = self.gen_per_sec - asset_gen
        for j in self.inventory:
            if asset in j:
                j[asset] -= amount

    #Takes 1 arg: interval. adds self.gen_per_sec to self.worth every time interval in seconds. Default is once every second
    def gen(self, interval=1):
        while True:
            self.worth = self.worth + self.gen_per_sec
            time.sleep(interval)

#takes 1 arg: Tycoon object. Using the "threading" module, a process using Tycoon.gen() function infinitely runs in the background.
#Problems: Program doesn't stop when ctrl-C. The Tycoon.gen() function never stops. Do this after you created all necessary class information.
def startup(Tycoon):
    proc = Thread(target=Tycoon.gen)
    proc.start()