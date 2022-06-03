# You run an e-commerce website and want to record the last N order ids in a log. 
# Implement a data structure to accomplish this, with the following API:
# -record(order_id): adds the order_id to the log
# -get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.

class Order():
    def __init__(self):
        self.orderIds = []
    
    def record(self, order_id):
        self.orderIds.append(order_id)

    def get_last(self, i):
    # i-th last element from the log
        return self.orderIds[-i]

if __name__ == "__main__":
    eCommerceOrders = Order()
    # add log from 1 to 100
    for i in range(1, 101):
        eCommerceOrders.record(i)

print(eCommerceOrders.get_last(10))
