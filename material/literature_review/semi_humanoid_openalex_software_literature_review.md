# OpenAlex Scholarly Software Literature Review: State-of-the-Art in Semi-Humanoid & Mobile Manipulation Robotics

**Author**: Senior Robotics & AI Software Group  
**Data Source**: OpenAlex Global Scholarly Database (Peer-Reviewed Journals, IEEE/ACM Conferences, Repositories, and DOIs)  
**Scope**: 2022–2026 Technological Breakthroughs, Software Stack Taxonomy, Middleware Protocols, VLA Models, and Real-Time Safety Watchdogs  
**Primary Focus**: High-Level Cognitive AI (OpenVLA/PCO Frameworks), Behavior Trees, ROS 2 Nav2 + MoveIt 2 Bimanual Planning, `ros2_control`, `rmw_zenoh` Middleware, 1 kHz MCU Safety Watchdogs, and Isaac Sim OpenUSD Digital Twins  

---

## 1. Executive Summary & Scholarly Software Overview

Building reliable software for **semi-humanoid mobile manipulators** requires connecting non-deterministic high-level AI reasoning (5–10 Hz VLA models) with hard real-time deterministic low-level motor execution (1,000 Hz motor loops).

Querying the global **OpenAlex Database** across peer-reviewed publications (2022–2026) reveals how leading international labs structure this multi-rate pipeline using **ROS 2 (Jazzy/Humble)**, **Navigation2 (Nav2)**, **MoveIt 2**, **`ros2_control`**, **Zenoh middleware (`rmw_zenoh`)**, **BehaviorTree.CPP**, and **NVIDIA Isaac Sim digital twins**.

This literature review evaluates state-of-the-art software frameworks across five technical pillars, establishes a multi-rate software stack taxonomy, identifies **five critical software literature gaps**, and derives direct design recommendations for our **Modular Semi-Humanoid Proposal**.

---

## 2. Multi-Rate Software Stack Taxonomy

Modern peer-reviewed literature (*Bonci et al., 2023; Iovino et al., 2022*) enforces a **Multi-Rate Decoupled Pipeline**, separating high-latency cognitive reasoning from microsecond-level motor control:

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                             MULTI-RATE SOFTWARE ARCHITECTURE                             │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ COGNITIVE & PERCEPTION LAYER (5–10 Hz - Edge GPU / NVIDIA Jetson Orin AGX)               │
│   • OpenVLA (7B Llama 2 + SigLIP + DINOv2) / OpenVLA-OFT (26x inference acceleration)      │
│   • Perception-Cognition-Operation (PCO) Multimodal Framework (Carvalho et al., 2026)     │
│   • Vision Perception: YOLOv11 (Bounding Box Detection) + Segment Anything (SAM Masks)  │
│   • Natural Language Speech Understanding: Whisper STT ➔ Goal Primitives                 │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ TASK ORCHESTRATION & MID-LEVEL PLANNING LAYER (30–100 Hz - Host CPU)                     │
│   • Mission Sequencing: ROS 2 BehaviorTree.CPP (Iovino et al., 2022, 262 Citations)       │
│   • Base Locomotion: ROS 2 Nav2 (2D/3D Costmaps, DWB / MPPI Local Planner, SLAM)         │
│   • Bimanual Manipulation: ROS 2 MoveIt 2 (IK Solvers, OPL Collision Avoidance)           │
│   • Software Reconfiguration & Lifecycle Management (Peldszus et al., 2023)              │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ REAL-TIME FRAMEWORK & COMMUNICATIONS LAYER (100–500 Hz - Middleware)                      │
│   • Hardware Abstraction: ros2_control (HardwareInterface, JointTrajectoryController)     │
│   • Network Communications: Zenoh (`rmw_zenoh`) Zero-Copy Shared Memory IPC              │
│   • Autonomous Pallet/Object Alignment Stack (Mökkönen et al., 2024)                      │
│   • Facility Integration: WMS / IoT Wireless Telemetry, TCP Camera Streaming, QML GUIs  │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ HARD REAL-TIME CONTROL & SAFETY REFLEX LAYER (1,000 Hz - Bare-Metal MCU / PREEMPT_RT)   │
│   • Decoupled MCU Execution: FreeRTOS / Zephyr on STM32H7 running FOC & Impedance Loops  │
│   • Dynamic Movement Primitives (DMP) Trajectory Execution (Saveriano et al., 2023)     │
│   • Firmware Safety Watchdog: Independent deadline monitor & FSR force threshold veto    │
│   • Telemetry & Command Sync: micro-ROS Budget-Based Executor (arXiv:2105.05590)        │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Systematic Review Across Software Pillars

