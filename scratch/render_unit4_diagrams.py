# -*- coding: utf-8 -*-
"""
Self-contained HTML/SVG visual diagrams generator for Blockchain Unit IV (Modules 14 to 18)
Matches the sleek dark UI theme and renders flawlessly without external dependencies.
"""

def icon_server():
    return '''<svg class="diagram-node-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect>
  <rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect>
  <line x1="6" y1="6" x2="6.01" y2="6"></line>
  <line x1="6" y1="18" x2="6.01" y2="18"></line>
</svg>'''

def icon_user():
    return '''<svg class="diagram-node-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
  <circle cx="12" cy="7" r="4"></circle>
</svg>'''

def icon_shield():
    return '''<svg class="diagram-node-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
</svg>'''

def icon_cpu():
    return '''<svg class="diagram-node-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect>
  <rect x="9" y="9" width="6" height="6"></rect>
  <line x1="9" y1="1" x2="9" y2="4"></line>
  <line x1="15" y1="1" x2="15" y2="4"></line>
  <line x1="9" y1="20" x2="9" y2="23"></line>
  <line x1="15" y1="20" x2="15" y2="23"></line>
  <line x1="20" y1="9" x2="23" y2="9"></line>
  <line x1="20" y1="14" x2="23" y2="14"></line>
  <line x1="1" y1="9" x2="4" y2="9"></line>
  <line x1="1" y1="14" x2="4" y2="14"></line>
</svg>'''

def icon_key():
    return '''<svg class="diagram-node-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="7.5" cy="15.5" r="5.5"></circle>
  <path d="m21 2-9.6 9.6"></path>
  <path d="m15.5 7.5 3 3L22 7l-3-3"></path>
</svg>'''

def icon_bolt():
    return '''<svg class="diagram-node-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
</svg>'''

def icon_wallet():
    return '''<svg class="diagram-node-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M21 12V7H5a2 2 0 0 1 0-4h14v4"></path>
  <path d="M3 5v14a2 2 0 0 0 2 2h16v-5"></path>
  <path d="M18 12a2 2 0 0 0 0 4h4v-4z"></path>
</svg>'''

def icon_chart():
    return '''<svg class="diagram-node-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <line x1="18" y1="20" x2="18" y2="10"></line>
  <line x1="12" y1="20" x2="12" y2="4"></line>
  <line x1="6" y1="20" x2="6" y2="14"></line>
</svg>'''

# ==============================================================================
# MODULE 14 DIAGRAMS
# ==============================================================================

