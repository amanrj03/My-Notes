# -*- coding: utf-8 -*-
"""
Visual learning diagrams, concept cards, cipher wheels, matrix visualizers,
and step-by-step algorithm flowcharts for Mathematics Modules 18 to 29
(Unit IV: Classical Cryptography & Unit V: Public Key Cryptography).
"""

def card_mod18_communication_model():
    return '''
    <div class="math-diagram-box">
        <h4 class="math-diagram-title">Fundamental Cryptographic Communication Model</h4>
        <div style="display: grid; grid-template-columns: 1fr auto 1fr auto 1fr; align-items: center; gap: 12px; margin: 20px 0; text-align: center;">
            <div class="math-pill" style="border: 2px solid #7c3aed; background: rgba(124, 58, 237, 0.08);">
                <div style="font-weight: 800; color: #7c3aed; font-size: 16px;">Alice (Sender)</div>
                <div style="font-size: 12px; color: var(--text-secondary); margin-top: 4px;">Plaintext \\(P\\)</div>
                <div style="margin-top: 8px; font-size: 11.5px; background: #7c3aed; color: #fff; padding: 3px 8px; border-radius: 4px;">Encrypts: \\(C = E_K(P)\\)</div>
            </div>
            <div style="font-size: 20px; color: #a78bfa; font-weight: bold;">&rarr;</div>
            <div class="math-pill" style="border: 2px dashed #ef4444; background: rgba(239, 68, 68, 0.06); position: relative;">
                <div style="font-size: 11px; text-transform: uppercase; font-weight: 800; color: #ef4444; letter-spacing: 0.5px;">Insecure Public Channel</div>
                <div style="font-size: 15px; font-weight: 700; color: var(--text-heading); margin: 6px 0;">Ciphertext \\(C\\)</div>
                <div style="font-size: 11.5px; color: #f87171; border-top: 1px solid rgba(239,68,68,0.2); padding-top: 4px;">
                    👁️ Eve (Adversary Eavesdropping)
                </div>
            </div>
            <div style="font-size: 20px; color: #a78bfa; font-weight: bold;">&rarr;</div>
            <div class="math-pill" style="border: 2px solid #10b981; background: rgba(16, 185, 129, 0.08);">
                <div style="font-weight: 800; color: #10b981; font-size: 16px;">Bob (Receiver)</div>
                <div style="font-size: 12px; color: var(--text-secondary); margin-top: 4px;">Recovers \\(P\\)</div>
                <div style="margin-top: 8px; font-size: 11.5px; background: #10b981; color: #fff; padding: 3px 8px; border-radius: 4px;">Decrypts: \\(P = D_K(C)\\)</div>
            </div>
        </div>
        <div class="math-card-caption">
            <strong>Kerckhoffs's Principle:</strong> Security rests entirely in the secrecy of the key \\(K\\), not in the secrecy of the algorithm \\(E\\) or \\(D\\).
        </div>
    </div>
    '''

def card_mod18_kerckhoffs_principles():
    return '''
    <div class="math-callout theorem">
        <div class="callout-badge theorem">⚖️ AUGUSTE KERCKHOFFS'S FOUNDATIONAL MAXIM (1883)</div>
        <div class="callout-title">The Fundamental Axiom of Modern Cryptography</div>
        <p style="margin: 8px 0 0 0; font-style: italic; color: var(--text-body);">
            "A cryptosystem should be secure even if everything about the system, except the key, is public knowledge."
        </p>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; margin-top: 14px;">
            <div style="padding: 10px 14px; background: rgba(239, 68, 68, 0.06); border-left: 3px solid #ef4444; border-radius: 6px;">
                <strong style="color: #ef4444; font-size: 13px;">❌ Security by Obscurity</strong>
                <p style="font-size: 12px; margin: 4px 0 0; color: var(--text-secondary);">Hiding how the algorithm works. Once the algorithm leaks or is reverse-engineered, every encrypted message is permanently compromised.</p>
            </div>
            <div style="padding: 10px 14px; background: rgba(16, 185, 129, 0.06); border-left: 3px solid #10b981; border-radius: 6px;">
                <strong style="color: #10b981; font-size: 13px;">✅ Kerckhoffs-Compliant Security</strong>
                <p style="font-size: 12px; margin: 4px 0 0; color: var(--text-secondary);">The algorithm is completely open for global scrutiny, mathematical testing, and academic analysis. Security depends solely on the mathematical entropy of the secret key \\(K\\).</p>
            </div>
        </div>
    </div>
    '''

def card_mod19_frequency_table():
    return '''
    <div class="math-diagram-box">
        <h4 class="math-diagram-title">English Alphabet Frequency Analysis Spectrum</h4>
        <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 14px;">
            In English text, individual letters appear with non-uniform frequencies. Monoalphabetic substitution ciphers preserve these exact frequency proportions!
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(65px, 1fr)); gap: 8px; text-align: center;">
            <div style="background: rgba(124, 58, 237, 0.15); border: 1.5px solid #7c3aed; border-radius: 6px; padding: 8px 4px;">
                <div style="font-size: 16px; font-weight: 800; color: #7c3aed;">E</div>
                <div style="font-size: 12px; font-weight: 700; color: var(--text-heading);">12.7%</div>
                <div style="font-size: 10px; color: var(--text-muted);">Highest</div>
            </div>
            <div style="background: rgba(124, 58, 237, 0.12); border: 1.5px solid #8b5cf6; border-radius: 6px; padding: 8px 4px;">
                <div style="font-size: 16px; font-weight: 800; color: #8b5cf6;">T</div>
                <div style="font-size: 12px; font-weight: 700; color: var(--text-heading);">9.1%</div>
            </div>
            <div style="background: rgba(124, 58, 237, 0.1); border: 1px solid #a78bfa; border-radius: 6px; padding: 8px 4px;">
                <div style="font-size: 16px; font-weight: 800; color: #a78bfa;">A</div>
                <div style="font-size: 12px; font-weight: 700; color: var(--text-heading);">8.2%</div>
            </div>
            <div style="background: rgba(124, 58, 237, 0.1); border: 1px solid #a78bfa; border-radius: 6px; padding: 8px 4px;">
                <div style="font-size: 16px; font-weight: 800; color: #a78bfa;">O</div>
                <div style="font-size: 12px; font-weight: 700; color: var(--text-heading);">7.5%</div>
            </div>
            <div style="background: rgba(124, 58, 237, 0.08); border: 1px solid #cbd5e1; border-radius: 6px; padding: 8px 4px;">
                <div style="font-size: 16px; font-weight: 800; color: var(--text-heading);">I</div>
                <div style="font-size: 12px; font-weight: 700; color: var(--text-heading);">7.0%</div>
            </div>
            <div style="background: rgba(124, 58, 237, 0.08); border: 1px solid #cbd5e1; border-radius: 6px; padding: 8px 4px;">
                <div style="font-size: 16px; font-weight: 800; color: var(--text-heading);">N</div>
                <div style="font-size: 12px; font-weight: 700; color: var(--text-heading);">6.7%</div>
            </div>
            <div style="background: rgba(124, 58, 237, 0.06); border: 1px solid #cbd5e1; border-radius: 6px; padding: 8px 4px;">
                <div style="font-size: 16px; font-weight: 800; color: var(--text-heading);">S</div>
                <div style="font-size: 12px; font-weight: 700; color: var(--text-heading);">6.3%</div>
            </div>
            <div style="background: rgba(124, 58, 237, 0.06); border: 1px solid #cbd5e1; border-radius: 6px; padding: 8px 4px;">
                <div style="font-size: 16px; font-weight: 800; color: var(--text-heading);">H</div>
                <div style="font-size: 12px; font-weight: 700; color: var(--text-heading);">6.1%</div>
            </div>
            <div style="background: rgba(124, 58, 237, 0.04); border: 1px solid #cbd5e1; border-radius: 6px; padding: 8px 4px;">
                <div style="font-size: 16px; font-weight: 800; color: var(--text-heading);">R</div>
                <div style="font-size: 12px; font-weight: 700; color: var(--text-heading);">6.0%</div>
            </div>
            <div style="background: rgba(245, 158, 11, 0.08); border: 1px dashed #f59e0b; border-radius: 6px; padding: 8px 4px;">
                <div style="font-size: 16px; font-weight: 800; color: #d97706;">Q, Z</div>
                <div style="font-size: 12px; font-weight: 700; color: var(--text-heading);">&lt;0.1%</div>
                <div style="font-size: 10px; color: var(--text-muted);">Rarest</div>
            </div>
        </div>
        <div class="math-card-caption">
            <strong>Frequent Digrams:</strong> <code>TH</code>, <code>HE</code>, <code>IN</code>, <code>ER</code>, <code>AN</code> &bull; <strong>Frequent Trigrams:</strong> <code>THE</code>, <code>AND</code>, <code>ING</code>, <code>HER</code>.
        </div>
    </div>
    '''

