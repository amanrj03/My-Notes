# -*- coding: utf-8 -*-
import sys

new_content = r'''### Worked example: Find every prime up to 30

We want to systematically find all prime numbers up to \(N = 30\) using the **Sieve of Eratosthenes**.

#### Step 0: Determine the stopping bound
Before crossing out any numbers, we determine which primes we must sieve with by applying the square-root theorem:

\[ \sqrt{30} \approx 5.48 \implies \lfloor \sqrt{30} \rfloor = 5. \]

Every composite integer \(n \le 30\) must have at least one prime divisor \(p \le \sqrt{30}\). Therefore, we only need to sieve by the primes not exceeding \(5\):

\[ \boxed{p \in \{2, 3, 5\}}. \]

Testing \(p = 7\) is unnecessary because \(7 > \sqrt{30}\) (its first new composite multiple is \(7^2 = 49 > 30\)).

---

#### Step-by-step sieving procedure

<div class="sieve-steps">

<div class="sieve-step-card">
<div class="sieve-step-title"><span>🔢 Step 1:</span> Sieve with prime \(p = 2\)</div>
<p>Keep <strong>2</strong> as prime. Cross out all multiples of \(2\) greater than \(2\) (starting at \(2^2 = 4\)):</p>
<p><strong>Multiples eliminated (14 numbers):</strong></p>
<div class="math-display">\[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30\]</div>
<p><em>Remaining uncrossed candidates:</em> \(2\text{ (prime)}, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29\).</p>
</div>

<div class="sieve-step-card">
<div class="sieve-step-title"><span>🔢 Step 2:</span> Sieve with prime \(p = 3\)</div>
<p>The next uncrossed number is <strong>3</strong>. Keep <strong>3</strong> as prime.</p>
<p>Cross out its remaining multiples greater than \(3\). We begin at \(3^2 = 9\) because \(3 \times 2 = 6\) was already eliminated in Step 1.</p>
<p><strong>New multiples eliminated (4 numbers):</strong></p>
<div class="math-display">\[9, 15, 21, 27\]</div>
<p><em>(Note: \(6, 12, 18, 24, 30\) were already crossed out by \(2\).)</em></p>
<p><em>Remaining uncrossed candidates:</em> \(2, 3\text{ (primes)}, 5, 7, 11, 13, 17, 19, 23, 25, 29\).</p>
</div>

<div class="sieve-step-card">
<div class="sieve-step-title"><span>🔢 Step 3:</span> Sieve with prime \(p = 5\)</div>
<p>The next uncrossed number is <strong>5</strong>. Keep <strong>5</strong> as prime.</p>
<p>Cross out its remaining multiples greater than \(5\). We begin at \(5^2 = 25\) because \(5 \times 2 = 10\), \(5 \times 3 = 15\), and \(5 \times 4 = 20\) were already eliminated by \(2\) or \(3\).</p>
<p><strong>New multiple eliminated (1 number):</strong></p>
<div class="math-display">\[25\]</div>
<p><em>(Note: \(10, 15, 20, 30\) were already eliminated earlier.)</em></p>
<p><em>Remaining uncrossed candidates:</em> \(2, 3, 5\text{ (primes)}, 7, 11, 13, 17, 19, 23, 29\).</p>
</div>

<div class="sieve-step-card">
<div class="sieve-step-title"><span>🛑 Step 4:</span> Stopping check at \(p = 7\)</div>
<p>The next uncrossed number is <strong>7</strong>.</p>
<p>Because \(7 > \sqrt{30} \approx 5.48\) and \(7^2 = 49 > 30\), all remaining uncrossed integers have no proper prime factors \(\le \sqrt{30}\). By the square-root theorem, <strong>every remaining uncrossed integer must be prime</strong>.</p>
<p><strong>The algorithm terminates immediately!</strong></p>
</div>

</div>

---

#### Visual Sieve Board (Integers 2 to 30)

<div class="sieve-board">
    <div class="sieve-legend">
        <span class="sieve-legend-item"><span class="sieve-badge prime">&#10003; Prime</span> Prime (Kept)</span>
        <span class="sieve-legend-item"><span class="sieve-badge elim-2">&times; 2</span> Crossed by 2</span>
        <span class="sieve-legend-item"><span class="sieve-badge elim-3">&times; 3</span> Crossed by 3</span>
        <span class="sieve-legend-item"><span class="sieve-badge elim-5">&times; 5</span> Crossed by 5</span>
    </div>
    <div class="sieve-grid">
        <div class="sieve-num prime">2 <span class="sieve-sub">Prime</span></div>
        <div class="sieve-num prime">3 <span class="sieve-sub">Prime</span></div>
        <div class="sieve-num elim-2">4 <span class="sieve-sub">&times; 2</span></div>
        <div class="sieve-num prime">5 <span class="sieve-sub">Prime</span></div>
        <div class="sieve-num elim-2">6 <span class="sieve-sub">&times; 2</span></div>
        <div class="sieve-num prime">7 <span class="sieve-sub">Prime</span></div>
        <div class="sieve-num elim-2">8 <span class="sieve-sub">&times; 2</span></div>
        <div class="sieve-num elim-3">9 <span class="sieve-sub">&times; 3</span></div>
        <div class="sieve-num elim-2">10 <span class="sieve-sub">&times; 2</span></div>
        <div class="sieve-num prime">11 <span class="sieve-sub">Prime</span></div>
        <div class="sieve-num elim-2">12 <span class="sieve-sub">&times; 2</span></div>
        <div class="sieve-num prime">13 <span class="sieve-sub">Prime</span></div>
        <div class="sieve-num elim-2">14 <span class="sieve-sub">&times; 2</span></div>
        <div class="sieve-num elim-3">15 <span class="sieve-sub">&times; 3</span></div>
        <div class="sieve-num elim-2">16 <span class="sieve-sub">&times; 2</span></div>
        <div class="sieve-num prime">17 <span class="sieve-sub">Prime</span></div>
        <div class="sieve-num elim-2">18 <span class="sieve-sub">&times; 2</span></div>
        <div class="sieve-num prime">19 <span class="sieve-sub">Prime</span></div>
        <div class="sieve-num elim-2">20 <span class="sieve-sub">&times; 2</span></div>
        <div class="sieve-num elim-3">21 <span class="sieve-sub">&times; 3</span></div>
        <div class="sieve-num elim-2">22 <span class="sieve-sub">&times; 2</span></div>
        <div class="sieve-num prime">23 <span class="sieve-sub">Prime</span></div>
        <div class="sieve-num elim-2">24 <span class="sieve-sub">&times; 2</span></div>
        <div class="sieve-num elim-5">25 <span class="sieve-sub">&times; 5</span></div>
        <div class="sieve-num elim-2">26 <span class="sieve-sub">&times; 2</span></div>
        <div class="sieve-num elim-3">27 <span class="sieve-sub">&times; 3</span></div>
        <div class="sieve-num elim-2">28 <span class="sieve-sub">&times; 2</span></div>
        <div class="sieve-num prime">29 <span class="sieve-sub">Prime</span></div>
        <div class="sieve-num elim-2">30 <span class="sieve-sub">&times; 2</span></div>
    </div>
</div>

#### Summary table of elimination passes

| Sieving Prime \(p\) | Starting Multiple (\(p^2\)) | Multiples Eliminated in this Step | New Eliminations | Remaining Candidates |
| :---: | :---: | :--- | :---: | :---: |
| **Initial list** | — | None (integers \(2\) through \(30\)) | 0 | 29 |
| **\(p = 2\)** | \(4\) | \(4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30\) | 14 | 15 |
| **\(p = 3\)** | \(9\) | \(9, 15, 21, 27\) | 4 | 11 |
| **\(p = 5\)** | \(25\) | \(25\) | 1 | 10 |
| **\(p = 7\)** | \(49\) | \(49 > 30 \implies\) **Algorithm terminates** | 0 | **10 primes** |

#### Final Result

The prime numbers not exceeding \(30\) are:

\[ \boxed{2,\ 3,\ 5,\ 7,\ 11,\ 13,\ 17,\ 19,\ 23,\ 29}. \]

The total prime count is \(\pi(30) = 10\).

> **High-yield exam takeaway:**
> Notice that we only needed **three elimination passes** (primes \(2, 3, 5\)) to find every prime up to 30. All other 7 primes (\(7, 11, 13, 17, 19, 23, 29\)) were certified prime without ever performing trial division on them!

'''

path = r'd:/Blockchain HTML/Django HTML/raw_notes/NumberTheory&Cryptography/8.txt'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

start_pos = text.find('### Worked example: Find every prime up to')
pos = text.find('### Why can we start crossing out multiples at')

if start_pos == -1 or pos == -1:
    print('Error: Could not locate markers!')
    sys.exit(1)

updated_text = text[:start_pos] + new_content + text[pos:]
with open(path, 'w', encoding='utf-8') as f:
    f.write(updated_text)

print('Successfully updated 8.txt!')