def diagram_p2p_handshake():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">Bitcoin P2P Handshake Protocol Flow</h4>
            <div class="diagram-subtitle">Two-way version / verack exchange establishing a peer connection</div>
        </div>
        <div class="diagram-nodes-row" style="justify-content: space-around; align-items: center;">
            <div class="diagram-node primary" style="flex: 1; max-width: 240px;">
                {icon_server()}
                <div class="diagram-node-title">Node A (Initiator)</div>
                <div class="diagram-node-desc">Client node connecting to peer</div>
            </div>
            <div style="flex: 2; padding: 0 15px; display: flex; flex-direction: column; gap: 14px;">
                <div style="display: flex; align-items: center; justify-content: space-between; background: rgba(56, 189, 248, 0.08); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 8px; padding: 8px 12px;">
                    <span style="font-family: monospace; font-weight: bold; color: #38bdf8;">1. version &rarr;</span>
                    <span style="font-size: 11.5px; color: #94a3b8;">Proto ver, block height, IP, timestamp</span>
                </div>
                <div style="display: flex; align-items: center; justify-content: space-between; background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 8px; padding: 8px 12px;">
                    <span style="font-size: 11.5px; color: #94a3b8;">Peer version info &amp; capabilities</span>
                    <span style="font-family: monospace; font-weight: bold; color: #34d399;">&larr; 2. version</span>
                </div>
                <div style="display: flex; align-items: center; justify-content: space-between; background: rgba(168, 85, 247, 0.08); border: 1px solid rgba(168, 85, 247, 0.25); border-radius: 8px; padding: 8px 12px;">
                    <span style="font-size: 11.5px; color: #94a3b8;">Peer acknowledges Node A version</span>
                    <span style="font-family: monospace; font-weight: bold; color: #c084fc;">&larr; 3. verack</span>
                </div>
                <div style="display: flex; align-items: center; justify-content: space-between; background: rgba(234, 179, 8, 0.08); border: 1px solid rgba(234, 179, 8, 0.25); border-radius: 8px; padding: 8px 12px;">
                    <span style="font-family: monospace; font-weight: bold; color: #facc15;">4. verack &rarr;</span>
                    <span style="font-size: 11.5px; color: #94a3b8;">Node A acknowledges; handshake complete!</span>
                </div>
            </div>
            <div class="diagram-node success" style="flex: 1; max-width: 240px;">
                {icon_server()}
                <div class="diagram-node-title">Node B (Responder)</div>
                <div class="diagram-node-desc">Remote Bitcoin full peer</div>
            </div>
        </div>
        <div class="diagram-footer" style="margin-top: 14px; font-size: 12.5px; color: #94a3b8; text-align: center;">
            💡 After the 4-step handshake succeeds, both nodes can safely exchange <code>inv</code>, <code>getdata</code>, <code>tx</code>, and <code>block</code> payloads.
        </div>
    </div>
    '''

def diagram_full_vs_spv():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">Full Node vs. SPV Lightweight Node Architecture</h4>
            <div class="diagram-subtitle">Comparing complete consensus verification with lightweight header-only verification</div>
        </div>
        <div class="diagram-nodes-row" style="gap: 20px;">
            <div class="diagram-node" style="flex: 1; min-width: 280px; text-align: left; background: #0f172a; border-color: #0284c7;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 8px;">
                    {icon_server()}
                    <span style="font-weight: 700; color: #38bdf8; font-size: 15px;">Full Node (Core Backbone)</span>
                </div>
                <ul style="margin: 0; padding-left: 18px; font-size: 13px; color: #cbd5e1; line-height: 1.6;">
                    <li><strong>Full Chain Storage:</strong> Stores 100% of historical blocks (~550+ GB).</li>
                    <li><strong>Full Rule Validation:</strong> Validates every signature, UTXO, and consensus rule autonomously.</li>
                    <li><strong>Zero Trust:</strong> Relies on no third party or centralized service.</li>
                    <li><strong>Resource Demands:</strong> Requires high bandwidth, storage &amp; CPU.</li>
                </ul>
            </div>
            <div class="diagram-node" style="flex: 1; min-width: 280px; text-align: left; background: #0f172a; border-color: #10b981;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 8px;">
                    {icon_user()}
                    <span style="font-weight: 700; color: #34d399; font-size: 15px;">SPV Lightweight Node (BIP37)</span>
                </div>
                <ul style="margin: 0; padding-left: 18px; font-size: 13px; color: #cbd5e1; line-height: 1.6;">
                    <li><strong>Headers Only:</strong> Downloads only 80-byte block headers (~50 MB total).</li>
                    <li><strong>Merkle Branch Verification:</strong> Verifies transaction inclusion via O(log N) Merkle paths.</li>
                    <li><strong>Honest Majority Assumption:</strong> Trusts the chain with most accumulated PoW.</li>
                    <li><strong>Ideal for Mobile:</strong> Lightweight, runs comfortably on smartphones &amp; IoT.</li>
                </ul>
            </div>
        </div>
    </div>
    '''

def diagram_inv_propagation():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">Bitcoin Inventory Gossip &amp; Data Propagation Flow</h4>
            <div class="diagram-subtitle">How new transactions and blocks propagate across the peer-to-peer network</div>
        </div>
        <div class="diagram-flow-row">
            <div class="flow-step-card">
                <div class="flow-step-num">Step 1</div>
                <div class="flow-step-title">inv Announcement</div>
                <div class="flow-step-desc">Node A broadcasts <code>inv</code> containing SHA-256 hashes of new transactions or blocks.</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step-card">
                <div class="flow-step-num">Step 2</div>
                <div class="flow-step-title">Mempool Lookup</div>
                <div class="flow-step-desc">Node B checks its mempool/ledger; checks if it already possesses these hashes.</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step-card">
                <div class="flow-step-num">Step 3</div>
                <div class="flow-step-title">getdata Request</div>
                <div class="flow-step-desc">For any missing items, Node B sends a <code>getdata</code> message requesting the full payload.</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step-card">
                <div class="flow-step-num">Step 4</div>
                <div class="flow-step-title">tx / block Delivery</div>
                <div class="flow-step-desc">Node A transmits full <code>tx</code> or <code>block</code> data; Node B validates and relays.</div>
            </div>
        </div>
    </div>
    '''

def diagram_ibd_comparison():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">Initial Block Download (IBD): Headers-First vs Blocks-First</h4>
            <div class="diagram-subtitle">Modern parallel headers-first synchronization vs legacy sequential downloading</div>
        </div>
        <div class="diagram-nodes-row" style="gap: 16px;">
            <div class="diagram-node" style="flex: 1; text-align: left; background: rgba(239, 68, 68, 0.05); border-color: rgba(239, 68, 68, 0.3);">
                <div style="font-weight: 700; color: #f87171; margin-bottom: 8px;">Legacy: Blocks-First Download</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.5;">
                    Downloads full blocks sequentially one by one from a single peer. If a peer stalls or delivers an invalid block, sync freezes and resources are wasted.
                </div>
            </div>
            <div class="diagram-node" style="flex: 1; text-align: left; background: rgba(16, 185, 129, 0.05); border-color: rgba(16, 185, 129, 0.3);">
                <div style="font-weight: 700; color: #34d399; margin-bottom: 8px;">Modern: Headers-First Download</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.5;">
                    Phase 1: Rapidly downloads all 80-byte block headers to validate the longest PoW chain.<br>
                    Phase 2: Downloads full block bodies in <strong>parallel</strong> across dozens of peers simultaneously!
                </div>
            </div>
        </div>
    </div>
    '''

