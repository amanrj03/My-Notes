# -*- coding: utf-8 -*-
"""
Card generators mirroring ChatGPT canvas cards and flowcharts for Modules 14 through 18.
"""

# ==============================================================================
# MODULE 14 CARDS
# ==============================================================================

def card_mod14_example_network():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">Example: Bitcoin network</div>
        <div style="max-width: 650px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px;">
            <div class="chatgpt-card-pill highlight">
                <strong>Aman's computer</strong>
                <div class="chatgpt-card-sub">Creates a Bitcoin transaction</div>
            </div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px;">
                <div class="chatgpt-card-pill">Node A</div>
                <div class="chatgpt-card-pill">Node B</div>
                <div class="chatgpt-card-pill">Node C</div>
                <div class="chatgpt-card-pill">Node D</div>
            </div>
            <div class="chatgpt-card-caption" style="margin-top: 4px;">Verifies and relays across peers</div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill success">
                <strong>Miner node</strong>
                <div class="chatgpt-card-sub">Can produce and broadcast valid blocks</div>
            </div>
        </div>
        <div class="chatgpt-card-caption">Illustrative network: real Bitcoin nodes have many connections, not necessarily this exact arrangement.</div>
    </div>
    '''

def card_mod14_centralized_server():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">Central server</div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; max-width: 700px; margin: 0 auto;">
            <div class="chatgpt-card-pill">Employee A</div>
            <div class="chatgpt-card-pill">Employee B</div>
            <div class="chatgpt-card-pill">Employee C</div>
        </div>
        <div class="chatgpt-card-caption">Every employee depends on the central server.</div>
    </div>
    '''

def card_mod14_p2p_mesh():
    return '''
    <div class="chatgpt-card-box">
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; max-width: 700px; margin: 0 auto;">
            <div class="chatgpt-card-pill"><strong>Peer A</strong></div>
            <div class="chatgpt-card-pill"><strong>Peer B</strong></div>
            <div class="chatgpt-card-pill"><strong>Peer C</strong></div>
            <div class="chatgpt-card-pill"><strong>Peer D</strong></div>
            <div class="chatgpt-card-pill"><strong>Peer E</strong></div>
            <div class="chatgpt-card-pill"><strong>Peer F</strong></div>
        </div>
        <div class="chatgpt-card-caption">Illustrative peers communicating directly through network connections.</div>
    </div>
    '''

def card_mod14_full_node():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header left">Full node</div>
        <div class="chatgpt-card-subhead">Bitcoin Core software</div>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; max-width: 750px; margin: 0 auto;">
            <div class="chatgpt-card-pill">Blockchain validation</div>
            <div class="chatgpt-card-pill">Blockchain storage</div>
            <div class="chatgpt-card-pill">Transaction relay</div>
            <div class="chatgpt-card-pill">Peer communication</div>
        </div>
    </div>
    '''

def card_mod14_spv_verification():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header left">SPV verification</div>
        <div style="max-width: 680px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px;">
            <div class="chatgpt-card-pill">
                <strong>SPV wallet</strong>
                <div class="chatgpt-card-sub">Requests proof of a transaction</div>
            </div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill">
                <strong>Full node</strong>
                <div class="chatgpt-card-sub">Provides transaction data and Merkle proof</div>
            </div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill">
                <strong>SPV client checks the Merkle proof</strong>
            </div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill filled">
                <strong>Checks inclusion against the block header's Merkle root</strong>
            </div>
        </div>
    </div>
    '''