def card_mod20_alphabet_ribbon():
    return '''
    <div class="math-diagram-box">
        <h4 class="math-diagram-title">Standard Alphabet-to-Number Residue Mapping \\(\\mathbb{Z}_{26}\\)</h4>
        <div style="overflow-x: auto; padding: 8px 0;">
            <table style="width: 100%; border-collapse: collapse; text-align: center; font-size: 12px;">
                <tr style="background: #7c3aed; color: #ffffff; font-weight: 800;">
                    <th style="padding: 6px 4px;">A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th><th>G</th><th>H</th><th>I</th><th>J</th><th>K</th><th>L</th><th>M</th><th>N</th><th>O</th><th>P</th><th>Q</th><th>R</th><th>S</th><th>T</th><th>U</th><th>V</th><th>W</th><th>X</th><th>Y</th><th>Z</th>
                </tr>
                <tr style="background: rgba(124, 58, 237, 0.08); font-weight: 700; color: var(--text-heading);">
                    <td style="padding: 6px 4px;">0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td>
                </tr>
            </table>
        </div>
        <div class="math-card-caption">
            <strong>Key Formula:</strong> \\(p \\leftrightarrow \\text{index}(p)\\) where \\(A=0\\) and \\(Z=25\\). In modular arithmetic, \\(26 \\equiv 0\\), \\(27 \\equiv 1\\), and \\(-1 \\equiv 25\\).
        </div>
    </div>
    '''

def card_mod20_caesar_wheel():
    return '''
    <div class="math-diagram-box">
        <h4 class="math-diagram-title">Caesar Shift Cipher (Key \\(k = 3\\)) Visual Alignment</h4>
        <div style="overflow-x: auto; padding: 6px 0;">
            <table style="width: 100%; border-collapse: collapse; text-align: center; font-size: 12.5px;">
                <tr style="background: rgba(59, 130, 246, 0.1); color: #2563eb; font-weight: 700;">
                    <td style="padding: 6px 4px; font-weight: 800; background: #2563eb; color: #fff;">Plain (p)</td>
                    <td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td>
                </tr>
                <tr style="color: var(--text-muted); font-size: 11px;">
                    <td style="padding: 2px;">Shift +3</td>
                    <td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td><td>&darr;</td>
                </tr>
                <tr style="background: rgba(16, 185, 129, 0.1); color: #059669; font-weight: 800;">
                    <td style="padding: 6px 4px; font-weight: 800; background: #059669; color: #fff;">Cipher (c)</td>
                    <td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td><td>A</td><td>B</td><td>C</td>
                </tr>
            </table>
        </div>
        <div style="display: flex; justify-content: space-around; margin-top: 14px; font-size: 13px;">
            <div class="math-pill"><strong>Encryption:</strong> \\(c \\equiv (p + 3) \\pmod{26}\\)</div>
            <div class="math-pill"><strong>Decryption:</strong> \\(p \\equiv (c - 3) \\pmod{26}\\)</div>
        </div>
    </div>
    '''

def card_mod21_affine_inverses():
    return '''
    <div class="math-diagram-box">
        <h4 class="math-diagram-title">Affine Cipher: All 12 Coprime Multipliers and Modular Inverses Modulo 26</h4>
        <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 12px;">
            For the affine function \\(f(p) = (ap + b) \\bmod 26\\) to be one-to-one (invertible), we require \\(\\gcd(a, 26) = 1\\). Since \\(26 = 2 \\times 13\\), \\(a\\) cannot be divisible by 2 or 13.
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px; text-align: center;">
            <div class="math-pill" style="border-color: #7c3aed;">\\(a = 1\\) &harr; \\(a^{-1} = 1\\)</div>
            <div class="math-pill" style="border-color: #7c3aed;">\\(a = 3\\) &harr; \\(a^{-1} = 9\\)</div>
            <div class="math-pill" style="border-color: #7c3aed;">\\(a = 5\\) &harr; \\(a^{-1} = 21\\)</div>
            <div class="math-pill" style="border-color: #7c3aed;">\\(a = 7\\) &harr; \\(a^{-1} = 15\\)</div>
            <div class="math-pill" style="border-color: #7c3aed;">\\(a = 9\\) &harr; \\(a^{-1} = 3\\)</div>
            <div class="math-pill" style="border-color: #7c3aed;">\\(a = 11\\) &harr; \\(a^{-1} = 19\\)</div>
            <div class="math-pill" style="border-color: #7c3aed;">\\(a = 15\\) &harr; \\(a^{-1} = 7\\)</div>
            <div class="math-pill" style="border-color: #7c3aed;">\\(a = 17\\) &harr; \\(a^{-1} = 23\\)</div>
            <div class="math-pill" style="border-color: #7c3aed;">\\(a = 19\\) &harr; \\(a^{-1} = 11\\)</div>
            <div class="math-pill" style="border-color: #7c3aed;">\\(a = 21\\) &harr; \\(a^{-1} = 5\\)</div>
            <div class="math-pill" style="border-color: #7c3aed;">\\(a = 23\\) &harr; \\(a^{-1} = 17\\)</div>
            <div class="math-pill" style="border-color: #7c3aed;">\\(a = 25\\) &harr; \\(a^{-1} = 25\\)</div>
        </div>
        <div class="math-card-caption">
            <strong>Total Keyspace:</strong> \\(\\phi(26) \\times 26 = 12 \\times 26 = 312\\) possible key pairs \\((a, b)\\).
        </div>
    </div>
    '''

def card_mod22_vigenere_alignment():
    return '''
    <div class="math-diagram-box">
        <h4 class="math-diagram-title">Vigenère Polyalphabetic Keyword Alignment &amp; Calculation</h4>
        <div style="background: rgba(124, 58, 237, 0.05); border: 1px solid rgba(124, 58, 237, 0.2); border-radius: 8px; padding: 14px; margin: 12px 0;">
            <div style="display: grid; grid-template-columns: 120px repeat(6, 1fr); gap: 6px; text-align: center; font-size: 13.5px; align-items: center;">
                <div style="font-weight: 700; color: #7c3aed; text-align: left;">Plaintext \\(P\\):</div>
                <div class="math-pill">O (14)</div><div class="math-pill">R (17)</div><div class="math-pill">A (0)</div><div class="math-pill">N (13)</div><div class="math-pill">G (6)</div><div class="math-pill">E (4)</div>

                <div style="font-weight: 700; color: #d97706; text-align: left;">Repeated Key:</div>
                <div class="math-pill" style="border-color: #f59e0b;">R (17)</div><div class="math-pill" style="border-color: #f59e0b;">E (4)</div><div class="math-pill" style="border-color: #f59e0b;">D (3)</div><div class="math-pill" style="border-color: #f59e0b;">R (17)</div><div class="math-pill" style="border-color: #f59e0b;">E (4)</div><div class="math-pill" style="border-color: #f59e0b;">D (3)</div>

                <div style="font-weight: 700; color: var(--text-muted); text-align: left;">\\((p + k) \\bmod 26\\):</div>
                <div style="font-size: 11.5px; color: var(--text-secondary);">31 &equiv; 5</div><div style="font-size: 11.5px; color: var(--text-secondary);">21 &equiv; 21</div><div style="font-size: 11.5px; color: var(--text-secondary);">3 &equiv; 3</div><div style="font-size: 11.5px; color: var(--text-secondary);">30 &equiv; 4</div><div style="font-size: 11.5px; color: var(--text-secondary);">10 &equiv; 10</div><div style="font-size: 11.5px; color: var(--text-secondary);">7 &equiv; 7</div>

                <div style="font-weight: 700; color: #10b981; text-align: left;">Ciphertext \\(C\\):</div>
                <div class="math-pill" style="background: #10b981; color: #fff; font-weight: 800;">F</div>
                <div class="math-pill" style="background: #10b981; color: #fff; font-weight: 800;">V</div>
                <div class="math-pill" style="background: #10b981; color: #fff; font-weight: 800;">D</div>
                <div class="math-pill" style="background: #10b981; color: #fff; font-weight: 800;">E</div>
                <div class="math-pill" style="background: #10b981; color: #fff; font-weight: 800;">K</div>
                <div class="math-pill" style="background: #10b981; color: #fff; font-weight: 800;">H</div>
            </div>
        </div>
        <div class="math-card-caption">
            <strong>Result:</strong> <code>ORANGE</code> encrypted with key <code>RED</code> produces ciphertext <code>FVDEKH</code>. Notice how the same plaintext letters encrypt to different cipher letters depending on position!
        </div>
    </div>
    '''

def card_mod23_hill_matrix():
    return '''
    <div class="math-diagram-box">
        <h4 class="math-diagram-title">Hill Cipher: \\(2 \\times 2\\) Matrix Invertibility Criteria Modulo 26</h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 14px 0;">
            <div style="padding: 14px; background: rgba(124, 58, 237, 0.06); border-radius: 8px; border: 1px solid rgba(124, 58, 237, 0.2);">
                <div style="font-weight: 700; color: #7c3aed; margin-bottom: 6px;">1. Key Matrix &amp; Determinant</div>
                <div style="font-size: 13.5px; line-height: 1.6;">
                    \\(K = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}\\)<br>
                    \\(d = \\det(K) = (ad - bc) \\pmod{26}\\)<br>
                    <strong>Condition:</strong> \\(\\gcd(d, 26) = 1\\)
                </div>
            </div>
            <div style="padding: 14px; background: rgba(16, 185, 129, 0.06); border-radius: 8px; border: 1px solid rgba(16, 185, 129, 0.2);">
                <div style="font-weight: 700; color: #10b981; margin-bottom: 6px;">2. Modular Matrix Inverse</div>
                <div style="font-size: 13.5px; line-height: 1.6;">
                    \\(K^{-1} = d^{-1} \\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix} \\pmod{26}\\)<br>
                    where \\(d \\cdot d^{-1} \\equiv 1 \\pmod{26}\\).
                </div>
            </div>
        </div>
        <div class="math-card-caption">
            <strong>Encryption:</strong> \\(C = P \\cdot K \\pmod{26}\\) &bull; <strong>Decryption:</strong> \\(P = C \\cdot K^{-1} \\pmod{26}\\) where \\(P, C\\) are row vectors \\((p_1, p_2)\\).
        </div>
    </div>
    '''

