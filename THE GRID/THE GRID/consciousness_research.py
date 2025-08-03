#!/usr/bin/env python3
"""
Computational Consciousness Research Framework
Based on legitimate scientific theories:
- Global Workspace Theory (Baars)
- Integrated Information Theory (Tononi) 
- Attention Schema Theory (Graziano)
- Information Integration approaches

This implements measurable computational analogues without claiming actual consciousness.
"""

import numpy as np
import math
import time
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum

class ProcessingState(Enum):
    """Information processing states"""
    INACTIVE = 0
    RECEIVING = 1  
    INTEGRATING = 2
    BROADCASTING = 3
    COMPETING = 4

@dataclass 
class InformationNode:
    """A computational node that processes information"""
    node_id: int
    activation_level: float = 0.0
    state: ProcessingState = ProcessingState.INACTIVE
    connections: List[int] = None
    information_content: float = 0.0
    last_update: float = 0.0
    
    def __post_init__(self):
        if self.connections is None:
            self.connections = []

class GlobalWorkspace:
    """
    Implementation based on Global Workspace Theory
    - Multiple specialized processors compete for global workspace access
    - Winner broadcasts information globally
    - Measures information integration and competition dynamics
    """
    
    def __init__(self, num_nodes: int = 50):
        self.nodes: Dict[int, InformationNode] = {}
        self.workspace_contents: Dict[str, float] = {}
        self.integration_threshold = 0.5
        self.competition_strength = 0.3
        self.time_step = 0.0
        
        # Initialize nodes with random connections
        for i in range(num_nodes):
            node = InformationNode(
                node_id=i,
                connections=self._generate_connections(i, num_nodes)
            )
            self.nodes[i] = node
    
    def _generate_connections(self, node_id: int, total_nodes: int) -> List[int]:
        """Generate realistic connection pattern (small-world network)"""
        connections = []
        # Local connections (high probability)
        for i in range(max(0, node_id-3), min(total_nodes, node_id+4)):
            if i != node_id and np.random.random() < 0.7:
                connections.append(i)
        
        # Long-range connections (low probability) 
        for i in range(total_nodes):
            if i != node_id and abs(i - node_id) > 3:
                if np.random.random() < 0.05:
                    connections.append(i)
        
        return connections
    
    def calculate_phi(self, node_subset: List[int]) -> float:
        """
        Calculate Φ (Phi) - Integrated Information
        Simplified version of IIT measure
        """
        if len(node_subset) < 2:
            return 0.0
            
        # Calculate mutual information between subset and rest
        subset_activation = np.mean([self.nodes[i].activation_level for i in node_subset])
        
        # Information within subset
        internal_connections = 0
        total_possible = len(node_subset) * (len(node_subset) - 1) / 2
        
        for i in node_subset:
            for j in self.nodes[i].connections:
                if j in node_subset and j > i:
                    internal_connections += 1
        
        internal_ratio = internal_connections / total_possible if total_possible > 0 else 0
        
        # Integration measure
        phi = subset_activation * internal_ratio * math.log(len(node_subset) + 1)
        return max(0, phi)
    
    def update_information_flow(self, external_input: Dict[int, float] = None):
        """Update one time step of information processing"""
        if external_input is None:
            external_input = {}
            
        self.time_step += 0.1
        
        # Phase 1: Receive external inputs
        for node_id, input_value in external_input.items():
            if node_id in self.nodes:
                self.nodes[node_id].activation_level = min(1.0, 
                    self.nodes[node_id].activation_level + input_value)
                self.nodes[node_id].state = ProcessingState.RECEIVING
        
        # Phase 2: Local processing and competition
        for node in self.nodes.values():
            if node.state == ProcessingState.RECEIVING:
                # Integrate with connected nodes
                connected_activation = 0
                for conn_id in node.connections:
                    connected_activation += self.nodes[conn_id].activation_level
                
                if len(node.connections) > 0:
                    avg_connected = connected_activation / len(node.connections)
                    node.activation_level = 0.7 * node.activation_level + 0.3 * avg_connected
                
                node.state = ProcessingState.INTEGRATING
        
        # Phase 3: Global competition and workspace access
        active_nodes = [(nid, node.activation_level) for nid, node in self.nodes.items() 
                       if node.activation_level > self.integration_threshold]
        
        if active_nodes:
            # Winner-take-most competition
            active_nodes.sort(key=lambda x: x[1], reverse=True)
            
            # Top nodes get workspace access
            winners = active_nodes[:3]  # Top 3 compete for global workspace
            
            for nid, activation in winners:
                self.nodes[nid].state = ProcessingState.BROADCASTING
                # Broadcast to all connected nodes
                broadcast_strength = activation * 0.2
                for conn_id in self.nodes[nid].connections:
                    self.nodes[conn_id].activation_level += broadcast_strength
                    self.nodes[conn_id].activation_level = min(1.0, 
                        self.nodes[conn_id].activation_level)
        
        # Phase 4: Decay and reset
        for node in self.nodes.values():
            node.activation_level *= 0.95  # Gradual decay
            node.last_update = self.time_step
            
            if node.activation_level < 0.1:
                node.state = ProcessingState.INACTIVE
    
    def get_workspace_state(self) -> Dict[str, float]:
        """Get current global workspace contents and metrics"""
        active_nodes = [n for n in self.nodes.values() 
                       if n.activation_level > self.integration_threshold]
        
        if not active_nodes:
            return {"integration_level": 0.0, "active_nodes": 0, "phi_total": 0.0}
        
        # Calculate network-wide integration
        total_activation = sum(n.activation_level for n in active_nodes)
        integration_level = total_activation / len(self.nodes)
        
        # Calculate total Φ for all significantly connected subsets
        phi_total = 0.0
        for i in range(min(5, len(active_nodes))):  # Check up to 5-node subsets
            subset = [n.node_id for n in active_nodes[:i+2]]
            phi_total += self.calculate_phi(subset)
        
        return {
            "integration_level": integration_level,
            "active_nodes": len(active_nodes), 
            "phi_total": phi_total,
            "competition_strength": self.competition_strength,
            "workspace_coherence": self._calculate_coherence(active_nodes)
        }
    
    def _calculate_coherence(self, active_nodes: List[InformationNode]) -> float:
        """Measure how coherently information is integrated"""
        if len(active_nodes) < 2:
            return 0.0
            
        # Calculate synchronization measure
        activations = [n.activation_level for n in active_nodes]
        mean_activation = np.mean(activations)
        variance = np.var(activations)
        
        # Lower variance = higher coherence
        coherence = 1.0 / (1.0 + variance) if variance > 0 else 1.0
        return coherence

