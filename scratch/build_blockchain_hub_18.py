# -*- coding: utf-8 -*-
"""
Rebuilds blockchain.html with 18 modules partitioned into 4 distinct units.
"""

MODULES_DATA = [
    # Unit 1
    (1, "Growth, History of Blockchain & Bitcoin", ["Bitcoin Evolution", "Double Spending", "Blind Signatures", "DigiCash"],
     "How e-cash problems, blind signatures, Hashcash, and B-money culminated in Satoshi Nakamoto's breakthrough Bitcoin whitepaper in 2008.",
     "🔥 10-Mark: Evolution of electronic cash to Bitcoin | ⭐ 5-Mark: Double spending problem & Blind signatures", 1),
    (2, "Distributed Systems & Blockchain", ["Distributed Systems", "Byzantine Generals", "Block Structure", "Merkle Trees"],
     "Centralized vs distributed models, network partitions, Byzantine fault tolerance, block headers, nonces, and blockchain layers.",
     "🎯 5-Mark: Byzantine Generals Problem | Structure of a Block | Merkle Root derivation", 1),
    (3, "Consensus Protocols ⭐⭐⭐⭐⭐", ["Proof of Work", "Proof of Stake", "PBFT", "Raft", "Paxos"],
     "How untrusted nodes reach consensus: PoW mining difficulty, PoS validators & slashing, PBFT 3-phase commit, and crash fault tolerance.",
     "🔥 10-Mark: Proof of Work vs Proof of Stake in detail | PBFT working and mathematical threshold (3f+1)", 1),
    (4, "Decentralization ⭐⭐⭐⭐⭐", ["Decentralization", "Disintermediation", "Public vs Private", "Governance"],
     "Architectural, political, and logical decentralization; routes to disintermediation, token economics, and consortium blockchains.",
     "🎯 5-Mark: Public vs Private vs Consortium blockchains | Routes to decentralization", 1),

    # Unit 2
    (5, "Symmetric Cryptography", ["Symmetric Ciphers", "DES & 3DES", "AES", "Stream vs Block"],
     "Symmetric encryption principles, substitution/transposition, Feistel networks, DES vulnerabilities, 3DES, and AES rounds.",
     "🎯 5-Mark: Symmetric vs Asymmetric Ciphers | DES vs AES architecture & round functions", 2),
    (6, "Public Key Cryptography 🔑", ["Asymmetric Crypto", "Diffie-Hellman", "RSA", "ECC secp256k1"],
     "Asymmetric keypairs, Diffie-Hellman key exchange, RSA mathematical mechanics (Euler totient), and Elliptic Curve Cryptography.",
     "🔥 10-Mark: RSA numerical calculation & key generation | ECC advantages over RSA", 2),
    (7, "Digital Signatures + Cryptographic Constructs", ["Digital Signatures", "ECDSA", "Schnorr", "Non-Repudiation"],
     "Signing and verification algorithms, ECDSA curve secp256k1 used in Bitcoin, signature aggregation, and blind signatures.",
     "🎯 5-Mark: Working of Digital Signatures | ECDSA verification process | Authentication vs Integrity", 2),
    (8, "SHA & Cryptographic Hash Functions 🔐", ["SHA-256", "Hash Properties", "Avalanche Effect", "Merkle Trees"],
     "One-way property, collision resistance, compression functions, SHA-256 internal rounds, Merkle tree proofs, and mining nonces.",
     "🔥 10-Mark: 3 Fundamental properties of cryptographic hash functions | SHA-256 internal pipeline", 2),

    # Unit 3
    (9, "Consensus Problem, Analysis & Design", ["Consensus", "CFT vs BFT", "SMR", "Safety & Liveness", "FLP Impossibility"],
     "Core foundations of distributed agreement: message passing vs shared memory, Byzantine Generals problem, State Machine Replication, network synchrony models, FLP impossibility, and lower bounds on fault tolerance (N >= 2F+1, 3F+1).",
     "🔥 10-Mark: Safety, Liveness & FLP Impossibility | ⭐ 5-Mark: CFT vs BFT & Node Count formulas (2F+1 vs 3F+1)", 3),
    (10, "Classification & Traditional Consensus (Paxos, Raft, PBFT)", ["Paxos", "Raft", "PBFT", "Voting Consensus", "View Change"],
     "Deep dive into traditional voting algorithms: Paxos prepare/accept phases, Raft leader election and log replication, PBFT three-phase commit (Pre-prepare, Prepare, Commit), view change subprotocol and checkpointing.",
     "🔥 10-Mark: Complete working of PBFT with 3 phases | ⭐ 5-Mark: Paxos Proposer/Acceptor/Learner & Raft States", 3),
    (11, "Blockchain Consensus (PoW, PoS, DPoS) & Selection", ["Proof of Work", "Proof of Stake", "DPoS", "Sybil Attacks", "51% Attack"],
     "Lottery-based consensus mechanisms: PoW nonce search & difficulty adjustment, Nakamoto consensus properties (Common Prefix, Chain Quality, Chain Growth), PoS staking & slashing, DPoS delegates, and criteria for choosing an algorithm.",
     "🔥 10-Mark: Proof of Work vs Proof of Stake in detail | Sybil Attacks vs 51% Attacks", 3),
    (12, "Bitcoin Architecture, Keys & Transactions", ["Bitcoin Architecture", "Private & Public Keys", "P2PKH & P2SH", "UTXO Model", "Bitcoin Script"],
     "The 7 structural components of Bitcoin, ECC secp256k1 key generation, P2PKH address generation pipeline (SHA-256 + RIPEMD-160 + Base58Check), digital signatures, UTXO lifecycle, and Bitcoin Script execution (locking & unlocking scripts).",
     "🔥 10-Mark: P2PKH Address Derivation Pipeline | ⭐ 5-Mark: UTXO Model vs Account Model & Bitcoin Script", 3),
    (13, "Bitcoin Blockchain, Network, Mining & Forks", ["Block Header", "Merkle Trees", "P2P Network", "Mining Lifecycle", "Halving", "Forks"],
     "Bitcoin block structure (80-byte header), Merkle root calculation & tamper detection, P2P peer discovery and transaction flooding, mining lifecycle & difficulty retargeting (every 2,016 blocks), halving (every 210,000 blocks), accidental/hard/soft forks, and confirmations.",
     "🔥 10-Mark: Complete Lifecycle of a Bitcoin Payment | ⭐ 5-Mark: Merkle Tree construction & Accidental vs Hard/Soft Forks", 3),

    # Unit 4
    (14, "The Bitcoin Network", ["Bitcoin P2P", "Full vs SPV", "Protocol Messages", "Headers-First IBD", "Stratum"],
     "P2P network discovery, protocol messages (version, verack, inv, getdata, tx, block), Full nodes vs SPV light clients (BIP37), Initial Block Download (IBD), and Stratum pool mining.",
     "🔥 10-Mark: Full Node vs SPV Architecture & Merkle Proofs | ⭐ 5-Mark: Bitcoin P2P Handshake & Initial Block Download", 4),
    (15, "Bitcoin Wallets", ["Private & Public Keys", "Address Pipeline", "HD Wallets BIP32/BIP44", "BIP39 Mnemonics", "Hot vs Cold", "UTXO Selection"],
     "Private and public key derivation (secp256k1, SHA-256, RIPEMD-160, Base58Check), non-deterministic (JBOK) vs hierarchical deterministic (HD) wallets, BIP39 mnemonic seed words, and UTXO transaction change management.",
     "🔥 10-Mark: Bitcoin Key & Address Pipeline + HD Wallets (BIP32/BIP44) | ⭐ 5-Mark: Hot vs Cold Wallets & BIP39 Mnemonics", 4),
    (16, "Bitcoin Payments", ["Point of Sale (POS)", "QR Codes", "BIP21 URI", "Payment Processors", "BIP70 Protocol", "X.509 PKI"],
     "Point-of-Sale (POS) crypto checkouts, dynamic QR codes, BIP21 URIs, merchant payment gateways (BitPay), and the BIP70 Payment Protocol (PaymentRequest, Payment, PaymentACK) with X.509 certificate authentication to prevent Man-in-the-Middle attacks.",
     "🔥 10-Mark: Complete BIP70 Payment Protocol with X.509 MITM Protection | ⭐ 5-Mark: Point of Sale (POS) Systems & BIP21 URIs", 4),
    (17, "Innovation in Bitcoin and Advanced Protocols", ["BIP Standards", "Soft vs Hard Forks", "SegWit (BIP141)", "Bitcoin Cash", "Bitcoin Gold", "Lightning Network"],
     "Bitcoin Improvement Proposals (BIPs), soft forks vs hard forks, Segregated Witness (SegWit BIP141, 4M weight units, bc1 Bech32), Bitcoin Cash (8MB), Bitcoin Gold (Equihash), and the Lightning Network Layer-2 3-stage payment lifecycle.",
     "🔥 10-Mark: Segregated Witness (SegWit BIP141) & Malleability Fix | ⭐ 5-Mark: Soft Fork vs Hard Fork & Lightning Network 3 Stages", 4),
    (18, "Bitcoin Investment, Buying and Selling Bitcoin", ["CEX vs DEX", "Long vs Short", "CFDs & Margin Trading", "Order Book", "Bid-Ask Spread", "Market vs Limit Orders"],
     "Centralized (CEX) vs decentralized (DEX) exchanges, buying vs selling, investment vs trading, long vs short positions, trading instruments (CFDs, spread betting, margin trading), order book mechanics (bids, asks, spread = ask - bid), market orders vs limit orders, and investment risks.",
     "🔥 10-Mark: Bitcoin Order Book Mechanics (Bid, Ask, Spread & Depth) | ⭐ 5-Mark: Market Orders vs Limit Orders & Long vs Short Positions", 4)
]

