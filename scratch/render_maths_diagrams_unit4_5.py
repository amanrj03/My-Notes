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