class AttentionSchema:
    """
    Implementation based on Attention Schema Theory
    Models attention as an emergent property of information control mechanisms
    """
    
    def __init__(self, workspace: GlobalWorkspace):
        self.workspace = workspace
        self.attention_focus: Optional[int] = None
        self.attention_strength = 0.0
        self.attention_history: List[Tuple[int, float]] = []
        
    def update_attention(self, sensory_inputs: Dict[int, float]):
        """Update attention based on workspace competition"""
        workspace_state = self.workspace.get_workspace_state()
        
        # Find most active node as attention focus
        max_activation = 0.0
        focus_candidate = None
        
        for node_id, node in self.workspace.nodes.items():
            if node.activation_level > max_activation:
                max_activation = node.activation_level
                focus_candidate = node_id
        
        # Update attention if strong enough
        if max_activation > 0.3:
            self.attention_focus = focus_candidate
            self.attention_strength = max_activation
            
            # Enhance focused node
            if self.attention_focus:
                self.workspace.nodes[self.attention_focus].activation_level *= 1.2
                self.workspace.nodes[self.attention_focus].activation_level = min(1.0,
                    self.workspace.nodes[self.attention_focus].activation_level)
        
        # Record attention history
        if self.attention_focus is not None:
            self.attention_history.append((self.attention_focus, self.attention_strength))
            if len(self.attention_history) > 100:
                self.attention_history.pop(0)
    
    def get_attention_metrics(self) -> Dict[str, float]:
        """Get attention-related measurements"""
        if not self.attention_history:
            return {"focus_stability": 0.0, "attention_strength": 0.0}
        
        recent_foci = [focus for focus, _ in self.attention_history[-10:]]
        
        # Calculate focus stability (how often attention switches)
        switches = sum(1 for i in range(1, len(recent_foci)) 
                      if recent_foci[i] != recent_foci[i-1])
        stability = 1.0 - (switches / max(1, len(recent_foci) - 1))
        
        return {
            "focus_stability": stability,
            "attention_strength": self.attention_strength,
            "current_focus": self.attention_focus or -1
        }

