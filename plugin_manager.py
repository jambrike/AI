import json
import importlib

class PluginManager:
    def __init__(self):
        with open("capability_map.json", "r") as f:
            self.cap_map = json.load(f)

    def execute_plan(self, plan):
        for step in plan:
            action = step.get("action")
            args = step.get("args", {})
            module_name = self.cap_map.get(action)
            if module_name:
                module = importlib.import_module(f"plugins.{module_name}")
                func = getattr(module, action, None)
                if func:
                    func(**args)
                else:
                    print(f"Plugin '{module_name}' missing action '{action}'.")
            else:
                print(f"No plugin registered for action '{action}'.")
