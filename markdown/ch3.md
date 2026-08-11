# Transkripsjon av ch3.pdf



<!-- START SIDE 1 -->
# Chapter 3

The structures and the mathematical approach.

This chapter is meant to be a presentation of the structures that I do computations on. And a presentation of the mathematical approach I choose for those computations. Particularly the approach for finding the matrix elements of the Green function. That is, how I find the surface Green matrices and how they are connected to the structure.

## 3.1 The structure from my project work.

For me it feels natural to start with the structure from my project work. Most of all to remind myself quickly of how I did this but also to show some clear similarities between what I have done and what I will do now. In the project work I started to analyze a semiconductor structure that started, from left, with a semi-infinite contact made of InGaSb that grew over into a pure InAs layer which had a boundary against a pure GaSb layer that finally grew over into a semi-infinite GaAlSb contact. During this project work I realized that I had to limit myself to do only parts of the calculations as the theory involved in the calculations was new for me, and I felt that it was smart to take one step at the time.

Figure 3.1 is showing the bandgaps for InAs and GaSb. The conduction bands have energies higher than the highest line in the figure and the valence bands have energies under the lowest line in the figure.

In this structure it is of specific interest to study electrons with energy of magnitude around \(0.5 \text{ eV}\), in relation to the top of the valence band of InAs. That is I have chosen to use the top of the valence band of InAs as zero level for the electron energy. The mentioned energy area is of interest because the bottom of the conduction band of InAs has the energy \(0.43 \text{ eV}\) and the top of the valence band of GaSb has the energy \(0.58 \text{ eV}\). As there is overlap between the conduction band of InAs and the valence bands of GaSb in this energy area it is here we might find recombinations of electrons and holes over the material boundary.

The mathematical approach in my project was to treat the two materials as if they were of infinite length, that is as if the InAs contact was infinite in the left direction and the GaSb contact was infinite in the right direction. This way I avoided all unnecessary problems related to boundary conditions. First I found the lattice constant, the hopping matrices and

41
<!-- SLUTT SIDE 1 -->


<!-- START SIDE 2 -->
An energy band diagram shows incoming electrons. On the left side, there is a region labeled "InAs" and on the right, "GaSb". The diagram illustrates energy differences: 0.68 eV between the conduction band edges of InAs and GaSb, 0.15 eV for the band gap of GaSb, and 0.43 eV between the valence band edges of InAs and GaSb.

Figure 3.1: The energy gaps of the structure from my project.

the energy vectors for each material involved from the VCA-parameters. Further I computed the surface Green matrix for each contact, from the hopping matrices and energy vectors. Next task was to compute the surface Green matrices connected to atomic layers in lattice points with energy relations different from the energy relations in the pure materials, because of having different atomic layers as closest neighbours. These surface Green matrices might be called gamma matrices later in this text. To find the matrix elements of the transport Green matrix I only multiplied the hopping matrices and the Green matrices together in a proper manner.

In the figure below I illustrate the system in one dimension; the growth direction. This seemed to be a great way of finding an easy mathematical approach of the problem:

A one-dimensional atomic lattice diagram is shown, representing a heterostructure. On the left, alternating Indium (In, represented by an open circle) and Arsenic (As, represented by a filled circle) atoms form the InAs region. On the right, separated by a vertical dashed line, alternating Gallium (Ga, represented by an open circle) and Antimony (Sb, represented by a filled circle) atoms form the GaSb region. Arrows above the atoms are labeled with VcaL and UacL for the InAs side, VcaR and UacR for the GaSb side, and VcaB at the interface. Below the atoms, lattice points are numbered sequentially from 0, 1, 2, 3... and specific atomic positions are labeled gpc0, gpa0, gpc1, gpa1, gpc2, gpa2, gpc3, gpa3, etc.

Figure 3.2: A one dimensional illustration of the system.

42
<!-- SLUTT SIDE 2 -->


<!-- START SIDE 3 -->
In the figure the unfilled circles mark cation layers in the structure and the filled circles mark anion layers. The figure is simplified in comparison to the real structure as the atoms in the figure are atomic layers in the real structure.

