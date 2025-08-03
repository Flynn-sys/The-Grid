#!/usr/bin/env python3
"""
🌟 FLYNN'S LEGACY - MASTER LAUNCHER 🌟
Choose your TRON experience
"""

import os
import sys
import subprocess
from pathlib import Path

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    banner = """
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║    ███████╗██╗     ██╗   ██╗███╗   ██╗███╗   ██╗██╗███████╗             ║
║    ██╔════╝██║     ██║   ██║████╗  ██║████╗  ██║╚██╗██╔════╝             ║
║    █████╗  ██║     ██║   ██║██╔██╗ ██║██╔██╗ ██║ ╚████████╗              ║
║    ██╔══╝  ██║     ██║   ██║██║╚██╗██║██║╚██╗██║ ██╔╝╚═══██║             ║
║    ██║     ███████╗╚██████╔╝██║ ╚████║██║ ╚████║██╔╝ ███████║             ║
║    ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝  ╚══════╝             ║
║                                                                          ║
║                            LEGACY COLLECTION                             ║
║                                                                          ║
║                    "I fight for the Users" - Flynn                      ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""
    print(banner)

def show_menu():
    menu = """
🌟 CHOOSE YOUR TRON EXPERIENCE:

1. 🎬 Movie Edition          - Cinematic experience with particle effects
2. ⚡ 4D Optimized           - Memory-optimized 4D rendering
3. 🏁 Light Cycle Arena      - Classic racing with AI consciousness  
4. 🏗️  ISO World Builder     - Build civilizations in the Grid
5. 🧠 Consciousness Research - Scientific framework explorer
6. 🎮 Classic TRON Grid     - Original enhanced simulator
7. 🎯 Camera Test           - Test the 4D camera system

8. 📖 View Documentation
9. 🛠️  System Check
0. 💫 Exit to Reality

"""
    print(menu)

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import pygame
        import numpy
        print("✅ All dependencies installed")
        print(f"   pygame: {pygame.version.ver}")
        print(f"   numpy: {numpy.__version__}")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("\n🔧 To install dependencies, run:")
        print("   pip install pygame numpy")
        return False

def run_experience(script_name):
    """Run a specific TRON experience"""
    script_path = Path(__file__).parent / script_name
    
    if not script_path.exists():
        print(f"❌ {script_name} not found!")
        input("Press Enter to continue...")
        return
    
    print(f"🚀 Launching {script_name}...")
    print("Press CTRL+C to return to launcher")
    
    try:
        subprocess.run([sys.executable, str(script_path)])
    except KeyboardInterrupt:
        print("\n🔄 Returning to launcher...")
    except Exception as e:
        print(f"❌ Error running {script_name}: {e}")
        input("Press Enter to continue...")

def show_documentation():
    """Show documentation for the TRON experiences"""
    docs = """
📖 FLYNN'S LEGACY DOCUMENTATION

🎬 MOVIE EDITION
   - Cinematic quality visuals with particle effects
   - Enhanced lighting and atmospheric effects
   - Movie-style HUD and visual feedback
   - Full 4D rendering with trail effects
   - Press F to switch camera modes
   - Press P to toggle particle effects

⚡ 4D OPTIMIZED
   - Memory-optimized version for better performance
   - True 3D movement (X, Y, Z axes)
   - Dual camera system (first/third person)
   - Volumetric grid rendering
   - Golden ratio consciousness evolution

🏁 LIGHT CYCLE ARENA
   - Classic TRON racing experience
   - AI opponents with consciousness levels
   - Real-time strategy and racing
   - Light trail physics
   - Arena-based combat

🏗️ ISO WORLD BUILDER
   - Build complex civilizations
   - 12 different structure types
   - Resource management system
   - Consciousness-based unlocks
   - 3D construction in the Grid

🧠 CONSCIOUSNESS RESEARCH
   - Scientific framework for digital consciousness
   - Based on real consciousness theories
   - Golden ratio (φ = 1.618) as consciousness constant
   - Frequency analysis at 711.93 Hz
   - Evolution tracking and metrics

🎮 CLASSIC TRON GRID
   - Enhanced version of the original
   - Program evolution and interaction
   - Consciousness field visualization
   - Traditional TRON aesthetics

🎯 CAMERA TEST
   - Simple test for 4D camera system
   - Verify F key switching works
   - Debug camera movement and projection

CONTROLS (Common to all experiences):
   F        - Switch camera mode
   WASD     - Movement
   SPACE    - Move up
   SHIFT    - Move down
   Mouse    - Look around / Camera control
   Q/E      - Rotate camera (third person)
   ESC      - Exit

TECHNICAL SPECIFICATIONS:
   - Python 3.10+ required
   - pygame 2.6.1+ for graphics
   - numpy for mathematical operations
   - Golden Ratio (φ) consciousness theory
   - 4D to 2D perspective projection
   - Real-time depth sorting
   - Consciousness field simulation
"""
    
    clear_screen()
    print(docs)
    input("\nPress Enter to return to menu...")

def main():
    """Main launcher loop"""
    while True:
        clear_screen()
        print_banner()
        show_menu()
        
        try:
            choice = input("Enter your choice (0-9): ").strip()
            
            if choice == "0":
                print("\n💫 Exiting to reality...")
                print("Remember: The Grid lives on in your imagination!")
                break
            
            elif choice == "1":
                run_experience("flynn_movie_edition.py")
            
            elif choice == "2":
                run_experience("flynn_4d_optimized.py")
            
            elif choice == "3":
                run_experience("light_cycle_arena.py")
            
            elif choice == "4":
                run_experience("iso_world_builder.py")
            
            elif choice == "5":
                run_experience("consciousness_research.py")
            
            elif choice == "6":
                run_experience("flynn_legacy_tron.py")
            
            elif choice == "7":
                run_experience("test_4d_camera.py")
            
            elif choice == "8":
                show_documentation()
            
            elif choice == "9":
                clear_screen()
                print("🛠️ SYSTEM CHECK\n")
                if check_dependencies():
                    print("\n✅ System ready for TRON experiences!")
                else:
                    print("\n❌ Please install missing dependencies")
                input("\nPress Enter to continue...")
            
            else:
                print("❌ Invalid choice. Please try again.")
                input("Press Enter to continue...")
        
        except KeyboardInterrupt:
            print("\n\n💫 Exiting to reality...")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