def diagram_stratum_pool():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">Mining Pool Architecture &amp; Stratum Protocol</h4>
            <div class="diagram-subtitle">How thousands of ASICs collaborate through a pool coordinator without running full nodes</div>
        </div>
        <div class="diagram-nodes-row" style="justify-content: space-around; align-items: center;">
            <div class="diagram-node" style="flex: 1; max-width: 220px; background: #0f172a;">
                {icon_cpu()}
                <div class="diagram-node-title">Mining Rig (ASIC)</div>
                <div class="diagram-node-desc">Executes fast hashing; submits shares over Stratum JSON-RPC</div>
            </div>
            <div style="display: flex; flex-direction: column; align-items: center; gap: 4px;">
                <span style="font-size: 11.5px; font-weight: bold; color: #38bdf8; background: rgba(56, 189, 248, 0.1); padding: 3px 8px; border-radius: 12px;">Stratum Protocol</span>
                <span style="font-size: 20px; color: #64748b;">&harr;</span>
                <span style="font-size: 11px; color: #94a3b8;">mining.notify / submit</span>
            </div>
            <div class="diagram-node primary" style="flex: 1; max-width: 240px;">
                {icon_server()}
                <div class="diagram-node-title">Pool Server Coordinator</div>
                <div class="diagram-node-desc">Constructs candidate block, validates shares, distributes coinbase reward</div>
            </div>
            <div style="display: flex; flex-direction: column; align-items: center; gap: 4px;">
                <span style="font-size: 11.5px; font-weight: bold; color: #34d399; background: rgba(16, 185, 129, 0.1); padding: 3px 8px; border-radius: 12px;">Bitcoin P2P</span>
                <span style="font-size: 20px; color: #64748b;">&rarr;</span>
                <span style="font-size: 11px; color: #94a3b8;">broadcast block</span>
            </div>
            <div class="diagram-node success" style="flex: 1; max-width: 220px;">
                {icon_shield()}
                <div class="diagram-node-title">Bitcoin Network</div>
                <div class="diagram-node-desc">Global decentralized nodes accept newly minted block</div>
            </div>
        </div>
    </div>
    '''

# ==============================================================================
# MODULE 15 DIAGRAMS
# ==============================================================================

def diagram_key_address_pipeline():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">Bitcoin Key &amp; Address Derivation Pipeline</h4>
            <div class="diagram-subtitle">From a 256-bit private key to a Base58Check legacy P2PKH address</div>
        </div>
        <div class="diagram-flow-row" style="flex-wrap: wrap;">
            <div class="flow-step-card" style="min-width: 170px;">
                <div class="flow-step-num">Step 1</div>
                <div class="flow-step-title">Private Key ($k$)</div>
                <div class="flow-step-desc">256-bit cryptographically secure random integer</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step-card" style="min-width: 170px;">
                <div class="flow-step-num">Step 2: ECDSA</div>
                <div class="flow-step-title">Public Key ($K$)</div>
                <div class="flow-step-desc">Elliptic Curve point multiplication: K = k &times; G (secp256k1)</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step-card" style="min-width: 170px;">
                <div class="flow-step-num">Step 3: Hash160</div>
                <div class="flow-step-title">Public Key Hash</div>
                <div class="flow-step-desc">RIPEMD160(SHA256(K)) produces 160-bit fingerprint</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step-card" style="min-width: 170px;">
                <div class="flow-step-num">Step 4: Base58Check</div>
                <div class="flow-step-title">Bitcoin Address</div>
                <div class="flow-step-desc">Prefix <code>0x00</code> + 4-byte SHA256 checksum &rarr; <code>1A1z...</code></div>
            </div>
        </div>
    </div>
    '''

