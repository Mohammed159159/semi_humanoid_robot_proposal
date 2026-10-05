# Conceptual Design and Engineering Requirements Clarification for a Modular Semi-Humanoid Robotic Platform

## 1. Formal Framework for Task Clarification and System Design

The engineering of advanced autonomous mobile manipulation platforms demands a rigorous departure from sequential, discipline-isolated development methodologies.

Traditional product engineering pipelines frequently treat the physical skeleton, electrical power infrastructure, motion actuation, and software intelligence as consecutive phases.

In high-degree-of-freedom mobile robotic systems, this fragmented approach produces structural inefficiencies, dynamic instabilities, interface mismatches, and software patches engineered solely to compensate for uncoordinated hardware selections.

The VDI 2206 standard ("Design Methodology for Mechatronic Systems") addresses these failure modes by establishing a structured, cross-domain procedure model that operates across iterative macro-cycles and micro-cycles of problem-solving.

At the macro-level, the VDI 2206 V-model defines an operational framework for multidisciplinary integration.

The left descending branch encompasses task clarification, system-level requirement formulation, and domain-embracing conceptual design.

The base of the V-model represents concurrent, domain-specific elaboration across mechanical engineering, electrical engineering, and computer science.

The right ascending branch tracks physical and logical integration, continuous property verification, software-in-the-loop (SIL) and hardware-in-the-loop (HIL) testing, and total system validation against the baseline specification.

Underlying this macro-architecture is the recurring problem-solving micro-cycle, derived from classical systems engineering.

This micro-cycle progresses sequentially through situation analysis, target formulation, solution synthesis, analysis and evaluation, decision-making, and subsequent planning.

When applied to a semi-humanoid robot, this continuous cognitive loop prevents premature convergence on rigid hardware concepts by compelling the engineering team to express system capabilities through abstract functional representations before fixing geometric dimensions, motor frame sizes, or communication protocols.

The target semi-humanoid platform functions as an advanced Cyber-Physical System (CPS) situated within the emerging paradigm of Industry 5.0.

Whereas Industry 4.0 prioritized hyper-connectivity, continuous data collection, and dark-factory autonomy, Industry 5.0 shifts focus toward human-centric collaboration, resilience, and sustainability within shared, human-inhabited environments.

A service or light-industrial mobile manipulator cannot rely on structured fixtures, isolated safety enclosures, or predictable workpieces.

The robot must integrate its physical body, distributed embedded processors, and cognitive pipelines into a unified whole that executes safe physical contact alongside human co-workers.

Achieving this functional harmony requires adhering to foundational mechatronic design principles governing machine dynamics and power distribution.

In dynamic motion control, joint compliance and structural rigidity directly govern operational bandwidth.

The undamped natural frequency of an actuated mechanical link is defined by the relationship between joint stiffness $K$ and moving inertia $M$:

$$
\omega_n = \sqrt{\frac{K}{M}}
$$

This relationship directly dictates the settling time of the mechanical manipulator following rapid repositioning maneuvers:

$$
t_{\text{settling}} \approx \frac{4}{\zeta \omega_n}
$$

where $\zeta$ represents the effective damping ratio of the joint assembly.

Minimizing the mass of distal links and eliminating unnecessary structural bulk shifts the structural resonance toward higher frequencies, which drastically reduces oscillation and allows high-gain, responsive closed-loop control.

Actuator oversizing introduces parasitic structural mass, accelerates battery depletion, and increases impact hazards during unexpected collisions in populated workspaces.

Conversely, implementing lightweight Quasi-Direct Drive (QDD) actuators, mechanical gravity-compensation mechanisms, and high-speed deterministic fieldbuses enables compliant, dynamic behavior while preserving structural rigidity.

The conceptual design phase—termed the task clarification and system design stage in VDI 2206—establishes the foundational boundary conditions of the platform.

Rather than engineering the robot for a single, narrow automation task, the platform architecture decouples physical capability from application-specific intent.

The physical body provides a stable, deterministic set of operational primitives, including omnidirectional base transit, torso elevation, coordinated dual-arm spatial reach, and multimodal scene perception.

The high-level application layer supplies the operational logic required to execute specific behaviors.

This decoupling is formally established by deriving requirements from standardized service robotics benchmarks, compiling these constraints into a structured mechatronic requirements list (Anforderungsliste), and translating them into comprehensive material, energy, and information flow structures.

## 2. Empirical Operational Task Formulation from Benchmark Competitions and Literature

Formulating operational objectives for a general-purpose semi-humanoid platform requires grounding abstract requirements in standardized, empirical benchmarks.

Rather than formulating arbitrary manipulation tasks, competitive service robotics leagues—most notably the international RoboCup@Home competition—provide standardized, highly validated test regimes that capture the true operational and physical difficulties of unstructured human spaces.

RoboCup@Home assesses autonomous service robots across open-ended scenarios in simulated residential, office, and light-industrial environments.

Evaluating the benchmarks across the Domestic Standard Platform League (DSPL), Open Platform League (OPL), and Social Standard Platform League (SSPL) reveals three canonical challenges that collectively span the functional envelope required for a general-purpose semi-humanoid: the General Purpose Service Robot (GPSR) benchmark, the Clean Up and Table Clearing challenges, and the Receptionist and Help-Me-Carry interaction tests.

The General Purpose Service Robot benchmark serves as the primary test for broad cognitive and physical generalization.

Unlike scripted automation routines, GPSR commands are generated pseudo-randomly by formal grammar engines, evaluating execution robustness across three escalating tiers of complexity.

- Category I tasks consist of fully specified sequential action requests combining mobile navigation, exteroceptive object recognition, and physical pick-and-place manipulation, such as navigating to a dining table, grasping a designated beverage container, and moving it to a waste receptacle.
- Category II tasks incorporate incomplete, underspecified instructions where contextual data is missing, requiring the platform to infer user intent, execute semantic reasoning, and engage in verbal clarification dialogue to identify ambiguous target items across multiple storage shelves.
- Category III tasks present erroneous or contradictory physical scenarios, such as commanding the retrieval of an item that is absent from its designated location, requiring the robot to detect the state discrepancy, abort execution safely, verbally inform the user of the failure state, and execute fallback behaviors.

The Clean Up and Table Clearing challenges benchmark fine-grained mobile manipulation and interaction with articulated domestic fixtures.

The operational scope requires the robot to approach standard dining surfaces, segment cluttered tableware, grasp varied geometric profiles such as cups, bowls, cutlery, and bottles, and clear the surface by transporting items to designated storage areas or into dishwasher racks.

In modern embodied artificial intelligence literature, physical rearrangement has been formalized as a canonical benchmark for intelligent agents.

The task space is defined mathematically over the special Euclidean group $SE(3) = \mathbb{R}^3 \times SO(3)$, requiring an autonomous system to transform an environment from an initial unorganized state $s_0 \in \mathcal{S}$ to a desired target configuration $s^* \in \mathcal{S}$ through direct physical contact.

This manipulation sequence requires the platform to negotiate physical clutter, handle occlusions, and operate articulated mechanisms such as spring-loaded cabinet doors, sliding drawers, and appliance covers.

The Receptionist and Help-Me-Carry tasks evaluate continuous human-robot interaction and dynamic spatial coordination.

The platform must detect human faces and body poses, maintain visual tracking of an unfamiliar walking guide, navigate populated corridors without violating personal safety boundaries, interpret natural pointing gestures, and handle physical handovers such as delivering drinks or taking heavy bags from a human hand.

Deconstructing these benchmarks reveals the operational primitives that the physical platform must support.

These primitives divide into spatial navigation, mobile manipulation, and human-robot interaction, operating within tightly defined physical constraints imposed by standard interior architecture.

- Standard doorway apertures range from 750 mm to 900 mm in width, dictating that a mobile base have a maximum footprint diameter between 540 mm and 650 mm to ensure collision-free clearance during autonomous transit.
- Standard furniture dimensions define the necessary vertical workspace boundaries. Dining tables, kitchen countertops, and workbenches are positioned between 720 mm and 900 mm above finished floor level. Storage shelving spans from 300 mm at lower tiers to 1300 mm through 1500 mm at intermediate tiers, while fallen items require retrieval at 0 mm directly from the floor surface. A fixed-height manipulator cannot cover this vertical span without encountering kinematic singularities or severe torque penalties. Consequently, an actively elevating prismatic torso column or a coordinated vertical degree of freedom is essential to provide unconstrained reach across all functional heights.
- Domestic manipulation targets commonly weigh between 0.2 kg for light cups and cutlery to 2.0 kg for full bottles, ceramic containers, and cooking pans. The robotic end-effectors must therefore supply normal clamping forces sufficient to retain these masses under rapid dynamic accelerations while retaining compliant grip surfaces to avoid crushing delicate items.

The following table links these standardized operational benchmarks directly to their underlying mechatronic primitives, execution parameters, and environmental boundary constraints.

