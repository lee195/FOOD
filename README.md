# FOOD
This is a practice project to keep my brain busy while looking for a job.

Fair Object Ordering for Distributed systems(FOOD) based on Blockchain and Correlated Sampling concepts.

Using common randomness to ensure fair ordering mechanisms in order resolution of distributed systems is an idea used in [ALGORAND*](https://www.algorand.com/) and the [Helix](https://www.orbs.com/white-papers/helix-consensus-whitepaper/) protocol.
Here I model a blockchain structure from scratch using the [Correlated Sampling](https://arxiv.org/abs/1612.01041) approach from [Helix](https://www.orbs.com/white-papers/helix-consensus-whitepaper/) as the ordering mechanism and PBFT as the consensus mechanism.

The project is inspired by the use-case of DB's [BRCS](https://www.youtube.com/watch?v=ia4qTpUfTio) which aims to automate the coordination of railway systems via blockchains.   
However not only railway systems can make use of verifiable fairness in distributed settings. Automated vehicles, drones, even distributed databases could potentially take advantage of the inherent openness and manipulation resistance of DLTs paired with the guaranteed fairness in resource contention through common randomness.   
Additionally concepts like [Threshold Cryptography](https://nvlpubs.nist.gov/nistpubs/ir/2019/NIST.IR.8214.pdf) could prove useful in preventing 3rd parties from interfering with the network.

Essentially this is going to be just a simplified version of [Helix](https://www.orbs.com/white-papers/helix-consensus-whitepaper/).

Since I'm building this from scratch there are probably mistakes made here and there that I will get rid of as I develop the project.