def card_mod14_handshake():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">Bitcoin node connection handshake</div>
        <div style="max-width: 680px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; color: #38bdf8; padding: 4px 10px;">
                <span>Node A</span>
                <span>Node B</span>
            </div>
            <div style="display: flex; align-items: center; justify-content: space-between; background: #0b0f17; border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; padding: 10px 14px;">
                <span style="color: #38bdf8; font-weight: 600;">version &rarr;</span>
                <span style="color: #94a3b8; font-size: 12px;">Receives version</span>
            </div>
            <div style="display: flex; align-items: center; justify-content: space-between; background: #0b0f17; border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; padding: 10px 14px;">
                <span style="color: #94a3b8; font-size: 12px;">Receives version</span>
                <span style="color: #38bdf8; font-weight: 600;">&larr; version</span>
            </div>
            <div style="display: flex; align-items: center; justify-content: space-between; background: #0b0f17; border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; padding: 10px 14px;">
                <span style="color: #34d399; font-weight: 600;">verack &rarr;</span>
                <span style="color: #94a3b8; font-size: 12px;">Acknowledges</span>
            </div>
            <div style="display: flex; align-items: center; justify-content: space-between; background: #0b0f17; border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; padding: 10px 14px;">
                <span style="color: #94a3b8; font-size: 12px;">Acknowledges</span>
                <span style="color: #34d399; font-weight: 600;">&larr; verack</span>
            </div>
            <div class="chatgpt-card-pill filled" style="margin-top: 8px;">
                <strong style="color: #34d399;">Connection established</strong>
            </div>
        </div>
        <div class="chatgpt-card-caption">Peer discovery and blockchain synchronisation can proceed.</div>
    </div>
    '''

def card_mod14_headers_first_flow():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header left">10.5 Headers-first synchronisation diagram</div>
        <div style="max-width: 680px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px;">
            <div class="chatgpt-card-pill">
                <strong>New node starts</strong>
                <div class="chatgpt-card-sub">Needs blockchain synchronisation</div>
            </div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Connect to existing peers</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Send getheaders message</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Receive headers message</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Validate block headers</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Request full blocks using getdata</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill filled"><strong>Download and validate blocks</strong></div>
        </div>
    </div>
    '''

def card_mod14_stratum_pool():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">Mining pool server</div>
        <div class="chatgpt-card-subhead">Coordinates mining work</div>
        <div class="chatgpt-card-arrow">&darr;</div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; max-width: 720px; margin: 0 auto;">
            <div class="chatgpt-card-pill">
                <strong>Miner 1</strong>
                <div class="chatgpt-card-sub">Stratum client</div>
            </div>
            <div class="chatgpt-card-pill">
                <strong>Miner 2</strong>
                <div class="chatgpt-card-sub">Stratum client</div>
            </div>
            <div class="chatgpt-card-pill">
                <strong>Miner 3</strong>
                <div class="chatgpt-card-sub">Stratum client</div>
            </div>
        </div>
        <div class="chatgpt-card-caption">Miners receive work and submit their results through the Stratum mining-pool protocol.</div>
    </div>
    '''

# ==============================================================================
# MODULE 15 CARDS
# ==============================================================================

def card_mod15_key_relationship():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">Relationship Between Keys and Address</div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; max-width: 780px; margin: 0 auto;">
            <div class="chatgpt-card-pill">
                <strong style="color: #f87171;">Private key</strong>
                <div class="chatgpt-card-sub">Secret number generated by wallet</div>
            </div>
            <div class="chatgpt-card-pill">
                <strong style="color: #60a5fa;">Public key</strong>
                <div class="chatgpt-card-sub">Derived using elliptic curve cryptography</div>
            </div>
            <div class="chatgpt-card-pill">
                <strong style="color: #34d399;">Bitcoin address</strong>
                <div class="chatgpt-card-sub">Derived from public key hash</div>
            </div>
        </div>
        <div class="chatgpt-card-caption">Private key &rarr; used to sign | Public key &rarr; used to verify | Bitcoin address &rarr; shared to receive payments.</div>
    </div>
    '''