def diagram_jbok_vs_hd():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">JBOK (Random) vs. Hierarchical Deterministic (HD BIP32/BIP44) Wallets</h4>
            <div class="diagram-subtitle">Single master seed backup vs hazardous independent random keys</div>
        </div>
        <div class="diagram-nodes-row" style="gap: 20px;">
            <div class="diagram-node" style="flex: 1; text-align: left; background: #0f172a; border-color: #ef4444;">
                <div style="font-weight: 700; color: #f87171; font-size: 15px; margin-bottom: 8px;">
                    JBOK / Type 0 (Just a Bunch of Keys)
                </div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.55;">
                    • Every key pair is generated randomly from independent entropy.<br>
                    • If a user creates 100 addresses, 100 independent private keys exist.<br>
                    • ⚠️ <strong>Dangerous:</strong> Wallet must be backed up after every transaction or address generation, or new funds are lost forever!
                </div>
            </div>
            <div class="diagram-node" style="flex: 1; text-align: left; background: #0f172a; border-color: #0284c7;">
                <div style="font-weight: 700; color: #38bdf8; font-size: 15px; margin-bottom: 8px;">
                    HD Wallet / Type 2 (BIP32 / BIP44 Standard)
                </div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.55;">
                    • <strong>One Master Seed:</strong> Derives an infinite mathematical tree of keys.<br>
                    • Derivation path: <code>m / purpose' / coin_type' / account' / change / index</code><br>
                    • ✅ <strong>Safe &amp; Easy:</strong> Backing up the single 12/24-word seed phrase restores all past, current, and future addresses automatically!
                </div>
            </div>
        </div>
    </div>
    '''

def diagram_bip39_seed():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">BIP39 Mnemonic Seed Phrase Generation Flow</h4>
            <div class="diagram-subtitle">Translating raw computer entropy into 12 to 24 human-readable English words</div>
        </div>
        <div class="diagram-flow-row">
            <div class="flow-step-card">
                <div class="flow-step-num">Step 1</div>
                <div class="flow-step-title">True Entropy</div>
                <div class="flow-step-desc">Generate 128 to 256 bits of cryptographically secure random data.</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step-card">
                <div class="flow-step-num">Step 2</div>
                <div class="flow-step-title">Checksum</div>
                <div class="flow-step-desc">Compute SHA-256 of entropy; append first 4 to 8 bits as checksum.</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step-card">
                <div class="flow-step-num">Step 3</div>
                <div class="flow-step-title">Word Mapping</div>
                <div class="flow-step-desc">Divide into 11-bit chunks; map each integer to BIP39 dictionary (2048 words).</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step-card">
                <div class="flow-step-num">Step 4</div>
                <div class="flow-step-title">Master 512-bit Seed</div>
                <div class="flow-step-desc">Run PBKDF2 (HMAC-SHA512 with 2048 rounds) with optional passphrase &rarr; Seed!</div>
            </div>
        </div>
    </div>
    '''

def diagram_utxo_change():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">UTXO Transaction Selection &amp; Change Address Mechanism</h4>
            <div class="diagram-subtitle">Unspent transaction outputs must be spent in their entirety</div>
        </div>
        <div class="diagram-nodes-row" style="justify-content: space-around; align-items: center;">
            <div class="diagram-node" style="flex: 1; max-width: 220px; background: rgba(56, 189, 248, 0.05); border-color: #0284c7;">
                <div style="font-weight: 700; color: #38bdf8; margin-bottom: 6px;">Inputs (UTXOs Spent)</div>
                <div style="font-size: 12.5px; color: #cbd5e1; line-height: 1.5;">
                    UTXO #1: <strong>0.80 BTC</strong><br>
                    UTXO #2: <strong>0.50 BTC</strong><br>
                    <hr style="border: none; border-top: 1px dashed rgba(255,255,255,0.2); margin: 6px 0;">
                    Total In: <span style="color: #38bdf8; font-weight: bold;">1.3000 BTC</span>
                </div>
            </div>
            <div style="font-size: 24px; color: #64748b;">&rarr;</div>
            <div class="diagram-node primary" style="flex: 1; max-width: 200px;">
                {icon_wallet()}
                <div class="diagram-node-title">Transaction Engine</div>
                <div class="diagram-node-desc">ECDSA signature unlocking scripts validated</div>
            </div>
            <div style="font-size: 24px; color: #64748b;">&rarr;</div>
            <div class="diagram-node" style="flex: 1; max-width: 260px; background: rgba(16, 185, 129, 0.05); border-color: #10b981;">
                <div style="font-weight: 700; color: #34d399; margin-bottom: 6px;">Outputs (New UTXOs)</div>
                <div style="font-size: 12.5px; color: #cbd5e1; line-height: 1.5;">
                    1. Recipient: <strong>1.0000 BTC</strong><br>
                    2. Change Address: <strong>0.2995 BTC</strong><br>
                    3. Miner Fee: <strong>0.0005 BTC</strong><br>
                    <hr style="border: none; border-top: 1px dashed rgba(255,255,255,0.2); margin: 6px 0;">
                    Total Out: <span style="color: #34d399; font-weight: bold;">1.3000 BTC</span>
                </div>
            </div>
        </div>
    </div>
    '''

# ==============================================================================
# MODULE 16 DIAGRAMS
# ==============================================================================

def diagram_pos_qr_flow():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">Point-of-Sale (POS) System &amp; BIP21 QR Code Payment Flow</h4>
            <div class="diagram-subtitle">From customer checkout counter to peer-to-peer network confirmation</div>
        </div>
        <div class="diagram-flow-row">
            <div class="flow-step-card">
                <div class="flow-step-num">Step 1</div>
                <div class="flow-step-title">POS Invoice</div>
                <div class="flow-step-desc">Merchant registers purchase; POS calculates real-time BTC amount and generates BIP21 URI.</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step-card">
                <div class="flow-step-num">Step 2</div>
                <div class="flow-step-title">QR Code Scan</div>
                <div class="flow-step-desc">Customer scans QR with smartphone wallet; address, exact amount, and label auto-populate.</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step-card">
                <div class="flow-step-num">Step 3</div>
                <div class="flow-step-title">Signing &amp; Broadcast</div>
                <div class="flow-step-desc">Customer reviews details, signs transaction with private key, and broadcasts to network.</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step-card">
                <div class="flow-step-num">Step 4</div>
                <div class="flow-step-title">POS Confirmation</div>
                <div class="flow-step-desc">POS node detects transaction in mempool / first block confirmation &amp; prints receipt!</div>
            </div>
        </div>
    </div>
    '''