The hopping matrices UacR, VcaR, UacL and VcaL are constructed from VCA-parameters which again are found from quantities measured by Vogl. These quantities are presented in the chapter named The Vogl files. The hopping matrices are a measure for the probability for an electron to jump from one orbital on one atom to an orbital on the closest neighbour atom. As one might see the U's give the hopping between neighbours on the same lattice point and the V's give the hopping between neighbour atoms at different lattice points.

The features named gpc0, gpa0, gpc1, gpa1,... are so called gamma plus matrices, they are found iteratively from the gamma plus matrix for the atomic neighbour layer on the right hand side in the structure. To find these matrices are the central task in the calculation of the transmission Green matrix. If one chooses to look at the structure the opposite direction one must use the gamma minus matrices. But, as I want to look at the electron transport from left to right in the structure I have to compute all the gamma plus matrices going iteratively from one atom layer to the next from right to left, starting with the gammaplus matrix for the pure material GaSb (in this specific case), that is the right contact material. Of course the gamma matrices depend on whether there are a cation or anion layer on the surface. And, therefore we get four possible solutions, one for starting on a cation layer and ending on an anion layer, one for starting on a cation layer and ending on a cation layer, one for starting on an anion layer and ending on an anion layer and finally one for starting on an anion layer and ending on a cation layer. All those four solutions are $5 \times 5$ matrices multiplied together, that is mainly the $5 \times 5$ matrices shown in last figure. These four $5 \times 5$ solutions are then put together to form the $10 \times 10$ transmission matrix.

Well, over to the actual system from my project work. In figure 3.2 the features gpa3 and gpc3 are the gamma plus matrices for the right material, i.e. for anode and cathode. The next lattice point seen from right is disturbed by the fact that the cation layer on this lattice point has two different neighbours and we must be careful with the energies and the hopping matrices when we try to find the gamma plus matrices for this lattice point. This is also true for the next two lattice points; nr. 2 and 1 in the structure. To find these gamma plus matrices we use the formula given in section 1.4.6 about surface Green functions:

$$
\begin{aligned}
\Gamma_{a,2}^{+} &= \frac{1}{E-E_{a,2}-V_{caR}(\Gamma_{c,3}^{+})V_{acR}} \\
\Gamma_{c,2}^{+} &= \frac{1}{E-E_{c,2}-U_{caR}(\Gamma_{a,2}^{+})U_{acR}}
\end{aligned}
\quad (3.1)
$$

If we continue to use the same iteration formula we see that we find the gamma matrices for lattice point one:

$$
\begin{aligned}
\Gamma_{a,1}^{+} &= \frac{1}{E-E_{a,1}-V_{caB}(\Gamma_{c,2}^{+})V_{acB}} \\
\Gamma_{c,1}^{+} &= \frac{1}{E-E_{c,1}-U_{caL}(\Gamma_{a,1}^{+})U_{acL}}
\end{aligned}
\quad (3.2)
$$

In the calculation of $\Gamma_{c,1}^{+}$ we use a new kind of hopping matrix; with subscript B for 'between' or 'boundary' or something else that makes sense. This is a hopping matrix for the pure material GaAs. If I instead of choosing to use the boundary where I go from an anion to a cation layer going from left to right, choose to use the boundary alternative where I go from a cation to an anion layer when going the same direction, I would have got a completely different hopping matrix on the boundary. I then would have to use an U matrix for InSb

43
<!-- SLUTT SIDE 3 -->


<!-- START SIDE 4 -->
to calculate the first gamma matrix in the left contact. This should not change the result for the transport Green matrix in any significant way so I do not repeat the approach for the calculations for this alternative. I just conclude that the alternative exists. By using the formula one time more we find the gamma matrix for the first anion layer in the left material that is not unique by means of its energy relations. That is, the anion layer related to lattice point 1 has two different neighbour atomic layers, indium on its left hand side and gallium on its right hand side. So because of all this we need to calculate the gamma matrix for the anionlayer on lattice point 0. That is done by using our iteration formula on the gamma matrix for the cation layer on lattice point 0:

\[ \Gamma_{\text{a},0}^+ = \frac{1}{E - E_{\text{a},0} - V_{\text{acL}} (\Gamma_{\text{c},1}^+) V_{\text{caL}}} \tag{3.3} \]

