# Transkripsjon av ch2.pdf

<!-- START SIDE 1 -->
Chapter 2

Energy vectors, hopping matrices, surface Green matrices and the local elements of the Green function.

In this chapter I will present the VCA parameters, measured by Vogl, Hjalmarson and Dow, presented in article [1]. That is, only for the materials I use in this diploma work. I will show how to use these parameters to make characteristic features for the materials such as energy vectors and hopping matrices. Further I will try to show how one uses the features mentioned above to find surface Green matrices for the materials. I hope this kind of matrices is known from the theory chapter, chapter 1. So, the actual content of this chapter will be an attempt to link the theory to the VCA parameters from article [1]. That is, the content of this chapter gives the formula for the features that is needed to compute transport Green matrices, and relates those formulas to the empirical data given in article [1].

## 2.1 The content of the Vogl files

The Hamiltonian for the 1-D single band system is written as in equation 1.12,

$$
H = \sum_j |j \rangle \epsilon_0 \langle j| + |j \rangle u \langle j \pm 1| \quad (2.1)
$$

In the 

$$
sp^3s^{\ast}
$$

 model we have 13 independent matrix elements to build up the energy vectors and the hopping matrices, equation 1.64:

30
<!-- SLUTT SIDE 1 -->

<!-- START SIDE 2 -->

$$
\begin{array}{ll}
E(s, b) & = \langle s, b, \vec{R} | H | s, b, \vec{R} \rangle \\
E(p, b) & = \langle p, b, \vec{R} | H | p, b, \vec{R} \rangle \\
E(s^{\ast}, b) & = \langle s^{\ast}, b, \vec{R} | H | s^{\ast}, b, \vec{R} \rangle \\
V(s, s) & = 4 \langle s, a, \vec{R} | H | s, c, \vec{R} \rangle \\
V(x, x) & = 4 \langle px, a, \vec{R} | H | px, c, \vec{R} \rangle \\
V(x, y) & = 4 \langle px, a, \vec{R} | H | py, c, \vec{R} \rangle \\
V(sa, pc) & = 4 \langle s, a, \vec{R} | H | px, c, \vec{R} \rangle \\
V(pa, sc) & = 4 \langle p, a, \vec{R} | H | s, c, \vec{R} \rangle \\
V(s^{\ast}a, pc) & = 4 \langle s^{\ast}, a, \vec{R} | H | px, c, \vec{R} \rangle \\
V(pa, s^{\ast}c) & = 4 \langle px, a, \vec{R} | H | s^{\ast}, c, \vec{R} \rangle
\end{array} \quad (2.2)
$$

The 3 first lines represent 6 independent elements when we insert values for $b$; anion or cation. In this approximation $s^{\ast}s$ and $s^{\ast}s^{\ast}$ elements are set to zero.
As only nearest neighbors are interacting, the $sp^3s^{\ast}$ model then has a Hamilton operator as follows:

$$
H = \sum_{n,b,i} |n, b, \vec{R}_i \rangle E(n,b) \langle n, b, \vec{R}_i | + \sum_{n,b,j=i+\frac{a}{4}(1,1,1)} |n, b, \vec{R}_i \rangle V \langle n, b, \vec{R}_j | \quad (2.3)
$$

As mentioned earlier I use VCA parameters for pure materials measured by Vogl as a basis for my calculations. Except from in the calculations of some offsets, where I have considered not only bandgaps that I find from these VCA parameters but also the bandgaps given in the article written by Y.H.Wang, M.H.Lium, M.P.Houng, J.F.Chen and A.Y.Cho, article [2].
For the materials involved in this diplomawork we have the VCA parameters that is given in tables 2.1, 2.2 and 2.3.
In article [1] $V(s^{\ast}, s^{\ast})$ is included even though it's value is measured to be zero. I have also included the bondlengths to the set of features that is presented in equations 1.64, see at the end of the list. These bondlengths are also found from article [1].
Tables 2.1 and the table on top in table 2.2 gives the needed VCA parameters for the layers of the structure that I work with. But, due to my calculation method I also need the VCA parameters in tables on bottom of 2.2 and table 2.3. The content of these tables is the empirical data for the materials one can say that there is one monolayer of at every boundary between different material layers. For the realisations of the structure in my diplomawork we find $AlAs$ and $InSb$ as new materials at the boundaries.
<!-- SLUTT SIDE 2 -->