def card_mod15_address_generation():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">2.5 Bitcoin Address Generation Steps</div>
        <div style="max-width: 650px; margin: 0 auto; display: flex; flex-direction: column; gap: 7px;">
            <div class="chatgpt-card-pill"><strong style="color: #f87171;">Private key</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong style="color: #60a5fa;">Public key</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>SHA-256</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>RIPEMD-160</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Add version information</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Double SHA-256 checksum</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Base58Check encoding</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill filled"><strong style="color: #34d399;">Bitcoin address</strong></div>
        </div>
    </div>
    '''

def card_mod15_receiving_flow():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">Bitcoin Receiving Flow</div>
        <div style="max-width: 680px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px;">
            <div class="chatgpt-card-pill"><strong>Rahul opens wallet</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Wallet generates or displays receiving address</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Rahul shares address with Aman</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Aman sends Bitcoin</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill filled"><strong style="color: #34d399;">Transaction is confirmed and Rahul's wallet recognises the payment</strong></div>
        </div>
    </div>
    '''

def card_mod15_utxo_example():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">Transaction UTXO Accounting Example</div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; max-width: 780px; margin: 0 auto;">
            <div class="chatgpt-card-pill">
                <div style="font-size: 11px; color: #94a3b8; text-transform: uppercase;">Inputs</div>
                <div style="font-size: 18px; font-weight: 800; color: #38bdf8; margin: 4px 0;">1.2 BTC</div>
                <div class="chatgpt-card-sub">0.4 + 0.8 BTC</div>
            </div>
            <div class="chatgpt-card-pill">
                <div style="font-size: 11px; color: #94a3b8; text-transform: uppercase;">Outputs</div>
                <div style="font-size: 18px; font-weight: 800; color: #34d399; margin: 4px 0;">1.198 BTC</div>
                <div class="chatgpt-card-sub">0.5 payment + 0.698 change</div>
            </div>
            <div class="chatgpt-card-pill">
                <div style="font-size: 11px; color: #94a3b8; text-transform: uppercase;">Transaction Fee</div>
                <div style="font-size: 18px; font-weight: 800; color: #f59e0b; margin: 4px 0;">0.002 BTC</div>
                <div class="chatgpt-card-sub">Miner incentive</div>
            </div>
        </div>
        <div class="chatgpt-card-caption">Inputs (1.2 BTC) = Outputs (1.198 BTC) + Fee (0.002 BTC)</div>
    </div>
    '''

def card_mod15_jbok_wallet():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">Non-deterministic wallet (JBOK)</div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; max-width: 750px; margin: 0 auto;">
            <div class="chatgpt-card-pill">
                <strong>Private key 1</strong>
                <div class="chatgpt-card-sub">Randomly generated</div>
            </div>
            <div class="chatgpt-card-pill">
                <strong>Private key 2</strong>
                <div class="chatgpt-card-sub">Randomly generated</div>
            </div>
            <div class="chatgpt-card-pill">
                <strong>Private key 3</strong>
                <div class="chatgpt-card-sub">Randomly generated</div>
            </div>
            <div class="chatgpt-card-pill">
                <strong>Private key 4</strong>
                <div class="chatgpt-card-sub">Randomly generated</div>
            </div>
            <div class="chatgpt-card-pill">
                <strong>Private key 5</strong>
                <div class="chatgpt-card-sub">Randomly generated</div>
            </div>
            <div class="chatgpt-card-pill">
                <strong>Private key 6</strong>
                <div class="chatgpt-card-sub">Randomly generated</div>
            </div>
        </div>
        <div class="chatgpt-card-caption">Each private key is generated independently without a common seed.</div>
    </div>
    '''

