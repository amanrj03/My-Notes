# -*- coding: utf-8 -*-
"""
Syncs navigation across all 18 blockchain modules, hubs, and portal index.
"""

import os
import re

MODULE_NAMES = {
    1: "Growth, History of Blockchain & Bitcoin",
    2: "Distributed Systems & Blockchain",
    3: "Consensus Protocols",
    4: "Decentralization",
    5: "Symmetric Cryptography",
    6: "Public Key Cryptography",
    7: "Digital Signatures + Cryptographic Constructs",
    8: "SHA & Cryptographic Hash Functions",
    9: "Consensus Problem, Analysis & Design",
    10: "Classification & Traditional Consensus (Paxos, Raft, PBFT)",
    11: "Blockchain Consensus (PoW, PoS, DPoS) & Selection",
    12: "Bitcoin Architecture, Keys & Transactions",
    13: "Bitcoin Blockchain, Network, Mining & Forks",
    14: "The Bitcoin Network",
    15: "Bitcoin Wallets",
    16: "Bitcoin Payments",
    17: "Innovation in Bitcoin and Advanced Protocols",
    18: "Bitcoin Investment, Buying and Selling Bitcoin"
}

UNITS = [
    ("Unit I: Blockchain Fundamentals", [1, 2, 3, 4]),
    ("Unit II: Cryptographic Primitives", [5, 6, 7, 8]),
    ("Unit III: Consensus & Bitcoin Core", [9, 10, 11, 12, 13]),
    ("Unit IV: Bitcoin Network, Wallets, Payments & Economics", [14, 15, 16, 17, 18])
]

def make_nav_panel(curr_mod):
    lines = []
    for unit_title, mods in UNITS:
        lines.append(f'<div class="nav-unit-header" style="font-weight: 800; font-size: 11.5px; text-transform: uppercase; color: #0284c7; margin: 12px 0 6px 4px; letter-spacing: 0.5px; break-inside: avoid;">{unit_title}</div>')
        for m in mods:
            t = MODULE_NAMES[m]
            if m == curr_mod:
                lines.append(f'<span class="nav-item current">{m}. {t}</span>')
            else:
                lines.append(f'<a class="nav-item" href="blockchain-module-{m}.html">{m}. {t}</a>')
    return "\n".join(lines)

def make_navbar_dropdown(curr_mod):
    lines = []
    active_str = " active" if (curr_mod is not None and 1 <= curr_mod <= 18) else ""
    lines.append('<div class="nav-dropdown">')
    lines.append(f'    <button class="nav-dropdown-btn{active_str}"><span class="icon">⛓️</span> Blockchain (18) ▾</button>')
    lines.append('    <div class="nav-dropdown-menu">')
    lines.append('        <a href="blockchain.html" class="nav-dropdown-header">📋 Blockchain Syllabus Hub (All 18)</a>')
    for unit_title, mods in UNITS:
        lines.append(f'        <div class="dropdown-section-title" style="font-size: 10.5px; font-weight: 700; color: #0284c7; padding: 4px 14px; text-transform: uppercase;">{unit_title}</div>')
        for m in mods:
            t = MODULE_NAMES[m]
            lines.append(f'        <a href="blockchain-module-{m}.html">Module {m}: {t}</a>')
    lines.append('        <a href="blockchain_guide.html" class="nav-dropdown-special">📖 Full 8-Module Reader</a>')
    lines.append('    </div>')
    lines.append('</div>')
    return "\n".join(lines)

def update_module_nav(mod_num):
    fname = f"blockchain-module-{mod_num}.html"
    if not os.path.exists(fname):
        print(f"Warning: {fname} does not exist!")
        return

    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update bcNavPanel
    new_panel = make_nav_panel(mod_num)
    # Replace content between <div class="nav-panel" id="bcNavPanel"> and next </div>
    pattern_panel = r'(<div class="nav-panel" id="bcNavPanel">)(.*?)(</div>\s*</div>)'
    html = re.sub(pattern_panel, r'\1\n' + new_panel + r'\n        \3', html, flags=re.DOTALL)

    # 2. Update global navbar dropdown
    new_dropdown = make_navbar_dropdown(mod_num)
    pattern_dropdown = r'<div class="nav-dropdown">\s*<button class="nav-dropdown-btn[^"]*">\s*<span class="icon">⛓️</span> Blockchain \(\d+\) ▾\s*</button>.*?</div>\s*</div>'
    html = re.sub(pattern_dropdown, new_dropdown, html, count=1, flags=re.DOTALL)

    # 3. If module 13, update next link and completion text
    if mod_num == 13:
        html = re.sub(r'<a class="pn-btn" href="blockchain\.html">Course Completed! &check;</a>',
                      r'<a class="pn-btn" href="blockchain-module-14.html">Module 14: The Bitcoin Network &rarr;</a>',
                      html)
        html = re.sub(r'<p><strong>All 13 Blockchain Modules are now fully covered!</strong>.*?</p>',
                      r'<p><strong>Unit III Complete!</strong> You have finished the consensus and Bitcoin architecture core. Continue to <strong>Unit IV: The Bitcoin Network, Wallets, Payments &amp; Economics</strong> in Module 14!</p>',
                      html, flags=re.DOTALL)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Updated navigation in {fname}")

if __name__ == "__main__":
    for i in range(1, 19):
        update_module_nav(i)