UNITS = [
    (1, "Unit I: Blockchain & Distributed Systems Fundamentals", "Modules 01–04 • History, Byzantine fault tolerance, consensus taxonomy & decentralization models", "4 Modules"),
    (2, "Unit II: Cryptographic Primitives in Blockchain", "Modules 05–08 • Symmetric encryption (DES/AES), Public Key (RSA/ECC), Digital Signatures & SHA-256", "4 Modules"),
    (3, "Unit III: Consensus Algorithms & Bitcoin Core Architecture", "Modules 09–13 • Traditional voting (Paxos, Raft, PBFT), Nakamoto PoW/PoS, Bitcoin UTXO & Mining lifecycle", "5 Modules"),
    (4, "Unit IV: Bitcoin Network, Wallets, Payments, Innovations & Economics", "Modules 14–18 • P2P network, HD wallets (BIP32/39), BIP70 payments, SegWit, Lightning & Exchange order books", "5 Modules")
]

def render_module_card(num, title, tags, desc, exam):
    tags_html = "".join([f'<span class="mod-cat badge-cat-bc">{t}</span>' for t in tags])
    mod_str = f"Module {num:02d}"
    return f'''
    <div class="bc-card" data-mod="{num}">
        <div class="mod-card-top">
            <span class="mod-num" style="color: #0284c7; background: rgba(2, 132, 199, 0.1);">{mod_str}</span>
            <div class="bc-tags-row">{tags_html}</div>
        </div>
        <h3 class="mod-title"><a href="blockchain-module-{num}.html">{title}</a></h3>
        <p class="mod-desc">{desc}</p>
        <div class="bc-exam-callout">
            <span class="exam-icon">📌</span>
            <div class="exam-text">{exam}</div>
        </div>
        <div class="mod-card-actions">
            <a href="blockchain-module-{num}.html" class="btn-read" style="color: #0284c7;">Read {mod_str} &rarr;</a>
            <label class="completion-checkbox" title="Mark as Completed">
                <input type="checkbox" onchange="toggleCardComplete('blockchain', {num}, this)">
                <span class="checkmark"></span>
            </label>
        </div>
    </div>'''

