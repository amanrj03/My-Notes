# -*- coding: utf-8 -*-
"""
Generator script for Blockchain Unit IV modules (14 to 18)
Creates:
- blockchain-module-14.html (The Bitcoin Network)
- blockchain-module-15.html (Bitcoin Wallets)
- blockchain-module-16.html (Bitcoin Payments)
- blockchain-module-17.html (Innovation in Bitcoin and Advanced Protocols)
- blockchain-module-18.html (Bitcoin Investment, Buying and Selling Bitcoin)
Includes:
- Full notes content preserved and formatted
- Self-contained dark-theme inline visual diagrams
- Interactive MCQ quizzes with explanations
- Complete 18-module navigation grouped into 4 units
"""

import os
import re
import json
import markdown

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

ALL_18_MODULES = [
    (1, "Growth, History of Blockchain & Bitcoin", 1),
    (2, "Distributed Systems & Blockchain", 1),
    (3, "Consensus Protocols", 1),
    (4, "Decentralization", 1),
    (5, "Symmetric Cryptography", 2),
    (6, "Public Key Cryptography", 2),
    (7, "Digital Signatures + Cryptographic Constructs", 2),
    (8, "SHA & Cryptographic Hash Functions", 2),
    (9, "Consensus Problem, Analysis & Design", 3),
    (10, "Classification & Traditional Consensus (Paxos, Raft, PBFT)", 3),
    (11, "Blockchain Consensus (PoW, PoS, DPoS) & Selection", 3),
    (12, "Bitcoin Architecture, Keys & Transactions", 3),
    (13, "Bitcoin Blockchain, Network, Mining & Forks", 3),
    (14, "The Bitcoin Network", 4),
    (15, "Bitcoin Wallets", 4),
    (16, "Bitcoin Payments", 4),
    (17, "Innovation in Bitcoin and Advanced Protocols", 4),
    (18, "Bitcoin Investment, Buying and Selling Bitcoin", 4)
]

print("Script template ready.")
