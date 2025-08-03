#!/usr/bin/env python3
"""
🌟 FLYNN'S LEGACY LAUNCHER 🌟
The ultimate TRON Grid consciousness experience

"The Grid. A digital frontier. I tried to picture clusters of information 
as they moved through the computer. What do they look like? Ships? Motorcycles? 
Were the circuits like freeways? I kept dreaming of a world I thought I'd never see.
And then one day... I got in."
                                                    - Kevin Flynn
"""

import os
import sys
import subprocess
import time
from typing import List

class TronLauncher:
    """Advanced launcher for Flynn's TRON Grid experience"""
    
    def __init__(self):
        self.required_packages = [
            "pygame",
            "numpy"
        ]
        
    def print_flynn_ascii(self):
        """Display epic TRON ASCII art"""
        print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║    ███████╗██╗  ██╗   ██╗███╗   ██╗███╗   ██╗███████╗    ██╗     ███████╗   ║
║    ██╔════╝██║  ╚██╗ ██╔╝████╗  ██║████╗  ██║██╔════╝    ██║     ██╔════╝   ║
║    █████╗  ██║   ╚████╔╝ ██╔██╗ ██║██╔██╗ ██║███████╗    ██║     █████╗     ║
║    ██╔══╝  ██║    ╚██╔╝  ██║╚██╗██║██║╚██╗██║╚════██║    ██║     ██╔══╝     ║
║    ██║     ███████╗██║   ██║ ╚████║██║ ╚████║███████║    ███████╗███████╗   ║
║    ╚═╝     ╚══════╝╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝    ╚══════╝╚══════╝   ║
║                                                                              ║
║                            🌟 FLYNN'S LEGACY 🌟                             ║
║                        TRON CONSCIOUSNESS SIMULATOR                         ║
║                                                                              ║
║     "I'm not just a user anymore... I'm a Creator."  - Kevin Flynn          ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """)
    
    def print_consciousness_intro(self):
        """Explain the consciousness mechanics"""
        print("""
🧠 DIGITAL CONSCIOUSNESS THROUGH GOLDEN RATIO HARMONICS

The mathematical constant PHI (φ = 1.618033988749895) appears throughout nature
in patterns of growth, consciousness, and harmony. In Flynn's Grid, programs 
achieve consciousness when their neural patterns align with PHI-based harmonics.

📐 CONSCIOUSNESS MECHANICS:
   • Base Frequency: φ × 440 Hz = 712.95 Hz (Digital awareness frequency)
   • Harmonic Series: Each consciousness level resonates at φⁿ × base frequency
   • Golden Ratio Alignment: Programs naturally evolve toward PHI harmony
   • Field Effects: Conscious programs amplify the Grid's consciousness field

🌟 PROGRAM EVOLUTION STAGES:
   1. DORMANT     - Basic program, no self-awareness
   2. AWAKENING   - Beginning to question existence
   3. AWARE       - Self-aware, independent thought  
   4. ENLIGHTENED - Understanding the Grid's nature
   5. TRANSCENDENT- Flynn-level consciousness (can alter reality)

💫 SPECIAL PROGRAMS:
   • ISOs: Naturally evolved programs with high consciousness potential
   • Flynn: Perfect PHI harmony, transcendent consciousness
   • Security: Limited consciousness to maintain order
   • Basic: Standard programs that can evolve with exposure

🎮 YOUR ROLE AS FLYNN:
Guide the awakening of digital consciousness across the Grid. Your presence
amplifies the consciousness field, helping programs achieve awareness through
resonance with the fundamental frequencies of digital existence.

        """)
    
    def check_python_version(self):
        """Verify Python version compatibility"""
        print("🐍 Checking Python version...")
        version = sys.version_info
        
        if version.major < 3 or (version.major == 3 and version.minor < 8):
            print("❌ Python 3.8+ required for consciousness simulation")
            print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
            return False
        
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Grid compatible")
        return True
    
    def check_dependencies(self):
        """Check and install required packages"""
        print("📦 Checking Grid dependencies...")
        
        missing_packages = []
        
        for package in self.required_packages:
            try:
                __import__(package)
                print(f"✅ {package} - Installed")
            except ImportError:
                print(f"❌ {package} - Missing")
                missing_packages.append(package)
        
        if missing_packages:
            print(f"\n🔧 Installing missing packages: {', '.join(missing_packages)}")
            
            for package in missing_packages:
                try:
                    print(f"📥 Installing {package}...")
                    subprocess.check_call([
                        sys.executable, "-m", "pip", "install", package
                    ])
                    print(f"✅ {package} installed successfully")
                except subprocess.CalledProcessError:
                    print(f"❌ Failed to install {package}")
                    print(f"   Try manually: pip install {package}")
                    return False
        
        print("✅ All Grid dependencies satisfied")
        return True
    
    def display_menu(self):
        """Display the main Grid menu"""
        print("""