def card_mod15_deterministic_wallet():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">Deterministic wallet</div>
        <div style="max-width: 680px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px;">
            <div class="chatgpt-card-pill highlight">
                <strong>Random seed</strong>
                <div class="chatgpt-card-sub">One starting value &bull; Cryptographic derivation</div>
            </div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
                <div class="chatgpt-card-pill">Private key 1</div>
                <div class="chatgpt-card-pill">Private key 2</div>
                <div class="chatgpt-card-pill">Private key 3</div>
            </div>
        </div>
        <div class="chatgpt-card-caption">The same seed and derivation procedure can regenerate all keys.</div>
    </div>
    '''

def card_mod15_university_hierarchy():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">Hierarchy Analogy: University Structure</div>
        <div style="max-width: 720px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px;">
            <div class="chatgpt-card-pill highlight"><strong>University</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;">
                <div class="chatgpt-card-pill"><strong>School A</strong></div>
                <div class="chatgpt-card-pill"><strong>School B</strong></div>
            </div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px;">
                <div class="chatgpt-card-pill">Dept A1</div>
                <div class="chatgpt-card-pill">Dept A2</div>
                <div class="chatgpt-card-pill">Dept B1</div>
                <div class="chatgpt-card-pill">Dept B2</div>
            </div>
        </div>
        <div class="chatgpt-card-caption">The university is at the top, schools are below it, and departments are further down.</div>
    </div>
    '''

def card_mod15_hd_tree():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">Hierarchical Deterministic (HD) Key Tree</div>
        <div style="max-width: 720px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px;">
            <div class="chatgpt-card-pill highlight"><strong>Seed</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Master key</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;">
                <div class="chatgpt-card-pill"><strong>Child key A</strong></div>
                <div class="chatgpt-card-pill"><strong>Child key B</strong></div>
            </div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px;">
                <div class="chatgpt-card-pill">Child A1</div>
                <div class="chatgpt-card-pill">Child A2</div>
                <div class="chatgpt-card-pill">Child B1</div>
                <div class="chatgpt-card-pill">Child B2</div>
            </div>
        </div>
        <div class="chatgpt-card-caption">Memory trick: Seed &rarr; Master &rarr; Parent &rarr; Child &rarr; Address.</div>
    </div>
    '''

def card_mod15_recovery_phrase():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">Illustrative recovery phrase format</div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; max-width: 720px; margin: 0 auto;">
            <div class="chatgpt-card-pill">Word 1<div class="chatgpt-card-sub">&bull;&bull;&bull;&bull;&bull;&bull;</div></div>
            <div class="chatgpt-card-pill">Word 2<div class="chatgpt-card-sub">&bull;&bull;&bull;&bull;&bull;&bull;</div></div>
            <div class="chatgpt-card-pill">Word 3<div class="chatgpt-card-sub">&bull;&bull;&bull;&bull;&bull;&bull;</div></div>
            <div class="chatgpt-card-pill">Word 4<div class="chatgpt-card-sub">&bull;&bull;&bull;&bull;&bull;&bull;</div></div>
            <div class="chatgpt-card-pill">Word 5<div class="chatgpt-card-sub">&bull;&bull;&bull;&bull;&bull;&bull;</div></div>
            <div class="chatgpt-card-pill">Word 6<div class="chatgpt-card-sub">&bull;&bull;&bull;&bull;&bull;&bull;</div></div>
            <div class="chatgpt-card-pill">Word 7<div class="chatgpt-card-sub">&bull;&bull;&bull;&bull;&bull;&bull;</div></div>
            <div class="chatgpt-card-pill">Word 8<div class="chatgpt-card-sub">&bull;&bull;&bull;&bull;&bull;&bull;</div></div>
            <div class="chatgpt-card-pill">Word 9<div class="chatgpt-card-sub">&bull;&bull;&bull;&bull;&bull;&bull;</div></div>
            <div class="chatgpt-card-pill">Word 10<div class="chatgpt-card-sub">&bull;&bull;&bull;&bull;&bull;&bull;</div></div>
            <div class="chatgpt-card-pill">Word 11<div class="chatgpt-card-sub">&bull;&bull;&bull;&bull;&bull;&bull;</div></div>
            <div class="chatgpt-card-pill">Word 12<div class="chatgpt-card-sub">&bull;&bull;&bull;&bull;&bull;&bull;</div></div>
        </div>
        <div class="chatgpt-card-caption">This is only a format illustration, not a usable recovery phrase.</div>
    </div>
    '''

# ==============================================================================
# MODULE 16 CARDS
# ==============================================================================