def diagram_payment_processor():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">Merchant Payment Processor Architecture (Volatility Shield)</h4>
            <div class="diagram-subtitle">How gateways insulate merchants from cryptocurrency market volatility</div>
        </div>
        <div class="diagram-nodes-row" style="justify-content: space-around; align-items: center;">
            <div class="diagram-node" style="flex: 1; max-width: 220px;">
                {icon_user()}
                <div class="diagram-node-title">Customer</div>
                <div class="diagram-node-desc">Pays 0.0025 BTC from mobile wallet</div>
            </div>
            <div style="font-size: 22px; color: #38bdf8;">&rarr; <span style="font-size: 11px; display: block; color: #94a3b8;">BTC Transfer</span></div>
            <div class="diagram-node primary" style="flex: 1; max-width: 250px;">
                {icon_server()}
                <div class="diagram-node-title">Payment Gateway (BitPay)</div>
                <div class="diagram-node-desc">Locks exchange rate (15 min), converts BTC &rarr; Fiat, manages liquidity</div>
            </div>
            <div style="font-size: 22px; color: #10b981;">&rarr; <span style="font-size: 11px; display: block; color: #94a3b8;">Bank Settlement</span></div>
            <div class="diagram-node success" style="flex: 1; max-width: 220px;">
                {icon_server()}
                <div class="diagram-node-title">Merchant Bank</div>
                <div class="diagram-node-desc">Receives guaranteed fiat ($150 USD) with zero volatility risk!</div>
            </div>
        </div>
    </div>
    '''

def diagram_bip70_protocol():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">BIP70 Payment Protocol 3-Step Architecture</h4>
            <div class="diagram-subtitle">Secure, authenticated end-to-end checkout protocol preventing address spoofing</div>
        </div>
        <div class="diagram-nodes-row" style="justify-content: space-around; align-items: center;">
            <div class="diagram-node primary" style="flex: 1; max-width: 240px;">
                {icon_user()}
                <div class="diagram-node-title">Customer Wallet</div>
                <div class="diagram-node-desc">BIP70-compatible Bitcoin wallet</div>
            </div>
            <div style="flex: 2; padding: 0 15px; display: flex; flex-direction: column; gap: 14px;">
                <div style="display: flex; align-items: center; justify-content: space-between; background: rgba(56, 189, 248, 0.08); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 8px; padding: 8px 12px;">
                    <span style="font-size: 11.5px; color: #94a3b8;">1. Fetch payment URL</span>
                    <span style="font-family: monospace; font-weight: bold; color: #38bdf8;">GET /invoice &rarr;</span>
                </div>
                <div style="display: flex; align-items: center; justify-content: space-between; background: rgba(168, 85, 247, 0.08); border: 1px solid rgba(168, 85, 247, 0.25); border-radius: 8px; padding: 8px 12px;">
                    <span style="font-family: monospace; font-weight: bold; color: #c084fc;">&larr; PaymentRequest</span>
                    <span style="font-size: 11.5px; color: #94a3b8;">X.509 cert, merchant name, outputs, expiry</span>
                </div>
                <div style="display: flex; align-items: center; justify-content: space-between; background: rgba(234, 179, 8, 0.08); border: 1px solid rgba(234, 179, 8, 0.25); border-radius: 8px; padding: 8px 12px;">
                    <span style="font-size: 11.5px; color: #94a3b8;">Signed tx + refund address</span>
                    <span style="font-family: monospace; font-weight: bold; color: #facc15;">Payment &rarr;</span>
                </div>
                <div style="display: flex; align-items: center; justify-content: space-between; background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 8px; padding: 8px 12px;">
                    <span style="font-family: monospace; font-weight: bold; color: #34d399;">&larr; PaymentACK</span>
                    <span style="font-size: 11.5px; color: #94a3b8;">Official cryptographic receipt &amp; memo</span>
                </div>
            </div>
            <div class="diagram-node success" style="flex: 1; max-width: 240px;">
                {icon_server()}
                <div class="diagram-node-title">Merchant Server</div>
                <div class="diagram-node-desc">Verified legal business entity</div>
            </div>
        </div>
    </div>
    '''

