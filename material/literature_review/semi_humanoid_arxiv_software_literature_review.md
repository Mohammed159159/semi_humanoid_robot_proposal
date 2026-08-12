# Software Architecture Literature Review: State-of-the-Art in Semi-Humanoid & Mobile Manipulation Robotics

**Author**: Senior Robotics & AI Software Group  
**Scope**: 2022–2026 Technological Breakthroughs, Software Stack Taxonomy, Middleware Protocols, VLA Models, and Real-Time Safety Watchdogs  
**Primary Focus**: High-Level Cognitive AI (OpenVLA/JEPA-WAM), Nav2 + MoveIt 2 Bimanual Planning, `ros2_control`, `rmw_zenoh` Middleware, 1 kHz MCU Safety Watchdogs, and Isaac Sim OpenUSD Digital Twins  

---

## 1. Executive Summary

As robotic systems transition from single-purpose industrial arms to general-purpose **semi-humanoid mobile manipulators**, the software architecture must solve a fundamental challenge: **bridging non-deterministic high-level AI reasoning with hard real-time deterministic low-level motor execution**.

Recent advances in **Vision-Language-Action (VLA) models** (e.g., OpenVLA, JEPA-WAM), **ROS 2 Navigation2 (Nav2)**, **MoveIt 2**, **`ros2_control`**, **Zenoh middleware (`rmw_zenoh`)**, **Variable Impedance Diffusion Policies (VIDP)**, and **NVIDIA Isaac Sim (Isaac Lab / EsaacSim)** enable unified physical AI pipelines.

This literature review evaluates state-of-the-art software frameworks across five technical pillars, establishes a comparative software taxonomy, identifies **five critical software literature gaps**, and derives concrete software design recommendations for our **Modular Semi-Humanoid Proposal**.

---

## 2. Multi-Rate Software Stack Taxonomy

Modern semi-humanoid software architectures enforce a **Multi-Rate Decoupled Pipeline**, separating high-latency cognitive reasoning from microsecond-level motor control:

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                             MULTI-RATE SOFTWARE ARCHITECTURE                             │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ COGNITIVE & PERCEPTION LAYER (5–10 Hz - Edge GPU / NVIDIA Jetson Orin AGX)               │
│   • OpenVLA (7B Llama 2 + SigLIP + DINOv2) / Panorama-Aware VLA (arXiv:2608.02257)       │
│   • JEPA-WAM: Joint-Embedding Prediction World-Action Models (arXiv:2608.10780)           │
│   • OpenVLA-OFT (Optimized Fine-Tuning with 26x inference acceleration) (arXiv:2502.19645)  │
│   • Semantic Perception: 3D Gaussian Splatting Grounding (arXiv:2608.10756) + YOLOv11    │
│   • Natural Language Speech Understanding: Whisper STT ➔ Goal Primitives                 │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ TASK ORCHESTRATION & MID-LEVEL PLANNING LAYER (30–100 Hz - Host CPU)                     │
│   • Mission Sequencing: ROS 2 BehaviorTree.CPP / Generative Finite State Machines        │
│   • Base Locomotion: ROS 2 Nav2 (2D/3D Costmaps, DWB / MPPI Local Planner, SLAM)         │
│   • Bimanual Manipulation: ROS 2 MoveIt 2 (IK Solvers, OPL Collision Avoidance)           │
│   • Coupled Whole-Body Kinematics: Kinematically-Coupled SVSDF MPC (arXiv:2608.07005)    │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ REAL-TIME FRAMEWORK & COMMUNICATIONS LAYER (100–500 Hz - Middleware)                      │
│   • Hardware Abstraction: ros2_control (HardwareInterface, JointTrajectoryController)     │
│   • Network Communications: Zenoh (`rmw_zenoh`) Zero-Copy Shared Memory IPC              │
│   • LiDAR-Inertial Odometry: Numerically-Robust ROS 2 iG-LIO Port (arXiv:2607.09947)       │
│   • Facility Integration: WMS / IoT Wireless Telemetry, TCP Camera Streaming, QML GUIs  │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ HARD REAL-TIME CONTROL & SAFETY REFLEX LAYER (1,000 Hz - Bare-Metal MCU / PREEMPT_RT)   │
│   • Decoupled MCU Execution: FreeRTOS / Zephyr on STM32H7 running FOC & Impedance Loops  │
│   • Variable Impedance Policies: VIDP Diffusion Compliant Control (arXiv:2608.06210)     │
│   • Firmware Safety Watchdog: Independent deadline monitor & FSR force threshold veto    │
│   • Telemetry & Command Sync: micro-ROS Budget-Based Executor (arXiv:2105.05590)        │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Systematic Review Across Software Pillars

