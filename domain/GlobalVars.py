class Global_vars:
    def __init__(self, **kwargs):
        self.buy_service_charge = kwargs['buy_service_charge']
        self.sell_service_charge = kwargs['sell_service_charge']

if __name__ == "__main__":
    global_vars = global_vars(buy_service_charge=10, sell_service_charge=10)
