# -*- coding: utf-8 -*-
"""
Build script for Blockchain Modules 14 through 18 with Token-based Diagram Injections.
"""

import os
import re
import sys
import markdown

# Import local quiz and diagram helpers
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from render_unit4_quiz import render_quiz_html
import render_unit4_diagrams as diag

RAW_DIR = r"raw_notes/blockchain"
OUT_DIR = r"."

MODULE_META = {
    14: {
        "title": "The Bitcoin Network",
        "badge": "Unit IV — Module 14 of 18 — The Bitcoin Network",
        "desc": "P2P network architecture, full nodes vs SPV light clients, network discovery, protocol messages (version, verack, inv, getdata, tx, block), Initial Block Download (blocks-first vs headers-first), and mining pool protocols (Stratum).",
        "exam": "🔥 10-Mark: Full Node vs SPV Architecture & Merkle Proofs | ⭐ 5-Mark: Bitcoin P2P Handshake & Initial Block Download"
    },
    15: {
        "title": "Bitcoin Wallets",
        "badge": "Unit IV — Module 15 of 18 — Bitcoin Wallets",
        "desc": "Private keys, public keys, and address derivation pipeline (secp256k1, SHA-256, RIPEMD-160, Base58Check), non-deterministic (JBOK) vs hierarchical deterministic (HD BIP32/BIP44) wallets, BIP39 mnemonic seed words, wallet types, hot vs cold storage, and UTXO transaction management.",
        "exam": "🔥 10-Mark: Bitcoin Key & Address Generation Pipeline + HD Wallets (BIP32/BIP44) | ⭐ 5-Mark: Hot vs Cold Wallets & BIP39 Mnemonics"
    },
    16: {
        "title": "Bitcoin Payments",
        "badge": "Unit IV — Module 16 of 18 — Bitcoin Payments",
        "desc": "Point-of-Sale (POS) Bitcoin payments, QR codes, BIP21 payment URIs, merchant payment processors, and the BIP70 Payment Protocol (PaymentRequest, Payment, PaymentACK) with X.509 certificate authentication to prevent Man-in-the-Middle attacks.",
        "exam": "🔥 10-Mark: Complete BIP70 Payment Protocol with X.509 MITM Protection | ⭐ 5-Mark: Point of Sale (POS) Systems & BIP21 URIs"
    },
    17: {
        "title": "Innovation in Bitcoin and Advanced Protocols",
        "badge": "Unit IV — Module 17 of 18 — Innovation in Bitcoin and Advanced Protocols",
        "desc": "Bitcoin Improvement Proposals (BIP standards, informational, process), soft forks vs hard forks, scalability, transaction malleability, Segregated Witness (SegWit BIP141, 4M weight units, bc1 Bech32), Bitcoin Cash (BCH 8MB), Bitcoin Unlimited, Bitcoin Gold (Equihash), and the Lightning Network Layer-2 3-stage payment lifecycle.",
        "exam": "🔥 10-Mark: Segregated Witness (SegWit BIP141) & Malleability Fix | ⭐ 5-Mark: Soft Fork vs Hard Fork & Lightning Network 3 Stages"
    },
    18: {
        "title": "Bitcoin Investment, Buying and Selling Bitcoin",
        "badge": "Unit IV — Module 18 of 18 — Bitcoin Investment, Buying & Selling",
        "desc": "Centralized (CEX) vs decentralized (DEX) exchanges, buying vs selling, investment vs trading, long vs short positions, trading instruments (CFDs, spread betting, margin trading), order book mechanics (bids, asks, spread = ask - bid), market orders vs limit orders, and investment risks.",
        "exam": "🔥 10-Mark: Bitcoin Order Book Mechanics (Bid, Ask, Spread & Depth) | ⭐ 5-Mark: Market Orders vs Limit Orders & Long vs Short Positions"
    }
}

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

def get_nav_panel_html(curr_mod):
    units = [
        ("Unit I: Blockchain Fundamentals", [1, 2, 3, 4]),
        ("Unit II: Cryptographic Primitives", [5, 6, 7, 8]),
        ("Unit III: Consensus & Bitcoin Core", [9, 10, 11, 12, 13]),
        ("Unit IV: Bitcoin Network, Wallets, Payments & Economics", [14, 15, 16, 17, 18])
    ]
    lines = []
    for unit_title, mods in units:
        lines.append(f'<div class="nav-unit-header" style="font-weight: 800; font-size: 11.5px; text-transform: uppercase; color: #0284c7; margin: 12px 0 6px 4px; letter-spacing: 0.5px; break-inside: avoid;">{unit_title}</div>')
        for m in mods:
            t = MODULE_NAMES[m]
            if m == curr_mod:
                lines.append(f'<span class="nav-item current">{m}. {t}</span>')
            else:
                lines.append(f'<a class="nav-item" href="blockchain-module-{m}.html">{m}. {t}</a>')
    return "\n".join(lines)

