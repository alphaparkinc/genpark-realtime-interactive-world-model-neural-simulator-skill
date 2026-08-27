from client import RealtimeInteractiveWorldModelNeuralSimulatorClient

def main():
    client = RealtimeInteractiveWorldModelNeuralSimulatorClient()
    res = client.simulate_interactive_world_step('ROTATE_CAMERA_RIGHT_CAST_FIREBALL_SPELL', 32)
    print('World Step ID: ' + res['world_frame_step_id'] + ' | Action: ' + res['action_applied'])
    print('Framerate: ' + str(res['rendering_framerate_fps']) + ' FPS (Latency: ' + str(res['latent_diffusion_step_latency_ms']) + 'ms)')
    print('Physics Consistency: ' + str(res['voxel_physics_consistency_score_pct']) + '% | Dynamic Lighting: ' + str(res['dynamic_lighting_propagated']))
    print('Live Stream URL: ' + res['h265_video_frame_stream_url'])

if __name__ == '__main__':
    main()
