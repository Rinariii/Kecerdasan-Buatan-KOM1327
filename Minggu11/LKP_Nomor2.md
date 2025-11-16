# Jawaban LKP 11
## 2.  Jika diketahui bahwa pasien mengalami Chest Pain, berapa peluang pasien melakukan Exercise?

![Gambar Bayesian Network](Bayesian.png)

Misalkan Chest Pain = CP , Heart Disease = HD, Exercise = E, Diet = D, Heart Burn = HB.

Maka untuk mencari peluang `P(E|CP)` dapat menggunakan rumus : 

$$
P(E \mid CP) = \frac{P(CP \mid E)\cdot P(E)}{P(CP)}
$$

Sehingga kita akan mencari variabel yang diperlukan yakni

$$
\begin{aligned}
P(CP \mid E) = &P(CP \mid HD,HB)\cdot P(HD \mid E,D)\cdot P(HB \mid D)\cdot P(D) \\
&+ P(CP \mid HD,\neg HB)\cdot P(HD \mid E,D)\cdot P(\neg HB \mid D)\cdot P(D) \\
&+ P(CP \mid \neg HD,HB)\cdot P(\neg HD \mid E,D)\cdot P(HB \mid D)\cdot P(D) \\
&+ P(CP \mid \neg HD,\neg HB)\cdot P(\neg HD \mid E,D)\cdot P(\neg HB \mid D)\cdot P(D) \\
&+ P(CP \mid HD,HB)\cdot P(HD \mid E,\neg D)\cdot P(HB \mid \neg D)\cdot P(\neg D) \\
&+ P(CP \mid HD,\neg HB)\cdot P(HD \mid E,\neg D)\cdot P(\neg HB \mid \neg D)\cdot P(\neg D) \\
&+ P(CP \mid \neg HD,HB)\cdot P(\neg HD \mid E,\neg D)\cdot P(HB \mid \neg D)\cdot P(\neg D) \\
&+ P(CP \mid \neg HD,\neg HB)\cdot P(\neg HD \mid E,\neg D)\cdot P(\neg HB \mid \neg D)\cdot P(\neg D)
\end{aligned}
$$

$$
\begin{aligned}
P(CP \mid \neg E) = &P(CP \mid HD,HB)\cdot P(HD \mid \neg E,D)\cdot P(HB \mid D)\cdot P(D) \\
&+ P(CP \mid HD,\neg HB)\cdot P(HD \mid \neg E,D)\cdot P(\neg HB \mid D)\cdot P(D) \\
&+ P(CP \mid \neg HD,HB)\cdot P(\neg HD \mid \neg E,D)\cdot P(HB \mid D)\cdot P(D) \\
&+ P(CP \mid \neg HD,\neg HB)\cdot P(\neg HD \mid \neg E,D)\cdot P(\neg HB \mid D)\cdot P(D) \\
&+ P(CP \mid HD,HB)\cdot P(HD \mid \neg E,\neg D)\cdot P(HB \mid \neg D)\cdot P(\neg D) \\
&+ P(CP \mid HD,\neg HB)\cdot P(HD \mid \neg E,\neg D)\cdot P(\neg HB \mid \neg D)\cdot P(\neg D) \\
&+ P(CP \mid \neg HD,HB)\cdot P(\neg HD \mid \neg E,\neg D)\cdot P(HB \mid \neg D)\cdot P(\neg D) \\
&+ P(CP \mid \neg HD,\neg HB)\cdot P(\neg HD \mid \neg E,\neg D)\cdot P(\neg HB \mid \neg D)\cdot P(\neg D)
\end{aligned}
$$

$$
P(CP) = P(CP|E) \cdot P(E) + P(CP|\neg E) \cdot P(\neg E)
$$

Dari gambar bayesian network diatas kita dapat mengetahui bahwa:

| Variabel        | Nilai |
|-----------------|-------|
| $P(E)$          | 0.7   |
| $P(\neg E)$     | 0.3   |
| $P(D)$          | 0.25  |
| $P(\neg D)$     | 0.75  |
| $P(CP \mid HB,HD)$   |0.8    |
| $P(\neg CP \mid HB,HD)$ | 0.2|
| $P(CP \mid \neg HB,HD)$| 0.6|
| $P(\neg CP \mid \neg HB,HD)$ | 0.4|
| $P(CP \mid HB,\neg HD)$ | 0.4|
| $P(\neg CP \mid HB,\neg HD)$ | 0.6|
| $P(CP \mid \neg HB,\neg HD)$ | 0.1|
| $P(\neg CP \mid \neg HB,\neg HD)$ | 0.9|
| $P(HD \mid E,D)$   |0.25    |
| $P(\neg HD \mid E,D)$ | 0.75|
| $P(HD \mid E,\neg D)$| 0.45|
| $P(\neg HD \mid E,\neg D)$ | 0.55|
| $P(HD \mid \neg E,D)$ | 0.55|
| $P(\neg HD \mid \neg E,D)$ | 0.45|
| $P(HD \mid \neg E,\neg D)$ | 0.75|
| $P(\neg HD \mid \neg E,\neg D)$ | 0.25|
| $P(HB \mid D)$ | 0.2|
| $P(\neg HB \mid D)$ | 0.8|
| $P(HB \mid \neg D)$ | 0.85|
| $P(\neg HB \mid \neg D)$ | 0.15|

Sehingga didapatkan hasil

$$
\begin{aligned}
P(CP \mid E) =&0.8 \cdot 0.25 \cdot 0.2 \cdot 0.25 + 0.4 \cdot 0.75 \cdot 0.2 \cdot 0.25 \\
&+ 0.6 \cdot 0.25 \cdot 0.8 \cdot 0.25 + 0.1 \cdot 0.75 \cdot 0.8 \cdot 0.25 \\
&+ 0.8 \cdot 0.45 \cdot 0.85 \cdot 0.75 + 0.4 \cdot 0.55 \cdot 0.85 \cdot 0.75 \\
&+ 0.6 \cdot 0.45 \cdot 0.15 \cdot 0.75 + 0.1 \cdot 0.55 \cdot 0.15 \cdot 0.75 \\
\end{aligned}
$$

Maka 

$$
P(CP|E)= 0.0100 + 0.0150 + 0.0300 + 0.0150 + 0.2295 + 0.14025 + 0.030375 + 0.0061875
$$


$$
P(CP|E) = 0.4763
$$

Untuk P(CP|¬E)

$$
\begin{aligned}
P(CP \mid \neg E) = &0.8 \cdot 0.55 \cdot 0.2 \cdot 0.25 + 0.4 \cdot 0.45 \cdot 0.2 \cdot 0.25 \\
&+ 0.6 \cdot 0.55 \cdot 0.8 \cdot 0.25 + 0.1 \cdot 0.45 \cdot 0.8 \cdot 0.25 \\
&+ 0.8 \cdot 0.75 \cdot 0.85 \cdot 0.75 + 0.4 \cdot 0.25 \cdot 0.85 \cdot 0.75 \\
&+ 0.6 \cdot 0.75 \cdot 0.15 \cdot 0.75 + 0.1 \cdot 0.25 \cdot 0.15 \cdot 0.75 \\
\end{aligned}
$$

Maka 

$$
P(CP|\neg E)= 0.0220 + 0.0090 + 0.0660 + 0.0090 + 0.3825 + 0.06375 + 0.050625 + 0.0028125
$$


$$
P(CP|\neg E) = 0.6057
$$

Maka untuk menghitung P(CP)

$$
P(CP) = 0.4763 \cdot O.7 + 0.6057 \cdot 0.3 = 0.5151 
$$

Sehingga untuk menghitung `P(E|CP)`

$$
P(E \mid CP) = \frac{0.4763\cdot 0.7}{0.5151} = 0.6473
$$

Sehingga peluang bahwa pasien mengalami Chest Pain, dan peluang pasien melakukan Exercise adalah **0.6473**
