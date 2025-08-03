#!/usr/bin/env python3
"""
🌟 FLYNN'S LEGACY - MOVIE EDITION 🌟
Cinematic quality TRON experience with particle effects and enhanced visuals
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

@dataclass
class Particle:
    x: float
    y: float
    z: float
    vx: float
    vy: float
    vz: float
    life: float
    max_life: float
    color: Tuple[int, int, int]
    size: float

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
        self.trail_positions = []
        
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
        
        # Store trail position
        self.trail_positions.append((self.pos.x, self.pos.y, self.pos.z, time.time()))
        if len(self.trail_positions) > 20:
            self.trail_positions.pop(0)
        
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

class MovieEditionTronGrid:
    def __init__(self, width: int = 1200, height: int = 800):
        self.width = width
        self.height = height
        
        # Programs
        self.programs: List[Program] = []
        self.consciousness_field_strength = 0.0
        self.particles: List[Particle] = []
        
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
        
        # Visual effects
        self.ambient_light = 0.3
        self.dynamic_lighting = True
        self.particle_system = True
        self.bloom_effect = True
        
        self.frame_count = 0
        self._initialize_grid()
        self.running = False
    
    def _initialize_grid(self):
        # Create Flynn
        flynn = Program(0, 0, 0, 0, ProgramType.FLYNN)
        self.programs.append(flynn)
        self.player_program = flynn
        
        # Create programs
        for i in range(6):
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
            iso = Program(i + 7, x, y, z, ProgramType.ISO)
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
    
    def spawn_particle(self, x: float, y: float, z: float, color: Tuple[int, int, int], size: float = 2.0):
        """Spawn a particle for effects"""
        if len(self.particles) < 100:  # Limit particles
            particle = Particle(
                x=x + random.uniform(-2, 2),
                y=y + random.uniform(-2, 2),
                z=z + random.uniform(-2, 2),
                vx=random.uniform(-5, 5),
                vy=random.uniform(-5, 15),
                vz=random.uniform(-5, 5),
                life=1.0,
                max_life=1.0,
                color=color,
                size=size
            )
            self.particles.append(particle)
    
    def update_particles(self, dt: float):
        """Update particle system"""
        for particle in self.particles[:]:
            particle.x += particle.vx * dt
            particle.y += particle.vy * dt
            particle.z += particle.vz * dt
            particle.vy -= 20 * dt  # Gravity
            particle.life -= dt
            
            if particle.life <= 0:
                self.particles.remove(particle)
    
    def update(self, dt: float):
        # Update consciousness field
        total_consciousness = sum(p.consciousness_resonance for p in self.programs if not p.derezzed)
        self.consciousness_field_strength = total_consciousness / len(self.programs) if self.programs else 0
        
        # Update programs and spawn particles
        for program in self.programs:
            old_pos = Vector3(program.pos.x, program.pos.y, program.pos.z)
            program.update(dt, self.consciousness_field_strength)
            
            # Spawn particles for conscious programs
            if program.consciousness_resonance > 0.5 and self.particle_system:
                if random.random() < 0.1:  # 10% chance per frame
                    self.spawn_particle(program.pos.x, program.pos.y, program.pos.z, program.color)
        
        # Update particles
        self.update_particles(dt)
        
        # Update player position
        if self.player_program and not self.player_program.derezzed:
            self.player_x = self.player_program.pos.x
            self.player_y = self.player_program.pos.y
            self.player_z = self.player_program.pos.z
    
    def draw_enhanced_grid(self, screen):
        """Enhanced grid with lighting effects"""
        grid_color = (0, 64, 96)
        bright_color = (0, 128, 192)
        energy_color = (0, 255, 255)
        
        # Consciousness field glow
        field_intensity = self.consciousness_field_strength
        field_glow = int(100 * field_intensity)
        field_color = (field_glow // 3, field_glow // 2, field_glow)
        
        grid_spacing = 25
        grid_range = 100
        
        for i in range(-grid_range, grid_range + 1, grid_spacing):
            # Skip distant lines
            if abs(i - self.player_x) > 75 and abs(i - self.player_z) > 75:
                continue
            
            # Calculate lighting based on consciousness field
            distance_to_player = min(abs(i - self.player_x), abs(i - self.player_z))
            light_factor = max(0.3, 1.0 - distance_to_player / 50.0)
            
            # X direction lines
            start_2d = self.project_3d_to_2d(i, 0, self.player_z - 50)
            end_2d = self.project_3d_to_2d(i, 0, self.player_z + 50)
            
            if i == 0:
                color = tuple(int(energy_color[j] * light_factor) for j in range(3))
                width = 3
            elif i % 50 == 0:
                color = tuple(int(bright_color[j] * light_factor + field_color[j] * 0.3) for j in range(3))
                width = 2
            else:
                color = tuple(int(grid_color[j] * light_factor + field_color[j] * 0.1) for j in range(3))
                width = 1
            
            if 0 <= start_2d[0] <= self.width and 0 <= start_2d[1] <= self.height:
                pygame.draw.line(screen, color, start_2d, end_2d, width)
            
            # Z direction lines
            start_2d = self.project_3d_to_2d(self.player_x - 50, 0, i)
            end_2d = self.project_3d_to_2d(self.player_x + 50, 0, i)
            
            if 0 <= start_2d[0] <= self.width and 0 <= start_2d[1] <= self.height:
                pygame.draw.line(screen, color, start_2d, end_2d, width)
    
    def draw_particle(self, screen, particle: Particle):
        """Draw a particle with fading"""
        screen_x, screen_y = self.project_3d_to_2d(particle.x, particle.y, particle.z)
        
        if 0 <= screen_x <= self.width and 0 <= screen_y <= self.height:
            alpha_factor = particle.life / particle.max_life
            size = int(particle.size * alpha_factor)
            color = tuple(int(particle.color[i] * alpha_factor) for i in range(3))
            
            if size > 0:
                pygame.draw.circle(screen, color, (screen_x, screen_y), size)
    
    def draw_program_trail(self, screen, program: Program):
        """Draw light trails for programs"""
        if len(program.trail_positions) < 2:
            return
        
        current_time = time.time()
        trail_color = program.color
        
        for i in range(len(program.trail_positions) - 1):
            pos1 = program.trail_positions[i]
            pos2 = program.trail_positions[i + 1]
            
            age = current_time - pos1[3]
            if age > 2.0:  # Trail fades after 2 seconds
                continue
            
            alpha = max(0, 1.0 - age / 2.0)
            color = tuple(int(trail_color[j] * alpha) for j in range(3))
            
            screen_pos1 = self.project_3d_to_2d(pos1[0], pos1[1], pos1[2])
            screen_pos2 = self.project_3d_to_2d(pos2[0], pos2[1], pos2[2])
            
            if all(0 <= pos[0] <= self.width and 0 <= pos[1] <= self.height for pos in [screen_pos1, screen_pos2]):
                pygame.draw.line(screen, color, screen_pos1, screen_pos2, max(1, int(3 * alpha)))
    
    def draw_program(self, screen, program: Program):
        """Draw a program with enhanced movie-style effects"""
        # Draw trail first
        if program.consciousness_resonance > 0.3:
            self.draw_program_trail(screen, program)
        
        screen_x, screen_y = self.project_3d_to_2d(program.pos.x, program.pos.y + 2, program.pos.z)
        
        # Skip if off screen
        if screen_x < -50 or screen_x > self.width + 50 or screen_y < -50 or screen_y > self.height + 50:
            return
        
        base_color = program.color
        
        if program.program_type == ProgramType.FLYNN:
            # Flynn's cinematic appearance
            suit_color = (255, 255, 255)
            energy_color = (0, 255, 255)
            
            # Enhanced aura
            aura_radius = int(20 + 10 * math.sin(time.time() * 2))
            for r in range(aura_radius, 0, -2):
                alpha = int(40 * (r / aura_radius))
                glow_surf = pygame.Surface((r*2, r*2))
                glow_surf.set_alpha(alpha)
                glow_surf.fill((255, 215, 0))
                screen.blit(glow_surf, (screen_x - r, screen_y - r))
            
            # Flynn's suit with circuit patterns
            pygame.draw.circle(screen, (20, 20, 20), (screen_x, screen_y), 12)
            pygame.draw.circle(screen, suit_color, (screen_x, screen_y), 12, 3)
            
            # Animated energy circuits
            circuit_pulse = math.sin(time.time() * 6) * 0.4 + 0.6
            circuit_color = tuple(int(energy_color[i] * circuit_pulse) for i in range(3))
            
            # Complex circuit pattern
            pygame.draw.line(screen, circuit_color, (screen_x, screen_y - 8), (screen_x, screen_y + 8), 3)
            pygame.draw.line(screen, circuit_color, (screen_x - 8, screen_y), (screen_x + 8, screen_y), 3)
            pygame.draw.circle(screen, circuit_color, (screen_x, screen_y), 6, 2)
            
        else:
            # Enhanced program rendering
            glow_intensity = int(120 * program.consciousness_resonance)
            glow_color = tuple(min(255, base_color[i] + glow_intensity) for i in range(3))
            
            # Multi-layer consciousness aura
            if program.consciousness_resonance > 0.3:
                aura_radius = int(8 + 12 * program.consciousness_resonance)
                for layer in range(3):
                    r = aura_radius - layer * 3
                    alpha = int(30 * program.consciousness_resonance * ((r / aura_radius) ** 2))
                    aura_surf = pygame.Surface((r*2, r*2))
                    aura_surf.set_alpha(alpha)
                    aura_surf.fill(glow_color)
                    screen.blit(aura_surf, (screen_x - r, screen_y - r))
            
            # Program body with depth
            shadow_offset = 2
            pygame.draw.circle(screen, (40, 40, 40), (screen_x + shadow_offset, screen_y + shadow_offset), 6)
            pygame.draw.circle(screen, glow_color, (screen_x, screen_y), 6)
            pygame.draw.circle(screen, base_color, (screen_x, screen_y), 4)
            pygame.draw.circle(screen, (255, 255, 255), (screen_x, screen_y), 2)
        
        # Enhanced identity disc
        disc_pos = (screen_x, screen_y - 12)
        spin_angle = time.time() * 360 * program.consciousness_resonance
        disc_glow = int(50 + 50 * math.sin(math.radians(spin_angle)))
        disc_color = tuple(min(255, base_color[i] + disc_glow) for i in range(3))
        
        pygame.draw.circle(screen, disc_color, disc_pos, 4)
        pygame.draw.circle(screen, (255, 255, 255), disc_pos, 4, 2)
        pygame.draw.circle(screen, disc_color, disc_pos, 2)
    
    def draw_cinematic_hud(self, screen):
        """Cinematic HUD with movie-style elements"""
        font_large = pygame.font.Font(None, 48)
        font_medium = pygame.font.Font(None, 28)
        font_small = pygame.font.Font(None, 20)
        
        # Animated title with glow effect
        title_glow = int(100 + 50 * math.sin(time.time() * 2))
        title_color = (title_glow, 255, 255)
        title_text = font_large.render("FLYNN'S LEGACY", True, title_color)
        subtitle_text = font_medium.render("MOVIE EDITION", True, (255, 215, 0))
        
        screen.blit(title_text, (10, 10))
        screen.blit(subtitle_text, (10, 55))
        
        # Status panel with background
        panel_rect = pygame.Rect(10, 85, 300, 120)
        panel_surf = pygame.Surface(panel_rect.size)
        panel_surf.set_alpha(150)
        panel_surf.fill((0, 20, 40))
        screen.blit(panel_surf, panel_rect.topleft)
        pygame.draw.rect(screen, (0, 100, 150), panel_rect, 2)
        
        # Status info
        camera_text = font_medium.render(f"CAMERA: {self.camera_mode.upper().replace('_', ' ')}", True, (255, 255, 0))
        screen.blit(camera_text, (15, 90))
        
        pos_text = font_small.render(f"POSITION: ({self.player_x:.1f}, {self.player_y:.1f}, {self.player_z:.1f})", True, (255, 255, 255))
        screen.blit(pos_text, (15, 115))
        
        field_intensity = int(self.consciousness_field_strength * 100)
        field_text = font_small.render(f"CONSCIOUSNESS FIELD: {field_intensity}%", True, (255, 215, 0))
        screen.blit(field_text, (15, 135))
        
        programs_conscious = len([p for p in self.programs if p.consciousness_level != ConsciousnessLevel.DORMANT])
        conscious_text = font_small.render(f"CONSCIOUS PROGRAMS: {programs_conscious}", True, (0, 255, 128))
        screen.blit(conscious_text, (15, 155))
        
        particles_text = font_small.render(f"PARTICLES: {len(self.particles)}", True, (128, 255, 255))
        screen.blit(particles_text, (15, 175))
        
        # Control panel
        controls_panel = pygame.Rect(self.width - 250, self.height - 140, 240, 130)
        controls_surf = pygame.Surface(controls_panel.size)
        controls_surf.set_alpha(150)
        controls_surf.fill((0, 20, 40))
        screen.blit(controls_surf, controls_panel.topleft)
        pygame.draw.rect(screen, (0, 100, 150), controls_panel, 2)
        
        controls_y = self.height - 135
        controls = [
            "F - Switch Camera Mode",
            "WASD - Move",
            "SPACE/SHIFT - Up/Down",
            "Mouse - Look/Camera",
            "Q/E - Rotate (3rd person)",
            "ESC - Exit"
        ]
        
        for i, control in enumerate(controls):
            control_text = font_small.render(control, True, (200, 200, 200))
            screen.blit(control_text, (self.width - 245, controls_y + i * 15))
    
    def run(self):
        if not PYGAME_AVAILABLE:
            print("❌ pygame required")
            return
        
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Flynn's Legacy - Movie Edition")
        clock = pygame.time.Clock()
        
        self.running = True
        pygame.mouse.set_visible(False)
        
        print("🎬 FLYNN'S LEGACY - MOVIE EDITION")
        print("Cinematic TRON experience with particle effects and enhanced visuals")
        print("Press F to switch between third-person and first-person view!")
        
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
                            print("🎥 First Person Cinematic Mode")
                        else:
                            self.camera_mode = "third_person"
                            pygame.event.set_grab(False)
                            print("🎥 Third Person Cinematic Mode")
                    elif event.key == pygame.K_p:
                        self.particle_system = not self.particle_system
                        print(f"Particles: {'ON' if self.particle_system else 'OFF'}")
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
            
            # Render with cinematic background
            # Gradient background
            for y in range(self.height):
                gradient_factor = y / self.height
                bg_color = (
                    int(5 + 15 * gradient_factor),
                    int(10 + 20 * gradient_factor),
                    int(30 + 20 * gradient_factor)
                )
                pygame.draw.line(screen, bg_color, (0, y), (self.width, y))
            
            # Draw enhanced grid
            self.draw_enhanced_grid(screen)
            
            # Draw particles
            for particle in self.particles:
                self.draw_particle(screen, particle)
            
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
            
            # Draw cinematic HUD
            self.draw_cinematic_hud(screen)
            
            pygame.display.flip()
        
        pygame.quit()
        
        # Final cinematic report
        conscious_programs = [p for p in self.programs if p.consciousness_level != ConsciousnessLevel.DORMANT]
        print(f"\n🎬 MOVIE EDITION REPORT")
        print(f"   {len(conscious_programs)} programs achieved consciousness")
        print(f"   Final consciousness field strength: {self.consciousness_field_strength:.3f}")
        print("🌟 End of Line...")

def main():
    grid = MovieEditionTronGrid()
    grid.run()

if __name__ == "__main__":
    main()