def render_unit_sections():
    sections_html = []
    for u_num, u_title, u_sub, u_count in UNITS:
        unit_mods = [m for m in MODULES_DATA if m[5] == u_num]
        cards_html = "\n".join([render_module_card(m[0], m[1], m[2], m[3], m[4]) for m in unit_mods])
        
        section = f'''
    <!-- {u_title.upper()} -->
    <section class="unit-group-container" id="unit-{u_num}">
        <div class="unit-header-card">
            <div class="unit-header-left">
                <span class="unit-badge">Unit {u_num}</span>
                <div>
                    <h2 class="unit-title">{u_title.split(': ')[1]}</h2>
                    <p class="unit-subtitle">{u_sub}</p>
                </div>
            </div>
            <div class="unit-count-pill">{u_count}</div>
        </div>
        <div class="modules-grid">
            {cards_html}
        </div>
    </section>'''
        sections_html.append(section)
    return "\n\n".join(sections_html)

def build_blockchain_html():
    units_content = render_unit_sections()

    dropdown_links = []
    dropdown_links.append('<div class="nav-dropdown">')
    dropdown_links.append('    <button class="nav-dropdown-btn active"><span class="icon">⛓️</span> Blockchain (18) ▾</button>')
    dropdown_links.append('    <div class="nav-dropdown-menu">')
    dropdown_links.append('        <a href="blockchain.html" class="nav-dropdown-header">📋 Blockchain Syllabus Hub (All 18)</a>')
    
    for u_num, u_title, _, _ in UNITS:
        dropdown_links.append(f'        <div class="dropdown-section-title" style="font-size: 10.5px; font-weight: 700; color: #0284c7; padding: 4px 14px; text-transform: uppercase;">{u_title}</div>')
        for m in MODULES_DATA:
            if m[5] == u_num:
                dropdown_links.append(f'        <a href="blockchain-module-{m[0]}.html">Module {m[0]}: {m[1].replace(" ⭐⭐⭐⭐⭐", "").replace(" 🔑", "").replace(" 🔐", "")}</a>')
    
    dropdown_links.append('        <a href="blockchain_guide.html" class="nav-dropdown-special">📖 Full 8-Module Reader</a>')
    dropdown_links.append('    </div>')
    dropdown_links.append('</div>')
    dropdown_html = "\n".join(dropdown_links)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blockchain &amp; Cryptography — 18 Modules Across 4 Units Complete Reference</title>
    <meta name="description" content="Comprehensive 18-module university study guide for Blockchain and Cryptography partitioned into 4 units: Fundamentals, Cryptography, Consensus, and Bitcoin Network, Wallets, Payments & Economics.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="shared.css">