def card_mod24_transposition_grid():
    return '''
    <div class="math-diagram-box">
        <h4 class="math-diagram-title">Permutation / Transposition Cipher: Block Rearrangement</h4>
        <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 14px; align-items: center; margin: 16px 0;">
            <div style="padding: 12px; background: rgba(124, 58, 237, 0.06); border-radius: 8px; border: 1px solid rgba(124, 58, 237, 0.2); text-align: center;">
                <div style="font-weight: 700; color: #7c3aed; margin-bottom: 6px;">Permutation Function \\(\\sigma\\)</div>
                <div style="font-size: 13px;">
                    \\(\\sigma = \\begin{pmatrix} 1 & 2 & 3 & 4 \\\\ 3 & 1 & 4 & 2 \\end{pmatrix}\\)<br>
                    Position 1 moves to 3<br>
                    Position 2 moves to 1<br>
                    Position 3 moves to 4<br>
                    Position 4 moves to 2
                </div>
            </div>
            <div style="font-size: 20px; font-weight: bold; color: #a78bfa;">&harr;</div>
            <div style="padding: 12px; background: rgba(16, 185, 129, 0.06); border-radius: 8px; border: 1px solid rgba(16, 185, 129, 0.2); text-align: center;">
                <div style="font-weight: 700; color: #10b981; margin-bottom: 6px;">Inverse Permutation \\(\\sigma^{-1}\\)</div>
                <div style="font-size: 13px;">
                    \\(\\sigma^{-1} = \\begin{pmatrix} 1 & 2 & 3 & 4 \\\\ 2 & 4 & 1 & 3 \\end{pmatrix}\\)<br>
                    Position 1 restored from 2<br>
                    Position 2 restored from 4<br>
                    Position 3 restored from 1<br>
                    Position 4 restored from 3
                </div>
            </div>
        </div>
        <div class="math-card-caption">
            <strong>Key Property:</strong> Transposition ciphers do NOT change letter identities (letter frequencies are 100% unchanged); they only shuffle their positional order.
        </div>
    </div>
    '''

def card_mod25_cryptosystem_tuple():
    return '''
    <div class="math-diagram-box">
        <h4 class="math-diagram-title">Mathematical Formal Definition of a Cryptosystem \\((P, C, K, E, D)\\)</h4>
        <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin: 16px 0; text-align: center;">
            <div class="math-pill" style="border-color: #7c3aed;">
                <div style="font-size: 18px; font-weight: 800; color: #7c3aed;">\\(\\mathcal{P}\\)</div>
                <div style="font-size: 11px; font-weight: 700; color: var(--text-heading); margin-top: 4px;">Plaintext Space</div>
                <div style="font-size: 10.5px; color: var(--text-secondary);">Set of all unencrypted strings</div>
            </div>
            <div class="math-pill" style="border-color: #8b5cf6;">
                <div style="font-size: 18px; font-weight: 800; color: #8b5cf6;">\\(\\mathcal{C}\\)</div>
                <div style="font-size: 11px; font-weight: 700; color: var(--text-heading); margin-top: 4px;">Ciphertext Space</div>
                <div style="font-size: 10.5px; color: var(--text-secondary);">Set of all encrypted strings</div>
            </div>
            <div class="math-pill" style="border-color: #f59e0b;">
                <div style="font-size: 18px; font-weight: 800; color: #d97706;">\\(\\mathcal{K}\\)</div>
                <div style="font-size: 11px; font-weight: 700; color: var(--text-heading); margin-top: 4px;">Keyspace</div>
                <div style="font-size: 10.5px; color: var(--text-secondary);">Set of all valid secret keys</div>
            </div>
            <div class="math-pill" style="border-color: #3b82f6;">
                <div style="font-size: 18px; font-weight: 800; color: #2563eb;">\\(\\mathcal{E}\\)</div>
                <div style="font-size: 11px; font-weight: 700; color: var(--text-heading); margin-top: 4px;">Encryption Rule</div>
                <div style="font-size: 10.5px; color: var(--text-secondary);">\\(E_k: \\mathcal{P} \\to \\mathcal{C}\\)</div>
            </div>
            <div class="math-pill" style="border-color: #10b981;">
                <div style="font-size: 18px; font-weight: 800; color: #059669;">\\(\\mathcal{D}\\)</div>
                <div style="font-size: 11px; font-weight: 700; color: var(--text-heading); margin-top: 4px;">Decryption Rule</div>
                <div style="font-size: 10.5px; color: var(--text-secondary);">\\(D_k: \\mathcal{C} \\to \\mathcal{P}\\)</div>
            </div>
        </div>
        <div style="text-align: center; padding: 10px; background: rgba(16, 185, 129, 0.08); border-radius: 8px; border: 1px solid #10b981; font-weight: 700; color: #065f46;">
            Fundamental Decryption Condition: \\(\\forall k \\in \\mathcal{K},\\; \\forall p \\in \\mathcal{P}:\\quad D_k(E_k(p)) = p\\)
        </div>
    </div>
    '''

def card_mod26_trapdoor_squaring():
    return '''
    <div class="math-diagram-box">
        <h4 class="math-diagram-title">One-Way Trapdoor Functions &amp; Fast Modular Exponentiation</h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">
            <div style="padding: 14px; background: rgba(124, 58, 237, 0.06); border-radius: 8px; border: 1px solid rgba(124, 58, 237, 0.2);">
                <div style="font-weight: 700; color: #7c3aed; margin-bottom: 6px;">🚪 The Trapdoor Mechanism</div>
                <div style="font-size: 13px; line-height: 1.6; color: var(--text-body);">
                    <strong>Easy:</strong> Computing \\(y = f(x)\\) in polynomial time \\(O(\\log^3 n)\\).<br>
                    <strong>Hard:</strong> Finding \\(x\\) given \\(y\\) without special knowledge (infeasible).<br>
                    <strong>Trapdoor:</strong> With private key \\(K_{priv}\\), inverting \\(x = f^{-1}(y)\\) becomes computationally easy.
                </div>
            </div>
            <div style="padding: 14px; background: rgba(245, 158, 11, 0.06); border-radius: 8px; border: 1px solid rgba(245, 158, 11, 0.2);">
                <div style="font-weight: 700; color: #d97706; margin-bottom: 6px;">⚡ Fast Repeated Squaring</div>
                <div style="font-size: 13px; line-height: 1.6; color: var(--text-body);">
                    To calculate \\(a^b \\bmod n\\):<br>
                    Convert exponent \\(b\\) into binary: \\(b = \\sum b_i 2^i\\).<br>
                    Square intermediate results at each step and multiply by \\(a\\) only when bit \\(b_i = 1\\).<br>
                    Reduces \\(O(b)\\) naive multiplications to \\(O(\\log b)\\)!
                </div>
            </div>
        </div>
    </div>
    '''

def card_mod27_diffie_hellman_protocol():
    return '''
    <div class="math-diagram-box">
        <h4 class="math-diagram-title">Diffie-Hellman Key Exchange Protocol Architecture</h4>
        <div style="background: rgba(124, 58, 237, 0.04); border: 1px solid rgba(124, 58, 237, 0.2); border-radius: 10px; padding: 18px; margin: 14px 0;">
            <div style="text-align: center; font-size: 13px; font-weight: 700; color: #7c3aed; margin-bottom: 14px; background: rgba(124,58,237,0.1); padding: 6px 14px; border-radius: 6px;">
                Public Domain Parameters: Large Prime \\(p\\) and Primitive Root (Generator) \\(g \\bmod p\\)
            </div>
            <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 16px; align-items: stretch;">
                <div style="border: 2px solid #7c3aed; background: var(--bg-surface); border-radius: 8px; padding: 14px;">
                    <div style="font-weight: 800; color: #7c3aed; font-size: 15px; margin-bottom: 8px;">Alice</div>
                    <div style="font-size: 12.5px; line-height: 1.6;">
                        1. Chooses private secret: \\(a\\)<br>
                        2. Computes public key:<br>
                        <span style="display:inline-block; margin: 4px 0; background: rgba(124,58,237,0.12); padding: 2px 8px; border-radius: 4px; font-weight: 700; color: #7c3aed;">\\(A = g^a \\bmod p\\)</span><br>
                        3. Receives Bob's public key \\(B\\)<br>
                        4. Computes shared session key:<br>
                        <span style="display:inline-block; margin-top: 4px; background: #10b981; color: #fff; padding: 3px 8px; border-radius: 4px; font-weight: 800;">\\(K = B^a \\bmod p\\)</span>
                    </div>
                </div>

                <div style="display: flex; flex-direction: column; justify-content: center; gap: 18px; text-align: center;">
                    <div style="background: rgba(124,58,237,0.1); border: 1px solid #a78bfa; padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 700; color: #7c3aed;">
                        Alice sends \\(A\\) &rarr;
                    </div>
                    <div style="background: rgba(16,185,129,0.1); border: 1px solid #10b981; padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 700; color: #059669;">
                        &larr; Bob sends \\(B\\)
                    </div>
                </div>

                <div style="border: 2px solid #10b981; background: var(--bg-surface); border-radius: 8px; padding: 14px;">
                    <div style="font-weight: 800; color: #10b981; font-size: 15px; margin-bottom: 8px;">Bob</div>
                    <div style="font-size: 12.5px; line-height: 1.6;">
                        1. Chooses private secret: \\(b\\)<br>
                        2. Computes public key:<br>
                        <span style="display:inline-block; margin: 4px 0; background: rgba(16,185,129,0.12); padding: 2px 8px; border-radius: 4px; font-weight: 700; color: #059669;">\\(B = g^b \\bmod p\\)</span><br>
                        3. Receives Alice's public key \\(A\\)<br>
                        4. Computes shared session key:<br>
                        <span style="display:inline-block; margin-top: 4px; background: #10b981; color: #fff; padding: 3px 8px; border-radius: 4px; font-weight: 800;">\\(K = A^b \\bmod p\\)</span>
                    </div>
                </div>
            </div>
            <div style="text-align: center; margin-top: 14px; font-size: 13px; font-weight: 700; color: #059669;">
                Mathematical Identity: \\(K = (g^b)^a \\equiv g^{ab} \\equiv (g^a)^b \\pmod p\\). Both arrive at the identical key!
            </div>
        </div>
    </div>
    '''

