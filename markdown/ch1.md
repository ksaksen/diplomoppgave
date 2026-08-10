# Transkripsjon av kapittel1.pdf

<!-- START SIDE 1 -->
# Chapter 1
## Nearest neighbor tight binding approximation.

In this chapter I will try to present the theory that gives me the methods I use in the calculations in this diploma work. As the model I use is a nearest neighbor tight binding approximation, the content of this chapter will be to establish a theory for such a model, and show the framework of the methods of calculation that is used in this model. The theory is identical to what I used in my fourth class project work. So this theory chapter is very much the same as the theory chapter in the report of my project work. But I hope that I will manage to change the presentation to the better. And, I find the theory to be essential in this diploma work and choose to include the theory chapter in the report and not only refer the report of my project work. I also hope to change the parts of the theory from the project that was unclear and fuzzy so that they will be more exact, and so that it will be easier to follow the arguments that lead to the methods used in the calculations.

The main purpose of this theory chapter is to show how one can go from the simplest form of the Schrödinger equation to a notation of the quantum mechanics that involves Green's functions, not Hamiltonian operators, how these Green's functions can be found, and how one can use them to find expressions for, for example, the transmission and reflection coefficients. Beside this, I will also explain the model that is used, a tight-binding nearest-neighbor approximation. And, strongly correlated to the explanation of the model I will use some space to tell about the internal structure of the semiconductors that are used.

### 1.1 The Schrödinger equation

In this section I will show how the wave function for an electron which is passing through a potential barrier in one dimension can be expressed by the reflection and transmission amplitudes $r(k)$ and $t(k)$. I will also show how the amplitudes $r$ and $t$ are expressed by the wave function on the surface between different semiconductors, or less specifically, how the amplitudes are expressed by means of the boundary conditions of the potential barrier. We start with the time-dependent Schrödinger equation:

$$
H\Psi = i\hbar \frac{\partial}{\partial t}\Psi \quad (1.1)
$$

Here is
<!-- SLUTT SIDE 1 -->

<!-- START SIDE 2 -->
and

$$
H = -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x) \quad (1.2)
$$

$$
\Psi = \Phi \exp \left( i \frac{E}{\hbar} t \right) \quad (1.3)
$$

The last equation shows how $\Psi$ might be separated into a time-independent part $\Phi$ and an exponential time factor, which is nothing more than a plane wave in the dimension of time. $H$ is the Hamiltonian for the electron in the semiconductor, and $V(x)$ is the potential barrier. Specifically, $V(x)$ might be due to the different band structure of different semiconductors. Using the mentioned separation, we obtain the time-independent Schrödinger equation:

$$
H \Phi = E \Phi. \quad (1.4)
$$

Here $E$ is the energy eigenvalue for the wave function $\Phi$. In the problem we are considering, we have a situation where a free electron is partly reflected by and partly transmitted through a potential barrier. As the kinetic energy of the incoming electron is assumed to be constant, the only effect of the separation is that the potential $V$ is also treated as constant in time. This situation is illustrated in Figure 1.1, that is, for a general potential barrier.

Figure 1.1: A general potential barrier.

In Figure 1.1, I is an incoming, R a reflected, and T a transmitted electron. The reflected and transmitted parts are moving as plane waves away from the barrier on each side. The

8
<!-- SLUTT SIDE 2 -->

<!-- START SIDE 3 -->
relative size of the two intensities (or probabilities for finding electrons) on each side of the barrier is given from the definition of the amplitudes $r$ and $t$. With an incoming electron wave, $\exp(ikx)$, the function $\Phi$ gets the value that is given in equation 1.5 for the different areas of the structure.

$$
\Phi(x) =
\begin{cases}
\exp(ikx) + r(k) \exp(-ikx) & \text{if } x < 0 \\
\chi(x) & \text{if } 0 < x < L \\
t(k) \exp(ikx) & \text{if } x > L
\end{cases}
\quad (1.5)
$$

$\chi$ is the wave function in the area where the potential $V(x)$ is nonzero. That is, inside the potential barrier. To make sure that this is correct we might test for $x < 0$. We assume that the electron moves as a free particle in the part of the semiconductor lattice where $V(x)=0$ (def. perfect lattice) if this lattice is infinite, with the energy $E = \vec{p}^2/2m$. Using $H$ on $\Phi$ in the area where $x < 0$ we obtain

$$
H[\exp(ikx) + r(k) \exp(-ikx)] = \frac{\hbar^2 k^2}{2m} [\exp(ikx) + r(k) \exp(-ikx)]. \quad (1.6)
$$

With $\hbar\vec{k} = \vec{p}$,

we get that $H\Phi = E\Phi$, which is nothing other than the time independent Schrödinger equation, which is a valid equation for structures like the one in figure 1.1. Usual demand on a wave function $\Phi$ is that both the function and its first derivative are continuous. This is especially important as it gives boundary conditions. In this diploma work, this will be both reflection and transmission coefficients. These demands give that:

$$
1 + r(k) = \chi(0) \quad (1.7)
$$

$$
t(k) \exp(ikL) = \chi(L) \quad (1.8)
$$

$$
ik(1 - r(k)) = \frac{\partial}{\partial x}\chi(0) \quad (1.9)
$$

$$
ikt(k) \exp(ikL) = \frac{\partial}{\partial x}\chi(L). \quad (1.10)
$$

And, these equations might be solved easily for a constant potential barrier, a potential wall, but that is not so for a more complicated potential. And that is exactly what I will treat in this diploma work. As mentioned earlier I will do calculations on the specific structure GaSb-AlSb-InAs-GaSb-AlSb-InAs. Here the potential barrier is the central AlSb-InAs-GaSb-AlSb composition. The real barrier in the composition is the AlSb layers. The InAs and GaSb layers in the center work more or less as a well. And what I am going to study is the recombination of electrons and holes as electrons are tunneling from conduction bands in the InAs contact to valence bands in the GaSb contact. The important phenomenon in this study is the resonance between the two AlSb barriers.

9
<!-- SLUTT SIDE 3 -->

<!-- START SIDE 4 -->
1.2 Discrete coordinates.

The way I solve the problems due to varying potential is to think of (the dimension in which the potential is varying) as a set of discrete points. The potential barrier extends across N atomic layers in the $x$ direction. We assume that only the nearest neighbor atoms are interacting. Motion in directions orthogonal to the current direction is conserved because of translation invariance in the $y$ and $z$ direction. We write

$$
V_j \begin{cases} \neq 0 & \text{when } 1 \leq j \leq N \\ = 0 & \text{otherwise} \end{cases} \quad (1.11)
$$

$V_j$ is the potential at the point $j$.
Figure 1.2 illustrates how the $x$ continuum is changed to a set of discrete points. The points have got numbers equal to the position of the atomic layers in the structure. We then treat the transport as hopping between atomic layers.

Figure 1.2: A picture of a potential barrier when the transport direction is changed from a continuum to a discrete set of points.

In the model I am going to use, the electrons can only move via hopping between neighbor layers in the structure. The hopping matrix element $u$ is connected to the probability for hopping from one layer to its closest neighbor in the transmission direction. The complex conjugated $u^{\ast}$ is connected to the probability for hopping the opposite direction. $V(x)$ has nonzero values only in the discrete points $j$.

In general we can write the Hamiltonian for a system set up by discrete points like this, figure 1.2, as a sum of contributions with hopping matrix elements $u$ and local energy eigenvalues $\epsilon_j$.

$$
H = \sum_j [\vert j \rangle \epsilon_j \langle j \vert + \vert j \rangle u \langle j+1 \vert + \vert j \rangle u^{\ast} \langle j-1 \vert] \quad (1.12)
$$