<style>
body {{
    font-family: 'Inter', sans-serif;
    background: var(--bg-body);
    color: var(--text-body);
    margin: 0; padding: 0;
}}

.hub-hero {{
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #0284c7 100%);
    color: white;
    padding: 60px 24px;
    position: relative;
    overflow: hidden;
}}

.hub-hero-container {{
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
    z-index: 2;
}}

.hub-badge {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(255, 255, 255, 0.18);
    border: 1px solid rgba(255, 255, 255, 0.25);
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 16px;
    letter-spacing: 0.5px;
}}

.hub-hero-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 38px;
    font-weight: 800;
    line-height: 1.2;
    margin: 0 0 16px;
}}

.hub-hero-desc {{
    font-size: 16.5px;
    line-height: 1.6;
    max-width: 820px;
    opacity: 0.95;
    margin-bottom: 28px;
}}

.hub-hero-actions {{
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
}}

.btn-hero-primary {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 24px;
    border-radius: 8px;
    background: #ffffff;
    color: #0f172a;
    font-size: 14.5px;
    font-weight: 700;
    text-decoration: none;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    transition: transform 0.2s, box-shadow 0.2s;
}}
.btn-hero-primary:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}}

.btn-hero-secondary {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 20px;
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.3);
    color: #ffffff;
    font-size: 14px;
    font-weight: 600;
    text-decoration: none;
    backdrop-filter: blur(8px);
    transition: background 0.2s, transform 0.2s;
}}
.btn-hero-secondary:hover {{
    background: rgba(255, 255, 255, 0.25);
    transform: translateY(-2px);
}}