### Pillar 1: High-Level Cognitive AI & Vision-Language-Action (VLA) Models
* **OpenVLA Architecture** (*Kim et al., 2024*) [[2406.09246]](https://arxiv.org/abs/2406.09246): Built on a 7B Llama 2 backbone fused with DINOv2 and SigLIP vision encoders, pretrained on 970k episodes from the Open X-Embodiment dataset.
* **Panorama-Aware VLA for Mobile Manipulation** (*Yang et al., 2026*) [[2608.02257]](https://arxiv.org/abs/2608.02257): Integrates panoramic visual streams with whole-body teleoperation, enabling mobile manipulators to orient vision dynamically while predicting 7-DoF delta actions.
* **JEPA-WAM (World-Action Models)** (*Liu et al., 2026*) [[2608.10780]](https://arxiv.org/abs/2608.10780): Introduces Joint-Embedding Predictive Architectures (JEPA) into World-Action Models, predicting stage-level visual outcomes for complex multi-step manipulation tasks.
* **Open-Vocabulary 3D Gaussian Splatting Grounding** (*Ou et al., 2026*) [[2608.10756]](https://arxiv.org/abs/2608.10756): Uses semantic 3D Gaussian Splatting to ground open-vocabulary natural language targets directly into 3D bounding spaces for mobile picking.

### Pillar 2: Navigation (Nav2) & Whole-Body Manipulation (MoveIt 2) Planning
* **Kinematically-Coupled SVSDF MPC** (*Li et al., 2026*) [[2608.07005]](https://arxiv.org/abs/2608.07005): Solves real-time whole-body motion planning for mobile manipulators carrying arbitrarily shaped payloads by coupling base velocity and arm joint limits in a Signed Distance Field (SDF).
* **Autonomous Locomotion (Nav2)**: ROS 2 Navigation2 handles base SLAM, global route generation, and local obstacle avoidance using Model Predictive Path Integral (MPPI) planners.
* **Bimanual Manipulation (MoveIt 2)**: Computes collision-free inverse kinematics (IK) for dual 6-7 DoF arms, integrating the mobile base as a virtual 3-DOF joint ($x, y, \theta$) into the MoveIt SRDF kinematic model.
* **Agentic Skill Distillation (RoboReact)** (*He et al., 2026*) [[2608.03387]](https://arxiv.org/abs/2608.03387): Distills generalizable whole-body manipulation skills from egocentric video demonstrations into executable ROS 2 action graphs.

### Pillar 3: Real-Time Frameworks (`ros2_control`) & Zenoh Middleware
* **`ros2_control` Abstraction Layer**: Standardizes joint state publishing (`joint_state_broadcaster`) and effort/position command distribution across heterogeneous actuators (VESC, ODrive, servo drives).
* **Zenoh Middleware (`rmw_zenoh`)**: Replaces traditional DDS protocols. Zenoh provides zero-copy shared-memory transport locally and high-efficiency publish/sub over lossy wireless networks.
* **Robust ROS 2 iG-LIO Odometry** (*Carvalho et al., 2026*) [[2607.09947]](https://arxiv.org/abs/2607.09947): Provides a numerically robust ROS 2 port of incremental GICP LiDAR-Inertial Odometry, ensuring drift-free mobile base SLAM.

### Pillar 4: Low-Level Control, Firmware & Safety Watchdogs
* **Variable Impedance Diffusion Policy (VIDP)** (*Khalil et al., 2026*) [[2608.06210]](https://arxiv.org/abs/2608.06210): Generates compliant, variable impedance control trajectories from human demonstrations, allowing the robot to dynamically adjust stiffness during contact-rich assembly.
* **Decoupled 1 kHz Control Loops** (*arXiv:2105.05590*): High-frequency impedance and joint control run directly on bare-metal MCU microcontrollers (FreeRTOS/Zephyr on STM32) **decoupled from micro-ROS callbacks** to avoid microsecond DDS jitter.
* **Conformal Whole-Body Touch Skin** (*Chen et al., 2026*) [[2608.02080]](https://arxiv.org/abs/2608.02080): 3D-printed Electrical Impedance Tomography (EIT) soft tactile skin providing geometry-scalable collision sensing across the robot's entire shell.

### Pillar 5: Digital Twin Simulation in NVIDIA Isaac Sim & OpenUSD
* **OpenUSD Parametric Scene Modeling**: Uses Universal Scene Description (OpenUSD) in Isaac Sim / Isaac Lab (*arXiv:2403.07257*) for procedural environment generation and sensor simulation.
* **EsaacSim Add-on for Isaac Sim** (*Bugueno-Cordova et al., 2026*) [[2608.08522]](https://arxiv.org/abs/2608.08522): Integrates event cameras and dynamic sensor models into NVIDIA Isaac Sim for ultra-fast visual servoing validation.

---

## 4. Deep Analysis of Software Literature Gaps

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                            FIVE CRITICAL SOFTWARE LITERATURE GAPS                        │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Asynchronous Disconnect: VLA Inference (5–10 Hz) vs. Hard Real-Time Motor Loops (1kHz)│
│ 2. Nav2 Base Motion & MoveIt 2 Arm Kinematic Coupling Bottlenecks                       │
│ 3. Micro-ROS Jitter in High-Frequency (500Hz+) Real-Time Impedance Control Loops         │
│ 4. Lack of Standardized ROS 2 Containerized Deployment Pipelines (Cloud to Edge)        │
│ 5. Vulnerability of End-to-End VLA Policies to Unseen Contact Force Perturbations        │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

### Gap 1: Asynchronous Disconnect (VLA to Real-Time Control)
* **The Problem**: OpenVLA and JEPA-WAM model inference outputs actions at 5–10 Hz. However, safe contact manipulation requires joint effort adjustment at 1,000 Hz (1 kHz).
* **Literature Deficit**: Most VLA papers execute raw low-frequency action steps without an intermediate **trajectory interpolator and variable impedance filter (VIDP)** to bridge the rate disparity safely.

### Gap 2: Nav2 & MoveIt 2 Kinematic Coupling Bottlenecks
* **The Problem**: Running Nav2 for the base and MoveIt 2 for arms as separate ROS 2 stacks causes jerky "stop-then-arm-move" behavior.
* **Literature Deficit**: There is a lack of open-source ROS 2 packages providing seamless, continuous whole-body trajectory generation (like SVSDF MPC) that co-optimizes base velocity and arm joint acceleration during active movement.

### Gap 3: Micro-ROS Jitter in 1 kHz Control Loops
* **The Problem**: Relying directly on micro-ROS callbacks for 1kHz motor loops introduces nondeterministic timing jitter caused by XRCE-DDS serialization overhead.
* **Literature Deficit**: Standard micro-ROS documentation recommends running 1kHz control inside micro-ROS threads, whereas empirical literature proves hard real-time loops must be decoupled into native MCU RTOS tasks.

### Gap 4: Lack of Standardized Cloud-to-Edge Containerized Deployment
* **The Problem**: Transitioning software from simulation (Isaac Sim / EsaacSim) to physical hardware suffers from dependency breakages.
* **Literature Deficit**: Publications rarely provide open-source Docker/Apptainer deployment specifications specifying how VLA containers, MoveIt 2 nodes, and `ros2_control` drivers are packaged and updated via Over-The-Air (OTA) pipelines.

### Gap 5: Vulnerability of Pure VLA Policies to Force Spikes
* **The Problem**: End-to-end VLA models rely purely on visual inputs and can generate dangerous motor commands if visual occlusion occurs during object grasping.
* **Literature Deficit**: Lack of a standardized **tactile-force veto node** in `ros2_control` that overrides VLA outputs when contact forces exceed safety limits.

---

## 5. Direct Proposal System Design Recommendations

Our semi-humanoid proposal directly addresses these five software gaps:

1. **Multi-Rate Control Architecture (Addressing Gap 1)**:
   - Implement an intermediate **ROS 2 Joint Trajectory Interpolator** that receives 10 Hz OpenVLA target deltas and generates smooth cubic spline trajectories evaluated at 1 kHz by `ros2_control`.
2. **BehaviorTree.CPP Whole-Body Coordinator (Addressing Gap 2)**:
   - Structure high-level autonomy using `BehaviorTree.CPP`, dynamically switching between Nav2 coarse base positioning and MoveIt 2 fine bimanual manipulation while leveraging SVSDF whole-body MPC.
3. **Decoupled Bare-Metal MCU Firmware (Addressing Gap 3)**:
   - Run 1 kHz motor commutation and variable impedance loops (VIDP) natively on STM32 FreeRTOS tasks, using micro-ROS strictly as an asynchronous telemetry and parameter bridge.
4. **Siemens VPC Containerized OTA Deployment (Addressing Gap 4)**:
   - Package high-level AI (OpenVLA, JEPA-WAM, YOLOv11, SAM), MoveIt 2, Nav2, and `ros2_control` into validated Docker container images, enabling seamless deployment from Isaac Sim SIL to physical hardware.
5. **1 kHz Tactile FSR Impedance Veto (Addressing Gap 5)**:
   - Embed a real-time safety watchdog in the `ros2_control` hardware interface that continuously evaluates fingertip FSR pressure arrays and 3D EIT skin, immediately freezing VLA motion if contact forces exceed 25 N.

---

## 6. Primary Cited Software Literature Index

1. **Yang, D., Chen, H., & Chen, X. (2026)**. *Learning Panorama-Aware VLA for Mobile Manipulation with Whole-Body Teleoperation*. arXiv: [2608.02257](https://arxiv.org/abs/2608.02257).
2. **Liu, X., Yang, Y., & Wang, X. (2026)**. *JEPA-WAM: Stage-Level Joint-Embedding Prediction for World-Action Models in Robot Manipulation*. arXiv: [2608.10780](https://arxiv.org/abs/2608.10780).
3. **Ou, H., Song, D., & Wang, Y. (2026)**. *Embodied Multimodal Grounding for Open-Vocabulary Mobile Manipulation via Semantic 3D Gaussian Splatting*. arXiv: [2608.10756](https://arxiv.org/abs/2608.10756).
4. **Li, Y., Yin, L., & Zhang, T. (2026)**. *Real-time Whole-Body Motion Planning for Mobile Manipulators Carrying Arbitrarily Shaped Payloads via Kinematically-Coupled SVSDF*. arXiv: [2608.07005](https://arxiv.org/abs/2608.07005).
5. **Khalil, H., Fernandes, N., & Kwok, T. M. (2026)**. *VIDP: Variable Impedance Diffusion Policy for Compliant Robot Manipulation from Diverse Demonstrations*. arXiv: [2608.06210](https://arxiv.org/abs/2608.06210).
6. **Chen, H., Kohlbrenner, C., & Kubik, J. (2026)**. *Toward Geometry-Scalable Whole-Body Touch for Humanoids: A 3D-Printed Conformal EIT Skin*. arXiv: [2608.02080](https://arxiv.org/abs/2608.02080).
7. **Bugueno-Cordova, I., et al. (2026)**. *EsaacSim: A Multimodal Event Camera Add-on for NVIDIA Isaac Sim*. arXiv: [2608.08522](https://arxiv.org/abs/2608.08522).
8. **Carvalho, A. E., Portugal, D., & Peixoto, P. (2026)**. *A Numerically-Robust ROS 2 Port of iG-LIO: Diagnosing and Fixing Toolchain-Induced Failures in Incremental GICP LiDAR-Inertial Odometry*. arXiv: [2607.09947](https://arxiv.org/abs/2607.09947).
9. **Kim, M. J., et al. (2024)**. *OpenVLA: An Open-Source Vision-Language-Action Model*. arXiv: [2406.09246](https://arxiv.org/abs/2406.09246).
10. **Kim, M. J., et al. (2025)**. *Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success*. arXiv: [2502.19645](https://arxiv.org/abs/2502.19645).
11. **Stoufs, N., et al. (2021)**. *Budget-Based Real-Time Executor for Micro-ROS*. arXiv: [2105.05590](https://arxiv.org/abs/2105.05590).
12. **Mittal, M., et al. (2024)**. *Isaac Lab: High-Performance Robot Learning Framework Built on NVIDIA Isaac Sim*. arXiv: [2403.07257](https://arxiv.org/abs/2403.07257).