10
<!-- SLUTT SIDE 4 -->

<!-- START SIDE 5 -->
Here, equation 1.12, the contribution of the hopping matrix elements gives us the kinetic part of the energy, and the energy eigenvalues $\epsilon_j$ give us the energy of the eigenstates $j$. In a later section I will explain in detail what these eigenstates are. Anyway, now I will continue with the Schrödinger equation for a homogeneous system, that is a system with $\epsilon_j = \epsilon_0$ for all $j$, as a sum over atoms $m$ (for a one dimensional string), or in reality over atom layers $m$.

### 1.2.1 Physical content of the hopping matrix elements

In this subsection I will use my knowledge about simple homogeneous discrete systems, specifically the Hamiltonian of such systems to try to obtain a feeling of what the physical content of the hopping matrix element is. I start by setting up the time independent Schrödinger equation for the discrete system and then of course with the Hamiltonian given in equation 1.12.

$$
H|\Phi_k\rangle = \left( \sum_m \left( |m\rangle \epsilon_0 \langle m| + |m\rangle u \langle m+1| + |m\rangle u^{\ast} \langle m-1| \right) \right) \cdot \left( \sum_j \exp(ikja)|j\rangle \right) = E_k|\Phi_k\rangle \quad (1.13)
$$

As the system is homogeneous it is here correct to use the energy $\epsilon_0$ overall and to use the Bloch like eigenstates.

Setting $m$ equal to $m_0$ in equation 1.13, that is, looking specifically on atom number $m_0$, or, more precise, atomic layer number $m_0$, we obtain equation 1.14.

$$
E_k \exp(ikm_0 a) = \epsilon_0 \exp(ikm_0 a) + u \exp(ik(m_0+1)a) + u^{\ast} \exp(ik(m_0-1)a) \quad (1.14)
$$

This because $\langle m | j \rangle = \delta_{mj}$ i.e. equals 1 for $j=m$ and 0 otherwise. Hence,

$$
|m_0\rangle \exp(ikm_0 a)[\epsilon_0 + u \exp(ika) + u^{\ast} \exp(-ika)] = |m_0\rangle \exp(ikm_0 a)E_k \quad (1.15)
$$

*and therefore,*

$$
E_k = \epsilon_0 + u \exp(ika) + u^{\ast} \exp(-ika) \quad (1.16)
$$

This is the expression for the discrete energy eigenvalues for particles moving between lattice points in a homogeneous lattice (this still means nothing else than keeping $\epsilon_j = \epsilon_0$ for all $j$), through hopping processes. And then through hopping processes that is characterised by the hopping matrix elements $u$. For a homogeneous system the electrons in the conduction bands have continuous $\vec{k}$ and the energy eigenvalues of such particles are also continuous, and take values equal to the square of the momentum divided with the mass twice.

The hopping matrix element $u$, that gives an expression for the hopping probability between $\vec{r}$ and $\vec{r} + \vec{R}$ is given as;

$$
u = \int d\vec{r} \Psi^{\ast}(\vec{r}) H \Psi(\vec{r} + \vec{R}) \sim \exp(i\phi) \quad (1.17)
$$

11
<!-- SLUTT SIDE 5 -->

<!-- START SIDE 6 -->
In the model I will use the position vectors are replaced by discrete eigen states $j$, but the meaning of equation 1.17 should still be clear. For the energy eigenvalues we obtain,

$$
E_k = \epsilon_0 + |u|\exp(i[ka+\phi]) + |u|\exp(-i[ka+\phi]) = \epsilon_0 + 2|u|\cos(ka+\phi). \quad (1.18)
$$

The center of the Brillouin zone is located where $E_k$ has its minimum, i.e., we choose $\phi = \pi$. We also choose the value of $\epsilon_0$ so that the energy eigenvalue is zero in the center of the Brillouin zone. With $u$ equal to its own negative absolute value, $u = -|u|$, we get an $\epsilon_0$ with value $-2u$ and the dispersion relation on the form

$$
E(k) = -2u + 2u \cos(ka). \quad (1.19)
$$

This expression can be expanded since

$$
\cos(ka) = 1 - \frac{1}{2}(ka)^2 + ...,
$$

and for small values of $k$ we may write

$$
E(k) \approx -uk^2a^2 = |u|a^2k^2. \quad (1.20)
$$

Through comparing the expression for the energy in the center of the Brillouin zone and the energy of a free electron we obtain an expression for the effective mass of the electrons close to the Brillouin zone center:

$$
\frac{\hbar^2 k^2}{2m^{\ast}} = |u|a^2k^2.
$$

This gives meaning to the hopping matrix element $u$; it is inversely proportional to the effective mass and the square of the unit cell constant, and it is also proportional to the square of $\hbar$:

$$
|u| = \frac{\hbar^2}{2m^{\ast}a^2}. \quad (1.21)
$$

This is valid for electrons in the valence band with wavelength $\lambda$ so that

$$
ka \ll 1 \Rightarrow \frac{2\pi}{\lambda}a \ll 1.
$$

The criterion for $\lambda$ then becomes

$$
\lambda \gg a. \quad (1.22)
$$

Finally we can conclude that the value of $\epsilon_j$ is

$$
\epsilon_j = \begin{cases} \epsilon_0 = -2u & \text{when } j \le 0 \\ \epsilon_0 + V_j = -2u + V_j & \text{when } 1 \le j \le N \\ \epsilon_0 = -2u & \text{when } j \ge N+1 \end{cases} \quad (1.23)
$$

I will now return to the original problem, the time independent Schrödinger equation $(E - H)|\Phi\rangle = 0$ for a system with a potential barrier, not a homogenous system.

12
<!-- SLUTT SIDE 6 -->

<!-- START SIDE 7 -->
## 1.2.2 Perturbation.

We separate the ket $|\Phi\rangle$ into a free particle contribution and a perturbation due to the potential $V$:

$$
|\Phi\rangle = |\Phi^\circ\rangle + |\Phi'\rangle,
$$

where

$$
|\Phi^\circ\rangle = \sum_{j=-\infty}^{0} \exp(ikja)|j\rangle.
$$

Here $|\Phi^\circ\rangle$ is the wave function for a free particle, with the characteristic Bloch form, and is valid only for the incoming electrons while the perturbation $|\Phi'\rangle$ gives contribution to the wave function all over the structure. The energy eigenvalue of this function is known. The Schrödinger equation gives

$$
(E - H)|\Phi'\rangle = -(E - H)|\Phi^\circ\rangle \quad (1.24)
$$

To proceed in our search for the perturbation we must define a Green function $G(E)$:

$$
(E - H)G(E) = 1
$$

or

$$
G(E) = \frac{1}{E - H} \quad (1.25)
$$

Using the Green function we can write the equation for the perturbation $|\Phi'\rangle$:

$$
|\Phi'\rangle = G(E)[-(E - H)|\Phi^\circ\rangle] \quad (1.26)
$$

## 1.3 The Green function $G(E)$.

In this section I will show how to find the matrix elements of the Green function $G(E)$ through recursion and show how to use the Green function to express the reflection and transmission coefficients.

First we recapture (in short) what we have already obtained. We can consider the problem of a free electron with the Schrödinger equation given by

$$
-\frac{\hbar^2}{2m} \frac{\partial^2 \Phi}{\partial x^2} = E \Phi
$$

If one assumes that the eigenstate changes linearly between nearest neighbor lattice points one get after the discretization yields:

