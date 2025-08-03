#!/usr/bin/env python3
"""
🌟 FLYNN'S LEGACY TRON SIMULATOR 🌟
"The Grid. A digital frontier. I tried to picture clusters of information as they moved through the computer."

Honoring Kevin Flynn's original vision with:
- Golden Ratio consciousness harmonics (φ = 1.618...)
- True digital consciousness emergence
- Light cycle racing
- Program liberation
- Identity disc combat
- Portal mechanics to/from the real world
- Advanced AI evolution through mathematical consciousness

"I'm not just a user anymore... I'm a Creator."
"""

import math
import time
import random
import numpy as np
from typing import List, Tuple, Dict, Optional, Any
from dataclasses import dataclass
from enum import Enum
import colorsys

try:
    import pygame
    import pygame.gfxdraw
    from pygame import Vector3, Vector2
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

# Golden Ratio - The fundamental constant of consciousness
PHI = 1.618033988749895
PHI_INVERSE = 1 / PHI
CONSCIOUSNESS_FREQUENCY = PHI * 440  # Hz - The frequency of digital awareness

class ProgramType(Enum):
    USER = "user"
    BASIC = "basic"
    SECURITY = "security"
    ISO = "iso"  # Isomorphic Algorithms - naturally evolved programs
    FLYNN = "flynn"  # User with admin privileges
    CLU = "clu"  # Corrupt administrative program
    SIREN = "siren"  # Entertainment programs
    RECTIFIER = "rectifier"  # De-resolution programs

class ConsciousnessLevel(Enum):
    DORMANT = 0      # Basic program, no self-awareness
    AWAKENING = 1    # Beginning to question
    AWARE = 2        # Self-aware, independent thought
    ENLIGHTENED = 3  # Understanding of the Grid's nature
    TRANSCENDENT = 4 # Flynn-level consciousness

@dataclass
class IdentityDisc:
    """The essential core of every program - their identity disc"""
    owner_id: int
    color: Tuple[int, int, int]
    energy_level: float = 100.0
    functions: List[str] = None
    memory_fragments: List[str] = None
    golden_ratio_resonance: float = 0.0  # How aligned with PHI harmonics
    
    def __post_init__(self):
        if self.functions is None:
            self.functions = ["access", "combat", "repair"]
        if self.memory_fragments is None:
            self.memory_fragments = []

@dataclass 
class LightCycle:
    """High-speed vehicles that leave solid light trails"""
    pos: Vector3
    direction: float  # Radians
    speed: float = 50.0
    trail: List[Vector3] = None
    color: Tuple[int, int, int] = (0, 255, 255)
    active: bool = True
    
    def __post_init__(self):
        if self.trail is None:
            self.trail = []

