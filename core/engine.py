# ARES-X File 08: Task Orchestrator
import subprocess
import importlib

class AresEngine:
    def __init__(self):
        self.active_tasks = []

    def execute_logic(self, module_path, target):
        """
        Dynamically loads one of the 35 modules.
        Example: module_path = 'network.scanner'
        """
        try:
            # This 'import_module' allows us to call any file in the /core folder
            module = importlib.import_module(f"core.{module_path}")
            print(f"[!] ARES-X: Launching {module_path} logic against {target}")
            return module.run(target)
        except Exception as e:
            return f"Error executing module: {str(e)}"

    def shell_command(self, cmd):
        """Runs raw terminal commands for the 'Click-to-Trigger' feel."""
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        return process