<!-- START SIDE 3 -->
-2.7219 $E(s,c)$
3.7201 $E(p,c)$
6.7401 $E(s^{\ast},c)$
-9.5381 $E(s,a)$
0.9099 $E(p,a)$
7.4099 $E(s^{\ast},a)$
-5.6052 $V(s,s)$
1.8398 $V(x,x)$
1.4693 $V(x,y)$
3.0354 $V(sa,pc)$
5.4389 $V(pa,sc)$
3.3744 $V(s^{\ast}a,pc)$
3.9097 $V(pa,s^{\ast}c)$
0.0000 $V(s^{\ast},s^{\ast})$
2.62 d=bondlength in Angstrom

-3.8993 $E(s,c)$
2.9146 $E(p,c)$
5.9846 $E(s^{\ast},c)$
-7.3207 $E(s,a)$
0.8554 $E(p,a)$
6.6354 $E(s^{\ast},a)$
-6.1567 $V(s,s)$
1.5789 $V(x,x)$
1.1285 $V(x,y)$
4.9601 $V(sa,pc)$
4.6675 $V(pa,sc)$
4.9895 $V(s^{\ast}a,pc)$
4.2180 $V(pa,s^{\ast}c)$
0.0000 $V(s^{\ast},s^{\ast})$
2.64 d=bondlength in Angstrom

Table 2.1: OVER: Empirical matrix elements of the $sp3s^\*$ Hamiltonian in eV for InAs.
UNDER: Empirical matrix elements of the $sp3s^\*$ Hamiltonian in eV for GaSb.

32
<!-- SLUTT SIDE 3 -->

<!-- START SIDE 4 -->
-2.0716 $E(s,c)$
3.0163 $E(p,c)$
6.1543 $E(s^{\ast},c)$
-6.1714 $E(s,a)$
0.9807 $E(p,a)$
6.7607 $V(s^{\ast},a)$
-5.6448 $V(s,s)$
1.7199 $V(x,x)$
3.6648 $V(x,y)$
4.9121 $V(sa,pc)$
4.2137 $V(pa,sc)$
4.3662 $V(s^{\ast}a,pc)$
3.0739 $V(pa,s^{\ast}c)$
0.0000 $V(s^{\ast},s^{\ast})$
2.66 d=bondlength in Angstrom

-3.4643 $E(s,c)$
2.9162 $E(p,c)$
5.9362 $E(s^{\ast},c)$
-8.0157 $E(s,a)$
0.6738 $E(p,a)$
6.4530 $E(s^{\ast},a)$
-5.5193 $V(s,s)$
1.4018 $V(x,x)$
3.8761 $V(x,y)$
3.7880 $V(sa,pc)$
4.5900 $V(pa,sc)$
3.5666 $V(s^{\ast}a,pc)$
3.4048 $V(pa,s^{\ast}c)$
0.0000 $V(s^{\ast},s^{\ast})$
2.81 d=bondlength in Angstrom

Table 2.2: OVER: Empirical matrix elements of the 

$$
sp^3s^{\ast}
$$

 Hamiltonian in eV for AlSb.
UNDER: Empirical matrix elements of the 

$$
sp^3s^{\ast}
$$

 Hamiltonian in eV for InSb.

33
<!-- SLUTT SIDE 4 -->

<!-- START SIDE 5 -->
-1.1627 $E(s,c)$
3.5867 $E(p,c)$
6.7267 $E(s^{\ast},c)$
-7.5273 $E(s,a)$
0.9833 $E(p,a)$
5.0483 $E(s^{\ast},a)$
-6.6642 $V(s,s)$
1.8780 $V(x,x)$
4.2919 $V(x,y)$
5.1106 $V(sa,pc)$
5.4965 $V(pa,sc)$
1.5216 $V(s^{\ast}a,pc)$
4.9950 $V(pa,s^{\ast}c)$
0.0000 $V(s^{\ast},s^{\ast})$
2.45 d=bond length in \text{Å}ngstrom.

Table 2.3: Empirical matrix elements of the 

$$
sp^3s^{\ast}
$$

 Hamiltonian in eV for AlAs.

With these tables I have the numerical data I need to do all the calculations that are done in this diploma work. It is now time to proceed, and try to show how I use this data material.

## 2.2 Energy vectors and hopping matrices.

The energy vectors $E_a$ and $E_c$ in the 