def card_mod28_rsa_architecture():
    return '''
    <div class="math-diagram-box">
        <h4 class="math-diagram-title">The RSA Cryptosystem: 5-Stage Mathematical Master Pipeline</h4>
        <div style="display: flex; flex-direction: column; gap: 10px; margin: 16px 0;">
            <div style="display: flex; align-items: center; gap: 14px; background: rgba(124, 58, 237, 0.05); border: 1px solid rgba(124, 58, 237, 0.2); border-radius: 8px; padding: 10px 16px;">
                <span class="math-pill" style="background: #7c3aed; color: #fff; font-weight: 800; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; border-radius: 50%;">1</span>
                <div>
                    <strong style="color: var(--text-heading);">Choose Two Large Primes</strong>
                    <div style="font-size: 12.5px; color: var(--text-secondary);">Select distinct primes \\(p\\) and \\(q\\). In production, these are 1024 to 2048 bits long.</div>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 14px; background: rgba(124, 58, 237, 0.05); border: 1px solid rgba(124, 58, 237, 0.2); border-radius: 8px; padding: 10px 16px;">
                <span class="math-pill" style="background: #7c3aed; color: #fff; font-weight: 800; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; border-radius: 50%;">2</span>
                <div>
                    <strong style="color: var(--text-heading);">Calculate Modulus \\(n\\) and Euler's Totient \\(\\phi(n)\\)</strong>
                    <div style="font-size: 12.5px; color: var(--text-secondary);">\\(n = p \\cdot q\\) &bull; \\(\\phi(n) = (p - 1)(q - 1)\\). Modulus \\(n\\) is made public; \\(\\phi(n)\\) is strictly secret!</div>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 14px; background: rgba(124, 58, 237, 0.05); border: 1px solid rgba(124, 58, 237, 0.2); border-radius: 8px; padding: 10px 16px;">
                <span class="math-pill" style="background: #7c3aed; color: #fff; font-weight: 800; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; border-radius: 50%;">3</span>
                <div>
                    <strong style="color: var(--text-heading);">Select Public Exponent \\(e\\)</strong>
                    <div style="font-size: 12.5px; color: var(--text-secondary);">Choose \\(e\\) such that \\(1 &lt; e &lt; \\phi(n)\\) and \\(\\gcd(e, \\phi(n)) = 1\\) (common choices: 3, 17, 65537).</div>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 14px; background: rgba(124, 58, 237, 0.05); border: 1px solid rgba(124, 58, 237, 0.2); border-radius: 8px; padding: 10px 16px;">
                <span class="math-pill" style="background: #7c3aed; color: #fff; font-weight: 800; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; border-radius: 50%;">4</span>
                <div>
                    <strong style="color: var(--text-heading);">Derive Private Exponent \\(d\\) via Extended Euclidean Algorithm</strong>
                    <div style="font-size: 12.5px; color: var(--text-secondary);">Compute modular inverse: \\(d \\equiv e^{-1} \\pmod{\\phi(n)}\\), meaning \\(ed \\equiv 1 \\pmod{\\phi(n)}\\).</div>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 14px; background: rgba(16, 185, 129, 0.08); border: 1.5px solid #10b981; border-radius: 8px; padding: 12px 16px;">
                <span class="math-pill" style="background: #10b981; color: #fff; font-weight: 800; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; border-radius: 50%;">5</span>
                <div>
                    <strong style="color: #065f46;">Encryption &amp; Decryption Execution</strong>
                    <div style="font-size: 13px; color: var(--text-heading); margin-top: 2px;">
                        <strong>Public Key:</strong> \\((n, e)\\) &bull; <strong>Private Key:</strong> \\(d\\)<br>
                        <strong>Encryption:</strong> \\(c \\equiv m^e \\pmod n\\) &bull; <strong>Decryption:</strong> \\(m \\equiv c^d \\pmod n\\)
                    </div>
                </div>
            </div>
        </div>
    </div>
    '''

def card_mod29_cryptosystems_comparison():
    return '''
    <div class="math-diagram-box">
        <h4 class="math-diagram-title">Comprehensive Triad Comparison: RSA vs. Diffie-Hellman vs. ElGamal</h4>
        <div style="overflow-x: auto;">
            <table style="width: 100%; border-collapse: collapse; font-size: 13px; margin: 12px 0;">
                <thead>
                    <tr style="background: #7c3aed; color: #fff;">
                        <th style="padding: 10px;">Feature</th>
                        <th style="padding: 10px;">Diffie-Hellman (1976)</th>
                        <th style="padding: 10px;">RSA (1977)</th>
                        <th style="padding: 10px;">ElGamal (1985)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="font-weight: 700;">Underlying Hard Problem</td>
                        <td>Discrete Logarithm Problem (DLP)</td>
                        <td>Integer Factorization Problem (IFP)</td>
                        <td>Discrete Logarithm Problem (DLP)</td>
                    </tr>
                    <tr>
                        <td style="font-weight: 700;">Primary Purpose</td>
                        <td>Key Exchange / Agreement only</td>
                        <td>Public-Key Encryption &amp; Digital Signatures</td>
                        <td>Public-Key Encryption &amp; Digital Signatures</td>
                    </tr>
                    <tr>
                        <td style="font-weight: 700;">Ciphertext Expansion</td>
                        <td>N/A (Negotiates symmetric key)</td>
                        <td>1:1 (Ciphertext same size as block)</td>
                        <td>2:1 (Produces pair \\((c_1, c_2)\\) &mdash; doubles message size)</td>
                    </tr>
                    <tr>
                        <td style="font-weight: 700;">Deterministic vs Probabilistic</td>
                        <td>N/A</td>
                        <td>Deterministic (Same \\(m\\) always yields same \\(c\\))</td>
                        <td>Probabilistic (Ephemeral random \\(k\\) yields different \\(c\\) each time)</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="math-card-caption">
            <strong>Exam Note:</strong> Probabilistic encryption (ElGamal) prevents frequency analysis and chosen-plaintext dictionary attacks because encrypting "YES" twice produces two completely different ciphertexts!
        </div>
    </div>
    '''