With this I have finished all the calculation of the gamma matrices or surface matrices that are needed to do all the calculations I did in my project work last year. It now only remains to calculate the local elements of the Green function for InAs. They are found directly from the gamma matrices gpa0 and gpcl1, ie. last figure, and the surface Green matrix for the left contact material, and of course one must involve some hopping matrices and energies. But anyway here is the formula for the two sets of local elements of the Green function, ie. for the anion and cation layers respectively:

\[ G_{\text{a}0\text{a}} = \frac{1}{EL-E_{\text{a},1} - U_{\text{acL}} (\Gamma_{\text{c,L}}^+) U_{\text{caL}} - V_{\text{acL}} (\Gamma_{\text{c},1}^+) V_{\text{caL}}} \tag{3.4} \]

\[ G_{\text{c}0\text{c}} = \frac{1}{EL-E_{\text{c},1} - V_{\text{caL}} (\Gamma_{\text{a,L}}^+) V_{\text{acL}} - U_{\text{caL}} (\Gamma_{\text{a},0}^+) U_{\text{acL}}} \tag{3.5} \]

With this most calculations of the central features involved in the calculation of the transport Green matrix should be explained and I don't think there is any need for further recapitulation from the projectwork. At least not on this stage of the diploma work. The next step in this chapter, that connects theory to calculations, must be to explain, in detail, how I have found the transport Green matrix for the two different kinds of structures I have done calculations on in my diploma work. This is in fact much more complicated than what I did in my projectwork. I will follow the same order as I in fact did under the calculations and start with the structure from the earlier mentioned article, article \[2].

### 3.2 The structures I do calculations on in my diploma work.

The structures from article \[2] which I have done calculations on are some simplified in relation to the structures that are used in the experiments. For example I do not consider doping at all. On the other hand, I have done calculations on dozens of structures that the experimentalists (at least they who wrote article \[2]) have not tested. That might be because they found them uninteresting, or it might be of economical reasons. So the structure that I present in fig.0.1 is a rough illustration, and it does not show all the different thicknesses of the two central layers that this structure will be, or has been realized for. In article \[2] it is studied how the current changes as the thickness of the central InAs if the InAs layer is removed, that is it is studied how the central GaSb layer affects the transmission of electrons. In my work I have done calculations on this structure varying the thickness of the InAs layer from 0 to 999 atomlayers. Of course not all of this presented in this diploma work, but it didn't cost any extrawork to get it done, so why not.

44
<!-- SLUTT SIDE 4 -->


<!-- START SIDE 5 -->
Figure 3.3: The energygaps of the structure from article [2].

As we might see, there are several factors that make this structure in fig.0.1 comparable with the one I considered in my projectwork. The contacts are for example identical. I consider electrons tunneling from conduction bands in the left contact material, InAs, to valence bands in the right contact material, GaSb. As in the projectwork I avoid problems with boundary conditions through considering the contacts as if they were infinite in one direction. In the center of the structure we find a diode like composition of GaSb and InAs, which gives me a boundary that is identical to that I treated in my project work, only the electron transport that is of interest crosses this boundary the opposite direction this time. The only real difference from the structure I considered in my project is the two AlSb blocking layers that make a quantum well in the center of the structure.

The energies that are used in the figure are those that are given in article [2]. For me this introduced a small problem in the approach of computation, as I needed to know the energy level of all atomic layers, also them with different neighbours. Such layers exist only on the boundaries between different materials. I used the top of the valence band for InAs as reference level for the energy and I produced offsets to find the energy of the electron everywhere in the structure. The problem occurred on the boundaries. For example was it a problem to decide whether the In atomic layer between InAs and AlSb belonged to the InAs contact or to the one monolayer of the material InSb. What I did was to use a combination of the two such that the energy of this problem layer became reasonable. But in the process of doing so I had to use bandgaps produced from the VCA-parameters from article [1]. These bandgaps were unfortunately different from those presented in article [2], and I had to adjust some of the bandgaps and offsets, so that the important energy areas came out correct in the right materials, in short, so that the overlap between conduction bands in the left contact and valence bands in the right contact came out with the correct magnitude. To do these adjustments I was closely guided by Jon Andreas Stovneng which was my advisor during the projectwork, and I am sure that this should be all right. The offset values that I have used are:

45
<!-- SLUTT SIDE 5 -->


<!-- START SIDE 6 -->
\[
\begin{aligned}
Eoff_{L1} &= 0.60\text{eV} \\
Eoff_{L2} &= -0.18\text{eV} \\
Eoff_{L3} &= -0.19\text{eV} \\
Eoff_{LR} &= -0.58\text{eV}
\end{aligned}
\tag{3.6}
\]

Here the indices are related to the material numbers in figure 3.4.
To proceed I will do as I did in the previous section for the structure from my project work. That is to make a one-dimensional model for the structure, and explain the mathematical approach for computing the transport Green matrix.
As I ran out of space I had to write the figure of the one-dimensional model, fig.3.4 over two pages, but I can't imagine that this can be any trouble for the reader.

46
<!-- SLUTT SIDE 6 -->


<!-- START SIDE 7 -->
### Diagram Elements

**Axes and General Labels:**
*   Material nr. L
*   Continuing to infinity.
*   Horizontal Axis Markers: 1, ...2..., R, ...R..., 3

**Material Designations:**
*   InAS
*   AlSb
*   GaSb

**Leftmost Vertical Stack of Elements:**
*   Vcal
*   UacL
    *   gpa0
    *   gpc0
*   0
*   UacL
    *   gpa1
    *   gpc1
*   UacL
    *   gpa2
    *   gpc2
*   UacL
    *   gpa3
    *   gpc3

**Central Vertical Stack of A-Sites and Associated Elements:**
*   A
    *   gpcA
*   UacL
        *   gpaA
    *   gpcA
*   A+1
    *   gpcA+1
*   UacL
    *   gpaA+1
    *   gpcA+1
*   A+2
    *   gpcA+2
*   UacL
    *   gpaA+2
    *   gpcA+2
*   A+3
    *   gpcA+3
*   UacL
    *   gpaA+3
    *   gpcA+3

**Central Vertical Stack of B-Sites:**
*   B
    *   gpcB
*   B+1
    *   gpcB+1

**Rightmost Vertical Stack of Elements:**
*   Vcal
*   VcaB1
*   UacR
    *   gpa1
    *   gpc1
*   Vcal
*   VcaB2
*   UacR
    *   gpaB
    *   gpcB
*   Vcal
*   VcaB3
*   UacR
    *   gpaB+1
    *   gpcB+1

---

Figure 3.2: A one dimensional model of the structure from article

47
<!-- SLUTT SIDE 7 -->


<!-- START SIDE 8 -->
So, with this busy figure, Fig. 3.4, I feel that I owe the reader an explanation in detail how to interpret the layers shown here. From top to bottom: The left contact material going from 1, and VcaL are representing the same material working from top to bottom. The left contact material, *i.e.* VcaB1, is involved, *and therefore,* is the contact for the first layer in the barriers. *In summary*, we call this first layer the *bottom contact*. This layer is then followed by a series of layers with a certain amount of repetition. This repetition is represented by B and S. B is the barrier layer and S is the well layer. In this case, B is GaSb and S is InAs. The barriers are composed of N layers, *and therefore,* N is the total number of periods for the barriers. The total amount of layer is L. This structure is symmetric, *and therefore,* the number of layers N-1 from the bottom contact, *i.e.* VcaB1, is equal to the number of layers R from the top contact.

---

**Diagram Labels (Figure 3.4):**

**Vertical Axis:**
...L...
1
...2...
R
*Axis Label:* Material nr.

**Left Side Elements:**
*   VcaB3
*   VcaL
*   VcaL
*   VcaB4
*   VcaL

**Right Side Elements:**
*   VcaR
*   VcaR
*   VcaR
*   VcaB5
*   VcaB3

**Material Regions (Diagonal Labels and Associated Points):**
*   **InAs**
    *   C (unfilled circle) with gpcC
    *   C+1 (unfilled circle) with gpcC+1
    *   C+2 (unfilled circle) with gpcC+2
    *   C+3 (unfilled circle) with gpcC+3
*   **AlSb**
    *   B+2 (unfilled circle) with gpcB+2
    *   B+3 (unfilled circle) with gpcB+3
