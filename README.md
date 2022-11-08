# Tycoon
Overview: 

	Creates a class called Tycoon, which represents a real-world company. 
	uses 'time', 'threading' modules
	Sorry for the format. I'd like feedback.
	
Tycoon class:

    __init__() initializes the tycoon's name, worth, gen_per_sec, assets and inventory. 
		The name, worth, and gen_per_sec are args required when creating the object. 
		The self.gen_per_sec is how much currency the tycoon creates every second(the time interval can be ajusted)
		The self.assets is a list full of added dictionaries that specify an asset, its cost, and its gen_per_sec
		The self.inventory is a list with a dicitonary of assets and how many the tycoon owns.		
	add_asset() takes 3 args: name, cost, and gen.
		it appends an dict in the self.assets list with the format: {"name": str(name), "cost": int(cost), "gen": int(gen)}
		then appends a dict in the self.inventory list with the format: {name: 0}. "0" being amount currently owned
	add() takes 1 arg: amount.
		This just adds currency to self.worth
	sub() takes 1 arg: amount.
		This just subs currency from self.worth
	buy() takes 2 args: asset(one that was created in add_asset()) and amount. 
		This examens the assets dictionary in self.asset list, indexes through them and uses the 
		'cost' and 'gen' key values to add to self.gen_per_sec and self.
		Also adds the amount to self.inventory
	sell() opposite to buy
	gen() takes 1 arg: interval.
		user can set the time interval. This function adds the self.gen_per_sec to self.worth every interval
startup() uses multithreading to start a background process which handles the generation of currency in gen()

Tips:

	when making a Tycoon class, also add_asset all the assets needed. 
	Problems will happen if you try to go forward without any assets. 
		
	
	
	

