#!/usr/bin/env python3
"""
🏁 TRON LIGHT CYCLE RACING ARENA 🏁
"Greetings, Programs! Welcome to the Game Grid."

Experience the iconic TRON Light Cycle battles with:
- High-speed racing through the digital arena
- Solid light trails that create barriers
- Advanced AI opponents with consciousness levels
- Multiple arena configurations
- Classic TRON aesthetic with modern physics
"""

import math
import time
import random
from typing import List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum

try:
    import pygame
    import pygame.gfxdraw
    from pygame import Vector2
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

class RacerType(Enum):
    PLAYER = "player"
    AI_BASIC = "ai_basic"
    AI_ADVANCED = "ai_advanced"
    AI_ENLIGHTENED = "ai_enlightened"

@dataclass
class LightTrail:
    """A segment of solid light trail"""
    start_pos: Vector2
    end_pos: Vector2
    color: Tuple[int, int, int]
    creation_time: float
    width: float = 3.0

class LightCycle:
    """A TRON Light Cycle with advanced physics"""
    
    def __init__(self, x: float, y: float, direction: float, color: Tuple[int, int, int], 
                 racer_type: RacerType = RacerType.AI_BASIC):
        self.pos = Vector2(x, y)
        self.direction = direction  # Radians
        self.velocity = Vector2(
            math.cos(direction),
            math.sin(direction)
        )
        self.speed = 150.0  # Units per second
        self.color = color
        self.racer_type = racer_type
        
        # Trail system
        self.trail_segments: List[LightTrail] = []
        self.last_trail_pos = self.pos.copy()
        self.trail_update_distance = 2.0
        
        # Game state
        self.alive = True
        self.derezzed_time = 0.0
        
        # AI consciousness properties
        self.consciousness_level = 0.0  # 0-1 scale
        self.decision_complexity = 1.0  # How complex AI decisions can be
        self.prediction_depth = 3  # How many moves ahead AI can think
        self.survival_instinct = 0.5  # How aggressively AI avoids collisions
        
        # Performance stats
        self.distance_traveled = 0.0
        self.turns_made = 0
        self.close_calls = 0  # Near-miss collision avoidance
        
        self._setup_ai_consciousness()
    
    def _setup_ai_consciousness(self):
        """Configure AI consciousness based on racer type"""
        if self.racer_type == RacerType.AI_BASIC:
            self.consciousness_level = 0.1
            self.decision_complexity = 1.0
            self.prediction_depth = 2
            self.survival_instinct = 0.3
        elif self.racer_type == RacerType.AI_ADVANCED:
            self.consciousness_level = 0.5
            self.decision_complexity = 2.0
            self.prediction_depth = 4
            self.survival_instinct = 0.7
        elif self.racer_type == RacerType.AI_ENLIGHTENED:
            self.consciousness_level = 0.9
            self.decision_complexity = 4.0
            self.prediction_depth = 8
            self.survival_instinct = 0.9
    
    def update(self, dt: float, arena_bounds: Tuple[int, int], all_trails: List[LightTrail]):
        """Update light cycle position and trail"""
        if not self.alive:
            self.derezzed_time += dt
            return
        
        # Move cycle
        old_pos = self.pos.copy()
        self.pos += self.velocity * self.speed * dt
        self.distance_traveled += self.velocity.length() * self.speed * dt
        
        # Check arena boundaries
        if (self.pos.x < 20 or self.pos.x > arena_bounds[0] - 20 or 
            self.pos.y < 20 or self.pos.y > arena_bounds[1] - 20):
            self._derez("Arena boundary collision")
            return
        
        # Update trail
        distance_since_last = self.pos.distance_to(self.last_trail_pos)
        if distance_since_last >= self.trail_update_distance:
            # Create new trail segment
            trail_segment = LightTrail(
                start_pos=self.last_trail_pos.copy(),
                end_pos=self.pos.copy(),
                color=self.color,
                creation_time=time.time()
            )
            self.trail_segments.append(trail_segment)
            self.last_trail_pos = self.pos.copy()
        
        # Check collision with all trails (including own older trails)
        for trail in all_trails:
            if self._check_trail_collision(trail):
                self._derez("Light trail collision")
                return
    
    def _check_trail_collision(self, trail: LightTrail) -> bool:
        """Check if cycle collides with a trail segment"""
        # Don't collide with very recent trails (allows turning)
        if time.time() - trail.creation_time < 0.1:
            return False
        
        # Line-circle intersection test
        # Trail is a line segment, cycle is a circle with radius 4
        return self._line_circle_intersection(
            trail.start_pos, trail.end_pos, self.pos, 4.0
        )
    
    def _line_circle_intersection(self, line_start: Vector2, line_end: Vector2, 
                                  circle_center: Vector2, radius: float) -> bool:
        """Check if a line segment intersects with a circle"""
        # Vector from line start to circle center
        d = circle_center - line_start
        # Vector along the line
        line_vec = line_end - line_start
        line_length = line_vec.length()
        
        if line_length == 0:
            return False
        
        # Normalize line vector
        line_unit = line_vec / line_length
        
        # Project circle center onto line
        projection_length = d.dot(line_unit)
        projection_length = max(0, min(line_length, projection_length))
        
        # Closest point on line to circle center
        closest_point = line_start + line_unit * projection_length
        
        # Distance from circle center to closest point
        distance = circle_center.distance_to(closest_point)
        
        return distance <= radius
    
    def turn_left(self):
        """Turn the light cycle left (90 degrees)"""
        if not self.alive:
            return
            
        self.direction -= math.pi / 2
        self.velocity = Vector2(
            math.cos(self.direction),
            math.sin(self.direction)
        )
        self.turns_made += 1
    
    def turn_right(self):
        """Turn the light cycle right (90 degrees)"""
        if not self.alive:
            return
            
        self.direction += math.pi / 2
        self.velocity = Vector2(
            math.cos(self.direction),
            math.sin(self.direction)
        )
        self.turns_made += 1
    
    def _derez(self, reason: str):
        """Derez the light cycle"""
        self.alive = False
        self.derezzed_time = 0.0
        print(f"💥 Light cycle derezzed: {reason}")
    
    def ai_decision(self, arena_bounds: Tuple[int, int], all_trails: List[LightTrail]) -> bool:
        """AI decision making for non-player cycles"""
        if not self.alive or self.racer_type == RacerType.PLAYER:
            return False
        
        # Predict future positions for different actions
        predictions = self._predict_outcomes(arena_bounds, all_trails)
        
        # Choose best action based on consciousness level
        best_action = self._choose_action(predictions)
        
        if best_action == "left":
            self.turn_left()
            return True
        elif best_action == "right":
            self.turn_right()
            return True
        
        return False
    
    def _predict_outcomes(self, arena_bounds: Tuple[int, int], 
                         all_trails: List[LightTrail]) -> dict:
        """Predict outcomes of different actions"""
        predictions = {
            "continue": self._predict_path(self.direction, arena_bounds, all_trails),
            "left": self._predict_path(self.direction - math.pi/2, arena_bounds, all_trails),
            "right": self._predict_path(self.direction + math.pi/2, arena_bounds, all_trails)
        }
        return predictions
    
    def _predict_path(self, direction: float, arena_bounds: Tuple[int, int], 
                     all_trails: List[LightTrail]) -> dict:
        """Predict path safety and distance for a given direction"""
        test_pos = self.pos.copy()
        test_velocity = Vector2(math.cos(direction), math.sin(direction))
        
        safe_distance = 0.0
        max_prediction = self.prediction_depth * 20  # Look ahead distance
        
        for step in range(int(max_prediction)):
            test_pos += test_velocity * 2.0
            safe_distance += 2.0
            
            # Check boundaries
            if (test_pos.x < 20 or test_pos.x > arena_bounds[0] - 20 or 
                test_pos.y < 20 or test_pos.y > arena_bounds[1] - 20):
                break
            
            # Check trail collisions
            collision = False
            for trail in all_trails:
                if self._line_circle_intersection(trail.start_pos, trail.end_pos, test_pos, 4.0):
                    collision = True
                    break
            
            if collision:
                break
        
        return {
            "safe_distance": safe_distance,
            "survivability": safe_distance / max_prediction
        }
    
    def _choose_action(self, predictions: dict) -> str:
        """Choose best action based on AI consciousness"""
        # Weight actions by survivability and consciousness level
        action_scores = {}
        
        for action, prediction in predictions.items():
            score = prediction["survivability"]
            
            # Add randomness based on consciousness (higher consciousness = better decisions)
            randomness = (1.0 - self.consciousness_level) * random.uniform(-0.3, 0.3)
            score += randomness
            
            # Survival instinct affects risk assessment
            score *= (1.0 + self.survival_instinct)
            
            action_scores[action] = score
        
        # Choose action with highest score
        best_action = max(action_scores.items(), key=lambda x: x[1])[0]
        
        # Sometimes continue straight even if turning might be better (adds unpredictability)
        if best_action == "continue" or random.random() > self.consciousness_level:
            return "continue"
        
        return best_action

