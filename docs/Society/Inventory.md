# Inventory

: 9
Tags: Inventory

> …
> 

## Conceptual Model

> …
> 

| **Category** | **Subcategory** | **Attributes** | **Examples** | **Purpose** |
| --- | --- | --- | --- | --- |
| **By Function** | Stock Inventory | Basic replenishment items | Groceries, apparel, electronics | Meet regular customer demand. |
|  | Safety Stock | Buffer against demand fluctuations | Extra units of popular products | Mitigate stockouts. |
|  | Seasonal Inventory | Items for specific seasons/events | Christmas decor, summer apparel | Capture seasonal demand. |
|  | Dead Stock | Obsolete or unsellable items | Outdated tech, expired food | Identify for liquidation or disposal. |
| **By Ownership** | Owned Inventory | Retailer-purchased stock | Products in storage or store shelves | Full control by the retailer. |
|  | Consignment Inventory | Vendor-owned until sold | Branded products provided by suppliers | Reduces upfront costs for the retailer. |
|  | Vendor-Managed Inventory (VMI) | Inventory managed by the supplier | Fast-moving consumer goods (FMCG) | Streamlines replenishment. |
| **By Lifecycle Stage** | Raw Materials | Inputs for in-house production | Packaging materials, bulk ingredients | Supports product manufacturing. |
|  | Work-in-Progress (WIP) | Partially completed products | Semi-finished baked goods, electronics | Tracks unfinished inventory. |
|  | Finished Goods | Ready-to-sell products | Packaged snacks, shoes | Drives sales directly. |
|  | Returns and Damaged Goods | Items returned or damaged | Defective appliances, mispicked items | Plan for repairs or refunds. |
| **By Demand Type** | Fast-Moving Inventory | High turnover rate | Snacks, toiletries | Frequent restocking required. |
|  | Slow-Moving Inventory | Low turnover rate | Specialty tools, high-end furniture | Requires discounting or promotions. |
| **By Storage Location** | On-Site Inventory | Stored within the retail location | Shelves, backroom stock | Immediate access for customers. |
|  | Off-Site Inventory | Stored externally | Distribution centers, warehouses | Supports large-scale operations. |
| **By Classification** | High-Value Inventory | Expensive, high-margin items | Luxury watches, premium electronics | Requires tighter security measures. |
|  | Perishable Inventory | Time-sensitive items | Fresh produce, dairy | Needs rapid turnover and cold storage. |
|  | Non-Perishable Inventory | Long shelf-life products | Canned goods, clothing | Allows for long-term storage. |
|  | Hazardous Inventory | Dangerous or regulated items | Cleaning chemicals, batteries | Requires compliance with safety laws. |
|  | Bulk Inventory | Large quantities purchased or stored | Wholesale items, palletized goods | Economical purchasing strategy. |

## Inventory Modelling Tools

> …
> 

| **Model** | **Purpose** | **Key Formula/Concept** | **Applications** |
| --- | --- | --- | --- |
| **Economic Order Quantity (EOQ)** | Minimize total inventory costs (ordering + holding) | $\text{EOQ} = \sqrt{\frac{2DS}{H}}$ | Bulk ordering optimization |
| **Reorder Point (ROP)** | Determine when to place a new order | $\text{ROP} = (d \times L) + \text{SS}$ | Avoid stockouts during lead time |
| **ABC Analysis** | Prioritize inventory management based on value | Categorize inventory into A (high), B (moderate), C (low) value based on consumption | Inventory prioritization |
| **Newsvendor Model** | Optimize inventory for single-period products | $Q^* = F^{-1}\left(\frac{C_u}{C_u + C_o}\right)$ | Seasonal or perishable goods |
| **Inventory Turnover Ratio** | Measure how efficiently inventory is sold | $\text{Turnover} = \frac{\text{COGS}}{\text{Average Inventory}}$ | Identify slow-moving inventory |
| **Base Stock Model** | Maintain consistent inventory levels | $\text{Base Stock Level} = d \times L + \text{SS}$ | High variability in demand |
| **Safety Stock Calculation** | Buffer against demand and lead time variability | $S = Z \times \sqrt{(L \cdot \sigma_d^2) + (d^2 \cdot \sigma_L^2)}$ | Avoid shortages during variability |
| **Dynamic Programming Models** | Optimize over multiple time periods | Minimizes costs dynamically considering future demand. | Seasonal inventory planning |
| **Stochastic Inventory Models** | Address uncertainty in demand and lead times | $(Q, R)$ Model: Orders triggered at $R$, with order size $E$. | FMCG, pharmaceuticals |
| **Lot Sizing Models** | Optimize batch sizes for production or orders | Examples: Silver-Meal Heuristic, Least Unit Cost (LUC) | Manufacturing, wholesale |
| **Simulation Models** | Analyze complex inventory scenarios | Uses simulations to model performance under varying demand, lead times, or disruptions. | Logistics, warehousing |

## References

- https://en.wikipedia.org/wiki/Inventory