$$
sp^3s^{\ast}
$$

 model have elements that deal with the energy of the orbitals at anion and cation layers. For the cations we get:

$$
\begin{aligned}
E_c(1) = E(s,c) = \langle s,c, \vec{R}|H|s,c, \vec{R} \rangle \\
E_c(2) = E(p,c) = \langle p,c, \vec{R}|H|p,c, \vec{R} \rangle \\
E_c(3) = E(p,c) = \langle p,c, \vec{R}|H|p,c, \vec{R} \rangle \\
E_c(4) = E(p,c) = \langle p,c, \vec{R}|H|p,c, \vec{R} \rangle \\
E_c(5) = E(s^{\ast},c) = \langle s^{\ast},c, \vec{R}|H|s^{\ast},c, \vec{R} \rangle
\end{aligned}
$$

(2.4)

And for the anions:

$$
\begin{aligned}
E_a(1) = E(s,a) = \langle s,a, \vec{R}|H|s,a, \vec{R} \rangle \\
E_a(2) = E(p,a) = \langle p,a, \vec{R}|H|p,a, \vec{R} \rangle \\
E_a(3) = E(p,a) = \langle p,a, \vec{R}|H|p,a, \vec{R} \rangle \\
E_a(4) = E(p,a) = \langle p,a, \vec{R}|H|p,a, \vec{R} \rangle \\
E_a(5) = E(s^{\ast},a) = \langle s^{\ast},a, \vec{R}|H|s^{\ast},a, \vec{R} \rangle
\end{aligned}
$$

(2.5)

As long as we deal with pure materials we now only need to put in the correct measurements as the correct element in the vector. If we deal with blends as InGaAs, GaAlSb, and so on, we only multiply the VCA parameter by the concentration of the material it is valid for and add the contributions together to find the VCA parameter for the mixed material.

34
<!-- SLUTT SIDE 5 -->

<!-- START SIDE 6 -->
The so called hopping matrices are build up from VCA parameters that are features that say something about the potential difference between states at closest neighbour lattice points. I use two kinds of hopping matrices, the $V_{hopping}$ matrices that deals with hopping between latticepoints (between the monolayers in the structure), and the $U_{hopping}$ matrices that concerns hopping between the anion and cation inside the same monolayer. The hopping matrices in the $sp^3s^{\ast}$ model are of dimension $5 \cdot 5$, and their elements are defined in the equations below. Before writing down the elements for the four matrices I will define four trigonometric functions, c1, c2, s1 and s2 that comes out as parts of the solutions for the matrix elements.

$$
\begin{aligned}
s1 = i \cdot \sin((ky + kz) \cdot a/4)/2 \\
s2 = i \cdot \sin((ky - kz) \cdot a/4)/2 \\
c1 = \cos((ky + kz) \cdot a/4)/2 \\
c2 = \cos((ky - kz) \cdot a/4)/2 \quad (2.6)
\end{aligned}
$$

Here $i$ is the imaginary constant.
I will start with the elements of the Uca matrix with cosinus like solutions:

$$
\begin{aligned}
Uca(1,1) = V(s,s) \cdot c2 = 4 \cdot c2 \langle s, a, \vec{R}|H|s, c, \vec{R} \rangle \\
Uca(1,2) = V(pa,sc) \cdot c2 = 4 \cdot c2 \langle p, a, \vec{R}|H|s, c, \vec{R} \rangle \\
Uca(2,1) = -V(sa,pc) \cdot c2 = -4 \cdot c2 \langle s, a, \vec{R}|H|px, c, \vec{R} \rangle \\
Uca(2,2) = V(x,x) \cdot c2 = 4 \cdot c2 \langle px, a, \vec{R}|H|px, c, \vec{R} \rangle \\
Uca(2,5) = -V(s^{\ast}a,pc) \cdot c2 = -4 \cdot c2 \langle s^{\ast}, a, \vec{R}|H|p, c, \vec{R} \rangle \\
Uca(3,3) = V(x,x) \cdot c2 = 4 \cdot c2 \langle px, a, \vec{R}|H|px, c, \vec{R} \rangle \\
Uca(3,4) = -V(x,y) \cdot c2 = -4 \cdot c2 \langle px, a, \vec{R}|H|py, c, \vec{R} \rangle \\
Uca(4,4) = V(x,x) \cdot c2 = 4 \cdot c2 \langle px, a, \vec{R}|H|px, c, \vec{R} \rangle \\
Uca(5,2) = V(pa,s^{\ast}c) \cdot c2 = 4 \cdot c2 \langle px, a, \vec{R}|H|s^{\ast}, c, \vec{R} \rangle \\
Uca(5,5) = (0,0) \quad (2.7)
\end{aligned}
$$