def card_mod16_payment_process():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">Diagram: Bitcoin payment process</div>
        <div style="max-width: 680px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px;">
            <div class="chatgpt-card-pill">
                <strong>Customer selects a product</strong>
                <div class="chatgpt-card-sub">Example: T-shirt worth ₹2,000</div>
            </div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Merchant provides Bitcoin address / QR code</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Customer scans QR code using wallet</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Wallet creates and signs transaction</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Transaction broadcast to Bitcoin network</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Miner includes transaction in a block</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill filled"><strong style="color: #34d399;">Merchant detects payment and processes order</strong></div>
        </div>
    </div>
    '''

def card_mod16_bip21_working():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">4.5 Working of BIP21</div>
        <div style="max-width: 680px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px;">
            <div class="chatgpt-card-pill"><strong>Merchant creates Bitcoin URI</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>URI is converted into QR code or shared as a link</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Customer scans or clicks it</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Bitcoin wallet reads payment details</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill filled"><strong style="color: #34d399;">Customer verifies and sends payment</strong></div>
        </div>
    </div>
    '''

def card_mod16_pos_working():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header left">5.4 Diagram of Bitcoin POS working</div>
        <div style="max-width: 680px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px;">
            <div class="chatgpt-card-pill highlight">
                <div style="font-size: 18px; font-weight: 800; color: #38bdf8;">₹500</div>
                <div class="chatgpt-card-sub">Coffee bill at a restaurant</div>
            </div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>POS terminal calculates Bitcoin amount</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>POS generates receipt and QR code</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Customer scans QR code using wallet</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Customer sends Bitcoin payment</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill filled"><strong style="color: #34d399;">Payment detected and receipt issued</strong></div>
        </div>
    </div>
    '''

def card_mod16_bip70_flow():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">BIP70 Payment Protocol Complete Flow</div>
        <div style="max-width: 680px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; justify-content: space-between; font-weight: 700; color: #a855f7; padding: 4px 10px;">
                <span>Merchant</span>
                <span>Customer wallet</span>
            </div>
            <div style="display: flex; align-items: center; justify-content: space-between; background: #0b0f17; border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; padding: 10px 14px;">
                <span style="color: #c084fc; font-weight: 600;">1. PaymentRequest &rarr;</span>
                <span style="color: #94a3b8; font-size: 12px;">Payment details and certificate information</span>
            </div>
            <div style="display: flex; align-items: center; justify-content: space-between; background: #0b0f17; border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; padding: 10px 14px;">
                <span style="color: #94a3b8; font-size: 12px;">Receives payment message</span>
                <span style="color: #38bdf8; font-weight: 600;">&larr; 2. Payment</span>
            </div>
            <div style="display: flex; align-items: center; justify-content: space-between; background: #0b0f17; border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; padding: 10px 14px;">
                <span style="color: #34d399; font-weight: 600;">3. PaymentACK &rarr;</span>
                <span style="color: #94a3b8; font-size: 12px;">Acknowledgement &amp; memo receipt</span>
            </div>
        </div>
    </div>
    '''

def card_mod16_mitm_attack():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header left">8.2 Man-in-the-Middle (MITM) Address Substitution Attack</div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; max-width: 750px; margin: 0 auto;">
            <div class="chatgpt-card-pill">
                <strong style="color: #38bdf8;">Merchant</strong>
                <div class="chatgpt-card-sub">Genuine payment details</div>
            </div>
            <div class="chatgpt-card-pill" style="border-color: #ef4444; background: rgba(239,68,68,0.08);">
                <strong style="color: #f87171;">Attacker (MITM)</strong>
                <div class="chatgpt-card-sub">Intercepts &amp; replaces merchant address</div>
            </div>
            <div class="chatgpt-card-pill">
                <strong style="color: #fbbf24;">Customer</strong>
                <div class="chatgpt-card-sub">Receives false payment address</div>
            </div>
        </div>
        <div class="chatgpt-card-caption">Illustration of an address-substitution attack. The customer mistakenly believes the attacker-controlled address belongs to the merchant.</div>
    </div>
    '''

# ==============================================================================
# MODULE 17 CARDS
# ==============================================================================

def card_mod17_bip_process():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">BIP Progression Lifecycle</div>
        <div style="max-width: 680px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px;">
            <div class="chatgpt-card-pill"><strong>Problem identified</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Improvement proposed</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>BIP document prepared</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Community discussion and review</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Proposal accepted and adopted</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill filled"><strong style="color: #34d399;">Implementation of improvement</strong></div>
        </div>
    </div>
    '''

