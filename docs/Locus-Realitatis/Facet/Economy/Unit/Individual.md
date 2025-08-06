# Individual

> An individual, as an economic interaction unit, is a bounded agent capable of making decisions, perceiving constraints, and acting purposefully within an economic system by allocating resources, forming preferences, responding to incentives, and participating in exchanges—either as a consumer, producer, worker, investor, or regulator—based on internal dispositions and external institutional conditions.

> An economic individual is a context-sensitive interaction unit endowed with internal preferences, behavioral dispositions, and constraints, capable of perceiving, evaluating, and acting within structured economic environments through adaptive and relational processes.

## Structure

| **Dimension**               | **Description**                                                                | **Attributes / Variables**                          |
| --------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| **Identity**                | Unique identifier and demographic profile                                      | Age, gender, education, social status                       |
| **Preferences**             | Internal ranking or valuation of goods, services, or outcomes                  | Utility functions, taste parameters, risk aversion          |
| **Endowments**              | Initial resources or assets available to the agent                             | Wealth, skills, labor, capital, information                 |
| **Constraints**             | Limits on choices due to resources, time, regulations, or cognitive capacity   | Budget limits, legal restrictions, attention span           |
| **Decision-making**         | Process and logic used for selecting among alternatives                        | Rational optimization, heuristics, satisficing              |
| **Expectations**            | Beliefs or forecasts about future states of the economy, prices, or others     | Price expectations, market trends, policy changes           |
| **Behavioral Dispositions** | Tendencies or habitual patterns of action                                      | Risk tolerance, time preference, social preferences         |
| **Information**             | Knowledge or signals accessible to the agent                                   | Market prices, peer behavior, news, personal experiences    |
| **Interactions**            | Relationships and exchanges with other agents                                  | Trading partners, social networks, institutional contacts   |
| **Adaptability**            | Ability to learn, update beliefs, and modify behavior based on new information | Learning algorithms, feedback response, innovation capacity |
| **Temporal Dimension**      | Time horizon over which decisions and behaviors are planned or evaluated       | Short-term vs. long-term orientation                        |
| **Cultural / Normative**    | Influence of social norms, values, and identity on choices                     | Cultural preferences, ethical constraints                   |

## Capability

| **Capability**        | **Purpose in Model**                                                              |
| --------------------- | --------------------------------------------------------------------------------- |
| **Perception**        | Receives signals (prices, availability, opportunities, social norms)              |
| **Evaluation**        | Assesses alternatives using preferences, utility, and constraints                 |
| **Decision-making**   | Selects action based on chosen strategy (e.g., utility-maximization, satisficing) |
| **Action / Behavior** | Executes transactions, produces goods, consumes, negotiates, signals, etc.        |
| **Adaptation**        | Updates behavior based on feedback, learning, or shocks                           |

## Interaction

| **Interface**    | **Connected To**                         | **Role**                                 |
| ---------------- | ---------------------------------------- | ---------------------------------------- |
| **Markets**      | Goods, labor, capital, services          | Buys, sells, negotiates                  |
| **Institutions** | Norms, rules, regulations                | Constrained or enabled by formal systems |
| **Other Agents** | Households, firms, governments           | Engages in transactions or communication |
| **Environment**  | Economic climate, geography, media, etc. | Receives context and boundary conditions |

## Behavior

> Behavior is the observable expression of an entity’s internal dispositions as it interacts with its environment over time. It reflects the structured sequence of actions or responses performed by an interaction unit in relation to stimuli, goals, norms, and constraints.

### Preference

> Preferences are internal dispositional structures within an agent that rank or evaluate potential states, actions, or outcomes relative to one another, thereby guiding choice behavior in the presence of alternatives.

#### Definition

**Set of alternatives (or consumption bundles):**
  Let $X$ be the set of all possible alternatives (e.g., bundles of goods, outcomes, choices).

**Preference relation:**
  A preference relation $\succeq$ is a binary relation on $X$, where for any two alternatives $x, y \in X$,

  $$
  x \succeq y
  $$

  means "alternative $x$ is **at least as preferred** as alternative $y$."

#### Formulation


**Types of Preference Relations**:

* **Strict preference**:
  $x \succ y$ means $x \succeq y$ but not $y \succeq x$ (i.e., $x$ is strictly preferred to $y$).