And for the matrix elements with sinus like solutions:

$$
\begin{aligned}
Uca(1,3) = V(pa,sc) \cdot s2 = 4 \cdot s2 \langle p, a, \vec{R}|H|s, c, \vec{R} \rangle \\
Uca(1,4) = -V(pa,sc) \cdot s2 = -4 \cdot s2 \langle p, a, \vec{R}|H|s, c, \vec{R} \rangle \\
Uca(1,5) = (0.0\text{d}0, 0.0\text{d}0) \\
Uca(2,3) = V(x,y) \cdot s2 = 4 \cdot s2 \langle px, a, \vec{R}|H|py, c, \vec{R} \rangle \\
Uca(2,4) = -V(x,y) \cdot s2 = -4 \cdot s2 \langle px, a, \vec{R}|H|py, c, \vec{R} \rangle \\
Uca(3,1) = -V(sa,pc) \cdot s2 = -4 \cdot s2 \langle s, a, \vec{R}|H|px, c, \vec{R} \rangle \\
Uca(3,2) = V(x,y) \cdot s2 = 4 \cdot s2 \langle px, a, \vec{R}|H|py, c, \vec{R} \rangle \\
Uca(3,5) = -V(s^{\ast}a,pc) \cdot s2 = -4 \cdot s2 \langle s^{\ast}, a, \vec{R}|H|px, c, \vec{R} \rangle \\
Uca(4,1) = V(sa,pc) \cdot s2 = 4 \cdot s2 \langle s, a, \vec{R}|H|px, c, \vec{R} \rangle \\
Uca(4,2) = -V(x,y) \cdot s2 = -4 \cdot s2 \langle px, a, \vec{R}|H|py, c, \vec{R} \rangle \\
Uca(4,5) = V(x,y) \cdot s2 = 4 \cdot s2 \langle px, a, \vec{R}|H|px, c, \vec{R} \rangle \\
Uca(5,1) = (0,0) \\
Uca(5,3) = V(pa,s^{\ast}c) \cdot c2 = 4 \cdot c2 \langle px, a, \vec{R}|H|s^{\ast}, c, \vec{R} \rangle \\
Uca(5,4) = -V(pa,s^{\ast}c) \cdot s2 = -4 \cdot s2 \langle px, a, \vec{R}|H|s^{\ast}, c, \vec{R} \rangle \quad (2.8)
\end{aligned}
$$

The other U-matrix, the matrix for electrons hopping the opposite direction between anions
<!-- SLUTT SIDE 6 -->

<!-- START SIDE 7 -->
and cations at the same latticepoint, is nothing else than the complex conjugate of the first U-matrix.
For hopping between different monolayers / lattice points we use so called V-matrices.
First I define the elements with cosinus solutions:

$$
\begin{aligned}
Vca(1,1) &= V(s,s)*cl = 4*cl \langle s, a, \vec{R}|H|s, c, \vec{R} \rangle \\
Vca(1,2) &= -V(pa,sc)*cl = -4*cl \langle p, a, \vec{R}|H|s, c, \vec{R} \rangle \\
Vca(1,5) &= (0,0) \\
Vca(2,1) &= V(sa,pc)*cl = 4*cl \langle s, a, \vec{R}|H|px, c, \vec{R} \rangle \\
Vca(2,2) &= V(x,x)*cl = 4*cl \langle px, a, \vec{R}|H|px, c, \vec{R} \rangle \\
Vca(2,5) &= V(s^{\ast}a,pc)*cl = 4*cl \langle s^{\ast}, a, \vec{R}|H|px, c, \vec{R} \rangle \\
Vca(3,3) &= V(x,x)*cl = 4*cl \langle px, a, \vec{R}|H|px, c, \vec{R} \rangle \\
Vca(3,4) &= V(x,y)*cl = 4*cl \langle px, a, \vec{R}|H|py, c, \vec{R} \rangle \\
Vca(4,3) &= V(x,y)*cl = 4*cl \langle px, a, \vec{R}|H|py, c, \vec{R} \rangle \\
Vca(4,4) &= V(x,x)*cl = 4*cl \langle px, a, \vec{R}|H|px, c, \vec{R} \rangle \\
Vca(5,1) &= (0,0) \\
Vca(5,2) &= -V(pa,s^{\ast}c)*cl = -4*cl \langle px, a, \vec{R}|H|s^{\ast}, c, \vec{R} \rangle \\
Vca(5,5) &= (0,0) \quad (2.9)
\end{aligned}
$$