def diagram_mitm_prevention():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">MITM Attack Prevention: Plain Address vs. X.509 Signed BIP70</h4>
            <div class="diagram-subtitle">Cryptographic public key infrastructure guarantees payment recipient identity</div>
        </div>
        <div class="diagram-nodes-row" style="gap: 20px;">
            <div class="diagram-node" style="flex: 1; text-align: left; background: rgba(239, 68, 68, 0.05); border-color: #ef4444;">
                <div style="font-weight: 700; color: #f87171; font-size: 15px; margin-bottom: 8px;">
                    ❌ Without BIP70 (Raw Bitcoin Address)
                </div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.55;">
                    • Attacker intercepts insecure HTTP link or tampers with clipboard/DNS.<br>
                    • Attacker swaps merchant address with attacker's address.<br>
                    • Customer wallet has no way to verify identity &rarr; <strong>Funds stolen!</strong>
                </div>
            </div>
            <div class="diagram-node" style="flex: 1; text-align: left; background: rgba(16, 185, 129, 0.05); border-color: #10b981;">
                <div style="font-weight: 700; color: #34d399; font-size: 15px; margin-bottom: 8px;">
                    ✅ With BIP70 (X.509 PKI Authenticated)
                </div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.55;">
                    • PaymentRequest is signed with merchant's trusted SSL/TLS Certificate.<br>
                    • If attacker alters address, cryptographic signature check fails.<br>
                    • Wallet displays: <span style="color: #34d399; font-weight: bold;">🔒 Verified Merchant Name</span> &rarr; <strong>100% Protected!</strong>
                </div>
            </div>
        </div>
    </div>
    '''

# ==============================================================================
# MODULE 17 DIAGRAMS
# ==============================================================================

def diagram_soft_vs_hard_fork():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">Soft Fork vs. Hard Fork Compatibility Diagram</h4>
            <div class="diagram-subtitle">Comparing rule restrictions (backward-compatible) vs rule expansions (network split risk)</div>
        </div>
        <div class="diagram-nodes-row" style="gap: 20px;">
            <div class="diagram-node" style="flex: 1; text-align: left; background: #0f172a; border-color: #10b981;">
                <div style="font-weight: 700; color: #34d399; font-size: 15px; margin-bottom: 8px;">
                    Soft Fork (Forward &amp; Backward Compatible)
                </div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.55;">
                    • <strong>Tightens / Restricts Rules:</strong> The set of valid blocks shrinks.<br>
                    • Unupgraded legacy nodes still accept new blocks as valid.<br>
                    • No network split occurs as long as majority hash power upgrades.<br>
                    • Examples: P2SH (BIP16), SegWit (BIP141), Taproot (BIP341).
                </div>
            </div>
            <div class="diagram-node" style="flex: 1; text-align: left; background: #0f172a; border-color: #ef4444;">
                <div style="font-weight: 700; color: #f87171; font-size: 15px; margin-bottom: 8px;">
                    Hard Fork (Backward Incompatible)
                </div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.55;">
                    • <strong>Loosens / Alters Rules:</strong> Previously invalid blocks become valid.<br>
                    • Unupgraded legacy nodes reject the new blocks as invalid.<br>
                    • Creates a permanent chain split unless 100% of nodes upgrade.<br>
                    • Examples: Bitcoin Cash (8MB limit), Bitcoin Gold (Equihash).
                </div>
            </div>
        </div>
    </div>
    '''

