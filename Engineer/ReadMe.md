"In practical term, two things are needed to transfer these sorts of theoretical advantages to real world advantages: *the devices themselves* and *the methodologies to unlock their potential*."

## Application
"The following three application areas represent targets in the noisy auqntum computing era, prior to the implementation of quantul error correction and fault-tolerance.

- Optimization
- Simulating Nature
- Finding structure in data (including machine learning)" 

## Track performance improvement

The three basic metrics - *scale, quality,* and *speed*

- Size

    More qubits are obviously better, but only if increasing the number doesn't degrade performance (which can happen). We want more good quality qubits that don’t interfere with one another through crosstalk when we don’t want them to. The way the qubits are connected to one another is also important, and figuring out how best to do this represents a challenge for superconducting qubit circuits.

- Quality

    Another important performance metric we track is two-qubit gate fidelity. Gates that run on single qubits are not as prone to errors as two-qubit gates, which are therefore the larger concern. (Two-qubit gates are also crucial because they're responsible for creating entanglement between the qubits, which helps give quantum computing its power.)

- Speed

    Last is speed and efficiency. In short, the time spent running a program (including both quantum and classical parts) should be as short as possible.

## Basics of running a quantum computation

1. What are Quantum Computers actually are? - How they generate the Qbit?

2. How to use coding tools (for example: Qiskit) to create and execute quantum circuits?

"What IBM Quantum computers actually are. You'll need to know the basics of the hardware features to optimally design your quantum circuits to run on it.

What Qiskit is, what primitives are, and how we can use them to create and execute quantum circuits.

The typical workflow we follow to run experiments at scale. This includes selecting the best primitives for your use-case, mapping a problem to a quantum circuit, and applying error mitigation and suppression, which enable us to squeeze as much power out of these machines as possible."

## Performance metrics for Processor

Each processor lists three performance metrics, which we discussed in the previous lesson, but as a reminder, they are: qubit count, EPLG, and CLOPS.

- Qubit count

    It's the number of total qubits available to use on a sole quantum processor. For a relatively large, utility-scale problem, you'll need to make sure you are using a processor with enough qubits to be able to tackle the problem.

- EPLG, or “errors per layered gate.”

     This is a measure of the quality of the qubits and quantum gates. It measures the average error each gate introduces in a circuit that entangles neighboring qubits in a chain of 100 qubits. You want this to be as small as possible.

- CLOPS, or “circuit layer operations per second.” 

     This quantifies the speed of the processor. It measures how many layers of a certain benchmarking circuit called a quantum volume circuit a quantum processing unit (QPU) can execute per unit of time. The higher the number, the faster we can compute.


# Quantum Open Source Survey

## Full-stack development platforms, compilers, and simulators.

**A full-stack development platform** is a Software Development Kit (SDK) or framework to design quantum algorithms (including quantum circuits) and run them on real or simulated back-ends.

**A compiler** is a tool that translates high-level quantum programming languages into lower-level instructions that can be executed by quantum hardware.

**A simulator** is a quantum circuit simulator that emulates computations as there were run on a quantum process unit (QPU).

Here is a list
- amazon-braket-sdk-python
- Bloqade
- Catalyst
- Cirq
- CUDA Quantum
- cuQuantum
- DDSIM
- dwave-ocean-sdk
- graphix
- HaeffnerLab / IonSim.jl
- Intel Quantum Simulator
- OpenQL
- PennyLane
- PennyLane Lightning
- Perceval
- ProjectQ
- Pulser
- Pymatching
- pyQuil
- q
- Q#
- Qbraid SDK
- QCompute
- Qibo
- Qiskit
- Qiskit Aer
- qiskit-ibm-transpiler
- Qlasskit
- Qrack
- qsim
- quantastica/quantum-circuit
- QuantumCircuitOpt.jl
- qubiter
- QuEST-Kit/QuEST
- quil-lang/qvm
- Quilc
- Quimb
- QuTiP-qip
- QWIRE
- RustQIP
- Silq
- softwareQinc/qpp (Q++)
- Staq
- Strawberry Fields
- Tangelo
- TensorCircuit
- Tequila
- t|ket>
- weinbe58/QuSpin
- XaCC
- Yao.jl

## Cloud services
**A Cloud Service** allows access to quantum processors or simulators via a remote API. Examples are the IBM Quantum, Rigetti Cloud Services, AWS Braket, etc. 

Here is a list
- Amazon Braket
- DWave
- Google
- IBM Quantum
- Infleqtion
- IonQ
- Microsoft's Azure Quantum
- Pasqal
- qBraid
- Quandela
- Quantinuum
- Quantum Inspire
- Rigetti Cloud Services
- Strangeworks
- Xanadu

## Software for applications and tools
**Software for applications and tools** refers to software for domain specific (such as machine learning or finance) or task specific (such as error correction or a quantum circuit debugger)
- AgnostiqHQ/covalent
- BQSKit/bqskit
- c3
- Dimod
- dwave-cloud-client
- hongyehu/PyClifford
- Infleqtion/Superstaq
- Krotov
- mit-han-lab/torchquantum
- NetKet/NetKet
- openqaoa
- openqasm/openqasm
- PennyLaneAI/qml
- Qadence
- qiskit-finance
- qiskit-machine-learning
- qiskit-nature
- qiskit-optimization
- Qiskit/qiskit
- Qiskit/qiskit-serverless
- Quantomatic/pyzx
- quantumlib/OpenFermion
- quantumlib/Stim
- tensorflow/quantum
- unitaryfund/mitiq
- vprusso/toqito
- Walrus
- zapatacomputing/orqviz