*   **GaSb**
    *   N-2 (unfilled circle) with gpcN-2
    *   N-1 (unfilled circle) with gpcN-1
    *   N (unfilled circle) with gpcN
*   Arrow from GaSb region: Continuing to infinity.

**Interface/Matrix Labels:**
*   **UacL** (with an upward arrow)
    *   gpaB+2
    *   gpaC
    *   gpaC+1
        *   gpaC+2
    *   gpaC+3
*   **UacR** (with a downward arrow)
    *   gpaN-2
    *   gpaN-1
    *   gpaN

**Descriptive Labels at Bottom of Diagram:**
*   **Leftmost Column:** V-matrices.
*   **Second Column (from left):** U-matrices. Gammamamatrices for cathodematerials.
*   **Third Column (from left):** Latticep. nr. Gammamamatrices for cathodematerials.
*   **Center Column:** Materials.
*   **Third Column (from right):** Latticep. nr. Gammamamatrices for cathodematerials.
*   **Second Column (from right):** U-matrices. Gammamamatrices for anodematerials.
*   **Rightmost Column:** V-matrices. Gammamamatrices for anodematerials.

---

Figure 3.4: A one dimensional model of the structure from article [2].

48
<!-- SLUTT SIDE 8 -->


<!-- START SIDE 9 -->
So, with this chaotic figure, fig. 3.4 I feel that I owe the reader to explain in detail how to read it. The first half is showing, from top to bottom: The left contact material coming from minus infinity and ending at lattice point 1. The features named \(U_{acL}\) and \(V_{caL}\) are hopping matrices that are typical for the left contact, that is the material InAs. Going from lattice point 1 to 2 the hopping matrix \(V_{caB1}\) is involved, \(B1\) because this is a feature that occurs on the first boundary. This hopping matrix is typical for the material InSb. As one follows the dotted line through the first layer in the barrier one goes from lattice point 2 to lattice point \(A+1\). We can conclude that the number of monolayers in this material layer is \(A = A1\). The hopping matrices that are included are \(U_{ac1}\) and \(V_{ca1}\) that is characteristic for the material AlSb. As we crosses the boundary between lattice point \(A+1\) and \(A+2\) we meet the hopping matrix \(V_{caB2}\) (\(B2\) for second boundary). This is characteristic for the material GaSb and it is clear that this hopping matrix is identical to the hopping matrix type \(V\) in the second layer, and those are again identical to them in the right contact material as we will see later. The same is valid for the hopping matrix type \(U\). This layer lasts from lattice point \(A+2\) to lattice point \(B+1\), it is therefore clear that the number of monolayers in this layer of a specific kind of material is \(B - A - 1 = A2\). As we follow the dotted line over the boundary we find the third boundary hopping matrix. This one is characteristic for the material InSb and is then identical to \(V_{caB1}\). Here our first little view on the first half of the one dimensional model of the system ends. Later we will follow the dotted line backwards to explain all the features \(gp\) in detail.

But before that we got to finish explaining the model by means of hopping matrices, lattice points and materials. The hopping matrix \(V_{caB3}\) took us to the third barrier layer which consist of InAs. This is identical to the material in the left contact. This layer has lattice points from \(B+2\) to \(C+1\), so the number of monolayers in this layer is \(C - B - 1 = A3\). Crossing the boundary we find the hopping matrix \(V_{caB4}\) that is characteristic of AlAs. Following the dotted line through this layer we find hopping matrices that are characteristic of AlSb. The layer reaches from lattice point \(C+2\) to lattice point \(N-1\). This gives that the number of monolayers in this last barrierlayer is \(N - C - 3 = A4\). Crossing the boundary and entering the right contact we use a hopping matrix that we have used before. \(V_{caB5}\) is characteristic for GaSb and is identical to all the hopping matrix of kind \(V\) in the second layer, in the right contact and on the second boundary. Of course all the hopping matrix of type \(U\) in the right contact is also characteristic of GaSb. As one might have admitted during this quick first overview of the structure the barrier starts from lattice point one and ends at lattice point \(N\), the layers between the contacts consist \(A1\), \(A2\), \(A3\) and \(A4\) lattice points and the relation between N's and A's is, \(N = A1 + A2 + A3 + A4 + 2\), the plus two at the end comes from the lattice points in the contacts that is included.

