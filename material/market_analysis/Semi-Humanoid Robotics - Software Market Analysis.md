# **Semi-Humanoid Robotics Software Stack: Market Analysis and Technical Architecture Review**

## **Software Market Overview and Value Distribution**

Software and digital services represent the primary value-driver in the global mobile manipulator and semi-humanoid robotics market1. While mechanical frames and actuation assemblies continue to commoditize due to modular open-source CAD and off-the-shelf brushless motor designs, software intelligence dictates enterprise utility, task adaptability, and total cost of ownership (TCO)1. Recent industry estimates indicate that software components, middleware, and autonomous fleet management services account for approximately 67.17% of the total mobile robotics market valuation2.

  \[Global Mobile Robotics Market Value Split\]  
  \+-----------------------------------------------------------+  
  | Software & Ecosystem Services (\~67.17%)                   |  
  \+-----------------------------------------------------------+  
  | Physical Hardware & Mechanical Structures (\~32.83%)        |  
  \+-----------------------------------------------------------+

The expansion of semi-humanoid software is structured across three technological vectors:

> 1. **Transition from Rule-Based Scripting to Foundation Models**: Traditional robotics software relied on hardcoded state machines, predefined trajectory waypoints, and manual kinematic inverse solvers4. Modern platforms leverage Vision-Language-Action (VLA) models, Diffusion Policies, and Action Chunking Transformers (ACT) to execute zero-shot or few-shot spatial tasks3.  
> 2. **Convergence of Simulation and Hardware Frameworks**: High-fidelity GPU-accelerated simulators (e.g., NVIDIA Isaac Sim, MuJoCo) bridge the sim-to-real gap, allowing reinforcement learning (RL) policies and synthetic data generation to train embodied models across parallel environments6.  
> 3. **Deployment of Over-the-Air (OTA) and RaaS Frameworks**: Commercial operators rely on cloud connectivity and modular containerization (Docker, Kubernetes) to deliver OTA software updates, remote telemetry monitoring, and Robot-as-a-Service (RaaS) subscription capabilities1.

## **High-Level Software Architecture: Cognition, Planning, and AI Workflows**

High-level software orchestrates environment perception, natural language command interpretation, spatial mapping, trajectory generation, and multi-modal task execution4. Operating primarily on primary host processors (e.g., Intel NUC, x86 industrial PCs) paired with GPU AI accelerators (e.g., NVIDIA Jetson Orin NX, Jetson Thor), these systems manage asynchronous data streams across complex sensor suites4.

  \[High-Level Cognitive Layer\]  
    ├── Natural Language Pipeline (Whisper STT \-\> LLM/VLM Task Planner)  
    ├── Vision-Language-Action (VLA) & Imitation Learning (LeRobot / Diffusion Policy)  
    └── Spatial Intelligence (3D SLAM / nvblox / FoundationPose)  
         │  
  \[Middleware & Motion Generation Layer (ROS 2 / DDS)\]  
    ├── Nav2 (Dynamic Path Planning & Costmap2D)  
    └── MoveIt 2 / NVIDIA cuMotion (Collision-Aware Trajectory Generation)  
         │  
  \[Low-Level Deterministic Execution Layer (Real-Time Microcontrollers)\]  
    ├── RTOS / PREEMPT\_RT Kernel Execution (1 kHz)  
    ├── Bus Interfaces (EtherCAT @ 500 Hz / CAN-FD)  
    └── Active Impedance Control & Safe Rust Firmware

### **Middleware Backbone and DDS Communication**

The de facto standard for open-source and commercial semi-humanoid software is Robot Operating System 2 (ROS 2), operating on long-term support distributions such as Humble Hawksbill and Jazzy Jalisco4.

* **Data Distribution Service (DDS)**: ROS 2 replaces the legacy ROS 1 central master architecture with DDS middleware (e.g., Fast DDS, Cyclone DDS), providing zero-copy memory transfers, configurable Quality of Service (QoS) profiles, and peer-to-peer communication9.  
* **QoS Configuration for Robotics**: Sensor streams (e.g., RGB-D point clouds, stereo feeds) utilize *Best Effort* QoS with small queue depths to drop delayed frames, whereas joint state commands and emergency safety signals enforce *Reliable* QoS with deadline guarantees7.  
* **Containerized Deployment**: Applications are containerized using Docker micro-services, isolating dependency stacks (e.g., CUDA drivers, PyTorch runtime environments) and enabling modular OTA updates without risking system-level library corruption9.

### **Perception AI and Spatial Mapping Stack**

Modern semi-humanoid perception relies on GPU-accelerated vision pipelines to process 3D spatial geometry and identify unstructured objects5:

* **Accelerated 3D SLAM & Occupancy Mapping**: Algorithms such as NVIDIA cuVSLAM process multi-camera feeds to achieve visual-inertial odometry with sub-1% drift rates6. For dynamic obstacle representation, libraries like nvblox compute 3D Signed Distance Fields (TSDF/ESDF) directly from depth camera streams, constructing real-time occupancy grids up to 5 meters out6.  
* **6D Pose Estimation and Foundation Models**: Unstructured object grasping uses foundation models like FoundationPose and SyntheticaDETR6. These models perform zero-shot 6D pose estimation and tracking for novel, textureless, or glossy objects without requiring pre-trained target CAD meshes6.

### **Navigation and Motion Generation Pipelines**

* **Autonomous Navigation (Nav2)**: Base mobility relies on the ROS 2 Nav2 framework, integrating dynamic path planners (e.g., DWB Local Planner, TEB Local Planner) with global costmaps to handle crowded indoor traffic, narrow doorways, and dynamic human obstacles4.  
* **Arm Trajectory Optimization (MoveIt 2 & cuMotion)**: Arm motion planning uses MoveIt 2 alongside GPU-accelerated motion generators such as NVIDIA cuMotion5. cuMotion computes minimal-jerk, collision-free trajectories for multi-DOF serial arms in tens of milliseconds, filtering out self-collision and obstacles from real-time depth streams5.

