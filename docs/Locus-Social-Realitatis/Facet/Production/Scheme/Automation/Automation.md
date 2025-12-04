# Automation

> **Automation** refers to the use of systems, machines, software, and control logic to perform tasks with reduced or no human intervention.

## Structure

> Which are the dimensions of automation?

Every automation system includes:

- Sensing (perception)
- Actuation (execution)
- Control (logic or decision rules)
- Integration (connectivity, data flow)
- Computation (algorithms, ML models)
- Feedback (closed-loop behavior)
- Goals/Constraints (desired system behavior)

## Levels of Intelligende

> Which are the elvel of 'Inteleligence' in Automation?

| **Level**                            | **Description**                                                              |
| ------------------------------------ | ---------------------------------------------------------------------------- |
| **0 — Manual**                       | No automation. Human performs all actions; no sensing or logic.              |
| **1 — Assistive**                    | System provides information or alerts; human decides and acts.               |
| **2 — Fixed Automation**             | Predefined rules/scripts (PLC logic). No adaptation.                         |
| **3 — Reactive Automation**          | Closed-loop control. System senses and automatically adjusts actions.        |
| **4 — Adaptive Automation**          | System adjusts parameters or behavior based on changing conditions.          |
| **5 — Contextual Automation**        | System perceives and interprets its environment (vision, sensors, context).  |
| **6 — Predictive Automation**        | System forecasts future states and acts proactively.                         |
| **7 — Goal-Optimizing Automation**   | System selects actions to optimize goals under constraints.                  |
| **8 — Self-Learning Automation**     | System improves performance through learning (experience-based).             |
| **9 — Self-Managing Automation**     | Autonomic: self-configuring, self-healing, self-optimizing, self-protecting. |
| **10 — Collaborative Intelligence**  | Human–machine joint reasoning; shared situational understanding.             |
| **11 — Organizational Intelligence** | Automation coordinates entire processes/units (multi-agent, VSM-like).       |
| **12 — Meta-Cognitive Automation**   | System reasons about its own reasoning; redesigns its own models/processes.  |

## Production System

| **Type of Production System**                     | **Typical Automation Level**                            |
| ------------------------------------------------- | ------------------------------------------------------- |
| **Craft / Manual Production System**              | **0–1** (Manual / Assistive)                            |
| **Workshop / Job Shop**                           | **1–2** (Assistive → Basic Automation)                  |
| **Mechanized Production System**                  | **2** (Fixed Logic / Mechanized)                        |
| **Classical Automated Production Line**           | **2–3** (Fixed Logic → Reactive)                        |
| **CNC-Based Production System**                   | **3–4** (Reactive → Adaptive)                           |
| **Lean Automated Cell**                           | **3–4** (Reactive → Adaptive)                           |
| **Robotic Production Cell**                       | **3–5** (Reactive → Contextual)                         |
| **Flexible Manufacturing System (FMS)**           | **4–6** (Adaptive → Predictive)                         |
| **Computer-Integrated Manufacturing (CIM)**       | **5–6** (Contextual → Predictive)                       |
| **MES-Orchestrated Production System**            | **4–6** (Adaptive → Predictive Scheduling)              |
| **Vision-Guided Robotic Line**                    | **5** (Contextual Automation)                           |
| **Digital Twin-Enabled Production System**        | **6–7** (Predictive → Goal-Optimizing)                  |
| **Smart Factory (Industry 4.0)**                  | **3–6** (Reactive → Predictive)                         |
| **Cognitive Factory**                             | **7–9** (Goal-Optimizing → Self-Managing)               |
| **Fully Autonomous Factory ("Lights-Out")**       | **9–11** (Self-Managing → Organizational Intelligence)  |
| **Distributed Cyber-Physical Production Network** | **10–11** (Collaborative / Organizational Intelligence) |
| **Self-Governing Production Ecosystem**           | **11–12** (Meta-Cognitive Automation)                   |

## Automation Stack

A canonical architecture:

- Physical Layer (machines, robots)
- Control Layer (PLC, CNC, PID)
- Execution Layer (MES, SCADA)
- Optimization Layer (APS, scheduling engines)
- Intelligence Layer (ML, RL, digital twins)
- Orchestration Layer (multi-agent coordination)

## References

- Frohm, Jörgen, et al. "Levels of automation in manufacturing." Ergonomia-an International journal of ergonomics and human factors 30.3 (2008).
