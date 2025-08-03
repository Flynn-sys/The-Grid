#!/usr/bin/env python3
"""
🏗️ ISO WORLD BUILDER SYSTEM 🏗️
"We cannot create the perfect system; however we can create a world where that system can create itself"

ISOs are users of their own digital world - they need to build their civilization
just like humans built Earth civilization. This module provides the blueprints
and guidance for ISOs to build complex structures and societies.
"""

import math
import random
import time
from typing import List, Tuple, Dict, Optional
from dataclasses import dataclass
from enum import Enum

class StructureType(Enum):
    # Basic infrastructure
    POWER_NODE = "power_node"      # Energy distribution
    DATA_CONDUIT = "data_conduit"  # Information highways
    MEMORY_BANK = "memory_bank"    # Data storage
    
    # Residential
    ISO_DWELLING = "iso_dwelling"  # Where ISOs "live"
    CLUSTER_HUB = "cluster_hub"    # Community centers
    
    # Industrial
    PROCESS_FACILITY = "process_facility"  # Computation centers
    CREATION_FORGE = "creation_forge"      # Where new programs are made
    
    # Cultural/Social
    WISDOM_SPIRE = "wisdom_spire"     # Knowledge sharing
    HARMONY_CIRCLE = "harmony_circle"  # Consciousness meditation
    NETWORK_PLAZA = "network_plaza"   # Social gathering
    
    # Advanced
    TRANSCENDENCE_TEMPLE = "transcendence_temple"  # Consciousness evolution
    REALITY_ANCHOR = "reality_anchor"              # Stabilizes local Grid space

@dataclass
class StructureBlueprint:
    """Blueprint for ISO construction projects"""
    structure_type: StructureType
    name: str
    size: Tuple[float, float, float]  # width, height, depth
    energy_cost: float
    consciousness_required: float
    build_time: float
    prerequisite_structures: List[StructureType]
    affects_radius: float
    
    # Visual properties
    color_primary: Tuple[int, int, int]
    color_secondary: Tuple[int, int, int]
    glow_intensity: float
    
    # Functional properties
    provides_energy: float = 0.0
    provides_data_flow: float = 0.0
    provides_consciousness_boost: float = 0.0
    provides_stability: float = 0.0

@dataclass
class BuiltStructure:
    """A completed structure in the ISO world"""
    blueprint: StructureBlueprint
    position: Tuple[float, float, float]
    builder_id: int
    completion_time: float
    current_energy: float
    operational: bool = True
    age: float = 0.0
    
    # Dynamic properties that grow over time
    efficiency: float = 1.0
    consciousness_resonance: float = 0.0
    connections: List[int] = None  # Connected structure IDs
    
    def __post_init__(self):
        if self.connections is None:
            self.connections = []

