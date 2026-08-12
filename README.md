# Modular Semi-Humanoid Robot — Research, Market & Design Proposal

**Building a $12K–18K, fully modular, wheeled semi-humanoid robot — the anthropomorphic reach and bimanual dexterity of a humanoid, without the expensive, unstable legs.**

This repository is the complete engineering evidence base behind a **flagship modular semi-humanoid robotics platform**: a system-level proposal that fuses an omnidirectional mobile base, a telescopic spine, dual 6–7 DoF tendon-driven arms, soft-rigid 5-finger hands, and an expressive 3-DoF perception head into one open, serviceable, fleet-ready machine.

It contains everything from raw source dossiers to professionally typeset deliverables:

- **Market analysis** (hardware + software) across the $20B+ mobile robotics sector
- **Literature reviews** (arXiv + OpenAlex) covering 2022–2026 state of the art
- **Systems architecture synthesis** distilled from 9 foundational research projects
- **A full software design report** with multi-rate autonomy, real-time safety, and sim-to-real architecture

---

## Why Semi-Humanoid?

Bipedal humanoids are spectacular — and expensive, unstable, and inefficient indoors. A wheeled semi-humanoid keeps the parts of a human that matter for work:

| Dimension | Wheeled Semi-Humanoid | Bipedal Humanoid |
|---|---|---|
| Continuous runtime | Up to ~8 h per charge | 1.5–2.5 h (active balance) |
| Payload stability | Static equilibrium over support polygon | Requires dynamic ZMP compensation |
| Control complexity | Standard ROS 2 Nav2 + MoveIt 2 stack | Whole-body gait, fall recovery |
| Regulatory path | Established (ISO/TS 15066, AMR codes) | Emerging, unsettled |
| Cost to build | **$12,000–$18,000** | $60K–$400K+ |

> The core research claim: the hard problem in semi-humanoid robotics is **not any single subsystem** — it is the *validated integration* of modular mechanics, isolated power domains, tactile contact, real-time safety, and VLA intelligence.

---

## System Vision

```
┌──────────────────────────────────────────────────────────────────────────┐
│                     MODULAR SEMI-HUMANOID PLATFORM                       │
├──────────────────────────────────────────────────────────────────────────┤
│  HEAD     3-DoF pan-tilt-roll gimbal + stereo RGB-D + 4-mic TDOA array   │
│  HANDS    Dual soft-rigid 5-finger hands, fingertip FSR, EMG interface   │
│  ARMS     Dual 6-7 DoF proximal tendon drives (low distal inertia)       │
│  TORSO    Topology-optimized "ribcage" chassis = passive heat sink       │
│  SPINE    1-2 DoF telescopic lift: 0.8 m tabletop → 1.8 m standing       │
│  BASE     Omnidirectional Mecanum/swerve + auto-docking BMS charge       │
├──────────────────────────────────────────────────────────────────────────┤
│  AI EDGE     NVIDIA Jetson Orin AGX (OpenVLA/Pi0, YOLOv11, SAM, TRT)     │
│  SPINAL CORD Dual STM32H7/ESP32 micro-ROS MCUs @ 1 kHz safety watchdog   │
│  POWER       Galvanically isolated dirty (24-48V) vs clean (12/19V)      │
│  TWIN        NVIDIA Isaac Sim OpenUSD digital twin, SIL → vHIL → real    │
└──────────────────────────────────────────────────────────────────────────┘
```

The platform is benchmarked against the current market (Hello Robot Stretch 3/4, Pollen Robotics Reachy 2, PAL TIAGo, Toyota HSR, legacy PR2) and targets the **gap between $25K single-arm platforms and $70K+ dual-arm humanoids** — with the goal of a **bimanual, open, modular** machine in the $12K–18K BOM range.

---

## Repository Layout

```
.
├── material/                          # Raw evidence & source dossiers
│   ├── meta/                          #   Working notes, key questions, roadmap
│   ├── useful_links.md                #   Curated market/tech link index
│   ├── literature_review/             #   arXiv + OpenAlex reviews (MD)
│   ├── market_analysis/               #   Hardware + software market studies (MD)
│   ├── robot_structure/               #   Reference full-body mechatronic PDFs
│   ├── projects/                      #   9 foundational project PDFs + synthesis
│   └── proposal_components/           #   Mechanical & electrical spec PDFs
│
└── reports/                           # Final typeset deliverables (LaTeX + PDF)
    ├── semi_humanoid_robotics_literature_review/          # Unified review
    ├── semi_humanoid_robotics_software_literature_review/ # Software review
    ├── market_analysis/                                    # Unified market report
    └── software_report/                                    # Software design report
```

---

## The Deliverables

### 1. Market Analysis — `reports/market_analysis/`
Why this is the right bet, with numbers to back it up.

- **Hardware market** — mobile manipulator segment forecast from **$1.52B (2025) → $3.95B (2032, 14.7% CAGR)**; AMMRs growing at **23.9% CAGR**
- **Software market** — software & ecosystem services represent **~67% of total mobile robotics market value**
- Competitive benchmark table across 5 commercial platforms (price, mass, payload, DoF, runtime, middleware)
- Cost-to-capability positioning analysis + TCO breakdown (~50% hardware, ~35% commissioning, ~15% licensing/maintenance)
- 4 strategic engineering directives: proximal tendon actuation, passive chassis cooling, AI/deterministic-control separation, VR-teleop data pipelines

### 2. Comprehensive Literature Review — `reports/semi_humanoid_robotics_literature_review/`
A 2022–2026 synthesis of platforms, control, embodied AI, and systems integration, consolidating:

- **arXiv review** — open platforms (YOR, Mobile ALOHA, Stretch), teleoperation (OmniH2O), VLA models (OpenVLA, SLIM), expressive HRI heads
- **OpenAlex review** — peer-reviewed tactile sensing, behavior trees, digital twins, proactive HRI, whole-body planning
- Identifies **five critical literature gaps**: modular quick-release interfaces, the VLM→1 kHz motor-loop safety chasm, power-domain isolation, expressive low-cost heads, and cost/fragility barriers

### 3. Software Literature Review — `reports/semi_humanoid_robotics_software_literature_review/`
The first-class software layer: multi-rate autonomy, real-time control, embodied AI, sim-to-real.

- Rate partitioning: **5–10 Hz cognition / 30–100 Hz planning / 100–500 Hz integration / 1 kHz real-time safety**
- Benchmarks of simulation engines (Isaac Sim, MuJoCo, Gazebo) and software stacks (Stretch vs Reachy 2 vs TIAGo)
- Identifies the **principal research gap: unspecified contracts between layers** — VLA→trajectory interpolation, base–arm coordination, jitter-isolated MCU control, tactile-force safety vetoes

### 4. Software Design Report — `reports/software_report/`
An implementation-oriented architecture for cognition, autonomy, safety, and fleet operations.

- Multi-rate execution model where **only the safety envelope may enforce actuator commands**
- Command contract: AI output is projected into the verified feasible set (`x_ref = Π_𝓕(x + Δx_AI)`)
- High-level stack: Whisper, OpenVLA/Pi0, YOLOv11, SAM, BehaviorTree.CPP missions, Nav2, MoveIt 2
- Low-level stack: EtherCAT/CAN-FD, micro-ROS, FreeRTOS firmware, impedance + tactile veto, safety state machine
- 4-phase implementation roadmap: safe platform → bounded autonomy → cognitive assistance → fleet productization

---

## Master Architecture Synthesis — `material/projects/projects_synthesis_architecture.md`

Nine foundational projects are merged into a single unified platform specification:

| Baseline project | Contributes |
|---|---|
| `robot_structure-1-27` | Full-body mechatronic reference (head, neck, ribcage torso, harmonic-drive shoulders, isolated power) |
| Project 01 — Pick-and-Place VLA | Single-arm OpenVLA/Pi0 manipulation, Jetson edge compute |
| Project 02 — Mobile VLA Assistant | Nav2 autonomy, voice HRI, semantic scene mapping |
| Project 03 — Strawberry Harvester | Isaac Sim OpenUSD digital twin, sim-to-real vHIL |
| Project 05 — Soft-Rigid Hand | 5-finger dexterous hand, tactile arrays, grasp control |
| Project 07 — WMS Forklift | Mecanum drive, WMS/IoT fleet integration, auto-docking |
| Project 08 — Multi-Floor (FLEXIBOT) | Elevator/door interaction, guarded force-aware motion |
| Project 09 — Empowered Grasp | Myoelectric EMG hand, ML grasp recognition |
| Project 15 — M4 Morphobot | Terrain-aware mobility, power distribution discipline |

The synthesis yields a **full feature-mapping matrix** — form factor, locomotion, arms, hands, perception, compute, power, navigation, AI, safety, and digital twin — for every project rolled into one platform.

---

## Key Technologies

| Layer | Stack |
|---|---|
| Middleware | ROS 2 (Humble/Jazzy), DDS / Zenoh, Docker containers |
| Navigation | Nav2, SLAM, MPPI/DWB planners, costmaps, speed zoning |
| Manipulation | MoveIt 2, `ros2_control`, whole-body coordination, guarded motion |
| AI / Perception | OpenVLA, Pi0, Whisper, YOLOv11, SAM, FoundationPose, nvblox, TensorRT |
| Real-time | micro-ROS, FreeRTOS, STM32H7/ESP32, EtherCAT / CAN-FD, 1 kHz impedance + watchdog |
| Simulation | NVIDIA Isaac Sim / Isaac Lab (OpenUSD), MuJoCo, Gazebo |
| Fleet | Signed OTA, telemetry, WMS/ERP/IoT adapters, staged rollout |

---

## Getting Started

This is a **research proposal / evidence base** — currently documentation-only. To work with the deliverables:

```bash
# Browse the final PDFs (precompiled)
open reports/semi_humanoid_robotics_literature_review/*.pdf
open reports/semi_humanoid_robotics_software_literature_review/*.pdf
open reports/market_analysis/*.pdf
open reports/software_report/*.pdf

# Rebuild any report from source (LaTeX)
cd reports/software_report
latexmk -pdf semi_humanoid_software_design_report.tex
```

---

## Project Status

- [x] General market analysis
- [x] Software market analysis
- [x] Technology extraction from 9 foundational projects (Siemens, Project 01/02, Dr. Mohammed Ibrahim projects)
- [x] arXiv + OpenAlex literature reviews (general & software)
- [x] Unified market report (hardware + software, LaTeX)
- [x] Unified general + software literature reviews
- [x] High-level software design report
- [ ] **Next:** check for integrity and comprehensiveness of reports and formatting for diagrams
- [ ] **Next:** enhanced hardware/mechanical design phase & prototype BOM

---

## License

Repository contents and all reports are provided for research and proposal purposes. See individual documents for source citations and attribution.

---

## Contributing

This is an academic/industrial proposal under active development. Questions, corrections, and collaboration offers are welcome — open an issue or reach out with feedback on the architecture synthesis.