| Operational Benchmark | Target Sub-Tasks | Underlying Mechatronic Primitives | Physical & Environmental Constraints |
| --- | --- | --- | --- |
| GPSR: Category I [cite: 16, 18] | Pick-and-place, point-to-point transit, object sorting | Autonomous SLAM, 3D object detection, inverse kinematics, open/close parallel grasp | Doorway clearance $\ge 750\text{ mm}$; table height $750\text{ mm}$; item mass $\le 1.5\text{ kg}$ [cite: 23, 25] |
| GPSR: Category II [cite: 18, 19] | Beverage fetching with dialogue, ambiguous item retrieval | Voice command parsing, semantic spatial reasoning, interactive clarification, pan-tilt visual search | Ambient noise $50\text{--}65\text{ dB}$; multi-shelf search heights ($300\text{--}1300\text{ mm}$) |
| GPSR: Category III [cite: 14, 18] | Missing item detection, conflicting order handling | Scene change verification, tactile/visual grasp failure detection, verbal status reporting | Execution timeout $\le 5\text{ min}$; dynamic human obstacles in navigation path |
| Clean Up / Tableware [cite: 14, 15, 20] | Clearing cups, bowls, cutlery; loading dishwasher/bin | Dense tabletop point cloud segmentation, surface normal estimation, compliant multi-angle grasping | Fragile objects; clearance envelope above table $\le 400\text{ mm}$; grasp span $20\text{--}85\text{ mm}$ [cite: 21] |
| Articulated Interaction [cite: 20, 21] | Opening/closing hinged doors, sliding drawers, appliances | Trajectory generation under kinematic constraints, contact force regulation, continuous joint torque | Pull/push forces up to $30\text{--}50\text{ N}$; base-assisted positioning maneuvers |
| Receptionist / Follow [cite: 14, 15] | Person detection, visual following, dynamic avoidance | Human skeletal tracking, dynamic local costmap planning, voice synthesis, conversational gaze | Walking velocity up to $1.2\text{ m/s}$; social distance maintenance ($0.8\text{--}1.5\text{ m}$) |
| Handover [cite: 14, 15] | Delivering drink/item to seated or standing person | Dynamic arm trajectory replanning, wrist force-torque sensing, intentional compliance, release timing | Safe velocity limits $\le 0.3\text{ m/s}$ near humans; safe payload release threshold |

## 3. Architectural and Morphological Benchmarking of Contemporary Mobile Manipulators

Analyzing existing mobile manipulation systems provides direct insight into proven kinematic arrangements, power architectures, actuator selections, and computing topologies.

Reference platforms documented across industry data sheets, academic literature, and open-source hardware repositories illustrate how varying design philosophies resolve the competing demands of payload capacity, reaching workspace, structural mass, and operational autonomy.

PAL Robotics' TIAGo series establishes a commercial standard for modular service robotics. The TIAGo Pro incorporates an anthropomorphic upper body mounted on an actively elevating torso column, supported by a compact mobile base. The platform utilizes Series Elastic Actuators (SEAs) across its dual 7-DoF arms, embedding joint-level torque sensors and mechanical safety brakes that permit compliant physical interaction in unconstrained human environments. The mobile chassis is offered in both differential-drive ($\varnothing 540\text{ mm}$) and omnidirectional Mecanum configurations ($710 \times 490\text{ mm}$), ensuring clearance through standard doorways. The joint network is coordinated across a 1 kHz EtherCAT fieldbus, coupling motor controllers with onboard compute resources consisting of an Intel Core i7 host paired with an NVIDIA Jetson GPU accelerator.

The companion PAL ARI platform focuses on social interaction and healthcare assistance, pairing a high-payload differential base with expressive touchscreen displays, wide-angle perception sensors, and animated upper-limb kinematics.

Pollen Robotics' Reachy 2 provides an open-source, anthropomorphic upper-body research platform optimized for bimanual manipulation, teleoperation, and human-robot interaction. Reachy 2 features 7-DoF arms powered by custom multi-axis spherical joint actuators (Orbita 2D and 3D modules) that yield compliant, human-like arm kinematics and a continuous payload capacity of 3.0 kg per arm. Its head houses an Orbbec Gemini 336 RGB-D stereo perception system mounted on a 3-DoF neck mechanism, providing human-like gaze tracking and visual exploration.

While Reachy 2 can operate as a static tabletop research unit, it is frequently integrated with omnidirectional wheeled bases to support mobile research workflows through an open-source Python SDK and ROS 2 middleware.

Stanford University's Mobile ALOHA illustrates the capabilities of low-cost, bimanual mobile manipulators running imitation learning policies for complex, long-horizon household chores such as cooking, table clearing, and door opening. Mobile ALOHA mounts two 6-DoF ViperX manipulators (handling ~0.75 kg payload per arm) onto an AgileX Tracer industrial differential AGV base. The base supports an onboard payload of 150 kg and reaches velocities up to 1.5–2.0 m/s using a 24V 30Ah LiFePO4 battery pack, providing up to 12 hours of operational autonomy. The platform relies on a passive leader-follower puppeteering exo-skeleton for teleoperation, recording synchronized 16-dimensional action trajectories spanning 14 arm/gripper joints and base velocity commands.

The industrial AgileX Cobot Magic evolution refines this concept by integrating an omnidirectional Mecanum chassis and high-payload PiPER arms communicating over high-bandwidth CAN buses.

Menlo Research's Asimov 1 represents an open-source humanoid robot that provides a reference for modular embedded architectures, actuation choices, and fabrication techniques. Although Asimov 1 is a bipedal robot (1.2 m height, 35 kg mass, 25 actuated DoFs), its upper-body design directly informs semi-humanoid architecture. The platform employs brushless DC motors with low-ratio planetary gearboxes (Quasi-Direct Drive, QDD) across its 5-DoF arms and single-axis waist yaw. Structural members are machined from 7075 aluminum and additive Multi Jet Fusion (MJF) PA12 nylon, maintaining high structural rigidity and low inertia. Its computing architecture isolates low-level motion control onto a dedicated system-on-module (Radxa CM5) connected across five independent 1 Mbps CAN buses, while high-level perception and networking run on a companion host computer (Raspberry Pi 5).

The Hello Robot Stretch represents a minimalist approach to mobile manipulation. Stretch replaces the anthropomorphic multi-joint arm topology with a compact differential-drive mobile base supporting a rigid vertical mast and a single telescoping horizontal arm ending in a 1-DoF compliant gripper. Weighing 24.5 kg, Stretch can reach from floor level to upper countertops while drawing minimal battery power. However, its single-arm prismatic morphology prevents it from executing bimanual tasks—such as stabilizing containers during opening, manipulating soft garments, or handling large, unwieldy objects.

The following table presents a comparative engineering benchmark of these reference systems, detailing their mechanical degrees of freedom, payloads, workspace geometries, internal buses, power profiles, and compute topologies.

| Specification Parameter | PAL Robotics TIAGo Pro | Pollen Robotics Reachy 2 | Mobile ALOHA (AgileX) | Menlo Research Asimov 1 | Hello Robot Stretch 3 |
| --- | --- | --- | --- | --- | --- |
| Morphology Category | Modular Semi-Humanoid (Wheeled) | Anthropomorphic Upper Body (Wheeled opt.) | Bimanual Mobile Manipulator | Bipedal Humanoid (Upper Body relevant) | Minimalist Prismatic Mobile Manipulator |
| Total Actuated DoF | 23 DoF (Base: 2/3, Torso: 1, Arms: $2 \times 7$, Head: 2, Grippers: 2) | 21–23 DoF (Arms: $2 \times 7$, Grippers: 2, Head: 3, Antennas: 2) | 16 DoF (Base: 2, Arms: $2 \times 6$, Grippers: 2) | 25 DoF (Legs: $2 \times 6$, Waist: 1, Arms: $2 \times 5$, Head: 2) | 5 DoF (Base: 2, Lift: 1, Arm Telescoping: 1, Wrist/Grip: 2) |
| Arm Payload Capacity | 3.0 kg per arm (continuous, excluding gripper) | 3.0 kg per arm | 0.75 kg (ViperX) to 1.5 kg (PiPER) per arm | ~1.5 kg per arm (nominal load) | 1.5 kg (at full horizontal extension) |
| Manipulator Reach | Vertical: 920–960 mm; Horizontal span: 2360 mm | Full arm span ~1400 mm; anthropomorphic workspace | Vertical: 650–2000 mm; Horizontal reach: 1000 mm | Arm reach ~600 mm; waist yaw rotation | Vertical: 1100 mm; Horizontal stroke: 520 mm |
| Torso / Lift Stroke | Actuated telescopic column: 350 mm stroke | Fixed anthropomorphic chest (or passive mounting) | Fixed aluminum extrusion frame; static mount | Fixed torso frame with 1-DoF waist yaw | Vertical prismatic carriage on fixed mast |
| Base Drive Kinematics | Differential drive ($\varnothing 540\text{ mm}$) or Omnidirectional Mecanum | Omnidirectional wheeled base (optional) | Differential drive (AgileX Tracer AGV, $\varnothing$ sweep 500 mm) | Bipedal dynamic walking legs (6-DoF per leg) | Differential drive with dual central wheels and passive castors |
| Maximum Base Speed | 1.0 m/s | 0.8–1.0 m/s (base dependent) | 1.5–2.0 m/s | 0.8–1.2 m/s (walking gait) | 0.6 m/s |
| Total System Weight | 60–72 kg (differential), 95 kg (omnidirectional) | ~35–40 kg (upper body + base) | ~75 kg (including power bank and arms) | 35 kg | 24.5 kg |
| Actuator & Sensing Tech | Series Elastic Actuators (SEA), joint torque sensors, safety brakes | Custom Orbita 2D/3D spherical joints, brushless motors | Off-the-shelf industrial servos / direct DC brushless | Dynamixel-Q / BLDC with low-ratio planetary gears (QDD) | Stepper motors with belt reductions and compliance springs |
| Internal Fieldbus | Real-time EtherCAT (1 kHz closed loop) | CAN bus & USB 3.0 / Serial | CAN bus (arms and base) | 5x CAN @ 1 Mbps + 1x CAN @ 500 kbps | USB over internal serial UART / CAN |
| Battery Power & Life | 36V 20Ah Li-ion (8–10 hours autonomy) | 24V–48V Li-ion (4–6 hours typical) | 24V 30Ah LFP base + EcoFlow 1024Wh pack (12 hours) | 48V Li-ion pack (~1–2 hours walking) | 12V 20Ah LiFePO4 (~4 hours continuous) |
| Primary Compute Architecture | Intel Core i7 + NVIDIA Jetson GPU expansion | Internal industrial SBC + NVIDIA Jetson Orin | Onboard high-performance laptop (Intel i7 + RTX GPU) | Heterogeneous: Radxa CM5 (motion) + Raspberry Pi 5 (media) | Intel Core i5 embedded computer |

