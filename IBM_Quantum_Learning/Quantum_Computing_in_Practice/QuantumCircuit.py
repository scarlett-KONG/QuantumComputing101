{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'qiskit'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[1], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mnumpy\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mnp\u001b[39;00m \n\u001b[0;32m----> 2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mqiskit\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m QuantumCircuit\n\u001b[1;32m      4\u001b[0m qc_example \u001b[38;5;241m=\u001b[39m  QuantumCircuit(\u001b[38;5;241m3\u001b[39m)\n\u001b[1;32m      5\u001b[0m qc_example\u001b[38;5;241m.\u001b[39mh(\u001b[38;5;241m0\u001b[39m)\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'qiskit'"
     ]
    }
   ],
   "source": [
    "import numpy as np \n",
    "from qiskit import QuantumCircuit\n",
    "\n",
    "qc_example =  QuantumCircuit(3)\n",
    "qc_example.h(0)\n",
    "qc_example.p(np.pi/2,0)\n",
    "qc_example.cx(0,1)\n",
    "qc_example.cx(1,2)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "quantum",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