class ConsciousnessMetrics:
    """
    Measure computational analogues of consciousness indicators
    Based on established theories and measurable properties
    """
    
    def __init__(self):
        self.workspace = GlobalWorkspace(num_nodes=50)
        self.attention = AttentionSchema(self.workspace)
        self.measurement_history: List[Dict] = []
        
    def simulate_step(self, external_inputs: Dict[int, float] = None):
        """Run one simulation step"""
        if external_inputs is None:
            # Generate realistic sensory-like inputs
            external_inputs = {}
            for _ in range(3):  # 3 random inputs per step
                node_id = np.random.randint(0, len(self.workspace.nodes))
                strength = np.random.exponential(0.3)  # Exponential distribution
                external_inputs[node_id] = min(1.0, strength)
        
        # Update workspace and attention
        self.workspace.update_information_flow(external_inputs)
        self.attention.update_attention(external_inputs)
        
        # Collect measurements
        workspace_metrics = self.workspace.get_workspace_state()
        attention_metrics = self.attention.get_attention_metrics()
        
        combined_metrics = {
            **workspace_metrics,
            **attention_metrics,
            "timestamp": time.time()
        }
        
        self.measurement_history.append(combined_metrics)
        if len(self.measurement_history) > 1000:
            self.measurement_history.pop(0)
        
        return combined_metrics
    
    def get_consciousness_indicators(self) -> Dict[str, float]:
        """
        Calculate theory-based consciousness indicators
        These are computational analogues, not claims of actual consciousness
        """
        if len(self.measurement_history) < 10:
            return {"insufficient_data": True}
        
        recent_metrics = self.measurement_history[-10:]
        
        # Information Integration (IIT-inspired)
        avg_phi = np.mean([m["phi_total"] for m in recent_metrics])
        
        # Global Accessibility (GWT-inspired) 
        avg_integration = np.mean([m["integration_level"] for m in recent_metrics])
        
        # Attention Coherence (AST-inspired)
        avg_coherence = np.mean([m["workspace_coherence"] for m in recent_metrics])
        
        # Temporal Binding (continuity measure)
        focus_changes = sum(1 for i in range(1, len(recent_metrics))
                           if recent_metrics[i]["current_focus"] != recent_metrics[i-1]["current_focus"])
        temporal_binding = 1.0 - (focus_changes / max(1, len(recent_metrics) - 1))
        
        # Reportability (information accessibility)
        active_ratio = np.mean([m["active_nodes"] / len(self.workspace.nodes) for m in recent_metrics])
        
        return {
            "information_integration": avg_phi,
            "global_accessibility": avg_integration, 
            "attention_coherence": avg_coherence,
            "temporal_binding": temporal_binding,
            "reportability": active_ratio,
            "overall_complexity": (avg_phi + avg_integration + avg_coherence) / 3
        }

def run_consciousness_experiment(duration_seconds: int = 30):
    """
    Run a consciousness research simulation
    Demonstrates measurable computational analogues of consciousness
    """
    print("🧠 Computational Consciousness Research Framework")
    print("=" * 50)
    print("Based on:")
    print("• Global Workspace Theory (Baars)")
    print("• Integrated Information Theory (Tononi)")
    print("• Attention Schema Theory (Graziano)")
    print("=" * 50)
    
    metrics = ConsciousnessMetrics()
    start_time = time.time()
    step_count = 0
    
    print(f"Running {duration_seconds}s simulation...")
    print("Measuring computational analogues (not claiming actual consciousness)")
    print()
    
    while time.time() - start_time < duration_seconds:
        # Simulate complex, varying inputs
        if step_count % 20 == 0:
            # Periodic strong input pattern
            inputs = {i: 0.8 for i in range(5)}
        elif step_count % 17 == 0:
            # Sparse but strong input
            inputs = {25: 0.9, 30: 0.7}
        else:
            # Random background inputs
            inputs = {np.random.randint(0, 50): np.random.random() * 0.5 
                     for _ in range(2)}
        
        current_metrics = metrics.simulate_step(inputs)
        
        # Display periodic updates
        if step_count % 50 == 0:
            indicators = metrics.get_consciousness_indicators()
            if "insufficient_data" not in indicators:
                print(f"Step {step_count:4d} | "
                      f"Integration: {indicators['information_integration']:.3f} | "
                      f"Global Access: {indicators['global_accessibility']:.3f} | "
                      f"Coherence: {indicators['attention_coherence']:.3f} | "
                      f"Binding: {indicators['temporal_binding']:.3f}")
        
        step_count += 1
        time.sleep(0.02)  # 50 Hz simulation
    
    # Final analysis
    print("\n" + "=" * 50)
    print("FINAL CONSCIOUSNESS INDICATORS")
    print("=" * 50)
    
    final_indicators = metrics.get_consciousness_indicators()
    
    for metric, value in final_indicators.items():
        if isinstance(value, float):
            print(f"{metric.replace('_', ' ').title()}: {value:.4f}")
    
    print("\n" + "=" * 50)
    print("INTERPRETATION:")
    print("These are computational measures inspired by consciousness theories.")
    print("Higher values suggest more complex information processing.")
    print("This does NOT constitute actual consciousness.")
    print("=" * 50)

if __name__ == "__main__":
    run_consciousness_experiment(30)