.exam-banner {{
    max-width: 1200px;
    margin: -24px auto 30px;
    padding: 20px 28px;
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    box-shadow: var(--shadow-md);
    position: relative;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    flex-wrap: wrap;
}}

.exam-banner-left {{
    display: flex;
    align-items: center;
    gap: 16px;
}}
.exam-banner-icon {{ font-size: 32px; }}
.exam-banner-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: var(--text-heading);
    margin: 0 0 4px;
}}
.exam-banner-sub {{
    font-size: 13.5px;
    color: var(--text-secondary);
    margin: 0;
}}

.exam-banner-pills {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}}
.exam-pill {{
    display: inline-block;
    padding: 6px 12px;
    background: rgba(2, 132, 199, 0.08);
    border: 1px solid rgba(2, 132, 199, 0.25);
    color: #0284c7;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.15s;
}}
.exam-pill:hover {{
    background: #0284c7;
    color: #ffffff;
}}

.modules-container {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 10px 24px 60px;
}}

.unit-group-container {{
    margin-bottom: 48px;
}}

.unit-header-card {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    margin: 0 0 20px 0;
    padding: 18px 24px;
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-left: 6px solid #0284c7;
    border-radius: 12px;
    box-shadow: var(--shadow-sm);
    flex-wrap: wrap;
}}

.unit-header-left {{
    display: flex;
    align-items: center;
    gap: 16px;
}}

.unit-badge {{
    background: linear-gradient(135deg, #0284c7, #1e3a8a);
    color: #ffffff;
    font-weight: 800;
    font-size: 12px;
    padding: 6px 14px;
    border-radius: 20px;
    text-transform: uppercase;
    letter-spacing: 1px;
    white-space: nowrap;
}}

.unit-title {{
    margin: 0;
    font-family: 'Outfit', sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: var(--text-heading);
}}

.unit-subtitle {{
    margin: 4px 0 0;
    font-size: 13px;
    color: var(--text-secondary);
}}

.unit-count-pill {{
    background: rgba(2, 132, 199, 0.1);
    color: #0284c7;
    font-size: 12.5px;
    font-weight: 700;
    padding: 5px 14px;
    border-radius: 16px;
    white-space: nowrap;
}}

.modules-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 24px;
}}

.bc-card {{
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
    box-shadow: var(--shadow-sm);
}}
.bc-card:hover {{
    transform: translateY(-3px);
    box-shadow: var(--shadow-md);
    border-color: #0284c7;
}}
.bc-card.completed {{
    border-left: 4px solid #10b981;
    background: rgba(16, 185, 129, 0.03);
}}

.bc-tags-row {{
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
}}

.badge-cat-bc {{
    background: rgba(2, 132, 199, 0.08);
    color: #0284c7;
    font-size: 11px;
    font-weight: 600;
    padding: 2px 7px;
    border-radius: 4px;
}}

.bc-exam-callout {{
    display: flex;
    align-items: flex-start;
    gap: 8px;
    padding: 10px 12px;
    background: var(--bg-subtle);
    border-left: 3px solid #0284c7;
    border-radius: 4px;
    margin: 14px 0;
    font-size: 12.5px;
    color: var(--text-secondary);
    line-height: 1.45;
}}

.mod-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 19px;
    font-weight: 700;
    margin: 10px 0 8px;
    line-height: 1.35;
}}
.mod-title a {{
    color: var(--text-heading);
    text-decoration: none;
}}
.mod-title a:hover {{
    color: #0284c7;
}}

.mod-desc {{
    font-size: 13.5px;
    color: var(--text-secondary);
    line-height: 1.5;
    margin: 0 0 10px;
    flex-grow: 1;
}}

.mod-card-actions {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: 14px;
    border-top: 1px solid var(--border-color);
}}

.btn-read {{
    font-size: 14px;
    font-weight: 600;
    text-decoration: none;
    transition: color 0.15s;
}}
.btn-read:hover {{
    text-decoration: underline;
}}