def get_navbar_dropdown_html(curr_mod):
    units = [
        ("Unit I (Mods 1–4)", [1, 2, 3, 4]),
        ("Unit II (Mods 5–8)", [5, 6, 7, 8]),
        ("Unit III (Mods 9–13)", [9, 10, 11, 12, 13]),
        ("Unit IV (Mods 14–18)", [14, 15, 16, 17, 18])
    ]
    lines = []
    active_str = " active" if (curr_mod is not None and 1 <= curr_mod <= 18) else ""
    lines.append('<div class="nav-dropdown">')
    lines.append(f'    <button class="nav-dropdown-btn{active_str}"><span class="icon">⛓️</span> Blockchain (18) ▾</button>')
    lines.append('    <div class="nav-dropdown-menu">')
    lines.append('        <a href="blockchain.html" class="nav-dropdown-header">📋 Blockchain Syllabus Hub (All 18)</a>')
    for unit_title, mods in units:
        lines.append(f'        <div class="dropdown-section-title" style="font-size: 10.5px; font-weight: 700; color: #0284c7; padding: 4px 14px; text-transform: uppercase;">{unit_title}</div>')
        for m in mods:
            t = MODULE_NAMES[m]
            lines.append(f'        <a href="blockchain-module-{m}.html">Module {m}: {t}</a>')
    lines.append('        <a href="blockchain_guide.html" class="nav-dropdown-special">📖 Full 8-Module Reader</a>')
    lines.append('    </div>')
    lines.append('</div>')
    return "\n".join(lines)

def convert_tab_tables(text):
    lines = text.splitlines()
    out = []
    tab_rows = []
    for l in lines:
        if '\t' in l:
            tab_rows.append([c.strip() for c in l.split('\t')])
        else:
            if tab_rows:
                max_cols = max(len(r) for r in tab_rows)
                padded = [r + [''] * (max_cols - len(r)) for r in tab_rows]
                header = '| ' + ' | '.join(padded[0]) + ' |'
                sep = '| ' + ' | '.join(['---'] * max_cols) + ' |'
                out.append(header)
                out.append(sep)
                for r in padded[1:]:
                    out.append('| ' + ' | '.join(r) + ' |')
                out.append('')
                tab_rows = []
            out.append(l)
    if tab_rows:
        max_cols = max(len(r) for r in tab_rows)
        padded = [r + [''] * (max_cols - len(r)) for r in tab_rows]
        header = '| ' + ' | '.join(padded[0]) + ' |'
        sep = '| ' + ' | '.join(['---'] * max_cols) + ' |'
        out.append(header)
        out.append(sep)
        for r in padded[1:]:
            out.append('| ' + ' | '.join(r) + ' |')
        out.append('')
    return "\n".join(out)

def format_module_18_markdown(text):
    lines = text.splitlines()
    formatted = []
    for l in lines:
        s = l.strip()
        if s.startswith('Topic ') and ':' in s:
            formatted.append(f"# **{s}**")
        elif re.match(r'^\d+\.\d+\s', s):
            formatted.append(f"## **{s}**")
        elif s.startswith('A. Important 5-mark') or s.startswith('B. Important 10-mark') or s.startswith('C. Exam-ready') or s.startswith('D. Quick revision') or s.startswith('E. Test your'):
            formatted.append(f"# **{s}**")
        elif s.startswith('Unit IV — Module 5:'):
            formatted.append(f"# **{s}**")
        elif s.startswith('Module 5 roadmap'):
            formatted.append(f"## **{s}**")
        else:
            formatted.append(l)
    return "\n".join(formatted)