def diagram_segwit_block():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">Segregated Witness (SegWit BIP141) Architecture</h4>
            <div class="diagram-subtitle">Separating witness data from the transaction tree eliminates malleability and expands capacity</div>
        </div>
        <div class="diagram-nodes-row" style="gap: 20px;">
            <div class="diagram-node" style="flex: 1; text-align: left; background: #0f172a; border-color: #64748b;">
                <div style="font-weight: 700; color: #94a3b8; font-size: 15px; margin-bottom: 8px;">
                    Legacy Bitcoin Block (1 MB Limit)
                </div>
                <div style="background: rgba(255,255,255,0.05); border-radius: 6px; padding: 10px; margin-bottom: 8px; font-size: 12px; font-family: monospace;">
                    [Tx Data + ScriptSig (Signatures) Inseparably Mixed]<br>
                    &bull; Max Block Size: 1,000,000 bytes<br>
                    &bull; TxID calculated over ScriptSig &rarr; Malleable!
                </div>
            </div>
            <div class="diagram-node" style="flex: 1; text-align: left; background: #0f172a; border-color: #0284c7;">
                <div style="font-weight: 700; color: #38bdf8; font-size: 15px; margin-bottom: 8px;">
                    SegWit Block (4 Million Weight Units Limit)
                </div>
                <div style="background: rgba(2, 132, 199, 0.1); border: 1px solid rgba(2, 132, 199, 0.3); border-radius: 6px; padding: 10px; margin-bottom: 8px; font-size: 12px; font-family: monospace;">
                    [Base Transaction Data] (4 WU / byte)<br>
                    [Detached Witness Structure] (1 WU / byte)<br>
                    &bull; Non-malleable TxIDs &bull; Enables Lightning &bull; bc1 Bech32
                </div>
            </div>
        </div>
    </div>
    '''

def diagram_lightning_lifecycle():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">Lightning Network Layer-2: 3-Stage Payment Lifecycle</h4>
            <div class="diagram-subtitle">High-speed, low-fee bidirectional payment channels anchored to the blockchain</div>
        </div>
        <div class="diagram-flow-row">
            <div class="flow-step-card">
                <div class="flow-step-num">Stage 1 (On-Chain)</div>
                <div class="flow-step-title">Funding Transaction</div>
                <div class="flow-step-desc">Alice &amp; Bob deposit funds into a 2-of-2 multisig channel address recorded on the main blockchain.</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step-card">
                <div class="flow-step-num">Stage 2 (Off-Chain)</div>
                <div class="flow-step-title">Instant Micropayments</div>
                <div class="flow-step-desc">Peers exchange signed commitment transactions and HTLCs off-chain. Sub-second speed, zero network fees!</div>
            </div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step-card">
                <div class="flow-step-num">Stage 3 (On-Chain)</div>
                <div class="flow-step-title">Settlement Transaction</div>
                <div class="flow-step-desc">When closing the channel, the single final net balance is published to Bitcoin blockchain, distributing funds.</div>
            </div>
        </div>
    </div>
    '''

# ==============================================================================
# MODULE 18 DIAGRAMS
# ==============================================================================

def diagram_cex_vs_dex():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">Centralized Exchange (CEX) vs. Decentralized Exchange (DEX)</h4>
            <div class="diagram-subtitle">Comparing custodial order matching platforms with non-custodial smart contract protocols</div>
        </div>
        <div class="diagram-nodes-row" style="gap: 20px;">
            <div class="diagram-node" style="flex: 1; text-align: left; background: #0f172a; border-color: #0284c7;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 8px;">
                    {icon_server()}
                    <span style="font-weight: 700; color: #38bdf8; font-size: 15px;">Centralized Exchange (CEX)</span>
                </div>
                <ul style="margin: 0; padding-left: 18px; font-size: 13px; color: #cbd5e1; line-height: 1.6;">
                    <li><strong>Custody:</strong> Platform holds users' private keys (custodial).</li>
                    <li><strong>Order Matching:</strong> Off-chain high-frequency order books.</li>
                    <li><strong>Fiat Support:</strong> Direct bank transfers, credit cards &amp; fiat pairs.</li>
                    <li><strong>KYC:</strong> Identity verification required by regulatory authorities.</li>
                </ul>
            </div>
            <div class="diagram-node" style="flex: 1; text-align: left; background: #0f172a; border-color: #10b981;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 8px;">
                    {icon_shield()}
                    <span style="font-weight: 700; color: #34d399; font-size: 15px;">Decentralized Exchange (DEX)</span>
                </div>
                <ul style="margin: 0; padding-left: 18px; font-size: 13px; color: #cbd5e1; line-height: 1.6;">
                    <li><strong>Self-Custody:</strong> Users trade directly from their personal wallets.</li>
                    <li><strong>Settlement:</strong> Executed through smart contracts or atomic swaps.</li>
                    <li><strong>Privacy &amp; Censorship:</strong> No central point of control or KYC requirement.</li>
                    <li><strong>Counterparty Risk:</strong> Immune to exchange insolvency/exit scams.</li>
                </ul>
            </div>
        </div>
    </div>
    '''

def diagram_long_vs_short():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">Long Position vs. Short Position Mechanics</h4>
            <div class="diagram-subtitle">How traders profit from bullish rising markets vs bearish declining markets</div>
        </div>
        <div class="diagram-nodes-row" style="gap: 20px;">
            <div class="diagram-node" style="flex: 1; text-align: left; background: rgba(16, 185, 129, 0.05); border-color: #10b981;">
                <div style="font-weight: 700; color: #34d399; font-size: 15px; margin-bottom: 8px;">
                    📈 Long Position (Bullish Strategy)
                </div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.55;">
                    1. Buy Bitcoin at <strong>$60,000</strong>.<br>
                    2. Price increases to <strong>$65,000</strong>.<br>
                    3. Sell Bitcoin at higher price.<br>
                    &bull; <strong>Net Profit:</strong> <span style="color: #34d399; font-weight: bold;">+$5,000</span>
                </div>
            </div>
            <div class="diagram-node" style="flex: 1; text-align: left; background: rgba(239, 68, 68, 0.05); border-color: #ef4444;">
                <div style="font-weight: 700; color: #f87171; font-size: 15px; margin-bottom: 8px;">
                    📉 Short Position (Bearish Strategy)
                </div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.55;">
                    1. Borrow 1 BTC and sell immediately at <strong>$60,000</strong>.<br>
                    2. Price falls to <strong>$55,000</strong>.<br>
                    3. Buy back 1 BTC for $55,000 and return to lender.<br>
                    &bull; <strong>Net Profit:</strong> <span style="color: #34d399; font-weight: bold;">+$5,000</span>
                </div>
            </div>
        </div>
    </div>
    '''