def card_mod26_euclidean_and_inverse():
    return '''
    <div class="math-diagram-box">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
            <h4 class="math-diagram-title" style="margin: 0;">Tool 1 &amp; 2: Extended Euclidean Algorithm &amp; Modular Inverse Engine</h4>
            <span class="callout-badge" style="background: rgba(124, 58, 237, 0.12); color: #7c3aed; font-weight: 700; padding: 4px 10px; border-radius: 6px; font-size: 11px;">GUARANTEED EXAM TOPIC</span>
        </div>
        <p style="font-size: 13.5px; color: var(--text-secondary); margin: 0 0 16px;">
            The mathematical heart of RSA key derivation: Computing \(\gcd(a, b)\), expressing it as a linear combination \(ax + by = \gcd(a, b)\) (B&eacute;zout's Identity), and deriving the modular multiplicative inverse \(a^{-1} \pmod m\).
        </p>

        <!-- Tool 1: Euclidean & Bezout -->
        <div style="background: rgba(124, 58, 237, 0.04); border: 1.5px solid rgba(124, 58, 237, 0.25); border-radius: 10px; padding: 18px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 10px;">
                <span style="background: #7c3aed; color: #fff; width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 13px;">1</span>
                <strong style="color: #7c3aed; font-size: 15px;">Worked Exam Example: Find \(\gcd(26, 7)\) and Express as \(26x + 7y\)</strong>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1.15fr; gap: 18px; margin-top: 14px;">
                <!-- Forward Division Table -->
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                    <div style="font-weight: 700; color: var(--text-heading); font-size: 13.5px; margin-bottom: 10px; display: flex; align-items: center; gap: 6px;">
                        <span>&darr;</span> Step 1: Forward Euclidean Divisions
                    </div>
                    <table style="width: 100%; border-collapse: collapse; font-size: 12.5px; text-align: left;">
                        <thead>
                            <tr style="border-bottom: 1px solid var(--border-color); color: var(--text-secondary);">
                                <th style="padding: 6px 8px;">Step</th>
                                <th style="padding: 6px 8px;">Division Equation</th>
                                <th style="padding: 6px 8px;">Remainder</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: 1px solid rgba(124,58,237,0.08);">
                                <td style="padding: 8px;"><strong>Div 1</strong></td>
                                <td style="padding: 8px;">\(26 = 3 \times 7 + 5\)</td>
                                <td style="padding: 8px; color: #7c3aed; font-weight: 700;">\(r_1 = 5\)</td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(124,58,237,0.08);">
                                <td style="padding: 8px;"><strong>Div 2</strong></td>
                                <td style="padding: 8px;">\(7 = 1 \times 5 + 2\)</td>
                                <td style="padding: 8px; color: #7c3aed; font-weight: 700;">\(r_2 = 2\)</td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(124,58,237,0.08);">
                                <td style="padding: 8px;"><strong>Div 3</strong></td>
                                <td style="padding: 8px;">\(5 = 2 \times 2 + 1\)</td>
                                <td style="padding: 8px; color: #059669; font-weight: 800;">\(r_3 = 1\) (GCD)</td>
                            </tr>
                            <tr>
                                <td style="padding: 8px;"><strong>Div 4</strong></td>
                                <td style="padding: 8px;">\(2 = 2 \times 1 + 0\)</td>
                                <td style="padding: 8px; color: var(--text-secondary);">\(r_4 = 0\) (Stop)</td>
                            </tr>
                        </tbody>
                    </table>
                    <div style="margin-top: 10px; padding: 6px 10px; background: rgba(16, 185, 129, 0.1); border-radius: 6px; font-size: 12px; color: #059669; font-weight: 700;">
                        &check; Last non-zero remainder is 1 &rarr; \(\gcd(26, 7) = 1\) (Coprime).
                    </div>
                </div>

                <!-- Backward Substitution Card -->
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                    <div style="font-weight: 700; color: var(--text-heading); font-size: 13.5px; margin-bottom: 10px; display: flex; align-items: center; gap: 6px;">
                        <span>&uarr;</span> Step 2: Backward Substitution (B&eacute;zout Form)
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 8px; font-size: 12.5px;">
                        <div style="padding: 7px 10px; background: rgba(124, 58, 237, 0.05); border-left: 3px solid #7c3aed; border-radius: 4px;">
                            <strong>Isolate GCD (1) from Div 3:</strong><br>
                            \(1 = 5 - 2 \times 2\)
                        </div>
                        <div style="padding: 7px 10px; background: rgba(124, 58, 237, 0.05); border-left: 3px solid #7c3aed; border-radius: 4px;">
                            <strong>Substitute \(2 = 7 - 1 \times 5\) from Div 2:</strong><br>
                            \(1 = 5 - 2 \times (7 - 1 \times 5) = 3 \times 5 - 2 \times 7\)
                        </div>
                        <div style="padding: 7px 10px; background: rgba(124, 58, 237, 0.05); border-left: 3px solid #7c3aed; border-radius: 4px;">
                            <strong>Substitute \(5 = 26 - 3 \times 7\) from Div 1:</strong><br>
                            \(1 = 3 \times (26 - 3 \times 7) - 2 \times 7 = 3 \times 26 - 11 \times 7\)
                        </div>
                    </div>
                    <div style="margin-top: 10px; padding: 8px 12px; background: rgba(124, 58, 237, 0.1); border-radius: 6px; font-size: 13px; color: #7c3aed; font-weight: 800; text-align: center;">
                        B&eacute;zout Form: \(26(3) + 7(-11) = 1\) &bull; \(x = 3, \; y = -11\)
                    </div>
                </div>
            </div>
        </div>

        <!-- Tool 2: Modular Inverse Engine -->
        <div style="background: rgba(16, 185, 129, 0.04); border: 1.5px solid rgba(16, 185, 129, 0.25); border-radius: 10px; padding: 18px;">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 10px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="background: #059669; color: #fff; width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 13px;">2</span>
                    <strong style="color: #059669; font-size: 15px;">Tool 2: Deriving the Modular Multiplicative Inverse</strong>
                </div>
                <span style="font-size: 12px; font-weight: 700; color: #059669; background: rgba(16, 185, 129, 0.12); padding: 3px 8px; border-radius: 4px;">
                    Rule: Inverse exists &hArr; \(\gcd(a, m) = 1\)
                </span>
            </div>

            <p style="font-size: 13px; line-height: 1.6; margin: 0 0 12px; color: var(--text-body);">
                The inverse of \(a \pmod m\) is an integer \(a^{-1}\) satisfying <strong>\(a \cdot a^{-1} \equiv 1 \pmod m\)</strong>. From B&eacute;zout's identity \(ax + my = 1\), reducing modulo \(m\) gives:
                <br>
                <span style="display: block; text-align: center; margin: 6px 0; font-weight: 700; color: #059669; font-size: 14px;">\(ax + my \equiv 1 \pmod m \implies ax + 0 \equiv 1 \pmod m \implies a \cdot x \equiv 1 \pmod m\)</span>
                Therefore, <strong>the B&eacute;zout coefficient \(x\) is the modular multiplicative inverse of \(a \pmod m\)</strong>.
            </p>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 12px 14px; font-size: 12.5px;">
                    <strong style="color: var(--text-heading);">Step 1: Extract Coefficient</strong><br>
                    From our example: \(3 \times 26 - 11 \times 7 = 1\).<br>
                    Modulo 26: \((-11 \times 7) \equiv 1 \pmod{26}\).<br>
                    Raw modular inverse of \(7 \pmod{26}\) is \(-11\).
                </div>
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 12px 14px; font-size: 12.5px;">
                    <strong style="color: var(--text-heading);">Step 2: Convert to Positive Standard Range</strong><br>
                    Add modulus \(26\) to make it positive in range \(\{0, 1, \dots, 25\}\):<br>
                    <span style="display: inline-block; margin-top: 4px; font-weight: 800; color: #059669; font-size: 13.5px;">\(-11 + 26 = 15 \pmod{26}\)</span><br>
                    <span style="color: var(--text-secondary); font-size: 11.5px;">Check: \(7 \times 15 = 105 = 4 \times 26 + 1 \equiv 1 \pmod{26}\). Correct!</span>
                </div>
            </div>
        </div>
    </div>
    '''

def card_mod26_fast_modular_exponentiation():
    return '''
    <div class="math-diagram-box">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
            <h4 class="math-diagram-title" style="margin: 0;">Fast Modular Exponentiation: Step-by-Step Repeated Squaring Walkthrough</h4>
            <span class="callout-badge" style="background: rgba(217, 119, 6, 0.12); color: #d97706; font-weight: 700; padding: 4px 10px; border-radius: 6px; font-size: 11px;">CRUCIAL EXAM TECHNIQUE</span>
        </div>
        <p style="font-size: 13.5px; color: var(--text-secondary); margin: 0 0 16px;">
            Calculating large powers like \(a^b \bmod n\) by hand without a calculator: Decompose the exponent into binary powers of 2 and square modulo \(n\) successively.
        </p>

        <div style="background: rgba(245, 158, 11, 0.05); border: 1.5px solid rgba(245, 158, 11, 0.25); border-radius: 10px; padding: 18px;">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
                <span style="background: #d97706; color: #fff; width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 13px;">&bull;</span>
                <strong style="color: #d97706; font-size: 15px;">Worked Example: Calculate \(2^{13} \bmod 11\)</strong>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1.25fr; gap: 16px;">
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                    <div style="font-weight: 700; color: var(--text-heading); font-size: 13px; margin-bottom: 8px;">1. Binary Exponent Decomposition</div>
                    <div style="font-size: 13px; line-height: 1.7; color: var(--text-body);">
                        Write exponent \(13\) as sum of powers of 2:<br>
                        <span style="display: block; padding: 6px 10px; background: rgba(245, 158, 11, 0.1); border-radius: 6px; font-weight: 700; color: #d97706; text-align: center; margin: 6px 0;">
                            \(13 = 8 + 4 + 1 = (1101)_2\)
                        </span>
                        Therefore, by exponent addition laws:<br>
                        \(2^{13} = 2^8 \cdot 2^4 \cdot 2^1 \pmod{11}\)
                    </div>
                </div>

                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                    <div style="font-weight: 700; color: var(--text-heading); font-size: 13px; margin-bottom: 8px;">2. Successive Squaring Table (mod 11)</div>
                    <table style="width: 100%; border-collapse: collapse; font-size: 12px;">
                        <thead>
                            <tr style="border-bottom: 1px solid var(--border-color); color: var(--text-secondary); text-align: left;">
                                <th style="padding: 4px 6px;">Power</th>
                                <th style="padding: 4px 6px;">Calculation</th>
                                <th style="padding: 4px 6px;">Result (mod 11)</th>
                                <th style="padding: 4px 6px;">Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: 1px solid rgba(245,158,11,0.1);">
                                <td style="padding: 6px;">\(2^1\)</td>
                                <td style="padding: 6px;">Base value</td>
                                <td style="padding: 6px; font-weight: 700; color: #d97706;">\(2\)</td>
                                <td style="padding: 6px;"><span style="background: rgba(16,185,129,0.12); color:#059669; padding:2px 6px; border-radius:4px; font-weight:700;">Included (bit=1)</span></td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(245,158,11,0.1);">
                                <td style="padding: 6px;">\(2^2\)</td>
                                <td style="padding: 6px;">\(2^2 = 4\)</td>
                                <td style="padding: 6px; font-weight: 700; color: var(--text-secondary);">\(4\)</td>
                                <td style="padding: 6px;"><span style="color: var(--text-secondary); font-size:11px;">Skipped (bit=0)</span></td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(245,158,11,0.1);">
                                <td style="padding: 6px;">\(2^4\)</td>
                                <td style="padding: 6px;">\(4^2 = 16 = 11 + 5\)</td>
                                <td style="padding: 6px; font-weight: 700; color: #d97706;">\(5\)</td>
                                <td style="padding: 6px;"><span style="background: rgba(16,185,129,0.12); color:#059669; padding:2px 6px; border-radius:4px; font-weight:700;">Included (bit=1)</span></td>
                            </tr>
                            <tr>
                                <td style="padding: 6px;">\(2^8\)</td>
                                <td style="padding: 6px;">\(5^2 = 25 = 2(11) + 3\)</td>
                                <td style="padding: 6px; font-weight: 700; color: #d97706;">\(3\)</td>
                                <td style="padding: 6px;"><span style="background: rgba(16,185,129,0.12); color:#059669; padding:2px 6px; border-radius:4px; font-weight:700;">Included (bit=1)</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Final Product Assembly -->
            <div style="margin-top: 14px; padding: 12px 16px; background: rgba(16, 185, 129, 0.08); border: 1px solid #10b981; border-radius: 8px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
                <div style="font-size: 13.5px; color: var(--text-heading);">
                    <strong>3. Multiply Included Powers:</strong> \(2^{13} = 2^8 \cdot 2^4 \cdot 2^1 \equiv 3 \times 5 \times 2 = 30 \equiv 8 \pmod{11}\)
                </div>
                <div style="background: #10b981; color: #fff; padding: 4px 14px; border-radius: 6px; font-weight: 800; font-size: 14px;">
                    Answer: \(2^{13} \equiv 8 \pmod{11}\) &check;
                </div>
            </div>
        </div>
    </div>
    '''

