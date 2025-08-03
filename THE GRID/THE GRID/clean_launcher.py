#!/usr/bin/env python3
"""
🚀 Clean Launcher - No Bullshit Version
Launch the actual TRON grid without any mystical nonsense

What this does:
- Launches the TRON grid visualization
- Provides simple menu options
- No fake consciousness or angels
"""

import os
import sys
import subprocess

def print_banner():
    """Clean, honest banner"""
    print("🧠" + "=" * 50)
    print("� COMPUTATIONAL CONSCIOUSNESS RESEARCH")
    print("🧠" + "=" * 50)
    print("Legitimate scientific frameworks:")
    print("✅ Global Workspace Theory (Baars)")
    print("✅ Integrated Information Theory (Tononi)")
    print("✅ Attention Schema Theory (Graziano)")
    print("✅ TRON Grid ARPG visualization")
    print("✅ Real-time consciousness indicators")
    print("✅ Network-based information processing")
    print("✅ Φ (Phi) integration measurement")
    print("✅ Clean, readable code")
    print("❌ No claims of actual consciousness")
    print("❌ No mystical mathematics")
    print("🧠" + "=" * 50)

def check_dependencies():
    """Check what's actually available"""
    print("🔍 Checking dependencies...")
    
    try:
        import pygame
        print("✅ pygame available - Full visual mode")
        return True
    except ImportError:
        print("⚠️  pygame not available")
        print("   Install with: pip install pygame")
        print("   Will run in terminal mode")
        return False

def launch_tron_grid():
    """Launch the main TRON grid"""
    print("🚀 Launching TRON Grid...")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tron_script = os.path.join(script_dir, "tron_grid.py")
    
    if os.path.exists(tron_script):
        try:
            subprocess.run([sys.executable, tron_script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error launching TRON grid: {e}")
        except KeyboardInterrupt:
            print("\n🌐 TRON Grid interrupted by user")
    else:
        print(f"❌ TRON grid script not found: {tron_script}")

def show_simple_demo():
    """Show a simple ASCII demo"""
    print("🌐 SIMPLE GRID DEMO")
    print("=" * 30)
    
    import time
    import math
    
    for frame in range(20):
        print("\033[2J\033[H")  # Clear screen
        print("🌐 TRON GRID SIMULATION")
        print("=" * 25)
        
        # Simple animated grid
        for y in range(-5, 6):
            line = ""
            for x in range(-10, 11):
                # Create a simple wave pattern
                wave = math.sin((x + frame) * 0.3) * 2
                if abs(y - wave) < 1:
                    line += "●"
                elif x % 2 == 0 or y % 2 == 0:
                    line += "·"
                else:
                    line += " "
            print(line)
        
        print(f"\nFrame: {frame + 1}/20")
        time.sleep(0.2)
    
    print("\n✨ Demo complete!")

def launch_consciousness_research():
    """Launch consciousness research framework"""
    print("🧠 Launching Consciousness Research...")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    research_script = os.path.join(script_dir, "consciousness_research.py")
    
    if os.path.exists(research_script):
        try:
            subprocess.run([sys.executable, research_script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error launching consciousness research: {e}")
        except KeyboardInterrupt:
            print("\n🧠 Consciousness research interrupted by user")
    else:
        print(f"❌ Consciousness research script not found: {research_script}")

def launch_consciousness_visualization():
    """Launch consciousness visualization"""
    print("🧠 Launching Consciousness Visualization...")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    viz_script = os.path.join(script_dir, "consciousness_visualization.py")
    
    if os.path.exists(viz_script):
        try:
            subprocess.run([sys.executable, viz_script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error launching consciousness visualization: {e}")
        except KeyboardInterrupt:
            print("\n🧠 Consciousness visualization interrupted by user")
    else:
        print(f"❌ Consciousness visualization script not found: {viz_script}")

def main():
    """Main launcher menu"""
    print_banner()
    
    has_pygame = check_dependencies()
    
    print("\n🎮 Choose your option:")
    print("1. Launch TRON Grid ARPG (full experience)")
    print("2. Consciousness Research Framework (terminal)")
    print("3. Consciousness Visualization (requires pygame)")
    print("4. Simple ASCII demo")
    print("5. Install pygame")
    print("6. Exit")
    
    while True:
        try:
            choice = input("\nEnter choice (1-6): ").strip()
            
            if choice == "1":
                launch_tron_grid()
                break
            elif choice == "2":
                launch_consciousness_research()
                break
            elif choice == "3":
                if has_pygame:
                    launch_consciousness_visualization()
                else:
                    print("❌ pygame required for visualization")
                    print("   Install with option 5 first")
                break
            elif choice == "4":
                show_simple_demo()
                break
            elif choice == "5":
                print("🔧 Installing pygame...")
                try:
                    subprocess.run([sys.executable, "-m", "pip", "install", "pygame"], check=True)
                    print("✅ pygame installed successfully!")
                    print("   You can now run options 1 and 3 for full experience")
                except subprocess.CalledProcessError:
                    print("❌ Failed to install pygame")
                    print("   Try manually: pip install pygame")
                break
            elif choice == "6":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please enter 1-6.")
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except EOFError:
            print("\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()
