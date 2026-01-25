# Monetary System

> A **monetary system** is the institutionally structured,  rule-governed subsystem of an economy that defines, issues, stabilizes, and coordinates the use of a unit of account for storing value, settling obligations, and enabling exchange.

- What should the national saving rate be? What should the national investment rate be as a percentage of GDP?
- What is the relationship between macroeconomic variables (such as monetary stability and inflation) and development performance?

## Structure

| **Component**                                        | **Technical Definition**                                                                                                                   | **Function in the System**                                                                       |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| **Money Creation**                                   | The set of institutional and algorithmic mechanisms through which new monetary units and credit-denominated claims are issued.             | Determines liquidity supply, shapes credit cycles, and enables economic transactions.            |
| **Encoding of Monetary Value**                       | The representational and record-keeping formats (physical, digital, ledger-based) that encode monetary units and validate their ownership. | Ensures integrity, traceability, fungibility, and interoperability of value.                     |
| **Payment, Clearing, and Settlement Infrastructure** | The communication, verification, and reconciliation subsystems that execute transfers and establish settlement finality.                   | Enables secure, ordered, low-latency movement of monetary claims across agents and institutions. |
| **Governance**                                       | The regulatory, supervisory, and policy mechanisms that stabilize purchasing power, control liquidity, and enforce systemic constraints.   | Maintains stability, prevents systemic risk, and ensures coherent macroeconomic behavior.        |
| **International Integration**                        | The cross-border linkages that connect domestic monetary arrangements to global payment, exchange-rate, and reserve-management systems.    | Manages external liquidity, exchange-rate dynamics, and international capital flows.             |

## Electronic Funds Transfer

> Electronic Funds Transfer (EFT) is the digitally mediated process by which monetary claims are transmitted, authenticated, cleared, and settled between accounts through an electronic communication and ledger-update infrastructure, without the use of physical payment instruments.

### Characterization


| **Characteristic**                   | **Definition**                                                                  |
| ------------------------------------ | ------------------------------------------------------------------------------- |
| **Processing Time**                  | The duration between initiation of the transfer and settlement completion.      |
| **Transaction Cost**                 | Fees charged per transfer, including fixed, variable, and network costs.        |
| **Settlement Method**                | Mechanism by which obligations are finalized between institutions.              |
| **Authorization & Security**         | Methods for validating identity, transaction integrity, and compliance.         |
| **Interoperability**                 | Ability to transact across systems, institutions, and countries.                |
| **Transaction Volume** | Maximum transactions per second or batch that the system can handle.            |
| **Dispute Handling** | Rules and mechanisms for canceling, reversing, or resolving disputed transfers. |

### Method Space

| **EFT Method** | **Description** | **Processing Time** | **Common Use Cases** |
| --- | --- | --- | --- |
| **ACH Transfer** | Batch-processed transfers via Automated Clearing House (low cost, bulk transactions). | 1-3 business days | Payroll, bill payments, direct deposits. |
| **Wire Transfer** | Real-time, high-value transfers between banks (domestic/international). | Minutes to 24 hours | Large purchases, real estate, cross-border. |
| **Card Payments** | Debit/credit card transactions via networks (Visa, Mastercard, etc.). | Instant (authorization) | Retail, e-commerce, POS transactions. |
| **Real-Time Payments (RTP)** | Instant 24/7 transfers (e.g., FedNow, SEPA Instant, UPI, Pix). | Seconds | P2P, urgent bills, gig economy payouts. |
| **Mobile Wallets** | Funds stored/transferred via apps (e.g., Apple Pay, PayPal, Venmo). | Instant to minutes | P2P, contactless payments, remittances. |
| **Cryptocurrency** | Decentralized transfers via blockchain (e.g., Bitcoin, Ethereum). | Minutes to hours | Cross-border, investments, DeFi. |
| **Direct Debit** | Merchant-initiated pull payments from a customer’s account (pre-authorized). | 1-3 business days | Subscriptions, utility bills. |
| **EFT POS** | Electronic transfers at point-of-sale terminals (e.g., debit card taps). | Instant | Retail, restaurants, in-store purchases. |

### Comparison

| **EFT System**                          | **Processing Time**                               | **Transaction Cost**           | **Authorization & Security**                   | **Interoperability**           | **Dispute Handling**                             |
| --------------------------------------- | ------------------------------------------------- | ------------------------------ | ---------------------------------------------- | ------------------------------ | ------------------------------------------------ |
| **Visa**                                | Near real-time authorization; settlement 1–2 days | Moderate, per-transaction fees | PIN, CVV, 3D Secure, tokenization              | Global card network, merchants | Chargeback mechanism available                   |
| **Mastercard**                          | Near real-time authorization; settlement 1–2 days | Moderate, per-transaction fees | PIN, CVV, 3D Secure, tokenization              | Global card network, merchants | Chargeback mechanism available                   |
| **UPI (India)**                         | Real-time                                         | Minimal                        | Mobile OTP, UPI PIN                            | Domestic banks                 | Pre-settlement reversal possible                 |
| **Bizum (Spain)**                       | Real-time                                         | Low                            | Mobile OTP, bank authentication                | Domestic banks                 | Pre-settlement cancellation possible             |
| **Swish (Sweden)**                      | Real-time                                         | Low                            | Mobile BankID, two-factor authentication       | Domestic banks                 | Pre-settlement cancellation possible             |
| **Zengin System (Japan, RTS)**          | Real-time                                         | Low–moderate                   | Bank authentication, digital signatures        | Domestic banks                 | Irreversible after settlement                    |
| **PayNow (Singapore)**                  | Real-time                                         | Low                            | Mobile authentication, two-factor              | Domestic banks                 | Pre-settlement cancellation possible             |
| **ACH (US)**                            | Batch, same-day or next-day                       | Low                            | Bank authentication, ACH rules                 | Domestic banks                 | Reversal within defined time frame               |
| **Wire Transfer (SWIFT/Bank Transfer)** | Same-day to 1–2 days internationally              | High                           | Bank authentication, SWIFT messaging standards | Global                         | Limited reversal; depends on correspondent banks |

## Electronic Money Infrastructure (EMI)

> Which subsystems should a fully Electronic Native Monetary System support?

> An Electronic Money Infrastructure (EMI) is the system of protocols, ledgers, and payment rails that supports the creation, transfer, and settlement of digital-native monetary units.

| **System**                              | **Description**                                                                                           | **Role in EMI**                                                                   |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Digital Issuance Engine**             | Module or authority that creates and issues digital monetary units.                                       | Controls money supply, ensures authenticity, and enforces issuance rules.         |
| **Account and Identity Ledger**         | Centralized or distributed ledger recording user accounts, balances, and identities.                      | Tracks ownership, enforces access control, and supports compliance (KYC/AML).     |
| **Payment and Settlement Rail**         | Real-time or batch-based infrastructure enabling transfer and clearing of digital units between accounts. | Executes transactions, reconciles balances, and ensures settlement finality.      |
| **Security and Authorization Layer**    | Protocols for encryption, digital signatures, authentication, and fraud detection.                        | Guarantees integrity, prevents double-spending, and enforces user permissions.    |
| **Regulatory and Governance Interface** | APIs and modules allowing supervisory authorities to monitor and enforce monetary rules.                  | Maintains system stability, enforces policy, and supports audits.                 |
| **Interoperability Gateway**            | Connectors to external payment networks, banks, and other EMIs.                                           | Enables cross-system transactions, international flows, and liquidity management. |

## References

- [Monetary System](https://en.wikipedia.org/wiki/Monetary_system)
