#!/usr/bin/env python3
"""
🎮 FLYNN 4D TEST - Minimal test for the 4D rendering system
"""

import pygame
import math
import time

# Test the basic 4D camera system
def test_4d_camera():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Flynn 4D Camera Test")
    clock = pygame.time.Clock()
    
    # Camera state
    camera_mode = "third_person"
    player_x, player_y, player_z = 0.0, 0.0, 0.0
    camera_distance = 50.0
    camera_angle_h, camera_angle_v = 0.0, 20.0
    fp_yaw, fp_pitch = 0.0, 0.0
    
    def project_3d_to_2d(x, y, z):
        """Simple 3D to 2D projection"""
        if camera_mode == "first_person":
            cam_x, cam_y, cam_z = player_x, player_y + 2.0, player_z
            yaw, pitch = math.radians(fp_yaw), math.radians(fp_pitch)
        else:
            yaw = math.radians(camera_angle_h)
            pitch = math.radians(camera_angle_v)
            cam_x = player_x + camera_distance * math.cos(pitch) * math.sin(yaw)
            cam_y = player_y + camera_distance * math.sin(pitch) + 10.0
            cam_z = player_z + camera_distance * math.cos(pitch) * math.cos(yaw)
        
        rel_x, rel_y, rel_z = x - cam_x, y - cam_y, z - cam_z
        
        # Simple perspective
        if rel_z <= 1.0:
            rel_z = 1.1
        
        screen_x = int(400 + (rel_x * 300 / rel_z))
        screen_y = int(300 - (rel_y * 300 / rel_z))
        
        return screen_x, screen_y
    
    print("🎮 4D Camera Test - Press F to switch camera modes")
    print("WASD to move, Mouse to look around")
    
    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    camera_mode = "first_person" if camera_mode == "third_person" else "third_person"
                    print(f"🎥 Switched to {camera_mode}")
        
        keys = pygame.key.get_pressed()
        mouse_rel = pygame.mouse.get_rel()
        
        # Movement
        speed = 30.0
        if keys[pygame.K_w]:
            player_z += speed * dt
        if keys[pygame.K_s]:
            player_z -= speed * dt
        if keys[pygame.K_a]:
            player_x -= speed * dt
        if keys[pygame.K_d]:
            player_x += speed * dt
        if keys[pygame.K_SPACE]:
            player_y += speed * dt
        if keys[pygame.K_LSHIFT]:
            player_y -= speed * dt
        
        # Camera controls
        if camera_mode == "first_person":
            fp_yaw += mouse_rel[0] * 0.1
            fp_pitch -= mouse_rel[1] * 0.1
            fp_pitch = max(-90, min(90, fp_pitch))
        else:
            camera_angle_h += mouse_rel[0] * 0.3
            camera_angle_v += mouse_rel[1] * 0.3
            camera_angle_v = max(-80, min(80, camera_angle_v))
        
        # Render
        screen.fill((0, 0, 20))
        
        # Draw simple grid
        for i in range(-100, 101, 20):
            # X lines
            start = project_3d_to_2d(i, 0, -100)
            end = project_3d_to_2d(i, 0, 100)
            pygame.draw.line(screen, (0, 100, 150), start, end, 1)
            
            # Z lines  
            start = project_3d_to_2d(-100, 0, i)
            end = project_3d_to_2d(100, 0, i)
            pygame.draw.line(screen, (0, 100, 150), start, end, 1)
        
        # Draw player
        player_screen = project_3d_to_2d(player_x, player_y, player_z)
        pygame.draw.circle(screen, (255, 255, 255), player_screen, 8)
        
        # Draw some test objects
        for i in range(-50, 51, 25):
            for j in range(-50, 51, 25):
                if i != 0 or j != 0:
                    obj_screen = project_3d_to_2d(i, 10, j)
                    pygame.draw.circle(screen, (255, 100, 100), obj_screen, 4)
        
        # HUD
        font = pygame.font.Font(None, 24)
        mode_text = font.render(f"Camera: {camera_mode}", True, (255, 255, 0))
        screen.blit(mode_text, (10, 10))
        
        pos_text = font.render(f"Pos: ({player_x:.1f}, {player_y:.1f}, {player_z:.1f})", True, (255, 255, 255))
        screen.blit(pos_text, (10, 35))
        
        pygame.display.flip()
    
    pygame.quit()
    print("✅ 4D Camera test complete!")

if __name__ == "__main__":
    test_4d_camera()