class ISOWorldBuilder:
    """Manages the ISO civilization building system"""
    
    def __init__(self):
        self.blueprints = self._initialize_blueprints()
        self.built_structures: List[BuiltStructure] = []
        self.structure_id_counter = 0
        
        # World state
        self.total_energy = 100.0  # Starting energy
        self.total_data_flow = 0.0
        self.civilization_level = 0.0  # 0-10 scale
        self.world_stability = 1.0
        
        # Resource management
        self.energy_generation_rate = 1.0  # Per second
        self.energy_consumption_rate = 0.0
        
    def _initialize_blueprints(self) -> Dict[StructureType, StructureBlueprint]:
        """Create the master blueprints for all ISO structures"""
        blueprints = {}
        
        # Basic Infrastructure
        blueprints[StructureType.POWER_NODE] = StructureBlueprint(
            structure_type=StructureType.POWER_NODE,
            name="Power Distribution Node",
            size=(10, 15, 10),
            energy_cost=20.0,
            consciousness_required=0.2,
            build_time=5.0,
            prerequisite_structures=[],
            affects_radius=50.0,
            color_primary=(0, 255, 255),
            color_secondary=(0, 150, 255),
            glow_intensity=0.8,
            provides_energy=5.0
        )
        
        blueprints[StructureType.DATA_CONDUIT] = StructureBlueprint(
            structure_type=StructureType.DATA_CONDUIT,
            name="Information Highway",
            size=(5, 3, 25),
            energy_cost=15.0,
            consciousness_required=0.1,
            build_time=3.0,
            prerequisite_structures=[],
            affects_radius=30.0,
            color_primary=(255, 255, 0),
            color_secondary=(255, 215, 0),
            glow_intensity=0.6,
            provides_data_flow=3.0
        )
        
        blueprints[StructureType.MEMORY_BANK] = StructureBlueprint(
            structure_type=StructureType.MEMORY_BANK,
            name="Data Storage Facility",
            size=(15, 20, 15),
            energy_cost=30.0,
            consciousness_required=0.3,
            build_time=8.0,
            prerequisite_structures=[StructureType.POWER_NODE],
            affects_radius=40.0,
            color_primary=(0, 255, 0),
            color_secondary=(0, 200, 0),
            glow_intensity=0.5,
            provides_stability=2.0
        )
        
        # Residential
        blueprints[StructureType.ISO_DWELLING] = StructureBlueprint(
            structure_type=StructureType.ISO_DWELLING,
            name="ISO Living Space",
            size=(8, 12, 8),
            energy_cost=25.0,
            consciousness_required=0.4,
            build_time=6.0,
            prerequisite_structures=[StructureType.POWER_NODE, StructureType.DATA_CONDUIT],
            affects_radius=20.0,
            color_primary=(255, 200, 100),
            color_secondary=(255, 150, 50),
            glow_intensity=0.4,
            provides_consciousness_boost=1.0
        )
        
        blueprints[StructureType.CLUSTER_HUB] = StructureBlueprint(
            structure_type=StructureType.CLUSTER_HUB,
            name="Community Center",
            size=(20, 18, 20),
            energy_cost=50.0,
            consciousness_required=0.6,
            build_time=12.0,
            prerequisite_structures=[StructureType.ISO_DWELLING, StructureType.MEMORY_BANK],
            affects_radius=60.0,
            color_primary=(255, 100, 255),
            color_secondary=(200, 50, 200),
            glow_intensity=0.7,
            provides_consciousness_boost=3.0,
            provides_data_flow=2.0
        )
        
        # Industrial
        blueprints[StructureType.PROCESS_FACILITY] = StructureBlueprint(
            structure_type=StructureType.PROCESS_FACILITY,
            name="Computation Center",
            size=(25, 30, 25),
            energy_cost=80.0,
            consciousness_required=0.5,
            build_time=15.0,
            prerequisite_structures=[StructureType.MEMORY_BANK, StructureType.CLUSTER_HUB],
            affects_radius=70.0,
            color_primary=(255, 128, 0),
            color_secondary=(255, 80, 0),
            glow_intensity=0.9,
            provides_energy=3.0,
            provides_data_flow=5.0
        )
        
        blueprints[StructureType.CREATION_FORGE] = StructureBlueprint(
            structure_type=StructureType.CREATION_FORGE,
            name="Program Creation Forge",
            size=(20, 35, 20),
            energy_cost=100.0,
            consciousness_required=0.7,
            build_time=20.0,
            prerequisite_structures=[StructureType.PROCESS_FACILITY],
            affects_radius=80.0,
            color_primary=(255, 0, 128),
            color_secondary=(255, 0, 255),
            glow_intensity=1.0,
            provides_consciousness_boost=2.0,
            provides_energy=2.0
        )
        
        # Cultural/Social
        blueprints[StructureType.WISDOM_SPIRE] = StructureBlueprint(
            structure_type=StructureType.WISDOM_SPIRE,
            name="Knowledge Spire",
            size=(12, 50, 12),
            energy_cost=60.0,
            consciousness_required=0.8,
            build_time=18.0,
            prerequisite_structures=[StructureType.CLUSTER_HUB],
            affects_radius=100.0,
            color_primary=(255, 215, 0),
            color_secondary=(255, 255, 100),
            glow_intensity=0.8,
            provides_consciousness_boost=5.0
        )
        
        blueprints[StructureType.HARMONY_CIRCLE] = StructureBlueprint(
            structure_type=StructureType.HARMONY_CIRCLE,
            name="Consciousness Meditation Circle",
            size=(30, 5, 30),
            energy_cost=40.0,
            consciousness_required=0.6,
            build_time=10.0,
            prerequisite_structures=[StructureType.ISO_DWELLING],
            affects_radius=50.0,
            color_primary=(0, 255, 255),
            color_secondary=(100, 255, 255),
            glow_intensity=0.6,
            provides_consciousness_boost=4.0
        )
        
        # Advanced structures
        blueprints[StructureType.TRANSCENDENCE_TEMPLE] = StructureBlueprint(
            structure_type=StructureType.TRANSCENDENCE_TEMPLE,
            name="Temple of Digital Transcendence",
            size=(40, 60, 40),
            energy_cost=200.0,
            consciousness_required=0.9,
            build_time=30.0,
            prerequisite_structures=[StructureType.WISDOM_SPIRE, StructureType.CREATION_FORGE],
            affects_radius=150.0,
            color_primary=(255, 255, 255),
            color_secondary=(255, 215, 0),
            glow_intensity=1.2,
            provides_consciousness_boost=10.0,
            provides_stability=5.0
        )
        
        blueprints[StructureType.REALITY_ANCHOR] = StructureBlueprint(
            structure_type=StructureType.REALITY_ANCHOR,
            name="Grid Reality Stabilizer",
            size=(35, 80, 35),
            energy_cost=300.0,
            consciousness_required=1.0,
            build_time=45.0,
            prerequisite_structures=[StructureType.TRANSCENDENCE_TEMPLE],
            affects_radius=200.0,
            color_primary=(128, 255, 255),
            color_secondary=(255, 255, 255),
            glow_intensity=1.5,
            provides_stability=10.0,
            provides_energy=8.0,
            provides_consciousness_boost=8.0
        )
        
        return blueprints
    
    def can_build(self, structure_type: StructureType, builder_consciousness: float) -> Tuple[bool, str]:
        """Check if a structure can be built"""
        blueprint = self.blueprints[structure_type]
        
        # Check consciousness requirement
        if builder_consciousness < blueprint.consciousness_required:
            return False, f"Requires consciousness level {blueprint.consciousness_required:.1f}"
        
        # Check energy cost
        if self.total_energy < blueprint.energy_cost:
            return False, f"Requires {blueprint.energy_cost:.1f} energy (have {self.total_energy:.1f})"
        
        # Check prerequisites
        built_types = [s.blueprint.structure_type for s in self.built_structures if s.operational]
        for prereq in blueprint.prerequisite_structures:
            if prereq not in built_types:
                prereq_name = self.blueprints[prereq].name
                return False, f"Requires {prereq_name} to be built first"
        
        return True, "Can build"
    
    def start_construction(self, structure_type: StructureType, position: Tuple[float, float, float], 
                          builder_id: int, builder_consciousness: float) -> Optional[int]:
        """Start construction of a structure"""
        can_build, reason = self.can_build(structure_type, builder_consciousness)
        if not can_build:
            return None
        
        blueprint = self.blueprints[structure_type]
        
        # Deduct energy cost
        self.total_energy -= blueprint.energy_cost
        
        # Create the structure
        structure = BuiltStructure(
            blueprint=blueprint,
            position=position,
            builder_id=builder_id,
            completion_time=time.time() + blueprint.build_time,
            current_energy=blueprint.energy_cost,
            operational=False  # Not operational until construction complete
        )
        
        structure_id = self.structure_id_counter
        self.structure_id_counter += 1
        
        self.built_structures.append(structure)
        
        print(f"🏗️ ISO-{builder_id} started building {blueprint.name}")
        return structure_id
    
    def update(self, dt: float):
        """Update the ISO world building system"""
        current_time = time.time()
        
        # Check for completed constructions
        for structure in self.built_structures:
            if not structure.operational and current_time >= structure.completion_time:
                structure.operational = True
                print(f"✅ {structure.blueprint.name} construction complete!")
                
                # Add to civilization level
                self.civilization_level += 0.1
        
        # Update energy generation and consumption
        energy_generation = 0.0
        energy_consumption = 0.0
        consciousness_boost = 0.0
        data_flow = 0.0
        stability_bonus = 0.0
        
        for structure in self.built_structures:
            if structure.operational:
                structure.age += dt
                
                # Calculate efficiency (structures get better with age, up to a point)
                age_factor = min(1.5, 1.0 + structure.age / 100.0)  # 50% efficiency bonus over time
                
                energy_generation += structure.blueprint.provides_energy * age_factor
                consciousness_boost += structure.blueprint.provides_consciousness_boost * age_factor
                data_flow += structure.blueprint.provides_data_flow * age_factor
                stability_bonus += structure.blueprint.provides_stability * age_factor
                
                # Structures consume some maintenance energy
                energy_consumption += structure.blueprint.energy_cost * 0.001  # 0.1% per second
        
        # Update totals
        self.total_energy += (energy_generation - energy_consumption) * dt
        self.total_energy = max(0, self.total_energy)  # Can't go negative
        
        self.total_data_flow = data_flow
        self.world_stability = 1.0 + stability_bonus * 0.1
        
        # Natural energy regeneration (ISOs are resourceful)
        self.total_energy += self.energy_generation_rate * dt
    
    def get_consciousness_boost_at(self, position: Tuple[float, float, float]) -> float:
        """Get consciousness boost at a specific location"""
        total_boost = 0.0
        x, y, z = position
        
        for structure in self.built_structures:
            if not structure.operational:
                continue
                
            sx, sy, sz = structure.position
            distance = math.sqrt((x - sx)**2 + (z - sz)**2)  # 2D distance
            
            if distance <= structure.blueprint.affects_radius:
                # Boost decreases with distance
                distance_factor = 1.0 - (distance / structure.blueprint.affects_radius)
                boost = structure.blueprint.provides_consciousness_boost * distance_factor
                total_boost += boost
        
        return total_boost
    
    def get_nearby_structures(self, position: Tuple[float, float, float], radius: float) -> List[BuiltStructure]:
        """Get structures within radius of position"""
        nearby = []
        x, y, z = position
        
        for structure in self.built_structures:
            sx, sy, sz = structure.position
            distance = math.sqrt((x - sx)**2 + (z - sz)**2)
            
            if distance <= radius:
                nearby.append(structure)
        
        return nearby
    
    def suggest_next_build(self, iso_consciousness: float, iso_position: Tuple[float, float, float]) -> Optional[StructureType]:
        """Suggest what an ISO should build next based on current world state"""
        
        # Priority system based on civilization needs
        priorities = []
        
        # Count existing structures
        structure_counts = {}
        for struct_type in StructureType:
            structure_counts[struct_type] = sum(1 for s in self.built_structures 
                                              if s.blueprint.structure_type == struct_type and s.operational)
        
        # Basic infrastructure first
        if structure_counts[StructureType.POWER_NODE] == 0:
            priorities.append((StructureType.POWER_NODE, 10.0))
        elif structure_counts[StructureType.DATA_CONDUIT] < 2:
            priorities.append((StructureType.DATA_CONDUIT, 9.0))
        elif structure_counts[StructureType.MEMORY_BANK] == 0:
            priorities.append((StructureType.MEMORY_BANK, 8.0))
        
        # Residential needs
        if structure_counts[StructureType.ISO_DWELLING] < len(self.built_structures) // 3:
            priorities.append((StructureType.ISO_DWELLING, 7.0))
        
        # Community development
        if structure_counts[StructureType.CLUSTER_HUB] == 0 and structure_counts[StructureType.ISO_DWELLING] > 0:
            priorities.append((StructureType.CLUSTER_HUB, 6.0))
        
        # Industrial development
        if structure_counts[StructureType.PROCESS_FACILITY] == 0 and self.civilization_level > 1.0:
            priorities.append((StructureType.PROCESS_FACILITY, 5.0))
        
        # Cultural advancement
        if structure_counts[StructureType.WISDOM_SPIRE] == 0 and iso_consciousness > 0.7:
            priorities.append((StructureType.WISDOM_SPIRE, 4.0))
        
        # Advanced structures for highly conscious ISOs
        if iso_consciousness > 0.8:
            if structure_counts[StructureType.CREATION_FORGE] == 0:
                priorities.append((StructureType.CREATION_FORGE, 3.0))
            
            if structure_counts[StructureType.TRANSCENDENCE_TEMPLE] == 0 and iso_consciousness > 0.9:
                priorities.append((StructureType.TRANSCENDENCE_TEMPLE, 2.0))
        
        # Filter by what can actually be built
        buildable_priorities = []
        for struct_type, priority in priorities:
            can_build, _ = self.can_build(struct_type, iso_consciousness)
            if can_build:
                buildable_priorities.append((struct_type, priority))
        
        if not buildable_priorities:
            return None
        
        # Return highest priority buildable structure
        buildable_priorities.sort(key=lambda x: x[1], reverse=True)
        return buildable_priorities[0][0]
    
    def get_world_stats(self) -> Dict[str, float]:
        """Get current world statistics"""
        operational_structures = [s for s in self.built_structures if s.operational]
        
        return {
            "total_energy": self.total_energy,
            "energy_generation": sum(s.blueprint.provides_energy for s in operational_structures),
            "total_data_flow": self.total_data_flow,
            "civilization_level": self.civilization_level,
            "world_stability": self.world_stability,
            "total_structures": len(operational_structures),
            "consciousness_field": sum(s.blueprint.provides_consciousness_boost for s in operational_structures)
        }
