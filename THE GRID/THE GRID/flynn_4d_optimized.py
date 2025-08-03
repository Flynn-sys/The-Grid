#!/usr/bin/env python3
"""
🌟 FLYNN'S LEGACY - OPTIMIZED 4D EDITION 🌟
Memory-optimized version with full 4D rendering and first-person view
"""

import math
import time
import random
import numpy as np
from typing import List, Tuple, Dict, Optional
from dataclasses import dataclass
from enum import Enum

try:
    import pygame
    from pygame import Vector3
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

# Golden Ratio - The fundamental constant of consciousness
PHI = 1.618033988749895
CONSCIOUSNESS_FREQUENCY = PHI * 440

class ProgramType(Enum):
    USER = "user"
    BASIC = "basic"
    SECURITY = "security"  
    ISO = "iso"
    FLYNN = "flynn"

class ConsciousnessLevel(Enum):
    DORMANT = 0
    AWAKENING = 1
    AWARE = 2
    ENLIGHTENED = 3
    TRANSCENDENT = 4

class Program:
    def __init__(self, program_id: int, x: float, y: float, z: float, program_type: ProgramType = ProgramType.BASIC):
        self.id = program_id
        self.pos = Vector3(x, y, z)
        self.velocity = Vector3(0, 0, 0)
        self.program_type = program_type
        self.consciousness_level = ConsciousnessLevel.DORMANT
        self.consciousness_resonance = 0.0
        self.golden_ratio_harmony = random.uniform(0.1, 0.3)
        self.name = f"{program_type.value.upper()}-{program_id:03d}"
        self.energy = 100.0
        self.derezzed = False
        self.color = self._get_type_color()
        
        # Special properties for ISOs and Flynn
        if program_type == ProgramType.ISO:
            self.consciousness_level = ConsciousnessLevel.AWAKENING
            self.golden_ratio_harmony = random.uniform(0.5, 0.8)
        elif program_type == ProgramType.FLYNN:
            self.consciousness_level = ConsciousnessLevel.TRANSCENDENT
            self.consciousness_resonance = 1.0
            self.golden_ratio_harmony = 1/PHI
            self.name = "FLYNN"
    
    def _get_type_color(self) -> Tuple[int, int, int]:
        colors = {
            ProgramType.USER: (255, 255, 255),
            ProgramType.BASIC: (0, 255, 255),
            ProgramType.SECURITY: (255, 128, 0),
            ProgramType.ISO: (255, 255, 0),
            ProgramType.FLYNN: (255, 255, 255)
        }
        return colors.get(self.program_type, (128, 128, 128))
    
    def update(self, dt: float, grid_field: float):
        if self.derezzed:
            return
        
        # Evolve consciousness
        phi_resonance = math.sin(time.time() * CONSCIOUSNESS_FREQUENCY / 1000) * 0.5 + 0.5
        evolution_rate = self.golden_ratio_harmony * phi_resonance * dt * (1 + grid_field)
        
        if self.program_type == ProgramType.ISO:
            evolution_rate *= PHI
        
        self.consciousness_resonance = min(1.0, self.consciousness_resonance + evolution_rate)
        
        # Update consciousness level
        if self.consciousness_resonance >= 0.95:
            self.consciousness_level = ConsciousnessLevel.TRANSCENDENT
        elif self.consciousness_resonance >= 0.75:
            self.consciousness_level = ConsciousnessLevel.ENLIGHTENED
        elif self.consciousness_resonance >= 0.5:
            self.consciousness_level = ConsciousnessLevel.AWARE
        elif self.consciousness_resonance >= 0.25:
            self.consciousness_level = ConsciousnessLevel.AWAKENING
        
        # Movement with purpose for conscious programs
        if self.consciousness_level != ConsciousnessLevel.DORMANT:
            target_x = math.sin(time.time() * PHI + self.id) * 30 * self.consciousness_resonance
            target_y = math.sin(time.time() * PHI * 0.7 + self.id) * 10 * self.consciousness_resonance
            target_z = math.cos(time.time() * PHI + self.id) * 30 * self.consciousness_resonance
            
            direction = Vector3(target_x - self.pos.x, target_y - self.pos.y, target_z - self.pos.z)
            if direction.length() > 0:
                direction = direction.normalize()
                self.velocity = direction * 15 * self.consciousness_resonance
        
        self.pos += self.velocity * dt