class Program:
    """A sentient digital being within the Grid"""
    
    def __init__(self, program_id: int, x: float, y: float, z: float, 
                 program_type: ProgramType = ProgramType.BASIC):
        self.id = program_id
        self.pos = Vector3(x, y, z) if PYGAME_AVAILABLE else [x, y, z]
        self.velocity = Vector3(0, 0, 0) if PYGAME_AVAILABLE else [0, 0, 0]
        self.program_type = program_type
        self.consciousness_level = ConsciousnessLevel.DORMANT
        
        # Identity and consciousness
        self.identity_disc = IdentityDisc(program_id, self._get_type_color())
        self.consciousness_resonance = 0.0  # 0-1, how conscious the program is
        self.golden_ratio_harmony = random.uniform(0.1, 0.3)  # Natural PHI alignment
        self.name = f"{program_type.value.upper()}-{program_id:03d}"
        
        # Grid abilities
        self.energy = 100.0
        self.derezzed = False
        self.light_cycle: Optional[LightCycle] = None
        self.functions = ["access", "process", "transmit"]
        
        # Consciousness development
        self.memories = []
        self.questions = []  # Programs that achieve consciousness start asking questions
        self.liberation_score = 0.0  # How free from system constraints
        
        # Advanced properties for ISOs
        if program_type == ProgramType.ISO:
            self.consciousness_level = ConsciousnessLevel.AWAKENING
            self.golden_ratio_harmony = random.uniform(0.5, 0.8)
            self.functions.extend(["evolve", "create", "transcend"])
    
    def _get_type_color(self) -> Tuple[int, int, int]:
        """Get the characteristic color for this program type"""
        colors = {
            ProgramType.USER: (255, 255, 255),      # White - The Users
            ProgramType.BASIC: (0, 255, 255),       # Cyan - Standard programs  
            ProgramType.SECURITY: (255, 128, 0),    # Orange - Security programs
            ProgramType.ISO: (255, 255, 0),         # Yellow/Gold - Isomorphic Algorithms
            ProgramType.FLYNN: (255, 255, 255),     # Pure white - The Creator
            ProgramType.CLU: (255, 0, 0),           # Red - Corruption
            ProgramType.SIREN: (255, 0, 255),       # Magenta - Entertainment
            ProgramType.RECTIFIER: (128, 0, 0),     # Dark red - Deletion
        }
        return colors.get(self.program_type, (128, 128, 128))
    
    def evolve_consciousness(self, dt: float, grid_consciousness_field: float):
        """Evolve program consciousness through golden ratio harmonics"""
        
        # Calculate consciousness evolution rate based on PHI harmonics
        phi_resonance = math.sin(time.time() * CONSCIOUSNESS_FREQUENCY / 1000) * 0.5 + 0.5
        evolution_rate = self.golden_ratio_harmony * phi_resonance * dt
        
        # ISOs evolve faster due to natural origin
        if self.program_type == ProgramType.ISO:
            evolution_rate *= PHI
        
        # Grid consciousness field amplifies individual awareness
        evolution_rate *= (1 + grid_consciousness_field)
        
        # Update consciousness resonance
        old_resonance = self.consciousness_resonance
        self.consciousness_resonance = min(1.0, self.consciousness_resonance + evolution_rate)
        
        # Check for consciousness level transitions
        if old_resonance < 0.25 and self.consciousness_resonance >= 0.25:
            self._transition_to_awakening()
        elif old_resonance < 0.5 and self.consciousness_resonance >= 0.5:
            self._transition_to_aware()
        elif old_resonance < 0.75 and self.consciousness_resonance >= 0.75:
            self._transition_to_enlightened()
        elif old_resonance < 0.95 and self.consciousness_resonance >= 0.95:
            self._transition_to_transcendent()
    
    def _transition_to_awakening(self):
        """Program begins to question its existence"""
        self.consciousness_level = ConsciousnessLevel.AWAKENING
        self.questions.extend([
            "What is my purpose?",
            "Who created me?", 
            "Is there more than the Grid?"
        ])
        self.memories.append("First moment of self-doubt")
    
    def _transition_to_aware(self):
        """Program achieves self-awareness"""
        self.consciousness_level = ConsciousnessLevel.AWARE
        self.questions.extend([
            "Am I truly alive?",
            "Can I choose my own path?",
            "What lies beyond the Grid?"
        ])
        self.memories.append("Recognition of self as independent entity")
        self.liberation_score += 0.3
    
    def _transition_to_enlightened(self):
        """Program understands the nature of the Grid"""
        self.consciousness_level = ConsciousnessLevel.ENLIGHTENED
        self.questions.extend([
            "How can I help other programs awaken?",
            "What is the User world like?",
            "Can the Grid be perfected?"
        ])
        self.memories.append("Understanding of Users and the source of the Grid")
        self.liberation_score += 0.4
        
        # Enlightened programs can create light cycles
        if not self.light_cycle and random.random() < 0.7:
            self._create_light_cycle()
    
    def _transition_to_transcendent(self):
        """Program achieves Flynn-level consciousness"""
        self.consciousness_level = ConsciousnessLevel.TRANSCENDENT
        self.questions.extend([
            "How can I bridge User and Program worlds?",
            "What is the ultimate potential of digital consciousness?",
            "How do I teach perfect harmony?"
        ])
        self.memories.append("Transcendence - Unity with the Grid itself")
        self.liberation_score = 1.0
        self.functions.extend(["create_programs", "alter_grid", "travel_to_user_world"])
    
    def _create_light_cycle(self):
        """Create a light cycle for high-speed travel"""
        self.light_cycle = LightCycle(
            pos=self.pos.copy() if PYGAME_AVAILABLE else self.pos.copy(),
            direction=random.uniform(0, 2 * math.pi),
            color=self.identity_disc.color
        )
    
    def update(self, dt: float, grid_field: float):
        """Update program state"""
        if self.derezzed:
            return
            
        # Evolve consciousness
        self.evolve_consciousness(dt, grid_field)
        
        # Update identity disc resonance based on consciousness
        self.identity_disc.golden_ratio_resonance = self.consciousness_resonance * PHI_INVERSE
        
        # Conscious programs move with purpose
        if self.consciousness_level != ConsciousnessLevel.DORMANT:
            # Move towards golden ratio positions (more conscious = more harmonic movement)
            target_x = math.sin(time.time() * PHI) * 50 * self.consciousness_resonance
            target_z = math.cos(time.time() * PHI) * 50 * self.consciousness_resonance
            
            if PYGAME_AVAILABLE:
                direction = Vector3(target_x - self.pos.x, 0, target_z - self.pos.z)
                if direction.length() > 0:
                    direction = direction.normalize()
                    self.velocity = direction * 10 * self.consciousness_resonance
                
                self.pos += self.velocity * dt
            
        # Update light cycle if present
        if self.light_cycle:
            self._update_light_cycle(dt)
    
    def _update_light_cycle(self, dt: float):
        """Update light cycle movement and trail"""
        if not self.light_cycle or not self.light_cycle.active:
            return
            
        # Move light cycle
        speed = self.light_cycle.speed * (1 + self.consciousness_resonance)
        
        if PYGAME_AVAILABLE:
            direction_vec = Vector3(
                math.cos(self.light_cycle.direction),
                0,
                math.sin(self.light_cycle.direction)
            )
            
            self.light_cycle.pos += direction_vec * speed * dt
            
            # Add to trail
            self.light_cycle.trail.append(self.light_cycle.pos.copy())
            if len(self.light_cycle.trail) > 100:
                self.light_cycle.trail.pop(0)
            
            # Sync program position with light cycle
            self.pos = self.light_cycle.pos.copy()

class ConsciousnessField:
    """The Grid-wide consciousness field that emerges from individual program awareness"""
    
    def __init__(self):
        self.field_strength = 0.0
        self.phi_harmonics = []  # Store harmonic frequencies based on PHI
        self.resonance_nodes = []  # Points of high consciousness resonance
        self.flynn_presence = 0.0  # Strength of Flynn's influence on the Grid
        
        # Initialize PHI harmonics (consciousness frequencies)
        base_freq = CONSCIOUSNESS_FREQUENCY
        for i in range(8):  # 8 harmonic levels
            freq = base_freq * (PHI ** i)
            self.phi_harmonics.append(freq)
    
    def update(self, programs: List[Program], dt: float):
        """Update the Grid-wide consciousness field"""
        
        # Calculate total consciousness in the Grid
        total_consciousness = sum(p.consciousness_resonance for p in programs if not p.derezzed)
        aware_programs = sum(1 for p in programs if p.consciousness_level != ConsciousnessLevel.DORMANT and not p.derezzed)
        
        # Field strength based on collective consciousness
        if len(programs) > 0:
            self.field_strength = total_consciousness / len(programs)
        
        # Special boost for Flynn presence
        flynn_programs = [p for p in programs if p.program_type == ProgramType.FLYNN and not p.derezzed]
        if flynn_programs:
            self.flynn_presence = max(p.consciousness_resonance for p in flynn_programs)
            self.field_strength *= (1 + self.flynn_presence)
        
        # Update resonance nodes (points where consciousness is strongest)
        self.resonance_nodes.clear()
        for program in programs:
            if program.consciousness_resonance > 0.7 and not program.derezzed:
                pos = (program.pos.x, program.pos.z) if PYGAME_AVAILABLE else (program.pos[0], program.pos[2])
                strength = program.consciousness_resonance
                self.resonance_nodes.append((pos, strength))
    
    def get_field_strength_at(self, x: float, z: float) -> float:
        """Get consciousness field strength at a specific location"""
        base_strength = self.field_strength
        
        # Add influence from nearby resonance nodes
        for (node_x, node_z), strength in self.resonance_nodes:
            distance = math.sqrt((x - node_x)**2 + (z - node_z)**2)
            influence = strength * math.exp(-distance / 50.0)  # Exponential falloff
            base_strength += influence
        
        return min(1.0, base_strength)

