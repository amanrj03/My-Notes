# -*- coding: utf-8 -*-
"""
Updates index.html, django.html, and maths.html with the 18-module Blockchain navigation.
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
    ("Unit I (Mods 1–4)", [1, 2, 3, 4]),
    ("Unit II (Mods 5–8)", [5, 6, 7, 8]),
    ("Unit III (Mods 9–13)", [9, 10, 11, 12, 13]),
    ("Unit IV (Mods 14–18)", [14, 15, 16, 17, 18])
]

def make_navbar_dropdown(active=False):
    active_str = " active" if active else ""
    lines = []
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

def update_index_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update dropdown
    new_dd = make_navbar_dropdown(active=False)
    pattern_dropdown = r'<div class="nav-dropdown">\s*<button class="nav-dropdown-btn[^"]*">\s*<span class="icon">⛓️</span> Blockchain \(\d+\) ▾\s*</button>.*?</div>\s*</div>'
    html = re.sub(pattern_dropdown, new_dd, html, count=1, flags=re.DOTALL)

    # 2. Update subject card sc-bc
    new_card_body = '''<div class="subject-card sc-bc">
            <div class="sc-header">
                <span class="sc-badge">18 Modules Ready &bull; 4 Units &bull; Distributed Systems &amp; Bitcoin</span>
                <h3 class="sc-title">Blockchain &amp; Cryptography</h3>
                <p class="sc-desc">Comprehensive reference spanning Bitcoin evolution, Byzantine fault tolerance, consensus protocols (PoW, PoS, PBFT, Paxos, Raft), symmetric/asymmetric ciphers, UTXO architecture, P2P networking, HD wallets, BIP70 payments, SegWit, Lightning, and market economics.</p>
            </div>
            <div class="sc-body">
                <ul class="sc-highlights">
                    <li><span class="check-icon">&check;</span> Modules 1–4: Unit I — Evolution, Distributed Systems, Consensus &amp; Decentralization</li>
                    <li><span class="check-icon">&check;</span> Modules 5–8: Unit II — Symmetric Crypto (AES), Public Key (RSA, ECC) &amp; SHA-256</li>
                    <li><span class="check-icon">&check;</span> Modules 9–13: Unit III — Consensus (Paxos, Raft, PBFT), PoW/PoS, UTXOs &amp; Mining</li>
                    <li><span class="check-icon">&check;</span> Modules 14–18: Unit IV — P2P Network, HD Wallets, BIP70 Payments, SegWit, Lightning &amp; Trading</li>
                </ul>
                <div class="sc-footer">
                    <a href="blockchain.html" class="btn-card-main">Explore 18 Modules Across 4 Units &rarr;</a>
                    <a href="blockchain_guide.html" class="btn-card-sub">Interactive Reader</a>
                </div>
            </div>
        </div>'''
    pattern_card = r'<div class="subject-card sc-bc">.*?</div>\s*</div>\s*</div>'
    html = re.sub(pattern_card, new_card_body, html, count=1, flags=re.DOTALL)

    # 3. Add search items for modules 14 to 18 if not already present
    new_search_items = ''', {"title": "Module 14: The Bitcoin Network, P2P & SPV", "subj": "Blockchain", "url": "blockchain-module-14.html", "keywords": "bitcoin network p2p peer to peer full node spv simple payment verification inv getdata stratum handshake initial block download ibd dns seeds"}, {"title": "Module 15: Bitcoin Wallets, Keys & BIP32/39", "subj": "Blockchain", "url": "blockchain-module-15.html", "keywords": "bitcoin wallets private keys public keys address derivation jbok hd wallet bip32 bip44 bip39 mnemonic seed words hot cold utxo change"}, {"title": "Module 16: Bitcoin Payments, POS & BIP70 Protocol", "subj": "Blockchain", "url": "blockchain-module-16.html", "keywords": "bitcoin payments pos point of sale qr code bip21 uri bitpay payment processor bip70 payment protocol paymentrequest payment paymentack x509 mitm"}, {"title": "Module 17: Innovation in Bitcoin, SegWit & Lightning", "subj": "Blockchain", "url": "blockchain-module-17.html", "keywords": "bitcoin innovation bip soft fork hard fork segwit segregated witness bip141 block weight bc1 bech32 bitcoin cash bch bitcoin gold equihash lightning network layer 2 htlc payment channels"}, {"title": "Module 18: Bitcoin Investment, Buying/Selling & Orders", "subj": "Blockchain", "url": "blockchain-module-18.html", "keywords": "bitcoin investment trading buying selling cex dex centralized decentralized exchange long short cfd spread betting margin trading order book bid ask spread market limit order slippage"}'''

    if 'blockchain-module-14.html' not in html:
        mod13_marker = '"url": "blockchain-module-13.html", "keywords": "bitcoin blockchain block header 80 bytes merkle tree merkle root p2p network transaction flooding block propagation mining difficulty adjustment 2016 halving 210000 accidental hard soft forks confirmations"}'
        html = html.replace(mod13_marker, mod13_marker + new_search_items)

    # 4. Footer link text
    html = html.replace('Blockchain &amp; Cryptography (13 Modules)', 'Blockchain &amp; Cryptography (18 Modules)')
    html = html.replace('Blockchain & Cryptography 13-module', 'Blockchain & Cryptography 18-module')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ Updated index.html")

def update_hub_file(fname):
    if not os.path.exists(fname):
        return
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    new_dd = make_navbar_dropdown(active=False)
    pattern_dropdown = r'<div class="nav-dropdown">\s*<button class="nav-dropdown-btn[^"]*">\s*<span class="icon">⛓️</span> Blockchain \(\d+\) ▾\s*</button>.*?</div>\s*</div>'
    if re.search(pattern_dropdown, html, flags=re.DOTALL):
        html = re.sub(pattern_dropdown, new_dd, html, count=1, flags=re.DOTALL)
        html = html.replace('Blockchain &amp; Cryptography (13 Modules)', 'Blockchain &amp; Cryptography (18 Modules)')
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ Updated dropdown in {fname}")

if __name__ == "__main__":
    update_index_html()
    update_hub_file('django.html')
    update_hub_file('maths.html')
