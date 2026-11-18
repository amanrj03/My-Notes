# -*- coding: utf-8 -*-
"""
Interactive Quiz Data and Renderer for Blockchain Modules 14-18
"""

import json

QUIZ_DATA_UNIT4 = {
    14: {
        "title": "Module 14: The Bitcoin Network — Self-Test",
        "description": "Test your mastery of Bitcoin P2P architecture, node types, handshake protocol, inventory propagation, IBD, and Stratum.",
        "questions": [
            {
                "id": 1,
                "question": "Which node independently validates Bitcoin's consensus rules?",
                "options": [
                    "SPV node",
                    "Full node",
                    "Wallet only",
                    "DNS seed"
                ],
                "correct": 1,
                "explanation": "A full node maintains a complete copy of the blockchain and independently validates every transaction and block against Bitcoin's consensus rules (such as checking signatures, inputs, and double-spends) without trusting any third party."
            },
            {
                "id": 2,
                "question": "Which message announces knowledge of a transaction or block?",
                "options": [
                    "getdata",
                    "verack",
                    "inv",
                    "pong"
                ],
                "correct": 2,
                "explanation": "The 'inv' (inventory) message is broadcast by a Bitcoin node to announce that it has new transactions or blocks available. A receiving peer can then request the actual payload by replying with 'getdata'."
            },
            {
                "id": 3,
                "question": "What does an SPV client download?",
                "options": [
                    "Every complete block",
                    "Only private keys",
                    "Block headers",
                    "Only mining rewards"
                ],
                "correct": 2,
                "explanation": "Simplified Payment Verification (SPV) clients (light nodes) download only the 80-byte block headers instead of complete multi-megabyte blocks. They rely on Merkle branches to verify whether a transaction is included in a block."
            },
            {
                "id": 4,
                "question": "Which service helps a new Bitcoin node discover peers?",
                "options": [
                    "DNS seeds",
                    "Coinbase transaction",
                    "Merkle root",
                    "Nonce"
                ],
                "correct": 0,
                "explanation": "When a new node starts with an empty peer database, it queries predefined DNS seeds (managed by trusted Bitcoin core contributors) which resolve to IP addresses of active full nodes on the network."
            },
            {
                "id": 5,
                "question": "Which approach downloads block headers before full blocks?",
                "options": [
                    "Blocks-first",
                    "Headers-first",
                    "Mining-first",
                    "Wallet-first"
                ],
                "correct": 1,
                "explanation": "In headers-first Initial Block Download (IBD), the node downloads all block headers first to construct and validate the longest Proof-of-Work chain before downloading full block payloads in parallel from multiple peers."
            },
            {
                "id": 6,
                "question": "Which protocol is commonly used in mining pools?",
                "options": [
                    "HTTP",
                    "SMTP",
                    "Stratum",
                    "FTP"
                ],
                "correct": 2,
                "explanation": "Stratum is a lightweight JSON-RPC based protocol designed specifically for communication between individual mining rigs (ASICs) and mining pool servers, avoiding the heavy overhead of running a full P2P node on each miner."
            }
        ]
    },
    15: {
        "title": "Module 15: Bitcoin Wallets — Self-Test",
        "description": "Test your understanding of private/public keys, address derivation, wallet types, HD BIP32/BIP44, BIP39 mnemonics, and UTXOs.",
        "questions": [
            {
                "id": 1,
                "question": "What does a Bitcoin wallet actually store and manage?",
                "options": [
                    "Actual bitcoins",
                    "Cryptographic keys",
                    "Only transaction fees",
                    "Mining blocks"
                ],
                "correct": 1,
                "explanation": "Bitcoins are never physically stored in a wallet; they exist solely as unspent transaction outputs (UTXOs) recorded on the public blockchain ledger. A wallet stores and manages the cryptographic keys used to unlock and spend those coins."
            },
            {
                "id": 2,
                "question": "Which key is used to sign an outgoing Bitcoin transaction?",
                "options": [
                    "Public key",
                    "Private key",
                    "Bitcoin address",
                    "Merkle root"
                ],
                "correct": 1,
                "explanation": "The private key (kept secret by the owner) is used to generate ECDSA digital signatures that prove ownership of the funds being spent. The public key is used by other network nodes to verify this signature."
            },
            {
                "id": 3,
                "question": "What does JBOK stand for?",
                "options": [
                    "Just a Bunch of Keys",
                    "Joint Bitcoin Online Key",
                    "Java Based Open Key",
                    "Just a Bitcoin Output Key"
                ],
                "correct": 0,
                "explanation": "JBOK stands for 'Just a Bunch of Keys' (Type 0 non-deterministic wallets). In JBOK wallets, every key pair is generated from an independent random number, requiring frequent backups whenever new addresses are used."
            },
            {
                "id": 4,
                "question": "Which BIP defines the HD wallet structure?",
                "options": [
                    "BIP21",
                    "BIP32",
                    "BIP70",
                    "BIP39 only"
                ],
                "correct": 1,
                "explanation": "BIP32 defines Hierarchical Deterministic (HD) wallets, allowing an infinite tree of child keys to be derived deterministically from a single master seed using chain codes."
            },
            {
                "id": 5,
                "question": "Which wallet derives a private key from a remembered passphrase?",
                "options": [
                    "Hardware wallet",
                    "Paper wallet",
                    "Brain wallet",
                    "Mobile wallet"
                ],
                "correct": 2,
                "explanation": "A brain wallet generates a private key from a passphrase memorized in the user's mind by passing it through a hash algorithm. They are highly discouraged today because humans choose predictable passphrases vulnerable to brute-force dictionary attacks."
            },
            {
                "id": 6,
                "question": "Which wallet uses a dedicated physical device to protect keys?",
                "options": [
                    "Online wallet",
                    "Hardware wallet",
                    "Brain wallet",
                    "Non-deterministic wallet"
                ],
                "correct": 1,
                "explanation": "A hardware wallet (e.g. Ledger, Trezor) stores private keys on a dedicated, secure microcontroller chip isolated from the internet. Transactions are signed inside the device, protecting keys from malware on host computers."
            },
            {
                "id": 7,
                "question": "What does BIP39 define?",
                "options": [
                    "Mining difficulty",
                    "Mnemonic code words",
                    "Block size",
                    "Payment channels"
                ],
                "correct": 1,
                "explanation": "BIP39 defines the standard for mnemonic code words—translating raw cryptographic entropy into a sequence of 12 to 24 human-readable English words with a built-in checksum for easy backup and recovery."
            },
            {
                "id": 8,
                "question": "Which is generally more suitable for long-term offline key storage?",
                "options": [
                    "Hot wallet",
                    "Cold wallet",
                    "Online exchange account",
                    "Web wallet"
                ],
                "correct": 1,
                "explanation": "A cold wallet stores cryptographic keys entirely offline, completely disconnected from the internet and network attacks, making it the industry standard for long-term secure holding."
            }
        ]
    },
    16: {
        "title": "Module 16: Bitcoin Payments — Self-Test",
        "description": "Test your understanding of POS systems, QR codes, BIP21 URIs, payment processors, and the BIP70 Payment Protocol with X.509 PKI.",
        "questions": [
            {
                "id": 1,
                "question": "Which BIP defines the Bitcoin URI payment format?",
                "options": [
                    "BIP32",
                    "BIP21",
                    "BIP70",
                    "BIP72"
                ],
                "correct": 1,
                "explanation": "BIP21 defines the standardized URI scheme `bitcoin:<address>?amount=<value>&label=<label>` used for click-to-pay links and QR codes."
            },
            {
                "id": 2,
                "question": "What is the main purpose of a Bitcoin POS system?",
                "options": [
                    "Mine Bitcoin",
                    "Accept Bitcoin payments at physical shops",
                    "Generate private keys only",
                    "Create new blocks"
                ],
                "correct": 1,
                "explanation": "A Point of Sale (POS) system allows brick-and-mortar retail shops to generate instant invoices, convert local currency amounts to Bitcoin at real-time exchange rates, and present dynamic QR codes for customer checkout."
            },
            {
                "id": 3,
                "question": "Which of these is an example of a Bitcoin payment processor mentioned in the textbook?",
                "options": [
                    "BitPay",
                    "Trezor",
                    "SHA-256",
                    "BIP32"
                ],
                "correct": 0,
                "explanation": "BitPay is a prominent merchant payment gateway that handles crypto checkout, manages exchange rate risk, and deposits fiat currency directly into the merchant's bank account."
            },
            {
                "id": 4,
                "question": "Which BIP describes the secure Bitcoin Payment Protocol?",
                "options": [
                    "BIP21",
                    "BIP32",
                    "BIP70",
                    "BIP39"
                ],
                "correct": 2,
                "explanation": "BIP70 defines the Bitcoin Payment Protocol, adding cryptographic signatures, merchant identification, refund addresses, and tamper-resistant payment verification to Bitcoin transactions."
            },
            {
                "id": 5,
                "question": "Which certificate standard is used by BIP70 for authentication?",
                "options": [
                    "AES",
                    "X.509",
                    "SHA-256",
                    "Base58"
                ],
                "correct": 1,
                "explanation": "BIP70 uses X.509 public-key infrastructure (PKI) digital certificates (the same standard securing HTTPS web traffic) to verify the legal identity of the merchant requesting payment."
            },
            {
                "id": 6,
                "question": "Which message is sent by the merchant to request payment?",
                "options": [
                    "PaymentACK",
                    "Payment",
                    "PaymentRequest",
                    "Block"
                ],
                "correct": 2,
                "explanation": "In the BIP70 flow, the merchant server generates a `PaymentRequest` message containing payment instructions, expiration time, memo, and an optional X.509 signature for wallet verification."
            },
            {
                "id": 7,
                "question": "Which message acknowledges the Payment message?",
                "options": [
                    "PaymentACK",
                    "PaymentRequest",
                    "Inv",
                    "Verack"
                ],
                "correct": 0,
                "explanation": "After receiving the signed Bitcoin transaction in a `Payment` message, the merchant server broadcasts it and returns a `PaymentACK` message as an official cryptographic receipt."
            },
            {
                "id": 8,
                "question": "Which BIP defines MIME types for the Payment Protocol?",
                "options": [
                    "BIP21",
                    "BIP70",
                    "BIP71",
                    "BIP72"
                ],
                "correct": 2,
                "explanation": "BIP71 specifies the formal MIME media types (e.g., application/bitcoin-paymentrequest, application/bitcoin-payment) for handling payment protocol messages over HTTP/email."
            },
            {
                "id": 9,
                "question": "Which BIP defines URI extensions for the Payment Protocol?",
                "options": [
                    "BIP32",
                    "BIP39",
                    "BIP71",
                    "BIP72"
                ],
                "correct": 3,
                "explanation": "BIP72 defines extensions to the BIP21 URI scheme to allow fetching BIP70 PaymentRequest files via URLs (e.g. `bitcoin:address?r=https://merchant.com/pay`)."
            },
            {
                "id": 10,
                "question": "What does a Man-in-the-Middle attacker attempt to do?",
                "options": [
                    "Mine a block",
                    "Intercept or modify communication",
                    "Generate a wallet seed",
                    "Confirm a transaction"
                ],
                "correct": 1,
                "explanation": "A Man-in-the-Middle (MITM) attacker attempts to intercept communication between customer and merchant to substitute the merchant's Bitcoin address with an attacker-controlled address. BIP70 stops this using X.509 certificate signatures."
            }
        ]
    },
    17: {
        "title": "Module 17: Innovation in Bitcoin and Advanced Protocols — Self-Test",
        "description": "Test your understanding of BIP types, soft vs hard forks, SegWit (BIP141), malleability, Bitcoin Cash, Bitcoin Gold, and the Lightning Network.",
        "questions": [
            {
                "id": 1,
                "question": "What does BIP stand for?",
                "options": [
                    "Bitcoin Internet Protocol",
                    "Bitcoin Improvement Proposal",
                    "Blockchain Integration Process",
                    "Bitcoin Internal Payment"
                ],
                "correct": 1,
                "explanation": "BIP stands for Bitcoin Improvement Proposal. It is the standardized design document used by the community to propose new features, consensus changes, or process guidelines for Bitcoin."
            },
            {
                "id": 2,
                "question": "Which type of BIP deals with major protocol changes?",
                "options": [
                    "Standard BIP",
                    "Process BIP",
                    "Informational BIP",
                    "None"
                ],
                "correct": 0,
                "explanation": "Standards BIPs specify changes that affect the core Bitcoin protocol, network rules, consensus validation, or transaction and block formats."
            },
            {
                "id": 3,
                "question": "Which fork is backward-compatible?",
                "options": [
                    "Hard fork",
                    "Soft fork",
                    "Temporary fork only",
                    "Neither"
                ],
                "correct": 1,
                "explanation": "A soft fork is backward-compatible because it tightens or restricts consensus rules. Blocks produced under the new rules are still recognized as valid by unupgraded nodes."
            },
            {
                "id": 4,
                "question": "What was the main purpose of SegWit?",
                "options": [
                    "Replace Bitcoin mining",
                    "Separate witness data and improve Bitcoin transactions",
                    "Create a new cryptocurrency",
                    "Remove digital signatures"
                ],
                "correct": 1,
                "explanation": "Segregated Witness (SegWit, BIP141) separated cryptographic signature scripts (witness data) from the base transaction tree. This solved transaction malleability, enabled Layer-2 networks (Lightning), and increased effective block capacity."
            },
            {
                "id": 5,
                "question": "Which address format is associated with native SegWit?",
                "options": [
                    "bc1",
                    "0x",
                    "LTC",
                    "ETH"
                ],
                "correct": 0,
                "explanation": "Native SegWit addresses use the Bech32 format defined in BIP173, which always starts with the prefix 'bc1' and uses lowercase alphanumeric characters without ambiguous glyphs."
            },
            {
                "id": 6,
                "question": "What is the maximum block weight introduced by SegWit?",
                "options": [
                    "1 million units",
                    "2 million units",
                    "4 million units",
                    "8 million units"
                ],
                "correct": 2,
                "explanation": "SegWit replaced the legacy 1 MB block size limit with a 4,000,000 Block Weight Unit (WU) limit, where base transaction data counts as 4 WU per byte and witness data counts as 1 WU per byte."
            },
            {
                "id": 7,
                "question": "Bitcoin Cash was created through which type of fork?",
                "options": [
                    "Soft fork",
                    "Hard fork",
                    "No fork",
                    "Temporary fork"
                ],
                "correct": 1,
                "explanation": "Bitcoin Cash (BCH) split from the main Bitcoin chain in August 2017 via a hard fork by increasing the base block size limit from 1 MB to 8 MB and rejecting SegWit."
            },
            {
                "id": 8,
                "question": "What is the main objective of Bitcoin Gold?",
                "options": [
                    "Increase mining centralisation",
                    "Reduce mining centralisation",
                    "Remove PoW completely",
                    "Eliminate wallets"
                ],
                "correct": 1,
                "explanation": "Bitcoin Gold (BTG) was created to democratize mining and resist hardware centralization by replacing SHA-256 with Equihash, allowing consumer GPUs to mine profitably again."
            },
            {
                "id": 9,
                "question": "Which algorithm is associated with Bitcoin Gold in the textbook?",
                "options": [
                    "SHA-256",
                    "Equihash",
                    "AES",
                    "RSA"
                ],
                "correct": 1,
                "explanation": "Bitcoin Gold adopted Equihash, a memory-hard Proof of Work algorithm designed to be resistant to ASIC optimization."
            },
            {
                "id": 10,
                "question": "What is the main purpose of the Lightning Network?",
                "options": [
                    "Increase mining rewards",
                    "Enable faster off-chain payments",
                    "Replace public keys",
                    "Increase block time"
                ],
                "correct": 1,
                "explanation": "The Lightning Network is a Layer-2 payment channel protocol that executes millions of instant, low-fee micropayments off-chain while anchoring final settlement onto the Bitcoin blockchain."
            }
        ]
    },
    18: {
        "title": "Module 18: Bitcoin Investment, Buying & Selling — Self-Test",
        "description": "Test your understanding of crypto exchanges (CEX vs DEX), trading positions, CFDs, margin trading, order books, bid-ask spread, and order types.",
        "questions": [
            {
                "id": 1,
                "question": "What is a Bitcoin exchange?",
                "options": [
                    "A mining algorithm",
                    "A platform for buying and selling Bitcoin",
                    "A type of wallet only",
                    "A consensus protocol"
                ],
                "correct": 1,
                "explanation": "A Bitcoin exchange is a digital marketplace (centralized or decentralized) where users can exchange fiat currencies (like USD, EUR, INR) for Bitcoin or swap Bitcoin with other crypto assets."
            },
            {
                "id": 2,
                "question": "A long position generally benefits when Bitcoin's price:",
                "options": [
                    "Increases",
                    "Decreases",
                    "Becomes zero",
                    "Does not change"
                ],
                "correct": 0,
                "explanation": "Taking a long position (buying with the expectation of rising value) yields a profit when the market price of the asset increases over time."
            },
            {
                "id": 3,
                "question": "A short position generally benefits when Bitcoin's price:",
                "options": [
                    "Increases",
                    "Decreases",
                    "Remains fixed",
                    "Doubles"
                ],
                "correct": 1,
                "explanation": "Taking a short position (selling borrowed assets) allows a trader to profit when the asset price declines, by buying it back later at a cheaper price."
            },
            {
                "id": 4,
                "question": "What is a CFD?",
                "options": [
                    "A Bitcoin wallet",
                    "A contract based on the difference in an asset's price",
                    "A mining device",
                    "A type of blockchain"
                ],
                "correct": 1,
                "explanation": "A Contract for Difference (CFD) is a financial derivative where buyer and seller agree to settle the cash difference between the opening and closing price of an asset without owning the underlying cryptocurrency."
            },
            {
                "id": 5,
                "question": "What does margin trading involve?",
                "options": [
                    "Trading only with cash",
                    "Using borrowed funds to increase trading exposure",
                    "Mining Bitcoin",
                    "Creating a new block"
                ],
                "correct": 1,
                "explanation": "Margin trading allows traders to borrow capital from an exchange to leverage their trading positions, increasing potential profit gains while also significantly magnifying liquidation risks."
            },
            {
                "id": 6,
                "question": "What is an order book?",
                "options": [
                    "A list of private keys",
                    "A list of outstanding buy and sell orders",
                    "A list of mined blocks",
                    "A wallet backup"
                ],
                "correct": 1,
                "explanation": "An order book is a real-time list maintained by an exchange of all open limit buy orders (bids) and sell orders (asks) organized by price level."
            },
            {
                "id": 7,
                "question": "What is a bid price?",
                "options": [
                    "The seller's lowest requested price",
                    "The buyer's offered price",
                    "The mining reward",
                    "The exchange fee"
                ],
                "correct": 1,
                "explanation": "The bid price is the highest price that prospective buyers in the market are currently offering to pay for an asset."
            },
            {
                "id": 8,
                "question": "What is an ask price?",
                "options": [
                    "The buyer's offered price",
                    "The seller's requested price",
                    "The average mining cost",
                    "The transaction ID"
                ],
                "correct": 1,
                "explanation": "The ask price (or offer price) is the lowest price that sellers in the market are currently willing to accept to sell their asset."
            },
            {
                "id": 9,
                "question": "How is the bid-ask spread calculated?",
                "options": [
                    "Bid + Ask",
                    "Ask − Bid",
                    "Bid × Ask",
                    "Ask ÷ Bid"
                ],
                "correct": 1,
                "explanation": "The bid-ask spread is calculated as Ask Price minus Bid Price. A narrower spread indicates higher liquidity and lower transaction friction."
            },
            {
                "id": 10,
                "question": "Which order specifies a price at which the trader is willing to buy or sell?",
                "options": [
                    "Market order",
                    "Limit order",
                    "Mining order",
                    "Block order"
                ],
                "correct": 1,
                "explanation": "A limit order specifies a strict price boundary at which the trader is willing to transact (or better). Unlike a market order, execution is not guaranteed if the market does not reach that price."
            }
        ]
    }
}