Synthesizing these architectural implementations reveals three major mechatronic design trade-offs that dictate the performance of a semi-humanoid platform:

- **In evaluating torso kinematics, the engineering choice balances an actively elevating prismatic column against a multi-axis revolute waist.** Prismatic telescoping columns maintain a stationary center of mass directly over the wheel baseline, preventing large out-of-plane cantilever moments during heavy pick-and-place cycles. While an articulated waist produces expressive anthropomorphic motions, forward pitching induces severe overturning moments that demand high-reduction gearmotors and risk tipping the mobile base. For a wheeled platform operating between floor level and high cabinetry, a vertical prismatic column driven by a ball screw or reinforced timing belt provides superior structural stiffness, simplified kinematic inversion, and consistent stability.
- **In evaluating base mobility, the choice balances holonomic Mecanum or omnidirectional drives against non-holonomic differential configurations.** While differential-drive bases offer mechanical simplicity, fewer drive components, and lower cost, their non-holonomic kinematic constraints complicate fine mobile manipulation. Interacting with cupboards, appliances, and dining tables requires frequent, small lateral adjustments. A non-holonomic base must execute multi-point turning maneuvers to achieve a sideways translation, whereas a holonomic omnidirectional chassis adjusts its lateral position vector instantaneously:

  $$
  \mathbf{v}_{\text{base}} = \begin{bmatrix} \dot{x} & \dot{y} & \dot{\theta} \end{bmatrix}^T
  $$

  This unconstrained mobility simplifies inverse kinematic solvers and teleoperated data collection.

- **In selecting an actuation paradigm, the trade-off lies between Quasi-Direct Drive (QDD) actuators, Series Elastic Actuators (SEAs), and conventional high-reduction servomotors.**
    - High-reduction geared servos ($>100:1$) provide high static holding torque in compact form factors but exhibit high reflected mechanical impedance, significant backlash, and poor backdrivability, which complicates open-loop force estimation and makes physical contact hazardous.
    - Series Elastic Actuators place a calibrated mechanical spring between the gearbox and the output link, converting physical deflection into accurate joint torque measurements and providing passive mechanical compliance. However, this elasticity limits control bandwidth and introduces low-frequency structural resonances.
    - Quasi-Direct Drive actuators combine high-torque-density brushless outrunner motors with low-ratio planetary gearings ($1:6$ to $1:10$), delivering low mechanical impedance, exceptional backdrivability, impact tolerance, and direct torque regulation via motor phase current measurements.

This makes QDD actuation an effective approach for safe, compliant manipulation in unstructured environments.

## 4. Functional Structure Modeling: Material, Energy, and Information Flows

In accordance with the task clarification procedures established in VDI 2206 and classical systems engineering, operational requirements must be abstracted into a functional structure (Funktionsstruktur).

A functional structure maps overall product functionality into discrete sub-functions governed by three fundamental physical flows across system boundaries: Material, Energy, and Information.

The primary function of the semi-humanoid platform is formally defined as:

> Autonomously transform unstructured human requests and sensory environmental observations into safe, coordinated physical mobile manipulation and material rearrangement.

**Material flow** ($\mathbf{M}$) encompasses all physical items, payloads, and mechanical contact forces transferred across the platform boundary.

- The input material flow ($\mathbf{M}_{\text{in}}$) includes target workpieces such as tableware, containers, bottles, dry goods, and light packages weighing between 0.05 kg and 3.0 kg, as well as physical fixtures encountered in the environment, such as cabinet doors, drawers, and furniture surfaces.
- The system accepts and isolates target workpieces using dual parallel-jaw or multi-fingered end-effectors.
- Once grasped, the robot supports and secures the payload against gravitational loads and dynamic transport accelerations through the structural link chains of the arms, torso column, and mobile chassis.
- The system then relocates and guides the workpiece through three-dimensional space via coordinated mobile base navigation and multi-joint arm articulation.
- Finally, the robot positions and releases the payload at the designated placement location, such as a table, shelf, or receptacle, under controlled contact forces.

The resulting output material flow ($\mathbf{M}_{\text{out}}$) manifests as reordered, stable environmental states, altered fixture configurations (such as opened doors or closed drawers), and mechanically stabilized cargo during transport.

**Energy flow** ($\mathbf{E}$) tracks the storage, regulation, conversion, and dissipation of electrical and mechanical energy through the platform.

- The primary input energy flow ($\mathbf{E}_{\text{in}}$) consists of external AC power supplied from charging docks ($110\text{--}230\text{V AC}$) and secondary DC energy stored in internal lithium battery chemistries ($24\text{V}$, $36\text{V}$, or $48\text{V}$).
- The platform stores this energy in high-capacity onboard battery packs designed to sustain continuous mixed operation for more than four hours.
- A power protection and management subsystem continuously monitors battery health, isolates short circuits, and triggers emergency-stop contactor cutoffs when safety interlocks are tripped.
- DC-DC converter stages condition and regulate the raw battery bus into galvanically isolated voltage domains: a high-power bus ($24\text{--}48\text{V}$) delivering current to motor drive inverters, an intermediate bus ($12\text{--}19\text{V}$) powering SBC compute units and edge GPUs, and regulated low-voltage rails ($5\text{V}$, $3.3\text{V}$) supplying microcontrollers, network switches, and sensor suites.
- Pulse-width modulated (PWM) gate drives convert these DC rails into polyphase AC drive signals across the brushless motors of the wheels, torso lift, and arm joints.

The resulting output energy flow ($\mathbf{E}_{\text{out}}$) comprises mechanical work executed on manipulated objects and mobile surfaces, thermal energy dissipated through heat sinks and motor casings, and electrical kinetic energy absorbed during regenerative braking or active damping.

**Information flow** ($\mathbf{I}$) encompasses the transmission, algorithmic processing, and feedback regulation of sensory signals, operational commands, and system telemetry.

- The input information flow ($\mathbf{I}_{\text{in}}$) includes natural language speech audio captured by head and torso microphone arrays, photon streams received by RGB-D cameras and planar LiDAR scanners, joint encoder counts, motor phase current measurements, wrist force-torque transducer signals, and high-level command packets transmitted across external software interfaces.
- Low-level signal conditioning circuits execute analog-to-digital conversion, anti-aliasing filtering, and quadrature decoding.
- Mid-level computing pipelines process exteroceptive sensor streams to perform 3D point cloud registration, surface normal calculation, human skeletal tracking, and Simultaneous Localization and Mapping (SLAM).
- Higher-level cognitive modules parse natural language instructions, evaluate semantic task states, plan collision-free global and local navigation paths, and resolve inverse kinematics.
- Embedded real-time microcontrollers execute closed-loop motion control—such as cascaded current, velocity, and position PID loops, or impedance controllers—at high update rates.
- Information is coordinated internally across deterministic, low-latency fieldbuses (EtherCAT or CAN FD operating at $500\text{--}1000\text{ Hz}$) for real-time motor control, paired with asynchronous publish-subscribe middleware (ROS 2 / DDS) for high-level processes.
- The output information flow ($\mathbf{I}_{\text{out}}$) includes high-frequency PWM switching vectors, synthesized speech audio generated through onboard loudspeakers, visual telemetry on status displays, and system diagnostics streamed across external communication ports.

## 5. Engineering Requirements Specification (Anforderungsliste)

Following VDI 2206 requirements engineering methodology, qualitative user expectations and functional objectives must be converted into a formal engineering requirements list (Anforderungsliste).

This requirements specification serves as the evaluation baseline for verifying and validating the system throughout its embodiment and integration phases.

Requirements are structured according to two core classification parameters:

- **Requirement Type:**
    - **Fixed Requirement (Festforderung, FF):** Absolute constraints that must be fulfilled under all operational conditions. Concepts failing to satisfy an FF are technically non-viable.
    - **Range Requirement (Bereichsforderung, BF):** Performance metrics that specify acceptable and optimal target bands. The design must achieve the minimum bound, with optimization directed toward the target value.
- **Criterion Characteristic:**
    - **Quantitative (quan):** Measurable physical parameters with defined engineering units, verifiable through numerical calculation, CAD modeling, or physical measurement.
    - **Qualitative (qual):** Functional and architectural characteristics verified through functional testing, structural inspection, or code compliance auditing.

The following table provides the complete engineering requirements specification for the modular semi-humanoid platform across its mechanical, electrical, embedded control, perception, and software architectural domains.