### Pillar 1: High-Level Cognitive AI & Perception-Cognition-Operation (PCO)
* **Perception-Cognition-Operation (PCO) Architecture** (*Carvalho et al., 2026*, DOI: [10.20944/preprints202603.0528.v1](https://doi.org/10.20944/preprints202603.0528.v1)): Establishes a 3-tier framework for autonomous mobile navigation, decoupling visual perception, high-level semantic reasoning, and low-level motion operations.
* **OpenVLA Architecture** (*Kim et al., 2024*, DOI: [10.48550/arXiv.2406.09246](https://doi.org/10.48550/arXiv.2406.09246)): Maps RGB images and natural language instructions directly to 7-DoF joint delta actions. OpenVLA-OFT fine-tuning accelerates inference by 26x for on-device edge execution.

### Pillar 2: Navigation (Nav2), MoveIt 2 & Behavior Trees
* **Behavior Trees for Robot Autonomy** (*Iovino et al., 2022*, DOI: [10.1016/j.robot.2022.104096](https://doi.org/10.1016/j.robot.2022.104096), **262 citations**): Proves that Behavior Trees (BTs) provide modular reactivity and superior fault recovery over state machines in ROS 2 task execution.
* **ROS 2 Autonomy Frameworks Survey** (*Bonci et al., 2023*, DOI: [10.3390/app132312796](https://doi.org/10.3390/app132312796)): Surveys ROS 2 frameworks for mobile manipulation, highlighting how Nav2 for base motion and MoveIt 2 for arm IK are integrated via behavior tree action servers.

### Pillar 3: Real-Time Frameworks (`ros2_control`) & Zenoh Middleware
* **Software Reconfiguration in Robotics** (*Peldszus et al., 2023*, DOI: [10.48550/arXiv.2310.01039](https://doi.org/10.48550/arXiv.2310.01039)): Evaluates dynamic node reconfiguration and lifecycle management in ROS 2, enabling hot-swapping of controller nodes without rebooting the system.
* **`ros2_control` & Zenoh (`rmw_zenoh`)**: Standardizes joint effort/position command interfaces while Zenoh provides zero-copy shared memory locally and high-efficiency publish/sub over lossy wireless networks.

### Pillar 4: Low-Level Control, Firmware & Safety Watchdogs
* **Dynamic Movement Primitives (DMP)** (*Saveriano et al., 2023*, DOI: [10.1177/02783649231201196](https://doi.org/10.1177/02783649231201196), **216 citations**): Surveys DMPs for smooth trajectory generation, impedance adaptation, and real-time perturbation recovery.
* **Decoupled 1 kHz Control Loops**: Hard real-time motor loops execute natively on MCU firmware (FreeRTOS on STM32) decoupled from micro-ROS callbacks to eliminate DDS timing jitter.

### Pillar 5: Digital Twin Sim-to-Real Simulation
* **Digital Twins for Human-Robot Collaboration** (*Ramasubramanian et al., 2022*, DOI: [10.3390/app12104811](https://doi.org/10.3390/app12104811)): Reviews real-time physics simulation and digital twin synchronization for collision-free human-robot co-presence in NVIDIA Isaac Sim.

---

## 4. Deep Analysis of OpenAlex Software Literature Gaps

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                         FIVE SCHOLARLY SOFTWARE LITERATURE GAPS                          │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Asynchronous Rate Disconnect: VLA Inference (5–10 Hz) vs. Real-Time Motor Loops (1kHz)│
│ 2. Lack of Open-Source Behavior Tree Bimanual Recovery Libraries in ROS 2                │
│ 3. Micro-ROS Jitter in High-Frequency (500Hz+) Real-Time Impedance Control               │
│ 4. Lack of Standardized Cloud-to-Edge Containerized Deployment (Isaac Sim to Hardware)    │
│ 5. Vulnerability of Pure Vision VLA Policies to Unseen Contact Force Perturbations       │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

### Gap 1: Rate Disparity (VLA 10Hz vs. Real-Time 1kHz Motor Loops)
* **The Problem**: VLA inference outputs low-frequency actions (5–10 Hz). Contact manipulation requires joint effort adjustment at 1,000 Hz (1 kHz).
* **Literature Deficit**: Published literature executes raw low-frequency action steps without an intermediate **trajectory interpolator and variable impedance filter** to bridge the rate gap safely.

### Gap 2: Lack of Open-Source Bimanual Behavior Tree Recovery Libraries
* **The Problem**: While Behavior Trees are widely studied (*Iovino et al.*), published implementations focus on single-arm or single-base navigation.
* **Literature Deficit**: There is no open-source library of **bimanual fallback and recovery tree nodes** in ROS 2 for handling partial arm slip or obstacle blocking during active transport.

### Gap 3: Micro-ROS Callback Jitter in 1 kHz Loops
* **The Problem**: Relying directly on micro-ROS callbacks for 1kHz motor loops introduces nondeterministic timing jitter caused by XRCE-DDS serialization overhead.
* **Literature Deficit**: Standard micro-ROS documentation recommends running 1kHz control inside micro-ROS threads, whereas empirical literature proves hard real-time loops must be decoupled into native MCU RTOS tasks.

### Gap 4: Cloud-to-Edge Containerized Deployment Breakages
* **The Problem**: Transitioning software from simulation (Isaac Sim) to physical hardware suffers from dependency breakages ("works on my machine").
* **Literature Deficit**: Publications rarely provide open-source Docker/Apptainer deployment specifications detailing how VLA containers, MoveIt 2 nodes, and `ros2_control` drivers are packaged and updated via Over-The-Air (OTA) pipelines.

### Gap 5: VLA Blindness to Force Perturbations
* **The Problem**: End-to-end VLA models rely purely on visual inputs and generate dangerous motor commands if visual occlusion occurs during object grasping.
* **Literature Deficit**: Lack of a standardized **tactile-force veto node** in `ros2_control` that overrides VLA outputs when contact forces exceed safety limits.

---

## 5. Direct Proposal Software System Design Recommendations

1. **Multi-Rate Trajectory Interpolator (Addressing Gap 1)**:
   - Implement an intermediate **ROS 2 Joint Trajectory Interpolator** receiving 10 Hz OpenVLA target deltas and generating smooth cubic spline trajectories evaluated at 1 kHz by `ros2_control`.
2. **Standardized Bimanual BehaviorTree.CPP Engine (Addressing Gap 2)**:
   - Develop an open-source library of Behavior Tree recovery nodes for multi-floor navigation (Project 8), elevator/door operation, and bimanual object handover fallback.
3. **Decoupled Bare-Metal MCU Firmware (Addressing Gap 3)**:
   - Execute 1 kHz motor commutation and impedance loops natively on STM32 FreeRTOS tasks, using micro-ROS strictly as an asynchronous telemetry and parameter bridge.
4. **Siemens VPC Containerized OTA Deployment (Addressing Gap 4)**:
   - Package high-level AI (OpenVLA, YOLOv11, SAM), MoveIt 2, Nav2, and `ros2_control` into validated Docker container images, enabling seamless deployment from Isaac Sim SIL to physical hardware.
5. **1 kHz Tactile FSR Impedance Veto (Addressing Gap 5)**:
   - Embed a real-time safety watchdog in the `ros2_control` hardware interface that continuously evaluates fingertip FSR pressure arrays, immediately freezing VLA motion if contact forces exceed 25 N.

---

## 6. OpenAlex Scholarly Software Bibliography & DOIs

1. **Iovino, M., Scukins, E., Styrud, J., et al. (2022)**. *A survey of Behavior Trees in robotics and AI*. Robotics and Autonomous Systems, 154, 104096. DOI: [10.1016/j.robot.2022.104096](https://doi.org/10.1016/j.robot.2022.104096).
2. **Saveriano, M., Abu‐Dakka, F. J., & Kramberger, A. (2023)**. *Dynamic movement primitives in robotics: A tutorial survey*. The International Journal of Robotics Research (IJRR), 42(14), 1231–1262. DOI: [10.1177/02783649231201196](https://doi.org/10.1177/02783649231201196).
3. **Bonci, A., Gaudeni, F., & Giannini, M. (2023)**. *Robot Operating System 2 (ROS2)-Based Frameworks for Increasing Robot Autonomy: A Survey*. Applied Sciences, 13(23), 12796. DOI: [10.3390/app132312796](https://doi.org/10.3390/app132312796).
4. **Ramasubramanian, A. K., Mathew, R., & Kelly, M. (2022)**. *Digital Twin for Human–Robot Collaboration in Manufacturing: Review and Outlook*. Applied Sciences, 12(10), 4811. DOI: [10.3390/app12104811](https://doi.org/10.3390/app12104811).
5. **Carvalho, M. V. L., Yoshioka, L. R., & Justo, J. F. (2026)**. *A Survey-Driven Framework for Autonomous Mobile Robot Navigation Systems: The Perception–Cognition–Operation (PCO) Approach*. Preprints.org. DOI: [10.20944/preprints202603.0528.v1](https://doi.org/10.20944/preprints202603.0528.v1).
6. **Peldszus, S., Brugali, D., & Strüber, D. (2023)**. *Software Reconfiguration in Robotics*. arXiv: [2310.01039](https://arxiv.org/abs/2310.01039).
7. **Mökkönen, T. (2024)**. *Autonomous pallet picking using ROS2*. Tampere University Institutional Repository. URI: [trepo.tuni.fi:10024/154752](https://trepo.tuni.fi/handle/10024/154752).
8. **Kim, M. J., et al. (2024)**. *OpenVLA: An Open-Source Vision-Language-Action Model*. arXiv: [2406.09246](https://arxiv.org/abs/2406.09246).
9. **Stoufs, N., et al. (2021)**. *Budget-Based Real-Time Executor for Micro-ROS*. arXiv: [2105.05590](https://arxiv.org/abs/2105.05590).
