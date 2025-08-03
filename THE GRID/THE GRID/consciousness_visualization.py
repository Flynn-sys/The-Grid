#!/usr/bin/env python3
"""
Consciousness Research Visualization
Integrates computational consciousness framework with TRON grid visualization
Shows real-time consciousness indicators based on legitimate theories
"""

import math
import time
import threading
from typing import Dict, List, Tuple, Optional

try:
    import pygame
    import pygame.gfxdraw
    from pygame import Vector3
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False
    print("⚠️  pygame not available - install with: pip install pygame")

if PYGAME_AVAILABLE:
    from consciousness_research import ConsciousnessMetrics, GlobalWorkspace
    
class ConsciousnessVisualization:
    """Visualize consciousness research metrics in real-time"""
    
    def __init__(self, width: int = 1200, height: int = 800):
        if not PYGAME_AVAILABLE:
            raise ImportError("pygame required for visualization")
            
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Consciousness Research Visualization")
        
        self.font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 18)
        
        # Consciousness metrics
        self.consciousness_metrics = ConsciousnessMetrics()
        self.current_indicators = {}
        self.metrics_history = []
        self.max_history = 200
        
        # Visualization parameters
        self.node_positions = self._calculate_node_positions()
        self.connection_alpha = 100
        
        # Colors
        self.bg_color = (10, 10, 20)
        self.node_color = (0, 200, 255)
        self.active_node_color = (255, 200, 0)
        self.connection_color = (50, 100, 150)
        self.text_color = (200, 200, 200)
        self.highlight_color = (255, 100, 100)
        
    def _calculate_node_positions(self) -> Dict[int, Tuple[int, int]]:
        """Calculate 2D positions for network nodes"""
        positions = {}
        num_nodes = len(self.consciousness_metrics.workspace.nodes)
        
        # Arrange nodes in a circle for better visualization
        center_x, center_y = self.width // 3, self.height // 2
        radius = min(200, min(center_x, center_y) - 50)
        
        for i in range(num_nodes):
            angle = 2 * math.pi * i / num_nodes
            x = center_x + int(radius * math.cos(angle))
            y = center_y + int(radius * math.sin(angle))
            positions[i] = (x, y)
            
        return positions
    
    def draw_network(self):
        """Draw the consciousness network visualization"""
        workspace = self.consciousness_metrics.workspace
        
        # Draw connections first (underneath nodes)
        for node_id, node in workspace.nodes.items():
            if node.activation_level > 0.1:  # Only show active connections
                node_pos = self.node_positions[node_id]
                
                for conn_id in node.connections:
                    if conn_id in workspace.nodes and workspace.nodes[conn_id].activation_level > 0.1:
                        conn_pos = self.node_positions[conn_id]
                        
                        # Connection strength based on activation
                        strength = (node.activation_level + workspace.nodes[conn_id].activation_level) / 2
                        alpha = int(strength * 150)
                        
                        if alpha > 20:  # Only draw visible connections
                            color = (*self.connection_color, alpha)
                            # Create surface for alpha blending
                            line_surf = pygame.Surface((abs(conn_pos[0] - node_pos[0]) + 2, 
                                                      abs(conn_pos[1] - node_pos[1]) + 2), pygame.SRCALPHA)
                            
                            # Draw line on alpha surface
                            start_pos = (min(node_pos[0], conn_pos[0]) - min(node_pos[0], conn_pos[0]),
                                       min(node_pos[1], conn_pos[1]) - min(node_pos[1], conn_pos[1]))
                            end_pos = (abs(conn_pos[0] - node_pos[0]), abs(conn_pos[1] - node_pos[1]))
                            
                            pygame.draw.line(self.screen, self.connection_color, node_pos, conn_pos, 1)
        
        # Draw nodes
        for node_id, node in workspace.nodes.items():
            pos = self.node_positions[node_id]
            
            # Node size based on activation
            base_radius = 3
            radius = base_radius + int(node.activation_level * 8)
            
            # Color based on state and attention
            if (hasattr(self.consciousness_metrics.attention, 'attention_focus') and 
                self.consciousness_metrics.attention.attention_focus == node_id):
                color = self.highlight_color
            elif node.activation_level > 0.5:
                color = self.active_node_color
            else:
                # Interpolate between inactive and active colors
                factor = node.activation_level
                color = tuple(int(self.node_color[i] * factor + 
                                self.connection_color[i] * (1 - factor)) for i in range(3))
            
            pygame.draw.circle(self.screen, color, pos, radius)
            
            # Add glow effect for highly active nodes
            if node.activation_level > 0.7:
                glow_radius = radius + 5
                glow_alpha = int(node.activation_level * 50)
                glow_surf = pygame.Surface((glow_radius * 2, glow_radius * 2), pygame.SRCALPHA)
                pygame.draw.circle(glow_surf, (*color, glow_alpha), (glow_radius, glow_radius), glow_radius)
                self.screen.blit(glow_surf, (pos[0] - glow_radius, pos[1] - glow_radius))
    
    def draw_metrics_panel(self):
        """Draw consciousness metrics panel"""
        panel_x = self.width - 350
        panel_y = 20
        panel_width = 330
        panel_height = self.height - 40
        
        # Panel background
        panel_surf = pygame.Surface((panel_width, panel_height), pygame.SRCALPHA)
        panel_surf.fill((20, 20, 40, 200))
        self.screen.blit(panel_surf, (panel_x, panel_y))
        
        # Title
        title = self.font.render("Consciousness Indicators", True, self.text_color)
        self.screen.blit(title, (panel_x + 10, panel_y + 10))
        
        y_offset = 50
        
        # Current indicators
        if self.current_indicators:
            for metric, value in self.current_indicators.items():
                if isinstance(value, float) and metric != "overall_complexity":
                    # Metric name
                    name = metric.replace('_', ' ').title()
                    text = self.small_font.render(f"{name}:", True, self.text_color)
                    self.screen.blit(text, (panel_x + 15, panel_y + y_offset))
                    
                    # Value bar
                    bar_width = 150
                    bar_height = 10
                    bar_x = panel_x + 15
                    bar_y = panel_y + y_offset + 20
                    
                    # Background bar
                    pygame.draw.rect(self.screen, (50, 50, 50), 
                                   (bar_x, bar_y, bar_width, bar_height))
                    
                    # Value bar
                    fill_width = int(value * bar_width)
                    color = self._get_metric_color(value)
                    pygame.draw.rect(self.screen, color,
                                   (bar_x, bar_y, fill_width, bar_height))
                    
                    # Value text
                    value_text = self.small_font.render(f"{value:.3f}", True, self.text_color)
                    self.screen.blit(value_text, (bar_x + bar_width + 10, bar_y - 2))
                    
                    y_offset += 45
        
        # Theory descriptions
        y_offset += 20
        theories = [
            "Based on:",
            "• Global Workspace Theory",
            "• Integrated Information Theory", 
            "• Attention Schema Theory",
            "",
            "Metrics show computational",
            "analogues, not actual",
            "consciousness."
        ]
        
        for line in theories:
            color = self.text_color if not line.startswith("•") else (150, 150, 150)
            text = self.small_font.render(line, True, color)
            self.screen.blit(text, (panel_x + 15, panel_y + y_offset))
            y_offset += 20
    
    def _get_metric_color(self, value: float) -> Tuple[int, int, int]:
        """Get color for metric value"""
        if value < 0.3:
            return (100, 100, 100)  # Low - gray
        elif value < 0.6:
            return (100, 150, 255)  # Medium - blue
        else:
            return (100, 255, 150)  # High - green
    
    def draw_history_graph(self):
        """Draw history graph of overall complexity"""
        if len(self.metrics_history) < 2:
            return
            
        graph_x = 50
        graph_y = self.height - 150
        graph_width = 400
        graph_height = 100
        
        # Graph background
        pygame.draw.rect(self.screen, (30, 30, 50), 
                        (graph_x, graph_y, graph_width, graph_height))
        pygame.draw.rect(self.screen, self.text_color, 
                        (graph_x, graph_y, graph_width, graph_height), 1)
        
        # Title
        title = self.small_font.render("Overall Complexity Over Time", True, self.text_color)
        self.screen.blit(title, (graph_x, graph_y - 25))
        
        # Draw graph line
        if len(self.metrics_history) > 1:
            points = []
            for i, metrics in enumerate(self.metrics_history[-graph_width:]):
                if "overall_complexity" in metrics:
                    x = graph_x + i * (graph_width / len(self.metrics_history[-graph_width:]))
                    y = graph_y + graph_height - (metrics["overall_complexity"] * graph_height)
                    points.append((x, y))
            
            if len(points) > 1:
                pygame.draw.lines(self.screen, (100, 200, 255), False, points, 2)
    
    def run_simulation(self):
        """Run the consciousness visualization simulation"""
        clock = pygame.time.Clock()
        running = True
        step_count = 0
        
        print("🧠 Consciousness Research Visualization")
        print("Controls: ESC to exit")
        print("Watch real-time consciousness indicators based on legitimate theories")
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            # Generate inputs for consciousness simulation
            inputs = {}
            if step_count % 20 == 0:
                # Periodic strong pattern
                inputs = {i: 0.8 for i in range(5)}
            elif step_count % 17 == 0:
                # Attention-grabbing event
                inputs = {25: 0.9, 30: 0.7}
            else:
                # Random sensory inputs
                import random
                inputs = {random.randint(0, 49): random.random() * 0.5 
                         for _ in range(3)}
            
            # Update consciousness metrics
            current_metrics = self.consciousness_metrics.simulate_step(inputs)
            self.current_indicators = self.consciousness_metrics.get_consciousness_indicators()
            
            # Store history
            if "insufficient_data" not in self.current_indicators:
                self.metrics_history.append(self.current_indicators)
                if len(self.metrics_history) > self.max_history:
                    self.metrics_history.pop(0)
            
            # Draw everything
            self.screen.fill(self.bg_color)
            self.draw_network()
            self.draw_metrics_panel()
            self.draw_history_graph()
            
            # Update display
            pygame.display.flip()
            clock.tick(30)  # 30 FPS
            step_count += 1
        
        pygame.quit()

def main():
    """Main function"""
    if not PYGAME_AVAILABLE:
        print("❌ pygame not available")
        print("Install with: pip install pygame")
        return
    
    try:
        viz = ConsciousnessVisualization()
        viz.run_simulation()
    except KeyboardInterrupt:
        print("\n🌐 Simulation interrupted")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
