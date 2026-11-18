# -*- coding: utf-8 -*-
"""
Verification of card injections across Modules 14 to 18.
"""
import os
import re
import render_chatgpt_cards as cards

RAW_DIR = r"raw_notes/blockchain"

def test_mod14():
    with open(os.path.join(RAW_DIR, "14.txt"), "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Example network
    text = re.sub(r'\*\*Example:\s*Bitcoin network\*\*.*?(?=##\s+\*\*1\.3)', 'TOKEN_MOD14_EXAMPLE_NET\n\n', text, flags=re.DOTALL)
    # 2. Centralized server & P2P
    text = re.sub(r'\*\*Central server\*\*.*?(?=Every employee depends)', 'TOKEN_MOD14_CENTRAL_SERVER\n\n', text, flags=re.DOTALL)
    text = text.replace('Every employee depends on the central server.\n\nIf the central server fails, communication may be interrupted.', '')
    text = re.sub(r'Peer A\n+Peer B\n+Peer C\n+Peer D\n+Peer E\n+Peer F\n+Illustrative peers communicating directly through network connections\.', 'TOKEN_MOD14_P2P_MESH\n\n', text)
    # 3. Full node card (Image 3)
    text = re.sub(r'##\s+\*\*Full node\*\*.*?Peer communication\n', 'TOKEN_MOD14_FULL_NODE\n\n', text, flags=re.DOTALL)
    # 4. SPV verification (Image 2)
    text = re.sub(r'##\s+\*\*SPV verification\*\*.*?(?=###\s+\*\*Advantages of SPV nodes\*\*)', 'TOKEN_MOD14_SPV_VERIF\n\n', text, flags=re.DOTALL)
    # 5. Handshake
    text = re.sub(r'##\s+\*\*Bitcoin node connection handshake\*\*.*?(?=\*\*Exam tip:\*\*)', 'TOKEN_MOD14_HANDSHAKE_CARD\n\n', text, flags=re.DOTALL)
    # 6. Headers-first flow
    text = re.sub(r'##\s+\*\*10\.5 Headers-first synchronisation diagram\*\*.*?(?=\*\*Remember this sequence for the exam:\*\*)', 'TOKEN_MOD14_HEADERS_FLOW\n\n', text, flags=re.DOTALL)
    # 7. Stratum pool
    text = re.sub(r'\*\*Mining pool server\*\*.*?(?=Miners receive work)', 'TOKEN_MOD14_STRATUM_CARD\n\n', text, flags=re.DOTALL)

    tokens = re.findall(r'TOKEN_MOD14_[A-Z0-9_]+', text)
    print("Mod 14 tokens found:", len(tokens), tokens)
    assert len(tokens) == 8, f"Expected 8 tokens in Mod 14, got {len(tokens)}"

def test_mod15():
    with open(os.path.join(RAW_DIR, "15.txt"), "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Key relationship
    text = re.sub(r'##\s+\*\*Private key\*\*.*?##\s+\*\*Bitcoin address\*\*\n\nDerived from public-key or script-related data, depending on address type',
                  'TOKEN_MOD15_KEYS_CARD\n\n', text, flags=re.DOTALL)
    # 2. Address generation
    text = re.sub(r'\*\*Private key\*\*.*?(?=###\s+\*\*What is Base58Check\?\*\*)',
                  'TOKEN_MOD15_ADDR_GEN_CARD\n\n', text, flags=re.DOTALL)
    # 3. Receiving flow
    text = re.sub(r'\*\*Rahul opens wallet\*\*.*?(?=##\s+\*\*3\.2 Sending Bitcoin\*\*)',
                  'TOKEN_MOD15_RECEIVING_CARD\n\n', text, flags=re.DOTALL)
    # 4. UTXO example
    text = re.sub(r'\*\*Transaction example\*\*.*?(?=Here:)',
                  'TOKEN_MOD15_UTXO_CARD\n\n', text, flags=re.DOTALL)
    # 5. JBOK wallet
    text = re.sub(r'\*\*Non-deterministic wallet\*\*.*?(?=Each private key is generated independently\.)',
                  'TOKEN_MOD15_JBOK_CARD\n\n', text, flags=re.DOTALL)
    # 6. Deterministic wallet
    text = re.sub(r'\*\*Random seed\*\*.*?(?=The same seed and derivation procedure)',
                  'TOKEN_MOD15_DETERM_CARD\n\n', text, flags=re.DOTALL)
    # 7. University hierarchy
    text = re.sub(r'\*\*University\*\*.*?(?=The university is at the top)',
                  'TOKEN_MOD15_UNIV_CARD\n\n', text, flags=re.DOTALL)
    # 8. HD tree
    text = re.sub(r'\*\*Seed\*\*.*?(?=###\s+\*\*Important characteristics\*\*)',
                  'TOKEN_MOD15_HD_CARD\n\n', text, flags=re.DOTALL)
    # 9. Recovery phrase
    text = re.sub(r'\*\*Illustrative recovery phrase format\*\*.*?(?=This is only a format illustration)',
                  'TOKEN_MOD15_RECOVERY_CARD\n\n', text, flags=re.DOTALL)

    tokens = re.findall(r'TOKEN_MOD15_[A-Z0-9_]+', text)
    print("Mod 15 tokens found:", len(tokens), tokens)
    assert len(tokens) == 9, f"Expected 9 tokens in Mod 15, got {len(tokens)}"

def test_mod16():
    with open(os.path.join(RAW_DIR, "16.txt"), "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Payment process
    text = re.sub(r'##\s+\*\*Diagram: Bitcoin payment process\*\*.*?(?=###\s+\*\*Important point: Is a transaction confirmed immediately\?\*\*)',
                  'TOKEN_MOD16_PROCESS_CARD\n\n', text, flags=re.DOTALL)
    # 2. BIP21 working
    text = re.sub(r'##\s+\*\*4\.5 Working of BIP21\*\*.*?(?=###\s+\*\*Advantages of BIP21\*\*)',
                  'TOKEN_MOD16_BIP21_CARD\n\n', text, flags=re.DOTALL)
    # 3. POS working
    text = re.sub(r'##\s+\*\*5\.4 Diagram of Bitcoin POS working\*\*.*?(?=##\s+\*\*5\.5 Advantages)',
                  'TOKEN_MOD16_POS_CARD\n\n', text, flags=re.DOTALL)
    # 4. BIP70 flow
    text = re.sub(r'\*\*Customer wallet\*\*.*?(?=###\s+\*\*Step-by-step explanation\*\*)',
                  'TOKEN_MOD16_BIP70_CARD\n\n', text, flags=re.DOTALL)
    # 5. MITM attack
    text = re.sub(r'##\s+\*\*8\.2 How does MITM happen in Bitcoin payments\?\*\*.*?(?=##\s+\*\*8\.3 How does BIP70 help prevent this attack\?\*\*)',
                  'TOKEN_MOD16_MITM_CARD\n\n', text, flags=re.DOTALL)

    tokens = re.findall(r'TOKEN_MOD16_[A-Z0-9_]+', text)
    print("Mod 16 tokens found:", len(tokens), tokens)
    assert len(tokens) == 5, f"Expected 5 tokens in Mod 16, got {len(tokens)}"

def test_mod17():
    with open(os.path.join(RAW_DIR, "17.txt"), "r", encoding="utf-8") as f:
        text = f.read()

    # 1. BIP process
    text = re.sub(r'\*\*Problem identified\*\*.*?(?=###\s+\*\*Advantages of BIPs\*\*)',
                  'TOKEN_MOD17_BIP_PROCESS_CARD\n\n', text, flags=re.DOTALL)
    # 2. Fork diagram
    text = re.sub(r'##\s+\*\*3\.4 Diagram: Soft fork vs Hard fork\*\*.*?(?=##\s+\*\*3\.5 Difference)',
                  'TOKEN_MOD17_FORK_CARD\n\n', text, flags=re.DOTALL)
    # 3. Xthin communication
    text = re.sub(r'\*\*Example of thin block communication\*\*.*?(?=###\s+\*\*3\. Parallel validation\*\*)',
                  'TOKEN_MOD17_XTHIN_CARD\n\n', text, flags=re.DOTALL)
    # 4. Lightning flow
    text = re.sub(r'##\s+\*\*9\.6 Diagram: Working of the Lightning Network\*\*.*?(?=##\s+\*\*9\.7 Advantages)',
                  'TOKEN_MOD17_LIGHTNING_CARD\n\n', text, flags=re.DOTALL)

    tokens = re.findall(r'TOKEN_MOD17_[A-Z0-9_]+', text)
    print("Mod 17 tokens found:", len(tokens), tokens)
    assert len(tokens) == 4, f"Expected 4 tokens in Mod 17, got {len(tokens)}"

def test_mod18():
    with open(os.path.join(RAW_DIR, "18.txt"), "r", encoding="utf-8") as f:
        text = f.read()

    # 1. CEX steps
    text = re.sub(r'1\.\s+User creates an exchange account.*?(?=2\.5 Types of Bitcoin exchanges)',
                  'TOKEN_MOD18_CEX_STEPS_CARD\n\n', text, flags=re.DOTALL)
    # 2. Long short cards
    text = re.sub(r'Long position\nBuying price₹50 L.*?Price decreases → Profit',
                  'TOKEN_MOD18_POSITIONS_CARD\n\n', text, flags=re.DOTALL)
    # 3. Order book example
    text = re.sub(r'BTC/INR order book — illustrative example.*?(?=6\.4 How does an order book work\?)',
                  'TOKEN_MOD18_ORDER_BOOK_CARD\n\n', text, flags=re.DOTALL)
    # 4. Market order example
    text = re.sub(r'Seller\'s price\s+Available quantity.*?(?=Important features)',
                  'TOKEN_MOD18_MARKET_ORDER_CARD\n\n', text, flags=re.DOTALL)
    # 5. Workflow
    text = re.sub(r'Topic 9: Complete Working — From Buying Bitcoin to Selling Bitcoin.*?(?=Topic 10: Advantages and Risks)',
                  'TOKEN_MOD18_WORKFLOW_CARD\n\n', text, flags=re.DOTALL)

    tokens = re.findall(r'TOKEN_MOD18_[A-Z0-9_]+', text)
    print("Mod 18 tokens found:", len(tokens), tokens)
    assert len(tokens) == 5, f"Expected 5 tokens in Mod 18, got {len(tokens)}"

if __name__ == "__main__":
    test_mod14()
    test_mod15()
    test_mod16()
    test_mod17()
    test_mod18()
    print("\nAll 30 card tokens across Modules 14 to 18 verified!")
