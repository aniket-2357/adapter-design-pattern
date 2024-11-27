from Adapter.WeightMachineAdapterImpl import WeightMachineAdapterImpl
from Adaptee.WeightMachineForBabies import WeightMachineForBabies
if __name__ == "__main__":
    weight_machine_adapter = WeightMachineAdapterImpl(WeightMachineForBabies())
    print(weight_machine_adapter.get_weight_in_kg())