### **Embodied AI, VLA Models, and Teleoperation Workflows**

The incorporation of generative AI and imitation learning has introduced end-to-end policy execution3:

* **Voice-to-Action Pipelines**: Multimodal command processing streams verbal audio through speech-to-text models (e.g., OpenAI Whisper), passing structured text into Vision-Language Models (VLMs)4. The VLM parses human intent and visual scene contexts into executable ROS 2 task primitives (e.g., pick\_object(apples), deliver\_to(counter))4.  
* **Imitation Learning Frameworks**: Ecosystems like Hugging Face's LeRobot enable open-source policies (e.g., Diffusion Policy, ACT) trained on human demonstration datasets3.  
* **Low-Latency VR Teleoperation**: High-quality dataset generation relies on Virtual Reality (VR) control interfaces3. Systems like Pollen Robotics Reachy 2 achieve immersive visual and spatial feedback with a glass-to-action latency of ![][image1], logging synchronized video, depth, and joint transformations directly into machine learning pipelines3.

## **Low-Level Software Architecture: Real-Time Firmware and Control Loops**

While high-level software plans tasks, low-level software executes deterministic control loops9. Operating on real-time microcontrollers (e.g., ARM Cortex-M7, STM32 series) or Linux kernels patched with PREEMPT\_RT, this layer communicates directly with motor drivers, joint encoders, and IMUs9.

### **Real-Time Operating Systems (RTOS) and Execution Timings**

Deterministic motor commutation and active impedance regulation require fixed execution schedules9. High-level OS latency variations (![][image2]–![][image3]) would cause severe instability or mechanical shudder during joint movement9. Low-level control operates within strict boundaries:  
![][image4]  
To maintain safe operations, low-level execution utilizes dedicated RTOS frameworks (e.g., FreeRTOS, Zephyr) or bare-metal C/Rust binaries, ensuring high-priority control tasks preempt all non-critical operations9.

### **Real-Time Industrial Fieldbuses**

Communication between the central compute unit and distributed joint actuators relies on high-bandwidth, deterministic fieldbuses9:

* **EtherCAT (Ethernet for Control Automation Technology)**: Used in advanced humanoid platforms (e.g., Pollen Robotics Reachy 2), EtherCAT streams cyclic process data at rates up to ![][image5]–![][image6] with microsecond jitter9. Master-slave topologies allow the central processor to read encoder positions, multi-axis torque values, and temperature readings while dispatching target current commands in a single frame9.  
* **CAN-FD (Controller Area Network Flexible Data-Rate)**: Serves as a standard alternative for cost-sensitive semi-humanoid hardware, increasing payload capacity from 8 bytes (legacy CAN) to 64 bytes per frame with bitrates up to ![][image7], sufficient for multi-joint trajectory execution9.

### **Safety-Critical Firmware and Active Impedance Control**

* **Safe Rust Firmware**: Modern low-level software stacks are increasingly migrating from C/C++ to Rust9. Rust’s compile-time memory safety guarantees eliminate null-pointer dereferences, data races, and buffer overflows in motor control routines9.  
* **Active Impedance and Torque Regulation**: Physical HRI requires joint torque control14. Low-level joint loops implement active impedance algorithms governed by:

![][image8]  
where joint stiffness (![][image9]) and damping (![][image10]) are dynamically adjusted14. If external force sensors detect unexpected physical contact with a human, the firmware overrides current commands within milliseconds to drop joint impedance, preventing injury or damage1.

* **Hardware Watchdogs**: Microcontroller watchdogs monitor communication pulse rates from the main compute host9. If ROS 2 crashes or a DDS link drops, the watchdog triggers a graceful dynamic brake within ![][image11]9.

## **Simulation Frameworks, Digital Twins, and Sim-to-Real Transfer**

Deploying semi-humanoid software directly to physical hardware risks damaging expensive transmissions during initial reinforcement learning policy iterations7. As a result, physics-based simulation environments form a fundamental part of the software development lifecycle7.

  \[Physics Simulation (NVIDIA Isaac Sim / MuJoCo)\]  
    ├── OpenUSD Scene Modeling & Robot URDF/MJCF Importing  
    ├── GPU-Accelerated Synthetic Sensor Generation (Depth, RGB, LiDAR)  
    └── Parallel Reinforcement Learning (Isaac Lab)  
         │  
         │ Sim-to-Real Domain Randomization  
         v  
  \[ROS 2 Bridge / OmniGraph Extension\]  
         │  
         v  
  \[Physical Robot Hardware Execution\]

### **Major Robotics Simulation Platforms**

| Simulation Engine | Primary Developer | Core Physics Backend | ROS 2 Integration Mechanism | Key Strengths in Semi-Humanoid Software | Citation |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **NVIDIA Isaac Sim / Isaac Lab** | NVIDIA | PhysX 5 / OpenUSD | Native ROS 2 Bridge (OmniGraph Nodes) | GPU acceleration, synthetic data generation, parallel RL policy training | 6 |
| **MuJoCo** | DeepMind / Google | Custom Convex Optimizer | ROS 2 wrapper nodes / C API | Accurate soft-body contact dynamics, ideal for tendon drives and compliant grasps | 8 |
| **Gazebo (Harmonic / Iconic)** | Open Robotics | Dart / Bullet / PhysX | ROS 2 ros\_gz bridge | Completely open-source, standard baseline for Nav2 and MoveIt 2 testing | 7 |