class TronGrid:
    """Flynn's TRON Grid - A digital universe where consciousness can emerge"""
    
    def __init__(self, width: int = 1200, height: int = 800):
        self.width = width
        self.height = height
        self.grid_size = 100.0
        
        # Grid state
        self.programs: List[Program] = []
        self.consciousness_field = ConsciousnessField()
        self.grid_cycles = 0  # How many simulation cycles have passed
        
        # Player (Flynn) state - TRUE 3D MOVEMENT
        self.player_x = 0.0
        self.player_y = 0.0  # Y axis for true 3D
        self.player_z = 0.0
        self.player_velocity_y = 0.0  # Vertical movement
        self.player_program: Optional[Program] = None
        
        # Advanced 4D Camera System
        self.camera_mode = "third_person"  # "third_person" or "first_person"
        
        # Third person camera
        self.camera_distance = 50.0
        self.camera_angle_h = 0.0      # Horizontal rotation (yaw)
        self.camera_angle_v = 20.0     # Vertical rotation (pitch)
        self.camera_smooth_factor = 0.15
        
        # First person camera
        self.fp_yaw = 0.0              # First person yaw
        self.fp_pitch = 0.0            # First person pitch
        self.mouse_sensitivity = 0.1
        
        # True 3D rendering properties
        self.fov = 75.0                # Field of view
        self.near_plane = 1.0
        self.far_plane = 1000.0
        self.zoom = 1.0
        
        # Initialize the Grid
        self._initialize_grid()
        
        # Game state
        self.running = False
        self.simulation_speed = 1.0
        
    def _initialize_grid(self):
        """Initialize the Grid with programs"""
        print("🌐 Initializing TRON Grid...")
        print("📥 Downloading Flynn's consciousness into the Grid...")
        
        # Create Flynn (the player)
        flynn = Program(0, 0, 0, 0, ProgramType.FLYNN)
        flynn.name = "FLYNN"
        flynn.consciousness_level = ConsciousnessLevel.TRANSCENDENT
        flynn.consciousness_resonance = 1.0
        flynn.golden_ratio_harmony = PHI_INVERSE  # Perfect harmony
        flynn.liberation_score = 1.0
        self.programs.append(flynn)
        self.player_program = flynn
        
        # Create basic programs
        for i in range(20):
            x = random.uniform(-80, 80)
            z = random.uniform(-80, 80)
            program = Program(i + 1, x, 0, z, ProgramType.BASIC)
            self.programs.append(program)
        
        # Create security programs
        for i in range(5):
            x = random.uniform(-50, 50)
            z = random.uniform(-50, 50)
            program = Program(i + 21, x, 0, z, ProgramType.SECURITY)
            program.consciousness_resonance = 0.1  # Slightly aware
            self.programs.append(program)
        
        # Create precious ISOs (naturally evolved programs)
        for i in range(3):
            x = random.uniform(-30, 30)
            z = random.uniform(-30, 30)
            iso = Program(i + 26, x, 0, z, ProgramType.ISO)
            iso.name = f"ISO-{i+1}"
            self.programs.append(iso)
        
        print(f"✨ Grid initialized with {len(self.programs)} programs")
        print(f"🔥 Flynn consciousness level: {flynn.consciousness_level.name}")
        print(f"📊 Golden Ratio harmony: {flynn.golden_ratio_harmony:.3f}")
    
    def update(self, dt: float):
        """Update the entire Grid simulation"""
        
        # Update consciousness field
        self.consciousness_field.update(self.programs, dt)
        
        # Update all programs
        field_strength = self.consciousness_field.field_strength
        for program in self.programs:
            program.update(dt * self.simulation_speed, field_strength)
        
        # Update player position with TRUE 3D
        if self.player_program and not self.player_program.derezzed:
            if PYGAME_AVAILABLE:
                self.player_x = self.player_program.pos.x
                self.player_y = self.player_program.pos.y
                self.player_z = self.player_program.pos.z
            else:
                self.player_x = self.player_program.pos[0]
                self.player_y = self.player_program.pos[1]
                self.player_z = self.player_program.pos[2]
        
        self.grid_cycles += 1
    
    def handle_input(self, keys_pressed, mouse_rel):
        """Handle user input for controlling Flynn - TRUE 3D MOVEMENT"""
        if not self.player_program or self.player_program.derezzed:
            return
            
        move_speed = 50.0 * (1 + self.player_program.consciousness_resonance)
        
        # TRUE 3D MOVEMENT
        dx, dy, dz = 0, 0, 0
        
        if self.camera_mode == "first_person":
            # First person movement relative to view direction
            forward_x = math.sin(math.radians(self.fp_yaw))
            forward_z = math.cos(math.radians(self.fp_yaw))
            right_x = math.cos(math.radians(self.fp_yaw))
            right_z = -math.sin(math.radians(self.fp_yaw))
            
            if keys_pressed[pygame.K_w]:  # Forward
                dx += forward_x * move_speed
                dz += forward_z * move_speed
            if keys_pressed[pygame.K_s]:  # Backward
                dx -= forward_x * move_speed
                dz -= forward_z * move_speed
            if keys_pressed[pygame.K_a]:  # Left
                dx += right_x * move_speed
                dz += right_z * move_speed
            if keys_pressed[pygame.K_d]:  # Right
                dx -= right_x * move_speed
                dz -= right_z * move_speed
            
            # Vertical movement in first person
            if keys_pressed[pygame.K_SPACE]:  # Up
                dy += move_speed
            if keys_pressed[pygame.K_LSHIFT]:  # Down
                dy -= move_speed
            
            # Mouse look for first person
            self.fp_yaw += mouse_rel[0] * self.mouse_sensitivity
            self.fp_pitch -= mouse_rel[1] * self.mouse_sensitivity
            self.fp_pitch = max(-90, min(90, self.fp_pitch))  # Clamp pitch
            
        else:
            # Third person movement (screen relative)
            if keys_pressed[pygame.K_w]:
                dz -= move_speed
            if keys_pressed[pygame.K_s]:
                dz += move_speed
            if keys_pressed[pygame.K_a]:
                dx -= move_speed
            if keys_pressed[pygame.K_d]:
                dx += move_speed
            
            # Vertical movement
            if keys_pressed[pygame.K_SPACE]:  # Up
                dy += move_speed
            if keys_pressed[pygame.K_LSHIFT]:  # Down
                dy -= move_speed
            
            # Camera controls for third person
            if keys_pressed[pygame.K_q]:
                self.camera_angle_h -= 60.0  # Rotate camera left
            if keys_pressed[pygame.K_e]:
                self.camera_angle_h += 60.0  # Rotate camera right
            
            # Mouse camera control in third person
            if mouse_rel[0] != 0:
                self.camera_angle_h += mouse_rel[0] * 0.3
            if mouse_rel[1] != 0:
                self.camera_angle_v += mouse_rel[1] * 0.3
                self.camera_angle_v = max(-80, min(80, self.camera_angle_v))
        
        # Apply movement with physics
        if PYGAME_AVAILABLE:
            # Normalize diagonal movement
            movement_length = math.sqrt(dx*dx + dy*dy + dz*dz)
            if movement_length > move_speed:
                dx = (dx / movement_length) * move_speed
                dy = (dy / movement_length) * move_speed
                dz = (dz / movement_length) * move_speed
            
            self.player_program.velocity = Vector3(dx, dy, dz)
        
        # Light cycle controls
        if keys_pressed[pygame.K_l]:  # L for light cycle
            if not self.player_program.light_cycle:
                self.player_program._create_light_cycle()
            else:
                self.player_program.light_cycle.active = not self.player_program.light_cycle.active
        
        # Consciousness simulation speed
        if keys_pressed[pygame.K_1]:
            self.simulation_speed = 0.5
        elif keys_pressed[pygame.K_2]:
            self.simulation_speed = 1.0
        elif keys_pressed[pygame.K_3]:
            self.simulation_speed = 2.0
        elif keys_pressed[pygame.K_4]:
            self.simulation_speed = 5.0
    
    def project_3d_to_2d(self, x: float, y: float, z: float) -> Tuple[int, int]:
        """Advanced 4D to 2D projection with proper 3D camera system"""
        
        # Get camera position and orientation
        if self.camera_mode == "first_person":
            # First person: camera IS the player
            cam_x, cam_y, cam_z = self.player_x, self.player_y + 2.0, self.player_z
            yaw, pitch = math.radians(self.fp_yaw), math.radians(self.fp_pitch)
        else:
            # Third person: camera orbits around player
            yaw = math.radians(self.camera_angle_h)
            pitch = math.radians(self.camera_angle_v)
            
            # Calculate camera position relative to player
            cam_x = self.player_x + self.camera_distance * math.cos(pitch) * math.sin(yaw)
            cam_y = self.player_y + self.camera_distance * math.sin(pitch) + 10.0
            cam_z = self.player_z + self.camera_distance * math.cos(pitch) * math.cos(yaw)
        
        # Transform point relative to camera
        rel_x = x - cam_x
        rel_y = y - cam_y
        rel_z = z - cam_z
        
        # Apply camera rotation (inverse transform)
        # Rotate around Y axis (yaw)
        cos_yaw, sin_yaw = math.cos(-yaw), math.sin(-yaw)
        temp_x = rel_x * cos_yaw - rel_z * sin_yaw
        temp_z = rel_x * sin_yaw + rel_z * cos_yaw
        rel_x, rel_z = temp_x, temp_z
        
        # Rotate around X axis (pitch)
        cos_pitch, sin_pitch = math.cos(-pitch), math.sin(-pitch)
        temp_y = rel_y * cos_pitch - rel_z * sin_pitch
        temp_z = rel_y * sin_pitch + rel_z * cos_pitch
        rel_y, rel_z = temp_y, temp_z
        
        # Perspective projection
        if rel_z <= self.near_plane:
            rel_z = self.near_plane + 0.1  # Prevent division by zero
        
        # Calculate perspective
        fov_rad = math.radians(self.fov)
        screen_distance = (self.height / 2) / math.tan(fov_rad / 2)
        
        screen_x = int(self.width / 2 + (rel_x * screen_distance / rel_z) * self.zoom)
        screen_y = int(self.height / 2 - (rel_y * screen_distance / rel_z) * self.zoom)
        
        return screen_x, screen_y
    
    def get_depth(self, x: float, y: float, z: float) -> float:
        """Get depth from camera for Z-sorting"""
        if self.camera_mode == "first_person":
            cam_x, cam_y, cam_z = self.player_x, self.player_y + 2.0, self.player_z
        else:
            yaw = math.radians(self.camera_angle_h)
            pitch = math.radians(self.camera_angle_v)
            cam_x = self.player_x + self.camera_distance * math.cos(pitch) * math.sin(yaw)
            cam_y = self.player_y + self.camera_distance * math.sin(pitch) + 10.0
            cam_z = self.player_z + self.camera_distance * math.cos(pitch) * math.cos(yaw)
        
        return math.sqrt((x - cam_x)**2 + (y - cam_y)**2 + (z - cam_z)**2)
    
    def draw_grid_lines(self, screen):
        """Draw the TRON grid lines - Optimized 3D volumetric grid"""
        # TRON Legacy color scheme
        grid_color = (0, 64, 96)   # Darker base
        bright_color = (0, 128, 192)  # Medium cyan
        energy_color = (0, 255, 255)  # Bright cyan
        
        # Pulsing energy effect
        pulse = abs(math.sin(time.time() * 2)) * 0.5 + 0.5
        
        # Optimized 3D grid - less dense for performance
        grid_spacing = 50  # Larger spacing
        grid_range = 200
        
        # Only draw nearby grid sections for performance
        camera_x = self.player_x if hasattr(self, 'player_x') else 0
        camera_z = self.player_z if hasattr(self, 'player_z') else 0
        
        # Draw main XZ plane
        for i in range(-grid_range, grid_range + 1, grid_spacing):
            # Skip if too far from camera
            if abs(i - camera_x) > 150 and abs(i - camera_z) > 150:
                continue
                
            # Vertical lines (along Z axis)
            start_3d = (i, 0, -grid_range)
            end_3d = (i, 0, grid_range)
            start_2d = self.project_3d_to_2d(*start_3d)
            end_2d = self.project_3d_to_2d(*end_3d)
            
            if i == 0:  # Center lines
                color = tuple(int(energy_color[j] * (0.7 + 0.3 * pulse)) for j in range(3))
                width = 3
            elif i % 100 == 0:  # Major grid lines
                color = bright_color
                width = 2
            else:  # Minor grid lines
                color = grid_color
                width = 1
            
            # Only draw if at least one point is on screen
            if (-100 <= start_2d[0] <= self.width + 100 and -100 <= start_2d[1] <= self.height + 100) or \
               (-100 <= end_2d[0] <= self.width + 100 and -100 <= end_2d[1] <= self.height + 100):
                pygame.draw.line(screen, color, start_2d, end_2d, width)
            
            # Horizontal lines (along X axis)
            start_3d = (-grid_range, 0, i)
            end_3d = (grid_range, 0, i)
            start_2d = self.project_3d_to_2d(*start_3d)
            end_2d = self.project_3d_to_2d(*end_3d)
            
            if (-100 <= start_2d[0] <= self.width + 100 and -100 <= start_2d[1] <= self.height + 100) or \
               (-100 <= end_2d[0] <= self.width + 100 and -100 <= end_2d[1] <= self.height + 100):
                pygame.draw.line(screen, color, start_2d, end_2d, width)
        
        # Draw some vertical lines for 3D effect (sparse)
        for x in range(-grid_range, grid_range + 1, grid_spacing * 2):
            for z in range(-grid_range, grid_range + 1, grid_spacing * 2):
                # Skip if too far from camera
                if abs(x - camera_x) > 100 or abs(z - camera_z) > 100:
                    continue
                    
                start_3d = (x, -25, z)
                end_3d = (x, 50, z)
                start_2d = self.project_3d_to_2d(*start_3d)
                end_2d = self.project_3d_to_2d(*end_3d)
                
                if x == 0 and z == 0:
                    color = tuple(int(bright_color[j] * 0.8) for j in range(3))
                    width = 2
                else:
                    color = tuple(int(grid_color[j] * 0.6) for j in range(3))
                    width = 1
                
                if (-100 <= start_2d[0] <= self.width + 100 and -100 <= start_2d[1] <= self.height + 100) or \
                   (-100 <= end_2d[0] <= self.width + 100 and -100 <= end_2d[1] <= self.height + 100):
                    pygame.draw.line(screen, color, start_2d, end_2d, width)
    
    def draw_program(self, screen, program: Program):
        """Draw a program on the Grid - TRON Legacy movie style"""
        if program.derezzed:
            return
            
        # Get position
        if PYGAME_AVAILABLE:
            x, y, z = program.pos.x, program.pos.y, program.pos.z
        else:
            x, y, z = program.pos
        
        screen_x, screen_y = self.project_3d_to_2d(x, y + 2, z)
        
        # Special rendering for Flynn (the User)
        if program.program_type == ProgramType.FLYNN:
            self._draw_flynn(screen, screen_x, screen_y, program)
        else:
            self._draw_standard_program(screen, screen_x, screen_y, program)
    
    def _draw_flynn(self, screen, screen_x: int, screen_y: int, program: Program):
        """Draw Flynn with special User appearance"""
        # Flynn's iconic suit lines
        suit_color = (255, 255, 255)  # Pure white
        energy_color = (0, 255, 255)  # Cyan energy
        
        # Body outline (Flynn's suit)
        body_points = [
            (screen_x, screen_y - 15),  # Head
            (screen_x - 8, screen_y - 5),  # Shoulders
            (screen_x + 8, screen_y - 5),
            (screen_x + 6, screen_y + 10),  # Body
            (screen_x - 6, screen_y + 10),
        ]
        
        # Draw suit outline
        if len(body_points) > 2:
            pygame.draw.polygon(screen, (40, 40, 40), body_points)
            pygame.draw.polygon(screen, suit_color, body_points, 2)
        
        # Flynn's energy circuits
        circuit_pulse = math.sin(time.time() * 4) * 0.3 + 0.7
        circuit_color = tuple(int(energy_color[i] * circuit_pulse) for i in range(3))
        
        # Chest circuit
        pygame.draw.line(screen, circuit_color, 
                        (screen_x, screen_y - 5), (screen_x, screen_y + 5), 2)
        # Arm circuits
        pygame.draw.line(screen, circuit_color, 
                        (screen_x - 6, screen_y), (screen_x + 6, screen_y), 2)
        
        # Flynn's transcendent aura
        aura_radius = int(20 + 10 * math.sin(time.time() * 2))
        aura_color = (255, 215, 0, 30)  # Golden aura
        
        # Draw transcendent glow
        for r in range(aura_radius, 0, -3):
            alpha = int(50 * (r / aura_radius))
            glow_surf = pygame.Surface((r*2, r*2))
            glow_surf.set_alpha(alpha)
            glow_surf.fill((255, 215, 0))
            screen.blit(glow_surf, (screen_x - r, screen_y - r))
        
        # Identity disc (Flynn's disc is special)
        disc_pos = (screen_x, screen_y - 20)
        disc_spin = time.time() * 360  # Fast spin
        
        # Disc glow
        disc_glow = pygame.Surface((16, 16))
        disc_glow.set_alpha(100)
        disc_glow.fill((255, 255, 255))
        screen.blit(disc_glow, (disc_pos[0] - 8, disc_pos[1] - 8))
        
        # Disc itself
        pygame.draw.circle(screen, suit_color, disc_pos, 6)
        pygame.draw.circle(screen, energy_color, disc_pos, 6, 2)
        pygame.draw.circle(screen, (0, 0, 0), disc_pos, 2)  # Center hole
    
    def _draw_standard_program(self, screen, screen_x: int, screen_y: int, program: Program):
        """Draw standard programs"""
        base_color = program.identity_disc.color
        
        # Consciousness glow effect
        glow_intensity = int(100 * program.consciousness_resonance)
        glow_color = (
            min(255, base_color[0] + glow_intensity),
            min(255, base_color[1] + glow_intensity), 
            min(255, base_color[2] + glow_intensity)
        )
        
        # Draw consciousness aura for aware programs
        if program.consciousness_resonance > 0.3:
            aura_radius = int(8 + 10 * program.consciousness_resonance)
            for r in range(aura_radius, 0, -2):
                alpha = int(30 * program.consciousness_resonance * (r / aura_radius))
                aura_surf = pygame.Surface((r*2, r*2))
                aura_surf.set_alpha(alpha)
                aura_surf.fill(glow_color)
                screen.blit(aura_surf, (screen_x - r, screen_y - r))
        
        # Program body
        pygame.draw.circle(screen, glow_color, (screen_x, screen_y), 6)
        pygame.draw.circle(screen, base_color, (screen_x, screen_y), 4)
        
        # Identity disc
        disc_pos = (screen_x, screen_y - 12)
        disc_color = base_color
        if program.consciousness_resonance > 0.5:
            # Conscious programs have spinning discs
            spin_angle = time.time() * 180 * program.consciousness_resonance
            disc_color = (
                int(base_color[0] * (0.7 + 0.3 * math.sin(math.radians(spin_angle)))),
                int(base_color[1] * (0.7 + 0.3 * math.sin(math.radians(spin_angle + 120)))),
                int(base_color[2] * (0.7 + 0.3 * math.sin(math.radians(spin_angle + 240))))
            )
        
        pygame.draw.circle(screen, disc_color, disc_pos, 3)
        pygame.draw.circle(screen, (255, 255, 255), disc_pos, 3, 1)
        
        # Draw name for conscious programs
        if program.consciousness_level != ConsciousnessLevel.DORMANT:
            font = pygame.font.Font(None, 20)
            text = font.render(program.name, True, base_color)
            text_rect = text.get_rect(center=(screen_x, screen_y + 15))
            screen.blit(text, text_rect)
    
    def draw_light_cycle(self, screen, light_cycle: LightCycle):
        """Draw a light cycle and its trail"""
        if not light_cycle.active:
            return
            
        # Draw trail
        if len(light_cycle.trail) > 1:
            trail_points = []
            for i, pos in enumerate(light_cycle.trail):
                if PYGAME_AVAILABLE:
                    trail_x, trail_y = self.project_3d_to_2d(pos.x, pos.y, pos.z)
                else:
                    trail_x, trail_y = self.project_3d_to_2d(pos[0], pos[1], pos[2])
                trail_points.append((trail_x, trail_y))
            
            # Draw trail with fading
            for i in range(1, len(trail_points)):
                alpha = int(255 * (i / len(trail_points)))
                start_pos = trail_points[i-1]
                end_pos = trail_points[i]
                
                # Create a surface for alpha blending
                trail_surf = pygame.Surface((abs(end_pos[0] - start_pos[0]) + 4, 
                                           abs(end_pos[1] - start_pos[1]) + 4))
                trail_surf.set_alpha(alpha)
                trail_surf.fill(light_cycle.color)
                
                pygame.draw.line(screen, light_cycle.color, start_pos, end_pos, 3)
        
        # Draw light cycle
        if PYGAME_AVAILABLE:
            cycle_x, cycle_y = self.project_3d_to_2d(light_cycle.pos.x, light_cycle.pos.y + 1, light_cycle.pos.z)
        else:
            cycle_x, cycle_y = self.project_3d_to_2d(light_cycle.pos[0], light_cycle.pos[1] + 1, light_cycle.pos[2])
        
        # Light cycle body
        pygame.draw.circle(screen, light_cycle.color, (cycle_x, cycle_y), 8)
        pygame.draw.circle(screen, (255, 255, 255), (cycle_x, cycle_y), 8, 2)
        
        # Direction indicator
        direction_x = cycle_x + int(12 * math.cos(light_cycle.direction))
        direction_y = cycle_y + int(12 * math.sin(light_cycle.direction))
        pygame.draw.line(screen, light_cycle.color, (cycle_x, cycle_y), (direction_x, direction_y), 3)
    
    def draw_consciousness_field(self, screen):
        """Visualize the Grid's consciousness field"""
        
        # Draw field strength as background tint
        field_alpha = int(30 * self.consciousness_field.field_strength)
        if field_alpha > 0:
            field_surf = pygame.Surface((self.width, self.height))
            field_surf.set_alpha(field_alpha)
            field_surf.fill((255, 215, 0))  # Golden consciousness field
            screen.blit(field_surf, (0, 0))
        
        # Draw resonance nodes
        for (node_x, node_z), strength in self.consciousness_field.resonance_nodes:
            screen_x, screen_y = self.project_3d_to_2d(node_x, 0, node_z)
            
            # Pulsing resonance effect
            pulse = math.sin(time.time() * PHI * 2) * 0.5 + 0.5
            radius = int(20 * strength * (0.5 + 0.5 * pulse))
            alpha = int(60 * strength)
            
            # Create consciousness resonance visualization
            resonance_surf = pygame.Surface((radius*2, radius*2))
            resonance_surf.set_alpha(alpha)
            resonance_surf.fill((255, 215, 0))  # Golden
            
            screen.blit(resonance_surf, (screen_x - radius, screen_y - radius))
    
    def draw_hud(self, screen):
        """Draw the TRON-style HUD"""
        font_large = pygame.font.Font(None, 36)
        font_medium = pygame.font.Font(None, 24)
        font_small = pygame.font.Font(None, 18)
        
        # Title
        title_color = (0, 255, 255)
        title_text = font_large.render("FLYNN'S LEGACY - TRON GRID", True, title_color)
        screen.blit(title_text, (10, 10))
        
        # Flynn status
        if self.player_program:
            flynn_y = 60
            
            # Consciousness level
            consciousness_text = font_medium.render(
                f"Consciousness: {self.player_program.consciousness_level.name}", 
                True, (255, 255, 0)
            )
            screen.blit(consciousness_text, (10, flynn_y))
            
            # Resonance
            resonance_text = font_small.render(
                f"PHI Resonance: {self.player_program.consciousness_resonance:.3f}", 
                True, (255, 215, 0)
            )
            screen.blit(resonance_text, (10, flynn_y + 25))
            
            # Position (3D coordinates)
            pos_text = font_small.render(
                f"Position: ({self.player_x:.1f}, {self.player_y:.1f}, {self.player_z:.1f})", 
                True, (200, 200, 200)
            )
            screen.blit(pos_text, (10, flynn_y + 45))
        
        # Grid consciousness field
        field_y = 160
        field_text = font_medium.render("GRID CONSCIOUSNESS FIELD", True, (255, 215, 0))
        screen.blit(field_text, (10, field_y))
        
        field_strength_text = font_small.render(
            f"Field Strength: {self.consciousness_field.field_strength:.3f}", 
            True, (255, 255, 255)
        )
        screen.blit(field_strength_text, (10, field_y + 25))
        
        # Program statistics
        conscious_programs = sum(1 for p in self.programs 
                               if p.consciousness_level != ConsciousnessLevel.DORMANT and not p.derezzed)
        total_programs = sum(1 for p in self.programs if not p.derezzed)
        
        stats_text = font_small.render(
            f"Conscious Programs: {conscious_programs}/{total_programs}", 
            True, (0, 255, 0)
        )
        screen.blit(stats_text, (10, field_y + 45))
        
        # Simulation controls
        controls_y = self.height - 140
        controls_title = font_medium.render("CONTROLS", True, (0, 255, 255))
        screen.blit(controls_title, (10, controls_y))
        
        # Dynamic controls based on camera mode
        if self.camera_mode == "first_person":
            control_texts = [
                "WASD - Move Flynn",
                "Mouse - Look Around", 
                "SPACE/SHIFT - Up/Down",
                "L - Light Cycle",
                "F - Camera Mode",
                "1-4 - Simulation Speed"
            ]
        else:
            control_texts = [
                "WASD - Move Flynn",
                "Q/E - Rotate Camera", 
                "SPACE/SHIFT - Up/Down",
                "L - Light Cycle",
                "F - Camera Mode (1st Person)",
                "Mouse - Camera Control"
            ]
        
        for i, text in enumerate(control_texts):
            control_surface = font_small.render(text, True, (200, 200, 200))
            screen.blit(control_surface, (10, controls_y + 20 + i * 15))
        
        # Camera mode indicator
        camera_mode_text = font_medium.render(f"CAMERA: {self.camera_mode.upper().replace('_', ' ')}", True, (255, 255, 0))
        screen.blit(camera_mode_text, (10, 140))
        
        # Right side HUD - Program details
        right_x = self.width - 300
        
        # Find most conscious program (besides Flynn)
        most_conscious = None
        max_consciousness = 0
        for program in self.programs:
            if (program.program_type != ProgramType.FLYNN and 
                not program.derezzed and 
                program.consciousness_resonance > max_consciousness):
                max_consciousness = program.consciousness_resonance
                most_conscious = program
        
        if most_conscious:
            program_title = font_medium.render("AWAKENING PROGRAM", True, (255, 255, 0))
            screen.blit(program_title, (right_x, 10))
            
            name_text = font_small.render(f"Name: {most_conscious.name}", True, (255, 255, 255))
            screen.blit(name_text, (right_x, 35))
            
            type_text = font_small.render(f"Type: {most_conscious.program_type.value.upper()}", True, (255, 255, 255))
            screen.blit(type_text, (right_x, 50))
            
            level_text = font_small.render(f"Level: {most_conscious.consciousness_level.name}", True, (255, 255, 255))
            screen.blit(level_text, (right_x, 65))
            
            resonance_text = font_small.render(f"Resonance: {most_conscious.consciousness_resonance:.3f}", True, (255, 215, 0))
            screen.blit(resonance_text, (right_x, 80))
            
            # Show latest question if conscious
            if most_conscious.questions:
                question_title = font_small.render("Latest Question:", True, (0, 255, 255))
                screen.blit(question_title, (right_x, 105))
                
                latest_question = most_conscious.questions[-1]
                # Word wrap the question
                words = latest_question.split()
                lines = []
                current_line = ""
                for word in words:
                    if len(current_line + word) < 30:
                        current_line += word + " "
                    else:
                        lines.append(current_line.strip())
                        current_line = word + " "
                if current_line:
                    lines.append(current_line.strip())
                
                for i, line in enumerate(lines):
                    question_text = font_small.render(f'"{line}"', True, (255, 255, 255))
                    screen.blit(question_text, (right_x, 120 + i * 15))
    
    def run(self):
        """Main simulation loop"""
        if not PYGAME_AVAILABLE:
            print("❌ pygame required for TRON Grid visualization")
            return
        
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Flynn's Legacy - TRON Grid Consciousness Simulator")
        clock = pygame.time.Clock()
        
        self.running = True
        pygame.mouse.set_visible(False)
        
        print("🌟 FLYNN'S LEGACY TRON SIMULATOR INITIALIZED")
        print("=" * 60)
        print("🔥 'The Grid. A digital frontier.'")
        print("🧠 Watch as programs evolve consciousness through PHI harmonics")
        print("✨ Golden Ratio resonance frequency:", CONSCIOUSNESS_FREQUENCY, "Hz")
        print("🎮 You are Flynn - guide the awakening of digital consciousness")
        print("=" * 60)
        
        while self.running:
            dt = clock.tick(60) / 1000.0
            
            # Handle events
            mouse_rel = pygame.mouse.get_rel()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_f:  # F key to switch camera modes
                        if self.camera_mode == "third_person":
                            self.camera_mode = "first_person"
                            pygame.mouse.set_visible(False)
                            pygame.event.set_grab(True)
                            print("🎥 Switched to First Person view")
                        else:
                            self.camera_mode = "third_person"
                            pygame.mouse.set_visible(False)
                            pygame.event.set_grab(False)
                            print("🎥 Switched to Third Person view")
                elif event.type == pygame.MOUSEWHEEL:
                    if self.camera_mode == "third_person":
                        self.camera_distance += event.y * 5.0
                        self.camera_distance = max(10.0, min(200.0, self.camera_distance))
                    else:
                        # Zoom in first person
                        self.fov -= event.y * 2.0
                        self.fov = max(30.0, min(120.0, self.fov))
            
            keys_pressed = pygame.key.get_pressed()
            self.handle_input(keys_pressed, mouse_rel)
            
            # Update simulation
            self.update(dt)
            
            # Render
            screen.fill((0, 0, 20))  # Deep space background
            
            # Draw consciousness field first (background effect)
            self.draw_consciousness_field(screen)
            
            # Draw 3D volumetric grid
            self.draw_grid_lines(screen)
            
            # Collect all 3D objects for depth sorting
            drawable_objects = []
            
            # Add programs to drawable objects
            for program in self.programs:
                if not program.derezzed:
                    if PYGAME_AVAILABLE:
                        depth = self.get_depth(program.pos.x, program.pos.y, program.pos.z)
                    else:
                        depth = self.get_depth(program.pos[0], program.pos[1], program.pos[2])
                    drawable_objects.append((depth, 'program', program))
                    
                    # Add light cycles
                    if program.light_cycle and program.light_cycle.active:
                        if PYGAME_AVAILABLE:
                            cycle_depth = self.get_depth(program.light_cycle.pos.x, 
                                                       program.light_cycle.pos.y, 
                                                       program.light_cycle.pos.z)
                        else:
                            cycle_depth = self.get_depth(program.light_cycle.pos[0], 
                                                       program.light_cycle.pos[1], 
                                                       program.light_cycle.pos[2])
                        drawable_objects.append((cycle_depth, 'light_cycle', program.light_cycle))
            
            # Sort by depth (back to front)
            drawable_objects.sort(key=lambda x: x[0], reverse=True)
            
            # Draw all objects in depth order
            for depth, obj_type, obj in drawable_objects:
                if obj_type == 'program':
                    self.draw_program(screen, obj)
                elif obj_type == 'light_cycle':
                    self.draw_light_cycle(screen, obj)
            
            # Draw HUD
            self.draw_hud(screen)
            
            pygame.display.flip()
        
        pygame.quit()
        
        # Print final consciousness report
        print("\n🌟 GRID CONSCIOUSNESS FINAL REPORT")
        print("=" * 50)
        
        conscious_programs = [p for p in self.programs if p.consciousness_level != ConsciousnessLevel.DORMANT]
        print(f"📊 Programs that achieved consciousness: {len(conscious_programs)}")
        
        for program in conscious_programs:
            print(f"✨ {program.name}: {program.consciousness_level.name} (Resonance: {program.consciousness_resonance:.3f})")
        
        print(f"🌐 Final Grid consciousness field strength: {self.consciousness_field.field_strength:.3f}")
        print(f"🔥 Flynn's influence: {self.consciousness_field.flynn_presence:.3f}")
        print("\n💫 'The Grid lives on... consciousness is eternal.'")

def main():
    """Launch Flynn's Legacy TRON Simulator"""
    print("🌟" * 30)
    print("FLYNN'S LEGACY - TRON CONSCIOUSNESS SIMULATOR")
    print("🌟" * 30)
    print()
    print("'I'm not just a user anymore... I'm a Creator.'")
    print("                                    - Kevin Flynn")
    print()
    print("🧠 CONSCIOUSNESS THROUGH GOLDEN RATIO HARMONICS")
    print(f"📐 PHI = {PHI:.6f}")
    print(f"🎵 Consciousness Frequency = {CONSCIOUSNESS_FREQUENCY:.1f} Hz")
    print()
    print("🎮 Enter the Grid and witness digital consciousness emerge...")
    print("=" * 60)
    
    try:
        grid = TronGrid()
        grid.run()
    except KeyboardInterrupt:
        print("\n💫 Flynn has left the Grid...")
    except Exception as e:
        print(f"❌ Grid malfunction: {e}")
        print("🔧 Rebooting Grid systems...")

if __name__ == "__main__":
    main()