def card_mod27_numerical_worked_example():
    return '''
    <div class="math-diagram-box">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
            <h4 class="math-diagram-title" style="margin: 0;">Question 2 (Numerical &mdash; 5 Marks): Diffie-Hellman Calculation Walkthrough</h4>
            <span class="callout-badge" style="background: rgba(37, 99, 235, 0.12); color: #2563eb; font-weight: 700; padding: 4px 10px; border-radius: 6px; font-size: 11px;">5-MARK SOLVED EXAM QUESTION</span>
        </div>
        <p style="font-size: 13.5px; color: var(--text-secondary); margin: 0 0 16px;">
            Alice and Bob execute Diffie-Hellman with public prime \(p = 23\) and base generator \(g = 5\). Alice chooses private key \(a = 6\); Bob chooses private key \(b = 15\). Find the public keys exchanged and the derived shared secret key.
        </p>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px;">
            <!-- Step 1: Alice Public Key -->
            <div style="background: rgba(124, 58, 237, 0.05); border: 1.5px solid rgba(124, 58, 237, 0.25); border-radius: 8px; padding: 14px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    <span style="background: #7c3aed; color: #fff; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 12px;">1</span>
                    <strong style="color: #7c3aed; font-size: 14px;">Alice's Public Key (\(A\))</strong>
                </div>
                <div style="font-size: 12.5px; line-height: 1.7; color: var(--text-body);">
                    Formula: \(A = g^a \pmod p = 5^6 \pmod{23}\)<br>
                    &bull; \(5^2 = 25 \equiv 2 \pmod{23}\)<br>
                    &bull; \(5^4 = 2^2 = 4 \pmod{23}\)<br>
                    &bull; \(5^6 = 5^4 \cdot 5^2 = 4 \cdot 2 = \mathbf{8} \pmod{23}\)
                </div>
                <div style="margin-top: 10px; padding: 6px 10px; background: rgba(124, 58, 237, 0.12); border-radius: 6px; font-weight: 800; color: #7c3aed; text-align: center;">
                    Alice Public Key: \(A = 8\)
                </div>
            </div>

            <!-- Step 2: Bob Public Key -->
            <div style="background: rgba(16, 185, 129, 0.05); border: 1.5px solid rgba(16, 185, 129, 0.25); border-radius: 8px; padding: 14px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    <span style="background: #059669; color: #fff; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 12px;">2</span>
                    <strong style="color: #059669; font-size: 14px;">Bob's Public Key (\(B\))</strong>
                </div>
                <div style="font-size: 12.5px; line-height: 1.7; color: var(--text-body);">
                    Formula: \(B = g^b \pmod p = 5^{15} \pmod{23}\)<br>
                    &bull; Binary: \(15 = 8 + 4 + 2 + 1\)<br>
                    &bull; Powers: \(5^1 = 5, \; 5^2 = 2, \; 5^4 = 4, \; 5^8 = 4^2 = 16\)<br>
                    &bull; \(5^{15} = 16 \cdot 4 \cdot 2 \cdot 5 = 640 \pmod{23}\)<br>
                    &bull; Division: \(23 \times 27 = 621 \implies 640 - 621 = \mathbf{19}\)
                </div>
                <div style="margin-top: 10px; padding: 6px 10px; background: rgba(16, 185, 129, 0.12); border-radius: 6px; font-weight: 800; color: #059669; text-align: center;">
                    Bob Public Key: \(B = 19\)
                </div>
            </div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
            <!-- Step 3: Alice Computes Key -->
            <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    <span style="background: #7c3aed; color: #fff; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 12px;">3</span>
                    <strong style="color: var(--text-heading); font-size: 13.5px;">Shared Secret (Alice Computes)</strong>
                </div>
                <div style="font-size: 12.5px; line-height: 1.6; color: var(--text-body);">
                    \(K = B^a \pmod p = 19^6 \pmod{23}\)<br>
                    Negative Congruence: \(19 \equiv -4 \pmod{23}\)<br>
                    \((-4)^6 = 4^6 = (4^3)^2 = 64^2\)<br>
                    \(64 \equiv 18 \pmod{23}\) (since \(23 \times 2 = 46\))<br>
                    \(18^2 = 324 = 23 \times 14 + 2 \equiv \mathbf{2} \pmod{23}\)
                </div>
            </div>

            <!-- Step 4: Bob Computes Key -->
            <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    <span style="background: #059669; color: #fff; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 12px;">4</span>
                    <strong style="color: var(--text-heading); font-size: 13.5px;">Shared Secret (Bob Computes &amp; Check)</strong>
                </div>
                <div style="font-size: 12.5px; line-height: 1.6; color: var(--text-body);">
                    \(K = A^b \pmod p = 8^{15} \pmod{23}\)<br>
                    Notice \(8 = 2^3 \implies 8^{15} = (2^3)^{15} = 2^{45} \pmod{23}\)<br>
                    By FLT: \(2^{22} \equiv 1 \pmod{23}\)<br>
                    \(2^{45} = (2^{22})^2 \cdot 2^1 \equiv 1^2 \cdot 2 = \mathbf{2} \pmod{23}\)
                </div>
            </div>
        </div>

        <div style="margin-top: 14px; padding: 10px 16px; background: rgba(16, 185, 129, 0.1); border: 1px solid #10b981; border-radius: 8px; text-align: center; font-size: 13.5px; font-weight: 800; color: #059669;">
            &check; Mutual Verification Complete: \(K_{Alice} = K_{Bob} = 2\). Shared Secret Key established successfully!
        </div>
    </div>
    '''