| ID | Engineering Requirement Category | Requirement Description and Engineering Metric | Parameter Value / Range | Unit | Type | Char | Verification / Validation Method |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G01 | Geometry & Envelope | Maximum mobile base footprint diameter / width envelope | $\le 600$ (Optimal: $\le 540$) | mm | BF | quan | Dimensional inspection of CAD model and physical chassis |
| G02 | Geometry & Envelope | Robot total height in contracted / home configuration | $1100\text{--}1250$ | mm | BF | quan | Coordinate measuring / vertical height gauge |
| G03 | Geometry & Envelope | Clearance for passing standard interior doorway apertures | $\ge 750$ clearance (margin $\ge 75$ per side) | mm | FF | quan | Physical arena passage verification test |
| K01 | Kinematics & Reach | Total active degrees of freedom (excluding end-effector tooling) | $18\text{--}22$ (Base: 2-3, Torso: 1, Arms: $2 \times 7$, Head: 2) | DoF | BF | quan | Kinematic topology verification and joint audit |
| K02 | Kinematics & Reach | Vertical active elevation stroke of torso / column module | $\ge 350$ (Continuous linear range) | mm | FF | quan | Prismatic rail travel measurement under load |
| K03 | Kinematics & Reach | Manipulator vertical reachable workspace envelope | $0$ (floor level) to $\ge 1350$ (shelf level) | mm | FF | quan | End-effector coordinate reach calibration across range |
| K04 | Kinematics & Reach | Dual-arm horizontal bimanual span | $1200\text{--}1600$ | mm | BF | quan | Workspace boundary mapping in simulation and real setup |
| D01 | Dynamics & Payload | Maximum continuous manipulation payload per arm at full extension | $\ge 2.0$ (Nominal: $3.0$) | kg | FF | quan | Static and dynamic load-holding tests at horizontal reach |
| D02 | Dynamics & Payload | Maximum base operational transit speed on smooth level surface | $0.8\text{--}1.2$ (Regulated indoor limit) | m/s | BF | quan | Laser-timed linear velocity profile tracking |
| D03 | Dynamics & Payload | End-effector Cartesian repeatability under nominal payload | $\le \pm 2.0$ (Optimal: $\le \pm 1.0$) | mm | BF | quan | Multi-cycle dial-indicator / laser tracker verification |
| D04 | Dynamics & Payload | Structural settling time after high-speed arm repositioning | $t_{\text{settling}} \le 0.4$ (Damped $\zeta \ge 0.65$) | s | BF | quan | Accelerometer decay measurement at end-effector flange |
| E01 | Electrical & Power | Nominal DC system bus voltage | $24.0\text{--}48.0$ (Galvanically isolated logic) | V | FF | quan | Multimeter / oscilloscope rail voltage verification |
| E02 | Electrical & Power | Operational battery run-time under continuous mixed duty cycle | $\ge 4.0$ (Optimal: $\ge 8.0$) | h | BF | quan | Automated continuous execution loop until low-SOC cutoff |
| E03 | Electrical & Power | Emergency power disconnect response time (Hardware E-Stop) | $\le 10$ (Direct actuator power cutoff) | ms | FF | quan | Oscilloscope timing of coil de-energization |
| C01 | Embedded Control | Real-time joint motion control loop cycle frequency | $\ge 500$ (Optimal: $1000$ via EtherCAT/CAN FD) | Hz | FF | quan | Jitter and loop-timing telemetry logging on real-time OS |
| C02 | Embedded Control | Bus communication protocol for motor drive synchronization | EtherCAT or CAN FD (CAN 2.0B minimum) | — | FF | qual | Protocol packet inspection and bus load analyzer |
| C03 | Embedded Control | Distributed compute topology separation | Tier 1: Real-time MCU; Tier 2: SBC/GPU host | — | FF | qual | Architectural audit of processor responsibilities |
| S01 | Sensing & Perception | Exteroceptive horizontal FoV coverage for local obstacle navigation | $360^{\circ}$ (Planar LiDAR / surround depth fusion) | deg | FF | quan | Blind-spot mapping using standard calibration targets |
| S02 | Sensing & Perception | Active head perception unit degrees of freedom | $\ge 2$ (Pan: $\pm 90^{\circ}$, Tilt: $+45^{\circ}/-30^{\circ}$) | DoF | BF | quan | Goniometer joint angle sweep verification |
| S03 | Sensing & Perception | Hand/wrist contact force sensing capability | $\ge 3$-axis F/T or compliant torque feedback | — | BF | qual | Calibration rig with calibrated static weights |
| A01 | Software & API | Standardized API middleware framework | ROS 2 (LTS release, e.g., Humble / Jazzy) | — | FF | qual | Interface compliance and package compilation audit |
| A02 | Software & API | High-level Task Port abstraction interface | Decoupled action servers (nav2, moveit2) | — | FF | qual | Unit tests flashing external application task node |
| A03 | Software & API | VLA inference and trajectory execution bandwidth | $\ge 10$ policy queries / trajectory streaming | Hz | BF | quan | End-to-end benchmark timing of inference-action loop |
| M01 | Modularity & HMI | Independent sub-assembly removal time (arms, head, base) | $\le 20$ using standard hand tools | min | BF | quan | Timed disassembly and re-assembly trial |
| M02 | Modularity & HMI | Visual system status and diagnostic dashboard | Integrated display or remote web dashboard | — | FF | qual | Inspection of live alarm and battery status telemetry |

## 6. Software Architecture, Task Port Abstraction, and Embodied AI Integration

The core architectural premise of the platform is the rigorous decoupling of capability from intent.

The platform is not engineered as a single-purpose automation cell; instead, it is structured as an integrated physical substrate that exposes its perception, navigation, and manipulation capabilities through stable, standardized interfaces. The downstream user or higher-level cognitive agent interacts with the robot at the level of high-level goals rather than low-level motor control loops.

The software stack is organized into four hierarchical layers, ensuring strict functional separation between real-time embedded control and cognitive planning:

- **Cognitive and Application Layer:** High-level natural language processing, behavioral task state machines, and learning-based policies that formulate situational intent.
- **Task Port Abstraction Layer:** The standardized software boundary that exposes high-level ROS 2 Action Servers, Topics, and Services, preventing application programs from directly touching lower-level control routines.
- **Core Platform Middleware Layer:** Autonomous navigation pipelines (Nav2), motion planning frameworks (MoveIt 2), and vision processing nodes running on the primary onboard compute host.
- **Embedded Real-Time Layer:** Dedicated microcontrollers executing deterministic motor commutation, sensor signal acquisition, and safety monitoring across high-speed fieldbuses.

The physical and logical bridge between the robotic platform and external application tasks is formalized through the Task Port. The Task Port is a dedicated, secure network and software gateway that exposes standardized ROS 2 interfaces, shielding core platform stability from user-level programming errors.

Application developers validate platform generalizability by deploying task nodes that interact exclusively through these abstraction boundaries.

The navigation interface accepts target poses in the global reference frame:

$$
\mathbf{T}_{\text{goal}} \in SE(2) = (x, y, \theta)
$$

The underlying Nav2 stack handles local costmap generation, obstacle avoidance, and path tracking without external intervention.

The manipulation interface accepts Cartesian tool-center-point (TCP) goals:

$$
\mathbf{T}_{\text{TCP}} \in SE(3)
$$

or synchronized joint-space trajectories.

The MoveIt 2 core computes collision-free kinematic inversions, enforces velocity and acceleration limits, and coordinates dual-arm trajectories.

The perception interface provides semantic segmentation and grasp synthesis services, converting user-specified queries into localized 3D target coordinates and surface normals.

Finally, the diagnostic interface streams real-time joint states, bus health metrics, battery state of charge (SoC), and safety interlock statuses to the external application layer and user dashboard.

To operate effectively in dynamic, unstructured settings, the platform accommodates modern Vision-Language-Action (VLA) models, such as OpenVLA and RT-X, derived from the Open X-Embodiment foundation. Unlike traditional pipelines that rely on hand-crafted state machines and explicit geometric feature modeling, VLAs map visual observations and natural language task instructions directly into continuous low-level action sequences:

$$
\mathbf{a}_t = \pi_{\text{VLA}}(\mathbf{o}_t, \mathbf{l})
$$

where $\mathbf{o}_t$ denotes multimodal sensory observations (RGB-D camera streams from the pan-tilt head and wrist-mounted cameras), $\mathbf{l}$ represents tokenized natural language instructions, and $\mathbf{a}_t$ is the predicted action vector.

In standard implementations, the action vector $\mathbf{a}_t$ is formulated in end-effector Cartesian space:

$$
\mathbf{a}_t = \begin{bmatrix} \Delta x & \Delta y & \Delta z & \Delta \phi_r & \Delta \phi_p & \Delta \phi_y & g \end{bmatrix}^T
$$

representing 3D translational increments, 3D rotational increments, and continuous or discrete gripper open/close states.

For whole-body coordination, the action vector expands to 16 or more dimensions to encompass base linear velocity $v_x$, lateral velocity $v_y$, angular velocity $\omega_z$, torso elevation $\dot{z}$, and dual-arm joint positions.

Integrating a VLA model into the platform introduces specific computational and real-time execution challenges that dictate the software architecture:

- **First, an operational bandwidth mismatch exists between high-level policy inference and low-level motor commutation.** Edge AI processors execute large autoregressive VLA models at rates between 5 Hz and 20 Hz. Applying raw 10 Hz step commands directly to joint motor drives induces high-frequency jerk that excites structural resonances ($\omega_n$) in the mechanical linkages, resulting in severe vibrations and premature mechanical wear.

  To maintain dynamic stability, the mid-level platform controller implements real-time cubic spline or quintic polynomial trajectory interpolation. This interpolator buffers discrete VLA action chunks and generates smooth, continuous position and velocity setpoints at 1 kHz to match the update rate of the motor fieldbus.

- **Second, neural network policies are fundamentally probabilistic and susceptible to out-of-distribution hallucinations or sudden control instabilities.** The Task Port architecture places a deterministic safety supervisor between the VLA policy output and the low-level joint drives.

  This supervisory node continuously checks joint position limits, Cartesian workspace boundaries, kinematic singularity proximities, and unexpected contact torques. If the policy commands an unsafe trajectory or encounters unexpected physical resistance, the safety node overrides the neural policy, arrests motion along a controlled deceleration profile, and signals a fault state to the application dashboard.