def card_mod17_fork_diagram():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header left">3.4 Diagram: Soft fork vs Hard fork</div>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; max-width: 780px; margin: 0 auto;">
            <div style="border: 1px solid #10b981; border-radius: 8px; padding: 14px; background: rgba(16,185,129,0.04);">
                <div style="color: #34d399; font-weight: 700; margin-bottom: 8px;">Soft fork</div>
                <div style="font-size: 12.5px; color: #cbd5e1; line-height: 1.6;">
                    Original blockchain<br>
                    &darr;<br>
                    New, more restrictive rules<br>
                    &darr;<br>
                    <strong style="color: #34d399;">One continuing blockchain</strong> (Backward-compatible)
                </div>
            </div>
            <div style="border: 1px solid #ef4444; border-radius: 8px; padding: 14px; background: rgba(239,68,68,0.04);">
                <div style="color: #f87171; font-weight: 700; margin-bottom: 8px;">Hard fork</div>
                <div style="font-size: 12.5px; color: #cbd5e1; line-height: 1.6;">
                    Original blockchain<br>
                    &darr;<br>
                    Incompatible protocol rules<br>
                    &darr;<br>
                    <span style="color: #94a3b8;">Old chain (Old rules)</span> &bull; <span style="color: #f87171; font-weight: bold;">New chain (New rules)</span>
                </div>
            </div>
        </div>
    </div>
    '''

def card_mod17_xthin_communication():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header left">Example of thin block communication</div>
        <div style="max-width: 720px; margin: 0 auto; display: flex; flex-direction: column; gap: 10px;">
            <div style="background: #090d16; border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; padding: 12px;">
                <div style="font-size: 11px; text-transform: uppercase; color: #94a3b8; font-weight: 700;">Requesting node already has</div>
                <div style="display: flex; gap: 8px; margin-top: 6px; flex-wrap: wrap;">
                    <span class="chatgpt-card-pill" style="padding: 4px 10px; font-size: 12px;">TX1</span>
                    <span class="chatgpt-card-pill" style="padding: 4px 10px; font-size: 12px;">TX2</span>
                    <span class="chatgpt-card-pill" style="padding: 4px 10px; font-size: 12px;">TX3</span>
                    <span class="chatgpt-card-pill" style="padding: 4px 10px; font-size: 12px;">TX4</span>
                </div>
            </div>
            <div style="background: #090d16; border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; padding: 12px;">
                <div style="font-size: 11px; text-transform: uppercase; color: #94a3b8; font-weight: 700;">Miner's block contains</div>
                <div style="display: flex; gap: 8px; margin-top: 6px; flex-wrap: wrap;">
                    <span class="chatgpt-card-pill" style="padding: 4px 10px; font-size: 12px;">TX1</span>
                    <span class="chatgpt-card-pill" style="padding: 4px 10px; font-size: 12px;">TX2</span>
                    <span class="chatgpt-card-pill" style="padding: 4px 10px; font-size: 12px;">TX3</span>
                    <span class="chatgpt-card-pill" style="padding: 4px 10px; font-size: 12px;">TX4</span>
                    <span class="chatgpt-card-pill" style="padding: 4px 10px; font-size: 12px; border-color: #10b981; color: #34d399;">TX5</span>
                    <span class="chatgpt-card-pill" style="padding: 4px 10px; font-size: 12px; border-color: #10b981; color: #34d399;">TX6</span>
                </div>
            </div>
            <div style="background: #18202f; border: 1px solid #0284c7; border-radius: 6px; padding: 12px;">
                <div style="font-size: 11px; text-transform: uppercase; color: #38bdf8; font-weight: 700;">Thin block sends only</div>
                <div style="display: flex; gap: 8px; margin-top: 6px;">
                    <span class="chatgpt-card-pill success" style="padding: 6px 14px; font-size: 13px;">TX5</span>
                    <span class="chatgpt-card-pill success" style="padding: 6px 14px; font-size: 13px;">TX6</span>
                </div>
            </div>
        </div>
    </div>
    '''