def inject_module_14_tokens(text):
    # 1. Centralized vs P2P (Topic 2)
    text = re.sub(r'\*\*Central server\*\*.*?(?=Every employee)', '', text, flags=re.DOTALL)
    text = re.sub(r'Peer A\n+Peer B\n+Peer C\n+Peer D\n+Peer E\n+Peer F\n+Illustrative peers communicating directly through network connections\.', '', text)
    text = re.sub(r'(Bitcoin uses this second architecture\.)', r'\1\n\nTOKEN_MOD14_TOPO\n\n', text)

    # 2. Node Functions Matrix (Topic 3.3)
    text = re.sub(r'(The functions depend on the type of node and its software configuration\.)', r'\1\n\nTOKEN_MOD14_MATRIX\n\n', text)

    # 3. SPV Merkle Verification (Topic 4.2 - replace raw text lines 402-415)
    text = re.sub(r'##\s+\*\*SPV verification\*\*.*?(?=###\s+\*\*Advantages of SPV nodes\*\*)', 'TOKEN_MOD14_SPV_MERKLE\n\n', text, flags=re.DOTALL)

    # 4. Full Node vs SPV Node (Topic 4.3)
    text = re.sub(r'(##\s+\*\*4\.3 Full node vs SPV node\*\*.*?\n)', r'\1\n\nTOKEN_MOD14_FULL_SPV\n\n', text, count=1)

    # 5. Packet Structure (Topic 5.3)
    text = re.sub(r'(\*\*Remember:\*\* mainnet is the real Bitcoin network, while testnet is used for testing\.)', r'\1\n\nTOKEN_MOD14_PACKET\n\n', text)

    # 6. Inventory Propagation (Topic 6)
    text = re.sub(r'(#\s+\*\*Topic 6: Important Bitcoin Protocol Messages\*\*.*?\n)', r'\1\n\nTOKEN_MOD14_INV\n\n', text, count=1)

    # 7. Handshake (Topic 7 - replace raw lines 737-760)
    text = re.sub(r'##\s+\*\*Bitcoin node connection handshake\*\*.*?(?=\*\*Connection established\*\*)', 'TOKEN_MOD14_HANDSHAKE\n\n', text, flags=re.DOTALL)
    text = text.replace('**Connection established**\n\nPeer discovery and blockchain synchronisation can proceed.', 'Peer discovery and blockchain synchronisation can proceed.')

    # 8. Node Discovery Flow (Topic 8.2)
    text = re.sub(r'(6\. Once connected, it can discover additional peers through the network\.)', r'\1\n\nTOKEN_MOD14_DISCOVERY\n\n', text)

    # 9. IBD Comparison (Topic 10)
    text = re.sub(r'(#\s+\*\*Topic 10: Blocks-First vs Headers-First Synchronisation\*\*.*?\n)', r'\1\n\nTOKEN_MOD14_IBD\n\n', text, count=1)

    # 10. Headers-first flow (Topic 10.5 - replace raw lines 955-972)
    text = re.sub(r'##\s+\*\*10\.5 Headers-first synchronisation diagram\*\*.*?(?=\*\*Remember this sequence for the exam:\*\*)', '## **10.5 Headers-first synchronisation diagram**\n\nTOKEN_MOD14_HEADERS_FLOW\n\n', text, flags=re.DOTALL)

    # 11. Stratum Protocol (Topic 11)
    text = re.sub(r'(#\s+\*\*Topic 11: Stratum Protocol\*\*.*?\n)', r'\1\n\nTOKEN_MOD14_STRATUM\n\n', text, count=1)
    return text

def inject_module_15_tokens(text):
    # 1. Clean broken external image links and stray footnote numbers
    text = re.sub(r'\[.*?\]\(https?://[^\)]+\)', '', text)
    text = re.sub(r'\n[0-9]\n', '\n', text)

    # 2. Misconception diagram (Topic 1.1 / 1.3)
    text = re.sub(r'(So, what does a Bitcoin wallet do\?\n\nIt manages the cryptographic keys that allow you to access and spend the Bitcoin associated with your wallet\.)',
                  r'\1\n\nTOKEN_MOD15_MISCONCEPTION\n\n', text)

    # 3. Key & Address Generation Pipeline (Topic 2.4 / 2.5)
    text = re.sub(r'##\s+\*\*Private key\*\*.*?##\s+\*\*Bitcoin address\*\*\n\nDerived from public-key or script-related data, depending on address type',
                  '', text, flags=re.DOTALL)
    text = re.sub(r'\*\*Private key\*\*.*?(?=###\s+\*\*What is Base58Check\?\*\*)',
                  'TOKEN_MOD15_PIPELINE\n\n', text, flags=re.DOTALL)

    # 4. Transaction Lifecycle (Topic 3.1 / 3.2)
    text = re.sub(r'\*\*Rahul opens wallet\*\*.*?(?=##\s+\*\*3\.2 Sending Bitcoin\*\*)',
                  'TOKEN_MOD15_LIFECYCLE\n\n', text, flags=re.DOTALL)

    # 5. UTXO Change Diagram (Topic 3.3)
    text = re.sub(r'\*\*Transaction example\*\*.*?(?=Here:)',
                  'TOKEN_MOD15_UTXO\n\n', text, flags=re.DOTALL)

    # 6. JBOK vs HD (Topic 4.3 Definition)
    text = re.sub(r'(An HD wallet follows a similar hierarchy for keys\.)',
                  r'\1\n\nTOKEN_MOD15_JBOK_HD\n\n', text)

    # 7. BIP44 Tree (Topic 4.3)
    text = re.sub(r'\*\*Seed\*\*.*?(?=###\s+\*\*Important characteristics\*\*)',
                  'TOKEN_MOD15_BIP44_TREE\n\n', text, flags=re.DOTALL)

    # 8. Paper Wallet (Topic 4.5)
    text = re.sub(r'(A \*\*paper wallet is a physical paper document.*?\.\*\*\n)',
                  r'\1\n\nTOKEN_MOD15_PAPER\n\n', text)

    # 9. Hardware Wallet (Topic 4.6)
    text = re.sub(r'(A \*\*hardware wallet is a dedicated physical device.*?\.\*\*\n)',
                  r'\1\n\nTOKEN_MOD15_HARDWARE\n\n', text)

    # 10. Hot vs Cold Spectrum (Topic 5)
    text = re.sub(r'(\*\*Hot wallet\*\*.*?offline key storage\.)',
                  r'TOKEN_MOD15_SPECTRUM\n\n', text, flags=re.DOTALL)

    # 11. BIP39 Mnemonic Card (Topic 7.2)
    text = re.sub(r'\*\*Illustrative recovery phrase format\*\*.*?(?=This is only a format illustration)',
                  'TOKEN_MOD15_CARD\n\n', text, flags=re.DOTALL)

    # 12. BIP39 Seed Derivation Pipeline (Topic 7.3)
    text = re.sub(r'(##\s+\*\*7\.3 How does a mnemonic phrase work\?\*\*.*?\n)',
                  r'\1\n\nTOKEN_MOD15_BIP39\n\n', text, count=1)
    return text