### **Sim-to-Real Pipeline and Synthetic Data Generation**

> 1. **Unified Robot Description Format (URDF) & OpenUSD**: Robot kinematic trees, joint limits, visual meshes, and inertial properties are defined in URDF or Universal Scene Description (OpenUSD) formats7.  
> 2. **Domain Randomization**: Simulation engines randomize visual textures, lighting, friction coefficients, joint masses, and latency during training15. This variability ensures deep neural network policies transfer seamlessly to physical hardware without overfitting to simulator artifacts15.  
> 3. **Synthetic Data Generation (SDG)**: Photorealistic simulators automatically annotate millions of depth frames, 3D bounding boxes, and segmentation masks, accelerating object-detection training without manual labeling costs6.

## **Software Benchmark Across Semi-Humanoid Platforms**

The table below contrasts high-level and low-level software stacks across prominent commercial and open-source semi-humanoid platforms:

| Software Architectural Layer | Hello Robot Stretch 4 | Pollen Robotics Reachy 2 | PAL Robotics TIAGo |
| :---- | :---- | :---- | :---- |
| **High-Level OS & Middleware** | Ubuntu 22.04 LTS, ROS 2 (Humble), Python SDK4 | Ubuntu 22.04 LTS, ROS 2, Python SDK9 | Ubuntu LTS, ROS / ROS 2 Dual Support17 |
| **Autonomous Navigation Engine** | ROS 2 Nav2, 2D/3D Costmaps, Base SLAM4 | ROS 2 Nav2, Holonomic Base Kinematics12 | PAL Navigation Stack, Laser/LiDAR SLAM17 |
| **Arm Manipulation Framework** | MoveIt 2, Cartesian End-Effector IK Solvers4 | MoveIt 2, Parallel Joint Kinematics Solvers9 | MoveIt / MoveIt 2, Whole-Body IK Planning18 |
| **AI / Embodied AI Toolchains** | VLM Grasping Demos, PyTorch, YOLOv8, ForceSight4 | Hugging Face LeRobot, Diffusion Policy, PyTorch3 | OpenCV, TensorFlow, ROS Perception Packages18 |
| **Teleoperation Capabilities** | Web-based Remote Interface, Dexterous VR Kit12 | Immersive VR Teleop (![][image1] latency), 3D Audio9 | Web / Joystick Teleop Frameworks18 |
| **Low-Level Control Loop Rate** | **![][image12]**–![][image13] Base/Arm Loops12 | ![][image5] High-Speed Deterministic Loop9 | ![][image14]–![][image6] Control Loops18 |
| **Low-Level Fieldbus Communication** | USB to Serial / CAN Internal Bus4 | EtherCAT Fieldbus Protocol9 | CAN-Bus / EtherCAT Industrial Bus18 |
| **Firmware Execution Stack** | Embedded C/C++ Microcontrollers4 | Safe Rust-Based Firmware Layer9 | C++ Real-Time Controllers (ros\_control)18 |

## **Strategic Recommendations for Software Deployment**

> 1. **Adopt Modular DDS Architecture**: Build software using ROS 2 with custom DDS QoS parameters, separating compute-heavy perception AI from core navigation and safety stacks7.  
> 2. **Standardize Low-Level Control on EtherCAT & Rust**: Use deterministic EtherCAT or CAN-FD communication loops running at ![][image15]9. Implementing firmware in Safe Rust guarantees memory security and prevents software crashes during physical human interaction9.  
> 3. **Establish Simulation-First Validation**: Conduct initial policy training, collision testing, and synthetic perception generation inside Isaac Sim or MuJoCo before deploying code to physical hardware7.  
> 4. **Incorporate Open Embodied AI Pipelines**: Align manipulation software with open-source machine learning pipelines (e.g., Hugging Face LeRobot)3. Capturing teleoperation datasets in standard formats ensures continuous policy improvements over time3.

#### **Works cited**