* **Indifference**:
  $x \sim y$ means $x \succeq y$ and $y \succeq x$ (i.e., the decision-maker is indifferent between $x$ and $y$).

#### Properties of Preference Relations

A preference relation $\succeq$ often satisfies:

* **Completeness:**
  For all $x, y \in X$, either $x \succeq y$ or $y \succeq x$ (or both).
  This means the agent can always compare any two alternatives.

* **Transitivity:**
  For all $x, y, z \in X$, if $x \succeq y$ and $y \succeq z$, then $x \succeq z$.

* **Reflexivity:**
  For all $x \in X$, $x \succeq x$.

#### Utility Function Representation

If preferences satisfy the above properties (completeness, transitivity, and often continuity), then there exists a **utility function**:

$$
u : X \to \mathbb{R}
$$

such that for all $x, y \in X$,

$$
x \succeq y \iff u(x) \ge u(y).
$$

This means the agent’s preferences can be represented by assigning a real number $u(x)$ to each alternative, so the preference ordering matches the ordering of these numbers.

### Utility

> Utility is a quantitative abstraction representing the degree to which an agent's preferences are satisfied by a particular outcome, state, or good; it serves as a formal measure used to evaluate and compare alternatives within decision-making processes.

> Ontologically, utility is not a concrete object or a directly observable phenomenon. It is a modeling construct that encodes the evaluative stance of an agent within a specific choice context, derived from preferences, and designed to support predictive or normative analysis of behavior.

## Modelling

| **Approach**              | **Modeling Feature**                                                           |
| ------------------------- | ------------------------------------------------------------------------------ |
| **Agent-Based Models**    | Encodes individual rules and interactions; tracks behavior over time and space |
| **Microeconomic Models**  | Represents individual as a utility-maximizer under budget constraints          |
| **Game-Theoretic Models** | Models strategic behavior among interdependent individuals                     |
| **Behavioral Models**     | Incorporates bounded rationality, heuristics, and psychological deviations     |
| **System Dynamics**       | Models population aggregates of individual behavior in feedback loops          |

## Case Study

> Model of Individual Economic Agents.

| **Model Name**                 | **Core Assumptions**                                                     | **Behavioral Logic**                                         | **Rationality Type**                | **Use Cases**                                     |
| ------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- | ---------------------------------------------------------- |
| **Homo Economicus**            | Fully rational, self-interested, perfect information, utility-maximizer  | Maximizes utility subject to constraints                     | Perfect rationality                 | Neoclassical economics, microeconomics                     |
| **Homo Heuristicus**           | Uses mental shortcuts and rules-of-thumb                                 | Simplifies decision-making via heuristics                    | Bounded rationality                 | Behavioral economics, ecological rationality               |
| **Homo Sociologicus**          | Behavior shaped by social norms, roles, expectations                     | Acts according to social expectations and institutions       | Socially constrained                | Institutional economics, sociology-influenced models       |
| **Homo Psychologicus**         | Affected by cognitive biases, emotions, non-linear utilities             | Decisions influenced by framing, loss aversion, etc.         | Emotionally and cognitively bounded | Behavioral & neuroeconomics                                |
| **Homo Reciprocans**           | Values fairness, cooperation, and reciprocity                            | Rewards fairness, punishes unfairness, even at a cost        | Social preference rationality       | Experimental economics, fairness games                     |
| **Homo Oeconomicus Dynamicus** | Adaptive, forward-looking, possibly learning over time                   | Updates beliefs, strategies based on feedback & expectations | Learning rationality                | Dynamic optimization, reinforcement learning               |
| **Constructivist Agent**       | Actively forms preferences, identities, and meanings through interaction | Decisions constructed in context, not pre-determined         | Constructed rationality             | Behavioral, institutional, sociotechnical systems modeling |
| **Homo Digitalis**             | Interacts in digital environments; algorithm-mediated behavior           | Affected by algorithms, nudges, attention economy            | Platform-constrained rationality    | Digital economy, behavioral tech models                    |

## References

- [Homo Economicus](https://en.wikipedia.org/wiki/Homo_economicus)
- [Preference](https://en.wikipedia.org/wiki/Preference_(economics))
- [Preference Modelling](../../../../Locus-Instrumentorum/Consumer//Preference-Modelling.md)