def inject_module_16_tokens(text):
    text = re.sub(r'\[.*?\]\(https?://[^\)]+\)', '', text)
    text = re.sub(r'\n[0-9]\n', '\n', text)
    text = re.sub(r'(\*\*5\.4 Diagram of Bitcoin POS working\*\*.*?\n\n).*?(?=##\s+\*\*5\.5 Advantages)', r'\1\n\nTOKEN_MOD16_POS_QR\n\n', text, count=1, flags=re.DOTALL)
    text = re.sub(r'(##\s+\*\*6\.4 Working of a Bitcoin payment processor\*\*.*?\n)', r'\1\n\nTOKEN_MOD16_PROCESSOR\n\n', text, count=1)
    text = re.sub(r'(##\s+\*\*7\.4 Complete working of BIP70\*\*.*?\n)', r'\1\n\nTOKEN_MOD16_BIP70\n\n', text, count=1)
    text = re.sub(r'(##\s+\*\*8\.3 How does BIP70 help prevent this attack\?\*\*.*?\n)', r'\1\n\nTOKEN_MOD16_MITM\n\n', text, count=1)
    return text

def inject_module_17_tokens(text):
    text = re.sub(r'\[.*?\]\(https?://[^\)]+\)', '', text)
    text = re.sub(r'\n[0-9]\n', '\n', text)
    text = re.sub(r'(\*\*3\.4 Diagram: Soft fork vs Hard fork\*\*.*?\n\n).*?(?=##\s+\*\*3\.5 Difference)', r'\1\n\nTOKEN_MOD17_FORK\n\n', text, count=1, flags=re.DOTALL)
    text = re.sub(r'(##\s+\*\*5\.3 Main idea behind SegWit\*\*.*?\n)', r'\1\n\nTOKEN_MOD17_SEGWIT\n\n', text, count=1)
    text = re.sub(r'(\*\*9\.6 Diagram: Working of the Lightning Network\*\*.*?\n\n).*?(?=##\s+\*\*9\.7 Advantages)', r'\1\n\nTOKEN_MOD17_LIGHTNING\n\n', text, count=1, flags=re.DOTALL)
    return text

def inject_module_18_tokens(text):
    text = re.sub(r'(##\s+\*\*2\.5 Types of Bitcoin exchanges\*\*.*?\n)', r'\1\n\nTOKEN_MOD18_CEX_DEX\n\n', text, count=1)
    text = re.sub(r'(#\s+\*\*Topic 4: Bitcoin Trading — Long and Short Positions\*\*.*?\n)', r'\1\n\nTOKEN_MOD18_LONG_SHORT\n\n', text, count=1)
    text = re.sub(r'(##\s+\*\*6\.3 Example of a Bitcoin order book\*\*.*?\n)', r'\1\n\nTOKEN_MOD18_ORDER_BOOK\n\n', text, count=1)
    text = re.sub(r'(#\s+\*\*Topic 8: Types of Bitcoin Orders\*\*.*?\n)', r'\1\n\nTOKEN_MOD18_ORDER_TYPES\n\n', text, count=1)
    return text