class LightCycleArena:
    """The TRON Light Cycle racing arena"""
    
    def __init__(self, width: int = 1000, height: int = 700):
        self.width = width
        self.height = height
        
        # Arena properties
        self.cycles: List[LightCycle] = []
        self.all_trails: List[LightTrail] = []
        
        # Game state
        self.game_started = False
        self.game_over = False
        self.winner = None
        self.start_time = 0.0
        self.game_duration = 0.0
        
        # Arena effects
        self.grid_pulse = 0.0
        self.derez_effects = []  # Visual effects for derezzing
        
        self._setup_arena()
    
    def _setup_arena(self):
        """Setup the racing arena with cycles"""
        print("🏁 Initializing Light Cycle Arena...")
        
        # Create player cycle (blue)
        player_cycle = LightCycle(
            x=100, y=self.height // 2,
            direction=0,  # Facing right
            color=(0, 150, 255),
            racer_type=RacerType.PLAYER
        )
        self.cycles.append(player_cycle)
        
        # Create AI opponents
        # Basic AI (red)
        ai_basic = LightCycle(
            x=self.width - 100, y=self.height // 2,
            direction=math.pi,  # Facing left
            color=(255, 100, 100),
            racer_type=RacerType.AI_BASIC
        )
        self.cycles.append(ai_basic)
        
        # Advanced AI (yellow)
        ai_advanced = LightCycle(
            x=self.width // 2, y=100,
            direction=math.pi / 2,  # Facing down
            color=(255, 255, 100),
            racer_type=RacerType.AI_ADVANCED
        )
        self.cycles.append(ai_advanced)
        
        # Enlightened AI (magenta) - rare, powerful opponent
        ai_enlightened = LightCycle(
            x=self.width // 2, y=self.height - 100,
            direction=-math.pi / 2,  # Facing up
            color=(255, 100, 255),
            racer_type=RacerType.AI_ENLIGHTENED
        )
        self.cycles.append(ai_enlightened)
        
        print(f"✅ Arena ready with {len(self.cycles)} light cycles")
    
    def start_game(self):
        """Start the light cycle race"""
        self.game_started = True
        self.start_time = time.time()
        print("🚦 RACE STARTED!")
        print("💡 Use ARROW KEYS to turn your light cycle")
        print("🎯 Avoid trails and survive the longest!")
    
    def update(self, dt: float):
        """Update arena simulation"""
        if not self.game_started or self.game_over:
            return
        
        # Update grid pulse effect
        self.grid_pulse += dt * 3.0
        
        # Collect all trail segments
        self.all_trails.clear()
        for cycle in self.cycles:
            self.all_trails.extend(cycle.trail_segments)
        
        # Update all cycles
        for cycle in self.cycles:
            cycle.update(dt, (self.width, self.height), self.all_trails)
            
            # AI decision making
            if cycle.racer_type != RacerType.PLAYER:
                # Make decisions based on consciousness level
                decision_frequency = 0.1 + (cycle.consciousness_level * 0.4)
                if random.random() < decision_frequency * dt:
                    cycle.ai_decision((self.width, self.height), self.all_trails)
        
        # Check win conditions
        alive_cycles = [c for c in self.cycles if c.alive]
        if len(alive_cycles) <= 1:
            self.game_over = True
            self.game_duration = time.time() - self.start_time
            
            if alive_cycles:
                self.winner = alive_cycles[0]
                print(f"🏆 WINNER: {self.winner.racer_type.value.upper()}")
            else:
                print("💥 SIMULTANEOUS DEREZ - NO WINNER")
            
            self._show_final_stats()
    
    def _show_final_stats(self):
        """Display final race statistics"""
        print("\n📊 RACE STATISTICS:")
        print("=" * 40)
        
        for i, cycle in enumerate(self.cycles):
            status = "ALIVE" if cycle.alive else "DEREZZED"
            print(f"Cycle {i+1} ({cycle.racer_type.value}): {status}")
            print(f"  Distance: {cycle.distance_traveled:.1f}")
            print(f"  Turns: {cycle.turns_made}")
            print(f"  Consciousness: {cycle.consciousness_level:.2f}")
            
            if not cycle.alive:
                print(f"  Survival Time: {cycle.derezzed_time:.1f}s")
            print()
        
        print(f"Race Duration: {self.game_duration:.1f} seconds")
    
    def handle_input(self, keys_pressed):
        """Handle player input"""
        if not self.game_started or self.game_over:
            return
        
        # Find player cycle
        player_cycle = None
        for cycle in self.cycles:
            if cycle.racer_type == RacerType.PLAYER and cycle.alive:
                player_cycle = cycle
                break
        
        if not player_cycle:
            return
        
        # Handle turning (with cooldown to prevent spam)
        current_time = time.time()
        if not hasattr(self, '_last_turn_time'):
            self._last_turn_time = 0
        
        turn_cooldown = 0.1  # Minimum time between turns
        
        if current_time - self._last_turn_time > turn_cooldown:
            if keys_pressed[pygame.K_LEFT]:
                player_cycle.turn_left()
                self._last_turn_time = current_time
            elif keys_pressed[pygame.K_RIGHT]:
                player_cycle.turn_right()
                self._last_turn_time = current_time
    
    def draw(self, screen):
        """Draw the entire arena"""
        # Clear screen with TRON-style background
        screen.fill((0, 5, 15))
        
        # Draw grid effect
        self._draw_grid_background(screen)
        
        # Draw all light trails
        for trail in self.all_trails:
            self._draw_trail(screen, trail)
        
        # Draw light cycles
        for cycle in self.cycles:
            self._draw_cycle(screen, cycle)
        
        # Draw HUD
        self._draw_hud(screen)
        
        # Draw game over screen
        if self.game_over:
            self._draw_game_over(screen)
    
    def _draw_grid_background(self, screen):
        """Draw the arena grid background"""
        grid_color = (0, 30, 50)
        pulse_color = (0, 60, 100)
        
        # Pulsing effect
        pulse_intensity = abs(math.sin(self.grid_pulse)) * 0.5 + 0.5
        current_color = tuple(int(grid_color[i] + (pulse_color[i] - grid_color[i]) * pulse_intensity) 
                             for i in range(3))
        
        # Draw grid lines
        grid_spacing = 40
        
        # Vertical lines
        for x in range(0, self.width, grid_spacing):
            pygame.draw.line(screen, current_color, (x, 0), (x, self.height), 1)
        
        # Horizontal lines
        for y in range(0, self.height, grid_spacing):
            pygame.draw.line(screen, current_color, (0, y), (self.width, y), 1)
        
        # Arena boundary
        pygame.draw.rect(screen, (0, 150, 255), (10, 10, self.width-20, self.height-20), 3)
    
    def _draw_trail(self, screen, trail: LightTrail):
        """Draw a light trail segment"""
        # Trail fading effect
        age = time.time() - trail.creation_time
        max_age = 2.0  # Trails fade after 2 seconds
        
        if age > max_age:
            return
        
        fade_factor = 1.0 - (age / max_age)
        faded_color = tuple(int(c * fade_factor) for c in trail.color)
        
        # Draw trail as thick line
        pygame.draw.line(screen, faded_color, trail.start_pos, trail.end_pos, int(trail.width))
        
        # Add glow effect
        glow_color = tuple(min(255, int(c * 1.5)) for c in faded_color)
        pygame.draw.line(screen, glow_color, trail.start_pos, trail.end_pos, 1)
    
    def _draw_cycle(self, screen, cycle: LightCycle):
        """Draw a light cycle"""
        if not cycle.alive:
            # Draw derez effect
            if cycle.derezzed_time < 1.0:
                # Fragmenting effect
                fragments = 8
                for i in range(fragments):
                    angle = (i / fragments) * 2 * math.pi
                    offset_x = math.cos(angle) * cycle.derezzed_time * 20
                    offset_y = math.sin(angle) * cycle.derezzed_time * 20
                    
                    fragment_pos = (
                        int(cycle.pos.x + offset_x),
                        int(cycle.pos.y + offset_y)
                    )
                    
                    fade = 1.0 - cycle.derezzed_time
                    faded_color = tuple(int(c * fade) for c in cycle.color)
                    
                    pygame.draw.circle(screen, faded_color, fragment_pos, 2)
            return
        
        # Draw cycle body
        cycle_pos = (int(cycle.pos.x), int(cycle.pos.y))
        
        # Glow effect
        glow_radius = 12
        glow_color = tuple(min(255, int(c * 0.3)) for c in cycle.color)
        pygame.gfxdraw.filled_circle(screen, cycle_pos[0], cycle_pos[1], glow_radius, glow_color)
        
        # Main body
        pygame.draw.circle(screen, cycle.color, cycle_pos, 6)
        pygame.draw.circle(screen, (255, 255, 255), cycle_pos, 6, 2)
        
        # Direction indicator
        direction_end = (
            int(cycle.pos.x + math.cos(cycle.direction) * 12),
            int(cycle.pos.y + math.sin(cycle.direction) * 12)
        )
        pygame.draw.line(screen, cycle.color, cycle_pos, direction_end, 3)
        
        # Consciousness indicator for AI
        if cycle.racer_type != RacerType.PLAYER and cycle.consciousness_level > 0.3:
            consciousness_color = (255, 215, 0)  # Gold
            consciousness_radius = int(8 + 4 * cycle.consciousness_level)
            pygame.draw.circle(screen, consciousness_color, cycle_pos, consciousness_radius, 1)
    
    def _draw_hud(self, screen):
        """Draw the heads-up display"""
        font_large = pygame.font.Font(None, 36)
        font_medium = pygame.font.Font(None, 24)
        font_small = pygame.font.Font(None, 18)
        
        # Title
        title_text = font_large.render("LIGHT CYCLE ARENA", True, (0, 255, 255))
        screen.blit(title_text, (10, 10))
        
        # Game status
        if not self.game_started:
            status_text = font_medium.render("PRESS SPACE TO START", True, (255, 255, 0))
            status_rect = status_text.get_rect(center=(self.width//2, self.height//2))
            screen.blit(status_text, status_rect)
        
        # Cycle status
        alive_cycles = [c for c in self.cycles if c.alive]
        status_text = font_small.render(f"Cycles Remaining: {len(alive_cycles)}", True, (255, 255, 255))
        screen.blit(status_text, (10, 50))
        
        # Race time
        if self.game_started:
            race_time = time.time() - self.start_time if not self.game_over else self.game_duration
            time_text = font_small.render(f"Race Time: {race_time:.1f}s", True, (255, 255, 255))
            screen.blit(time_text, (10, 70))
        
        # Player status
        player_cycle = None
        for cycle in self.cycles:
            if cycle.racer_type == RacerType.PLAYER:
                player_cycle = cycle
                break
        
        if player_cycle:
            player_status = "ALIVE" if player_cycle.alive else "DEREZZED"
            color = (0, 255, 0) if player_cycle.alive else (255, 100, 100)
            
            player_text = font_small.render(f"Player: {player_status}", True, color)
            screen.blit(player_text, (10, 90))
            
            if player_cycle.alive:
                distance_text = font_small.render(f"Distance: {player_cycle.distance_traveled:.0f}", True, (255, 255, 255))
                screen.blit(distance_text, (10, 110))
                
                turns_text = font_small.render(f"Turns: {player_cycle.turns_made}", True, (255, 255, 255))
                screen.blit(turns_text, (10, 130))
        
        # Controls
        controls_y = self.height - 80
        controls = [
            "ARROW KEYS - Turn",
            "SPACE - Start Race",
            "ESC - Exit Arena"
        ]
        
        for i, control in enumerate(controls):
            control_text = font_small.render(control, True, (200, 200, 200))
            screen.blit(control_text, (10, controls_y + i * 15))
    
    def _draw_game_over(self, screen):
        """Draw game over screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        font_large = pygame.font.Font(None, 72)
        font_medium = pygame.font.Font(None, 36)
        
        # Game Over text
        game_over_text = font_large.render("GAME OVER", True, (255, 100, 100))
        game_over_rect = game_over_text.get_rect(center=(self.width//2, self.height//2 - 50))
        screen.blit(game_over_text, game_over_rect)
        
        # Winner text
        if self.winner:
            winner_text = font_medium.render(f"WINNER: {self.winner.racer_type.value.upper()}", True, (255, 255, 0))
            winner_rect = winner_text.get_rect(center=(self.width//2, self.height//2))
            screen.blit(winner_text, winner_rect)
        
        # Restart prompt
        restart_text = font_medium.render("PRESS R TO RESTART", True, (0, 255, 255))
        restart_rect = restart_text.get_rect(center=(self.width//2, self.height//2 + 50))
        screen.blit(restart_text, restart_rect)

def main():
    """Launch the Light Cycle Arena"""
    if not PYGAME_AVAILABLE:
        print("❌ pygame required for Light Cycle Arena")
        return
    
    pygame.init()
    
    arena = LightCycleArena()
    screen = pygame.display.set_mode((arena.width, arena.height))
    pygame.display.set_caption("TRON Light Cycle Arena")
    clock = pygame.time.Clock()
    
    print("🏁 TRON LIGHT CYCLE ARENA")
    print("=" * 40)
    print("🎮 Navigate with ARROW KEYS")
    print("🚦 Press SPACE to start race")
    print("💥 Avoid light trails to survive!")
    print("🏆 Last cycle standing wins!")
    print("=" * 40)
    
    running = True
    
    while running:
        dt = clock.tick(60) / 1000.0
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE and not arena.game_started:
                    arena.start_game()
                elif event.key == pygame.K_r and arena.game_over:
                    # Restart game
                    arena = LightCycleArena()
        
        # Handle continuous input
        keys_pressed = pygame.key.get_pressed()
        arena.handle_input(keys_pressed)
        
        # Update
        arena.update(dt)
        
        # Draw
        arena.draw(screen)
        pygame.display.flip()
    
    pygame.quit()
    print("🏁 Light Cycle Arena shut down")

if __name__ == "__main__":
    main()