Then I define the elements with sinus like solutions:

$$
\begin{aligned}
Vca(1,3) &= V(pa,sc)*s1 = 4*s1 \langle p, a, \vec{R}|H|s, c, \vec{R} \rangle \\
Vca(1,4) &= V(pa,sc)*s1 = 4*s1 \langle p, a, \vec{R}|H|s, c, \vec{R} \rangle \\
Vca(2,3) &= -V(x,y)*s1 = -4*s1 \langle px, a, \vec{R}|H|py, c, \vec{R} \rangle \\
Vca(2,4) &= -V(x,y)*s1 = -4*s1 \langle px, a, \vec{R}|H|py, c, \vec{R} \rangle \\
Vca(3,1) &= -V(sa,pc)*s1 = -4*s1 \langle s, a, \vec{R}|H|px, c, \vec{R} \rangle \\
Vca(3,2) &= -V(x,y)*s1 = -4*s1 \langle px, a, \vec{R}|H|py, c, \vec{R} \rangle \\
Vca(3,5) &= V(s^{\ast}a,pc)*s1 = -4*s1 \langle s^{\ast}, a, \vec{R}|H|px, c, \vec{R} \rangle \\
Vca(4,1) &= -V(sa,pc)*s1 = -4*s1 \langle s, a, \vec{R}|H|px, c, \vec{R} \rangle \\
Vca(4,2) &= -V(x,y)*s1 = -4*s1 \langle px, a, \vec{R}|H|py, c, \vec{R} \rangle \\
Vca(4,5) &= V(s^{\ast}a,pc)*s1 = -4*s1 \langle s^{\ast}, a, \vec{R}|H|px, c, \vec{R} \rangle \\
Vca(5,3) &= V(pa,s^{\ast}c)*s1 = 4*s1 \langle px, a, \vec{R}|H|s^{\ast}, c, \vec{R} \rangle \\
Vca(5,4) &= V(pa,s^{\ast}c)*s1 = 4*s1 \langle px, a, \vec{R}|H|s^{\ast}, c, \vec{R} \rangle \quad (2.10)
\end{aligned}
$$

Also for the V-matrix, the other alternative, the one for going the opposite direction between lattice points, is the complex conjugate of the first one.
With this I feel that the presentation of the matrix elements of the hopping matrices is completed. Anyway, the theory behind the formula for each matrix element is presented in more detail in the theory chapter. At least, I have tried to connect the content of the Vogl files, the VCA parameters, to the theory. And I hope that this last presentation will make every little detail in the theory less dizzy.
For finishing this section I will write down the equation that computes the lattice constant $a$ from the measured bond length $d$.

$$
a = \frac{4d}{\sqrt{3}} \quad (2.11)
$$

36
<!-- SLUTT SIDE 7 -->

<!-- START SIDE 8 -->
And now the only thing reminding in this chapter is is to show how to find the surface Green matrices.

## 2.3 The surface Green matrices

To use the VCA parameters, via hopping matrices and energy vectors, and the lattice constant, to find the surface Green functions for the homogeneous materials we need to solve for the complex band structure and find the eigenstates corresponding to the various impulses. When these eigenstates is found we can compute the surface Green functions, which I prefer to refer to as gamma-matrices from now on.

If I consider a semiconductor barrier system with electrons tunneling from a left contact to a right contact, I compute gamma-plus matrices for the material of the right contact (which in my case is GaSb) and gamma-minus matrices for the left contact (InAs). The minuses and the pluses are connected to the direction we consider as the positive transport direction.

The gamma-matrices, or the surface Green functions, say something about the electrons probability for tunneling from the lattice point where it is stated, into a contact. That is, the gamma-minus matrix concernes tunneling back into the left contact, the contact the electron came from. And the gamma-plus matrix concerns the tunneling in the forward direction, or the tunneling into the right contact.