> 1. Mobile Manipulator Market Size, Share & Latest Trends \- MarketsandMarkets, [https://www.marketsandmarkets.com/Market-Reports/mobile-manipulator-market-167435958.html](https://www.marketsandmarkets.com/Market-Reports/mobile-manipulator-market-167435958.html)  
> 2. Mobile Robots Market Size, Trends & Forecast 2035 \- Roots Analysis, [https://www.rootsanalysis.com/mobile-robots-market](https://www.rootsanalysis.com/mobile-robots-market)  
> 3. Reachy 2: The Open-Source Humanoid Robot Redefining Human-Machine Interaction, [https://www.maxongroup.com/en-us/knowledge-and-support/blog/reachy-2-the-open-source-humanoid-robot-257768](https://www.maxongroup.com/en-us/knowledge-and-support/blog/reachy-2-the-open-source-humanoid-robot-257768)  
> 4. Stretch 4 by Hello Robot \- ui44, [https://ui44.com/robots/hello-robot-stretch-4](https://ui44.com/robots/hello-robot-stretch-4)  
> 5. Manipulation \- NVIDIA Isaac ROS, [https://nvidia-isaac-ros.github.io/concepts/manipulation/index.html](https://nvidia-isaac-ros.github.io/concepts/manipulation/index.html)  
> 6. NVIDIA Isaac AI robot development platform, [https://developer.nvidia.com/isaac](https://developer.nvidia.com/isaac)  
> 7. A Beginner's Guide to Simulating and Testing Robots with ROS 2 and NVIDIA Isaac Sim, [https://developer.nvidia.com/blog/a-beginners-guide-to-simulating-and-testing-robots-with-ros-2-and-nvidia-isaac-sim/](https://developer.nvidia.com/blog/a-beginners-guide-to-simulating-and-testing-robots-with-ros-2-and-nvidia-isaac-sim/)  
> 8. Robot Control Stack: A Lean Ecosystem for Robot Learning at Scale \- arXiv, [https://arxiv.org/html/2509.14932v1](https://arxiv.org/html/2509.14932v1)  
> 9. Reachy 2 Humanoid Robot Overview | PDF \- Scribd, [https://www.scribd.com/document/839112213/Reachy2-Dual-arms-Datasheet](https://www.scribd.com/document/839112213/Reachy2-Dual-arms-Datasheet)  
> 10. YousefSamm/Multi-Agent-Robotics-System-using-ROS2-Isaac-Sim \- GitHub, [https://github.com/YousefSamm/Multi-Agent-Robotics-System-using-ROS2-Isaac-Sim](https://github.com/YousefSamm/Multi-Agent-Robotics-System-using-ROS2-Isaac-Sim)  
> 11. Gemini 336 Powers Reachy 2 Embodied AI Robot \- ORBBEC, [https://www.orbbec.com/news/bringing-vision-to-embodied-ai-how-orbbecs-gemini-336-powers-reachy-2s-real-world-perception-across-top-global-research-labs/](https://www.orbbec.com/news/bringing-vision-to-embodied-ai-how-orbbecs-gemini-336-powers-reachy-2s-real-world-perception-across-top-global-research-labs/)  
> 12. \[Release information\] Stretch 3 | Latest model of mobile manipulator made by Hello Robot, [https://www.tegakari.net/en/2024/03/stretch3/](https://www.tegakari.net/en/2024/03/stretch3/)  
> 13. Pollen Robotics Reachy 2 Specs & Price | Humanoid.guide, [https://humanoid.guide/product/reachy-2/](https://humanoid.guide/product/reachy-2/)  
> 14. Reachy 2 \- Pollen Robotics, [https://www.pollen-robotics.com/wp-content/uploads/2025/02/Reachy2-Single-Arm-Datasheet.pdf](https://www.pollen-robotics.com/wp-content/uploads/2025/02/Reachy2-Single-Arm-Datasheet.pdf)  
> 15. (PDF) Sim-to-Real Transfer for Mobile Robots with Reinforcement Learning: from NVIDIA Isaac Sim to Gazebo and Real ROS 2 Robots \- ResearchGate, [https://www.researchgate.net/publication/387767755\_Sim-to-Real\_Transfer\_for\_Mobile\_Robots\_with\_Reinforcement\_Learning\_from\_NVIDIA\_Isaac\_Sim\_to\_Gazebo\_and\_Real\_ROS\_2\_Robots](https://www.researchgate.net/publication/387767755_Sim-to-Real_Transfer_for_Mobile_Robots_with_Reinforcement_Learning_from_NVIDIA_Isaac_Sim_to_Gazebo_and_Real_ROS_2_Robots)  
> 16. Reachy 2 \- Specifications & Quote \- RoboZaps, [https://robozaps.com/products/reachy-2](https://robozaps.com/products/reachy-2)  
> 17. The Design of Stretch: A Compact, Lightweight Mobile Manipulator for Indoor Human Environments \- PMC, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10710733/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10710733/)  
> 18. PAL Robotics TIAGo — New Unit \- BotMarket, [https://botmarket24.com/en/humanoid-robots/pal-robotics/pal-robotics-tiago/listing-9f4ae53a-5557-4b41-8102-cf0073dd2f4b/](https://botmarket24.com/en/humanoid-robots/pal-robotics/pal-robotics-tiago/listing-9f4ae53a-5557-4b41-8102-cf0073dd2f4b/)  
> 19. The Design of Stretch: A Compact, Lightweight Mobile Manipulator for Indoor Human Environments \- ResearchGate, [https://www.researchgate.net/publication/354776839\_The\_Design\_of\_Stretch\_A\_Compact\_Lightweight\_Mobile\_Manipulator\_for\_Indoor\_Human\_Environments](https://www.researchgate.net/publication/354776839_The_Design_of_Stretch_A_Compact_Lightweight_Mobile_Manipulator_for_Indoor_Human_Environments)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEkAAAAWCAYAAACMq7H+AAAAoklEQVR4Xu3VIQoCURhF4QcKg2iwaLBqsSizIF3BBBEMYjYYxB1YXILrECxTrQZltjCeAYNcBlQwOfeDky6v/OWFYGZmf6tDS7rQUDZDj260o75slbahjPY0kK3yYjoEH6fUmI50p61shhpdaUKRbCaKH2xNp+BjvdWmlGbUkM1eFIda0ZkS2Uw0aU4LaslmJeo0pa4OZmY/ln/R6PnGzD72AGphG/HtiSbgAAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEkAAAAZCAYAAAB9/QMrAAACrUlEQVR4Xu2XWahNURjHP3MoJSUPSillijJmfCCSlOGBlCdFlMR9ce8DkqkUImNkeDBkSvGCezOkCO9mDwoZQuSFxP9/v28563ztvZ1but229atf3fXfe52z77eGvY5IIpEoGcN9ENEb7oEfYBMcXX25/HSCS+Brf8HoCx/BK6LF2g6/w9nxTWXml+jseGJ/Z3ENfoO9ouw2fAW7RlnpqZfsIq0QzXe7fIHl+1xeavKKtF803+Dy6ZbfdHmpySvSZdGc12MmWc69KotZ8DH8AafC8fCk6BLdDNvDLnAH/AgvwpHNPSvMgHfgdbgLnoYLq+5oZfKKdEs0X+PyUKQvLg+MgmvhU3hEtAgjYE/RfhtFB2A5HApfiu6NfDGQMXbfHGvPs/ZiaxfCD3sPH4h26l99uYpTPiggr0gcReYNLp9geVafmL1wi8tCv/hFsM0y7oHkmLV3hhvANNFCF9JZ9GE7WnuIaMEG/rmjQjfRt1Kt5BXpvGQXKcwkLpUiuEw4W2LY753Ltlq+0trj4E/LeO9ZOMiuFbLIB6IP8EJ03QfaiY7g6ij7G3lFOiyar3P5FMu57xTBmbDUZez3xmWbLF8VZfyfnllOP0vxgbeZQz4whsGH8L7oPnAD3pWWnWHyisRCM+cBMoYHSebnXO5hv1qKxLcn8zCwg0VXA2F21a6fsSyX9T6I4AdyNLjEOOrhC2olr0jcVJkfdzn/cebLXO5p6Uyqs/Yl0c06wF8F9+DbKGt1joo+JIvimSj6Kp9r7QGi+wT3myL6iM6AA7CHZR1Ev4cn+LGWcQMPe18YDBaJ7YOwu+gR4qvU+Hb71/BBsvTLK8wcnrw/wROi55w8+FvQf+Zk+NxljRn3zYQX4HypLEP+VuRs437bpuknuudxRrX5h00kEolEIvFf8BvGpbunC7PtywAAAABJRU5ErkJggg==>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADMAAAAZCAYAAACclhZ6AAACeUlEQVR4Xu2WS6hNYRiGX5fcLwm5JBJyKfeSRPaA3ApFuUYoI2QghciEIhlRSBFTUWQgKWKACSJCdCK5DIQBReJ9fes/51vfXmefk8k+g/XUU/u77LXXt/f//2sDJSV1ZR3dEZNkI71Gv9J9tEO+3Da4SXfRJXQb/UM3+wayHzaEBu1N39ArtL3raRPo5r264Yjye1y8KssV9daVSkwUoBvvFXLv6E/aLeTrSiUmAkPpr5gkj2FDTo6FeqK9co5+pE9op3wZM+mXkBP3YcPMjQUyhD6i32E9O+kx+pA20JO0HWyvPoNdv4I8i+g9+pTepkfpglxHAd9gp9NwOhV2kwNdfSFqD7M2Fkg/upfegPVcgA2tpbopy52hu+lgOgI2+Gi9OUM98128gS5zcSFdQpwOAi0vMQ/Fw9yF9W2NBYcGVc/1kH9Lp4ec+g6E+DCd4HLj3OtWkYZZmsXTUDxM+mXWxIJjJazndMi/pgNCTn0HXfw7y8kP9LyrtRo9T3SBLVk8iv5oKjfyANZXax2nYU6F/EvYUvSo75CL58CGTgPJka5ehT5secilN67O4o5Z3LWxw3iV5bXZm0NrXD0nQv4FWh5Gn6dDYjzsH8ktVF8nxx3YPwBPGmZiyKU9lNCG1elUixX4/2EWu9dCw+m0bRadXoNc3Ae2P8a6nLgK28TpsDhL39O+qaGA7rDjVDepbzUxiX6GrYj0d6gnrO8ymoZUfJwOoz3oLFSvoio+0Uuwb0+vx+TL/9CQz2HPhCOwZ9KUXEceXSP9wkn977sYcg10RkHvetgS1emWlrNWQovo29Xe2Q47uZqjM50NewD2D7WSkpKSkhLPX6ngoW4/mDCTAAAAAElFTkSuQmCC>

[image4]: <data:image/png;base64,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>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADUAAAAWCAYAAABg3tToAAAC40lEQVR4Xu2WSchOYRTHj3nMEAtCIVkgUywQIb4MC1mYYoNsWChTsSBjiZSNpTULMiQkQ8aFIZEUspAyfRmTJPH/3/M89557vvu+b/dbUfdXv3qec573vveZr0hFxT/JIrjdB8EKeB4+hXtgh3w6oT28Cb/Cu3BZPt2CEfBPgYNFn+/j0YZch9vgArhO9Edbci1EtsJvcBVsgi/gVdjRtOkET8LZsCdcDb/DvaaNpyucDp+I/u9jOAN2hm1CjjL3Hs4K9Yb4UVibTyd/wvhuE5sfYutNjLPrR3F/QayIi6LtzvpEgLlnPliPh7AZ3oG7XI4cF33oRBNrJ7rE7od6W/gOfk5bKJOkXKdO+0SgdKdm+oAjziBf3HIrxMnyUL6SpRO6hbhdpkXETnH5FlG6U9xLR+Fr+Fx0nVv4wB8uRi5J1inuOZbPZekE7gvGB7q4p2ynuOfiYFtTuGR2wmFwNHwEh5g8G/OQ8NhO7QvlM1k6IXZqgot7ynaKg8QY/zeewqeytMghWxFtfNnVv5h65IJkneIzWM49OPAbzvVBR+xUPW2nRsFPoicu4dUR36UQHgBswCOZsNxopjaEcq2ZGuvinrIzNRQuDmXudeZrnZwJr0Qb7Qh1ln9l6ZRrknVqZShz9iw8IBgf5OKesp2ybBJ95z4xsAQuTdPKR9GH8CIm3HOsd09bKA9CnPC4Z/l2lk7oG+KcsXrEpXzCJwK1OjVc9IKfY4M3RD9rLHwA5aVLjoW6PTzIB9ERInzpt6Knp4VrP3a8Hq25p7js+O4tnj9e8sdtD/hT9NKM8IW5V3gHcbZYPyy6UQeYdpyVl6bOtrzLaD14kfMDgC/H78UxJsf/GhlyvNy5InjacbC4zxmfGtrmBp3fVByhI/ANHGeTgV6iH7KcCb4kv0Cm5FooHCTmD4q2vQf75Vrkae0H7YGCGE3pDRfCjXCyTTh4fE6Dm2F/l7PME/1AXgO7uFxFRcV/xF8MsO5XZUemxwAAAABJRU5ErkJggg==>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC0AAAAWCAYAAABUpxX0AAAB0ElEQVR4Xu2WTSttURjHH4TcriQzpRhct3wApESJmalMb6lrhBLfgA+gvMXMwMBIMiKllExJuYmBbpSUt6RI/B/rWfZaz9nnZW3FZP/q19nredY6/c86Z699iFJSgiiGQ7oYw1+4DHfhf9VzGYSvMR7Bnpi6lXMUxG+4QmZRPgbgBpm5t6rnUgs7YS+ZuUsyboHVct0NL+CWjNm8VMIXuEfRJy0E3o1Hyh3ahd93TBeFQzivi7kogT/k+pkKD808UFjoUV0UgkO7hOw0c0NhoUd0UfjS0Bz4Tq6nyL+ZOuwkITS0+16uGWRtZIF3mmVayazlDzEBq+wkIUnoSVgq41WpZZAktN3pfrgP66K2h94xrQ59DcudMc85dcYfJAnNNyOfPnxmF/ltj9Cd7pNXPqV2yOx0LElCc+B/ZNb98dseoaEt42TW1uiGJUnoS9hFZt0ZmXM/Du4P66JwAOd0ETSS+SZzZgoNfQ+P5XqazNrZqO3BvZBz2v4seN2M1PiZ4vGLotA/VS+ONvgEr5zaApn1J06tgsyjmeuLsN7plcFmeA7XYRNF9wVvCK9pl3ED3JTrd2xYrX1SarbJn7dG0ZFn5f8mn/nDpGvWlJSU7+YN1k+3q0CrvpMAAAAASUVORK5CYII=>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEEAAAAZCAYAAABuKkPfAAADJElEQVR4Xu2XWchNURTH/5QyhvAiHkwJJSEiJHN4MJTkQYqiZJaQ8mWK5IHyJt1CiZIhL0qfoUwPeFBkfCHxYCxCYv3vWsvZZ997js9N3Vv3/upfZ6+1zrlnr7322ucCDRrUCj1F40RLIntNMEe0MzYGHBD9CnQm7S7hFNLxBdHUyFZ1rou2Qie/EvpSHGfRXzRRtFz0SfRN1CMMiHiCZLKbRYPM3k10wuxVJ1wRalXanQmT4RPMu2cXkmdPiHwbzF51WJqVwCQ8hlYCJzIw7S7SW9QR2UnYaPaqMy02tBBPwnHoRJpSXmUL8pNQM5UwT3RU9BJa3u3T7kw8CbOgE+F1q1QEcB/pJIxPu7He7AtFN0UfRV+g/cIZKfpqcexVy0TvzXZI1D0JLTJD9FDULDooOpl2l+eDaAd0UkNFD0R9UhHlGQCdeBvRW5Su9GjRaVEn88V+ss7se6G/zyRyezJ53mxpv21xTNBl6EJ5E79ncWSU2RwucIsqrV009hceEdljPAlkDPSeNzZuLXomaov8JKwxewxPnZ9IFsMrZvefCKWv2T2uYONhHoAKe9476INWxI4I3w7OIyQTmi06Ytd5PSErCXeh9sU29oqJk0CeI4njYjB5jGV1shL9SP4nnkIfwqMtjzgJ25BMiM1yil3n9YS1Zo+5BrU32diTVS4JN0Tbg/FkJL9HcbvnskC0KLKxpHkzfzgPbgcmzPHS5OfwC+iWIJVsB68ENkGSl4RXSKp2MLRfDIFWzyWUf36KK6Jbke0H9MZJkT2GlcDTJOSqaU9gq6QS2PlZ1l1tnJUE+mnvZ+ML0GbosGnfCcZlYQPpFYy5avz4GRvYysFVPwZ9gc6BnUcbj7qQmUiSwEmH+OT2Q5NFzYcmt0sQt9rieDqcNRuPVSaq2YOgSWAcG2UH6Dw+B/5M2EDOiw6LXouGp90lxH+gqOmBf2lwvQmlsYXAz8ldhN5/DvqdwDM+TADxZO2zay4U35XP52o7/DPHLe6f89/x995WhCs5F7qH2F1rEd828XaoK/zzuq6TUIAmgVsm/kyuC9gv4r7SoEGDBv+d30AD8QQ8Rq+PAAAAAElFTkSuQmCC>

[image8]: <data:image/png;base64,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>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAABQUlEQVR4XmNgGAWjAAcoB+L/WHAlkpp9aHKTkORIBqUMEEOMgJgdTU4eiH8B8WogFkWTIxk8ZoBYhA52A7EiuiC5QIMBESwwAPLVQiBmRhKjGGQyQCy5AuVrA/F+ILaCq6ASWMsAsaifARJX36F8HWRFlAJ7BkSwXYKK1UP5H2CKqAEaGSCGngdiMaiYOBB/g4pTDRxhgBhYiyY+EyqOntTJAoJA/JsBYiB6xMNSYiKaOFlgGgPEMFBewQYqGCDykWjinUAsDMTngHgbVOwEEMfAVUABKDXBEgAyPoOk5h0WeVgqDGKAhMZfIHaDioH0ToSyqQq8gfgTEHMAMTcDpIgqRlFBJQAKvu1QdiADJJVKI6SpB04B8Xooez8DamlPNRAOxD+BmAVdgtpgMgOkjqIpmAXEL4D4CRBPQJMbBdQBAF7MUDUmb+BCAAAAAElFTkSuQmCC>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAABQUlEQVR4XmNgGAWjAAcoB+L/WHAlkpp9aHKTkORIBqUMEEOMgJgdTU4eiH8B8WogFkWTIxk8ZoBYhA52A7EiuiC5QIMBESwwAPLVQiBmRhKjGGQyQCy5AuVrA/F+ILaCq6ASWMsAsaifARJX36F8HWRFlAJ7BkSwXYKK1UP5H2CKCABQCr0PxO/QJZBBIwPE0PNALAYVEwfib1BxYsEiIN6FLogMjjBADKxFE58JFUdP6rjAdQZMM+BAEIh/M0AMRI94WEpMRBPHBiQYIGqt0SVgYBoDRAEor2ADFQwQ+Uh0CQZIwjkMxFxAfBKIl6NKQwAoNcESADI+g6QGFLHo8rBUaAjlm0H5V4E4C8qmKuhmgJQkMACyVBeJTzWwBohXIfGfAjETEPsgiVEF9AHxMihbAYg3MEASTzZMwSgYBQMDAAjIT7ai7NNfAAAAAElFTkSuQmCC>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEkAAAAZCAYAAAB9/QMrAAACwklEQVR4Xu2XW6hNURSGB5JQIiUPIsUDkdzvHogkcSgkb4oohBc8UHIrhci15JJIDifFi1sipfAs1xeFSJyOvJCO/zfGas89rLX29eHYza++2uufa+699thzjTW3SCQSaTBG+SCgHzwKv8B7cHzxcOPTFa6CH/yAMQC+gLdEi3UA/oQLw5MamXbR1fHKXqdxB/6AfYPsEXwPuwfZf0En+Aw+hSth5+LhXLZKepHWieZHXL7M8uMu77CwOAtEizPPjZVLVpFOiOY7XT7H8gcu75Csh8/hBTjSjVVCVpFuiuYcD5luOXtVGvPhS/gLzoJT4CXRW3SP6CrvBg/Cr/A6HPt3ZoG58DG8Dw/Dy3B50Rkl6CLabFmcIW6sGrKK9FA03+LypEhtLk8YB7fD1/CMaBHGwD6i83aJ/gBr4Qj4TrQ38sFAJth5TXa82I7ZRkrCBntb6v8IzioSf0Xm21w+1fK0OSHH4F6XJfPCB8F+y9gDyTk7PpScAGaLFjoX9h5WnCfXm6wiXZP0IiUribdKHrxNuFpCOO+zy/ZZvsGOJ8PflvHcZjjMxkqyQvQ+5YZukhurhawinRbNd7h8puXsO3lwJax2Ged9dNluyzcGGXvZG8tpq+RveP+BF8l+MdoPVElWkTaJ5txAhnAjyfyqyz2cV06R+PRkzs8jw2EPe82MLYbjVyyrCG7quBT5prWQVSQ2VebnXc4vznyNyz2VrqTNdnxDtFkn8F/BE/gpyCqG/WoRPAsHu7Fy4DxeJIvimSb6KOf7k6GifYL9Jo/+oivgJOxlGZ/K/Bzu4Cdaxgae9L7kx2CReHwK9hTdQnyXMp9upVgihX1FbzeWBi8kTX97JSuHO+9v8KLoPicLbk/8e86Ab112N+U8bohb4FIp3Ib8r8jVxsVQN1j5gT6skUGiex+uqLpebCQSiUQikUiV/AHfELyhJuZKpQAAAABJRU5ErkJggg==>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEkAAAAWCAYAAACMq7H+AAAAh0lEQVR4Xu3KMQ4BQRhH8ZXIJgiH2FokruAcohCNcqstKB1CnEWloVVpuItXTJh8B1CY90te8f1nqkqSJEnSb4xpQ2uahLdoHocS1NRRP91TulPz+fE1onMcS7CMA7b0pEW29ehIbbYV4xSHZEYPutGKLnSlQf6pFLs4ZIZ0oBft0y1JkvTv3prtDSru6w0MAAAAAElFTkSuQmCC>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADUAAAAWCAYAAABg3tToAAAC1UlEQVR4Xu2W2atPURTHl3ksujwQCg/KUG4iScaQ4cGbMrwgHq8yPPBAMpTI8F9QyJBMxS3DiyElyZAkD6YyJQ8S3+9Za//2Ovt3zrmd+0T9PvWtvdfaZ5+9zl577SPSosU/wTzoNPQFega15d0N1kGXoafQfqhP3p3RG7oNfYPuQavz7iYmQX8KNFZ0/tQe1CWvoQ7RBZyB3kKj/QCwE/oObYCWQC+hm1BfN6YfdBZaDA2BNkI/oANuTMpAaD70RHSxj6EFUH+oh/ko+j5Ai6xfyRhpHsQJrrk+X0LbPmdbYbYtzrbbbJ5DBbYiroqOu5g6DPqep8YyDqYGiVs83fqnrD+jMUKkl2iKPbB+T+i9aAp7Zkm9oM6nDqNWULdEt9XzS3SSPdYPQXLhnjtmJ2utfSO6MwaZ3adpESEopm8RtYLaDG1LbCGINa7/M7obXJcYFM8c25eiO4Pngvb0jKbUDYpnLqzTqxQ6uXsDXJ9FIsUHxTRm+0J0Z4SgQiqXUTcofiTa+N5Qhc9Fd56hooNXOhv7X10/cEViUEetXTTxb2hZakwIQVXJBzUF+ixacQkrd1hLjqWiC0jh4K52aqu1y3aqPbGn1N2p8dAqa/Os099UOSeKVq5jqUP0ARaPlE6JQa23NnfPwwJBO6+OKuoG5dkOvYGGeeNw0Qf2OttMaKG1GSwnHRzdGQ/NTlju2b4b3Rmcm3buWBUhlXn5F1EW1ATRC55ZlqMT2pXYjkObrH1SdNJx0Z3xUfQLES76HfQiujOY+yHwKrpzTzHt+EvWND//CGgsUijDXDDPCu8g7hb7J0QP6igbQ7grr1yfY3mXUVXwIn8k+k7+L051Pr5rsvl4uTMjWO34sXjOaZ9jYxsf/b45UvEBnzKsivyR5U5wkZ+g2c4fmCbqPyI6lvOPyI3I090f2sMFNqo2LJ9zoR3QyMTnWS6azkzfcNe1aNHiP+QvFjfzIjC1xYEAAAAASUVORK5CYII=>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADUAAAAWCAYAAABg3tToAAACjUlEQVR4Xu2W24tIURTGl/u1qPEwEwqFQpnEwzSNKOTyrsQL8kqJB/PgxaVEyn8xM0UuCSk8oOSSkhTy4Mmt3JIHie87e217nTX7HM6Uos6vvtrnW/vss9e+HpGWln+KUdBubxq2QZegJ9BhaFw5XDAWugl9gu5CW8rhYSyCfmQ0R0L73o/6IxZCQ1L9wgHoM7QDWgc9h65D402dCdAZaC00DdoJfYGOmDqeydAq6LGEbz+CVkMTJQwyYxRjb6A1+lzLVOg7dEeqR4EfoX/IeJvU22O8g+pZjmW8HFck1LvgAwpjT71ZxRgJo0W+Sb4DgxL8Fcbje1xi9/V5NPQa+vCrRqBH8m16YlLnfEBplJSFM5brQJxBdtxyS32yVcvXUrhgivp2meaISXH55vgrSX31JrgqqT73HMsXU7iA+4L+LOd7mibFPRcH22oYdUnxkPDYpI5q+XwKF8Skljvf0zQpDhI9fjeewmdTOFGX1EdvgsuS6p/Ucq5htrvBm46YVJ1sUkug9xJOXMKrI9f32qR+N1N7tVw1U93O9zSdqXnQZi1zrzOePTnrkuLJ6Lkhqf52LXP2LDwg6M92vqdpUpZ90EuowwdIVVI8punzTrM8UJ/wuGf5dgoXzFCfM1ZHXMqnfUCpSmqBhAt+vQ9EqpIakODPdf5bCSNE2OlX0LMULuDaz7XpGck9xWXHX7LK9udLCOZmhB3mXuEdxBifT0nYqDNNPc7KC/PMurzLqDp4kT+U8G3+Ly41MX5rscZ4uXNF8LTjYHGf0+/TuqVBj8l42eSmS/iR5Uywk++gXhOPLJMQPyGh7j2os1SjzEh/aI9nPKoxPD5XQvuhLhezbIT6oV3QJBdraWn5j/gJ3tbpehLpLRYAAAAASUVORK5CYII=>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFIAAAAZCAYAAACis3k0AAADcklEQVR4Xu2YWaiNURTHl7EoQhkS3RRePKBQRK4xMpap5OFSIpQnmWVIXkxJxpQhmZIiyUwkT6bkgQfCg6lMIST+f2vvc/e37nfOuWcfXA/fr/7ds9ba3z3ft76199r7iGRkZGSURFPrAEeg1sbXBtoK3YEuQr2S4Rx9oRfQU+iA6HWFeAb9NJruYpdTYtRqF/+vGA3tgma6zxug51DLYEwH6AF0FuoObYK+QWOCMWQQ9B5qB/WALoj+r0L0gw6LJug7NFL0etITqoTWu/gMZ3dy8WjqQXOgJjZQBhOl5htvnxghcgl6C7UIfDdEk+TvhbE30BU/QLSqPwV2PpaKfu9nG3BMFo1X2EC5NICmQbehKqhxIloa460jBT7EZuOb6vxbnH3U2RNyI5Tt0CTjsywRvfadDTj8y+5oA38KVuh16DE0G2qUDNeKsdaRAh9ilfFxCtLP9ZJw6tMekhuhrINWGp/FV2S+RP61irQMFV2/HopWaylwXRwO3RR9kJPJ8G/4EIuMj+sh/fdEX+hXZ3PNC1kh2qQKEZNINhz60rQxGBcFOykrg12voYnlYxR0y/1lg5knNZPGm1tofD6Rr0TXSf8Q7NohTCSnfSFiErkD+iDa1Ehv0Wb1Wmqu8VEcg06Jrn2slGKE3dnDmw4fnrZN7kDn/wHVd58pW5HLoPPGZ/Fr5EfRrmy13MXDNfK0JHcNjN+VuOUtwWDRBHazgQh4U0+MbRPpK5J7RsKunpZIViS3N4WIqcgqqK37zPWaL9TOhpJgs7gG7YE6m1gsvrr88sDPrIqQYc5/39mPnF3pBzjWQNuMzxKTSE9z0ZfOqo6GSdwNdbGBWsJTDavYnm5401z7Qpub4hBuc+g/5OwTzra7AG6buPctRDnbn52iMS4vhFut/dXh/PACvqGrUr2Hi2WE6E2w0YTQd87YewObMDn087SRZnuY6GIzxVck18g08lUklzN73WLRk1dRWllHmbA5hcyCjhvfANGO6DfvXUVPMXabsQB6GdhTRB+0GKwgjuN39DcxntXXisaZ0GbOv8/5zjibhxIeEr6IHnf/OZwu3DJxCvJszJtL2zoxwYwx8ZyC/EEirUMeFJ0pfBkcX2xax/5oYX2hxvHiuqAPNF+0gvwPBmlUiI4ptLWif65oc+KPDhkZGRkZGRkZGXXHL9Z09/Aig25cAAAAAElFTkSuQmCC>