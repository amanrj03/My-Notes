# Define and append step-wise, line-by-line exam question cards to render_maths_diagrams_unit4_5.py

STEPWISE_CARDS = '''

def card_mod26_exam_questions():
    return \'\'\'
    <div class="math-diagram-box">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
            <h4 class="math-diagram-title" style="margin: 0;">Exam-Style Questions (Step-by-Step &amp; Line-by-Line Solutions)</h4>
            <span class="callout-badge" style="background: rgba(124, 58, 237, 0.12); color: #7c3aed; font-weight: 700; padding: 4px 10px; border-radius: 6px; font-size: 11px;">SOLVED IN DETAIL</span>
        </div>
        <p style="font-size: 13.5px; color: var(--text-secondary); margin: 0 0 16px;">
            Every single step and mathematical equation is formatted line-by-line for effortless reading, maximum clarity, and instant exam recall.
        </p>

        <!-- Q1: MCQ 1 Mark -->
        <div style="background: rgba(37, 99, 235, 0.04); border: 1.5px solid rgba(37, 99, 235, 0.25); border-radius: 10px; padding: 18px; margin-bottom: 18px;">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 8px;">
                <strong style="color: #2563eb; font-size: 15px;">Q1. (MCQ &mdash; 1 Mark)</strong>
                <span style="font-size: 11px; background: rgba(37, 99, 235, 0.12); color: #2563eb; padding: 3px 8px; border-radius: 4px; font-weight: 700;">Totient Calculation</span>
            </div>
            <p style="font-size: 13.5px; font-weight: 600; color: var(--text-heading); margin: 0 0 10px;">
                If \\(n = 77\\), what is \\(\\phi(n)\\)?
            </p>
            <div style="display: flex; flex-direction: column; gap: 6px; margin-bottom: 12px;">
                <div style="padding: 7px 12px; background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 6px; font-size: 13px;">
                    <strong>A)</strong> 76
                </div>
                <div style="padding: 7px 12px; background: rgba(16, 185, 129, 0.08); border: 1.5px solid #10b981; border-radius: 6px; font-size: 13px; font-weight: 700; color: #059669;">
                    <strong>B)</strong> 60 &check; (Correct Option)
                </div>
                <div style="padding: 7px 12px; background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 6px; font-size: 13px;">
                    <strong>C)</strong> 70
                </div>
                <div style="padding: 7px 12px; background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 6px; font-size: 13px;">
                    <strong>D)</strong> 66
                </div>
            </div>
            <div style="padding: 10px 14px; background: rgba(16, 185, 129, 0.08); border-radius: 6px; font-size: 12.5px; line-height: 1.7; color: var(--text-body);">
                <strong>Step-by-Step Derivation:</strong><br>
                &bull; Step 1: Factor \\(77\\) into prime factors: \\(77 = 7 \\times 11\\)<br>
                &bull; Step 2: Apply Euler\'s product formula for distinct primes: \\(\\phi(n) = (p-1)(q-1)\\)<br>
                &bull; Step 3: Compute: \\(\\phi(77) = (7-1)(11-1) = 6 \\times 10 = \\mathbf{60}\\)<br>
                <span style="font-weight: 800; color: #059669;">&rArr; Answer: B</span>
            </div>
        </div>

        <!-- Q2: Solving 5 Marks -->
        <div style="background: rgba(124, 58, 237, 0.04); border: 1.5px solid rgba(124, 58, 237, 0.25); border-radius: 10px; padding: 18px; margin-bottom: 18px;">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 8px;">
                <strong style="color: #7c3aed; font-size: 15px;">Q2. (Solving &mdash; 5 Marks)</strong>
                <span style="font-size: 11px; background: rgba(124, 58, 237, 0.12); color: #7c3aed; padding: 3px 8px; border-radius: 4px; font-weight: 700;">Extended Euclidean Algorithm</span>
            </div>
            <p style="font-size: 13.5px; font-weight: 600; color: var(--text-heading); margin: 0 0 12px;">
                Find the modular inverse of \\(13 \\pmod{42}\\) using the Extended Euclidean Algorithm.
            </p>
            <div style="font-size: 13px; line-height: 1.7; color: var(--text-body);">
                <div style="margin-bottom: 10px; padding: 10px 14px; background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 6px;">
                    <strong style="color: #7c3aed;">Step 1: Forward Euclidean Divisions on 42 and 13:</strong><br>
                    1. \\(42 = 3 \\times 13 + 3\\) &nbsp; &bull; &nbsp; (Remainder = 3)<br>
                    2. \\(13 = 4 \\times 3 + 1\\) &nbsp; &bull; &nbsp; (Remainder = 1)<br>
                    3. \\(3 = 3 \\times 1 + 0\\) &nbsp; &bull; &nbsp; (Remainder = 0 &rarr; \\(\\gcd(42, 13) = 1\\), so inverse exists)
                </div>
                <div style="margin-bottom: 10px; padding: 10px 14px; background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 6px;">
                    <strong style="color: #7c3aed;">Step 2: Backward Substitution (Isolate Remainder 1):</strong><br>
                    &bull; From division 2: \\(1 = 13 - 4 \\times 3\\)<br>
                    &bull; Substitute \\(3 = 42 - 3 \\times 13\\) from division 1:<br>
                    &nbsp;&nbsp; \\(1 = 13 - 4 \\times (42 - 3 \\times 13)\\)<br>
                    &nbsp;&nbsp; \\(1 = 13 - 4 \\times 42 + 12 \\times 13\\)<br>
                    &nbsp;&nbsp; \\(1 = 13 \\times 13 - 4 \\times 42\\)
                </div>
                <div style="padding: 10px 14px; background: rgba(16, 185, 129, 0.08); border: 1px solid #10b981; border-radius: 6px;">
                    <strong style="color: #059669;">Step 3: Read Coefficient Modulo 42:</strong><br>
                    Reducing modulo 42 eliminates the multiple of 42:<br>
                    \\(13 \\times 13 \\equiv 1 \\pmod{42}\\)<br>
                    <span style="font-weight: 800; color: #059669; font-size: 13.5px;">&rArr; The modular inverse of \\(13 \\pmod{42}\\) is \\(\\mathbf{13}\\).</span><br>
                    <span style="font-size: 12px; color: var(--text-secondary);">Check: \\(13 \\times 13 = 169 = 4 \\times 42 + 1 \\equiv 1 \\pmod{42}\\). (Exact match!)</span>
                </div>
            </div>
        </div>

        <!-- Q3: Solving 4 Marks -->
        <div style="background: rgba(245, 158, 11, 0.04); border: 1.5px solid rgba(245, 158, 11, 0.25); border-radius: 10px; padding: 18px;">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 8px;">
                <strong style="color: #d97706; font-size: 15px;">Q3. (Solving &mdash; 4 Marks)</strong>
                <span style="font-size: 11px; background: rgba(245, 158, 11, 0.12); color: #d97706; padding: 3px 8px; border-radius: 4px; font-weight: 700;">FLT &amp; Exponentiation</span>
            </div>
            <p style="font-size: 13.5px; font-weight: 600; color: var(--text-heading); margin: 0 0 12px;">
                Calculate \\(3^{17} \\bmod 5\\) using Fermat\'s Little Theorem and modular exponentiation.
            </p>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; font-size: 12.5px;">
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 12px 14px; line-height: 1.7;">
                    <strong style="color: #d97706;">Method 1: Fermat\'s Little Theorem (Fastest)</strong><br>
                    &bull; Since \\(p = 5\\) is prime and \\(\\gcd(3, 5) = 1\\):<br>
                    &nbsp;&nbsp; \\(3^{5-1} = 3^4 \\equiv 1 \\pmod 5\\)<br>
                    &bull; Decompose exponent \\(17\\): \\(17 = 4 \\times 4 + 1\\)<br>
                    &bull; Substitute:<br>
                    &nbsp;&nbsp; \\(3^{17} = (3^4)^4 \\times 3^1 \\equiv 1^4 \\times 3 \\equiv \\mathbf{3} \\pmod 5\\)
                </div>
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 12px 14px; line-height: 1.7;">
                    <strong style="color: #d97706;">Method 2: Binary Exponentiation (Step-by-Step)</strong><br>
                    &bull; Binary for 17: \\(17 = 16 + 1\\)<br>
                    &bull; \\(3^1 = 3\\)<br>
                    &bull; \\(3^2 = 9 \\equiv 4 \\equiv -1 \\pmod 5\\)<br>
                    &bull; \\(3^4 = (-1)^2 = 1\\)<br>
                    &bull; \\(3^8 = 1^2 = 1\\)<br>
                    &bull; \\(3^{16} = 1^2 = 1\\)<br>
                    &bull; Product: \\(3^{17} = 3^{16} \\cdot 3^1 = 1 \\cdot 3 = \\mathbf{3} \\pmod 5\\)
                </div>
            </div>
            <div style="margin-top: 12px; padding: 8px 12px; background: rgba(16, 185, 129, 0.1); border-radius: 6px; font-weight: 800; color: #059669; text-align: center; font-size: 13.5px;">
                &rArr; Final Answer: \\(3^{17} \\equiv 3 \\pmod 5\\) &check;
            </div>
        </div>
    </div>
    \'\'\'

def card_mod27_exam_questions():
    return \'\'\'
    <div class="math-diagram-box">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
            <h4 class="math-diagram-title" style="margin: 0;">3. Solved Exam Questions (Step-by-Step &amp; Line-by-Line)</h4>
            <span class="callout-badge" style="background: rgba(37, 99, 235, 0.12); color: #2563eb; font-weight: 700; padding: 4px 10px; border-radius: 6px; font-size: 11px;">EXAM MASTERY</span>
        </div>
        <p style="font-size: 13.5px; color: var(--text-secondary); margin: 0 0 16px;">
            Standard examination questions with clear line-by-line separation, equations, and full derivations:
        </p>

        <!-- Question 1: MCQ 1 Mark -->
        <div style="background: rgba(37, 99, 235, 0.04); border: 1.5px solid rgba(37, 99, 235, 0.25); border-radius: 10px; padding: 18px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 8px;">
                <strong style="color: #2563eb; font-size: 15px;">Question 1 (MCQ &mdash; 1 Mark)</strong>
                <span style="font-size: 11px; background: rgba(37, 99, 235, 0.12); color: #2563eb; padding: 3px 8px; border-radius: 4px; font-weight: 700;">Theory Concept</span>
            </div>
            <p style="font-size: 13.5px; font-weight: 600; color: var(--text-heading); margin: 0 0 12px;">
                In the Diffie-Hellman protocol, if Alice\'s private key is \\(a\\), Bob\'s private key is \\(b\\), and the public base is \\(g\\) modulo prime \\(p\\), what is the shared secret key?
            </p>

            <div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 12px;">
                <div style="padding: 8px 12px; background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 6px; font-size: 13px;">
                    <strong>A)</strong> \\(g^a + g^b \\pmod p\\)
                </div>
                <div style="padding: 8px 12px; background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 6px; font-size: 13px;">
                    <strong>B)</strong> \\(g^{a+b} \\pmod p\\)
                </div>
                <div style="padding: 8px 12px; background: rgba(16, 185, 129, 0.08); border: 1.5px solid #10b981; border-radius: 6px; font-size: 13px; font-weight: 700; color: #059669;">
                    <strong>C)</strong> \\(g^{ab} \\pmod p\\) &check; (Correct Option)
                </div>
                <div style="padding: 8px 12px; background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 6px; font-size: 13px;">
                    <strong>D)</strong> \\(a \\cdot b \\pmod p\\)
                </div>
            </div>

            <div style="padding: 10px 14px; background: rgba(16, 185, 129, 0.08); border-radius: 6px; font-size: 12.5px; line-height: 1.6; color: var(--text-body);">
                <strong>Answer: C</strong><br>
                <em>Mathematical Reason:</em> Alice raises Bob\'s public value \\(B = g^b\\) to her private secret \\(a\\): \\(K = (g^b)^a = g^{ab} \\pmod p\\). Bob raises Alice\'s public value \\(A = g^a\\) to his private secret \\(b\\): \\(K = (g^a)^b = g^{ab} \\pmod p\\). Both arrive at the identical key \\(g^{ab} \\pmod p\\).
            </div>
        </div>

        <!-- Question 2: Numerical 5 Marks -->
        <div style="background: rgba(124, 58, 237, 0.04); border: 1.5px solid rgba(124, 58, 237, 0.25); border-radius: 10px; padding: 18px;">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 8px;">
                <strong style="color: #7c3aed; font-size: 15px;">Question 2 (Numerical &mdash; 5 Marks): Diffie-Hellman Calculation Walkthrough</strong>
                <span style="font-size: 11px; background: rgba(124, 58, 237, 0.12); color: #7c3aed; padding: 3px 8px; border-radius: 4px; font-weight: 700;">5-MARK SOLVED QUESTION</span>
            </div>
            <p style="font-size: 13.5px; color: var(--text-body); margin: 0 0 14px;">
                Alice and Bob use the Diffie-Hellman key exchange with prime \\(p = 23\\) and base generator \\(g = 5\\).<br>
                &bull; Alice chooses private key \\(a = 6\\).<br>
                &bull; Bob chooses private key \\(b = 15\\).<br>
                <strong>Goal:</strong> Find the public keys exchanged and the shared secret key.
            </p>

            <!-- Line-by-line Steps -->
            <div style="display: flex; flex-direction: column; gap: 14px;">
                <!-- Step 1: Alice Public Key -->
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                        <span style="background: #7c3aed; color: #fff; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 11px;">1</span>
                        <strong style="color: #7c3aed; font-size: 14px;">Step 1: Alice\'s Public Key (\(A\))</strong>
                    </div>
                    <div style="font-size: 13px; line-height: 1.8; color: var(--text-body);">
                        Formula: \\(A = g^a \\pmod p = 5^6 \\pmod{23}\\)<br>
                        &bull; Line 1: \\(5^2 = 25 \\equiv 2 \\pmod{23}\\)<br>
                        &bull; Line 2: \\(5^4 = 2^2 = 4 \\pmod{23}\\)<br>
                        &bull; Line 3: \\(5^6 = 5^4 \\cdot 5^2 = 4 \\cdot 2 = \\mathbf{8} \\pmod{23}\\)<br>
                        <span style="font-weight: 800; color: #7c3aed;">&rArr; Alice\'s Public Key: \\(A = 8\\)</span>
                    </div>
                </div>

                <!-- Step 2: Bob Public Key -->
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                        <span style="background: #059669; color: #fff; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 11px;">2</span>
                        <strong style="color: #059669; font-size: 14px;">Step 2: Bob\'s Public Key (\(B\))</strong>
                    </div>
                    <div style="font-size: 13px; line-height: 1.8; color: var(--text-body);">
                        Formula: \\(B = g^b \\pmod p = 5^{15} \\pmod{23}\\)<br>
                        &bull; Line 1: Binary decomposition: \\(15 = 8 + 4 + 2 + 1\\)<br>
                        &bull; Line 2: Successive powers modulo 23:<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;\\(5^1 = 5\\)<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;\\(5^2 = 25 \\equiv 2\\)<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;\\(5^4 = 2^2 = 4\\)<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;\\(5^8 = 4^2 = 16\\)<br>
                        &bull; Line 3: Multiply active terms:<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;\\(5^{15} = 5^8 \\cdot 5^4 \\cdot 5^2 \\cdot 5^1 = 16 \\cdot 4 \\cdot 2 \\cdot 5 = 640 \\pmod{23}\\)<br>
                        &bull; Line 4: Divide: \\(23 \\times 27 = 621 \\implies 640 - 621 = \\mathbf{19}\\)<br>
                        <span style="font-weight: 800; color: #059669;">&rArr; Bob\'s Public Key: \\(B = 19\\)</span>
                    </div>
                </div>

                <!-- Step 3: Shared Key Alice -->
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                        <span style="background: #7c3aed; color: #fff; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 11px;">3</span>
                        <strong style="color: #7c3aed; font-size: 14px;">Step 3: Shared Secret Key (Alice Computes)</strong>
                    </div>
                    <div style="font-size: 13px; line-height: 1.8; color: var(--text-body);">
                        Formula: \\(K = B^a \\pmod p = 19^6 \\pmod{23}\\)<br>
                        &bull; Line 1: Use negative residue to simplify: \\(19 \\equiv -4 \\pmod{23}\\)<br>
                        &bull; Line 2: \\((-4)^6 = 4^6 = (4^3)^2 = 64^2\\)<br>
                        &bull; Line 3: Reduce 64: \\(64 = 2(23) + 18 \\equiv 18 \\pmod{23}\\)<br>
                        &bull; Line 4: Square 18: \\(18^2 = 324\\)<br>
                        &bull; Line 5: Reduce 324: \\(23 \\times 14 = 322 \\implies 324 - 322 = \\mathbf{2}\\)<br>
                        <span style="font-weight: 800; color: #7c3aed;">&rArr; Alice computes: \\(K = 2\\)</span>
                    </div>
                </div>

                <!-- Step 4: Bob Verification -->
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                        <span style="background: #059669; color: #fff; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 11px;">4</span>
                        <strong style="color: #059669; font-size: 14px;">Step 4: Check / Verification (Bob Computes)</strong>
                    </div>
                    <div style="font-size: 13px; line-height: 1.8; color: var(--text-body);">
                        Formula: \\(K = A^b \\pmod p = 8^{15} \\pmod{23}\\)<br>
                        &bull; Line 1: Since \\(8 = 2^3\\), rewrite: \\(8^{15} = (2^3)^{15} = 2^{45} \\pmod{23}\\)<br>
                        &bull; Line 2: By Fermat\'s Little Theorem (prime 23): \\(2^{22} \\equiv 1 \\pmod{23}\\)<br>
                        &bull; Line 3: Decompose exponent: \\(2^{45} = (2^{22})^2 \\cdot 2^1 \\equiv 1^2 \\cdot 2 = \\mathbf{2} \\pmod{23}\\)<br>
                        <span style="font-weight: 800; color: #059669;">&rArr; Bob computes: \\(K = 2\\)</span>
                    </div>
                </div>
            </div>

            <div style="margin-top: 14px; padding: 10px 16px; background: rgba(16, 185, 129, 0.1); border: 1px solid #10b981; border-radius: 8px; text-align: center; font-size: 13.5px; font-weight: 800; color: #059669;">
                &check; Mutual Verification Complete: \\(K_{Alice} = K_{Bob} = \\mathbf{2}\\). The Shared Secret Key is 2.
            </div>
        </div>
    </div>
    \'\'\'

def card_mod28_exam_questions():
    rsa_numerical_card = card_mod28_numerical_rsa_stop_help()
    return f\'\'\'
    <div class="math-diagram-box">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
            <h4 class="math-diagram-title" style="margin: 0;">📝 Solved Exam Questions (Step-by-Step &amp; Line-by-Line)</h4>
            <span class="callout-badge" style="background: rgba(124, 58, 237, 0.12); color: #7c3aed; font-weight: 700; padding: 4px 10px; border-radius: 6px; font-size: 11px;">RSA MASTER EXAM QUESTIONS</span>
        </div>
        <p style="font-size: 13.5px; color: var(--text-secondary); margin: 0 0 16px;">
            Step-by-step mathematical solutions for key generation, numerical encryption/decryption, and the theoretical proof of correctness:
        </p>

        <!-- Question 1: Key Generation 5 Marks -->
        <div style="background: rgba(37, 99, 235, 0.04); border: 1.5px solid rgba(37, 99, 235, 0.25); border-radius: 10px; padding: 18px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 8px;">
                <strong style="color: #2563eb; font-size: 15px;">Question 1 (Key Generation &mdash; 5 Marks)</strong>
                <span style="font-size: 11px; background: rgba(37, 99, 235, 0.12); color: #2563eb; padding: 3px 8px; border-radius: 4px; font-weight: 700;">Setup &amp; Derivation</span>
            </div>
            <p style="font-size: 13.5px; font-weight: 600; color: var(--text-heading); margin: 0 0 12px;">
                Let \\(p = 3\\) and \\(q = 11\\). Choose public exponent \\(e = 7\\). Find the public key, private key, and \\(\\phi(n)\\).
            </p>
            <div style="font-size: 13px; line-height: 1.8; color: var(--text-body);">
                &bull; <strong>Line 1 (Compute Modulus):</strong> \\(n = p \\times q = 3 \\times 11 = \\mathbf{33}\\)<br>
                &bull; <strong>Line 2 (Compute Totient):</strong> \\(\\phi(n) = (p-1)(q-1) = (3-1)(11-1) = 2 \\times 10 = \\mathbf{20}\\)<br>
                &bull; <strong>Line 3 (Check Coprimality):</strong> \\(\\gcd(e, \\phi(n)) = \\gcd(7, 20) = 1\\) &bull; Valid public exponent.<br>
                &bull; <strong>Line 4 (State Public Key):</strong> \\((n, e) = \\mathbf{(33, 7)}\\)<br>
                &bull; <strong>Line 5 (Solve for Private Exponent \(d\)):</strong> We require \\(e \\cdot d \\equiv 1 \\pmod{\\phi(n)}\\), meaning \\(7d \\equiv 1 \\pmod{20}\\).<br>
                &bull; <strong>Line 6 (Test Multiples):</strong> \\(7(3) = 21 = 20 + 1 \\equiv 1 \\pmod{20} \\implies \\mathbf{d = 3}\\)<br>
                <div style="margin-top: 10px; padding: 8px 12px; background: rgba(16, 185, 129, 0.08); border-radius: 6px; font-weight: 800; color: #059669;">
                    &rArr; Public Key = \\((33, 7)\\) &bull; Private Key = \\(d = 3\\) (or \\((33, 3)\\)) &bull; \\(\\phi(n) = 20\\)
                </div>
            </div>
        </div>

        <!-- Question 2: STOP / HELP 10 Marks -->
        {rsa_numerical_card}

        <!-- Question 3: Theoretical Proof 5 Marks -->
        <div style="background: rgba(245, 158, 11, 0.04); border: 1.5px solid rgba(245, 158, 11, 0.25); border-radius: 10px; padding: 18px; margin-top: 20px;">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 8px;">
                <strong style="color: #d97706; font-size: 15px;">Question 3 (Theoretical/Proof &mdash; 5 Marks)</strong>
                <span style="font-size: 11px; background: rgba(245, 158, 11, 0.12); color: #d97706; padding: 3px 8px; border-radius: 4px; font-weight: 700;">Mathematical Proof</span>
            </div>
            <p style="font-size: 13.5px; font-weight: 600; color: var(--text-heading); margin: 0 0 12px;">
                Why does RSA Decryption work? Prove that \\((M^e)^d \\equiv M \\pmod n\\).
            </p>
            <div style="font-size: 13px; line-height: 1.8; color: var(--text-body);">
                &bull; <strong>Step 1 (Inverse Definition):</strong> By definition of private key, \\(e \\cdot d \\equiv 1 \\pmod{\\phi(n)}\\). Therefore, there exists an integer \\(k\\) such that:<br>
                <span style="display: block; text-align: center; margin: 4px 0; font-weight: 700;">\\(ed = 1 + k(p-1)(q-1)\\)</span>
                &bull; <strong>Step 2 (Power Expansion):</strong> Applying this to ciphertext decryption:<br>
                <span style="display: block; text-align: center; margin: 4px 0; font-weight: 700;">\\(C^d \\equiv (M^e)^d = M^{ed} = M^{1 + k(p-1)(q-1)} = M \\cdot \\left(M^{p-1}\\right)^{k(q-1)} \\pmod n\\)</span>
                &bull; <strong>Step 3 (Modulo \(p\) via Fermat\'s Little Theorem):</strong> Since \\(p\\) is prime, \\(M^{p-1} \\equiv 1 \\pmod p\\). Thus:<br>
                <span style="display: block; text-align: center; margin: 4px 0; font-weight: 700; color: #7c3aed;">\\(C^d \\equiv M \\cdot (1)^{k(q-1)} \\equiv M \\pmod p\\)</span>
                &bull; <strong>Step 4 (Modulo \(q\) via Fermat\'s Little Theorem):</strong> Similarly, since \\(q\\) is prime, \\(M^{q-1} \\equiv 1 \\pmod q\\). Thus:<br>
                <span style="display: block; text-align: center; margin: 4px 0; font-weight: 700; color: #7c3aed;">\\(C^d \\equiv M \\cdot (1)^{k(p-1)} \\equiv M \\pmod q\\)</span>
                &bull; <strong>Step 5 (Chinese Remainder Theorem):</strong> Since \\(p\\) and \\(q\\) are distinct primes (coprime), if an equation holds modulo \\(p\\) and modulo \\(q\\), it holds modulo \\(p \\times q = n\\):<br>
                <span style="display: block; text-align: center; margin: 6px 0; font-weight: 800; color: #059669; font-size: 14px;">\\(C^d \\equiv M \\pmod n \\implies M = C^d \\bmod n\\)</span>
                <div style="text-align: right; font-weight: 800; color: #059669; margin-top: 4px;">Q.E.D. &check;</div>
            </div>
        </div>
    </div>
    \'\'\'

def card_mod29_exam_questions():
    return \'\'\'
    <div class="math-diagram-box">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
            <h4 class="math-diagram-title" style="margin: 0;">📝 Solved Exam Questions for ElGamal (Step-by-Step &amp; Line-by-Line)</h4>
            <span class="callout-badge" style="background: rgba(37, 99, 235, 0.12); color: #2563eb; font-weight: 700; padding: 4px 10px; border-radius: 6px; font-size: 11px;">5-MARK SOLVED EXAM QUESTION</span>
        </div>
        <p style="font-size: 13.5px; color: var(--text-secondary); margin: 0 0 16px;">
            Complete line-by-line solution for ElGamal parameter setup, encryption, and decryption:
        </p>

        <!-- Question 1: Numerical 5 Marks -->
        <div style="background: rgba(37, 99, 235, 0.04); border: 1.5px solid rgba(37, 99, 235, 0.25); border-radius: 10px; padding: 18px;">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 8px;">
                <strong style="color: #2563eb; font-size: 15px;">Question 1 (Numerical &mdash; 5 Marks)</strong>
                <span style="font-size: 11px; background: rgba(37, 99, 235, 0.12); color: #2563eb; padding: 3px 8px; border-radius: 4px; font-weight: 700;">Parameters: \(p = 23, g = 5, x = 6\)</span>
            </div>
            <p style="font-size: 13.5px; color: var(--text-body); margin: 0 0 14px;">
                Given prime \\(p = 23\\) and generator \\(g = 5\\). Bob chooses private key \\(x = 6\\).<br>
                (a) Find Bob\'s public key \\(y\\).<br>
                (b) Alice encrypts message \\(M = 10\\) using random key \\(k = 3\\). Find ciphertext \\((C_1, C_2)\\).<br>
                (c) Show how Bob decrypts it.
            </p>

            <div style="display: flex; flex-direction: column; gap: 14px;">
                <!-- Part (a) -->
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                    <div style="font-weight: 700; color: #2563eb; font-size: 14px; margin-bottom: 6px;">
                        (a) Bob\'s Public Key (\(y\))
                    </div>
                    <div style="font-size: 13px; line-height: 1.8; color: var(--text-body);">
                        &bull; Formula: \\(y = g^x \\bmod p = 5^6 \\bmod 23\\)<br>
                        &bull; Line 1: \\(5^2 = 25 \\equiv 2 \\pmod{23}\\)<br>
                        &bull; Line 2: \\(5^4 = 2^2 = 4 \\pmod{23}\\)<br>
                        &bull; Line 3: \\(5^6 = 5^4 \\cdot 5^2 = 4 \\cdot 2 = \\mathbf{8} \\pmod{23}\\)<br>
                        <span style="font-weight: 800; color: #2563eb;">&rArr; Bob\'s Public Key: \\((p=23, g=5, y=8)\\)</span>
                    </div>
                </div>

                <!-- Part (b) -->
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                    <div style="font-weight: 700; color: #2563eb; font-size: 14px; margin-bottom: 6px;">
                        (b) Alice Encrypts \(M = 10\) with \(k = 3\)
                    </div>
                    <div style="font-size: 13px; line-height: 1.8; color: var(--text-body);">
                        &bull; Compute \\(C_1\\): \\(C_1 = g^k \\bmod p = 5^3 \\bmod 23 = 125 \\bmod 23\\)<br>
                        &nbsp;&nbsp; Division: \\(23 \\times 5 = 115 \\implies 125 - 115 = \\mathbf{10} \\implies C_1 = 10\\)<br>
                        &bull; Compute \\(C_2\\): \\(C_2 = (M \\cdot y^k) \\bmod p = (10 \\cdot 8^3) \\bmod 23\\)<br>
                        &nbsp;&nbsp; Line 1: \\(8^3 = 512\\)<br>
                        &nbsp;&nbsp; Line 2: \\(23 \\times 22 = 506 \\implies 512 - 506 = 6 \\implies 8^3 \\equiv 6 \\pmod{23}\\)<br>
                        &nbsp;&nbsp; Line 3: \\(C_2 = (10 \\cdot 6) = 60 \\bmod 23\\)<br>
                        &nbsp;&nbsp; Line 4: \\(23 \\times 2 = 46 \\implies 60 - 46 = \\mathbf{14} \\implies C_2 = 14\\)<br>
                        <span style="font-weight: 800; color: #2563eb;">&rArr; Transmitted Ciphertext Pair: \\((C_1, C_2) = (10, 14)\\)</span>
                    </div>
                </div>

                <!-- Part (c) -->
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                    <div style="font-weight: 700; color: #059669; font-size: 14px; margin-bottom: 6px;">
                        (c) Bob Decrypts with Private Key \(x = 6\)
                    </div>
                    <div style="font-size: 13px; line-height: 1.8; color: var(--text-body);">
                        &bull; Line 1 (Compute Shared Secret): \\(S = C_1^x \\bmod p = 10^6 \\bmod 23\\)<br>
                        &nbsp;&nbsp; \\(10^2 = 100 \\equiv 8 \\pmod{23}\\)<br>
                        &nbsp;&nbsp; \\(10^4 = 8^2 = 64 \\equiv 18 \\pmod{23}\\)<br>
                        &nbsp;&nbsp; \\(10^6 = 18 \\cdot 8 = 144 = 23(6) + 6 \\equiv \\mathbf{6} \\implies S = 6\\)<br>
                        &bull; Line 2 (Find Modular Inverse \(S^{-1}\)): We solve \\(6z \\equiv 1 \\pmod{23}\\)<br>
                        &nbsp;&nbsp; \\(6 \\times 4 = 24 = 23 + 1 \\equiv 1 \\pmod{23} \\implies \\mathbf{S^{-1} = 4}\\)<br>
                        &bull; Line 3 (Recover Message): \\(M = (C_2 \\cdot S^{-1}) \\bmod p = (14 \\cdot 4) \\bmod 23 = 56 \\bmod 23\\)<br>
                        &nbsp;&nbsp; \\(23 \\times 2 = 46 \\implies 56 - 46 = \\mathbf{10}\\)<br>
                        <span style="font-weight: 800; color: #059669;">&rArr; Decrypted Message: \\(M = 10\\) &check; (Perfect Match!)</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    \'\'\'
'''

with open('scratch/render_maths_diagrams_unit4_5.py', 'a', encoding='utf-8') as f:
    f.write(STEPWISE_CARDS)

print("Appended all 4 step-wise question cards to render_maths_diagrams_unit4_5.py!")