Well, this was a lot of talk about the different kinds of hopping matrices in the structure. The content of all these hopping matrices are explained in section 2.2 chapter 2.

As the figure now should be understood well I will try to connect the surface Green matrices, or the gamma matrices, that is connected to the energy of each atomic layer in the structure, to the theory.

I start with the gamma matrices that are connected to lattice point \(N\). In the figure they are given the names \(g_{paN}\) and \(g_{pcN}\). To find these matrices we need to know the gamma matrices for the lattice point \(N+1\) and uses these equations from the chapter 1 section 1.9:
<!-- SLUTT SIDE 9 -->


<!-- START SIDE 10 -->
This is not only the most general form of the equation for my choice of structure but also the specific equation for the gamma matrices connected to lattice point $N+1$ in figure 3.4 as the gamma matrices for lattice point $N+1$ are identical to the surface Green function of the right contact. Just to write the equations with correct indices:

\[
\begin{aligned}
\Gamma_{\text{a,N}}^{+} &= \frac{1}{E-E_{\text{a,N}}-V_{\text{ac}}(\Gamma_{\text{cN}}+1^{+})V_{\text{ca}}} \\
\Gamma_{\text{c,N}}^{+} &= \frac{1}{E-E_{\text{c,N}}-U_{\text{ca}}(\Gamma_{\text{a,N}}^{+})U_{\text{ac}}}
\end{aligned} \tag{3.7}
\]

As the cathion at lattice point $N$ has the same neighbouring materials at both sides, Sb, I assume that the energy relations are the same for this cation layer as for all the other cationlayers in GaSb.

From these equations all the other gamma matrices follows by using the same formula with correct input for energies, energy vectors and hopping matrices. For lattice point $N-1$ is we get for the anion layer:

\[
\begin{aligned}
\Gamma_{\text{a,R}}^{+} &= \frac{1}{E-E_{\text{a,R}}-V_{\text{acR}}(\Gamma_{\text{cR}}^{+})V_{\text{caR}}} \\
\Gamma_{\text{c,R}}^{+} &= \frac{1}{E-E_{\text{cat,R}}-U_{\text{caR}}(\Gamma_{\text{a,N}}^{+})U_{\text{acR}}}
\end{aligned} \tag{3.8}
\]

\[
\Gamma_{\text{a,N-1}}^{+} = \frac{1}{E-E_{\text{an,N-1}}-V_{\text{acR}}(\Gamma_{\text{cN}}^{+})V_{\text{caR}}} \tag{3.9}
\]

As we see, this anion layer is connected to the previous cation layer with hopping matrices that is typical for GaSb. This because of my choice of using anion-cation as the sequence of ions when crossings the boundary from left right. See figure 3.4. The energy $E_{\text{a,N-1}}$ is a approximation of the energy of the electron when it is located at this lattice point. Referred to the energy, in the left contact, of incoming electrons this energy is:

\[
E_{\text{a,N-1}} = E_L + (Eoff_{L2} + Eoff_{LR})/2 \tag{3.10}
\]

Where the $Eoff$'s are energy offsets between the gamma points, to the top of the valence bands, of the left contact material and all the others. The indices of material kinds are identical to the material numbers given in figure 3.4. For example $Eoff_{L2}$ are the energy offset between the left contact material and the material given the number 2 in the figure. The materials given numbers 1 and 3 are special as they occur only at boundaries.
Further we find all the gamma matrices in the first barrier layer seen from right through repeated use of the iteration formula with the characteristic features for AlSb.

\[
\begin{aligned}
\Gamma_{\text{c,n}}^{+} &= \frac{1}{E_{2}-E_{\text{c,2}}-U_{\text{ca2}}(\Gamma_{\text{a,n+1}}^{+})U_{\text{ac2}}} \\
\Gamma_{\text{a,n-1}}^{+} &= \frac{1}{E_{2}-E_{\text{a,2}}-V_{\text{ac2}}(\Gamma_{\text{c,n}}^{+})V_{\text{ca2}}}
\end{aligned} \tag{3.11}
\]

