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

> 1. Lecture 2 and 3 \- VDI.pdf  
> 2. VDI 2206.pdf  
> 3. Lecture 01.pdf  
> 4. Lecture 1 \- Mechatronic System Design Principles.pdf  
> 5. TIAGo Pro | PAL Robotics, [https://pal-robotics.com/wp-content/uploads/2025/05/2025-Datasheet-TIAGo-Pro.pdf](https://pal-robotics.com/wp-content/uploads/2025/05/2025-Datasheet-TIAGo-Pro.pdf)  
> 6. TIAGo hardware overview \- PAL OS 24.9 documentation, [https://docs.pal-robotics.com/sdk/24.09/hardware/tiago/hardware-overview.html](https://docs.pal-robotics.com/sdk/24.09/hardware/tiago/hardware-overview.html)  
> 7. project\_overview.pdf  
> 8. Jesus SAVAGE | Professor | Doctor of Philosophy \- ResearchGate, [https://www.researchgate.net/profile/Jesus-Savage](https://www.researchgate.net/profile/Jesus-Savage)  
> 9. TIAGo Pro by PAL Robotics Specs & Review | OOB \- Origin of Bots, [https://www.originofbots.com/robot/tiago-pro-by-pal-robotics-details-specifications-rating](https://www.originofbots.com/robot/tiago-pro-by-pal-robotics-details-specifications-rating)  
> 10. Competition Videos \- RoboCup@Home, [https://athome.robocup.org/2021-videos/](https://athome.robocup.org/2021-videos/)  
> 11. TIAGo Pro \- Empowering Mobile Manipulation \- PAL Robotics, [https://pal-robotics.com/robot/tiago-pro/](https://pal-robotics.com/robot/tiago-pro/)  
> 12. ROBOTIS Enters the Open-Source Humanoid Arena with "AI, [https://www.humanoidsdaily.com/news/robotis-enters-the-open-source-humanoid-arena-with-ai-sapiens-k0-platform](https://www.humanoidsdaily.com/news/robotis-enters-the-open-source-humanoid-arena-with-ai-sapiens-k0-platform)  
> 13. Vdi 2206 \- PDFCOFFEE.COM, [https://pdfcoffee.com/vdi-2206-4-pdf-free.html](https://pdfcoffee.com/vdi-2206-4-pdf-free.html)  
> 14. RoboCup@Home Rules and Regulations, [https://athome.robocup.org/wp-content/uploads/2018/10/2018\_rulebook.pdf](https://athome.robocup.org/wp-content/uploads/2018/10/2018_rulebook.pdf)  
> 15. Development of RoboCup@Home Simulation towards Long-term, [http://www.sigverse.org/wiki/en/index.php?plugin=attach\&refer=Paper%20Lists\&openfile=RoboCupSymp2013.pdf](http://www.sigverse.org/wiki/en/index.php?plugin=attach&refer=Paper+Lists&openfile=RoboCupSymp2013.pdf)  
> 16. RoboCup@Home: Analysis and Results of Evolving Competitions, [https://iris.uniroma1.it/retrieve/e383532b-a848-15e8-e053-a505fe0a3de9/Iocchi\_preprint\_RoboCup%40Home\_2015.pdf](https://iris.uniroma1.it/retrieve/e383532b-a848-15e8-e053-a505fe0a3de9/Iocchi_preprint_RoboCup%40Home_2015.pdf)  
> 17. (PDF) Benchmarking Intelligent Service Robots through Scientific, [https://www.researchgate.net/publication/253650395\_Benchmarking\_Intelligent\_Service\_Robots\_through\_Scientific\_Competitions\_the\_RoboCupHome\_approach](https://www.researchgate.net/publication/253650395_Benchmarking_Intelligent_Service_Robots_through_Scientific_Competitions_the_RoboCupHome_approach)  
> 18. RoboCupAtHome/gpsr\_command\_generator: Command generator, [https://github.com/RoboCupAtHome/gpsr\_command\_generator](https://github.com/RoboCupAtHome/gpsr_command_generator)  
> 19. (PDF) Semantic reasoning in service robots using expert systems, [https://www.researchgate.net/publication/330730957\_Semantic\_reasoning\_in\_service\_robots\_using\_expert\_systems](https://www.researchgate.net/publication/330730957_Semantic_reasoning_in_service_robots_using_expert_systems)  
> 20. (PDF) Rearrangement: A Challenge for Embodied AI \- ResearchGate, [https://www.researchgate.net/publication/345316601\_Rearrangement\_A\_Challenge\_for\_Embodied\_AI](https://www.researchgate.net/publication/345316601_Rearrangement_A_Challenge_for_Embodied_AI)  
> 21. Demonstrating Everyday Manipulation Skills in RoboCup@Home, [https://www.ais.uni-bonn.de/papers/RAM\_2012\_Home.pdf](https://www.ais.uni-bonn.de/papers/RAM_2012_Home.pdf)  
> 22. (PDF) A Contemporary Survey on Intelligent Human-Robot, [https://www.researchgate.net/publication/342720301\_A\_Contemporary\_Survey\_on\_Intelligent\_Human-Robot\_Interfaces\_Focused\_on\_Natural\_Language\_Processing](https://www.researchgate.net/publication/342720301_A_Contemporary_Survey_on_Intelligent_Human-Robot_Interfaces_Focused_on_Natural_Language_Processing)  
> 23. A Collaborative Healthcare and Home Service and Assistant Robot, [https://pdfs.semanticscholar.org/a7c8/c3250a76375a49223ac9482fb1c5c0fcc60c.pdf](https://pdfs.semanticscholar.org/a7c8/c3250a76375a49223ac9482fb1c5c0fcc60c.pdf)  
> 24. AhaRobot: A Low-Cost Open-Source Bimanual Mobile Manipulator, [https://arxiv.org/html/2503.10070v2](https://arxiv.org/html/2503.10070v2)  
> 25. arXiv:2401.02117v1 \[cs.RO\] 4 Jan 2024, [https://arxiv.org/pdf/2401.02117](https://arxiv.org/pdf/2401.02117)  
> 26. System Architecture for Low-Cost, GPU-Accelerated Bimanual, [https://arxiv.org/html/2603.09051v2](https://arxiv.org/html/2603.09051v2)  
> 27. TIAGo Head: an AI Powered Platform for Social Robotics, [https://www.researchgate.net/publication/397228140\_TIAGo\_Head\_an\_AI\_Powered\_Platform\_for\_Social\_Robotics](https://www.researchgate.net/publication/397228140_TIAGo_Head_an_AI_Powered_Platform_for_Social_Robotics)  
> 28. An Open-Source Holonomic Mobile Manipulator for Robot Learning, [https://raw.githubusercontent.com/mlresearch/v270/main/assets/wu25a/wu25a.pdf](https://raw.githubusercontent.com/mlresearch/v270/main/assets/wu25a/wu25a.pdf)  
> 29. useful\_links.md  
> 30. menloresearch/asimov-1 \- Open-Source Humanoid Robot \- GitHub, [https://github.com/menloresearch/asimov-1](https://github.com/menloresearch/asimov-1)  
> 31. 38 Best Humanoid Robots in 2026 (Evidence-Ranked) \- Blog, [https://blog.robozaps.com/b/best-humanoid-robots](https://blog.robozaps.com/b/best-humanoid-robots)  
> 32. HRI2023 \- Human-Robot Interaction, [https://humanrobotinteraction.org/2023/toc/index.html](https://humanrobotinteraction.org/2023/toc/index.html)  
> 33. The Humanoid Open Source Robot Reachy 2 of Pollen Robotics, [https://xpert.digital/en/humanoid-open-source-robots/](https://xpert.digital/en/humanoid-open-source-robots/)  
> 34. Reachy 2 \- Robot Harbour, [https://robotharbour.com/robot/reachy-2/](https://robotharbour.com/robot/reachy-2/)  
> 35. Reachy2 Dual arms with mobile base Datasheet \- Pollen Robotics, [https://pollen-robotics.com/assets/reachy2/datasheets/reachy2-dual-arm-mobile-base.pdf](https://pollen-robotics.com/assets/reachy2/datasheets/reachy2-dual-arm-mobile-base.pdf)  
> 36. Motors & Actuators specifications \- Reachy 2, [https://docs.pollen-robotics.com/hardware-guide/specifications/motors-actuators/](https://docs.pollen-robotics.com/hardware-guide/specifications/motors-actuators/)  
> 37. Research Platforms \- Chironix, [https://chironix.com/robots/research-platforms/](https://chironix.com/robots/research-platforms/)  
> 38. AGILEX MOBILE ALOHA ver.2 | 모바일매니플레이터 | 자율주행로봇, [https://wego-robotics.com/robot/AGILEX\_MOBILE\_ALOHA\_ver2\_detail.php](https://wego-robotics.com/robot/AGILEX_MOBILE_ALOHA_ver2_detail.php)  
> 39. Development of an Autonomous Mobile Manipulator for Industrial, [https://www.politesi.polimi.it/retrieve/60b35cd7-fc91-47da-9139-99722300c063/2024\_07\_Giampa\_thesis.pdf](https://www.politesi.polimi.it/retrieve/60b35cd7-fc91-47da-9139-99722300c063/2024_07_Giampa_thesis.pdf)  
> 40. Birdwave Market, [https://market.birdwave.io/](https://market.birdwave.io/)  
> 41. Asimov 1: The \$20000 IKEA Humanoid for Robot Builders, [https://robohorizon.uk/en-gb/magazine/2026/08/asimov-1-the-20000-ikea-humanoid-for-robot-builders/](https://robohorizon.uk/en-gb/magazine/2026/08/asimov-1-the-20000-ikea-humanoid-for-robot-builders/)  
> 42. Beyond the Kit: Asimov Details the 100-Hour Path to a Walking, [https://www.humanoidsdaily.com/news/beyond-the-kit-asimov-details-the-100-hour-path-to-a-walking-humanoid](https://www.humanoidsdaily.com/news/beyond-the-kit-asimov-details-the-100-hour-path-to-a-walking-humanoid)  
> 43. How we built humanoid legs from the ground up in 100 days, [https://menlo.ai/research/humanoid-legs-100-days](https://menlo.ai/research/humanoid-legs-100-days)  
> 44. Open-Source Humanoid Robots in 2025: A Practical Guide, [https://www.roboticscenter.ai/blog/open-source-humanoid-robots-2025](https://www.roboticscenter.ai/blog/open-source-humanoid-robots-2025)  
> 45. Formatvorlage Dissertation ZeMA \- Universität des Saarlandes, [https://publikationen.sulb.uni-saarland.de/bitstream/20.500.11880/27366/1/Diss%20Wandlungsf%C3%A4hige%20und%20angepasste%20Automation%20in%20der%20Automobilmontage%20mittels%20durchg%C3%A4ngigem%20modularem%20Engineering.pdf](https://publikationen.sulb.uni-saarland.de/bitstream/20.500.11880/27366/1/Diss%20Wandlungsf%C3%A4hige%20und%20angepasste%20Automation%20in%20der%20Automobilmontage%20mittels%20durchg%C3%A4ngigem%20modularem%20Engineering.pdf)  
> 46. Mirokaï by Enchanted Tools Specs & Review | OOB \- Origin of Bots, [https://www.originofbots.com/robot/miroka-by-enchanted-tools-details-specifications-rating](https://www.originofbots.com/robot/miroka-by-enchanted-tools-details-specifications-rating)  
> 47. MechatronicswithExperiments2ndEditionbySabriCetinkunt-1.pdf  
> 48. Learn – Robohub, [https://robohub.org/category/learn/feed/](https://robohub.org/category/learn/feed/)  
> 49. Sample-Efficient Robot Skill Learning For Construction Tasks, [https://www.scribd.com/document/1015146710/2512-14031v1](https://www.scribd.com/document/1015146710/2512-14031v1)  
> 50. Open X-Embodiment: Robotic Learning Datasets and RT-X Models, [https://robotics-transformer-x.github.io/](https://robotics-transformer-x.github.io/)  
> 51. updates.md  
> 52. OpenVLA: An Open-Source Vision-Language-Action Model, [https://openvla.github.io/](https://openvla.github.io/)