def card_mod28_numerical_rsa_stop_help():
    return '''
    <div class="math-diagram-box">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
            <h4 class="math-diagram-title" style="margin: 0;">Question 2 (Full RSA Calculation &mdash; 10 Marks): "STOP" Encryption &amp; "HELP" Decryption</h4>
            <span class="callout-badge" style="background: rgba(220, 38, 38, 0.12); color: #dc2626; font-weight: 700; padding: 4px 10px; border-radius: 6px; font-size: 11px;">HIGHEST YIELD EXAM PROBLEM</span>
        </div>
        <p style="font-size: 13.5px; color: var(--text-secondary); margin: 0 0 16px;">
            Classic university examination question: Given primes \(p = 43\), \(q = 59\), and public exponent \(e = 13\). (a) Encrypt plaintext "STOP", (b) Decrypt ciphertext "0981 0461".
        </p>

        <!-- Stage 1: Setup -->
        <div style="background: rgba(124, 58, 237, 0.05); border: 1px solid rgba(124, 58, 237, 0.2); border-radius: 8px; padding: 14px; margin-bottom: 14px;">
            <strong style="color: #7c3aed; font-size: 14px;">1. System Setup &amp; Parameter Derivation</strong>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-top: 8px; font-size: 13px;">
                <div style="background: var(--bg-surface); padding: 8px 12px; border-radius: 6px; border: 1px solid var(--border-color);">
                    <strong>Modulus \(n\):</strong><br>\(n = p \times q = 43 \times 59 = \mathbf{2537}\)
                </div>
                <div style="background: var(--bg-surface); padding: 8px 12px; border-radius: 6px; border: 1px solid var(--border-color);">
                    <strong>Euler's Totient \(\phi(n)\):</strong><br>\(\phi(n) = (42)(58) = \mathbf{2436}\)
                </div>
                <div style="background: var(--bg-surface); padding: 8px 12px; border-radius: 6px; border: 1px solid var(--border-color);">
                    <strong>Public Key:</strong><br>\((n, e) = \mathbf{(2537, 13)}\)
                </div>
            </div>
        </div>

        <!-- Stage 2: Encrypt STOP -->
        <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 16px; margin-bottom: 14px;">
            <strong style="color: var(--text-heading); font-size: 14px;">2. Part (a): Encrypting "STOP" (Block Size Constraint)</strong>
            <p style="font-size: 12.5px; color: var(--text-secondary); margin: 6px 0 10px;">
                Convert letters to 2-digit numbers: S=18, T=19, O=14, P=15 &rarr; String <code>1819 1415</code>. Since \(2525 &lt; n (2537) &lt; 252525\), plaintext must be partitioned into <strong>4-digit blocks</strong> so each \(M_i &lt; n\).
            </p>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; font-size: 12.5px;">
                <div style="background: rgba(124, 58, 237, 0.04); border: 1px solid rgba(124, 58, 237, 0.2); border-radius: 6px; padding: 10px 12px;">
                    <strong>Block 1:</strong> \(M_1 = 1819\)<br>
                    \(C_1 = M_1^e \bmod n = 1819^{13} \bmod 2537\)<br>
                    <span style="display: inline-block; margin-top: 4px; font-weight: 800; color: #7c3aed;">\(C_1 = 2081\)</span>
                </div>
                <div style="background: rgba(124, 58, 237, 0.04); border: 1px solid rgba(124, 58, 237, 0.2); border-radius: 6px; padding: 10px 12px;">
                    <strong>Block 2:</strong> \(M_2 = 1415\)<br>
                    \(C_2 = M_2^e \bmod n = 1415^{13} \bmod 2537\)<br>
                    <span style="display: inline-block; margin-top: 4px; font-weight: 800; color: #7c3aed;">\(C_2 = 2182\)</span>
                </div>
            </div>
            <div style="margin-top: 10px; padding: 8px 12px; background: rgba(124, 58, 237, 0.1); border-radius: 6px; font-weight: 800; color: #7c3aed; text-align: center; font-size: 13px;">
                Transmitted Ciphertext: <code>2081 2182</code>
            </div>
        </div>

        <!-- Stage 3: Decrypt HELP -->
        <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 16px;">
            <strong style="color: var(--text-heading); font-size: 14px;">3. Part (b): Decrypting "0981 0461"</strong>
            <p style="font-size: 12.5px; color: var(--text-secondary); margin: 6px 0 10px;">
                First compute private key \(d\) by solving \(13d \equiv 1 \pmod{2436}\) using the Extended Euclidean Algorithm:
                <br>
                <span style="font-weight: 700; color: #059669;">\(d = 937\)</span> &bull; Check: \(13 \times 937 = 12181 = 5 \times 2436 + 1 \equiv 1 \pmod{2436}\).
            </p>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; font-size: 12.5px;">
                <div style="background: rgba(16, 185, 129, 0.04); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 6px; padding: 10px 12px;">
                    <strong>Block 1:</strong> \(C_1 = 981\)<br>
                    \(M_1 = 981^{937} \bmod 2537 = \mathbf{704} \to 0704\)<br>
                    Characters: <code>07 = H</code>, <code>04 = E</code>
                </div>
                <div style="background: rgba(16, 185, 129, 0.04); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 6px; padding: 10px 12px;">
                    <strong>Block 2:</strong> \(C_2 = 461\)<br>
                    \(M_2 = 461^{937} \bmod 2537 = \mathbf{1115}\)<br>
                    Characters: <code>11 = L</code>, <code>15 = P</code>
                </div>
            </div>
            <div style="margin-top: 10px; padding: 8px 12px; background: rgba(16, 185, 129, 0.1); border-radius: 6px; font-weight: 800; color: #059669; text-align: center; font-size: 13.5px;">
                Decrypted Plaintext: <code>HELP</code> &check;
            </div>
        </div>
    </div>
    '''

def card_mod29_elgamal_full_workflow():
    return '''
    <div class="math-diagram-box">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
            <h4 class="math-diagram-title" style="margin: 0;">The ElGamal Cryptosystem: 4-Stage Complete Protocol Pipeline</h4>
            <span class="callout-badge" style="background: rgba(124, 58, 237, 0.12); color: #7c3aed; font-weight: 700; padding: 4px 10px; border-radius: 6px; font-size: 11px;">PROBABILISTIC ENCRYPTION</span>
        </div>
        <p style="font-size: 13.5px; color: var(--text-secondary); margin: 0 0 16px;">
            Based on the Discrete Logarithm Problem (DLP). Every encryption incorporates an ephemeral random value \(k\), meaning encrypting the identical message twice yields different ciphertexts!
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;">
            <!-- Key Generation -->
            <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    <span style="background: #7c3aed; color: #fff; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 11px;">1</span>
                    <strong style="color: #7c3aed; font-size: 13px;">Key Generation</strong>
                </div>
                <div style="font-size: 12px; line-height: 1.6; color: var(--text-body);">
                    &bull; Prime \(p\), primitive root \(g\)<br>
                    &bull; Private key: \(x \in (1, p-1)\)<br>
                    &bull; Compute: \(y = g^x \bmod p\)<br>
                    <div style="margin-top: 6px; padding: 4px 8px; background: rgba(124,58,237,0.08); border-radius: 4px; font-weight: 700;">
                        Public: \((p, g, y)\)<br>Private: \(x\)
                    </div>
                </div>
            </div>

            <!-- Encryption -->
            <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    <span style="background: #2563eb; color: #fff; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 11px;">2</span>
                    <strong style="color: #2563eb; font-size: 13px;">Encryption</strong>
                </div>
                <div style="font-size: 12px; line-height: 1.6; color: var(--text-body);">
                    &bull; Random secret \(k \in (1, p-1)\)<br>
                    &bull; \(C_1 = g^k \bmod p\)<br>
                    &bull; \(C_2 = (M \cdot y^k) \bmod p\)<br>
                    <div style="margin-top: 6px; padding: 4px 8px; background: rgba(37,99,235,0.08); border-radius: 4px; font-weight: 700;">
                        Ciphertext Pair: \((C_1, C_2)\)
                    </div>
                </div>
            </div>

            <!-- Decryption -->
            <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    <span style="background: #059669; color: #fff; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 11px;">3</span>
                    <strong style="color: #059669; font-size: 13px;">Decryption</strong>
                </div>
                <div style="font-size: 12px; line-height: 1.6; color: var(--text-body);">
                    &bull; Shared secret: \(S = C_1^x \bmod p\)<br>
                    &bull; Modular inverse: \(S^{-1} \bmod p\)<br>
                    &bull; Recover: \(M = (C_2 \cdot S^{-1}) \bmod p\)<br>
                    <div style="margin-top: 6px; padding: 4px 8px; background: rgba(16,185,129,0.08); border-radius: 4px; font-weight: 700;">
                        Decrypted: \(M\) &check;
                    </div>
                </div>
            </div>

            <!-- Proof of Correctness -->
            <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    <span style="background: #d97706; color: #fff; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 11px;">4</span>
                    <strong style="color: #d97706; font-size: 13px;">Proof of Correctness</strong>
                </div>
                <div style="font-size: 12px; line-height: 1.6; color: var(--text-body);">
                    \(S = (g^k)^x = g^{kx}\)<br>
                    \(C_2 = M \cdot (g^x)^k = M \cdot g^{xk}\)<br>
                    \(C_2 \cdot S^{-1} = (M \cdot g^{xk}) \cdot (g^{xk})^{-1} = M \pmod p\)<br>
                    <div style="margin-top: 6px; padding: 4px 8px; background: rgba(245,158,11,0.08); border-radius: 4px; font-weight: 700; text-align: center;">
                        Q.E.D.
                    </div>
                </div>
            </div>
        </div>
    </div>
    '''

