I am writing my PhD thesis based on 5 papers -paper 1 to 5, starting with the code 001). I need to brainstorm a potential structure for the thesis. I am a PhD student in machine learning applied for physics, and in particular astroparticle physics and dark matter research. 

The common theme of these articles is the search for dark matter using statistical/machine learning techniques, using gamma ray data from the fermi-LAT telescope.

The thesis is done by compendium, meaning that I will write a general physical introduction to the problem of dark matter, and then a more detailed physical introduction to the problems dealt with in details in the papers. 
I am thinking of structuring the thesis as follows.

First a general introduction to the problem of dark matter: talk about the open cosmological problems, how dark matter may solve them, and which are the main evidences for the presence of dark matter.
Then we will introduce WIMPS as a potential dark matter candidate, what is the wimp miracle, how it can solve the problems of dark matter, and explain how it could annihilate or decay.
We will then argue that dark matter / wimps can produce gamma rays, and explore in depth why it could be a good idea to search for dark matter using gamma rays, namely the fact that the gamma-ray background is potentially lower when compared to the astrophysical background in other bands. 

At some point we will have to introduce the halo model in lambda cdm, we need to explain how dark matter clusters (the overdensities that form halos), introduce the density function (NFW for example, vs Burkert and Einasto) hinting to the open question of the different dark matter profiles (cored vs cusped for example). We will then argue that the galactic center is a promising target to look for a DM signal given the higher density of dark matter, and thus introduce my GCE paper. We will have to talk about the galactic center excess, possible interpretations as MSPs vs a diffuse dark matter signal. We need to think more of that.

Then we will introduce dark matter subhalos, what they are, how they form, and explain the idea that the more massive ones may host stellar formation, and be seen in the form of dwarf spheroidal galaxies. On the other hand, a much more abundant population of lighter subhalos with masses from 1e6 1e8 Msun may exist, which would not be able to host stellar formation (explain why) which could still emit gamma rays while annihilating. We will then introduce the problem of associated/unassociated gamma ray sources, and the paper on DM subhalo classification with machine learning. 

We will then move on to studying the unresolved gamma ray background. 

First we will introduce the problem of being able to detect or not gamma ray sources, given the fermi sensitivity. We will then introduce the fermi source catalog, and argue how an important property to study is the source count distribution function (dN/dS), which is directly connected to the gamma ray luminosity function when integrated along the line of sight (try to explain this connection). We should also highlight how this quantity can in principle be used for DM searches, as if we knew with precision the dNdS of individual source populations, knowing the overall one would help in trying to identify discrepancies, or as an upper bound for other astrophysical studies (there can't be more sources than the total).
We will then argue that it is possible to determine the dN/dS using machine learning techniques, introduce Simulation Based Inference, neural posterior estimation, and thus the paper on the dN/dS using ML and spherical convolutions. 
We will then talk about a practical application of this dN/dS and introduce the paper where we derive the probabilistic catalog using a dNdS. To do so, we need to talk about the fermi detection pipeline from FermiPy and the fermitools. We will highlight how the TS cut is arbitrary, also given how the galactic foreground is renormalized patch by patch, and how the TS they define is not a globally consistent variable. We will then introduce the new methodology of the paper, which introduces a new TS scale for detection based on the quality factor, which would be useful for studies where statistics is more important than potentially spurious detection (See the paper for more information).

Finally, we will argue that it is possible to extract more information from the unresolved gamma ray background by employing the cross correlation technique.
We need to introduce the cross correlation technique and formalism based on the halo model (not as in depth as the thesis from Pinetti, but drawing from it), specifically drawing from papers 1212.5018 and 1312.4835



These are my initial thoughts on how to structure the thesis. Lets review them, and potentially improve the structure for the thesis. 