.completion-checkbox input {{
    cursor: pointer;
    accent-color: #0284c7;
    width: 17px;
    height: 17px;
}}

[data-theme="dark"] .unit-header-card {{
    background: #111827;
    border-color: #1e293b;
    border-left-color: #0284c7;
}}
[data-theme="dark"] .unit-title {{
    color: #f8fafc;
}}

@media (max-width: 768px) {{
    .hub-hero-title {{ font-size: 28px; }}
    .exam-banner {{ margin-top: 15px; flex-direction: column; align-items: stretch; }}
    .modules-grid {{ grid-template-columns: 1fr; }}
    .unit-header-card {{ flex-direction: column; align-items: flex-start; }}
}}
</style>
</head>
<body>

<!-- GLOBAL NAVIGATION HEADER -->
<header class="global-navbar">
    <div class="nav-container">
        <a href="index.html" class="nav-brand">
            <span class="nav-brand-icon">⚡</span>
            <span class="nav-brand-text">OmniCourse<span class="nav-brand-accent">.Hub</span></span>
        </a>
        <div class="nav-links">
            <a href="index.html" class="nav-link"><span class="icon">🏠</span> All Subjects</a>
            {dropdown_html}
            <div class="nav-dropdown">
                <button class="nav-dropdown-btn"><span class="icon">🐍</span> Django Course (45) ▾</button>
                <div class="nav-dropdown-menu">
                    <a href="django.html" class="nav-dropdown-header">📋 Django Syllabus Hub</a>
                    <a href="module-1.html">Module 1: Introduction to Web &amp; Django</a>
                    <a href="module-2.html">Module 2: Project Architecture</a>
                    <a href="django_guide.html" class="nav-dropdown-special">📖 Full 45-Module Reader</a>
                </div>
            </div>
            <div class="nav-dropdown">
                <button class="nav-dropdown-btn"><span class="icon">📐</span> Mathematics (17) ▾</button>
                <div class="nav-dropdown-menu">
                    <a href="maths.html" class="nav-dropdown-header">📋 Number Theory Hub (All 17)</a>
                    <a href="maths-module-1.html">Module 1: Divisibility Algorithm</a>
                    <a href="maths-module-2.html">Module 2: Modular Arithmetic</a>
                </div>
            </div>
            <button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode" onclick="toggleTheme()">
                <span class="theme-toggle-icon">🌙</span>
            </button>
        </div>
    </div>
</header>

<!-- HERO -->
<section class="hub-hero">
    <div class="hub-hero-container">
        <div class="hub-badge">⛓️ 18 Modules Across 4 Units • Complete Reference</div>
        <h1 class="hub-hero-title">Blockchain &amp; Cryptography</h1>
        <p class="hub-hero-desc">Complete university syllabus mastery guide covering Bitcoin's history, Byzantine Generals problem, Consensus mechanisms (PoW, PoS, PBFT, Paxos, Raft), Symmetric/Asymmetric ciphers, RSA &amp; ECC, Digital Signatures, SHA-256, Bitcoin architecture, P2P network, HD Wallets, BIP70 Payments, SegWit &amp; Lightning Network, and Financial Investment &amp; Trading.</p>
        <div class="hub-hero-actions">
            <a href="blockchain-module-1.html" class="btn-hero-primary">Start Module 01 &rarr;</a>
            <a href="#unit-2" class="btn-hero-secondary">🔐 Unit II: Crypto (Mod 05)</a>
            <a href="#unit-3" class="btn-hero-secondary">📘 Unit III: Consensus (Mod 09)</a>
            <a href="#unit-4" class="btn-hero-secondary">🌐 Unit IV: Network &amp; Wallets (Mod 14)</a>
            <a href="blockchain_guide.html" class="btn-hero-secondary">📖 Full Interactive Guide (1–8)</a>
        </div>
    </div>
</section>