When I have found gammamatrices for the contact materials I can find the gammamatrices for new materials adding atomlayer for atomlayer by use of an iteration formula, which I have verified in the theory chapter. This new materials might for example be the semi infinite GaSb contact with one layer of AsSb on the right hand side, or the semi infinite InAs contact with ten monolayers of AlSb and one monolayer of GaSb. Here is the formula is in its most general form as in equation 1.111:

$$
\Gamma_{a,N}^{+} = \frac{1}{E-E_{a,N}-V_{ac}(\Gamma_{c,N+1}^{+})V_{ca}}
$$

$$
\Gamma_{c,N}^{+} = \frac{1}{E-E_{c,N}-U_{ca}(\Gamma_{a,N}^{+})U_{ac}}
$$

And, for gamma-plus matrices.

$$
\Gamma_{c,N+1}^{-} = \frac{1}{E-E_{c,N}-V_{ca}(\Gamma_{a,N}^{-})V_{ac}} \quad (2.12)
$$

$$
\Gamma_{a,N+1}^{-} = \frac{1}{E-E_{a,N}-U_{ac}(\Gamma_{c,N+1}^{-})U_{ca}} \quad (2.13)
$$

for gamma-minus matrices.

Ok, back to the problem of finding the gamma-matrices for the pure materials, that builds up my halfinfinite contacts. To find these surface Green functions that gives me a starting point for using the iteration formula shown over, equation 1.111, I have to involve eigenstates $w_j$ that is related to an impuls vector $k$. These features the complex band structure, and they will be explained later.
In my case the right end of the structure will be something like what is presented in figure 2.1.
<!-- SLUTT SIDE 8 -->

<!-- START SIDE 9 -->
The first lattice point in the right contact that is unaffected by the barrier in the nearest neighbor interaction model

The barrier is continuing in the left direction.
A boundary.
The right contact.
One lattice point.

The only lattice point in the right contact that is disturbed by the effects from the barrier.

Figure 2.1: The right end of the structure.

As we see, the first lattice point in the right contact seen from left is a cation. This is common for all the layers in the structure. This first lattice point is also disturbed by the presence of the barrier layers and is not a part of the homogeneous system that I will find gamma-plus matrices for by use of the eigenstates. The first lattice point that is a part of this system is the second lattice point, seen from left, in the right contact. For this lattice point I find the gamma matrices; remember that the gamma matrices I need in the right contact are gamma-plus matrices, for the anion layer via the eigenstates, and I use the iteration formula 1.111 to find the gamma matrix for the cation layer. The formula used to find the surface Green function for the mentioned anion layer is:

$$
\Gamma_a^+ = Aap \frac{1}{Acp} U_{a,c}
$$

(2.14)

Here $Aap$ and $Acp$ are two 5 times 5 parts of the $w$ matrix. More precise: $Aap$ has 1.1 element equal to the 1.1 element in $w$, 1.2 element equal to the 1.2 element of $w$ and so on till the 5.5 element. $Acp$ has 1.1 element equal to the 6.1 element in $w$, 1.2 element equal to the 6.2 element in $w$ until the 5.5 element in $Acp$ that is equal to the 10.5 element in $w$. The $w$ matrix contains eigenstates obtained from solving for the complex band structure. The content of $w$ can be explained by relating $w$ to the $k$'s belonging to the eigenstates.

*   $ks(1)=$smallest real $k$ with $v > 0$
*   $ks(5)=$complex $k$ with largest positive $Im$ $k$
*   $ks(6)=$smallest real $k$ with $v < 0$
*   $ks(10)=$complex $k$ with largest negative $Im$ $k$

Here the $k$ are the impulses found from solving for the complex band structure. They are sorted after the principles sketched in the items above. The first elements in the $k$ vector are those with $Im(k)$ equal to zero and eigenstates that give positive velocities; they are sorted after the value of the real part of $k$, the smallest first and so on. The next elements are those with $Im(k) > 0$, the smallest first... The rest of the sorting of the elements of the $k$ vector should be easy to see from the items, now as the idea is explained.

38
<!-- SLUTT SIDE 9 -->

