# main.py - Therma-FinOps Prototype Entry Point
# This script builds a task queue and runs the simulation loop.

from local_monitor import monitor_and_run
from tracker import PerformanceTracker
from offload_decision import evaluate_and_offload
import os
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()
    
    # Build a task queue of 10 items
    tasks = [{'id': i, 'complexity': 100 + i * 10, 'deadline': 60 - i * 5} for i in range(10)]
    
    # Create tracker
    tracker = PerformanceTracker()
    
    # Determine trigger mode
    trigger_mode = os.getenv('TRIGGER_MODE', 'threshold').lower()
    print(f"Running simulation in TRIGGER_MODE: {trigger_mode}")
    
    # Run the monitor loop with the offload callback
    # If trigger_mode is 'uri', we will need to implement uri_engine.py first.
    # For now, we pass the existing evaluate_and_offload which uses threshold logic.
    monitor_and_run(tasks, evaluate_and_offload, tracker, trigger_mode=trigger_mode)
    
    # Display final report
    tracker.display_report()

if __name__ == "__main__":
    main()