def replace_diagram_tokens(html, mod_num):
    diagram_map = {
        14: {
            "TOKEN_MOD14_TOPO": diag.diagram_centralized_vs_p2p(),
            "TOKEN_MOD14_MATRIX": diag.diagram_node_functions_matrix(),
            "TOKEN_MOD14_SPV_MERKLE": diag.diagram_spv_merkle_verification(),
            "TOKEN_MOD14_FULL_SPV": diag.diagram_full_vs_spv(),
            "TOKEN_MOD14_PACKET": diag.diagram_p2p_packet_structure(),
            "TOKEN_MOD14_INV": diag.diagram_inv_propagation(),
            "TOKEN_MOD14_HANDSHAKE": diag.diagram_p2p_handshake(),
            "TOKEN_MOD14_DISCOVERY": diag.diagram_node_discovery_flow(),
            "TOKEN_MOD14_IBD": diag.diagram_ibd_comparison(),
            "TOKEN_MOD14_HEADERS_FLOW": diag.diagram_headers_first_flow(),
            "TOKEN_MOD14_STRATUM": diag.diagram_stratum_pool()
        },
        15: {
            "TOKEN_MOD15_MISCONCEPTION": diag.diagram_wallet_misconception(),
            "TOKEN_MOD15_PIPELINE": diag.diagram_key_address_pipeline(),
            "TOKEN_MOD15_LIFECYCLE": diag.diagram_wallet_transaction_lifecycle(),
            "TOKEN_MOD15_UTXO": diag.diagram_utxo_change(),
            "TOKEN_MOD15_JBOK_HD": diag.diagram_jbok_vs_hd(),
            "TOKEN_MOD15_BIP44_TREE": diag.diagram_bip44_derivation_tree(),
            "TOKEN_MOD15_PAPER": diag.diagram_paper_wallet(),
            "TOKEN_MOD15_HARDWARE": diag.diagram_hardware_wallet(),
            "TOKEN_MOD15_SPECTRUM": diag.diagram_hot_vs_cold_spectrum(),
            "TOKEN_MOD15_CARD": diag.diagram_bip39_mnemonic_card(),
            "TOKEN_MOD15_BIP39": diag.diagram_bip39_seed()
        },
        16: {
            "TOKEN_MOD16_POS_QR": diag.diagram_pos_qr_flow(),
            "TOKEN_MOD16_PROCESSOR": diag.diagram_payment_processor(),
            "TOKEN_MOD16_BIP70": diag.diagram_bip70_protocol(),
            "TOKEN_MOD16_MITM": diag.diagram_mitm_prevention()
        },
        17: {
            "TOKEN_MOD17_FORK": diag.diagram_soft_vs_hard_fork(),
            "TOKEN_MOD17_SEGWIT": diag.diagram_segwit_block(),
            "TOKEN_MOD17_LIGHTNING": diag.diagram_lightning_lifecycle()
        },
        18: {
            "TOKEN_MOD18_CEX_DEX": diag.diagram_cex_vs_dex(),
            "TOKEN_MOD18_LONG_SHORT": diag.diagram_long_vs_short(),
            "TOKEN_MOD18_ORDER_BOOK": diag.diagram_order_book(),
            "TOKEN_MOD18_ORDER_TYPES": diag.diagram_order_types()
        }
    }
    tokens = diagram_map.get(mod_num, {})
    for token, d_html in tokens.items():
        html = html.replace(f"<p>{token}</p>", d_html)
        html = html.replace(token, d_html)
    return html