$$
\frac{\partial^2 \Phi_i}{\partial x^2} = \frac{\Phi_{i+1} + \Phi_{i-1} - 2\Phi_i}{(\Delta x)^2} \quad (1.27)
$$

13
<!-- SLUTT SIDE 7 -->

<!-- START SIDE 8 -->
This gives for the Schrödinger equation:

$$
-\frac{\hbar^2}{2m (\Delta x)^2}(\Phi_{i+1} + \Phi_{i-1} - 2\Phi_i) = E\Phi_i \quad (1.28)
$$

In section 1.2 we obtained the Hamiltonian as a sum of hopping matrix elements $u$. Assuming that $u$ is real we get

$$
H = \sum_j [|j\rangle \epsilon_0 \langle j| + |j\rangle u \langle j+1| + |j\rangle u \langle j-1|] \quad (1.29)
$$

With this Hamiltonian we get the following Schrödinger equation:

$$
\langle i|H|\Phi\rangle = \langle i|E|\Phi\rangle \equiv E\Phi_i \quad (1.30)
$$

That is

$$
\begin{matrix}
\langle i|E|\Phi\rangle & = \langle i| \sum_j [|j\rangle \epsilon_0 \langle j| + |j\rangle u \langle j+1| + |j\rangle u \langle j-1|] |\Phi\rangle \\
& = \displaystyle \epsilon_0 \Phi_i + u\Phi_{i+1} + u\Phi_{i-1} \\
& = \displaystyle E\Phi_i
\end{matrix}
$$

By comparing with the expression 1.28 obtained from the assumption 1.27 we can see the following:

$$
\frac{\hbar^2}{m(\Delta x)^2} = \epsilon_0
$$

and

$$
-\frac{\hbar^2}{2m(\Delta x)^2} = u
$$

From this we can conclude that

$$
\epsilon_0 = -2u \quad (1.31)
$$

as assumed earlier.
We then assume that the wave function can be written as a sum. Which is nothing other than the plane wave and the perturbation mentioned in the previous section. By writing the Schrödinger equation one gets the definition of the Green function in the last section.
Further we include a potential barrier. We can now write the time independent unperturbed wave function in the area in front of the barrier (where the potential is zero) like this:

$$
|\Phi^o\rangle = \sum_{j \le -1} \exp(ikja) |j\rangle \quad (1.32)
$$

Here $(ja)$ is the position of the atoms, or atomic layers, and $a$ is the lattice constant. Still assuming that $u$ is real we find that

$$
\begin{aligned} -(E-H)|\Phi^o\rangle &= -E \sum_{j \le -1} \exp(ikja) |j\rangle \\ &+ \sum_i (|i\rangle \epsilon_i \langle i| + |i\rangle u \langle i+1| + |i\rangle u \langle i-1|) \sum_{j \le -1} \exp(ikja) |j\rangle, \end{aligned}
$$

<!-- SLUTT SIDE 8 -->

<!-- START SIDE 9 -->
may be written

$$
-(E - H)|\Phi^\circ \rangle = (-E + \epsilon_0 + u \exp(ika) + u \exp(-ika))\Sigma_{j \le -2} \exp(ikja)|j \rangle + |-1 \rangle (-E + \epsilon_0 + u \exp(-ika) + \epsilon_0 \exp(-ika) + u \exp(-2ika)) + |0 \rangle u \exp(ika).
$$

Earlier we calculated the dispersion relation

$$
E(k) = \epsilon_0 + 2u \cos(ka). \quad (1.33)
$$

Putting this in for E, we get a new equality:

$$
|-1 \rangle u \exp(ika) = -(E-H)|\Phi^\circ \rangle = (E-H)|\Phi' \rangle. \quad (1.34)
$$

This leads us to an equation for the perturbed part of the wave function:

$$
|\Phi_k' \rangle = G(E)(|-1 \rangle u + |0 \rangle u \exp(ika)) \quad (1.35)
$$

* $|\Phi^\circ \rangle$ is the incoming part of the wave function for $j \le -1$, an area where the potential $V$ is zero, so that we got a known solution of the time independent Schrödinger equation.
* Through the expression $|\Phi \rangle = |\Phi^\circ \rangle + |\Phi' \rangle$ we now got the unknown $|\Phi' \rangle$ expressed by the known $|\Phi^\circ \rangle$.

We use the notation $G_{ij} = \langle i|G(E)|j \rangle$ for the matrix element $ij$ of the Green function $G(E)$. Then we get

$$
\langle j|\Phi_k' \rangle = u \exp(ika)G_{j,0} - uG_{j,-1}. \quad (1.36)
$$

Using the definition of G and H we get two important equations showing the relation between G, $G^\circ$ and $H'$, where $H = H^\circ + H'$, and $H'$ is obtained from treating the structure as if it consisted of two parts. One involves the right hand side of $i+1$ and $i+1$ itself, and one involves the left hand side of $i+1$ so that $H' = |i \rangle u \langle i+1| + |i+1 \rangle u \langle i|$.

$$
(E-H)G = 1 \quad (E-H^\circ)G^\circ = 1
$$

$$
\Downarrow
$$