def card_mod17_lightning_diagram():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header left">9.6 Diagram: Working of the Lightning Network</div>
        <div style="max-width: 720px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px;">
            <div class="chatgpt-card-pill highlight">
                <strong>Bitcoin main blockchain</strong>
                <div class="chatgpt-card-sub">Layer 1 Base Settlement</div>
            </div>
            <div class="chatgpt-card-arrow">&darr; (Open payment channel &bull; On-chain funding transaction)</div>
            <div style="border: 1px solid #a855f7; border-radius: 8px; padding: 14px; background: rgba(168,85,247,0.06);">
                <div style="color: #c084fc; font-weight: 700; text-align: center; margin-bottom: 8px;">Lightning payment channel (Layer 2)</div>
                <div style="font-size: 11.5px; color: #94a3b8; text-align: center; margin-bottom: 10px;">Multiple instant off-chain payments</div>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
                    <div class="chatgpt-card-pill">Payment 1</div>
                    <div class="chatgpt-card-pill">Payment 2</div>
                    <div class="chatgpt-card-pill">Payment 3</div>
                </div>
            </div>
            <div class="chatgpt-card-arrow">&darr; (Close payment channel &bull; Final settlement transaction)</div>
            <div class="chatgpt-card-pill filled">
                <strong style="color: #34d399;">Final balance recorded on Bitcoin blockchain</strong>
            </div>
        </div>
    </div>
    '''

# ==============================================================================
# MODULE 18 CARDS
# ==============================================================================

def card_mod18_cex_steps():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">Centralized Exchange (CEX) Trading Steps</div>
        <div style="max-width: 680px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px;">
            <div class="chatgpt-card-pill"><strong>Step 1: Create an account</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Step 2: Complete required verification (KYC/AML)</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Step 3: Add funds (Fiat deposit)</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Step 4: Select Bitcoin (Trading pair)</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Step 5: Place an order</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>Step 6: Order matching (Off-chain engine)</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill filled"><strong style="color: #34d399;">Step 7: Bitcoin is credited</strong></div>
        </div>
    </div>
    '''