## 7. Synthesis and Strategic Implementation Pathways

Applying VDI 2206 design methodologies alongside empirical service benchmarks and reference hardware analyses establishes four core architectural directives that govern subsequent embodiment design phases:

- **For the kinematic configuration,** the platform should integrate an actively elevating prismatic torso column (minimum travel stroke of 350 mm) onto a holonomic omnidirectional wheeled base (maximum footprint diameter of 540 mm). This configuration preserves static overturning stability during pick-and-place routines by keeping the system center of mass centered within the wheel footprint, while providing complete vertical coverage from floor level (0 mm) to high shelving (1350 mm) and ensuring unconstrained maneuverability through narrow interior doorways.
- **For the actuation topology,** the upper-body manipulators should employ Quasi-Direct Drive (QDD) actuators or Series Elastic Actuators (SEAs) rather than conventional high-reduction servomotors. High backdrivability and low reflected mechanical impedance protect the structural linkages from shock loads during accidental collisions, enable direct torque control via motor phase current feedback, and ensure inherent physical compliance in shared human environments.
- **For the embedded computing topology,** computational responsibilities must be partitioned across dedicated functional tiers. High-level cognitive reasoning, VLA policy inference, 3D point cloud segmentation, and SLAM mapping execute on an onboard GPU host computer running ROS 2 under a real-time Linux kernel. Hard real-time motion control—including cascaded current, velocity, and position regulation—executes on dedicated ARM Cortex-M or DSP microcontrollers communicating with individual motor drives across a deterministic 1 kHz fieldbus such as EtherCAT or high-speed CAN FD.
- **For interface encapsulation,** platform capabilities must remain decoupled from application intent through the standardized Task Port. By implementing standard ROS 2 action interfaces for navigation, manipulation, and perception, external programs can command complete tasks—such as RoboCup@Home GPSR sequences or table clearing routines—without accessing low-level joint drivers. Validating these capabilities through external application nodes confirms that the platform provides a verified, extensible foundation for advanced robotics and physical AI research.


#### **Works cited**

### Annotated Reference Directory & Requirements Knowledge Base

> **Citation Indexing Note:** All original citation identifiers `[1]` through `[52]` are strictly preserved to maintain full backward compatibility with in-text references (e.g., `[cite: 14, 18]`, `[cite: 23, 25]`). The 34 supplementary resources are indexed from `[53]` through `[86]`. For optimal engineering clarity, all 86 resources are organized into six domain-specific categories with concise annotations detailing their technical contributions and relevance to the robot's requirements.

---

### Category 1: Systems Engineering, Mechatronic Methodologies & Product Architecture

Foundational engineering standards, cross-domain design methodologies (VDI 2206), function-to-structure synthesis, capability-based planning, and energy-sensitive development frameworks.

- **[1] Lecture 2 and 3 - VDI.pdf**  
  *Source / Reference:* Course lecture notes on VDI 2206 mechatronic development process, iterative macro/micro-cycles, and domain allocation (`material/mechatronic_principles/Lecture 2 and 3 - VDI.pdf`).  
  *System Relevance:* Establishes the multidisciplinary V-model workflow spanning requirements specification, domain-specific elaboration, and continuous SIL/HIL verification.
- **[2] VDI 2206.pdf**  
  *Source / Reference:* Verein Deutscher Ingenieure (VDI), *VDI 2206: Design Methodology for Mechatronic Systems (Entwurfsmethodik für mechatronische Systeme)* (`material/mechatronic_principles/VDI 2206.pdf`).  
  *System Relevance:* Core methodology governing the platform design loop; guides problem-solving micro-cycles (situation analysis $\to$ target formulation $\to$ solution synthesis) and Anforderungsliste formalization.
- **[3] Lecture 01.pdf**  
  *Source / Reference:* Lecture notes on fundamental mechatronic engineering concepts, interfaces, and system lifecycle engineering (`material/mechatronic_principles/Lecture 01.pdf`).  
  *System Relevance:* Informs the holistic definition of the semi-humanoid platform as an integrated Cyber-Physical System (CPS).
- **[4] Lecture 1 - Mechatronic System Design Principles.pdf**  
  *Source / Reference:* Lecture notes on machine dynamics, joint compliance, structural rigidity, and natural frequency calculations (`material/mechatronic_principles/Lecture 1 - Mechatronic System Design Principles.pdf`).  
  *System Relevance:* Provides mathematical foundations for link natural frequency ($\omega_n = \sqrt{K/M}$), damping ratios ($\zeta$), and settling time optimization ($t_{\text{settling}} \le 0.4\text{ s}$, Requirement D04).