$$
(E-H^\circ - H')G = 1 \quad \text{;using the definition of H.}
$$

$$
\Downarrow
$$

$$
G^\circ\left(\frac{1}{G^\circ}\right)G - H'G = G^\circ \quad \text{;multiplying with } G^\circ \text{ from left.}
$$

$$
\Downarrow
$$

$$
G = G^\circ + GH'G^\circ \quad \text{;using the 2.statement and multiplying with G from left.}
$$

<!-- SLUTT SIDE 9 -->

<!-- START SIDE 10 -->
We have then got the two equations mentioned earlier:

$$
G = G^\circ + G^\circ H'G = G^\circ + GH'G^\circ. \quad (1.37)
$$

This is the Dyson equation. The following relation is satisfied: $ \langle m|G^\circ|n \rangle = 0 $ if $ m \leq i $ and $ n \geq i+1 $ or if $ n \leq i $ and $ m \geq i+1 $.
We then move to the definition of the surface matrix elements of the Green function $G$.
They are given the names $\Gamma^+$ and $\Gamma^-:$

$$
G_{i,i}^\circ = \langle i|G^\circ|i \rangle \equiv \Gamma_i^-,
$$

$$
G_{i+1,i+1}^\circ = \langle i+1|G^\circ|i+1 \rangle \equiv \Gamma_{i+1}^+.
$$

With $G = G^\circ + G^\circ H'G$ we get

$$
\begin{aligned}
G_{i,i} = G_{i,i}^\circ + \langle i|G^\circ H'G|i \rangle \\
= G_{i,i}^\circ + \langle i|G^\circ|[i \rangle u \langle i+1|G|i \rangle \\
= G_{i,i}^\circ + \langle i|G^\circ|i \rangle u \langle i+1|G|i \rangle \\
= G_{i,i}^\circ + G_{i,i}^\circ u G_{i+1,i}. \quad (1.39)
\end{aligned}
$$

Similarly as $G_{i+1,i}^\circ$ is zero,

$$
G_{i+1,i} = G_{i+1,i+1}^\circ u G_{i,i}. \quad (1.40)
$$

From equations 1.40 and 1.41 we can find the following useful formula connected to the matrix elements of the Green function:

$$
\frac{1}{G_{i,i}} = \frac{1}{\Gamma_i^-} - u(\Gamma_{i+1}^+)u,
$$

Setting in expressions 1.25 and 1.39 we obtain

$$
\frac{1}{G_{i,i}} = E - \epsilon_i - u(\Gamma_{i-1}^-)u - u(\Gamma_{i+1}^+)u,
$$

and inverting to get

$$
G_{i,i} = \frac{1}{E - \epsilon_i - u(\Gamma_{i-1}^-)u - u(\Gamma_{i+1}^+)u}. \quad (1.42)
$$

From repeated use of equation 1.41 we find an iteration formula for the elements $ i+n, i $ of the Green matrix.

$$
G_{i+n,i} = (\Gamma_{i+n}^+)u(\Gamma_{i+n-1}^+)u \ldots (\Gamma_{i+1}^+)u G_{i,i}. \quad (1.43)
$$

and for iterating in the opposite direction.

$$
G_{i+n,i} = G_{i+n,i+n} u(\Gamma_{i+n-1}^-)- \ldots u(\Gamma_i^-). \quad (1.44)
$$

16
<!-- SLUTT SIDE 10 -->

<!-- START SIDE 11 -->
To find the density of states $D(E)$ one can use the surface element of the Green matrix, $G_{i,i}$. $D(E)$ is per definition like

$$
D(E) = - \frac{1}{\pi} \text{Im}[G_{i,i}(E_k)]. \quad (1.45)
$$

For a homogeneous one dimensional chain one has

$$
D(E) = \frac{1}{2\pi|u|\sin(ka)}. \quad (1.46)
$$

From general quantum mechanics one finds the dependence on the energy for the density of states $D(E)$:

$$
D(E) \sim \begin{cases} \frac{1}{\sqrt{E}} & \text{for 1D} \\ \frac{1}{E^0} & \text{for 2D} \\ \sqrt{E} & \text{for 3D}. \end{cases} \quad (1.47)
$$

For $ka \ll 1$, $E_k$ is equal to $-2u + 2u \cos(ka)$ which is approximately equal to $|u|k^2a^2$ and $ka$ is equal to the square root of $\sqrt{E_k/|u|}$. This gives us that $D(E_k) \approx |u|ka/2\pi \approx 1/2\pi \sqrt{|u|} \cdot 1/\sqrt{E_k}$. This is equivalent to the general result from quantum mechanics which shows that $D(E)$ is proportional to $1/\sqrt{E_k}$ in the one dimensional case.

## 1.4 Impurities.
Impurities in the materials that sets up the lattice changes the energy relations slightly. And therefore also the Green functions. Earlier we have found for a homogeneous system that

$$
G_{i+n,i}(E_k) = \Gamma_{i+n}u\Gamma_{i+n-1}u...\Gamma_i G_{i,i}
$$

$$
= (\Gamma u)^n G_{i,i}
$$

$$
= E^{inka} G_{i,i}(E_k). \quad (1.48)
$$

as the hopping matrix elements and the surface Green functions are identical for all monolayers in a homogeneous lattice. For a system with an impurity $\Delta$ in the position $l$ we got

$$
\frac{1}{G_{ii}(z)} = [z-\epsilon_i - u(\Gamma_{i-1}^-)u - u(\Gamma_{i+1}^+)u]
$$

$$
= [z-\epsilon_0-\Delta - 2u^2[\frac{1}{z-\epsilon_0} - \frac{1}{2u^2}\sqrt{(z-\epsilon_0)^2-4u^2}]]
$$

$$
= [-\Delta + \sqrt{(z-\epsilon_0)^2-4u^2}]. \quad (1.49)
$$

So $G_{i,i}$ has pole for $-\Delta + \sqrt{(z-\epsilon_0)^2 - 4u^2} = 0$ which implies that $z = \epsilon_0 \pm \sqrt{\Delta^2 + 4u^2}.$

## 1.5 Transmission and reflection coefficients
Taking into account 1.35, which says that

$$
\vert \Phi_k' \rangle = G(E)[\vert -1 \rangle u + \vert 0 \rangle u \exp(-ika)]
$$

17
<!-- SLUTT SIDE 11 -->

<!-- START SIDE 12 -->
and as the $i$-th element of the state vector $|\Phi'_k\rangle$ is obtained by multiplying it by $\langle i|$ as follows:

$$
\Phi'_i \equiv \langle i|\Phi'_k\rangle = -G_{i,-1}(E)u + G_{i,0}(E)u \exp(ika),
$$

where

$$
G_{i,-1}(E) = G^\circ_{i,-1}(E) + G_{i,0}u_{0,-1}G^\circ_{-1,-1} = G_{i,0}u\Gamma^-,
$$

gives that

$$
\Phi'_i = -G_{i,0}u\Gamma^- u + G_{i,0}u \exp(ika) = -2iu \sin(ka)G_{i,0} \quad (1.50)
$$

for $i \geq 0$. It is understood that $G_{i,0} = G^\circ_{i,0}(E)$ and that all other elements of $G$ are functions of $E$, even though it is not written everywhere. The lattice points are numbered as in figure 2 with 0 as the last atomic layer before the potential barrier and $N$ as the last atomic layer before the end of the potential barrier. Since

$$
\Phi(N+1) = t(k) \exp(ika(N+1)), \quad (1.51)
$$

we find the result for $t(k)$:

$$
t(k) = -2iu \sin(ka) \exp(-ika(N+1))G_{N+1,0}^\circ. \quad (1.52)
$$

Through the same procedure we get from the knowledge of lattice point number $-1$ the expression for the reflection coefficient

$$
r(k) = -G_{-1,-1}u \exp(-ika) = G_{-1,0}u \exp(-2ika). \quad (1.53)
$$

We have then expressed the reflection and transmission coefficients by means of the Green function; as we wanted. As we first are dealing with observables we might for example look at the current density $j(x)$:

$$
j(x) = \frac{e\hbar}{2im} \left( \Phi^{\ast}(x) \frac{\partial\Phi(x)}{\partial x} - \frac{\partial\Phi(x)^{\ast}}{\partial x} \Phi(x) \right). \quad (1.54)
$$

The operator which belongs to $j(x)$ is identical to the velocity operator.

$$
\begin{aligned}
\hat{j} = -e\hat{v} = -\frac{ei}{\hbar}[\hat{v}, H] \\ = -\frac{ei}{\hbar}\sum_{j}|j\rangle ja \langle j| \sum_m \left( |m\rangle \epsilon_0 \langle m| + |m\rangle u \langle m \pm 1| \right). \quad (1.55)
\end{aligned}
$$

This because
and

$$
i\hbar \frac{\partial A}{\partial t} = [A, H],
$$

18
<!-- SLUTT SIDE 12 -->

<!-- START SIDE 13 -->
$\hat{x} = \sum_j \vert j \rangle ja \langle j \vert$.

Further we have that hopping matrix elements $u$ give the only contributions to the current. Through further calculations we get that

$$
\hat{j} = \frac{ei}{\hbar} \sum_j (\vert j \rangle ja \langle j+1 \vert - \vert j \rangle ja \langle j-1 \vert ) \quad (1.56)
$$

That is; the current operator has matrix elements as follows:

$$
\hat{j}_{i,i+1} = \frac{ei}{\hbar}ua(\vert i \rangle \langle i+1 \vert - \vert i+1 \rangle \langle i \vert) \quad (1.57)
$$

Through multiplication with the state vector $\vert \Phi \rangle$ and its adjoint $\langle \Phi \vert$ we get the current density expectation value:

$$
j_{i,i+1} = \frac{eiua^2}{\hbar} \left(\Phi_i^{\ast} \frac{\partial \Phi_i}{\partial x} - \frac{\partial \Phi_i^{\ast}}{\partial x} \Phi_i \right) \quad (1.58)
$$

by use of the assumption that $\partial \Phi_i/\partial x \approx \Phi_{i+1} - \Phi_i / a$. Further we use the dispersion relation $E_k = -2u + 2u \cos(ka) \approx -uk^2a^2$ as $ka \ll 1$, then from the definition $E_k = \hbar^2 k^2 / 2m$ we get an expression for $u$; $u \approx -\hbar^2/2ma^2$. This yields

$$
\tilde{j}_{i,i+1} = -\frac{i\hbar}{2m} \left(\Phi_i^{\ast} \frac{\partial \Phi_i}{\partial x} - \frac{\partial \Phi_i^{\ast}}{\partial x} \Phi_i \right), \quad (1.59)
$$

in agreement with the continuum expression 1.54.

## 1.6 1D $\rightarrow$ 3D, single band $\rightarrow$ multiple band.

In the previous sections I have presented theory that is valid only for one dimension and for structures with one band only. For generalizing to three dimensions and multiple bands we have to consider several aspects. They are treated in the following subsections.

### 1.6.1 The crystal lattice.

We have various types of semiconductors:
*   “III – V” semiconductors. GaAs, InAs, GaP..., Ga$_x$In$_{1-x}$As...
*   “II – VI” semiconductors. (CdTe), (HgTe), ZnSe, ZnTe...
*   “IV” semiconductors (C), Si, Ge, Sn...

All these semiconductors have the zincblende structure. The primitive lattice vectors for this sort of structure:

$$
\vec{A}1 = \frac{a}{2}(1,1,0)
$$

$$
\vec{A}2 = \frac{a}{2}(1,0,1)
$$

$$
\vec{A}3 = \frac{a}{2}(0,1,1) \quad (1.60)
$$

19
<!-- SLUTT SIDE 13 -->

<!-- START SIDE 14 -->
The reciprocal unit vectors:

$$
\begin{aligned}
\vec{a}_1 &= \frac{2\pi}{a} (1, 1, -1) \\
\vec{a}_2 &= \frac{2\pi}{a} (-1, 1, 1) \\
\vec{a}_3 &= \frac{2\pi}{a} (1, 1, 1).
\end{aligned}
$$

(1.61)

Here we have $\mathbf{a}_{i} \cdot \mathbf{A}_{j} = 2\pi\delta_{i j}$, where $\delta_{i j}$ has the value 1 for $i$ and $j$ equal and zero otherwise.
In the first Brillouin zone we have $\vec{k} = 2\pi/a*(u1, u2, u3)$ where $u1 + u2 + u3$ is less than or equal to 3/2. If we define the transport direction in the semiconductor structure as the [1,0,0] direction, we get the following four parallel vectors: Two for each kind of atomic layer, (that is; cation or anion), set up by the vectors from one atom to its closest neighbour in each of the two independent directions in the layers orthogonal to the current direction:

$$
\begin{aligned}
\vec{R}_0 &= \frac{a}{2}(j, j + 2l) & \text{connected to anion layers} \\
\vec{R}_1 &= \frac{a}{2}(j + \frac{1}{2}, j + 2l + \frac{1}{2}) & \text{connected to cation layers} \\
\vec{R}_2 &= \frac{a}{2}(j + 1, j + 2l) & \text{connected to anion layers; and} \\
\vec{R}_3 &= \frac{a}{2}(j + \frac{3}{2}, j + 2l + \frac{1}{2}) & \text{connected to cation layers} .
\end{aligned}
$$

(1.62)
In short, we got expressions for the four independent vectors in the two different kinds of layers orthogonal to the current direction.

### 1.6.2 Basis for eigenfunctions

From the one-dimensional case we had a state vector $\vert j \rangle$ with properties $\sum_j \vert j \rangle \langle j \vert = 1$ and $\langle j \vert i \rangle = \delta_{ij}$. The state vector in the 3-D multiband system is written such that one gets information on what lattice point the vector element is related to; that is where it is in the structure, about the kind of layer involved; anion or cation and what kind of orbital it is related to. The notation might look like this: $\vert n, b, \vec{R}_j \rangle$. Here $n$ gives information about the kind of orbital: $s, px, py, pz$ or $s^{\ast}$, $b$ might be either cation or anion and $\vec{R}_j$ is the position in the lattice. These state vectors have the same properties as the $\vert j \rangle$ from the 1-D single band version: $\langle n', b', \vec{R}_j' \vert n, b, \vec{R}_j \rangle$ is one for $n' = n$, $b' = b$ and $\vec{R}_j' = \vec{R}_j$ and it is zero otherwise. $\sum_{n,b,j} \vert n, b, \vec{R}_j \rangle \langle n, b, \vec{R}_j \vert = 1$.

### 1.6.3 The Hamiltonian.

The Hamiltonian for the 1-D single band system is written

$$
H = \sum_j \vert j \rangle \epsilon_0 \langle j \vert + \vert j \rangle u \langle j \pm 1 \vert.
$$

(1.63)
In the $sp^3s^{\ast}$ model, see article [1], we have 13 independent matrix elements:

20
<!-- SLUTT SIDE 14 -->

<!-- START SIDE 15 -->

$$
\begin{aligned}
E(s,a) &= \langle s, a, \tilde{R} | H | s, a, \tilde{R} \rangle \\
E(p,a) &= \langle p, a, \tilde{R} | H | p, a, \tilde{R} \rangle \\
E(s^{\ast},a) &= \langle s^{\ast}, a, \tilde{R} | H | s^{\ast}, a, \tilde{R} \rangle \\
E(s,c) &= \langle s, c, \tilde{R} | H | s, c, \tilde{R} \rangle \\
E(p,c) &= \langle p, c, \tilde{R} | H | p, c, \tilde{R} \rangle \\
E(s^{\ast},c) &= \langle s^{\ast}, c, \tilde{R} | H | s^{\ast}, c, \tilde{R} \rangle \\
V(s,s) &= 4 \langle s, a, \tilde{R} | H | s, c, \tilde{R} \rangle \\
V(px,px) &= 4 \langle px, a, \tilde{R} | H | px, c, \tilde{R} \rangle \\
V(px,py) &= 4 \langle px, a, \tilde{R} | H | py, c, \tilde{R} \rangle \\
V(sa,pxc) &= 4 \langle s, a, \tilde{R} | H | px, c, \tilde{R} \rangle \\
V(pxa,sc) &= 4 \langle px, a, \tilde{R} | H | s, c, \tilde{R} \rangle \\
V(s^{\ast}a,pxc) &= 4 \langle s^{\ast}, a, \tilde{R} | H | px, c, \tilde{R} \rangle \\
V(pxa,s^{\ast}c) &= 4 \langle px, a, \tilde{R} | H | s^{\ast}, c, \tilde{R} \rangle \qquad (1.64)
\end{aligned}
$$

Here $s$, $p$ and $s^{\ast}$ refers to orbitals in the materials. $s^{\ast}$ is a virtual orbital that has $s$ symmetry, and that is meant to cover for the effects of the orbitals in the actual materials with energy higher than the energy of the first set of $p$ orbitals. $px$ and $py$ are related to the orientation of the actual $p$ orbital.

The symbols $a$ and $c$ in equation 1.64 refer to whether the actual lattice point we deal with is an anion or a cation in the structure. For example, in InAs, In is the cation material and As is the anion material.

The feature $\tilde{R}$ is of course the position vector in the lattice.

As only nearest neighbours are interacting, the $sp^3s^{\ast}$ model then has a Hamiltonian as follows:

$$
H = \sum_{n,b,i} |n, b, \tilde{R}_i \rangle E(n,b) \langle n, b, \tilde{R}_i| + \sum_{n,b,j=i+\frac{a}{4}(1,1,1)} |n, b, \tilde{R}_i \rangle V \langle n, b, \tilde{R}_j| \qquad (1.65)
$$

1.7 The scattering problem.

Referring to figure 1.2, we have a structure with a potential barrier that starts after lattice point zero and ends after lattice point $N$. For such a structure we can separate the state vector into a contribution from the unperturbed incoming electron wave and a perturbation contribution due to the potential barrier.

where

$$
|\Psi \rangle = |S_\alpha \rangle + |\phi \rangle \qquad (1.66)
$$

$$
|S_\alpha \rangle = \sum_{j \le 0,b} \exp \left( ik_\alpha j \frac{a}{2} \right) |j, \alpha \rangle \qquad (1.67)
$$

that is, the sum over all atomic layers before the potential barrier. If the sequence of anions and cations is anion-cation as one enters the barrier from the left hand side, the first atomic layer in the half-infinite structure will be the cation layer for lattice point minus infinity, and the last atomic layer before entering the structure is the anion layer for lattice point number

21
<!-- SLUTT SIDE 15 -->

<!-- START SIDE 16 -->
minus one. So the integer value of $j$ is the number of the lattice point, and the state $|j, \alpha \rangle$ is the state of ion type $b$ at lattice point $j$. The exponential factor has the periodicity of the lattice, that is, we have a Bloch state in the area in front of the barrier for the unperturbed wave. The $10 \times 1$ vector $|j, \alpha \rangle$ has elements as follows:

$$
|j, \alpha \rangle =
\begin{pmatrix}
\alpha_{s,c} \\
\alpha_{px,c} \\
\alpha_{py,c} \\
\alpha_{pz,c} \\
\alpha_{s^{\ast},c} \\
\alpha_{s,a} \\
\alpha_{px,a} \\
\alpha_{py,a} \\
\alpha_{pz,a} \\
\alpha_{s^{\ast},a}
\end{pmatrix}
$$

. (1.68)

The $10 \times 10$ Hamiltonian consists of elements coupling equal orbitals on the diagonal and elements coupling anion and cation layers off the diagonal. For a given $E$ and parallel component of the momentum; that is, component orthogonal to the current direction, the solution of the Schrödinger equation gives $10$ possible $k_\alpha$ with their eigenfunctions $|\alpha \rangle$. For a given momentum one gets as solution of the Schrödinger equation the real band structure, that is $10$ possible energy eigenvalues with belonging eigenfunctions. The determinant of the energy minus the Hamiltonian is zero. The eigenfunctions $|\alpha \rangle$ might for example be;

$$
|s \rangle =
\begin{pmatrix}
1 \\
0 \\
0 \\
0 \\
0 \\
0 \\
0 \\
0 \\
0 \\
0
\end{pmatrix}
$$

.

or;

$$
|py \rangle =
\begin{pmatrix}
0 \\
0 \\
1 \\
0 \\
0 \\
0 \\
0 \\
0 \\
0 \\
0
\end{pmatrix}
$$

.
<!-- SLUTT SIDE 16 -->

<!-- START SIDE 17 -->
The contribution due to the potential barrier $|\phi\\rangle$ is given by means of the Green function, the energy, the Hamiltonian and the unperturbed state vector $|S_\alpha\\rangle.$

$$
\begin{aligned}
|\phi\\rangle = G^R[-(E-H)|S_\alpha\\rangle]. \quad (1.69)
\end{aligned}
$$

If the barrier is in the 0-th lattice point, then the perturbed contribution can be written

$$
\begin{aligned}
|\phi\\rangle = G^R[U_{a,c}|0, c, \alpha \\rangle - U_{c,\alpha}|0, a, \alpha \\rangle] \\ = \frac{4\pi i}{a} G^R \hat{v}|0, \alpha \\rangle. \quad (1.70)
\end{aligned}
$$

Have I mentioned that I have changed the name of the hopping matrix? The name is now depending on from what kind of atomic layer the electron is hopping from and it is also depending on what kind of atomic layer the electron is hopping to. The names I will use are as follows: For hopping between different monolayers I use $V_{c,\alpha}$ for hopping from an anion layer and $V_{a,c}$ for hopping from a cation layer. For hopping between atomic layers at one and the same lattice point, or monolayer, I use $U_{a,c}$ for hopping from an anion and $U_{c,\alpha}$ for hopping to a cation. As my model is a nearest neighbour model it should be obvious to what layer the electron is hopping in every case. In equation 1.70 the velocity operator is equal to;

$$
\hat{v} = \frac{a}{4\hbar} \begin{bmatrix} 0 & iU_{c,\alpha} \\ -iU_{a,c} & 0 \end{bmatrix}. \quad (1.71)
$$

The state vector $|0, \alpha \\rangle$ is a vector consisting of two elements; one for the anion layer and one for the cation layer:

$$
|0, \alpha \\rangle = \begin{pmatrix} |0, c, \alpha \\rangle \\ |0, a, \alpha \\rangle \end{pmatrix}.
$$

From earlier we know that

$$
\hat{v} = -\frac{i}{\hbar}[\hat{x}, H]. \quad (1.72)
$$

The position operator is given from

$$
\begin{aligned}
\hat{x} = \sum_j (|j,c\\rangle \frac{ja}{2} \\langle j,c| + |j,a\\rangle [\frac{ja}{2} + \frac{a}{4}] \\langle j,a|). \quad (1.73)
\end{aligned}
$$

and it has the property

$$
\begin{aligned}
\\langle i, c|\hat{x}|j, c \\rangle = \frac{ja}{2}\delta_{ij}. \quad (1.74)
\end{aligned}
$$

and so on.

Next let us discuss scattering amplitudes. We start by writing the state vector $|\Psi \\rangle$ in terms of the features found above:

$$
\begin{aligned}
|\Psi \\rangle = \sum_{j \le 0} [\exp (ik_\alpha \frac{j a}{2}) |j, \alpha \\rangle + \sum_\beta \sqrt{\frac{v_\alpha}{v_\beta}} r_{\alpha\beta} \exp (-ik_\beta \frac{j a}{2}) |j, \beta \\rangle] \\ + \sum_{1 \le j \le N} \sum_k X_{\alpha jk} |j, k \\rangle \\ + \sum_{j \ge N+1} \sum_\beta \sqrt{\frac{v_\alpha}{v_\beta}} t_{\alpha\beta} \exp (ik_\beta \frac{j a}{2}) |j, \beta \\rangle. \quad (1.75)
\end{aligned}
$$

23
<!-- SLUTT SIDE 17 -->

<!-- START SIDE 18 -->
As the incoming current density must be equal to the outgoing current density one can write

$$
|v_{\text{in}}||\Psi_{\text{in}}|^2 = \sum_{\text{ut}} |v_{\text{out}}||\Psi_{\text{out}}|^2
$$

This leads to an equation for $v_\alpha$:

$$
v_\alpha = \sum_{\beta} [|v_\beta|v_\beta|r_{\alpha\beta}|^2 + |v_\beta|v_\beta|t_{\alpha\beta}|^2]
$$

$$
= v_\alpha \sum_{\beta} [|r_{\alpha\beta}|^2 + |t_{\alpha\beta}|^2]
$$

We now have two different ways to express the scattering; one where the wave function is written as a sum over the three different areas in the structure, 1.75, and one where the scattered contributions are represented as a perturbation to the incoming wave, 1.66. Through multiplying 1.75 from left with the feature $\{N+1, \beta|$, (whose properties will be explained later,) we obtain the following expression for the transmission coefficient:

$$
t_{\alpha\beta} = \sqrt{\frac{v_\beta}{v_\alpha}} \exp\left(-ik_\beta(N+1)\frac{a}{2}\right) \frac{4i\hbar}{a} \langle N+1, \beta|G^R\hat{v}|0, \alpha \rangle
$$

The feature $\{N+1, \beta|$ is a row vector like $\langle N+1, \beta|$ with slightly different properties. That is, $\{N+1, \beta|\Psi \rangle \neq \langle N+1, \beta|\Psi \rangle$, but $\{j, \beta|$ is orthonormal to $|i, \alpha \rangle$. We further get for the reflection coefficient, by multiplying 1.75 with $\{0, \beta|$ from the left;

$$
r_{\alpha\beta} = \sqrt{\frac{v_\beta}{v_\alpha}} \frac{4i\hbar}{a} \langle 0, \beta|G^R\hat{v}|0, \alpha \rangle - \delta_{\alpha\beta} \langle 0, \alpha|\hat{v}|0, \alpha \rangle
$$

To specify the properties of the feature $\{N+1, \beta|$ and to avoid confusion about which bases are orthogonal to each other I summarize the properties of the three different bases that are involved in a set of equations:

$$
\langle j, \alpha|j, \beta \rangle \neq \delta_{\alpha\beta}
$$

$$
|\Psi_\beta \rangle = \sum_{-\infty \leq j \leq \infty} \exp\left(ik_\beta j\frac{a}{2}\right) |j, \beta \rangle
$$

$$
\langle \Psi_\alpha | \Psi_\beta \rangle = \delta[\alpha - \beta]
$$

$$
\{j, \alpha|j, \beta \rangle = \delta_{\alpha\beta}
$$

If we think of a $10 \times 10$ matrix $B$, then the column vectors can be thought of as the ket $|j, \beta \rangle$. Then the inverted matrix $B^{-1}$ is a matrix with row vectors $\{j, \beta|$, so that; $\{\beta|\alpha \rangle = \delta_{\beta\alpha}$. We conclude:

$$
\sum_\beta |\beta \rangle \{\beta| = \sum_\beta |\beta \rangle \langle \beta| = 1
$$

and
<!-- SLUTT SIDE 18 -->

<!-- START SIDE 19 -->

$$
\hat{v}|\alpha\rangle = \sum_\beta |\beta\rangle \langle\beta|\hat{v}|\alpha\rangle = v_\alpha|\alpha\rangle \quad (1.85)
$$

since $\langle\beta|\hat{v}|\alpha\rangle$ is equal to $v_\alpha\delta_{\alpha\beta}$.

## 1.8 Complex band structure.
For a given $E$ and $k$-parallel, we want to find the solution of the time independent Schrödinger equation $(E - H)|\alpha\rangle = 0$ and find $k_\alpha$ and $|\alpha\rangle$ for $\alpha$ between 1 and 10, that is find the complex band structure. We define the operator $Y$ as follows:

$$
\Psi_{i+1} = Y\Psi_i \quad (1.86)
$$

Here

$$
\begin{aligned}
\langle i+1|\Psi \rangle \equiv \Psi_{i+1} \\ = \sum_\alpha \langle i+1|\alpha \rangle \langle\alpha|\Psi \rangle \\ = Y \sum_\alpha \langle i|\alpha \rangle \langle\alpha|\Psi \rangle \\ = Y\Psi_i. \quad (1.87)
\end{aligned}
$$

This leads to

$$
\sum_\alpha \alpha_{i+1} \Psi_\alpha = \sum_\alpha Y \alpha_i \Psi_\alpha \quad (1.88)
$$

It is then easy to see that

$$
\alpha_{i+1} = Y\alpha_i \quad (1.89)
$$

Since $\alpha$ is a Bloch wave we can write

$$
\alpha_{i+1} = \exp\left(ik_\alpha \frac{a}{2}\right)\alpha_i \quad (1.90)
$$

and this shows that the operator $Y$ can be associated with $\exp\left(ik_\alpha \frac{a}{2}\right)$, and we can write

$$
Y\alpha_i = \exp\left(ik_\alpha \frac{a}{2}\right)\alpha_i \quad (1.91)
$$

Repeating:

$$
\Psi_{i+1} = Y\Psi_i
$$

<!-- SLUTT SIDE 19 -->

<!-- START SIDE 20 -->

$$
\Psi_{i+1} = \begin{pmatrix}
i+1, c, s \\
i+1, c, px \\
i+1, c, py \\
i+1, c, pz \\
i+1, c, s^{\ast} \\
i+1, a, s \\
i+1, a, px \\
i+1, a, py \\
i+1, a, pz \\
i+1, a, s^{\ast}
\end{pmatrix}
$$

We write the state vector above as

$$
\Psi_{i-1} = \begin{pmatrix}
i+1, c \\
i+1, a
\end{pmatrix},
$$

where the first component represents the five components dealing with the cation layers and the last component represents the five components dealing with anion layers. We can then express the operator $Y$ by means of two components $T1$ and $T2$:

$$
\begin{pmatrix}
i+1, c \\
i+1, a
\end{pmatrix} = T_2 \begin{pmatrix}
i, a \\
i+1, c
\end{pmatrix} = T_2 T_1 \begin{pmatrix}
i, c \\
i, a
\end{pmatrix} = Y \begin{pmatrix}
i, c \\
i, a
\end{pmatrix}. \quad (1.92)
$$

Next we look at the Schrödinger equation. We know that $E\vert i, a \rangle$ might be written

$$
E\vert i, a \rangle = E_a \vert i, a \rangle + U_{a,c} \vert i, c \rangle + V_{a,c} \vert i+1, c \rangle. \quad (1.93)
$$

We can then write the time independent Schrödinger equation as

$$
E\vert \Psi \rangle = H\vert \Psi \rangle
$$

$$
= [\vert i, a \rangle E_a \langle i, a \vert + \vert i, a \rangle U_{a,c} \langle i, c \vert + \vert i, a \rangle V_{a,c} \langle i+1, c \vert + ..]\vert \Psi \rangle. \quad (1.94)
$$

$$
\langle i, a \vert E \vert \Psi \rangle = \langle i, a \vert \left[ \quad \right] \vert \Psi \rangle
$$

$$
= \langle i, a \vert \left[ \quad \right] \sum_{j,b'} \vert j, b' \rangle
$$

$$
= \delta_{i,j} \delta_{b,b'}. \quad (1.95)
$$

where $[\quad]$ contains the same as in 1.94 and $b$ or $b'$ takes the value $c$ for cation and $a$ for anion.
Since

$$
E\vert i, a \rangle = E_a \vert i, a \rangle + U_{a,c} \vert i, c \rangle + V_{a,c} \vert i+1, c \rangle \quad \text{and}
$$

$$
E\vert i+1, c \rangle = E_c \vert i+1, c \rangle + U_{c,a} \vert i+1, a \rangle + V_{c,a} \vert i, a \rangle
$$

26
<!-- SLUTT SIDE 20 -->

<!-- START SIDE 21 -->
then

$$
|i+1, c\rangle = -V_{a,c}^{-1}U_{a,c}|i, c\rangle + V_{a,c}^{-1}(E-Ea)|i, a\rangle
$$

and

$$
|i+1, a\rangle = -U_{c,\alpha}^{-1}V_{c,\alpha}|i, a\rangle + U_{c,\alpha}^{-1}(E-Ec)|i+1, c\rangle
$$

which gives

$$
\begin{pmatrix} |i+1, c\rangle \\ |i, a\rangle \end{pmatrix} = \begin{bmatrix} 0 & 1 \\ A & B \end{bmatrix} \begin{pmatrix} |i, c\rangle \\ |i, a\rangle \end{pmatrix} = T1 \begin{pmatrix} |i, c\rangle \\ |i, a\rangle \end{pmatrix} \quad (1.96)
$$

and

$$
\begin{pmatrix} |i+1, c\rangle \\ |i+1, a\rangle \end{pmatrix} = \begin{bmatrix} 0 & 1 \\ C & D \end{bmatrix} \begin{pmatrix} |i, a\rangle \\ |i+1, c\rangle \end{pmatrix} = T2 \begin{pmatrix} |i, a\rangle \\ |i+1, c\rangle \end{pmatrix} \quad (1.97)
$$

Here

$$
\begin{aligned}
A &= -V_{a,c}^{-1}U_{a,c} \\
B &= V_{a,c}^{-1}(E-Ea) \\
C &= -U_{c,\alpha}^{-1}V_{c,\alpha} \quad \text{and} \\
D &= U_{c,\alpha}^{-1}(E-Ec)
\end{aligned}
\quad (1.98)
$$

This gives the expression for Y:

$$
Y = T2T1 = \begin{bmatrix} A & B \\ DA & C+DB \end{bmatrix} \quad (1.99)
$$

The eigenvalues of this operator (Y) is given from the equation

$$
Y|\alpha\rangle = y_{\alpha} |\alpha\rangle \quad (1.100)
$$

where

$$
y_{\alpha} = \exp(ik_{\alpha}\frac{a}{2}) \quad (1.101)
$$

These eigenvalues leads to the following conclusions:

$$
\begin{aligned}
& |y_{\alpha}| = 1 \text{ ;the values of } k_{\alpha} \text{ are real.} \\
& |y_{\alpha}| < 1 \text{ ;the imaginary part of } k_{\alpha} \text{ is greater than 0} \\
& |y_{\alpha}| > 1 \text{ ;the imaginary part of } k_{\alpha} \text{ is less than}
\end{aligned}
\quad (1.102)
$$

We have four different sorts of $k_{\alpha}$:
*   Real $k_{\alpha}$ with $v_{\alpha} = \frac{1}{\hbar}\frac{\partial E}{\partial k_{\alpha}} > 0$.
*   Real $k_{\alpha}$ with $v_{\alpha} = \frac{1}{\hbar}\frac{\partial E}{\partial k_{\alpha}} < 0$.
*   Complex $k_{\alpha}$ with $\text{Im}[k_{\alpha}] > 0$.
*   Complex $k_{\alpha}$ with $\text{Im}[k_{\alpha}] < 0$.

27
<!-- SLUTT SIDE 21 -->

<!-- START SIDE 22 -->
1.9 Surface Green functions.

In our system with a general potential barrier which is illustrated in figure 2 with discrete coordinates, we may write the wave function as 1.66. It is then possible to write the perturbation $\phi$ of the wavefunction due to the potential barrier as follows, see also equation 1.69:

$$
\vert \phi \rangle = G^{\text{R}}[-(E-H)\vert S_{\alpha} \rangle] = G^{\text{R}} \vert i_0 \rangle \qquad (1.103)
$$

here $G^{\text{R}}$ is the Green function for the homogenous unperturbed right contact. It doesn't really matter whether it is the right or left contact, as long as it is homogenous. When this is multiplied with $\langle i + 2 \vert$ and $\langle i + 1 \vert$ from left we obtain the two equations written below:

$$
\begin{aligned}
\langle i + 2 \vert \phi \rangle = \langle i + 2 \vert G^{\text{R}} \vert i_0 \rangle = \langle i + 2 \vert [G^0 + G^0VG^{\text{R}}] \vert i_0 \rangle \\
\langle i + 1 \vert \phi \rangle = \langle i + 1 \vert G^{\text{R}} \vert i_0 \rangle \qquad (1.104)
\end{aligned}
$$

Through further calculations we obtain for $\langle i + 2 \vert \phi \rangle$:

$$
\begin{aligned}
\langle i + 2 \vert \phi \rangle = \langle i + 2 \vert G^0 \vert i + 2 \rangle V_{i+2,i+1} \langle i + 1 \vert G^{\text{R}} \vert i_0 \rangle \\
= \Gamma_{i+2} + V_{i+2,i+1} \langle i + 1 \vert \phi \rangle \qquad (1.105)
\end{aligned}
$$

This gives that

$$
\phi_{i+2} = \Gamma_{i+2} + V_{i+2,i+1}\phi_{i+1} \qquad (1.105)
$$

Here $V$ is a general hopping matrix connecting neighbor lattice points. We may also write

$$
\vert \alpha_a^+ \rangle = \Gamma_a^+ U_{a,c} \vert \alpha_c^+ \rangle \qquad (1.106)
$$

Here $\vert \alpha^+ \rangle$ is a state vector with 10 components, 5 for each kind of atomic layer; anion and cation. If we introduce a matrix $A^+$ for each kind of atomic layer with one column for each state vector $\vert \alpha \rangle$ (that is, with elements equal to the elements of the state vector), where each state vector represents one of five orbitals, we get an expression for the surface Green functions:

$$
A_a^+ = \Gamma_a^+ U_{a,c} A_c^+ \qquad (1.107)
$$

Follows from 1.106. Thus

$$
\begin{aligned}
\Gamma_a^+ = A_a^+ \frac{1}{A_c} \frac{1}{U_{c,a}} \\
\Gamma_c^+ = \frac{1}{E-E_c-U_{c,a}(\Gamma_a^+)U_{a,c}} \qquad (1.108)
\end{aligned}
$$

Analogously,

$$
A_c^- = (\Gamma_c^-) U_{c,a} A_a^- \qquad (1.109)
$$

$$
\begin{aligned}
\Gamma_c^- = A_c^- \frac{1}{A_a^-} \frac{1}{U_{c,a}} \\
\Gamma_a^+ = \frac{1}{E-E_a-U_{a,c}(\Gamma_c^-)U_{c,a}} \qquad (1.110)
\end{aligned}
$$

28
<!-- SLUTT SIDE 22 -->

<!-- START SIDE 23 -->
We can then write for the various possible surface Green functions:

$$
\Gamma_{c,1}^{+} = \frac{1}{E-E_{c,1}-V_{c,a}(\Gamma_{a,0}^{-})V_{a,c}}
$$

$$
\Gamma_{a,1}^{+} = \frac{1}{E-E_{a,1}-U_{a,c}(\Gamma_{c,1}^{-})U_{c,a}}
$$

.
.
.

$$
\Gamma_{a,N}^{+} = \frac{1}{E-E_{a,N}-V_{a,c}(\Gamma_{c,N-1}^{+})V_{c,a}} \quad \text{(1.111)}
$$

$$
\Gamma_{c,N}^{+} = \frac{1}{E-E_{c,N}-U_{c,a}(\Gamma_{a,N}^{+})U_{a,c}}
$$

.
.
.

1.10 Alloys and interfaces.

For a structure where the two materials A and B are the cation materials with concentration $x$ and $1-x$, and a third material C is the anion material, we use the virtual crystal approximation (VCA) which tells us that

$$
H[A_x B_{1-x} C] = xH[AC] + (1-x)H[BC] \quad \text{(1.112)}
$$

Across interfaces where the material is different on each side of the surface, we use the average energy for the surface layer:

$$
E_a[interface] = \frac{1}{2}(E_a[AC] + E_a[BC]) \quad \text{(1.113)}
$$

29
<!-- SLUTT SIDE 23 -->