<!-- EXAM BANNER -->
<div class="exam-banner">
    <div class="exam-banner-left">
        <div class="exam-banner-icon">🎯</div>
        <div>
            <h3 class="exam-banner-title">Semester Exam &amp; Viva Focus Ready — 18 Modules</h3>
            <p class="exam-banner-sub">Every module includes one-page revision sheets, memory tricks, 5- &amp; 10-mark standard university questions, and interactive quizzes.</p>
        </div>
    </div>
    <div class="exam-banner-pills">
        <a href="blockchain-module-9.html" class="exam-pill">Mod 9 FLP &amp; SMR</a>
        <a href="blockchain-module-10.html" class="exam-pill">Mod 10 PBFT &amp; Paxos</a>
        <a href="blockchain-module-11.html" class="exam-pill">Mod 11 PoW vs PoS</a>
        <a href="blockchain-module-12.html" class="exam-pill">Mod 12 Bitcoin UTXO</a>
        <a href="blockchain-module-13.html" class="exam-pill">Mod 13 Mining &amp; Halving</a>
        <a href="blockchain-module-14.html" class="exam-pill">Mod 14 P2P &amp; SPV</a>
        <a href="blockchain-module-15.html" class="exam-pill">Mod 15 Wallets &amp; BIP39</a>
        <a href="blockchain-module-16.html" class="exam-pill">Mod 16 BIP70 Payments</a>
        <a href="blockchain-module-17.html" class="exam-pill">Mod 17 SegWit &amp; Lightning</a>
        <a href="blockchain-module-18.html" class="exam-pill">Mod 18 Order Book &amp; Trading</a>
    </div>
</div>

<!-- MODULES CONTAINER -->
<div class="modules-container">
{units_content}
</div>

<!-- FOOTER -->
<footer class="portal-footer">
    <div class="portal-footer-container">
        <div class="footer-col">
            <h4>OmniCourse Hub</h4>
            <p>A unified, interactive study and revision platform built for Computer Science &amp; Engineering students.</p>
        </div>
        <div class="footer-col">
            <h4>Courses</h4>
            <ul>
                <li><a href="django.html">Django Full Course (45 Modules)</a></li>
                <li><a href="blockchain.html">Blockchain &amp; Cryptography (18 Modules)</a></li>
                <li><a href="maths.html">Mathematics: Number Theory (17 Modules)</a></li>
            </ul>
        </div>
        <div class="footer-col">
            <h4>Special Guides</h4>
            <ul>
                <li><a href="django_guide.html">Django Full Reader</a></li>
                <li><a href="blockchain_guide.html">Blockchain Full Reader</a></li>
                <li><a href="module-45.html">Django Cheat Sheet</a></li>
            </ul>
        </div>
        <div class="footer-col">
            <h4>Repository</h4>
            <ul>
                <li><a href="https://github.com/amanrj03/Django-Full-Course.git" target="_blank" rel="noopener">GitHub Project</a></li>
                <li><a href="index.html">Master Portal Home</a></li>
            </ul>
        </div>
    </div>
    <div class="footer-bottom">
        <div>&copy; 2026 OmniCourse Hub. Open Source &amp; Free for All Learners.</div>
        <div>Connected via Git Repository</div>
    </div>
</footer>

<script src="shared.js"></script>
<script>
function toggleCardComplete(subject, modNum, checkbox) {{
    var card = checkbox.closest('.bc-card');
    var isDone = window.toggleModuleCompletion(subject, modNum);
    if (isDone) {{
        card.classList.add('completed');
    }} else {{
        card.classList.remove('completed');
    }}
}}

// Restore checkboxes state from localStorage
document.addEventListener('DOMContentLoaded', function() {{
    var doneList = window.getSubjectProgress('blockchain');
    doneList.forEach(function(modNum) {{
        var card = document.querySelector('.bc-card[data-mod="' + modNum + '"]');
        if (card) {{
            card.classList.add('completed');
            var chk = card.querySelector('input[type="checkbox"]');
            if (chk) chk.checked = true;
        }}
    }});
}});
</script>
</body>
</html>
'''
    with open('blockchain.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Generated blockchain.html ({len(html):,} bytes) with 4 unit partitions!")

if __name__ == '__main__':
    build_blockchain_html()