- **[13] VDI 2206 Reference Documentation**  
  *Source / Reference:* [PDFCoffee VDI 2206 Archive](https://pdfcoffee.com/vdi-2206-4-pdf-free.html)  
  *System Relevance:* Reference digital distribution of VDI 2206 guidelines for multidisciplinary validation and system integration.
- **[45] Wandlungsfähige und angepasste Automation in der Automobilmontage mittels durchgängigem modularem Engineering**  
  *Source / Reference:* ZeMA / Universität des Saarlandes Dissertation, [Document Link](https://publikationen.sulb.uni-saarland.de/bitstream/20.500.11880/27366/1/Diss%20Wandlungsf%C3%A4hige%20und%20angepasste%20Automation%20in%20der%20Automobilmontage%20mittels%20durchg%C3%A4ngigem%20modularem%20Engineering.pdf)  
  *System Relevance:* Modular systems engineering methodology for reconfigurable automation cells, supporting rapid physical sub-assembly decoupling (Requirement M01).
- **[47] Mechatronics with Experiments (2nd Edition)**  
  *Source / Reference:* Sabri Cetinkunt, Wiley Textbook (`material/mechatronic_principles/MechatronicswithExperiments2ndEditionbySabriCetinkunt-1.pdf`).  
  *System Relevance:* Applied engineering handbook for brushless DC motor drives, PWM gate timing, encoder quadrature decoding, and cascaded closed-loop fieldbus control (Requirement C01).
- **[75] Herzog, Jan (2023) — Entwicklung einer fähigkeitsbasierten Planungsmethode zur Wiederverwendbarkeit von Anlagen**  
  *Source / Reference:* Dissertation, Martin-Luther-Universität Halle-Wittenberg, [Repository Link](https://repo.bibliothek.uni-halle.de/bitstream/1981185920/113917/1/Herzog_Jan_Dissertation_2023.pdf) (DOI: 10.25673/111959).  
  *System Relevance:* Formulates formal capability-based planning and modeling (Product, Process, Resource, Skill/Capability - PPRS), directly justifying the Task Port architecture that decouples physical capabilities from task-level application intent.
- **[76] Reichel, Thomas; Rünger, Gudula; Steger, Daniel; Xu, Haibin (2010) — IT-Unterstützung zur energiesensitiven Produktentwicklung**  
  *Source / Reference:* Chemnitzer Informatik-Berichte CSR-10-02, Fakultät für Informatik, Technische Universität Chemnitz, [Repository Copy](file:///home/mohany/Projects/gp/semi-humanoid-robot-proposal/material/mechatronic_principles/2010_Reichel_ITUnterstuetzungZurEnergiesens_Monarch.pdf) / [Local Downloads](file:///home/mohany/Downloads/2010_Reichel_ITUnterstuetzungZurEnergiesens_Monarch.pdf).  
  *System Relevance:* Establishes computational methods for evaluating energy profiles during early-stage conceptual design, directly informing Section 4 Energy Flow modeling and battery runtime sizing (Requirements E01–E02).
- **[77] VDI Zentrum Ressourceneffizienz (VDI ZRE) — Kurzanalyse Nr. 20: Ressourceneffizienz durch Maßnahmen in der Produktentwicklung**  
  *Source / Reference:* VDI Technologiezentrum GmbH, [Report Link](https://www.ressource-deutschland.de/fileadmin/user_upload/1_Themen/h_Publikationen/Kurzanalysen/VDI-ZRE_Kurzanalyse_Nr._20_Produktentwicklung_bf.pdf).  
  *System Relevance:* Details lightweighting measures, material reduction strategies, and modular component integration to minimize structural inertia and parasitic battery drain.
- **[78] Gehrke, Matthias (2006) — Entwurf mechatronischer Systeme auf Basis von Funktionshierarchien und Systemstrukturen**  
  *Source / Reference:* Dissertation, Heinz Nixdorf Institut, Universität Paderborn (s-lab), [PDF Link](https://web.cs.upb.de/archive/s-lab/fileadmin/Informatik/slab/veroeffentlichungen/2006_Entwurf_mechatronischer_Systeme_auf_Basis_von_Funktionshierarchien_und_Systemstrukturen.pdf).  
  *System Relevance:* Directly underpins Section 4 by formalizing the derivation of functional hierarchies from requirements and their systematic mapping onto concrete physical system architectures (Funktions- und Systemstrukturen).
- **[79] Leitfaden zur agilen, datenbasierten Produktentwicklung in der Windenergiebranche**  
  *Source / Reference:* RWTH Aachen Lehrstuhl für Software Engineering (Rumpe et al.), [Publication Link](https://www.se-rwth.de/publications/Leitfaden-zur-agilen-datenbasierten-Produktentwicklung-in-der-Windenergiebranche.pdf).  
  *System Relevance:* Provides procedural guidelines for integrating agile sprint cycles, continuous operational telemetry data, and model-based software engineering in complex mechatronic systems.
- **[80] Plötner, Maik (2018) — Integriertes Vorgehen zur selbstindividualisierungsgerechten Produktstrukturplanung**  
  *Source / Reference:* Dissertation, Technische Universität München (TUM), Fakultät für Maschinenwesen, [Dissertation Link](https://mediatum.ub.tum.de/doc/1355438/1355438.pdf).  
  *System Relevance:* Formulates modular product architecture rules that support field-level modular customization, interchangeable end-effectors, and standardized mechanical interfaces (Requirement M01).

---

### Category 2: Benchmark Competitions, Operational Service Tasks & Manipulation In-The-Wild

Empirical performance standards, international service robotics league rules (RoboCup@Home), manipulation benchmarking, and in-the-wild grasp strategies.

- **[10] Competition Videos - RoboCup@Home**  
  *Source / Reference:* [RoboCup@Home Video Archive](https://athome.robocup.org/2021-videos/)  
  *System Relevance:* Provides qualitative behavioral benchmarks and failure mode demonstrations across GPSR, cleaning, and social interaction challenges.
- **[14] RoboCup@Home Rules and Regulations (2018)**  
  *Source / Reference:* RoboCup Federation, [Rulebook Link](https://athome.robocup.org/wp-content/uploads/2018/10/2018_rulebook.pdf)  
  *System Relevance:* Foundational operational specification establishing doorway clearance constraints ($\ge 750\text{ mm}$, G03), standard table heights ($750\text{ mm}$), and safety protocol limits.
- **[15] Development of RoboCup@Home Simulation towards Long-Term Service**  
  *Source / Reference:* RoboCup Symposium Proceedings, [Paper Link](http://www.sigverse.org/wiki/en/index.php?plugin=attach&refer=Paper%20Lists&openfile=RoboCupSymp2013.pdf)  
  *System Relevance:* Simulation methodologies for evaluating social navigation, persistent mapping, and human-robot interaction over extended temporal horizons.
- **[16] RoboCup@Home: Analysis and Results of Evolving Competitions**  
  *Source / Reference:* L. Iocchi et al., Artificial Intelligence, [Preprint Link](https://iris.uniroma1.it/retrieve/e383532b-a848-15e8-e053-a505fe0a3de9/Iocchi_preprint_RoboCup%40Home_2015.pdf)  
  *System Relevance:* Longitudinal empirical study quantifying baseline success rates in SLAM navigation, speech parsing, and pick-and-place manipulation under competitive conditions.
- **[17] Benchmarking Intelligent Service Robots through Scientific Competitions: The RoboCup@Home Approach**  
  *Source / Reference:* ResearchGate Article, [Publication Link](https://www.researchgate.net/publication/253650395_Benchmarking_Intelligent_Service_Robots_through_Scientific_Competitions_the_RoboCupHome_approach)  
  *System Relevance:* Establishes methodology for deriving reproducible engineering metrics from unstructured domestic service tasks.
- **[18] RoboCupAtHome/gpsr_command_generator**  
  *Source / Reference:* Official GitHub Repository, [Repository Link](https://github.com/RoboCupAtHome/gpsr_command_generator)  
  *System Relevance:* Formal context-free grammar engine generating multi-tier randomized natural language action requests for GPSR Categories I, II, and III.
- **[19] Semantic Reasoning in Service Robots Using Expert Systems**  
  *Source / Reference:* ResearchGate Article, [Publication Link](https://www.researchgate.net/publication/330730957_Semantic_reasoning_in_service_robots_using_expert_systems)  
  *System Relevance:* Informs high-level semantic task parsing, situational ambiguity resolution, and conversational clarification routines.
- **[20] Rearrangement: A Challenge for Embodied AI**  
  *Source / Reference:* D. Batra et al., ResearchGate, [Publication Link](https://www.researchgate.net/publication/345316601_Rearrangement_A_Challenge_for_Embodied_AI)  
  *System Relevance:* Mathematical formalization of embodied physical rearrangement over the special Euclidean group $SE(3)$, defining workspace transformation from $s_0$ to $s^*$.
- **[21] Demonstrating Everyday Manipulation Skills in RoboCup@Home**  
  *Source / Reference:* J. Stückler et al., IEEE Robotics & Automation Magazine, [Paper Link](https://www.ais.uni-bonn.de/papers/RAM_2012_Home.pdf)  
  *System Relevance:* Details physical implementation of table clearing, dishwasher rack loading, and door opening, establishing grasp span parameters ($20\text{--}85\text{ mm}$) and contact forces.
- **[64] Business Insider — Complex Manipulation Tasks Demonstration**  
  *Source / Reference:* Video Feature Report, [Media Link](https://www.facebook.com/businessinsider/posts/i-think-these-are-probably-the-most-complex-tasks-ever-being-performed-by-a-robo/1341100961221518/)  
  *System Relevance:* Visual industry evidence demonstrating cutting-edge high-complexity manipulation, bimanual coordination, and dexterity thresholds in commercial deployments.
- **[81] RoboCup 2019 International Symposium Program & Proceedings**  
  *Source / Reference:* International RoboCup Federation (Sydney, Australia), [Program Link](https://2019.robocup.org/downloads/program/2019RCS-Program_v12.pdf)  
  *System Relevance:* Outlines technical advances and benchmark revisions in mobile service robotics, deep learning perception pipelines, and autonomous manipulation.
- **[82] RoboCup@Home Rules and Regulations (Foundational Rulebook 2009)**  
  *Source / Reference:* University of Groningen Archive, [Rulebook Link](https://www.ai.rug.nl/robocupathome/documents/rulebook2009_DRAFT.pdf)  
  *System Relevance:* Historical baseline defining early core benchmarks (Who-is-Who, Fetch & Carry, Open Challenge) that formed modern service robotics metrics.
- **[85] Stückler, J.; Schwarz, M.; Schadler, M.; Topalidou-Kyniazopoulou, A.; Behnke, S. (2016) — Cognitive Service Robot Cosero**  
  *Source / Reference:* Frontiers in Robotics and AI, [Article Link](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2016.00058/full)  
  *System Relevance:* Canonical mobile manipulator architecture featuring dual 7-DoF arms, an active torso lift, and an omnidirectional drive base; benchmarks tool use (bottle opening) and intuitive physical handover.
- **[86] SHOPPER: Practical Insights on Grasp Strategies for Mobile Manipulation in the Wild (2025)**  
  *Source / Reference:* arXiv:2504.12512 [cs.RO], [Paper Link](https://arxiv.org/html/2504.12512v2)  
  *System Relevance:* Provides real-world empirical data on grasping strategies under dense clutter, multi-angle approach vectors, and payload stability across varying object geometries in supermarket and home settings.

---

### Category 3: Reference Mobile Manipulators, Humanoid Morphologies & Open Hardware

State-of-the-art commercial and academic mobile manipulators, open-hardware bimanual platforms, kinematics, actuators, and computing architectures.

- **[5] TIAGo Pro Datasheet (PAL Robotics, 2025)**  
  *Source / Reference:* PAL Robotics Commercial Datasheet, [PDF Link](https://pal-robotics.com/wp-content/uploads/2025/05/2025-Datasheet-TIAGo-Pro.pdf)  
  *System Relevance:* Primary benchmark for modular semi-humanoid architecture: Series Elastic Actuators, dual 7-DoF arms ($3.0\text{ kg}$ continuous payload), $350\text{ mm}$ prismatic lift, and 1 kHz EtherCAT fieldbus.
- **[6] TIAGo Hardware Overview (PAL OS 24.9 Documentation)**  
  *Source / Reference:* PAL Robotics Developer Portal, [Documentation Link](https://docs.pal-robotics.com/sdk/24.09/hardware/tiago/hardware-overview.html)  
  *System Relevance:* Technical reference for onboard power management, safety contactor circuits, and heterogeneous compute allocation.
- **[9] TIAGo Pro Specs & Technical Review**  
  *Source / Reference:* Origin of Bots (OOB), [Review Link](https://www.originofbots.com/robot/tiago-pro-by-pal-robotics-details-specifications-rating)  
  *System Relevance:* Engineering breakdown of mechanical degrees of freedom, reach envelope, and operational duty cycles.
- **[11] TIAGo Pro — Empowering Mobile Manipulation**  
  *Source / Reference:* PAL Robotics Platform Portal, [Product Link](https://pal-robotics.com/robot/tiago-pro/)  
  *System Relevance:* Application cases for mobile manipulation, ROS 2 integration, and human-safe collaborative interaction.
- **[12] ROBOTIS AI Sapiens K0 Platform**  
  *Source / Reference:* Humanoids Daily News, [Article Link](https://www.humanoidsdaily.com/news/robotis-enters-the-open-source-humanoid-arena-with-ai-sapiens-k0-platform)  
  *System Relevance:* Open-source humanoid research platform highlighting modular DYNAMIXEL smart actuators and distributed bus control.
- **[24] AhaRobot: A Low-Cost Open-Source Bimanual Mobile Manipulator (2025)**  
  *Source / Reference:* arXiv:2503.10070 [cs.RO], [Paper Link](https://arxiv.org/html/2503.10070v2)  
  *System Relevance:* Architectural reference for low-cost bimanual mobile manipulation, open-source Bill of Materials, and accessible fabrication techniques.
- **[25] Low-Cost Bimanual Mobile Manipulation (Mobile ALOHA)**  
  *Source / Reference:* Stanford University / Zipeng Fu et al., [Preprint Link](https://arxiv.org/pdf/2401.02117)  
  *System Relevance:* Reference platform coupling an AgileX Tracer differential base with dual ViperX arms; validates imitation learning for fine domestic tasks (cooking, wiping).
- **[26] System Architecture for Low-Cost, GPU-Accelerated Bimanual Manipulation (2026)**  
  *Source / Reference:* arXiv:2603.09051 [cs.RO], [Paper Link](https://arxiv.org/html/2603.09051v2)  
  *System Relevance:* Informs edge GPU integration, multi-camera USB/Ethernet pipeline synchronization, and hard real-time motor thread isolation.
- **[27] TIAGo Head: An AI Powered Platform for Social Robotics**  
  *Source / Reference:* ResearchGate Publication, [Publication Link](https://www.researchgate.net/publication/397228140_TIAGo_Head_an_AI_Powered_Platform_for_Social_Robotics)  
  *System Relevance:* 2-DoF active pan-tilt head kinematics, microphone array placement, and RGB-D sensor synchronization for natural gaze tracking (Requirement S02).
- **[28] An Open-Source Holonomic Mobile Manipulator for Robot Learning**  
  *Source / Reference:* CoRL / MLResearch Proceedings, [Paper Link](https://raw.githubusercontent.com/mlresearch/v270/main/assets/wu25a/wu25a.pdf)  
  *System Relevance:* Evaluates omnidirectional Mecanum chassis dynamics during dynamic manipulation, demonstrating simplified Cartesian IK solving.
- **[30] Asimov 1 Open-Source Humanoid Robot**  
  *Source / Reference:* Menlo Research GitHub Repository, [Repository Link](https://github.com/menloresearch/asimov-1)  
  *System Relevance:* Open-source hardware CAD and firmware; demonstrates Quasi-Direct Drive (QDD) actuators, 7075 aluminum CNC machining, and MJF PA12 nylon structural components.
- **[33] The Humanoid Open Source Robot Reachy 2 of Pollen Robotics**  
  *Source / Reference:* Xpert.digital Review, [Article Link](https://xpert.digital/en/humanoid-open-source-robots/)  
  *System Relevance:* Architectural overview of Reachy 2's anthropomorphic upper body, Orbita spherical joint modules, and teleoperation control stacks.
- **[34] Reachy 2 Technical Profile**  
  *Source / Reference:* Robot Harbour, [Product Profile](https://robotharbour.com/robot/reachy-2/)  
  *System Relevance:* Kinematic workspace boundaries, dual-arm horizontal reach ($1400\text{ mm}$), and $3.0\text{ kg}$ payload specifications.
- **[35] Reachy 2 Dual Arms with Mobile Base Datasheet**  
  *Source / Reference:* Pollen Robotics Technical Datasheet, [PDF Link](https://pollen-robotics.com/assets/reachy2/datasheets/reachy2-dual-arm-mobile-base.pdf)  
  *System Relevance:* Engineering specifications for integrating Reachy 2's upper torso onto an omnidirectional wheeled base.
- **[36] Motors & Actuators Specifications — Reachy 2**  
  *Source / Reference:* Pollen Robotics Hardware Guide, [Documentation Link](https://docs.pollen-robotics.com/hardware-guide/specifications/motors-actuators/)  
  *System Relevance:* Joint-level torque limits, brushless motor windings, gear reduction ratios, and thermal dissipation metrics.
- **[37] Research Platforms Catalogue**  
  *Source / Reference:* Chironix Robotics Portal, [Catalogue Link](https://chironix.com/robots/research-platforms/)  
  *System Relevance:* Commercial distribution and integration reference for academic service robotics platforms.
- **[38] AgileX Mobile ALOHA Ver. 2 Overview**  
  *Source / Reference:* WeGo Robotics Commercial Specification, [Product Link](https://wego-robotics.com/robot/AGILEX_MOBILE_ALOHA_ver2_detail.php)  
  *System Relevance:* Commercialized turnkey implementation of Mobile ALOHA featuring industrial PiPER arms and CAN bus architectures.
- **[39] Development of an Autonomous Mobile Manipulator for Industrial Applications**  
  *Source / Reference:* Andrea Giampà, Master's Thesis, Politecnico di Milano (2024), [Thesis Link](https://www.politesi.polimi.it/retrieve/60b35cd7-fc91-47da-9139-99722300c063/2024_07_Giampa_thesis.pdf)  
  *System Relevance:* Detailed kinematic inversion algorithms, hardware-in-the-loop validation, and ROS 2 Nav2/MoveIt 2 configuration on mobile platforms.
- **[41] Asimov 1: The $20,000 IKEA Humanoid for Robot Builders**  
  *Source / Reference:* RoboHorizon Technical Review (2026), [Article Link](https://robohorizon.uk/en-gb/magazine/2026/08/asimov-1-the-20000-ikea-humanoid-for-robot-builders/)  
  *System Relevance:* Detailed breakdown of modular flat-pack mechanical assembly, distributed CAN bus topology, and cost-optimized bill of materials.
- **[42] Beyond the Kit: Asimov Details the 100-Hour Path to a Walking Humanoid**  
  *Source / Reference:* Humanoids Daily Technical Feature, [Article Link](https://www.humanoidsdaily.com/news/beyond-the-kit-asimov-details-the-100-hour-path-to-a-walking-humanoid)  
  *System Relevance:* Assembly timing, fabrication tolerances, and integration overhead analysis for open-source humanoid hardware.
- **[43] How We Built Humanoid Legs from the Ground Up in 100 Days**  
  *Source / Reference:* Menlo Research Engineering Blog, [Blog Link](https://menlo.ai/research/humanoid-legs-100-days)  
  *System Relevance:* Quasi-Direct Drive (QDD) design methodologies, cycloidal/planetary gear comparisons, and structural finite element analysis.
- **[44] Open-Source Humanoid Robots in 2025: A Practical Guide**  
  *Source / Reference:* RoboticsCenter AI Guide, [Guide Link](https://www.roboticscenter.ai/blog/open-source-humanoid-robots-2025)  
  *System Relevance:* Comparative technical survey evaluating accessible open-source humanoid and mobile manipulator frameworks.
- **[46] Mirokaï by Enchanted Tools Specs & Review**  
  *Source / Reference:* Origin of Bots (OOB), [Review Link](https://www.originofbots.com/robot/miroka-by-enchanted-tools-details-specifications-rating)  
  *System Relevance:* Expressive social service robot with ball-based omnidirectional mobility, compact footprint, and specialized logistics grippers.
- **[62] Intermediate 3D-Printable Robots — orobot.io**  
  *Source / Reference:* orobot.io Repository, [Directory Link](https://orobot.io/robots/difficulty/intermediate)  
  *System Relevance:* Database of intermediate-complexity 3D-printable robotic links, cycloidal gearheads, and compliant grippers for rapid physical prototyping.
- **[63] YOR: Your Own Mobile Manipulator for Generalizable Robotics**  
  *Source / Reference:* ResearchGate Technical Paper, [Publication Link](https://www.researchgate.net/publication/400705357_YOR_Your_Own_Mobile_Manipulator_for_Generalizable_Robotics)  
  *System Relevance:* Open-architecture mobile manipulation platform designed for low-cost, generalizable policy learning, providing an accessible reference for modular arm and base integration.
- **[65] Menlo Research Official Engineering Portal**  
  *Source / Reference:* Menlo Research Portal, [Homepage Link](https://menlo.ai)  
  *System Relevance:* Central repository for open-source CAD releases, firmware distributions, and hardware errata for the Asimov platform series.
- **[84] Lucio at RoboCup@Home: An Open-Hardware Mobile Manipulator with Modular Software and On-Device LLM Planning**  
  *Source / Reference:* IDOLL Research Technical Report, [Project Link](https://www.idoll.love/en/our-research/lucio-at-robocup-home)  
  *System Relevance:* Highly relevant open-hardware mobile manipulator competing at RoboCup@Home, featuring modular structural design, ROS 2 software nodes, and on-device language-model task planning.

---

### Category 4: Embodied AI, Vision-Language-Action (VLA) & Machine Ethics

Embodied artificial intelligence foundation models (RT-X, OpenVLA), training data infrastructure, policy execution bandwidth, and formal ethical/safety supervisory constraints.

- **[22] A Contemporary Survey on Intelligent Human-Robot Interfaces Focused on NLP**  
  *Source / Reference:* ResearchGate Survey, [Publication Link](https://www.researchgate.net/publication/342720301_A_Contemporary_Survey_on_Intelligent_Human-Robot_Interfaces_Focused_on_Natural_Language_Processing)  
  *System Relevance:* Human-robot natural language interaction, dialogue management architectures, and intent recognition pipelines.
- **[49] Sample-Efficient Robot Skill Learning For Construction Tasks**  
  *Source / Reference:* Scribd Academic Document, [Document Link](https://www.scribd.com/document/1015146710/2512-14031v1)  
  *System Relevance:* Sample-efficient reinforcement learning and imitation learning for contact-rich manipulation tasks.
- **[50] Open X-Embodiment: Robotic Learning Datasets and RT-X Models**  
  *Source / Reference:* Open X-Embodiment Collaboration, [Project Link](https://robotics-transformer-x.github.io/)  
  *System Relevance:* Foundational cross-embodiment dataset aggregating over 1 million trajectories; underpins RT-1 and RT-2 Transformer policies.
- **[52] OpenVLA: An Open-Source Vision-Language-Action Model**  
  *Source / Reference:* OpenVLA Project / Stanford & UC Berkeley, [Project Link](https://openvla.github.io/)  
  *System Relevance:* 7B-parameter open-source VLA model directly outputting 7-DoF end-effector control increments from RGB observations and natural language instructions.
- **[55] Anderson, Michael; Leigh Anderson, Susan (Eds.) — Machine Ethics**  
  *Source / Reference:* Cambridge University Press, [Book Link](https://dokumen.pub/machine-ethics-9780521112352-0521112354.html)  
  *System Relevance:* Foundational text establishing formal mathematical and rule-based ethical constraints in autonomous decision-making agents; directly informs the Task Port safety supervisor rules for human-inhabited environments.
- **[58] There's An AI For That — AI Tools for Robotics**  
  *Source / Reference:* Aggregator Directory, [Platform Link](https://theresanaiforthat.com/task/robotics/)  
  *System Relevance:* Curated tracking directory of generative AI tools, vision backbones, and simulation utilities applied to robotic perception and control.
- **[61] There's An AI For That — AI Tools for Task Automation**  
  *Source / Reference:* Aggregator Directory, [Platform Link](https://theresanaiforthat.com/task/task-automation/)  
  *System Relevance:* Directory of autonomous task orchestration frameworks, workflow state machines, and API integration agents.
- **[73] Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines (2026)**  
  *Source / Reference:* arXiv:2604.23001 [cs.RO], [Paper Link](https://arxiv.org/html/2604.23001v1)  
  *System Relevance:* Authoritative 2026 survey synthesizing current VLA models, multi-modal demonstration datasets, real-to-sim validation loops, and data generation engines for physical manipulation.
- **[74] What Vision-Language-Action Models Need from Training Data — Avala AI**  
  *Source / Reference:* Avala AI Technical Report, [Article Link](https://avala.ai/news/vla-data-requirements-training-infrastructure)  
  *System Relevance:* Outlines data infrastructure requirements for training VLA models, including multi-view visual tokenization, high-frequency proprioceptive trajectory logging, and latency considerations (Requirement A03).

---

### Category 5: Healthcare, Assistive Technologies & Collaborative Robotics

Assistive manipulation primitives, human-robot physical collaboration standards (ISO/TS 15066), eldercare service robots, and clinical deployment requirements.

- **[8] Jesus Savage — Autonomous Service Robotics & Human-Robot Interaction**  
  *Source / Reference:* UNAM / RoboCup Trustee Profile, [ResearchGate Profile](https://www.researchgate.net/profile/Jesus-Savage)  
  *System Relevance:* Research contributions in autonomous domestic navigation, cognitive service architectures, and competitive evaluation protocols.
- **[23] CHARMIE: A Collaborative Healthcare and Home Service and Assistant Robot (Semantic Scholar)**  
  *Source / Reference:* Semantic Scholar Publication, [PDF Link](https://pdfs.semanticscholar.org/a7c8/c3250a76375a49223ac9482fb1c5c0fcc60c.pdf)  
  *System Relevance:* Architectural baseline for collaborative assistive robots operating in healthcare and domestic settings.
- **[60] International Federation of Robotics (IFR) — STIHL Opens Up New Fields with Cobots**  
  *Source / Reference:* IFR Case Study, [Report Link](https://ifr.org/case-studies/collaborative-robots/stihl-opens-up-new)  
  *System Relevance:* Real-world collaborative robot implementation detailing physical safety enclosures, ISO collaborative speed limits, and ergonomic human-cobot handovers.
- **[71] Assistive Technologies in Care and Rehabilitation**  
  *Source / Reference:* MDPI Book Edition, [Book Link](https://mdpi-res.com/bookfiles/book/11830/Assistive_Technologies_in_Care_and_Rehabilitation.pdf?v=1787965968)  
  *System Relevance:* Peer-reviewed compendium addressing assistive robotic kinematics, wheelchair-accessible manipulation, user physical safety, and ethical caregiving constraints.
- **[72] Service Robots in the Healthcare Sector**  
  *Source / Reference:* ResearchGate Systematic Review, [Publication Link](https://www.researchgate.net/publication/349976485_Service_Robots_in_the_Healthcare_Sector)  
  *System Relevance:* Comprehensive analysis of service robots in hospital and eldercare environments; provides operational metrics for sanitization, navigation in crowded corridors, and delivery payloads.
- **[83] Ribeiro, Tiago et al. — CHARMIE: Healthcare and Home Service Assistant Robot for Elderly Care**  
  *Source / Reference:* ResearchGate Full Article, [Publication Link](https://www.researchgate.net/publication/353742553_CHARMIE_A_Collaborative_Healthcare_and_Home_Service_and_Assistant_Robot_for_Elderly_Care)  
  *System Relevance:* Upgraded full peer-reviewed documentation of the CHARMIE platform [complements [cite: 23]]; details the torso lift mechanism, bimanual arm payloads, and real-world trials in domestic and eldercare facilities.

---

### Category 6: Market Intelligence, Directories, Technical Feeds & Infrastructure

Industry market forecasts, hardware marketplace indices, commercial humanoid benchmarking, and open-source embedded software infrastructure.

- **[7] project_overview.pdf**  
  *Source / Reference:* Internal Proposal Specification, `reports/project_overview/project_overview.pdf`.  
  *System Relevance:* Core scope document detailing baseline requirements, budget constraints, and project development milestones.
- **[29] useful_links.md**  
  *Source / Reference:* Repository Resource Index, [Local File](file:///home/mohany/Projects/gp/semi-humanoid-robot-proposal/material/useful_links.md).  
  *System Relevance:* Internal repository directory cataloging robotics market analyses, robot datasheets, and open-source software libraries.
- **[31] 38 Best Humanoid Robots in 2026 (Evidence-Ranked)**  
  *Source / Reference:* Robozaps Market Report, [Report Link](https://blog.robozaps.com/b/best-humanoid-robots)  
  *System Relevance:* Commercial benchmarking ranking contemporary humanoid and semi-humanoid systems across payload, autonomy, and market readiness.
- **[32] HRI 2023 — Human-Robot Interaction Conference Proceedings**  
  *Source / Reference:* ACM/IEEE HRI 2023, [Proceedings Link](https://humanrobotinteraction.org/2023/toc/index.html)  
  *System Relevance:* Research papers on non-verbal communication, social distance maintenance, and multimodal human tracking.
- **[40] Birdwave Market**  
  *Source / Reference:* Birdwave Hardware Marketplace, [Market Link](https://market.birdwave.io/)  
  *System Relevance:* Sourcing directory for smart servo actuators, brushless motors, harmonic drive gearboxes, and LiDAR sensors.
- **[48] Learn – Robohub**  
  *Source / Reference:* Robohub Educational Category Feed, [Feed Link](https://robohub.org/category/learn/feed/)  
  *System Relevance:* Educational tutorials and engineering articles covering mechatronics, motion planning, and robot ethics.
- **[51] updates.md**  
  *Source / Reference:* Internal Milestone Tracker, `reports/detailed_project_description/updates.md`.  
  *System Relevance:* Working development log detailing functional allocation across mechanical, electrical, and software engineering domains.
- **[53] Robohub Main RSS Feed**  
  *Source / Reference:* Robohub Syndicate Feed, [Feed Link](https://robohub.org/feed/)  
  *System Relevance:* Continuous news feed tracking global robotics research breakthroughs, university lab releases, and industry partnerships.
- **[54] Robohub Sensors RSS Feed**  
  *Source / Reference:* Robohub Perception & Sensor Stream, [Feed Link](https://robohub.org/search/sensors/feed/rss2/)  
  *System Relevance:* Continuous RSS feed monitoring developments in exteroceptive sensing, depth cameras, solid-state LiDAR, and tactile arrays (Requirement S01).
- **[56] Petter Reinholdtsen Technical Blog (Entries Tagged English)**  
  *Source / Reference:* Personal Technical Blog, [Blog Link](http://www.hungry.com/~pere/blog/tags/english/)  
  *System Relevance:* Technical articles on Debian Linux system administration, real-time packaging, and deterministic network service configurations.
- **[57] Review of 30+ Humanoid Robotics Companies: Who Will Prevail in 2026?**  
  *Source / Reference:* PANews on Binance Square, [Article Link](https://www.binance.com/en/square/post/325008783702337)  
  *System Relevance:* Broad market intelligence report profiling commercial humanoid ventures in 2026, comparing supply chain dependencies and commercial deployment viability.
- **[59] Humanoid Observer**  
  *Source / Reference:* Industry Publication Portal, [Portal Link](https://www.humanoidobserver.com)  
  *System Relevance:* Dedicated trade publication tracking humanoid hardware unveilings, VC investments, and technical benchmarking.
- **[66] Robot King — RoboHorizon Author Profile**  
  *Source / Reference:* RoboHorizon Contributor Archive, [Author Link](https://robohorizon.uk/en-gb/authors/robot-king/)  
  *System Relevance:* In-depth mechanical teardowns, actuator gear analysis, and engineering reviews of modern humanoid platforms.
- **[67] Research Robots Directory — ui44**  
  *Source / Reference:* ui44 Platform Catalogue, [Directory Link](https://ui44.com/categories/research)  
  *System Relevance:* Comprehensive database indexing commercial research robots, mobile manipulators (Stretch, TIAGo), and academic testbeds.
- **[68] Humanoid.guide Platform & Component Shop**  
  *Source / Reference:* Commercial Guide, [Shop Link](https://humanoid.guide/shop/page/4/)  
  *System Relevance:* Commercial aggregator tracking commercial pricing, specifications, and availability for humanoid robot platforms and actuators.
- **[69] Humanoids Daily Editorial Directory**  
  *Source / Reference:* Humanoids Daily Contributor Portal, [Editorial Link](https://www.humanoidsdaily.com/authors/default)  
  *System Relevance:* Technical news stream covering embodied AI breakthroughs, humanoid locomotion, and dexterity demonstrations.
- **[70] RoboHorizon Main Portal**  
  *Source / Reference:* RoboHorizon Technical Magazine, [Portal Link](https://robohorizon.uk/en-gb/)  
  *System Relevance:* Analytical magazine covering modern robotics engineering, embedded hardware topologies, and autonomous manipulation.