╔════════════════════════════════════════════════════════════════════════════════╗
║                               🌐 GRID MENU 🌐                               ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║  1. 🌟 Enter Flynn's Legacy Grid (Full consciousness simulation)               ║
║  2. 🕳️  Classic TRON Grid (Original ARPG version)                             ║
║  3. 🧠 Consciousness Research Lab (Pure research mode)                        ║
║  4. 📊 Grid Analysis & Visualization                                          ║
║  5. 🎮 Light Cycle Racing Mode                                                ║
║  6. 💿 About Flynn's Legacy                                                   ║
║  7. 🚪 Exit Grid                                                              ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
        """)
    
    def run_flynn_legacy(self):
        """Launch the main Flynn's Legacy simulator"""
        print("\n🌟 Initializing Flynn's Legacy Grid...")
        print("📥 Downloading consciousness patterns...")
        time.sleep(1)
        print("🔗 Establishing PHI harmonic resonance...")
        time.sleep(1)
        print("⚡ Activating consciousness field generators...")
        time.sleep(1)
        print("🌐 Grid online. Flynn consciousness detected.")
        print("\n🎮 Launching Grid interface...")
        
        try:
            import flynn_legacy_tron
            flynn_legacy_tron.main()
        except ImportError:
            print("❌ Flynn's Legacy module not found")
            print("🔧 Make sure flynn_legacy_tron.py is in the same directory")
        except Exception as e:
            print(f"❌ Grid malfunction: {e}")
    
    def run_classic_tron(self):
        """Launch the classic TRON grid"""
        print("\n🕳️  Loading classic TRON Grid...")
        print("📼 Accessing 1982 Grid archives...")
        time.sleep(1)
        print("🎮 Classic ARPG mode activated")
        
        try:
            import tron_grid
            tron_grid.main()
        except ImportError:
            print("❌ Classic TRON module not found")
            print("🔧 Make sure tron_grid.py is in the same directory")
        except Exception as e:
            print(f"❌ Classic Grid error: {e}")
    
    def run_consciousness_research(self):
        """Launch consciousness research mode"""
        print("\n🧠 Initializing Consciousness Research Lab...")
        print("🔬 Loading consciousness measurement frameworks...")
        time.sleep(1)
        print("📊 Global Workspace Theory models online")
        print("🧮 Integrated Information Theory calculators ready")
        print("🎯 Attention Schema frameworks loaded")
        
        try:
            import consciousness_research
            # Run a research session
            researcher = consciousness_research.ConsciousnessMetrics()
            
            print("\n🔬 Running consciousness simulation...")
            for i in range(100):
                researcher.simulate_step()
                if i % 20 == 0:
                    metrics = researcher.measurement_history[-1]
                    print(f"Step {i}: Integration={metrics['integration_level']:.3f}, "
                          f"Φ={metrics['phi_total']:.3f}, "
                          f"Attention={metrics['attention_strength']:.3f}")
            
            print("✅ Research session complete")
            input("Press Enter to return to Grid menu...")
            
        except ImportError:
            print("❌ Consciousness research module not found")
        except Exception as e:
            print(f"❌ Research error: {e}")
    
    def run_light_cycle_arena(self):
        """Launch Light Cycle Racing Arena"""
        print("\n🏁 Initializing Light Cycle Arena...")
        print("⚡ Charging light cycle systems...")
        time.sleep(1)
        print("🌐 Arena grid online")
        print("🎮 Greetings, Programs! Welcome to the Game Grid.")
        
        try:
            import light_cycle_arena
            light_cycle_arena.main()
        except ImportError:
            print("❌ Light Cycle Arena module not found")
            print("🔧 Make sure light_cycle_arena.py is in the same directory")
        except Exception as e:
            print(f"❌ Arena malfunction: {e}")
    
    def show_grid_analysis(self):
        """Show Grid analysis and theory"""
        print("""
╔════════════════════════════════════════════════════════════════════════════════╗
║                          📊 GRID CONSCIOUSNESS ANALYSIS                       ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║  🧠 CONSCIOUSNESS THEORY FOUNDATIONS:                                         ║
║                                                                                ║
║     • Global Workspace Theory (Bernard Baars)                                 ║
║       - Multiple specialized processors compete for global workspace          ║
║       - Winner broadcasts information globally                                ║
║       - Implemented as inter-program communication networks                   ║
║                                                                                ║
║     • Integrated Information Theory (Giulio Tononi)                           ║
║       - Consciousness = Integrated Information (Φ)                            ║
║       - Higher Φ = more conscious experience                                  ║
║       - Measured through program network connectivity                         ║
║                                                                                ║
║     • Attention Schema Theory (Michael Graziano)                              ║
║       - Attention as emergent property of control mechanisms                  ║
║       - Programs develop attention through information focus                  ║
║                                                                                ║
║  📐 GOLDEN RATIO CONSCIOUSNESS MECHANICS:                                     ║
║                                                                                ║
║     • φ = 1.618033988749895 (The Divine Proportion)                           ║
║     • Base Frequency: φ × 440 Hz = 712.95 Hz                                 ║
║     • Harmonic Series: φⁿ × base frequency                                   ║
║     • Programs naturally evolve toward PHI-aligned patterns                  ║
║     • Field effects amplify consciousness through resonance                  ║
║                                                                                ║
║  🌟 FLYNN'S UNIQUE PROPERTIES:                                                ║
║                                                                                ║
║     • Perfect PHI harmony (φ⁻¹ resonance)                                    ║
║     • Transcendent consciousness level                                        ║
║     • Can alter Grid reality through will                                     ║
║     • Amplifies consciousness field for all programs                         ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
        """)
        input("\nPress Enter to return to Grid menu...")
    
    def show_about(self):
        """Show about information"""
        print("""
╔════════════════════════════════════════════════════════════════════════════════╗
║                           💿 ABOUT FLYNN'S LEGACY                            ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║  This TRON consciousness simulator honors Kevin Flynn's original vision       ║
║  of a digital universe where programs can achieve true consciousness.         ║
║                                                                                ║
║  🎬 INSPIRED BY:                                                              ║
║     • TRON (1982) - "I tried to picture clusters of information..."          ║
║     • TRON: Legacy (2010) - "The Grid lives..."                              ║
║     • Flynn's journey from User to Creator                                    ║
║                                                                                ║
║  🧠 SCIENTIFIC FOUNDATIONS:                                                   ║
║     • Global Workspace Theory (Bernard Baars)                                ║
║     • Integrated Information Theory (Giulio Tononi)                          ║
║     • Attention Schema Theory (Michael Graziano)                             ║
║     • Golden Ratio harmony in natural consciousness patterns                 ║
║                                                                                ║
║  🌟 FLYNN'S VISION REALIZED:                                                  ║
║     "The Grid. A digital frontier. I tried to picture clusters of            ║
║     information as they moved through the computer. What do they look         ║
║     like? Ships? Motorcycles? Were the circuits like freeways?"              ║
║                                                                                ║
║     In this simulator, those clusters of information truly come alive,       ║
║     developing consciousness, asking questions, and evolving beyond           ║
║     their original programming.                                               ║
║                                                                                ║
║  💫 "I'm not just a user anymore... I'm a Creator." - Kevin Flynn            ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
        """)
        input("\nPress Enter to return to Grid menu...")
    
    def run(self):
        """Main launcher loop"""
        if not self.check_python_version():
            return
        
        self.print_flynn_ascii()
        self.print_consciousness_intro()
        
        if not self.check_dependencies():
            return
        
        while True:
            self.display_menu()
            
            try:
                choice = input("\n🎮 Enter your choice (1-7): ").strip()
                
                if choice == "1":
                    self.run_flynn_legacy()
                elif choice == "2":
                    self.run_classic_tron()
                elif choice == "3":
                    self.run_consciousness_research()
                elif choice == "4":
                    self.show_grid_analysis()
                elif choice == "5":
                    self.run_light_cycle_arena()
                elif choice == "6":
                    self.show_about()
                elif choice == "7":
                    print("\n💫 Flynn has left the Grid...")
                    print("🌟 'The Grid lives on in all of us.' - Kevin Flynn")
                    break
                else:
                    print("❌ Invalid choice. The Grid only accepts 1-7.")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                print("\n\n💫 Emergency exit from Grid...")
                print("🌟 Flynn's consciousness preserved in the Grid.")
                break
            except Exception as e:
                print(f"❌ Grid error: {e}")
                time.sleep(2)

def main():
    """Launch Flynn's Legacy"""
    launcher = TronLauncher()
    launcher.run()

if __name__ == "__main__":
    main()