def render_quiz_html(mod_num):
    data = QUIZ_DATA_UNIT4.get(mod_num)
    if not data:
        return ""
    
    questions = data["questions"]
    q_count = len(questions)
    
    q_cards = []
    letters = ["A", "B", "C", "D"]
    
    for idx, q in enumerate(questions):
        qid = q["id"]
        q_text = q["question"]
        opts = q["options"]
        correct_idx = q["correct"]
        
        opt_btns = []
        for o_idx, opt_text in enumerate(opts):
            letter = letters[o_idx]
            opt_btns.append(f'''
            <button class="quiz-option-btn" 
                    id="q_{mod_num}_{qid}_opt_{o_idx}"
                    onclick="handleQuizClick({mod_num}, {qid}, {o_idx}, {correct_idx})">
                <span class="opt-letter">{letter}</span>
                <span class="opt-text">{opt_text}</span>
            </button>''')
        
        opt_grid = "".join(opt_btns)
        
        q_cards.append(f'''
        <div class="quiz-question-box" id="qbox_{mod_num}_{qid}">
            <div class="quiz-q-header">
                <span class="quiz-q-badge">Question {qid} of {q_count}</span>
                <span class="quiz-q-status" id="qstatus_{mod_num}_{qid}">⏳ Not answered</span>
            </div>
            <h4 class="quiz-q-text">{qid}. {q_text}</h4>
            <div class="quiz-options-grid">
                {opt_grid}
            </div>
            <div class="quiz-explanation-box" id="qexp_{mod_num}_{qid}">
                <div class="exp-content" id="qexp_text_{mod_num}_{qid}"></div>
            </div>
        </div>''')

    cards_html = "\n".join(q_cards)
    explanations_json = json.dumps({q["id"]: q["explanation"] for q in questions})

    quiz_component = f'''
    <div class="quiz-section-wrap" id="module-quiz-section">
        <div class="quiz-card-container">
            <div class="quiz-main-header">
                <div class="quiz-title-area">
                    <h3 class="quiz-title">📝 Quick Self-Test &amp; Knowledge Check</h3>
                    <p class="quiz-subtitle">{data["description"]}</p>
                </div>
                <div class="quiz-action-bar">
                    <span class="quiz-stat-pill" id="quiz-progress-text-{mod_num}">0/{q_count} Answered</span>
                    <span class="quiz-score-pill" id="quiz-score-text-{mod_num}">🏆 Score: 0/{q_count}</span>
                    <button class="quiz-reset-btn" onclick="resetQuiz({mod_num}, {q_count})">
                        🔄 Reset Quiz
                    </button>
                </div>
            </div>

            <div class="quiz-progress-track">
                <div class="quiz-progress-fill" id="quiz-progress-fill-{mod_num}"></div>
            </div>

            <div class="quiz-questions-list">
                {cards_html}
            </div>

            <div class="quiz-result-banner" id="quiz-result-banner-{mod_num}">
                <div class="res-title" id="quiz-res-title-{mod_num}">🎉 Module Quiz Completed!</div>
                <p class="res-score" id="quiz-res-score-{mod_num}"></p>
                <div class="res-actions">
                    <button class="quiz-reset-btn" onclick="resetQuiz({mod_num}, {q_count})">Retake Quiz</button>
                </div>
            </div>
        </div>
    </div>

    <script>
    (function() {{
        const mod = {mod_num};
        const totalQ = {q_count};
        const explanations = {explanations_json};
        let userAnswers = {{}};
        let score = 0;

        window.handleQuizClick = function(m, qid, selectedIdx, correctIdx) {{
            if (m !== mod) return;
            if (userAnswers[qid] !== undefined) return; // already answered

            userAnswers[qid] = selectedIdx;
            const isCorrect = (selectedIdx === correctIdx);
            if (isCorrect) score++;

            // Highlight buttons
            for (let i = 0; i < 4; i++) {{
                const btn = document.getElementById(`q_${{m}}_${{qid}}_opt_${{i}}`);
                if (btn) {{
                    btn.disabled = true;
                    if (i === correctIdx) {{
                        btn.className = 'quiz-option-btn correct';
                    }} else if (i === selectedIdx && !isCorrect) {{
                        btn.className = 'quiz-option-btn incorrect';
                    }} else {{
                        btn.className = 'quiz-option-btn dim';
                    }}
                }}
            }}

            // Update question status
            const statusEl = document.getElementById(`qstatus_${{m}}_${{qid}}`);
            if (statusEl) {{
                statusEl.textContent = isCorrect ? '✅ Correct' : '❌ Incorrect';
                statusEl.className = isCorrect ? 'quiz-q-status correct' : 'quiz-q-status incorrect';
            }}

            // Show explanation
            const expBox = document.getElementById(`qexp_${{m}}_${{qid}}`);
            const expText = document.getElementById(`qexp_text_${{m}}_${{qid}}`);
            if (expBox && expText) {{
                const exp = explanations[qid] || '';
                expText.innerHTML = (isCorrect ? '<strong>Right on target!</strong> ' : '<strong>Concept clarity:</strong> ') + exp;
                expBox.className = 'quiz-explanation-box ' + (isCorrect ? 'correct' : 'incorrect');
                expBox.style.display = 'block';
            }}

            // Update stats
            const answeredCount = Object.keys(userAnswers).length;
            const progText = document.getElementById(`quiz-progress-text-${{mod}}`);
            if (progText) progText.textContent = `${{answeredCount}}/${{totalQ}} Answered`;

            const scoreText = document.getElementById(`quiz-score-text-${{mod}}`);
            if (scoreText) scoreText.textContent = `🏆 Score: ${{score}}/${{totalQ}}`;

            const progFill = document.getElementById(`quiz-progress-fill-${{mod}}`);
            if (progFill) progFill.style.width = `${{Math.round((answeredCount / totalQ) * 100)}}%`;

            // If complete, show banner
            if (answeredCount === totalQ) {{
                const banner = document.getElementById(`quiz-result-banner-${{mod}}`);
                const resTitle = document.getElementById(`quiz-res-title-${{mod}}`);
                const resScore = document.getElementById(`quiz-res-score-${{mod}}`);
                if (banner && resTitle && resScore) {{
                    banner.style.display = 'block';
                    if (score === totalQ) {{
                        resTitle.innerHTML = '🏆 Perfect Score! Mastermind Level';
                        resScore.innerHTML = `Incredible work! You answered all ${{totalQ}} questions correctly. You have mastered this module!`;
                    }} else if (score >= Math.ceil(totalQ * 0.6)) {{
                        resTitle.innerHTML = '🌟 Great Job! Concept Check Passed';
                        resScore.innerHTML = `You scored ${{score}} out of ${{totalQ}} (${{Math.round((score/totalQ)*100)}}%). Review the explanations above for complete mastery.`;
                    }} else {{
                        resTitle.innerHTML = '📚 Good Effort! Keep Revising';
                        resScore.innerHTML = `You scored ${{score}} out of ${{totalQ}}. Review the module summary above and retake the quiz to boost your score!`;
                    }}
                }}
            }}
        }};

        window.resetQuiz = function(m, tQ) {{
            if (m !== mod) return;
            userAnswers = {{}};
            score = 0;

            for (let qid = 1; qid <= tQ; qid++) {{
                for (let i = 0; i < 4; i++) {{
                    const btn = document.getElementById(`q_${{m}}_${{qid}}_opt_${{i}}`);
                    if (btn) {{
                        btn.disabled = false;
                        btn.className = 'quiz-option-btn';
                    }}
                }}
                const statusEl = document.getElementById(`qstatus_${{m}}_${{qid}}`);
                if (statusEl) statusEl.textContent = '⏳ Not answered';

                const expBox = document.getElementById(`qexp_${{m}}_${{qid}}`);
                if (expBox) {{
                    expBox.style.display = 'none';
                    expBox.className = 'quiz-explanation-box';
                }}
            }}

            const progText = document.getElementById(`quiz-progress-text-${{mod}}`);
            if (progText) progText.textContent = `0/${{totalQ}} Answered`;

            const scoreText = document.getElementById(`quiz-score-text-${{mod}}`);
            if (scoreText) scoreText.textContent = `🏆 Score: 0/${{totalQ}}`;

            const progFill = document.getElementById(`quiz-progress-fill-${{mod}}`);
            if (progFill) progFill.style.width = '0%';

            const banner = document.getElementById(`quiz-result-banner-${{mod}}`);
            if (banner) banner.style.display = 'none';
        }};
    }})();
    </script>
    '''
    return quiz_component