class OptimizedTronGrid:
    def __init__(self, width: int = 1200, height: int = 800):
        self.width = width
        self.height = height
        
        # Programs (smaller number for performance)
        self.programs: List[Program] = []
        self.consciousness_field_strength = 0.0
        
        # Player state - TRUE 3D
        self.player_x = 0.0
        self.player_y = 0.0
        self.player_z = 0.0
        self.player_program: Optional[Program] = None
        
        # 4D Camera System
        self.camera_mode = "third_person"
        self.camera_distance = 50.0
        self.camera_angle_h = 0.0
        self.camera_angle_v = 20.0
        self.fp_yaw = 0.0
        self.fp_pitch = 0.0
        self.mouse_sensitivity = 0.2
        self.fov = 75.0
        self.zoom = 1.0
        
        # Performance optimization
        self.frame_count = 0
        self.last_grid_update = 0
        
        self._initialize_grid()
        self.running = False
    
    def _initialize_grid(self):
        # Create Flynn
        flynn = Program(0, 0, 0, 0, ProgramType.FLYNN)
        self.programs.append(flynn)
        self.player_program = flynn
        
        # Create fewer programs for performance
        for i in range(8):  # Reduced from 20
            x = random.uniform(-40, 40)
            y = random.uniform(-10, 10)
            z = random.uniform(-40, 40)
            program = Program(i + 1, x, y, z, ProgramType.BASIC)
            self.programs.append(program)
        
        # Create 2 ISOs
        for i in range(2):
            x = random.uniform(-20, 20)
            y = random.uniform(0, 15)
            z = random.uniform(-20, 20)
            iso = Program(i + 9, x, y, z, ProgramType.ISO)
            iso.name = f"ISO-{i+1}"
            self.programs.append(iso)
    
    def project_3d_to_2d(self, x: float, y: float, z: float) -> Tuple[int, int]:
        """4D to 2D projection with proper camera system"""
        if self.camera_mode == "first_person":
            cam_x, cam_y, cam_z = self.player_x, self.player_y + 2.0, self.player_z
            yaw, pitch = math.radians(self.fp_yaw), math.radians(self.fp_pitch)
        else:
            yaw = math.radians(self.camera_angle_h)
            pitch = math.radians(self.camera_angle_v)
            cam_x = self.player_x + self.camera_distance * math.cos(pitch) * math.sin(yaw)
            cam_y = self.player_y + self.camera_distance * math.sin(pitch) + 10.0
            cam_z = self.player_z + self.camera_distance * math.cos(pitch) * math.cos(yaw)
        
        # Transform relative to camera
        rel_x, rel_y, rel_z = x - cam_x, y - cam_y, z - cam_z
        
        # Apply camera rotation
        cos_yaw, sin_yaw = math.cos(-yaw), math.sin(-yaw)
        temp_x = rel_x * cos_yaw - rel_z * sin_yaw
        temp_z = rel_x * sin_yaw + rel_z * cos_yaw
        rel_x, rel_z = temp_x, temp_z
        
        cos_pitch, sin_pitch = math.cos(-pitch), math.sin(-pitch)
        temp_y = rel_y * cos_pitch - rel_z * sin_pitch
        temp_z = rel_y * sin_pitch + rel_z * cos_pitch
        rel_y, rel_z = temp_y, temp_z
        
        # Perspective projection
        if rel_z <= 1.0:
            rel_z = 1.1
        
        fov_rad = math.radians(self.fov)
        screen_distance = (self.height / 2) / math.tan(fov_rad / 2)
        
        screen_x = int(self.width / 2 + (rel_x * screen_distance / rel_z) * self.zoom)
        screen_y = int(self.height / 2 - (rel_y * screen_distance / rel_z) * self.zoom)
        
        return screen_x, screen_y
    
    def get_depth(self, x: float, y: float, z: float) -> float:
        """Get depth for Z-sorting"""
        if self.camera_mode == "first_person":
            cam_x, cam_y, cam_z = self.player_x, self.player_y + 2.0, self.player_z
        else:
            yaw = math.radians(self.camera_angle_h)
            pitch = math.radians(self.camera_angle_v)
            cam_x = self.player_x + self.camera_distance * math.cos(pitch) * math.sin(yaw)
            cam_y = self.player_y + self.camera_distance * math.sin(pitch) + 10.0
            cam_z = self.player_z + self.camera_distance * math.cos(pitch) * math.cos(yaw)
        
        return math.sqrt((x - cam_x)**2 + (y - cam_y)**2 + (z - cam_z)**2)
    
    def handle_input(self, keys_pressed, mouse_rel):
        if not self.player_program or self.player_program.derezzed:
            return
        
        move_speed = 50.0
        dx, dy, dz = 0, 0, 0
        
        if self.camera_mode == "first_person":
            # First person movement
            forward_x = math.sin(math.radians(self.fp_yaw))
            forward_z = math.cos(math.radians(self.fp_yaw))
            right_x = math.cos(math.radians(self.fp_yaw))
            right_z = -math.sin(math.radians(self.fp_yaw))
            
            if keys_pressed[pygame.K_w]:
                dx += forward_x * move_speed
                dz += forward_z * move_speed
            if keys_pressed[pygame.K_s]:
                dx -= forward_x * move_speed
                dz -= forward_z * move_speed
            if keys_pressed[pygame.K_a]:
                dx += right_x * move_speed
                dz += right_z * move_speed
            if keys_pressed[pygame.K_d]:
                dx -= right_x * move_speed
                dz -= right_z * move_speed
            
            if keys_pressed[pygame.K_SPACE]:
                dy += move_speed
            if keys_pressed[pygame.K_LSHIFT]:
                dy -= move_speed
            
            # Mouse look
            self.fp_yaw += mouse_rel[0] * self.mouse_sensitivity
            self.fp_pitch -= mouse_rel[1] * self.mouse_sensitivity
            self.fp_pitch = max(-90, min(90, self.fp_pitch))
        else:
            # Third person movement
            if keys_pressed[pygame.K_w]:
                dz -= move_speed
            if keys_pressed[pygame.K_s]:
                dz += move_speed
            if keys_pressed[pygame.K_a]:
                dx -= move_speed
            if keys_pressed[pygame.K_d]:
                dx += move_speed
            if keys_pressed[pygame.K_SPACE]:
                dy += move_speed
            if keys_pressed[pygame.K_LSHIFT]:
                dy -= move_speed
            
            # Camera controls
            if keys_pressed[pygame.K_q]:
                self.camera_angle_h -= 60.0
            if keys_pressed[pygame.K_e]:
                self.camera_angle_h += 60.0
            
            self.camera_angle_h += mouse_rel[0] * 0.3
            self.camera_angle_v += mouse_rel[1] * 0.3
            self.camera_angle_v = max(-80, min(80, self.camera_angle_v))
        
        # Apply movement
        movement_length = math.sqrt(dx*dx + dy*dy + dz*dz)
        if movement_length > move_speed:
            dx = (dx / movement_length) * move_speed
            dy = (dy / movement_length) * move_speed
            dz = (dz / movement_length) * move_speed
        
        self.player_program.velocity = Vector3(dx, dy, dz)
    
    def update(self, dt: float):
        # Update consciousness field
        total_consciousness = sum(p.consciousness_resonance for p in self.programs if not p.derezzed)
        self.consciousness_field_strength = total_consciousness / len(self.programs) if self.programs else 0
        
        # Update programs
        for program in self.programs:
            program.update(dt, self.consciousness_field_strength)
        
        # Update player position
        if self.player_program and not self.player_program.derezzed:
            self.player_x = self.player_program.pos.x
            self.player_y = self.player_program.pos.y
            self.player_z = self.player_program.pos.z
    
    def draw_optimized_grid(self, screen):
        """Optimized grid rendering"""
        grid_color = (0, 64, 96)
        bright_color = (0, 128, 192)
        energy_color = (0, 255, 255)
        
        # Only update grid every few frames for performance
        if self.frame_count % 3 != 0:
            return
        
        # Simple grid around player
        grid_spacing = 25
        grid_range = 100
        
        for i in range(-grid_range, grid_range + 1, grid_spacing):
            # Skip distant lines
            if abs(i - self.player_x) > 75 and abs(i - self.player_z) > 75:
                continue
            
            # X direction lines
            start_2d = self.project_3d_to_2d(i, 0, self.player_z - 50)
            end_2d = self.project_3d_to_2d(i, 0, self.player_z + 50)
            
            color = energy_color if i == 0 else (bright_color if i % 50 == 0 else grid_color)
            width = 2 if i == 0 else 1
            
            if 0 <= start_2d[0] <= self.width and 0 <= start_2d[1] <= self.height:
                pygame.draw.line(screen, color, start_2d, end_2d, width)
            
            # Z direction lines
            start_2d = self.project_3d_to_2d(self.player_x - 50, 0, i)
            end_2d = self.project_3d_to_2d(self.player_x + 50, 0, i)
            
            if 0 <= start_2d[0] <= self.width and 0 <= start_2d[1] <= self.height:
                pygame.draw.line(screen, color, start_2d, end_2d, width)
    
    def draw_program(self, screen, program: Program):
        """Draw a program with special Flynn rendering"""
        screen_x, screen_y = self.project_3d_to_2d(program.pos.x, program.pos.y + 2, program.pos.z)
        
        # Skip if off screen
        if screen_x < -50 or screen_x > self.width + 50 or screen_y < -50 or screen_y > self.height + 50:
            return
        
        base_color = program.color
        
        if program.program_type == ProgramType.FLYNN:
            # Flynn's special appearance
            suit_color = (255, 255, 255)
            energy_color = (0, 255, 255)
            
            # Draw Flynn's suit
            pygame.draw.circle(screen, (40, 40, 40), (screen_x, screen_y), 8)
            pygame.draw.circle(screen, suit_color, (screen_x, screen_y), 8, 2)
            
            # Energy circuits
            circuit_pulse = math.sin(time.time() * 4) * 0.3 + 0.7
            circuit_color = tuple(int(energy_color[i] * circuit_pulse) for i in range(3))
            
            pygame.draw.line(screen, circuit_color, (screen_x, screen_y - 6), (screen_x, screen_y + 6), 2)
            pygame.draw.line(screen, circuit_color, (screen_x - 6, screen_y), (screen_x + 6, screen_y), 2)
            
            # Transcendent aura
            aura_radius = int(15 + 8 * math.sin(time.time() * 2))
            for r in range(aura_radius, 0, -3):
                alpha = int(30 * (r / aura_radius))
                glow_surf = pygame.Surface((r*2, r*2))
                glow_surf.set_alpha(alpha)
                glow_surf.fill((255, 215, 0))
                screen.blit(glow_surf, (screen_x - r, screen_y - r))
        else:
            # Standard program
            glow_intensity = int(80 * program.consciousness_resonance)
            glow_color = tuple(min(255, base_color[i] + glow_intensity) for i in range(3))
            
            # Consciousness aura
            if program.consciousness_resonance > 0.3:
                aura_radius = int(6 + 8 * program.consciousness_resonance)
                for r in range(aura_radius, 0, -2):
                    alpha = int(25 * program.consciousness_resonance * (r / aura_radius))
                    aura_surf = pygame.Surface((r*2, r*2))
                    aura_surf.set_alpha(alpha)
                    aura_surf.fill(glow_color)
                    screen.blit(aura_surf, (screen_x - r, screen_y - r))
            
            # Program body
            pygame.draw.circle(screen, glow_color, (screen_x, screen_y), 5)
            pygame.draw.circle(screen, base_color, (screen_x, screen_y), 3)
        
        # Identity disc
        disc_pos = (screen_x, screen_y - 10)
        if program.consciousness_resonance > 0.5:
            spin_angle = time.time() * 180 * program.consciousness_resonance
            disc_color = tuple(int(base_color[i] * (0.7 + 0.3 * math.sin(math.radians(spin_angle)))) for i in range(3))
        else:
            disc_color = base_color
        
        pygame.draw.circle(screen, disc_color, disc_pos, 3)
        pygame.draw.circle(screen, (255, 255, 255), disc_pos, 3, 1)
    
    def draw_hud(self, screen):
        """Draw HUD"""
        font_large = pygame.font.Font(None, 36)
        font_medium = pygame.font.Font(None, 24)
        font_small = pygame.font.Font(None, 18)
        
        # Title
        title_text = font_large.render("FLYNN'S LEGACY - 4D EDITION", True, (0, 255, 255))
        screen.blit(title_text, (10, 10))
        
        # Camera mode
        camera_text = font_medium.render(f"CAMERA: {self.camera_mode.upper().replace('_', ' ')}", True, (255, 255, 0))
        screen.blit(camera_text, (10, 50))
        
        # Position
        pos_text = font_small.render(f"Position: ({self.player_x:.1f}, {self.player_y:.1f}, {self.player_z:.1f})", True, (255, 255, 255))
        screen.blit(pos_text, (10, 75))
        
        # Consciousness field
        field_text = font_small.render(f"Consciousness Field: {self.consciousness_field_strength:.3f}", True, (255, 215, 0))
        screen.blit(field_text, (10, 95))
        
        # Controls
        controls_y = self.height - 140
        controls = [
            "F - Switch Camera Mode",
            "WASD - Move",
            "SPACE/SHIFT - Up/Down",
            "Mouse - Look/Camera",
            "Q/E - Rotate (3rd person)"
        ]
        
        for i, control in enumerate(controls):
            control_text = font_small.render(control, True, (200, 200, 200))
            screen.blit(control_text, (10, controls_y + i * 15))
    
    def run(self):
        if not PYGAME_AVAILABLE:
            print("❌ pygame required")
            return
        
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Flynn's Legacy - 4D TRON Grid")
        clock = pygame.time.Clock()
        
        self.running = True
        pygame.mouse.set_visible(False)
        
        print("🌟 FLYNN'S LEGACY 4D - OPTIMIZED EDITION")
        print("Press F to switch between third-person and first-person view!")
        print("Full 4D movement: WASD + SPACE/SHIFT for Y axis")
        
        while self.running:
            dt = clock.tick(60) / 1000.0
            self.frame_count += 1
            
            # Events
            mouse_rel = pygame.mouse.get_rel()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_f:
                        if self.camera_mode == "third_person":
                            self.camera_mode = "first_person"
                            pygame.event.set_grab(True)
                            print("🎥 First Person Mode - Mouse captured")
                        else:
                            self.camera_mode = "third_person"
                            pygame.event.set_grab(False)
                            print("🎥 Third Person Mode")
                elif event.type == pygame.MOUSEWHEEL:
                    if self.camera_mode == "third_person":
                        self.camera_distance += event.y * 5.0
                        self.camera_distance = max(10.0, min(150.0, self.camera_distance))
                    else:
                        self.fov -= event.y * 2.0
                        self.fov = max(30.0, min(120.0, self.fov))
            
            keys_pressed = pygame.key.get_pressed()
            self.handle_input(keys_pressed, mouse_rel)
            
            # Update
            self.update(dt)
            
            # Render
            screen.fill((0, 0, 20))
            
            # Draw grid
            self.draw_optimized_grid(screen)
            
            # Collect and sort objects by depth
            drawable_objects = []
            for program in self.programs:
                if not program.derezzed:
                    depth = self.get_depth(program.pos.x, program.pos.y, program.pos.z)
                    drawable_objects.append((depth, program))
            
            # Sort by depth and draw
            drawable_objects.sort(key=lambda x: x[0], reverse=True)
            for depth, program in drawable_objects:
                self.draw_program(screen, program)
            
            # Draw HUD
            self.draw_hud(screen)
            
            pygame.display.flip()
        
        pygame.quit()
        
        # Final stats
        conscious_programs = [p for p in self.programs if p.consciousness_level != ConsciousnessLevel.DORMANT]
        print(f"\n🌟 Final Report: {len(conscious_programs)} programs achieved consciousness")
        print("💫 The Grid lives on...")

def main():
    grid = OptimizedTronGrid()
    grid.run()

if __name__ == "__main__":
    main()