<!-- START SIDE 10 -->
The eigenvectors are stored in a 10 times 10 matrix $w$. Each column in this matrix is an eigenvector belonging to an element in the $k$ vector. The $n$'th column in $w$ is belonging to the $n$'th element in $k$. Well, I hope this can help on the understanding of equation 2.14. Anyway I will now continue with the equation for gammaminusmatrices in the left contact. But, first I will show the lattice point that I choose to calculate the gamma-minus matrix for the cation layer for.

The first latticepoint in the left contact that is not disturbed by the barrier.
The only latticepoint in the left contact that is disturbed by the barrier.
The first latticepoint in the barrier.

The left contact.
The barrier is preceding in the right direction

Figure 2.2: The left end of the structure.

The formula for the gamma-minus matrix is given in equation 2.15:

$$
\Gamma_c^- = Acm \frac{1}{Aam} U_{a,c}^{-1} \quad (2.15)
$$

Here $Acm$ and $Aam$ have elements equal to the elements of the region of contact and has elements that reaches from 6.6 to 10.10 in $w$.
$Aam$ has elements that reaches from 1.6 to 5.10 in the $w$ matrix.
$Acm$ has elements that reaches from 1.6 to 5.10 in the $w$ matrix.

The reason why I chose to find the gamma-minus matrix for an cation layer in the homogeneous left contact (of semi infinite dimension) is similar to the reason why I chose to find the gamma-plus matrix for an anion layer in the right contact. Partly because of my choice to use anion-cation as the sequence of layers over the boundaries. That is, seen from left will every material end on an anion layer and start on an cation layer. And partly because I feel that it is easy to keep order in the chaos if I produce gamma matrices for an integer number of monolayers. And finally because I don't want to use the formula for producing gamma matrices through use of eigenstates for homogeneous materials on atomic layers in a lattice point that do not entirely belong to a homogeneous contact. This might be the first lattice point seen from left in the right contact, or the first lattice point seen from right in the left contact, see figures 2.1, 2.2 and 2.3.

In figure 2.3 I show the opposite choice of sequence of anions and cations as I cross the boundaries going from left to right. One can easily see that I would have to calculate gamma-minus matrices in the left contact for an anion layer and gamma-plus matrices in the right contact, if I should insist on following the demands that is mentioned over. I'm aware of the fact that these demands is not necessary, but only a result of an attempt of trying to do

39
<!-- SLUTT SIDE 10 -->

<!-- START SIDE 11 -->
things as clean as possible.

Figure 2.3: The opposite configuration of anions and cations.

To end this section I can mention two more features connected to the $k$ values from solving for the complex band structure, namely $y$ and $v$. For each element in the $k$ vector there is a eigenvector in the $w$ matrix, a $y$ value and a $v$ value. The formula for the $y$ value is given in equation 1.91 and the formula for the connected velocities is given in equation 1.71.

## 2.4 The local elements of the Greenfunction.

To complete this chapter I will write down the formula for getting the local elements of the Greenfunction from the hopping matrices and the gamma matrices found in the previous sections. To find these local elements I use two kinds of surface Greenfunctions, gamma-minus matrices and gamma-plus matrices. The general idea is that one use the gamma matrix for the two nearest neighbors of one atomic layer, and the hopping matrices that connect the two different nearest neighbors to the atomic layer, to create the local element of the Greenfunction. For cationlayers the formula is:

$$
G_{00c} = \left( E-E_c-U_{c,a}(\Gamma_a^+)^{-1}U_{a,c}-V_{c,a}(\Gamma_a^-)^{-1}V_{a,c} \right)^{-1} \quad (2.16)
$$

In this formula $E$ is the energy of the electron and $E_c$ is the energy vector with the energy of the orbitals of the atomic layer we want to find the local Greenfunction for as elements. The matrix $\Gamma_a^+$ that is being multiplied with hopping matrices $U$ is the gamma-plus matrix for the anionlayer at the same lattice point as the cationlayer we want to find the local Greenfunction for. The other gamma matrix $\Gamma_a^-$ is the gamma-minus matrix for the other nearest neighbor atomic layer. For anionlayers the formula is:

$$
G_{00a} = \left( E-E_a-V_{a,c}(\Gamma_c^+)^{-1}V_{c,a}-U_{a,c}(\Gamma_c^-)^{-1}U_{c,a} \right)^{-1} \quad (2.17)
$$

Here the energy vector $E_a$ has elements equal to the energy of the orbitals of the atoms in the atomic layer that I compute the local Greenfunction for.

40
<!-- SLUTT SIDE 11 -->