def card_mod18_long_short_cards():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header">Trading Positions Example</div>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; max-width: 780px; margin: 0 auto;">
            <div style="border: 1px solid #10b981; border-radius: 8px; padding: 14px; background: rgba(16,185,129,0.04);">
                <div style="color: #34d399; font-weight: 700; margin-bottom: 6px;">Long position</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.6;">
                    Buying price: <strong>₹50 L</strong><br>
                    Selling price: <strong>₹55 L</strong><br>
                    <span style="color: #34d399; font-weight: bold;">Price increases &rarr; Profit: ₹5,00,000</span>
                </div>
            </div>
            <div style="border: 1px solid #f59e0b; border-radius: 8px; padding: 14px; background: rgba(245,158,11,0.04);">
                <div style="color: #fbbf24; font-weight: 700; margin-bottom: 6px;">Short position</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.6;">
                    Opening price: <strong>₹50 L</strong><br>
                    Closing price: <strong>₹45 L</strong><br>
                    <span style="color: #fbbf24; font-weight: bold;">Price decreases &rarr; Profit: ₹5,00,000</span>
                </div>
            </div>
        </div>
    </div>
    '''

def card_mod18_order_book_example():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header left">6.3 Example of a Bitcoin order book (BTC/INR)</div>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; max-width: 780px; margin: 0 auto;">
            <div style="border: 1px solid rgba(16,185,129,0.3); border-radius: 8px; padding: 12px; background: rgba(16,185,129,0.03);">
                <div style="font-weight: 700; color: #34d399; margin-bottom: 8px;">Buy orders (Bids) &mdash; BUYERS</div>
                <table style="width: 100%; font-size: 12px; color: #cbd5e1;">
                    <tr style="color: #94a3b8; border-bottom: 1px solid #1e293b;"><th>Price</th><th>Quantity</th></tr>
                    <tr><td style="color: #34d399; font-weight: bold;">₹50,00,000</td><td>0.10 BTC</td></tr>
                    <tr><td style="color: #34d399;">₹49,90,000</td><td>0.20 BTC</td></tr>
                    <tr><td style="color: #34d399;">₹49,80,000</td><td>0.15 BTC</td></tr>
                </table>
            </div>
            <div style="border: 1px solid rgba(239,68,68,0.3); border-radius: 8px; padding: 12px; background: rgba(239,68,68,0.03);">
                <div style="font-weight: 700; color: #f87171; margin-bottom: 8px;">Sell orders (Asks) &mdash; SELLERS</div>
                <table style="width: 100%; font-size: 12px; color: #cbd5e1;">
                    <tr style="color: #94a3b8; border-bottom: 1px solid #1e293b;"><th>Price</th><th>Quantity</th></tr>
                    <tr><td style="color: #f87171; font-weight: bold;">₹50,10,000</td><td>0.12 BTC</td></tr>
                    <tr><td style="color: #f87171;">₹50,20,000</td><td>0.08 BTC</td></tr>
                    <tr><td style="color: #f87171;">₹50,30,000</td><td>0.25 BTC</td></tr>
                </table>
            </div>
        </div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; max-width: 780px; margin: 12px auto 0;">
            <div class="chatgpt-card-pill" style="border-color: #10b981;">Best bid: <strong style="color: #34d399;">₹50,00,000</strong></div>
            <div class="chatgpt-card-pill" style="border-color: #ef4444;">Best ask: <strong style="color: #f87171;">₹50,10,000</strong></div>
            <div class="chatgpt-card-pill" style="border-color: #f59e0b;">Bid-ask spread: <strong style="color: #fbbf24;">₹10,000</strong></div>
        </div>
    </div>
    '''

def card_mod18_market_order_example():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header left">Market Order Immediate Execution Example</div>
        <div style="max-width: 680px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px;">
            <div class="chatgpt-card-pill">
                <strong>Best available ask: ₹50,00,000 (0.01 BTC available)</strong>
            </div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill highlight">
                <strong>Aman places market buy order for 0.01 BTC</strong>
            </div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill filled">
                <strong style="color: #34d399;">Exchange matches order instantly with best ask &rarr; 0.01 BTC purchased at ₹50,00,000</strong>
            </div>
        </div>
        <div class="chatgpt-card-caption">Immediate execution without waiting in the order book.</div>
    </div>
    '''

def card_mod18_complete_working():
    return '''
    <div class="chatgpt-card-box">
        <div class="chatgpt-card-header left">Topic 9: Complete Working &mdash; From Buying Bitcoin to Selling Bitcoin</div>
        <div style="max-width: 680px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px;">
            <div class="chatgpt-card-pill"><strong>1. Deposit money (Fiat INR/USD on-ramp)</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>2. Select cryptocurrency (BTC/INR pair)</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>3. Choose order type (Market vs Limit order)</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>4. Check order book (Review bid, ask, and spread)</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>5. Complete order (Matching engine fills order)</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill"><strong>6. Secure wallet transfer (Withdraw to self-custody cold storage)</strong></div>
            <div class="chatgpt-card-arrow">&darr;</div>
            <div class="chatgpt-card-pill filled"><strong style="color: #34d399;">7. Later selling for fiat (Deposit back to exchange &amp; execute sell order)</strong></div>
        </div>
    </div>
    '''