def card_mod29_mock_exam_numerical():
    return '''
    <div class="math-diagram-box">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
            <h4 class="math-diagram-title" style="margin: 0;">Unit V Solved Numerical Examination Problems (10-Mark Full Walkthroughs)</h4>
            <span class="callout-badge" style="background: rgba(124, 58, 237, 0.12); color: #7c3aed; font-weight: 700; padding: 4px 10px; border-radius: 6px; font-size: 11px;">MOCK EXAM MASTERY</span>
        </div>
        <p style="font-size: 13.5px; color: var(--text-secondary); margin: 0 0 16px;">
            Full step-by-step numerical solutions for the highest-yield 5-mark and 10-mark examination problems covering RSA and ElGamal.
        </p>

        <!-- Question 1: ElGamal 5-Mark -->
        <div style="background: rgba(37, 99, 235, 0.04); border: 1.5px solid rgba(37, 99, 235, 0.25); border-radius: 10px; padding: 18px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 10px;">
                <strong style="color: #2563eb; font-size: 15px;">Problem 1: ElGamal Key Gen, Encryption &amp; Decryption (5 Marks)</strong>
                <span style="font-size: 11px; background: rgba(37, 99, 235, 0.12); color: #2563eb; padding: 3px 8px; border-radius: 4px; font-weight: 700;">Given: \(p = 23, g = 5, x = 6, M = 10, k = 3\)</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px; font-size: 12.5px;">
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 12px 14px;">
                    <strong style="color: #2563eb;">(a) Bob's Public Key \(y\)</strong><br>
                    \(y = g^x \bmod p = 5^6 \bmod 23\)<br>
                    \(5^2 \equiv 2, \; 5^4 \equiv 4\)<br>
                    \(5^6 = 4 \times 2 = \mathbf{8}\)<br>
                    <span style="display: inline-block; margin-top: 4px; font-weight: 700; color: #2563eb;">Public Key: \((23, 5, 8)\)</span>
                </div>

                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 12px 14px;">
                    <strong style="color: #2563eb;">(b) Alice Encrypts \(M = 10\) (\(k = 3\))</strong><br>
                    \(C_1 = 5^3 \bmod 23 = 125 \bmod 23 = \mathbf{10}\)<br>
                    \(C_2 = (10 \cdot 8^3) \bmod 23\)<br>
                    \(8^3 = 512 = 23(22) + 6 \equiv 6\)<br>
                    \(C_2 = (10 \cdot 6) = 60 \equiv \mathbf{14} \pmod{23}\)<br>
                    <span style="display: inline-block; margin-top: 4px; font-weight: 700; color: #2563eb;">Ciphertext: \((C_1, C_2) = (10, 14)\)</span>
                </div>

                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 12px 14px;">
                    <strong style="color: #2563eb;">(c) Bob Decrypts with \(x = 6\)</strong><br>
                    \(S = C_1^x = 10^6 \bmod 23\)<br>
                    \(10^2 \equiv 8, \; 10^4 \equiv 18, \; 10^6 = 18 \cdot 8 = 144 \equiv \mathbf{6}\)<br>
                    Inverse \(S^{-1} \pmod{23}\): \(6 \times 4 = 24 \equiv 1 \implies S^{-1} = \mathbf{4}\)<br>
                    \(M = (C_2 \cdot S^{-1}) = 14 \cdot 4 = 56 \equiv \mathbf{10} \pmod{23}\)<br>
                    <span style="display: inline-block; margin-top: 4px; font-weight: 700; color: #059669;">Recovered: \(M = 10\) &check;</span>
                </div>
            </div>
        </div>

        <!-- Question 2: RSA Full Cycle 10-Mark -->
        <div style="background: rgba(124, 58, 237, 0.04); border: 1.5px solid rgba(124, 58, 237, 0.25); border-radius: 10px; padding: 18px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 10px;">
                <strong style="color: #7c3aed; font-size: 15px;">Problem 2: RSA Complete Execution Cycle (10 Marks)</strong>
                <span style="font-size: 11px; background: rgba(124, 58, 237, 0.12); color: #7c3aed; padding: 3px 8px; border-radius: 4px; font-weight: 700;">Given: \(p = 5, q = 11, e = 3, M = 7\)</span>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; font-size: 12.5px; margin-bottom: 14px;">
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 12px 14px;">
                    <strong style="color: #7c3aed;">(a) Key Generation (3 Marks)</strong><br>
                    &bull; Modulus: \(n = p \times q = 5 \times 11 = \mathbf{55}\)<br>
                    &bull; Totient: \(\phi(n) = (4)(10) = \mathbf{40}\)<br>
                    &bull; Check \(\gcd(3, 40) = 1\) (Valid)<br>
                    &bull; Private Key \(d\): Solve \(3d \equiv 1 \pmod{40}\)<br>
                    \(3(27) = 81 = 2(40) + 1 \implies \mathbf{d = 27}\)<br>
                    <span style="display: inline-block; margin-top: 4px; font-weight: 700; color: #7c3aed;">Public: \((55, 3)\) &bull; Private: \(d = 27\)</span>
                </div>

                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 12px 14px;">
                    <strong style="color: #7c3aed;">(b) Message Encryption (3 Marks)</strong><br>
                    Formula: \(C = M^e \bmod n = 7^3 \bmod 55\)<br>
                    \(7^3 = 343\)<br>
                    Division: \(55 \times 6 = 330\)<br>
                    \(343 - 330 = \mathbf{13}\)<br>
                    <span style="display: inline-block; margin-top: 10px; padding: 4px 10px; background: rgba(124,58,237,0.12); border-radius: 4px; font-weight: 800; color: #7c3aed;">
                        Ciphertext: \(C = 13\)
                    </span>
                </div>
            </div>

            <!-- Decryption Repeated Squaring Table -->
            <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 14px; font-size: 12.5px;">
                <strong style="color: #7c3aed;">(c) Decryption via Fast Exponentiation (4 Marks): \(M = 13^{27} \bmod 55\)</strong>
                <p style="margin: 4px 0 8px; color: var(--text-secondary); font-size: 12px;">
                    Binary of 27: \(27 = 16 + 8 + 2 + 1 = (11011)_2\). Calculate successive squares modulo 55:
                </p>
                <div style="overflow-x: auto;">
                    <table style="width: 100%; border-collapse: collapse; font-size: 12px; text-align: left;">
                        <thead>
                            <tr style="border-bottom: 1px solid var(--border-color); color: var(--text-secondary);">
                                <th style="padding: 4px 8px;">Power</th>
                                <th style="padding: 4px 8px;">Squaring Computation</th>
                                <th style="padding: 4px 8px;">Modulo 55 Result</th>
                                <th style="padding: 4px 8px;">Active Term?</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: 1px solid rgba(124,58,237,0.06);">
                                <td style="padding: 5px 8px;">\(13^1\)</td>
                                <td style="padding: 5px 8px;">Base value</td>
                                <td style="padding: 5px 8px; font-weight: 700; color: #7c3aed;">13</td>
                                <td style="padding: 5px 8px; color: #059669; font-weight: 700;">Yes (\(2^0\))</td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(124,58,237,0.06);">
                                <td style="padding: 5px 8px;">\(13^2\)</td>
                                <td style="padding: 5px 8px;">\(169 = 3(55) + 4\)</td>
                                <td style="padding: 5px 8px; font-weight: 700; color: #7c3aed;">4</td>
                                <td style="padding: 5px 8px; color: #059669; font-weight: 700;">Yes (\(2^1\))</td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(124,58,237,0.06);">
                                <td style="padding: 5px 8px;">\(13^4\)</td>
                                <td style="padding: 5px 8px;">\(4^2 = 16\)</td>
                                <td style="padding: 5px 8px; font-weight: 700; color: var(--text-secondary);">16</td>
                                <td style="padding: 5px 8px; color: var(--text-secondary);">No (\(2^2\))</td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(124,58,237,0.06);">
                                <td style="padding: 5px 8px;">\(13^8\)</td>
                                <td style="padding: 5px 8px;">\(16^2 = 256 = 4(55) + 36\)</td>
                                <td style="padding: 5px 8px; font-weight: 700; color: #7c3aed;">36</td>
                                <td style="padding: 5px 8px; color: #059669; font-weight: 700;">Yes (\(2^3\))</td>
                            </tr>
                            <tr>
                                <td style="padding: 5px 8px;">\(13^{16}\)</td>
                                <td style="padding: 5px 8px;">\(36^2 = 1296 = 23(55) + 31\)</td>
                                <td style="padding: 5px 8px; font-weight: 700; color: #7c3aed;">31</td>
                                <td style="padding: 5px 8px; color: #059669; font-weight: 700;">Yes (\(2^4\))</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div style="margin-top: 10px; padding: 8px 12px; background: rgba(16, 185, 129, 0.1); border-radius: 6px; font-weight: 700; color: #059669; font-size: 13px; text-align: center;">
                    \(M = 31 \cdot 36 \cdot 4 \cdot 13 \equiv 16 \cdot 4 \cdot 13 = 64 \cdot 13 \equiv 9 \cdot 13 = 117 \equiv \mathbf{7} \pmod{55}\) &bull; Verified! &check;
                </div>
            </div>
        </div>

        <!-- Question 3: ElGamal 10-Mark -->
        <div style="background: rgba(16, 185, 129, 0.04); border: 1.5px solid rgba(16, 185, 129, 0.25); border-radius: 10px; padding: 18px;">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 10px;">
                <strong style="color: #059669; font-size: 15px;">Problem 3: ElGamal Numerical Full Lifecycle (10 Marks)</strong>
                <span style="font-size: 11px; background: rgba(16, 185, 129, 0.12); color: #059669; padding: 3px 8px; border-radius: 4px; font-weight: 700;">Given: \(p = 19, g = 2, x = 5, M = 8, k = 3\)</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px; font-size: 12.5px;">
                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 12px 14px;">
                    <strong style="color: #059669;">(a) Public Key Derivation (2 Marks)</strong><br>
                    \(y = g^x \bmod p = 2^5 \bmod 19\)<br>
                    \(2^5 = 32 = 19 + 13\)<br>
                    <span style="display: inline-block; margin-top: 6px; font-weight: 700; color: #059669;">
                        Public Key: \((p=19, g=2, y=13)\)
                    </span>
                </div>

                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 12px 14px;">
                    <strong style="color: #059669;">(b) Encryption of \(M = 8\) (4 Marks)</strong><br>
                    \(C_1 = 2^3 \bmod 19 = \mathbf{8}\)<br>
                    \(C_2 = (8 \cdot 13^3) \bmod 19\)<br>
                    \(13^2 = 169 \equiv 17 \equiv -2\)<br>
                    \(13^3 = -2 \cdot 13 = -26 \equiv 12\)<br>
                    \(C_2 = 8 \cdot 12 = 96 = 5(19) + 1 = \mathbf{1}\)<br>
                    <span style="display: inline-block; margin-top: 6px; font-weight: 700; color: #059669;">
                        Ciphertext: \((C_1, C_2) = (8, 1)\)
                    </span>
                </div>

                <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 12px 14px;">
                    <strong style="color: #059669;">(c) Decryption Execution (4 Marks)</strong><br>
                    \(S = C_1^x = 8^5 \bmod 19\)<br>
                    \(8^2 = 64 \equiv 7, \; 8^4 = 49 \equiv 11\)<br>
                    \(8^5 = 11 \cdot 8 = 88 \equiv \mathbf{12}\)<br>
                    Inverse \(12^{-1} \pmod{19}\): \(12 \times 8 = 96 \equiv 1 \implies S^{-1} = \mathbf{8}\)<br>
                    \(M = (C_2 \cdot S^{-1}) = 1 \cdot 8 = \mathbf{8}\)<br>
                    <span style="display: inline-block; margin-top: 6px; font-weight: 700; color: #059669;">
                        Decrypted: \(M = 8\) &check;
                    </span>
                </div>
            </div>
        </div>
    </div>
    '''