def diagram_order_book():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">Bitcoin Order Book &amp; Bid-Ask Spread Structure</h4>
            <div class="diagram-subtitle">Real-time matching engine ledger of limit buy orders (bids) and limit sell orders (asks)</div>
        </div>
        <div style="max-width: 550px; margin: 0 auto; background: #0f172a; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); padding: 16px;">
            <div style="display: flex; justify-content: space-between; font-weight: bold; font-size: 12px; color: #94a3b8; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 6px; margin-bottom: 8px;">
                <span>Type</span>
                <span>Price (USD)</span>
                <span>Amount (BTC)</span>
                <span>Total</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-family: monospace; font-size: 13px; color: #f87171; padding: 3px 0;">
                <span>Ask</span><span>$64,250</span><span>1.20 BTC</span><span>$77,100</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-family: monospace; font-size: 13px; color: #f87171; padding: 3px 0;">
                <span>Ask</span><span>$64,200</span><span>2.50 BTC</span><span>$160,500</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-family: monospace; font-size: 13px; color: #f87171; padding: 3px 0; background: rgba(239,68,68,0.1); border-radius: 4px;">
                <span><strong>Best Ask</strong></span><span><strong>$64,150</strong></span><span>0.80 BTC</span><span>$51,320</span>
            </div>
            <div style="display: flex; align-items: center; justify-content: center; gap: 8px; margin: 10px 0; padding: 6px; background: rgba(56, 189, 248, 0.12); border: 1px dashed rgba(56, 189, 248, 0.4); border-radius: 6px;">
                <span style="font-size: 12px; font-weight: bold; color: #38bdf8;">Bid-Ask Spread = Ask ($64,150) &minus; Bid ($64,100) = $50.00</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-family: monospace; font-size: 13px; color: #34d399; padding: 3px 0; background: rgba(16,185,129,0.1); border-radius: 4px;">
                <span><strong>Best Bid</strong></span><span><strong>$64,100</strong></span><span>1.50 BTC</span><span>$96,150</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-family: monospace; font-size: 13px; color: #34d399; padding: 3px 0;">
                <span>Bid</span><span>$64,050</span><span>3.00 BTC</span><span>$192,150</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-family: monospace; font-size: 13px; color: #34d399; padding: 3px 0;">
                <span>Bid</span><span>$64,000</span><span>5.20 BTC</span><span>$332,800</span>
            </div>
        </div>
    </div>
    '''

def diagram_order_types():
    return f'''
    <div class="diagram-box">
        <div class="diagram-header">
            <h4 class="diagram-title">Market Order vs. Limit Order Execution Flow</h4>
            <div class="diagram-subtitle">Comparing immediate liquidity taker execution with resting maker order placement</div>
        </div>
        <div class="diagram-nodes-row" style="gap: 20px;">
            <div class="diagram-node" style="flex: 1; text-align: left; background: #0f172a; border-color: #f59e0b;">
                <div style="font-weight: 700; color: #fbbf24; font-size: 15px; margin-bottom: 8px;">
                    ⚡ Market Order (Liquidity Taker)
                </div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.55;">
                    • Executes <strong>immediately</strong> at current best available market prices.<br>
                    • ✅ <strong>Guaranteed Execution:</strong> Filled right away without waiting.<br>
                    • ⚠️ <strong>Price Uncertainty:</strong> Subject to market slippage if large volumes consume multiple book levels.
                </div>
            </div>
            <div class="diagram-node" style="flex: 1; text-align: left; background: #0f172a; border-color: #3b82f6;">
                <div style="font-weight: 700; color: #60a5fa; font-size: 15px; margin-bottom: 8px;">
                    🎯 Limit Order (Liquidity Maker)
                </div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.55;">
                    • Rests on the order book until market reaches specified limit price (or better).<br>
                    • ✅ <strong>Guaranteed Price:</strong> You never pay more or sell for less than your limit.<br>
                    • ⚠️ <strong>Execution Uncertainty:</strong> May never fill if market price does not reach your limit.
                </div>
            </div>
        </div>
    </div>
    '''
