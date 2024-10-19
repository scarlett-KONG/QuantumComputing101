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