Here $n$ is running from $N-1$ to $N-A4+1$ so that the last atomic layer that we find the gamma matrix for is the first anion layer seen from left in the first barrier layer seen from right. The energy $E_2 = E_L + Eoff_{L2}$. The energy vectors is calculated from the VCA-parameters that is found from the measured data in the Vogl files. This calculation is presented in more detail in the chapter about the Vogl files.
Now we have arrived at the second boundary seen from right. Here we have two atomic layers that have different closest neighbours. These layers must be treated with care because of the disturbance in the energetic relations connected to having different neighbours.
<!-- SLUTT SIDE 10 -->


<!-- START SIDE 11 -->
\[
\Gamma_{\text{c},N - A4}^+ = \frac{1}{E_{\text{c},N - A4} - E_{\text{cat},N - A4} - U_{\text{ca}2}(\Gamma_{\text{a},N - A4} + 1)^+U_{\text{ac}2}} \quad \text{(3.12)}
\]

The energy \(E_{\text{c},N - A4}\) are related to the energy in the left contact in the following manner:

\[
E_{\text{c},N - A4} = E_{\text{L}} + (Eoff_{\text{L}1} + Eoff_{\text{L}2})/2 \quad \text{(3.13)}
\]

As one might remember the energy offsets are the energy differences between the gamma matrices energy vectors of the two actual material. That is the energy differences between \(E_{\text{cat},N - A4}\) are just a middle of the two materials that one might see this specific cation as a part of, the first layer seen from right or the one monolayer of AlAs at the boundary, the materials 1 and 2 from the figure. We continue with the one anion layer at this boundary that is also unique in the structure.

\[
\Gamma_{\text{a},N - A4 - 1}^+ = \frac{1}{E_{\text{a},N - A4 - 1} - E_{\text{an}_{\text{a},N - A4 - 1}} - V_{\text{ac}1}(\Gamma_{\text{c},N - A4}^+ )V_{\text{ca}1}} \quad \text{(3.14)}
\]

Here the energy is given from the equation:

\[
E_{\text{a},N - A4 - 1} = E_{\text{L}} + (Eoff_{\text{L}1})/2 \quad \text{(3.15)}
\]

And the energy vector is still a middle value between the two possible choices of materials for this specific anion layer.

Preceding left we now enter the second layer in the barrier seen from right. For each atomic layer in this material layer we calculate new gamma matrices in the same way as in the previous material layer:

Now, the hopping matrices and the energies are characteristic of InAs. And the index \(n\) is running from \(N - A4 - 1\) to \(N - A4 - A3 + 1\), such that the last atomic layer that is involved is the anion layer at latticepoint \(N - A4 - A3\) (\(N - A4 - A3 = A1 + A2 + 2\)). At the next boundary we compute the gamma matrices as follows:

\[
\Gamma_{\text{c},N - A4 - A3}^+ = \frac{1}{E_{\text{c},N - A4 - A3} - E_{\text{cat}_{\text{c},N - A4 - A3}} - U_{\text{ca}3}(\Gamma_{\text{a},N - A4 - A3 + 1}^+)U_{\text{ac}3}} \quad \text{(3.17)}
\]

\[
\Gamma_{\text{a},N - A4 - A3 - 1}^+ = \frac{1}{E_{\text{a},N - A4 - A3 - 1} - E_{\text{an}_{\text{a},N - A4 - A3 - 1}} - V_{\text{ac}3}(\Gamma_{\text{c},N - A4 - A3}^+)V_{\text{ca}3}} \quad \text{(3.17)}
\]

Here are the energies \(E_{\text{c},N - A4 - A3}\) and \(E_{\text{a},N - A4 - A3 - 1}\) related to the energy in the left contact in the following manner:

\[
E_{\text{c},N - A4 - A3} = Eoff_{\text{L}} + (Eoff_{\text{L}3})/2 \quad \text{(3.18)}
\]

\[
E_{\text{a},N - A4 - A3 - 1} = Eoff_{\text{L}} + (Eoff_{\text{LR}} + Eoff_{\text{L}3})/2 \quad \text{(3.18)}
\]

And the energy vectors are still middle values. Well, already now it is clear why I had to use other signs for the lattice point numbers in Figure 3.4.

To fulfill the computing of the gamma matrices I continue quickly through the second barrier layer seen from left.

51
<!-- SLUTT SIDE 11 -->
