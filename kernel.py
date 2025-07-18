from planner import Planner
from plugin_manager import PluginManager

class Kernel:
    def __init__(self):
        self.planner = Planner()
        self.plugin_manager = PluginManager()

def main():
    core = Kernel()
    print("AI Kernel ready. Type commands:")
    while True:
        instruction = input(">> ")
        if instruction.lower() in ("exit", "quit"):
            print("Exiting kernel.")
            break
        try:
            plan = core.planner.create_plan(instruction)
            core.plugin_manager.execute_plan(plan)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