def process_raw_notes_for_module(mod_num):
    raw_path = os.path.join(RAW_DIR, f"{mod_num}.txt")
    with open(raw_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    # Cut off raw test your understanding
    split_markers = [
        "## **F. Test your understanding**",
        "## **E. Test your understanding**",
        "# **E. Test your understanding**",
        "# **F. Test your understanding**",
        "Test your understanding**",
        "E. Test your understanding"
    ]
    body_raw = raw_text
    for marker in split_markers:
        idx = body_raw.find(marker)
        if idx != -1:
            body_raw = body_raw[:idx].strip()
            break

    # Strip initial Chapter title if present
    body_raw = re.sub(r'^#\s+\*\*Unit\s+IV\s+—\s+Module\s+\d+:[^\n]+\n', '', body_raw, flags=re.IGNORECASE)

    # Clean teacher PPT and PDF references to sleek pills
    body_raw = re.sub(r'([A-Za-z0-9_\-\s]+\.pptx)', r'<span class="ref-pill">📄 Slides Reference: \1</span>', body_raw)
    body_raw = re.sub(r'([A-Za-z0-9_\-\s]+\.pdf)', r'<span class="ref-pill">📚 Textbook Reference: \1</span>', body_raw)

    # For Module 18: convert tab tables and headings
    if mod_num == 18:
        body_raw = convert_tab_tables(body_raw)
        body_raw = format_module_18_markdown(body_raw)

    # Inject diagram tokens (clean text without HTML indentation)
    if mod_num == 14:
        body_raw = inject_module_14_tokens(body_raw)
    elif mod_num == 15:
        body_raw = inject_module_15_tokens(body_raw)
    elif mod_num == 16:
        body_raw = inject_module_16_tokens(body_raw)
    elif mod_num == 17:
        body_raw = inject_module_17_tokens(body_raw)
    elif mod_num == 18:
        body_raw = inject_module_18_tokens(body_raw)

    # Protect MathJax display math \\[ ... \\] and inline math \\( ... \\)
    math_display = []
    def rep_disp(m):
        idx = len(math_display)
        content = m.group(1).replace('₹', r'\text{₹}')
        math_display.append(content)
        return f"TOKEN_MATH_DISP_{idx}"
    body_raw = re.sub(r'\\\[(.*?)\\\]', rep_disp, body_raw, flags=re.DOTALL)

    math_inline = []
    def rep_inline(m):
        idx = len(math_inline)
        content = m.group(1).replace('₹', r'\text{₹}')
        math_inline.append(content)
        return f"TOKEN_MATH_INL_{idx}"
    body_raw = re.sub(r'\\\((.*?)\\\)', rep_inline, body_raw)

    # Convert markdown to HTML
    body_html = markdown.markdown(body_raw, extensions=['tables', 'fenced_code', 'nl2br'])

    # Restore diagram tokens to real HTML diagrams
    body_html = replace_diagram_tokens(body_html, mod_num)

    # Restore MathJax
    for idx, content in enumerate(math_display):
        body_html = body_html.replace(f"<p>TOKEN_MATH_DISP_{idx}</p>", f'<div class="math-display">$${content.strip()}$$</div>')
        body_html = body_html.replace(f"TOKEN_MATH_DISP_{idx}", f'<div class="math-display">$${content.strip()}$$</div>')

    for idx, content in enumerate(math_inline):
        body_html = body_html.replace(f"TOKEN_MATH_INL_{idx}", f'<span class="math-inline">\\({content.strip()}\\)</span>')

    # Enhance Exam Headers and Callouts
    body_html = re.sub(r'<h([1-3])>(Exam-ready[^\n<]*|Likely 5-mark[^\n<]*|Likely 10-mark[^\n<]*|Important 5-mark[^\n<]*|Important 10-mark[^\n<]*|Important definitions[^\n<]*)</h\1>',
                      r'<div class="exam-header-banner">🎯 \2</div>', body_html, flags=re.IGNORECASE)
    
    body_html = re.sub(r'<h([1-3])>(Memory trick[^\n<]*|Easy memory trick[^\n<]*|Exam memory trick[^\n<]*)</h\1>',
                      r'<div class="memory-trick-banner">🧠 \2</div>', body_html, flags=re.IGNORECASE)

    # Append interactive quiz
    quiz_html = render_quiz_html(mod_num)
    body_html += "\n" + quiz_html

    # Module completion summary
    if mod_num < 18:
        completion_msg = f'''
        <div style="margin-top: 35px; padding: 20px 24px; background: rgba(2, 132, 199, 0.05); border: 1.5px solid rgba(2, 132, 199, 0.2); border-radius: 12px;">
            <h4 style="margin: 0 0 8px 0; color: #0284c7; font-size: 16px;">🚀 Module {mod_num} Completed!</h4>
            <p style="margin: 0; font-size: 14px; color: var(--text-body); line-height: 1.6;">
                Great progress! You have mastered <strong>{MODULE_META[mod_num]["title"]}</strong>. Continue to <strong>Module {mod_num+1}: {MODULE_NAMES[mod_num+1]}</strong> to advance through Unit IV!
            </p>
        </div>
        '''
    else:
        completion_msg = f'''
        <div style="margin-top: 35px; padding: 22px 26px; background: rgba(16, 185, 129, 0.06); border: 1.5px solid rgba(16, 185, 129, 0.3); border-radius: 12px;">
            <h4 style="margin: 0 0 8px 0; color: #10b981; font-size: 18px;">🎓 All 18 Blockchain Modules Completed!</h4>
            <p style="margin: 0; font-size: 14.5px; color: var(--text-body); line-height: 1.6;">
                Outstanding achievement! You have thoroughly completed all 18 modules across <strong>Unit I, Unit II, Unit III, and Unit IV</strong> of Blockchain &amp; Cryptography. Review the syllabus hub, recap key revision sheets, and retake quizzes for 100% exam mastery!
            </p>
        </div>
        '''
    body_html += "\n" + completion_msg

    return body_html

def generate_module_page(mod_num):
    meta = MODULE_META[mod_num]
    body_html = process_raw_notes_for_module(mod_num)
    nav_panel = get_nav_panel_html(mod_num)
    navbar_dropdown = get_navbar_dropdown_html(mod_num)

    prev_link = f"blockchain-module-{mod_num-1}.html"
    prev_label = f"&larr; Module {mod_num-1}"

    if mod_num < 18:
        next_link = f"blockchain-module-{mod_num+1}.html"
        next_label = f"Module {mod_num+1} &rarr;"
    else:
        next_link = "blockchain.html"
        next_label = "Blockchain Completed! &check;"

    page_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module {mod_num}: {meta["title"]} — Blockchain Study Guide</title>
    <meta name="description" content="Blockchain &amp; Cryptography study guide — {meta["badge"]}: {meta["desc"]}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="shared.css">

    <!-- MathJax for LaTeX rendering -->
    <script>
    MathJax = {{
        tex: {{
            inlineMath: [['\\\\(', '\\\\)']],
            displayMath: [['$$', '$$']],
        }},
        options: {{
            skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
        }}
    }};
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<style>
@page {{ size: A4; margin: 15mm; }}
*, *::before, *::after {{ box-sizing: border-box; }}

body {{
    font-family: 'Inter', Arial, Helvetica, sans-serif;
    font-size: 15px;
    line-height: 1.65;
    color: var(--text-body, #2d3748);
    margin: 0; padding: 0;
    background-color: var(--bg-body, #f3f5f8);
}}

.page-container {{
    max-width: 1100px;
    margin: 25px auto 40px;
    padding: 40px 55px;
    background-color: var(--bg-page, #ffffff);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    border-radius: 12px;
}}

.module-banner {{
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #0284c7 100%);
    border-radius: 10px;
    padding: 28px 32px;
    margin-bottom: 28px;
    color: #fff;
    box-shadow: 0 4px 15px rgba(2, 132, 199, 0.2);
}}
.module-badge {{
    display: inline-block;
    background: rgba(255,255,255,0.18);
    font-size: 12px; font-weight: 700;
    padding: 4px 16px; border-radius: 20px;
    text-transform: uppercase; letter-spacing: 1.5px;
    border: 1px solid rgba(255,255,255,0.25);
    margin-bottom: 10px;
}}
.module-banner-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 26px; font-weight: 700; line-height: 1.3;
    margin: 0; color: #fff !important; border: none !important; padding: 0 !important;
}}

.nav-toggle {{ margin-bottom: 24px; }}
.nav-toggle-btn {{
    display: inline-block;
    background: #0284c7;
    color: #fff;
    padding: 8px 18px;
    border-radius: 6px;
    font-size: 13px; font-weight: 600;
    cursor: pointer;
    border: none;
    text-decoration: none;
    transition: background 0.2s;
}}
.nav-toggle-btn:hover {{ background: #0369a1; }}

.nav-panel {{
    display: none;
    background: var(--bg-subtle, #f8fafc);
    border: 1px solid var(--border-color, #e2e8f0);
    border-radius: 8px;
    padding: 16px 20px;
    margin-top: 8px;
    column-count: 2;
    column-gap: 24px;
}}
.nav-panel.open {{ display: block !important; }}

.nav-item {{
    display: block;
    padding: 6px 10px;
    font-size: 13px;
    color: var(--link-color, #0284c7);
    text-decoration: none;
    border-radius: 4px;
    break-inside: avoid;
    transition: all 0.15s;
}}
.nav-item:hover {{ background: rgba(2, 132, 199, 0.1); color: #0284c7; }}
.nav-item.current {{
    background: #0284c7;
    color: #fff !important;
    font-weight: 600;
}}

h1 {{
    font-family: 'Outfit', sans-serif;
    font-size: 24px;
    color: var(--heading-color, #0f172a);
    border-bottom: 2px solid #0284c7;
    padding-bottom: 8px;
    margin-top: 36px; margin-bottom: 18px;
    line-height: 1.3;
}}
h2 {{
    font-family: 'Outfit', sans-serif;
    font-size: 20px;
    color: var(--heading-h2, #0369a1);
    border-left: 5px solid #0284c7;
    padding-left: 12px;
    margin-top: 30px; margin-bottom: 14px;
    line-height: 1.35;
}}
h3 {{
    font-family: 'Outfit', sans-serif;
    font-size: 17px;
    color: var(--heading-h3, #075985);
    margin-top: 22px; margin-bottom: 10px;
    line-height: 1.4;
}}

p {{ margin-top: 0; margin-bottom: 14px; overflow-wrap: break-word; }}
ul, ol {{ margin-top: 0; margin-bottom: 16px; padding-left: 28px; }}
li {{ margin-bottom: 6px; }}
hr {{ border: none; border-top: 1px solid var(--border-color, #e2e8f0); margin: 28px 0; }}

code {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 13.5px;
    background: var(--code-bg, #f1f5f9);
    padding: 2px 6px;
    border-radius: 4px;
    border: 1px solid var(--border-color, #e2e8f0);
}}

pre {{
    background: #0f172a;
    color: #f8fafc;
    padding: 16px;
    border-radius: 8px;
    overflow-x: auto;
    font-size: 13.5px;
}}
pre code {{ background: transparent; border: none; color: inherit; padding: 0; }}

table {{
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 14px;
}}
th, td {{
    border: 1px solid var(--border-color, #cbd5e1);
    padding: 10px 14px;
    text-align: left;
}}
th {{
    background: var(--table-th-bg, #f1f5f9);
    font-weight: 700;
    color: var(--text-heading, #0f172a);
}}

.ref-pill {{
    display: inline-flex;
    align-items: center;
    background: rgba(2, 132, 199, 0.08);
    color: #0284c7;
    border: 1px solid rgba(2, 132, 199, 0.2);
    border-radius: 16px;
    padding: 3px 10px;
    font-size: 12px;
    font-weight: 600;
    margin: 4px 4px 4px 0;
}}

.exam-header-banner {{
    background: linear-gradient(135deg, #1e3a8a, #0284c7);
    color: #ffffff;
    font-weight: 700;
    font-size: 16px;
    padding: 10px 16px;
    border-radius: 8px;
    margin: 28px 0 16px 0;
}}

.memory-trick-banner {{
    background: linear-gradient(135deg, #065f46, #10b981);
    color: #ffffff;
    font-weight: 700;
    font-size: 15px;
    padding: 10px 16px;
    border-radius: 8px;
    margin: 24px 0 14px 0;
}}

.math-display {{
    margin: 18px 0;
    overflow-x: auto;
    text-align: center;
}}

.prev-next {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 40px;
    padding-top: 24px;
    border-top: 1px solid var(--border-color, #e2e8f0);
}}

.pn-btn {{
    display: inline-block;
    background: #0284c7;
    color: #fff;
    padding: 10px 22px;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 600;
    font-size: 14px;
    transition: background 0.2s, transform 0.15s;
}}
.pn-btn:hover {{ background: #0369a1; transform: translateY(-1px); }}

.pn-reader {{
    color: #64748b;
    font-size: 13.5px;
    text-decoration: none;
    font-weight: 500;
}}
.pn-reader:hover {{ color: #0284c7; }}

/* Dark mode overrides */
[data-theme="dark"] .page-container {{
    background-color: var(--bg-page, #0b1120);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
}}
[data-theme="dark"] code {{
    background: #1e293b;
    border-color: #334155;
    color: #38bdf8;
}}
[data-theme="dark"] th {{
    background: #1e293b;
    color: #f8fafc;
}}
[data-theme="dark"] .nav-panel {{
    background: #0f172a;
    border-color: #1e293b;
}}

@media (max-width: 768px) {{
    .page-container {{ padding: 24px 18px; margin: 15px auto; }}
    .module-banner {{ padding: 20px; }}
    .module-banner-title {{ font-size: 20px; }}
    .nav-panel {{ column-count: 1; }}
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
            {navbar_dropdown}
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

<div class="page-container">

    <div class="module-banner">
        <div class="module-badge">{meta["badge"]}</div>
        <h1 class="module-banner-title">{meta["title"]}</h1>
    </div>

    <div class="nav-toggle">
        <button class="nav-toggle-btn" onclick="document.getElementById('bcNavPanel').classList.toggle('open')">
            📚 All 18 Blockchain Modules ▾
        </button>
        <div class="nav-panel" id="bcNavPanel">
{nav_panel}
        </div>
    </div>

    <div class="module-content">
{body_html}
    </div>

    <div class="prev-next">
        <a class="pn-btn" href="{prev_link}">{prev_label}</a>
        <a class="pn-reader" href="blockchain.html">📋 Blockchain Hub</a>
        <a class="pn-btn" href="{next_link}">{next_label}</a>
    </div>

</div>

<script src="shared.js"></script>
</body>
</html>
'''
    out_file = f"blockchain-module-{mod_num}.html"
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(page_html)
    print(f"✅ Generated {out_file} ({len(page_html):,} bytes)")

if __name__ == "__main__":
    for m in range(14, 19):
        generate_module_page(m)
    print("All 5 Unit IV modules successfully built with real diagrams!")
