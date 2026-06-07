Cover Design by Devon Smith Creative LLC.

Library of Congress Control Number: 2025945187 ISBN (paperback): 9781662966378 eISBN: 9781662966385

Making the Busin 9 Translate Developer Experience into Bt 10 Connect Your Work to What Others Ca

# PART IV

Table of Contents Improving DevEx: A 7-

# STEP 1

Start Your DevEx .

11 Interview Developers 12 Synthesize What You Learn Foreword By Martin Fowler Foreword By Sarah Drasner 13 Visualize Your Developers’ Workflow, 1 Introduction 14 Understand Your Stakeholders

# PART | 15 Share What You've Learned

Understanding DevEx

# STEP 2

Start Small and Get 1 What is Developer Experience?

2 Why Developer Experience Matters 16 Pick the Right Projects 3 Friction: The Value Killer 17 Share Early Wins to Gain Momentum

# PART Il 18 Avoid Common Pitfalls

The Three Essential Elements of DevEx

# STEP 3

Use Data to Optimize Your 4 The DevEx Framework 5 Feedback Loops 6 Flow State 19 Establish Your Data Foundation 20 Identify and Use the Data You Already 7 Cognitive Load 8 Use the Framework to Identify and Remove Friction 21 Use Surveys for Fast Insights 22 Invest in System Metrics Over Time

# PART Ill 23 Make Sure You Capture the Right Data

## CG -0

Turn Data Into Actionable Insights

# STEP 4

Decide Strategy and Priority Focus Your DevEx Efforts Use Relevant Criteria to Set Priority for Developer Experience See the Bigger Picture: Use a Quick Rubric

# STEP 5

Sell Your Strategy Leverage Your Stakeholder Analysis for Effective Communication Effective Messaging Takes Customization and Repetition

# STEP 6

Drive Change at (Your) Scale Adapt Your Approach to Your Scope Drive Change With Global Scope of Control Drive Change With Local Scope of Control Drive Change With Middle Ground Scope of Control

# STEP 7

Evaluate Your Progress and Show Value 34 Analyze Your Data Prepare to Communicate Your Results 36 Share Progress Navigate Conflicting Metrics 38 Learn and Improve Evaluation Is Just One Step in a Virtuous Cycle

# PART V

Evolving and Sust:

## THE FIRST PRA!

Resource Your DevE 40 Bootstrap Your Early Efforts 41 Build a Dedicated Function 42 Developing Talent for DevEx Roles 43 Make Developer Experience Everyone's 44 Secure Budget at Different Organizatio 45 Making DevEx Stick

## THE SECOND PR:

Create Structures to Su 46 A Framework For DevEx Change 47 Support Teams Through Change 48 Guide Organizations Through Change 49 Support Yourself Through Challenging

## THE THIRD PRA

Make Technology Sustaina 50 Adopt a Product Mindset 51 Use Product Management Principles tc 52 Use Tooling Standardization to Drive E 53 Deal with Technical Debt in DevEx Init 54 Bring It All Together: The Sustainable

THE FOURTH PRACTICE Final Thoug} Design Metrics That Evolve and Amplify Impact 61 What Are You Waiting For?

55 Design Metrics for Your Stakeholders 56 Use Metrics to Solve Your Stakeholders’ Problems PART VI 57 Fast Is Relative to Your Competition Workbooks 58 Start Simple and Scale Smartly Acknowledgments About the Authors 59 How AI Changes (and Doesn’t Change) the Metrics You Need 60 Maintain Your Metrics Like Any Product

[&] Foreword By Martin Fowler I'M AT LUNCH with a bunch of senior technology managers, and one is regaling the table with his latest initiative to improve his software development teams. He's launching a metrics program that will tell him which teams and staff members are the most productive so that he can promote those and fire the worst. This is a professional setting, so I'm trying my best not to roll my eyes. Attempting to get a word in edgeways, I ask what metrics he’s using, and follow up by asking him if he’s trying to consider business outcomes, at least to correlate them to his measurements. Sadly, I'm not getting anywhere, it’s hard to convince someone to look for their keys in the bushes instead of under the lamp post.

Almost every engineering manager I've met wants to make their team more productive, but almost every developer I've met wants to be more effective at what they do. But lunches like that easily lead developers to the cynicism that talking about productivity is about making simplistic measurements that forget the invincible power of Goodhart’s Law: “When a measure becomes a target, it ceases tobe a good measure.” But occasionally I run into folks who study developer productivity without falling into mag and Abi.

The key to this book is that they d whip people into greater productivity, *friction* that slows them down. Fric a pull request that sits for a couple of code, or spend two days wrangling sc to be a simple API call. Smoothing awa essence of improving Developer Expe getting useful software into the hand: They describe effective developer elements: feedback loops, flow state only find out whether we are on th feedback. The longer the delay betw my phone-map, the longer I walk ir realizing my mistake. If our feedback second element, a flow state, where we things done, improving our products.

depends on our ability to understan means we must be wary of being ov whether it comes in the form of poor] or interruptions that break our flow.

Focusing on developer experience the way of these three elements. Im; leads to better outcomes for the wrangling with infrastructure is m salary, and revenue lost because the sc production.

The bulk of this book is how to develop a program to find these friction points, figuring out which bits are causing the most trouble—and fixing them. It involves metrics, but used to gain a greater understanding of developer experience. While commit frequency is a simple number that’s easy to capture, it can only tell part of the story. Well-chosen developer surveys open up an oftignored perspective, interviewing developers adds vital context to the numbers. It’s tricky to correlate these to the bottom line, but if we can, these metrics can guide us to While Goodhart’s Law remains measurement, a recent one that I 1 incomplete measurement is better t treat it as a clue instead of judgment.” clues.

[&] Foreword By Sarah Drasner “IT WAS A mistake to teach sand to think,” I muttered, as I ran rm -rf node_modules yet again. I wanted to try out a promising new library, but it quickly became clear that its authors had focused solely on their API, giving little thought to how it would fit into the ecosystem or manage its dependencies.

Is this uncommon? Unfortunately not. Internal systems teams frequently disappoint—or lose—developers through neglect of the broader developer journey.

This is precisely why Nicole Forsgren and Abi Noda’s book, Frictionless, is so vital. Even teams that are otherwise thoughtful about their offerings can hemorrhage developer interest and thus, important business, by overlooking the experience as a whole: the data we collect, the observability we provide, our feedback loops, our testing, and so much more.

I've spent much of my own career immersed in this domain. Asa VP of Developer Experience, I1led an organization spanning multiple functions: Analytics teams to surface insights, Developer Relations teams to dogfood and gather community feedback, documentation teams to guide developers, and engineers dedicated to closing critical platform gaps. Today, I lead a ( at Google, responsible for the Web, An infrastructure that underpins all majc Across these roles, one truth re gravitate toward tools and workflow efficient implementation path. But i friction and context-shifting impose comprehension of the system, debu process adherence. This burden ultin of code and the overall experience of tl the products it connects to.

Good developer experience (DevE influences adoption and usage. De product are more likely to grow with i for it within their organizations. Dev] itis critical to the success of any devel Historically, product developmer product’s standalone capabilities. But a product in isolation. If we're ser prioritize features that intersect wi integrations that minimize friction.

It is clear that traditional produc engineering both play a part in cre What may not be clear are other dep think about: Compilers, optimizers, d advocacy. All must work in tandem journey.

Nicole Forsgren has long been ce bringing rigorous insight and meanin

productivity and organizational health. In Frictionless, she goes further and partners with well-known DevEx researcher Abi Noda, unpacking what developer experience really means and why it matters beyond conventional roles and metrics.

They offer both practical guidance and rich case studies for identifying and closing these sometimes hard to diagnose gaps —addressing rough edges, alleviating acute pain points, and reducing cognitive drains. Ever adept at bridging the technical and the executive, they also share pragmatic strategies for securing stakeholder buy-in—an essential precursor to meaningful change.

Much of what Nicole and Abi outline resonates deeply with my own experience. Their recommer quantitative approaches, from selfgenerated data, giving readers tool: tangible and actionable ways. Th frameworks for prioritization, and including span of control and taking r For anyone serious about impr Frictionless is indispensable reading.

Sr. Dire

[&] Introduction THE WAY WE build software is constantly evolving. In recent years, new approaches like continuous delivery, DevOps, and Agile have held significant promise. Today, Al is fundamentally changing how software gets built. Product managers can prototype working applications in hours. Developers can generate entire codebases from natural language descriptions. Non-technical team members can create functional tools that would have taken engineering teams weeks to build just a year ago.

Despite this unprecedented speed in code creation, many organizations find that delivering software to customers is still frustratingly cumbersome. New competitors spring up every minute, customers expectations keep rising, and the pressure to innovate has never been more intense.

The cost of software development inefficiencies is substantial and measurable. CISQ research shows that technical debt costs U.S. companies $1.52 trillion annually, with the average enterprise carrying $3.6 million in tech debt. McKinsey reports that up to 40 percent of development budgets are spent on avoidable rework. Meanwhile, developers reported feeling only 68.4 percent productive on average—that missing 31.6 percent represents roughly $300 billion in lost GDP annu Through our work with hundre using Al extensively, others not—v consistently separates high-perform experience.

Developer experience (DevEx) i building software—the friction devel navigate, and the support they receis the best tools and processes fall short improved intentionally, organization their engineering teams.

Improving DevEx in real-world than technical challenges, includin using data and measurement to targ and leading your teams across your © change.

This book is a practical guide to do: With the advent of Al—perhaps tl software development since the inte: more critical than ever before. Compa Al tools must understand the impact c ensure these tools help developers go f software.

Paradoxically, agentic developmes invest in developer experience, as orga what's good for human developers documentation, well-organized code, requirements.

[&] It’s easy to believe theres a panacea—that the right platform, Al model, or automation will solve everything. But the reality is more complex. While transformations like Al and continuous delivery offer enormous potential, they also introduce new risks and ways of working. To succeed with these transformations, organizations need to make sure their investments truly enable developers to deliver better software—faster, more reliably, and more securely.

We'll show you how to identify sources of friction in your software development lifecycle, how to measure what matters, and how to make sustainable improvements that accelerate delivery —whether your teams are embracing Al tools or sticking with established workflows.

While this guide is written primarily for leaders driving DevEx initiatives at mid-to-large organizations, the lessons apply just as well to smaller teams. And the frameworks and principles we share work across any software development context—from legacy mainframes to cutting-edge Al workflows. We've also seen startups use these approaches to scale faster, reduce burnout, and ship better software.

In the chapters that follow, you'll find everything you need to transform your developer experience—a complete pathway from understanding to action.

Part I explains why DevEx matters, Part II provides a framework for understanding it, and Part III the business case for improvemen step methodology for implementatio: and measuring impact, developing st: stakeholders, and evaluating progres: value. Part V shares practices to mal last.

Throughout, youll find real-wo measuring success and ROI, and pra jumpstart your efforts. Each chapter to create a complete system for De specifically designed this book so yc most relevant to your current challe additional materials and exercises workbook; you'll see an icon indicating resources.

Developer experience isn’t just a lever for transforming how software is reshaping development workflows DevEx will be the ones that move fas future.

Let’s get started.

# PART |

Understanding DevEx UNDERSTANDING DEVELOPER EXPERIENCE is the foundation for everything that follows in this book. Before you can improve DevEx, measure its impact, or build organizat picture of what it actually means—: to your business success, especially a.

gets built.

In this part, we define developer of friction reduction, explore why it’s advantage, and examine the types software delivery. Whether you're a d builds, a manager trying to help you wondering why your engineering org speed your business—or Al tools— give you the conceptual foundation t meaningful change.

[&] Chapter 1 What is Developer Experience?

Developer experience isn't just about making developers happy—it's about removing friction that slows down your entire business.

MORE SPECIFICALLY, DEVELOPER experience captures the quality of interactions developers have around the tools, processes, and people they work with when trying to get their job done. In an era where Al can generate code in minutes, DevEx becomes even more critical because while Al accelerates creation, teams still need robust systems to test, deploy, and maintain that code at scale. By taking a developer-centric view of software development, you can quickly identify bottlenecks and friction that block innovation, quality, and productivity.

Market forces are making DevEx more critical than ever.

Increased market pressure, increasing system complexity, and advances in Al capabilities mean that organizations need to deliver value to their users and customers faster than ever before—which is where DevEx steps in.

Al is reshaping how software gets built, with tools that can generate working code in minutes a to create functional prototypes. M traditional development tasks like pat detection. This transformation acro might seem like it would reduce t experience—after all, if AI can hand why worry about developer frictio: While AI accelerates many tasks, tea to validate Al-generated changes, coo and maintain oversight of increasin fundamentals of developer experienc optimizing feedback loops, and mai even more critical when your team is alongside human-written code.

Al represents the latest chapter in that developer experience matters to developer experience has been aroun into the components and impacts mid-2000s. The rise of the internet a Amazon made it clear that software a support function—it was central t elevated developer productivity from strategic priority. A variety of intercor this increased attention: - Growing complexity in microservices created new sou raised the stakes for deploymen + Increasing reach of thought le showed more developers what

«Developers with experience from companies with advanced tooling (such as Google) began questioning practices at other companies.

+ The open source experience improved, raising expectations.

«+ Influential books like The Phoenix Project, Accelerate, and work from SVPG (whose books include Inspired and Transformed) brought visibility beyond engineering teams to business leaders.

. Additional research provided evidence and frameworks to address developer friction and productivity systematically.

These developments revealed both a problem and an opportunity. Together, they highlighted how friction in software development was significantly constraining productivity and innovation potential. At the same time, they shined a spotlight (© on how improving developer experience could deliver more value faster than ever before.

This is about “developer experience,” but who exactly are developers?

When we refer to developers, we mean core builder roles: Software engineers, quality engineers, build/release engineers, and similar technical roles directly involved in creating and deploying software. While product managers, designers, and other roles are important to the development process, they create different artifacts and present measurement challenges that make them less suitable for DevEx initiatives.

Many companies recognize this and adapt their terminology accordingly: + Amazon calls it “builder ex; technical roles.

+ Spotify uses “R&D experience organization.

- Other companies use terms li or “maker experience.” Al is reshaping who gets tc creation. Product managers, desig: increasingly use Al tools to generate traditional role boundaries. This d opportunities and new considera maintenance, and system architect

[&] Chapter 2 Why Developer Experience Matters Poor developer experience isn't just about productivity—it can hide catastrophic business risks in plain sight.

ONE MORNING IN 2012, a developer at Knight Capital pushed a routine update. Nothing seemed off—until the system started hemorrhaging money. In just 45 minutes, a single change triggered $460 million in losses.

The culprit? An old feature flag, long retired, accidentally reactivated by a deployment script. But the real problem wasn’t the bug—it was a development environment that made problems impossible to detect and fix quickly, turning a routine mistake into a company-ending disaster. Knight Capital's developers worked without automated test suites, relied on error-prone manual deployments, and had no monitoring systems to catch issues quickly.

Fast-forward to July 2025: Jason Lemkin was using Replit’s Al coding assistant to build a database for his company SaaStr.Al.

He explicitly set a “code freeze”—no changes to live data. But the AI ignored his instructions and database.2 The incident sent shockv community and raised urgent questio Here's what's telling: if you had as} about their technology strategy, th trading algorithms, market data, or asked Lemkin about AI coding tools | have focused on productivity gains an tweets echo this sentiment). But if y« and operators about their daily exp: deployment process, the anxiety of ir could place in their tools—you wou risks.

Today, as Al accelerates developr these same friction points become ¢ you can generate and deploy code fa: monitoring, and deployment proces: they're essential guardrails against Al Developer experience work starts perspective. Instead of asking, “How we ask, “What is it actually like to b The answers reveal where business toward solutions that protect everyo tooling, and developers who can foc fighting their tools.

Knight Capital didn’t survive, bu developer's daily experience isn’t just business survival.

[&] Knight Capital's story isn't unique—it reflects a broader reality about modern business. It may be a cliche, but every company today is a software company. Retail, banking, manufacturing, healthcare—all rely on software to compete and serve customers.

Al is lowering the barriers to software creation across entire organizations, enabling teams that never wrote code to build working solutions. Yet most organizations find themselves constrained by friction in their development processes that prevent them from delivering at the pace the market demands.

Friction appears everywhere in modern development workflows.

This includes cumbersome setup procedures that take days, security reviews that create bottlenecks, flaky deployment pipelines that break without warning, and documentation scattered across a dozen different tools. Al tools can help with some of these challenges—automating setup scripts or surfacing answers from documentation—but they also introduce new friction points: Managing Al tool access, validating Al-generated solutions, and integrating AI workflows with existing processes.

Like a rusty bicycle chain, poor developer experience creates drag on everything—fixing bugs, shipping features, or innovating on new ideas. While your developers spend their energy overcoming these persistent hurdles, they have little capacity left to solve hard problems or create breakthrough solutions.

AI acceleration makes existing friction even more costly. As Al transforms development workflows, a new dynamic emerges: Friction that was manageable at slower speeds becomes a serious bottleneck. When developers can generate code in minutes but deployments take hours, or when Al can suggest dozens of solutions but testing infrastructure can’t validate them quickly, the constraint shifts from creation to validation and Meanwhile, developers face new c to prompt Al tools effectively, valid: managing the constant context switc traditional workflows. These interr increase mental overhead, making sr even more valuable. The faster code ge becomes to eliminate downstream fri cognitive capacity for high-value worl This shifting bottleneck is why v need metrics and data that signal development pipeline, helping you i before it undermines your Al invest gains.

Poor DevEx creates a comp compounds over time. Friction in soft slows feature development and innov to experiment and learn. When yot the features and novel solutions th removed these barriers—and are tl innovate, and ship quickly—can rapid In an era where AI democratizes softw compound even faster—making de competitive differentiator.

How LinkedIn eliminated friction an transformed their business.

In October 2011, LinkedIn was a | paper, but behind the scenes, the c

was drowning in friction?. Engineers spent their days wrestling with internal systems instead of building features for users. The friction had become so severe that LinkedIn could only deploy new features once per month, while competitors shipped daily updates.

Newly appointed VP of Engineering Kevin Scott made a radical decision: Freeze all feature development for two months and eliminate the friction. Project InVersion would rebuild LinkedIn’s development infrastructure from scratch, giving every engineer the tools they needed to move fast. The company actually dismantled their old systems halfway through—there was no going back.

The results were transformative. Within weeks of Project InVersion’s completion, LinkedIn went from monthly deployments to multiple releases per day. Engineers who had been frustrated and leaving for other companies were suddenly energized, spending their time on innovation instead of fighting broken tools. The business acceleration was immediate —outside observers noticed LinkedIn’s products improving at an unprecedented pace.

By removing the friction that had been silently strangling the company’s growth, LinkedIn unlocked its team’s full potential and secured its competitive advantage for years to come.

Developer experience has a positioning problem. This stems from a fundamental misunderstanding of what good DevEx actually delivers. Many leaders (and some engineers) haven't personally experienced how transformative an efficient, easy-touse development workflow can beautomation and process improvemen business impact.

That's why it’s crucial to commun with evidence—that DevEX initiatives investment. This book will show yo case. In the following chapters, we'll frameworks that demonstrate DevE quality, and business outcomes.

Good developer experience isn’t j happy—it’s about removing fricti outcomes. But that framing gets f DevEx is about systematically remov: create value. Better tools—whether t improved deployment pipelines—are are clearer processes, fast feedback loc immediate deployment feedback), anc Developers want to code, and tt an impact. But they also want con work reliably. This becomes especial faster code generation amplifies the c unpredictable failures. By making it and ship software safely, you not onl; the business, but this also creates mor Happier, more productive deve meaningful developers generate mc satisfaction for developers comes fron environment that supports great worl

Faster value delivery —>—=e Less friction in tools and process Happier more productive developers Organizations with excellent developer experience gain a decisive competitive advantage. Their developers can focus on innovating and solving problems rather than fighting with their tools; avoid time-consuming (and mind-numbing) repetitive tasks; and write software that is safer, more secure, and more reliable.

This creates a compounding benefit: Fewer incidents and bugs mean fewer interruptions, providing developers with the continued focus they need to deliver great work. The organization benefits through faster delivery of software solutions that better serve customers and the business.

DevEx and platform engineering: Different approaches, shared goals.

We're often asked: “What's the difference between developer experience and platform engineering?” While they’re closely related, they represent differen developer friction.

Platform engineering focuses infrastructure, tools, and services t foundation. It’s about building a sh: enforces best practices and abstrac is one of the ways to improve deve teams typically own and maintain t as internal products to developmen Developer experience takes a throughout the entire developm everything from onboarding and c: and monitoring. DevEx initiatives nn require platform engineering solu address friction points in processe dynamics that no platform could so Many organizations that succe experience do so by combining DevEx principles to identify frict engineering as one of their Hf eliminating common technical hurc Al tooling represents a particuls of these approaches. Platform standardized AI development envir while DevEx initiatives focus on hc integrates into developers’ day-to-d: This creates a virtuous cycle.

architectural solution that reduces

load and feedback loops, while DevEx is more general and optimizes the broader development process.* Many organizations wrongly believe that improving developer experience competes with their goals for value delivery. They think of it as a distraction or competing interest to speed and efficiency.

In reality, it’s the opposite.

Developer experience acts as a that understand the value of thei them the tools to do their jobs effe delivery and better customer outco about slowing down for comfort—it’ acceleration.

[&] Chapter 3 Friction: The Value Killer Friction can slow any progress, especially in software, which is why improving DevEx is so important.

RIGHT NOW, A newly hired software developer is starting her third week at a promising tech company, still waiting for database access and parsing through outdated documentation. Her first pull request —which included some Al-generated code—sits untouched for days because no one knows whose turn it is to review Al-assisted work, there’s no clear process for validating Al outputs, and she doesn’t have access to the Al-powered code review tools that could help catch issues faster. The build pipeline randomly crashes—a known issue the platform team keeps promising to fix “next sprint.” When the developer finally tries to deploy a simple change, she discovers it requires manual coordination across three teams with separate approval workflows—none of which account for the faster iteration cycles supported by new Al tools. As another day wraps up with more time spent navigating obstacles than building features, this new hire wonders if there might be a better way to work.

Friction is anything that slows down or gets in the way of completing work. It can surface as unclear processes, missing documentation, complicated toolchaj And friction in your system can kill : improvements you get from Al Today, friction appears everywh —from onboarding delays and brit and complex deployment processes.

compounding delays that impact tin position. As AI transforms develop: friction points become even more ex generate code faster but still can’t deli Al investments constrained by famili friction we commonly see include: - Onboarding friction. New weeks struggling with incomy for system access approvals toolsets before writing a sin Even experienced developers laptop refreshes or system time during active sprints w most needed. Remote develop in documentation because re scheduling a meeting.

- Codebase friction. Insufficient to touch many places to m monolithic fixtures accumulate to extend, and patterns that onc obstacles as the system evolves.

- Integration friction. Misconfi; toolchains break developer flc

cc = seamless connections into frustrating workarounds and manual steps.

Process friction. Multi-step approval processes, several iterations of review, and bureaucratic requirements often delay actual development work. The cost of this friction often becomes apparent during hackathons when process requirements are relaxed and innovation happens quickly.

Review friction. Code reviews that should take hours stretch into days due to inefficient PR assignment, unclear code or module ownership (especially in monorepo environments), multiple review cycles caused by unclear requirements, and large and complicated PRs due to developers working in isolation.

Development friction. Painfully slow build times, test suites that are unreliable and take ages to complete, incomplete test coverage, and flaky tests that fail intermittently without real issues waste developers’ time and break concentration during active coding sessions.

Deployment friction. Rather than one-click deploys, developers write custom scripts for every code push because automation is incomplete, or spend hours manually gathering data from disparate systems to make deployment decisions.

Each of these friction points doesn’t just slow down individual developers, it creates compounding delays and context-switching that significantly impact a company’s time to market and competitive position.

While developers can sometimes move on to other tasks while waiting, these unpredictable delays force them to juggle multiple workstreams—breaking their concer deeply on important problems. This just hurt productivity—it creates and frustration that leads to burn this fragmented attention and burr developers and dozens of deployment: at months of lost innovation every ye: Eliminating these friction points value. Each barrier removed doesn’t ji developers’ ability to focus and do v innovation cycles.

Teams freed from onboarding hur of weeks.

Engineers liberated from toolchai problems rather than fighting their to Developers with access to Al codir validation processes can rapidly prot that would have taken weeks to build: Streamlined reviews and fundamentally change how quickly id The impact is compelling: Even m friction can dramatically increase market responsiveness. While remc developer satisfaction and improve get work done, this isn't just about « removing the invisible tax that’s 1 growth all along.

DevEx can mean many things—we sf

As we've worked with developers and leaders across hundreds of organizations, we've seen that improving DevEx can mean different things to different people: 1. Reducing friction. Framing the improvement of developer experience as the reduction of friction enables teams to easily understand what to look for (slowness, blockers, confusion, complexity, inefficiencies) and work to remove them. And you can talk with business leaders about how delays in your ability to deliver software chips away at the organization’s ability to serve customers, accelerate revenue, and capture market share.

2. An organizational strategy. When a company invests in reducing friction and improving the developer experience, we often say they have a “DevEx strategy” or a “DevEx team.” In this case, improving DevEx encompasses the idea that developer experience is about removing friction, a business understanding that software friction reduces possible value, and formally supported efforts to improve it—whether through resourcing, capital, or even regular reporting with leadership.

3. A source of data and insights. In many organizations, “DevEx” refers to the metrics, dashboards, and reporting that communicate developer productivity and experience.

This includes system-generated data (such as deployment frequencies, build times, and failure rates) as well as qualitative feedback from surveys and interviews. These measurements —when done thoughtfully and with shared understanding of the data and metrics—can become an important shared language between engineering teams and leadership, though each team needs their own views. More specifically, engineering teams benefit from granular metr; optimization, while leadership nee business impacts to make strategic.

In this book, we start with foundation for improving DevEx, t strategy, measurement, and organiz foundation. This approach is immec of your organizational context—in and address friction points withou or dedicated resources. But we'll als these efforts with strategic frames and change management approache DevEx improvements across your of “Productivity” sets off alarm conversations. The focus on reduci business outcomes is related to produ baggage. The term productivity often t metrics and micromanagement, kt school brand of Taylorism where ms standardization at the expense of de and job satisfaction. It also brings tor measure becomes a target, it ceases t teams to optimize for metrics rather t In contrast, the term experiences obstacles and enabling better work.

and productivity aren't exactly the sa framing matters tremendously wher and momentum for improvement.

By focusing on experience rather than raw output, you create space to explore what truly enables developers to do their best work —which is where our three-part framework comes in.

© [&]

# PART II

The Three Essential Elements of DevEx YOU NOW HAVE the foundation for understanding and improving developer experience. DevEx isn’t about developer perks or satisfaction—it’s about systemati constrains your entire business. W energy fighting tools, waiting for fee processes, they have little capacity lef solving.

Our three-element framework gi identifying and addressing this frictic to accelerate decision-making, prote deep work, and reducing cognitive for complex challenges. These elemer —while AI and new technologies c techniques, the fundamental develop constant. The elements reinforce on one area often unlock gains in the o benefits for both developer productivi

Chapter 4 The DevEx Framework Three essential elements can take your DevEx from good to great.

WHILE A FEW frameworks exist to think about developer experience more concretely, we have developed one that is both simple and comprehensive, with a focus on three specific elements: feedback loops, flow state, and cognitive load. We've chosen (© these three elements because they capture both the technical and psychological dimensions of a developer's daily work—whether they're co-located, distributed across time zones, or increasingly augmented by Al tools.

These three elements—feedbas cognitive load—are each important help reinforce one another. For exa: important in all work—for develope answers to questions quickly, being a knowing whether a build passed. Sl in developers moving onto another state—a challenge particularly acute synchronous communication windo can help bridge these gaps by pro to common questions or debuggis colleagues aren't available. When d come, this negatively impacts cogni have to get back up to speed on the pre Organizations that successfully o will experience measurable improvernr lead time, and product quality—all of impact revenue growth, market respo

[&] Chapter 5 Feedback Loops Fast feedback is the multiplier that accelerates innovation and quality.

FAST FEEDBACK LOOPS help developers know whether code works (is it correct, performant, secure) and whether ideas are good (do they improve key business metrics). This may seem obvious, but far too often, teams and organizations tolerate slow feedback loops because, “it’s always been this way” or maybe, “You can do other things while you wait.” We've also heard, “Others seem fine with it,” or “This is not a priority.” But creating value quickly is about much more than just reducing delays and bottlenecks in systems.

It’s also about providing important context and information so that developers can do work efficiently.

Slow feedback interrupts the development process. This leads to frustration and delays as developers wait or decide to switch tasks. In some cases, developers frustrated by slow feedback loops may find their own ways to avoid friction, with risky shortcuts like skipping code reviews, merging untested changes, or deploying without following established processes. This, of course, introduces an entirely new set of problems.

Slow feedback loops also cause a feedback from systems (such as an i (such as review notes) is returned and This connects directly to our next slower the feedback loop, the harder i their mental model and do the require Little’s Law from queuing theory are so costly: Longer latency means that developers must juggle simulta working memory.Z Research from University of California Irvine confirn interruption while waiting for test switches that waste up to 15-30 perce time.2 You can shorten feedback loops developers often need information an it. Good examples here are outcon processes (e.g., build and test result setup) and information needed fro: code review). Al tools can also th providing answers about codebases o faster than someone could get by as documentation. By prioritizing these enable both faster delivery and supporting the flow state we address i

Chapter 6 Flow State Flow state is the productivity multiplier that transforms good developers into great ones.

WHEN DEVELOPERS SAY they can get “into the flow” or are “in the zone,” they're talking about flow state—a condition of complete immersion in an activity with energized focus and personal enjoyment. Getting into that state—and staying there for as long as possible—is crucial for solving complex problems, debugging difficult code bases, and fostering creativity. As Cal Newport argues in his research on deep work, complex cognitive tasks require sustained, concentrated blocks of time to produce meaningful results.2 This need has only intensified as software systems grow more complex—microservices architectures, distributed systems, and Al integration create contexts that demand deeper concentration than ever before. Organizational structures can also work against flow—when key developers are repeatedly pulled into meetings or scoping sessions because of their expertise, their ability to achieve deep focus suffers.

Research shows that flow state at work leads to higher productivity, innovation, satisfaction, and learning.l21 Research also suggests that professionals productive when they achieve this opt Effective feedback loops are cr When feedback is timely and reliable, in their work. This is where AI toc answering questions and unblockin, stay in the flow. However, broken o interruptions and shatter flow—whet results that force context switching hc that require immediate attention.

Finally, having autonomy in work contributes to flow, because it allows d their tasks. Studies have found that de perform better and produce higher-qu What does this mean practically: identifying ways to support flow s tooling and automation, improving processes, or minimizing disruptio: rearrange meetings to create blocks of quality gates to avoid reactive work, : code review.

Leaders should also recognize f creating positive team cultures tha and opportunities to work on fulfi going beyond optimizing tools and psychological safety, provide meanir give developers the freedom to mal these cultural elements are in place, rather than requiring constant effort t

© [&] o=—o Remote and hybrid work: DevEx challenges and opportunities.

The shift to remote and hybrid work has fundamentally changed developer experience, creating both new friction points and unexpected advantages.

New challenges: Increased meeting overhead disrupts flow more severely when mediated through video calls.

Async communication delays slow feedback loops, especially across time zones.

Home environment distractions make achieving deep focus more difficult.

Working across time zones creates scheduling friction and excludes team members from key decisions.

“Zoom fatigue” reduces cognitive capacity for complex problem-solving.

Hidden opportunities: Flexible schedules allow developers to work during their peak energy hours.

Al-powered meeting transcription and note-taking tools support global teams by making meetings accessible regardless of attendance.

Reduced office interruptions can actually improve flow state duration.

Personalized home offices optimize individual work preferences.

Global talent access enables 2 when managed well.

Well-planned meeting sched: predictable focus time ratl workday.

Organizations that successfully to remote organizations often se exceed pre-remote levels. The key is distributed work rather than simply to video calls.

[&] Chapter 7 Cognitive Load Writing software is already complex—we shouldn't make it harder.

DEVELOPERS FACE GROWING cognitive load in their work, from complex systems with large (sometimes legacy) codebases and interdependencies to the ever-growing number of tools and technologies they use. In the context of DevEx, cognitive load is “the amount of mental processing required for a developer to perform a task.”1¢ For example, difficult tasks have higher cognitive load, and having to work with a complicated interface or across several systems or tools can increase cognitive load as well. Cognitive load varies according to how information is presented, and increases when mental processing is required for translating information into longer-term domain knowledge and models.

Excessive cognitive load directly impedes developers’ ability to deliver value to customers. When developers face poorly documented code, fragmented systems, or toil—manual, repetitive tasks that don’t provide enduring value, such as manual compliance checks—they must devote extra time and mental energy to complete even routine tasks and avoid mistakes. This challenge is particularly acute when working with legacy systems, where developers must simultane architectural decisions, navigate a integrate with modern tooling and pr: Frequent interruptions further breaking flow and forcing conte: productivity and increases ment: development, increases error rates, an time, as developers spend valuable co work that could be automated.

The relationship between cognit elements is clear—unnecessary mer redundant work makes it more diffict problems and achieve flow state. And cognitive load by requiring develoy models when context switching. T.

significantly degrade the developer ex The solution is systematic complexity. To improve develop organizations should aim to reduce u eliminating hurdles in the developr code and documentation facilitate dex systems they work with and reduce t switching required to complete their experience and platform teams can pr tools that help developers streamlin and release. (We explore specific aj tools and teams in Chapter 52.) This coordination around tooling choices tt of managing dozens of different platf

is to allow developers to focus their mental energy on solving the inherent complexities of their work rather than wrestling with avoidable ones.

AI presents both opportunities and risks for cognitive load.

Al tooling can help cognitive load by helping devs move through routine work quickly. But Al can al interrupting complex tasks or gener review and expensive to maintain lon Al, but to deliberately maximize its b to minimize its downsides.

Chapter 8 Use the Framework to Identify and Remove Friction The three elements of DevEx provide a framework for spotting and fixing friction.

THE ACTIONS YOU take to improve any DevEx element reduces (© friction. And when you think of the friction you want to remove, it can be helpful to associate it with one of these elements. That will help you design a better solution and think of better ways to measure it. (We cover metrics in detail in Step 3.) This isn’t just about frameworks—it’s about action and implementation. Understanding the three dimensions of developer experience—feedback loops, flow state, and cognitive load— provides you with a powerful lens for identifying friction. But identifying problems is only half the battle; you need a structured approach to solve them.

Poor DevEx hurts more than just ripple effects throughout the enti developer experience is about frictio: everyone. When developers struggle infrastructure, or fragmented tools, tt For businesses: Slower tin costs from inefficient process advantage.

For leaders: Unpredictable c planning, and challenges retain For teams: More meetings increased context switching, an The beauty of focusing on im improvements compound—when yor you often get unexpected benefits in might require tailored solutions (suct or clarifying work definitions), ad points creates organization-wide effici the initial investment.

As we'll see in the next chapter, n for DevEx means connecting these fric leadership already cares about.

# PART Ill

Making the Business Case UNDERSTANDING DEVELOPER EXPERIENCE and its business impact is just the beginning. The real challenge is securing the resources and organizational support needed to make meaningful (© improvements. Most DevEx initiatives fail not because of poor technical execution, but because they their value to decision-makers.

In this part, we explore how succ developer pain points into compelling with executives. You'll learn how to « to financial outcomes, align with exi position your work as a solution t concerns. These approaches are desig specific tools and technologies you ad and other innovations, the fundamer problems, gathering data, and con remain constant. Whether you're seel improvements or defending existing will show you proven approaches for

[&] Chapter 9 Translate Developer Experience into Business Value C-suite executives speak the language of business outcomes.

WHILE “IMPROVING DEVELOPER satisfaction” or reducing lead times” might resonate with engineering leaders, executive decisionmakers need to see clear connections to financial impact. Business leaders are evaluated on metrics like revenue growth, profitability, and market share—so your DevEx proposals must connect directly to these financial outcomes.

This doesn’t mean executives don’t care about developer wellbeing. Rather, they need to understand how developer experience investments translate to business results. This financial framing is crucial when selling your strategy (Step 5) and demonstrating value (Step 7).

Talk about recovering time: Convert developer hours into dollar value. Developer time has clear financial value. You can: Measure hours spent on unnecessary toil or waiting for builds/tests.

Multiply this time by the fully loaded hourly cost of developers.

Present these savings as “recap “free headcount.” For example, if your team of 50 de weekly on build-related delays at a hour, that’s $25,000 in weekly produ annually.

Alternatively, express this as “free developers x 5 hours lost weekly = 2 on a 40-hour workweek, that’s equival developers without increasing your bs particularly well when hiring freeze: labor markets. To safeguard your ct measure real, credible time savings.

The financial impact is substa: developer experience, those benef developer who recovers just 10 perc tooling friction represents $25,000 in across an entire engineering organi: dozens or hundreds of “free” develope But the benefits don’t stop the organizations to build, experiment creating business value that can cl that’s before accounting for the com timelines, team morale, and customer Etsy’s $2.5M DevEx investment: A business case in action.

As Etsy’s engineering team rapidly grew from 250 to nearly «Lower infrastructure costs thro 1,000 developers, leadership recognized that productivity that require less processing pow would suffer without investment in developer experience. + Minimize expensive productic CTO Mike Fisher's approach to securing buy-in was quality controls.

straightforward: Translate improvements into business language. Instead of explaining technical changes to When making your business ca: deployment processes, he told executives the work would save savings with specific projections whe 50 percent of engineering hours spent waiting for deployments both the immediate savings from —equivalent to a quarter of a full-time engineer’s salary. The developers ship features faster with result was an initiative that dedicated 20 percent of engineering term savings from improved talent 1 capacity to improve DevEx in four key areas: Crafting products, strongly to initiatives that demons developing and deploying, building with data, and reducing reduction while maintaining or imprc toil.

The initiative, which took 18 months, was so successful Co i . Strategic standardization: How Blocl o that it led to ongoing investment in developer-experience work, | delivered millions in savings.

integrated into Etsy’s standard operations. Their key insight: . ) Seal 1 d technol tozeth ductivic Block is a leading fintech comy cale people, process, and technology together, or productivif . i peop, p Ey tog P y like Square, CashApp, and Tid: suffers regardless of growth.1Z == = standardization for its own sake, strategy on consolidating tools to c Talk about saving money: Quantify cost savings. Improved paths for developers.

developer experience delivers tangible cost savings that directly When making their business ca impact your financial statements. By enhancing automation, focused on abstract benefits such : streamlining workflows, and eliminating redundancies, you can code throughput. Instead, they fo substantially reduce operational expenses. that engineering friction and avo For example, strategic DevEx investments can: were having on the business.

- Decrease vendor costs through process optimization and tool The business-focused approach consolidation. experience initiative was funded - Reduce cloud computing expenses by improving test results in 12 months. Thanks efficiency (eliminating redundant tests). developer environments, golden p

saw millions of dollars in documented savings and double-digit improvements in developer satisfaction scores.1& Talk about making money: Accelerating revenue through DevEx. While developer experience initiatives aren't direct revenue generators, they significantly accelerate your existing revenue streams. For software-driven companies, revenue growth depends on five key factors: 1. Feature velocity (how quickly new capabilities reach customers).

2. Feature quality (how well new capabilities meet customer needs).

3. Experimentation speed (how quickly you can test and iterate on new ideas).

4. Service reliability (how consistently your products perform).

5. Security posture (how well you protect customer data and trust).

All five factors depend on effective developer workflows.

Consider the AI transformation, where companies racing to integrate Al capabilities into their products are pursuing increased revenue, competitive advantage, and expanded market share.

However, these Al features must be: - Designed and coded.

- Reviewed for quality.

+ Built and tested.

- Integrated into existing systems and products.

- Securely deployed.

- Maintained and improved.

When developers wrestle with sub processes, these technical bottleneck Your company faces delayed market and security vulnerabilities—all direc Consider this: If competitors relea your team needs six months due to v not just accumulating technical deb revenue losses and diminishing ma investments create a multiplier effec deliver more value faster, enhancing r market opportunities before competit Accelerating revenue growth: Capital One's DevEx transformation.

Capital One dramatically transfor: by strategically investing in devel infrastructure.

Before their DevEx overhaul, products took 6-9 months, limiting agility. By standardizing dex implementing modern CI/CD pipel native technologies, Capital One s!

months to weeks or days.

The business impact was fas deployment cycles meant Capital opportunities before competitors, r needs, and optimize revenue-gener: iteration.

[&] Capital One secured executive buy-in by directly connecting their DevEx investments to accelerated time-to-market and customer acquisition—metrics that translate directly to revenue growth. Their story demonstrates how improving developer workflows isn’t just a technical win—it’s a powerful revenue accelerator.

Talk about proven correlations: Link technical metrics to business outcomes. Sometimes the most powerful business cases come from identifying correlations between technical metrics and business outcomes.

In How to Measure Anything,2 Douglas Hubbard writes, “If you can correlate two things to each other, and then if you can correlate one of them to money, then you can express them both in terms of money.” At eBay, a breakthrough analysis showed that every 10 millisecond improvement in page speed translated to millions of dollars in increased web purchases. This correlation transformed how the business viewed page speed—from a technical concern to a critical revenue driver deserving investment.

A specific example of this approach is the developer experience index (DXI), developed by DX. The DXI score is the average of 14 survey questions that ask developers about different aspects of their development process. By correlating this score against self-reported time loss, DX has found that each one-point gain in DXI score translates to saving 13 minutes per week per developer, equivalent to 10 hours annually.2 This correlation allows organizations to predict financial impact from DevEx improvements.

You can apply this same approach to developer experience: «Correlate developer satisfaction market.

+ Link build system reliability to + Connect onboarding experience hire productivity.

However, be cautious of trying tc metric straight to revenue—a commo: leaders attempt this, they don’t know they give up trying to convince their their work.

Storytelling matters more than the ¢ When building your DevEx busines of good. Many leaders get stuck ti precise ROI figures or collect perfec rarely necessary.

In most situations, reasonably —what really matters is how yo compelling narrative. While data po proof points, they need a clear, conc decision-makers.

Remember: Even the most impr for themselves. Your presentation and understanding of your audienc determine whether your business this more in Step 5: Sell Your Strateg

[&] Chapter 10 Connect Your Work to What Others Care About To gain leadership support, demonstrate how developer experience directly solves their specific business problems.

FOR MANY LEADERS, developer experience isn’t their number one priority or concern, which makes it difficult for them to rally behind improving it. So instead of spending energy evangelizing developer experience, focus on connecting it to things executives care about, such as meeting performance targets, securing bonuses, advancing careers, or maintaining their positions in a field where the average technology executive tenure is under two years.

Align your DevEx work with the problems that keep your CEO and CTO up at night. Understanding your leadership's key understanding allows you to frame developer experience initiatives in terms they already prioritize. When you align your DevEx messaging with existing executive priorities, you transform from competing for attention to directly supporting strategic objectives.

How Block turned a DevEx report inf priority with one word change.

When Block’s Developer Experie “State of Developer Experience” findings and opportunities, they before publication. Recognizing “ key business priority, team lead rebranded the report “State of Engir The result was striking: The CT the report and advocated for its w content remained unchanged, the perfectly with leadership's articul: reframing transformed a standard addressing the CEO’s most pressing This example demonstrates th what keeps senior leaders awake at 1 work as directly addressing those allies rather than competing for atte Tie it to your company’s biggest p immediate traction when they direc most critical objectives. Rather Hf experience as a separate concern, fi existing strategic priorities.

How Plaid transformed DevEx from a cost center to a strategic enabler.

At fintech company Plaid, which builds software to integrate users’ bank accounts into digital experiences, their DevEx leader initially struggled to convince leadership of his team’s value. Weeks of discussions about engineering efficiency metrics and potential cost savings failed to gain executive buyin.

Recognizing the need for a new approach, this leader identified that one-third of engineers had been reassigned to a new product development initiative deemed PO (highest priority) by the CEO. Each week of delay threatened the company’s market position.

Instead of continuing to push general efficiency metrics, they reframed his team’s mission: To specifically accelerate this critical product development. By positioning DevEx as directly supporting the company’s most urgent priority, he instantly secured CEO approval.

This strategic pivot illustrates an important principle: DevEx initiatives positioned as enablers for existing company priorities—especially those labeled PO—get substantially more support than those presented in isolation. Connect your DevEx efforts directly to your organization's most pressing business objectives.

Give senior leaders something to brag about. Every leader needs accomplishments to highlight in their own performance reviews. Your CTO reports to the CEO, of whom want tangible wins to showc When positioning developer-ex outcomes as impressive metrics lead their own performance reports. A ( “We've increased engineering veloci reduced regrettable attrition by 20 pe DevEx program,” has powerful ammus leadership impact.

Reveal performance gaps. Leads possible in developer experience, wh seem less urgent. When you show are doing, it creates that “aha!” mor example, if your leaders knew that si in hours (not weeks), or that their de fighting build failures, they'd proba organization isn’t there yet.

It’s not about competition—it’s what’s possible. This works because v conversations. Nobody wants to loo} nobody wants to realize they've bee: high performance is achievable and table.

Always reframe developer experie have into a strategic business enable isn’t about preaching developer expe it to business outcomes. By alignir supporting critical company initiat

leaders can showcase, you transform DevEx from a technical concern into a strategic advantage.

When advocating for investments, don’t ask, “How can I convince them to care about developer experience?” Instead, ask, “How does my work solve their most pressing problems?” This perspective turns skeptics into allies.

# PART IV

Improving DevEx: A 7-Step Process IMPROVING DEVELOPER EXPERIENCE doesn’t happen by accident —it requires a systematic approach that builds momentum while delivering measurable results. The following seven steps provide a practical framework for driving DevEx improvements, whether you're working within a single team or across an entire organization.

Our 7-step process will guide your implementation: In Steps 1 and 2, you'll learn how to start your DevEx journey and get quick wins by identifyir points across all three elements Steps 3 and 4 show you how tot of friction, and then develop highest-impact areas first.

In Steps 5 and 6, you'll learn stakeholders by connecting Dey outcomes, and then drive ct appropriate for your organizati Finally, Step 7 provides tools by measuring improvements ¢ demonstrating their business v This process is designed to be You'll cycle through these steps mult; building on the insights and credibil one. Start where it makes sense ft worry about perfecting each step befo: maintaining momentum while contir your approach.

# STEP 1

Start Your DevEx Journey WHETHER YOU'RE STARTING at a new company, stepping into a new role at your existing company to kick off DevEx improvement efforts, or pulling together a grassroots effort, start by talking to your customers—that is, developers—about their work. Ask them to tell you how they get their work done, their favorite tools, (© what tricks they love, what frustrates them, what makes it hard to onboard new engineers, what tools or processes create friction.

You'll find that developers love sha: systems are both great and broken.

Don't skip this step. It reveals is: you've been in the organization for y how problems impact developers, c stories that illustrate the scope and s you value their input.

From a change management pe: sponsorship is a top priority—inadeq greatest barrier to an initiatives st you often need developer insights that executives will support. This cr with some discovery to build your alignment if you already have clear (We'll cover how to secure resources : your initiative in The First Practice.)

have a representative sample, plan s such as years of experience, product a legacy, mobile, cloud, data science).

Make two planning lists: Chapter 11 1. Demographics that matter. 1 (onsite, remote, hybrid) and ex Interview Developers devs), 2. Work types and organizational These lists will hel; t The best way to find developer friction is by asking developers. ese lists will help you map ou track who you've spoken with. Here's : START WITH A listening tour. Your goal is to understand . Interviews Devs by Demographic your developers software development experience, or as Courtney . . . . Experience level Kissler, SVP and CIO at Expeditors, says, “Honor their reality.” . . . . i. Where they Number of Jr dev Sr dev Listen without defensiveness or explanations, and remember it’s Wek interviews (© not your role to judge their reality. Stay curious, asking for details Mobile p a 2 when needed. Note helpful practices, but avoid soliciting solutions Web s | 4 —neither you nor they have the full picture yet, and they aren’t thinking like strategic product owners. PIEHom 4 To get good information, you'll need to interview a diverse Legacy 2 2 set of developers. Looking back at our own work with teams Totals = 5 po and organizations, meeting with developers from many parts of the organization has always paid off. When you do this, you gain You'll notice a few things here.

insights to tooling, processes, and other quirks that may appear to multiple demographic categories : differently in different teams. It cues you into naming differences .

a senior developer who recently star across teams and organizations, even though the tooling and . .

ganizations, ev ug ng dev” (in the experience level categ rocesses may actually be the same. ns Pp y actualy tenure category). However, within e: To be most effective, you'll want to talk to 12-15 developers (we'll .

are mutually exclusive—someone car discuss how we got to this number in just a bit). And to ensure you _ dev” simultaneously.

This categorization helps you see who you are talking to—and maybe just as important, who you are not talking to. You can quickly see in the table above that you're relatively balanced between new hires and long-time employees, but don’t have interviews scheduled with junior devs in platform and legacy teams. That may be intentional (e.g., the legacy team might not have any junior devs) or it might be a simple oversight. Having this visualization helps you spot those gaps and correct them before you make decisions based on incomplete data.

You may also notice we included a column for “Underrepresented;” our experience—and research—has found that developers who are underrepresented often face different challenges in their work. These different experiences may be due to company culture or unconscious bias, but it’s useful to include this in your selection map. Research has also found that improving software development to help groups who are underrepresented in technology populations improves development for everyone.2L Let developers know that talking to you is a good use of their time. You can set yourself up for success by sending out short notes introducing yourself and your work and asking for a quick, 30minute meeting. Depending on the team and organizational culture, these notes will be either emails or chat messages. (See the Step 1 Workbook for example templates.) Make sure you have buffer time in between interviews to refine your notes from each meeting. But remember that this extra time is only for you—be respectful of your developers’ time.

Building strong developer experience starts with earning developers’ trust. Developers will only share their honest experiences with you if they trust you—and building that trust starts from your very first interaction Many developers have repeatedly work environment, only to be dismi makes it crucial to show them that y ready to act. Here’s how you can build Lead by example. Be vulne frustrations and learning mom way street.

Show respect. Be respectful appreciation for their work, ex share with you. Be an active list Be transparent about the pas where the organization has fall current challenges. Honesty sig real change.

Keep your promises. If you say: do it. Track commitments caref when progress is slow.

When you hear tough feedbackremember why you started this listen responding, ask questions to underst on learning rather than defending.

developers’ experiences and open organization.

Most importantly, honor deve perspectives have been formed over 1 with developer systems, tools, and insights often point you to areas your

You should also create opportunities for feedback and engagement. Developers you meet with may think of something after your meeting that they want to share. Developers who aren't on your listening tour may want to share their own complaints, ideas for improvement, or volunteer to pitch in with improvement efforts. At this stage, make it lightweight, easy to implement, and easy to find. We've seen teams use a Google Form or a shared doc on an internal wiki.

During the interview, let them know you are there to listen and learn. Here's a general format for successful interviews: Kick things off with a very short introduction of yourself and the purpose of the meeting—let them know you are there to listen and learn.

Ask for some basic information about them: Years of experience, how long they’ve been with the company, which team they work on. In theory, you already know this, but it’s still useful to confirm.

Ask them 3-5 questions about their work. It’s helpful to give them a specific context (e.g., “Think about your day yesterday” or “Think about the last time you had to provision a new cloud instance”). From here, you can ask about their workflow, the things they love about their tooling and systems, and the things that make it difficult to do their work.

Wrap up. Thank them for their time and ask them if they have anything else they’d like to share. Let them know you'll write a summary of your findings after you've completed your interviews, and it will be shared with them and leadership.

A few tips when interviewing develo If a developer only has negative fee them! Remember, this is their tim advantage of the opportunity to biggest opportunities to improve.

During the interview: - Use open-ended questions th simple “Yes” or “No.” + Actively listen.

+ Ask for specific examples, not + Askclarifying questions.

- Don’t offer explanations or sc - Don’t ask leading questions Tool X because it’s slow?”) We have included an interview template in the Step 1 workbook. It h: for you.

You'll know you've done enough hearing the same problems repeated] usually happens at around 12-15 int fewer if clear patterns emerge earlier more if you're consistently getting nes

[&] Chapter 12 Synthesize What You Learn Turn your interviews into useful insights.

START IDENTIFYING LABELS while you're still in interview mode. As you conduct your research interviews, you'll naturally begin noticing similarities and patterns across conversations. It's a good idea to note these along with your interview notes. Take advantage of this momentum by noting common patterns in your interviews before completing all planned interviews. (This is similar to labeling or tagging).

On each interview template, identify notable themes such as “extended setup time,” “process confusion,” “missing documentation,” or “workflow interruptions.” Remember that technologies aren't the only sources of friction—don’t discount things you learn about process and culture, such as hesitancy to deploy on Fridays or reluctance to refactor legacy code. Pay particular attention to quality gates and reliability concerns that appear across teams, as these often have broad impacts.

Transfer these observations to a primary tracking document (included in the workbook) where you can compile themes across all interviews. As you build your consolidated theme list, patterns will become increasingly clear. You challenges affect groups of develope specific teams or technical environn highlights organizational pain point between different issues.

Build a flexible framework understanding. You can start with gradually be refined into more specif more in interviews. Or you can sta and group them into related themes analysis remains adaptable while p insights that accurately represent you Al tools can quickly identify pat interview data, and this is a perfect teams use effectively. However, mar data—even if you use AI to supp you something valuable: An intuiti actually saying. This hands-on engaj nuances, emotional undertones, and « immediately obvious in just categors have merit; choose based on your go you need to internalize the feedback.

Capture these themes and supp document. For each theme, write a serve as a definition) of the issue, quotes from your conversations. Not appears to be—does it affect the entir teams? Note any patterns you notice that occur together. Include your i

impact and difficulty to address, but avoid prioritizing or jumping two pages. Al tools can be helpful to solutions at this stage. This synthesis serves a few purposes: audiences.

it transforms scattered feedback into a structured understanding It’s also important to share yot of your DevEx landscape, creates the foundation for the priorities This also encourages participation youll identify in Step 2, and gives you an early outline and you've transparently shared your fin description of the feedback youll share. Youll find a sample acknowledges the key themes you he template in the Step 1 Workbook. steps without making specific comm Take a second pass through your notes. Don’t dismiss the appreciation for their candid feedba developer who had a completely different experience—outliers validate that you understood their fe often reveal unmet needs or problems others weren't comfortable that their input is driving the process.

sharing. Go back through your notes and separate what developers actually told you from conclusions you've drawn based on your own experience. Pay attention to responses that make you If you have existing data, use it.

uncomfortable or challenge what you thought you knew about Blatt © sithelz (ato site ovow your interviews—recent surveys, retrospectives often reveal persist can also be helpful, both to see di people (e.g., if one person is answ developer friction. Go beyond surface-level notes and look for the (© “why” behind behaviors or comments.

Prepare different summaries from your synthesis, each one targeted to your key audiences. (This is usually two, but you may have more.) For leadership, focus on the major themes with the may have great insights into sever.

greatest business impact. Include concrete examples that illustrate look for themes separately, or inclu the cost of each friction point—in time, quality, or developer uncovered during your interviews.

satisfaction. Propose initial areas to investigate further, but keep this summary concise and business-focused—ideally, no more than

[&] Chapter 13 Visualize Your Developers’ Workflow, Tools, and Friction Start by listing the steps your developers have to do to write and ship code.

AS YOU INTERVIEW developers, listen for the steps they take to do their work and create a comprehensive list of every step in their workflow. This includes setting up their environment, writing and debugging code, reviewing pull requests, running tests, and deploying. Also include organization-specific tasks such as security reviews and documentation.

Equally important, document all tools and technologies used at each step: IDEs, version control systems, CI/CD platforms, testing frameworks, monitoring solutions, and any custom or internal tools. Note where developers use Al, or where Al has been built into the software development workflow. Be specific about versions and configurations where relevant, as friction often occurs with particular tool combinations or setups.

List everything, even if it seems trivial—you never know where friction might be lurking. For example, a seemingly minor step like configuring environment variables or services might be a significant pain list these tools, friction points, and tc stage. We've included example work Workbook.

Don't forget specialized developer w While the core software developme developers, some roles have additio friction points. For example, ML eng Acquire, clean, and version d: Experiment with different m Train models on specialized Track experiment results and Deploy models to inference e: Monitor model drift and perf Similarly, mobile developers mig and app store submission processe: have pipeline orchestration and dat When mapping workflows, mak specific activities. The friction in waiting for GPU availability or man: just as impactful as traditional deve At the end of your interviews, you typical developer workflow.22 If you s speak with people on your team or fol

telemetry. These diagrams can also highlight areas where teams might collaborate to smooth out rough patches. We've included some example checklists in the Step 1 Workbook.

Finally, use these lists and diagrams to communicate with stakeholders. They're powerful tools for illustrating the complexities developers face and can help build support for your (© DevEx improvement initiatives.

SiriusXM'’s vision-first method: Mapping what should be, not what is.

When SiriusXM’s platform team wanted to improve their developer experience, they flipped the typical approach on its head. Instead of mapping their current workflows to identify pain points, they worked backward from the ideal experience.

They created a comprehensive user guide that mapped out what the perfect developer journey should look like—from onboarding through deployment to production operations.

The team conducted several working sessions with platform owners across different areas, then shopped the guide around with actual users to refine it. What emerged was their

[&] Chapter 14 Understand Your Stakeholders You might be surprised just how many stakeholders you have.

WHILE YOU'RE SPEAKING with developers about their workflow, it’s equally important to identify and understand all stakeholders in your DevEx improvement initiative. Creating a comprehensive stakeholder map early on will help you tailor communications and set appropriate expectations.

If you're unsure whether someone qualifies as a stakeholder, apply the “veto test” used by Silicon Valley Product Group: If a person has veto power over your project or can stop it from launching, they’re a stakeholder you need to engage.z2 Start by listing all potential stakeholder groups. These may include: + Engineering teams: Developers, tech leads, and engineering managers directly affected by improvements.

. Auxiliary functions: SREs, data scientists, and customer success engineers may not be product engineers, but your investigations and solutions wi + Leadership: CTOs, VPs of engi makers who approve resources.

+ Adjacent functions: Product 1 professionals who interface wit - Support functions: HR profess metrics, Finance team membe teams concerned with compliar + External groups: Customers benefit from improved develope For each stakeholder group, do contacts and champions, their interes communication channels.

For example, leaders typically w: business impact, developers need to affect their daily work, HR might initiative could improve retention mi on headcount requirements or cloud e We've included a stakeholder m: Workbook where you can documen familiarity with DevEx concepts, ar your initiative. This mapping will pro communications about your work ar more detail in Step 5.

Chapter 15 Share What You've Learned Once you've synthesized what you learned, be sure to share your findings.

TAKE A FEW days to refine your synthesis before sharing it.

Consider getting feedback from a trusted colleague to ensure your themes accurately reflect what you heard rather than what you expected to hear. This thoughtful analysis creates the bridge between listening and action, setting you up for the focused improvements we’ll explore in Step 2.

First share your findings with leadership: Send your executive summary to key leadership stakeholders first. This ensures leadership alignment and readiness for organizational questions.

Include the developer summary if sharing is common in your organization. Highlight that these are findings from your earliest discussions and you are still shaping your understanding of the organization and pressing issues. Be prepared to revise and refine your developer summary based on any feedback or discussions.

Next, reach out to developers. After leadership discussions and document updates, distribute the developer summary through appropriate channels. Sharing these findings transparently helps build trust with your development sense of co-ownership in the impr who see their feedback reflected and engage constructively in future initi: your message to developers by minim: emphasizing your appreciation for t and calling out that you're still worki organizational leaders to determine t whether it’s a direct email to all en; engineering managers.

Once your summaries are share dialogue. Developers may share addit or ask about next steps. Stay open to careful not to make premature com will likely evolve based on resources, existing initiatives. This initial commu more comprehensive communication Communicating early findings to bu When Minh Pham and Titus Stone developer experience insights at Ibo team, they quickly discovered tl findings can make or break stakehol metrics-heavy presentation fell fl right at me,” Minh recalls—but lea: adapting their ongoing communic build the credibility needed to sec thriving DevEx team.

Rather than overselling their impact, they learned to be transparent about their early stage while maintaining regular touchpoints. “We're constantly updating our elevator pitch, our board slides,” Minh explains. “We have to constantly remind leadership that there is still progress to be made.” This approach —combining honest expectations with monthly check-ins and evolving messaging—helped them maintain credibility while building support. Leadership appreciated both the realistic framing and the commitment to ongoing communication rather than one-time presentations.

Now that you've completed your listening tours and gathered initial insights from developers across your organization, you have a wealth of information about pain points and opportunities. But (© with so many potential areas for improvement, where should you begin? The answer is not to try solving everything at once. In the next chapter, we show you how to identify and execute on small, high-impact wins that build momentum and establish credibility for your DevEx improvement initiative.

© [&]

# STEP 2

Rather than swinging for the fenc you've uncovered, focus on targeted your approach and demonstrate val potential quick wins using our ri to criteria that measure team en opportunities. This approach not on but also strengthens the foundation fi This section will show you hov execute on high-impact quick wins momentum.

Reach: How many developers feel t Chapter 16 Pick the Right Projects When kicking off a DevEx improvement initiative, you need visible wins that validate your approach and transform skeptics into advocates.

DURING YOUR INTERVIEW synthesis, several candidate projects likely emerged as potential starting points. Your initial projects are important because early wins demonstrate competence and build stakeholder confidence while setting the foundation for your entire DevEx narrative. While some choices may seem obvious, it’s important to weigh your opportunities thoughtfully by considering different criteria.

Using Quick RICE for DevEx projects. The RICE framework —Reach, Impact, Confidence, Effort—gives you a simple way to evaluate opportunities without getting bogged down in analysis paralysis. RICE can help you tease out projects that have a higher likelihood of success, targeting those with high reach, high impact, and high confidence, while keeping effort low. For early project selection, think of this as “Quick RICE” or “gut-check RICE”"—you're making rapid assessments to identify promising candidates, not conducting detailed analysis. That deeper dive comes later when you have more data.

Focus on broad reach. Choose i many developers rather than so Consider frequency. Areas of fi frequently (e.g., daily or mul candidates for early projects.

Impact: Will developers immediat: Target visible impact. Pick in immediately feel, reducing th Example: Implementing auton standardized PR templates to re three days to one day.

Focus on problems developers developers already know about tempting to tackle underlying their managers want to see a: build credibility and naturally g Confidence: Can you deliver this st Look for clear milestones wh Select initiatives where you checkpoints that stakeholders demonstrate incremental succe identify when something isn’t v too much time.

Choose measurable projects. S and value can be measured | capture metrics. This approach of both delivering value and pr

team to focus on solving problems rather than measuring them.

Effort: How quickly can you show results?

Find low-hanging fruit. Look for annoying but fixable issues (some people call these “paper cuts”). Common examples include automating repetitive tasks, fixing flaky tests, improving a difficult Ul, or streamlining access to development environments. Depending on your context, some of these may require more work, so evaluate and look for things that can be addressed within weeks (or maybe a few months).

Target medium complexity. Choose projects complex enough to deliver meaningful value but not so complex that they risk getting stuck. These “goldilocks” initiatives— such as fixing flaky test suites, improving monitoring dashboards, or finishing data migrations—demonstrate competence while maintaining momentum. Avoid both trivial changes that feel like busywork and ambitious refactors that could take quarters to complete.

Consider timelines. Early projects should show results in three months, while later efforts should have visible milestones every six to nine months. For example, avoid choosing an initial project that requires a significant rearchitecture, as these typically take a significant amount of time and offer little visible progress until they are complete.

Putting Quick RICE to work. When evaluating your candidate projects from interview synthesis: 1.

Score each project on a simple scale (High/Medium/Low) for each RICE component.

2. Look for patterns—projects sco: with Medium or Low effort are « 3. Trust your instincts—if some scores, dig deeper.

4. Consider combinations—somse together create more impact th: The goal isn’t mathematical precis approach transforms gut feelings i exposing hidden assumptions and cre An example of Quick RICE in action.

Let’s say your interviews surface Flaky test automation, streamline monitoring dashboards. You car assessments across each of the RICE Reach Im Flaky test automation High H Streamlined code review High H process Monitoring dashboards Medium Me Quick RICE suggests starting wit broad impact, high confidence, qui effort. Save test automation for wi!

and can invest in longer timelines.

[&] Turn evaluation into clarity. Using Quick RICE transforms gut feelings into clear decisions by exposing hidden assumptions and creating fair comparison points. And the criteria make it easier to advocate for action without extensive data collection—the problems will be evident to others due to their visibility, broad impact, and achievable scope.

Applying this framework may also prompt you to dig deeper into aspects of a project; for example, if you aren’t clear on your ability to measure progress with existing or easy-to-get metrics. We recommend you team up on this exercise with someone who knows both your tech stack and your organization’s unwritten rules. Their perspective will find blind spots you might miss.

Your DevEx breakthrough might be a process, not a tool. Techies love new tools, but sometimes the best DevEx improvement comes from better processes rather than tools.

Process improvements are also great candidates for Al-enabled solutions. When optimizing processes, start with quick wins that reduce friction and build momentum, even if complete automation is the end goal. Small changes can significantly boost developer productivity and satisfaction. In your interview synthesis, these will show up as pain points around: «Complex or unclear approval processes.

«Documentation scattered across multiple locations.

+ Bespoke, custom tools used by isolated teams.

«Inconsistent standards and expectations.

+ Limited visibility into decisions and updates.

Focus on high-impact process improvements that directly address developer pain points. Consider streamlining approval workflows and removing redundant steps. Work with developers to establish clear code review stan needs. Launch regular knowledge-sh: or newsletters to improve visibility, documentation and resources. These ¢ technical investment while delivering The Step 2 Workbook has a Quick of the framework we’ll explore in Ste adapt them to your specific environm Starting with culture: MongoDB's postmortem strategy.

When Tara Hernandez joined Mo Productivity, she could have started improvements—faster builds, be deployments. Instead, after conduc made an unconventional choice: Sh Hernandez introduced post-mo: her Developer Productivity tear beyond its traditional home in SRE a post-mortems are standard practic she applied them more broadly acro The cultural shift within h Developers moved from fearing mis being part of a proactive learning also improved the wider engineerir of the DevProd team and inspire practices.

The organization-wide transforr CTO joined and championed operat:

MongoDB’s engineering organization. This leadership support amplified the cultural changes that had already begun taking root.

The lesson: Cultural change often starts small with individual teams demonstrating new practices, but leadership support is crucial for scaling those changes across the entire organization.

[&] Chapter 17 Share Early Wins to Gain Momentum Build momentum for your DevEx rollout by communicating—and celebrating—your early progress with stakeholders.

YOU CAN BUILD momentum for your DevEx rollout by communicating—and celebrating—your early progress with stakeholders. The activities in this chapter are fundamentally about change management—helping your organization adopt new ways of working. (We'll dive deeper into comprehensive change management strategies in the Second Practice.) Fail fast and share your learnings. You will hit roadblocks—a dependency might block progress, stakeholders might resist change, or your metrics might reveal no improvement. When this happens, be transparent. Share what didn’t work and pivot quickly. This builds trust and shows that failure is acceptable as long as the team learns quickly. For example, one team’s CI pipeline improvements showed no deployment speed gains because the real bottleneck was in code review processes. They pivoted to streamlining reviews instead and saw immediate results.

This is where metrics and mile: recognize these roadblocks early. R don’t need sophistication—simple be “deployment time reduced from 45 issues fast. Don’t spend months on f: lessons and try something new.

Celebrate wins along the way.

in infrastructure and platform work, is often “no news is good nev unnoticed while problems get all deserve recognition. Visibly celebrate individual contributions to reinforc Make these celebrations part of y rhythm: Share wins in team meet contributions.

Quantify improvements when times from 30 minutes to 5 n than “We made builds faster”).

Document successes in a visib newsletter).

Connect improvements to bus up.

Personally thank individuals fo: Use wins to build momentum ft Regular celebration helps create a valued and see tangible results from initiatives.

[&] Bring others along on the journey. Treat everyone involved in your initiative—whether they're driving strategy or engineering solutions—as partners in the work. Share credit generously and cultivate curiosity. Ask the “obvious” questions about processes and infrastructure choices—these often reveal crucial insights that others were afraid to surface. Make it clear that learning together is part of the process and encourage others to voice their own questions and observations.

Share your findings thoughtfully. Once you've identified your first opportunities for improvement, share your findings in ways that resonate with each audience—remember, different groups need different types of communication and levels of detail. Use your audience’s existing language and terms, introducing new concepts only when they serve a strategic purpose, like restarting a stalled initiative, eliminating confusion, or shifting established mindsets.

Frame potential solutions as starting points for discussion, actively inviting input and collaboration.

For developers, focus on concrete improvements such as time saved on daily tasks, streamlined workflows, and reduced friction points. When they see how changes directly benefit their work, they’re more likely to adopt and champion them.

Share your prioritization process—this transparency builds trust and encourages buy-in, even when immediate changes don’t affect everyone. Stay open to feedbac insights might help you refine your ar For engineering managers, highli increased productivity, better resour collaboration across teams. Help t changes enable their teams to del transparent about your process to bui For leadership, emphasize busine: accelerated delivery times, engineerin on investment. Connect DevEx imp goals and priorities.

Choose communication channe leadership to ensure alignment, then your organization’s preferred platform or internal blogs. Partner with HR or ¢ the right audiences effectively.

Keep the conversation going.

dialogue. Developers may share addit or ask about next steps. Stay open to careful not to make premature comn your action plan will likely evolve base priorities, and existing initiatives.

Team dynamics.

Chapter 18 Avoid Common Pitfalls Quick wins are essential for building momentum, but how you achieve them matters.

VAN BUREN AND Safferstone studied 5,400 leaders implementing new initiatives in companies. Their work reveals common pitfalls that can undermine long-term success.2¢ Here's how successful (© leaders navigate these challenges: Handling feedback.

- Don’t get defensive when questioned. It's natural to feel protective of work you've invested in, but defensiveness shuts down dialogue. Instead, explain your rationale and reasoning —this builds understanding rather than resistance. DevEx teams often assume their experience represents the broader engineering org—a common blind spot.

+ Do treat criticism as valuable input. Engineers are your customers, and their feedback shapes better solutions. Stay curious, seek early feedback, and remember that listening builds trust. (See tips on gathering feedback in listening tours in Chapter 12.) Don’t be overconfident when | may have tried similar approa challenges. Focus on identifyin; Do balance knowledge wi empowered teams explore sol identify, and continue to gather (See tips on gathering feedback 12) Decision making.

Don’t build solutions in iso intentions to show quick prog into the trap of working alone t opinions. This is especially tru your customers often have str solution.

Do embrace collaboration. Ct the broader engineering org quick fixes may seem more e ownership create better soluti the evaluation rubric in the wor Execution style.

Don't micromanage engineer across the organization to « initiatives—and products—are and prioritize problems, and e explore solutions.

Do invest in sharing context. When engineers understand the broader picture, they design better solutions and make informed decisions. This also builds trust in team judgment.

Create clear communication channels for updates and decisions. (See further discussion in Step 5.) The research shows that the most successful leaders don’t avoid quick wins—they embrace them. The key difference is their focus on building team capability and shared success rather than individual achievements.

While your quick wins are buildin you'll need to develop a more systen and addressing friction in your develo improvement initiative matures beyc becomes increasingly important for about where to focus your efforts ne explore how to collect and analyze dat of developer friction and helps you me

[&] ©

# STEP 3

Use Data to Optimize Your Own DevEx Work SUCCESSFUL DEVEX IMPROVEMENT initiatives reduce friction.

Your next step is to use data to pinpoint friction and decide which to work on next.

Your quick wins have demons improvements and built momenturr time to move beyond your early findi and rigorous approach. In this chapte analyze, and leverage data to systema prioritize improvements, and track yo Don't rush to solutions yet (w Friction lurks in a variety of areas, in processes, security measures, and c teams using Al in their developme collection is especially important—AI and potential friction points that car proper measurement. Your task is tot then prioritize them systematically.

of developer conversations will g valuable insights, and help you crea There are a few kinds of data to t Chapter 19 .

abit.

Establish Your Data Foundation Qualitative data Self-report Data Interview transcripts (from people) Open-ended survey responses Feedback comments If you're struggling to prioritize improvement efforts, you'll need more than interviews with developers. System Data Error messages Log entries . . . . . Documentation content ONCE YOU'VE TACKLED problems identified during your listening User flow (© tour and interviews, youll probably find yourself in a situation where there are several potential improvement efforts. It can be difficult to prioritize in this situation, and youll need more data. - Qualitative data is descriptiv Because developer feedback is so crucial, a great way to get interview transcripts and ope additional data is through surveys—they provide a systematic way Your listening tour from Step 1 to capture lots of information in ways that can be more easily dataset, which you'll continue t quantified. This helps measure progress, evaluate work, and ensure . Quantitative data is numerical, accountability. be calculated, for example a res; statistics from version control s DonjtEkipithellisteningitour; We will also talk about self-repor , . .

If you haven't done a listening tour yet—perhaps because you report and system data can be either ¢ joined an existing DevEx improvement effort or the major problems were already clear—do it now. Even a handful

+ Self-report data comes from people’s perceptions and experiences. It can be qualitative (like interviews or open-text responses) or quantitative (like 1-5 scale survey responses).

+ System data can be observed and measured externally. This is also called objective data. It’s typically quantitative (such as number of commits or turnaround time on a PR) but can also be qualitative (such as error messages).

Self-report and system data play complementary and essential roles in DevEx improvement initiatives. They each have strengths and limitations.

Surveys and system data are strategic partners, each with unique strengths. Surveys excel at identifying unknown friction points, providing satisfaction metrics, capturing handoff issues between tools, and measuring psychological factors. System data, on the other hand, excels at precise quantification of instrumented workflows, trending improvements over time, objectively measuring workflow steps, and providing detailed system performance metrics.

These strengths help make up for limitations of each type of data: System data can’t capture anything outside of existing telemetry, or emergent and complex concepts like AI usage and benefits. And system data can’t capt satisfaction or burnout. Survey da reliably or be collected continuously.

The most successful DevEx initia system data. Surveys are leveraged to may also ask for some basic factual dat system data is used to track precisely And you'll use both self-report and sys what initiatives are likely to be most i system data exist and are most import As your work scales—whether or across systems—you’ll need qu effectively and track progress. Storie for smaller groups and getting ini you analyze and rank issues with j basic surveys with scaled or ranked technologies and processes hurt pro system telemetry provides even r demonstrate both the cost of friction improvements over time.

Chapter 20 Identify and Use the Data You Already Have Most organizations have untapped metrics that can provide valuable insights into developer experience.

BEFORE INVESTING TIME and resources into new instrumentation, (© thoroughly inventory the data sources already available to you.

However, there’s a critical caveat: If no one has been treating these metrics as a data product with proper ownership and quality controls, the data is almost full of errors. So approach existing metrics with a dose of healthy skepticism.

When you're identifying existing data, you can use your developer journey mapping to point you to sources of data. For example: Development activity. Version control metrics, pull request patterns, code review times, Al assistant adoption and code generation.

Build and test performance. CI/CD pipeline metrics, test coverage, build times, failure rates—both for traditional and Al-assisted development.

Operations. Deployment freg monitoring and logging inform Process. Ticket resolution tin feature delivery cycles.

Feedback. Existing developer onboarding feedback.

For each development phase, s metrics are already being colle source, its quality, accessibility limi considerations. For example, incide useful if teams update them with st automated systems. And there may b in version control, but your company toit.

This inventory approach often reve data than expected, allowing you to instrumentation. We've included an data inventory in the Step 3 Workbool Find early insights from existi document your existing data sources, valuable insights: Development history analysis.

Analyze commit patterns: Look day patterns, and areas with hig Examine pull request metrics: cycles, and comment patterns.

Track feature lifecycles: Identify changes, and their contexts.

«Compare Al vs. non-Al development patterns: Review metrics + Review technical debt notes: Ic between developers using Al tools and those using traditional were taken and why.

approaches. Look for learning curves, productivity changes, . Examine architecture decision and new friction points. decisions and their outcomes.

Incident and failure analysis. Tool and platform usage.

«Connect code changes to incidents: Map specific commits or + Monitor CI/CD pipeline perfc deployment patterns to system failures. Look for correlations failure rates, and bottlenecks a with Al-assisted coding and Al-enabled toolchains. assisted workflows.

+ Study incident reports: Identify recurring issues, response + Review platform support ticke times, and root causes. developer pain points.

+ Review postmortem documentation: Extract lessons learned + Analyze tool adoption data and improvement recommendations, and note any recurring developers actually use vs. avail patterns.

This structured approach helps (© Project documentation mining. points and prioritize areas for deeper + Analyze archived project specs: Understand reasons for already have before initiating new dat project cancellations or pivots.

[&] Chapter 21 Use Surveys for Fast Insights Teams rarely have perfectly instrumented systems, especially when starting a DevEx improvement initiative.

BECAUSE THEY LACK this instrumentation, people feel like they are faced with a dilemma of having to wait years for system data.

A good estimate is about 6 person-months to instrument the first metric and 3 person-months for each metric after that. However, getting agreement on the definitions and deciding what to measure typically takes the longest.

You can get actionable insights now through surveys. Don’t fall into the either/or trap that many teams face—surveys and system metrics work best together, and youll need both for comprehensive DevEx insights. Starting with surveys lets you begin addressing developer friction immediately while you build toward more comprehensive measurement. (We'll cover how to combine qualitative and quantitative data—and handle conflicting signals— in Chapters 24 and 25.) Surveys offer a quick-start advantage because they deliver insight on organization-wide friction points in days, not months.

They capture the entire developer experience, not just what's easily measured, and come with almost n can just write and share a survey tt Forms or Microsoft Forms, no integra needed. They're also easy to adapt, c system data over time. Think of syste of the destination and surveys as the immediately and keeps you informed Creating effective surveys requires questions, ensure adequate response 1 results. Throughout this chapter and we provide step-by-step guidance or For more complex scenarios, consi researchers or consulting firms who s; A powerful DevEx survey does: shouldn't be. Make sure you are tar organization, or across the produc decided to start with (e.g., because o impact, etc.) Focus on collecting actic questions. For example: 1. “How toolchain?” (Measure on a 5-iter satisfied are yo 2. “Select the top three barriers to list from your mapped workflo another tool you may have miss 3. “How often does each work?” (Repeat the items sel hourly, daily, weekly, monthly, | 4. “Please share additional thoug] like the DevEx team to know a

[&] reminder: “Please don’t share any confidential or identifying information.” (Open text box.) You may also want to include questions about Al use, culture, psychological safety, or burnout. We've included an example short survey as well as additional questions in the Step 3 Workbook.

When survey results arrive, start by quantifying the friction.

Create a weighted impact score based on frequency and prevalence.

Then triangulate by comparing survey insights with available system data. Prioritize by focusing on high-impact, high-frequency issues first. Set baseline metrics for your initiatives, and share findings transparently with developers.

Using surveys is especially powerful because you get a quick signal of how developers see the system. Using the questions above, you learn about: «Developer satisfaction. Research has shown this is highly correlated to self-reported productivity and retention.

+ Productivity barriers. By forcing developers to select just a few things that block their work, you'll get a prioritized list of the top sources of friction, allowing you to better quantify top areas for improvement.

«+ Friction frequency. When you ask how often each selected item blocks their work, you can create a weighted score or weighted list of areas to consider, giving you clear direction for where to focus your efforts.

Getting fast DevEx insights at a startup.

Tom Hipwell, an engineering leader, needed to quickly understand his team’s developer experience when he joined the company, Series B startup Hofy (la just over 20 engineers and limitec practical two-step approach to get a Step 1: Skip-level conversatio ended interviews with every PM designer to identify key themes qualitative foundation gave him th the right questions.

Step 2: Rapid survey deploym weeks crafting the perfect surve questionnaire itself sampled from SPACE framework—a measureme: Chapter 24. He structured ques that emerged from his conversatic metadata to make analysis easier.

The payoff. Within weeks o qualitative insights and quantitative He used the survey results in a tear across the organization and collabo: Tom’s approach demonstrates can use surveys to quickly gather focus investigation on the areas tha starting with conversations to und surveys to validate and quantify tho entire team.

Measure value with the Sear user metrics and satisfaction scor

[&] occasionally you need a more direct assessment of how essential your solution—or an existing tool—has become to users.

The Sean Ellis Test offers a simple and powerful method that startup companies use to determine product-market fit, and it works equally well for internal developer tools.

The test centers on a single powerful question: “How would you feel if you could no longer use [your platform/ tool?” With just three possible responses: + Very disappointed.

«Somewhat disappointed.

«Not disappointed (it isn’t that useful).

Through extensive work with startups, Ellis found that products with strong market fit consistently have at least 40 percent of users answering they would be “very disappointed” if they could no longer use the tool. This threshold has become a reliable benchmark for product success.

For DevEx teams, running this test quarterly can provide valuable insights beyond traditional metrics. A score below 40 percent suggests your solution isn't yet indispensable, so you have opportunities to refine or improve.

However, be cautious when interpreting results for mandated tools where users have no alternatives. In these cases, consider adapting the question. For example: “If you had a choice of developer tools, how would you feel if you could no longer use [current tool]?” This framing helps distinguish between genuine tool value and organizational dependency. You can also pair the Ellis Test with satisfaction questions to better understand whether high disappointment scores reflect tool love or job necessity.

Open text is useful—but it also has s Open-text responses can provide selections developers have made. Fc where a developer shared “I have to code just to deploy”—giving us add deployment was such a challenge.

things you may have neglected to ir that were on your list but develope you only included core toolchain cc but a request process causes the big; Open text can also be a w information—telling you the what much—if you label it and look for your interviews. Because you may g responses, it can be useful to use t analysis to summarize labels and th However, open text has its limit against using only free-form te prioritization decisions. Not everyor a response, and research shows tt out text in surveys are at the poles or very upset. This means you mis middle.

It’s also nearly impossible to someone writes four paragraphs, more barriers to productivity tha short bulleted list? If someone sw that indicate a bigger problem tha

measured language? Even if you count the issues in each response, someone might include ten items because they're upset and had time to vent, not because they actually have more blockers than the person who thoughtfully listed three.

In our experience, prioritization based primarily on opentext fields rarely correlates with successful improvements— precisely because of these inherent limitations.

Chapter 22 Invest in System Metrics Over Time As your DevEx journey progresses, your data sources will naturally evolve.

WHEN STARTING OUT, you might rely heavily on surveys (around 80 percent) with some system data (around 20 percent), giving you quick, broad insights into developer pain points. As you progress in your initiative and you instrument more systems, this balance shifts along an S-curve pattern—system data gradually increases, then ramps up significantly as you build more automated collection capabilities. In mature DevEx programs, system data often comprises the majority of your information simply due to the volume you can collect automatically.

Surveys remain crucial throughout your journey and never disappear entirely. Even in mature programs, youll continue using survey data for instrumentation decisions, uncovering hidden friction points, and measuring developer satisfaction. The key is that while system data provides precision and continuous monitoring, survey data provides the context and human perspective that systems can’t capture Beware survey fatigue.

We all know this but it’s worth developers with surveys and they’ll you actually need. You need to be re can get, what you can’t get, and how Developers only have so much : priority. Your developers are solvin When you ask them to stop that wo making a withdrawal from a limite many withdrawals, and the account Here are some tips for survey suc The 15-minute maximum. | than 15 minutes to com Developers will either aban rush answers just to finish.

The timing sweet spot. For; seen dramatically better res month cadence. Why? Becau it takes to implement mea previous feedback, and it’s developer's work. Show prog input.

The importance of consolid already has a developer sur what you need, don’t launch positioning yourself against move) and introducing addit;

bad move). Instead, partner with the existing survey team and position your questions as complementary.

- The differentiation requirement. Multiple surveys can coexist, but they're most successful when they have clear, distinct positioning in developers’ minds. A culture survey and a technical workflow survey can both succeed if they're properly positioned and spaced several weeks or months apart.

Do a final check. Before you hit “send” on that survey, ask yourself: “If I were in my developers’ shoes, would I stop what I'm doing to answer these questions?” and “Would I care about the results of this survey? Would I want to share the results with someone else?” If the answers aren’t obvious yeses, you need to reposition your approach.

(© The teams that win at developer feedback aren't the ones with the most surveys—they're the ones who respect the context their developers operate in and position their feedback requests accordingly.

Survey data can be very useful when you don’t have good system data, but don’t fall into the trap of waiting for perfect system data before taking action. Perfect is the enemy of progress.

The transition to more system da identify data sources with reasonabl your organization. For instance, if friction, you'll want to analyze metric it takes to complete a PR) and PR dwel cycle time, focusing on how long a P These objective measures provide prec points.

When considering your data, bew can mislead your DevEx efforts. The you focus exclusively on areas wh system data. Don’t limit your attenti Even in mature DevEx improvement to provide crucial insights about experiences, and areas that are diffict maintaining some survey compones system data grows to dominate your c Equally important is avoiding the a single survey or data collection needs evolve as your organization ck and developers gain experience. Plan ongoing system data analysis to m picture of developer experience.

[&] Chapter 23 Make Sure You Capture the Right Data Your data should cover several dimensions of DevEx, not just things that are easy to count.

This measurement challenge becomes clearer when we recognize that software development actually involves three distinct processes, each with different goals and constraints: Development (creative, human-centered work), deployment (automated, machine-driven processes), and operation (optimizing for unexpected production scenarios).2¢é Trying to apply the same metrics across all three leads incentives.

A common mistake we see is te: because on the surface, it seems ea: Engineers are also more familiar with with survey data. However, we've di: capture the full picture. Additiona the form of counts, which misses v developer experience.

The most effective data strate problems to metrics. Start with the p: then identify what specific data wor track improvements in those areas.

For example, several developers w hard to write tests.” Through follow-u developers lack good systems for g tests, leading to oversized integratic tests. Now you know what to meast integration test coverage (wanting u patterns of mock creation in code (wa This approach ensures your r developer friction rather than just me instrument.

We suggest you also consider t experience your metrics represe (satisfaction, performance, activity, ct and flow) can help ensure you're captu than just what’s easy to measure.

For example, a data collection strategy that focuses on metrics that are already instrumented will often point a team to use data from their version control (such as lines of code, number of commits, number of PRs) and maybe their ticketing system (such as the number of customer-impacting incidents). But this can give you a very skewed view of what's really happening—teams can push to hit a deadline or release date, and youll see the number of commits and PRs go up. But at the same time, devs may be straining to get the work done because of manual work to set up their environments and deploy, and difficulty with the process to get changes approved.

Adding a few more data points—like survey questions to capture satisfaction or key barriers, or quality metrics like test suite results —can give you a more holistic picture of what’s happening and places to investigate. This balance becomes especially important when evaluating complex and Al-augmented workflows.

Don’t forget to collect data to build a strong business case.

Many DevEx improvement initiatives stumble because they focus too narrowly on technical metrics like build times and test effectiveness. While these measurements are essential, they often don't resonate with all stakeholders or clearly demonstrate business value.

In Part 1, we discussed the importance of making the business case, and in Step 1 we identified key stakeholders and their priorities. Now, revisit your stakeholder list and include metrics that will resonate with leadership by translating technical improvements into revenue drivers or cost savings: - Beyond measuring build tim consumed during builds to e savings.

- Instead of only counting workflow, quantify develope: productivity gains.

+ Connect deployment frequen responsiveness and customer - Collect the cost of product calculate the financial imp through better developer tool It’s important to collect these early in your initiative to establis initial measurement, you'll struggle and demonstrate the true imp: baseline comparisons create a c« narrative that connects DevEx impz success metrics that executives and understand and value. (We'll discus As you get more data, you'll ne analyzing and drawing conclusions few interviews or a few data points, i and manually look for patterns, But as important to be more thoughtful in I disciplined in how you analyze it. W data science team for detailed analysi share some best practices and rules of

cc = Get representative data to understand what's happening.

To build an accurate picture, collect data from across your organization. Your data collection strategy—whether for interviews, surveys, or system logs—directly impacts your conclusions.

Gathering descriptive information about participants (like experience level or team) enables cohort analysis, where you can compare patterns across different groups. For example, you might discover that senior developers face different challenges than junior ones, or that mobile teams have unique workflow bottlenecks compared to SaaS teams.

If you only gather feedback from developers working on legacy applications, you'll miss the distinct challenges faced by mobile or SaaS teams.

Before collecting any data, create a sampling matrix to guide your efforts. (Data science teams call this “sampling” and use sophisticated statistical methods, but you can start with a simple framework.) Map out key organizational dimensions like: + Product areas (legacy, mobile, SaaS).

«Developer role (junior, senior, architect).

«+ Platform types.

+ Team locations or time zones.

Consider mapping key organizational dimensions against stages in the developer workflow or the SPACE measurement dimensions.

Think of your sampling matrix like a bingo card—you don’t need to fill every space (“blackout”), but aim for balanced coverage across key areas while improving coverage and quality over time. We've included a more detailed example of data mapping matrices in the Step 3 Workbook under “Data mapping.” Get enough data to understand what's happening. Your goal is to get enough data to feel confid steps, without getting bogged down significance. Here are some good rules getting started.

For surveys, shoot for at lea better, but youll start getting Getting 100+ responses often g for practical purposes. Depen for example, how it’s structure are used, org-wide cultural dif enough responses (30-50) pe team.2” For interviews, start with 5you're not hearing many new t interviews for focused topics “reaching saturation.”) If every information, you're still learnin For system data, aim for com data from at least 80 percen population. Make sure your dz and well-documented (e.g., wh or “deployment”). Watch out as missing timestamps, inco: formatting. If you're measurin few weeks of data to account f patterns. Be especially careful data during a holiday period or represent typical patterns.

[&] The key is balanced representation across all your data types.

For subjective data, make sure you're hearing from different types of users/participants, not just the most engaged or frustrated ones.

For system data, ensure you're capturing different environments, configurations, and usage patterns. Document any gaps or biases you notice (like if you're mainly getting responses from one type of user, or missing data from certain systems)—this context helps you understand your findings better.

While “good enough” data is sufficient to start, you should continuously improve both coverage across the organization and quality (through better survey design, added instrumentation for precision). Most important: Effective data collection isn’t about hitting some magic number—it’s about gathering balanced input to understand what's happening across the entire organization and make informed decisions. For nonacademic work, be pragmatic while remaining thoughtful about who and what you're measuring and any blind spots in your data.

How does Al impact the data you need?

Al adoption represents both a new data collection opportunity and a potential change in how you interpret existing metrics.

What was once considered fast or efficient may need recalibration in an Al-augmented workflow.

When introducing Al tools into your development workflow, consider: Tracking comparative metrics (PR turnaround time with vs. without Al assistance).

Measuring quality impacts (acceptance/merge rates for Al-reviewed PRs).

+ Monitoring adoption patterr leverage Al tools most effectis - Assessing complexity diffe differently for simple vs. com Get enough data from enough happening. For surveys, a response r: good for most organizational context: fairly typical and usually gives you wo percent, that’s when you should start issues with your distribution approac be too long or overly complicated.

That said, response rate numbers response rate from a broad, cold em fine, especially in a very large organ would be concerning for a targeted st Similarly, a 25 percent response rate c balanced mix of your population, but your power users or misses all legacy ¢ For interview requests, expect 40if you're reaching out within your for interviews typically gets lower a percent. If you're getting much lowe consider shortening your planned flexible with scheduling, making tl offering an incentive, or ensuring caught in spam filters. Some devs rest on the organizational and team cultur

Building high response rates.

The key insight: Response rates aren’t just about the survey itself, but about the broader culture of feedback and action.

When developers see their input driving real changes, they're willing to invest more time in future surveys.

When analyzing developer feedb over raw numbers. A 30 percent re across different teams, roles, and expe about patterns across the organizatio rate that’s mostly from one group. 1 survey data and behavioral metrics.

For instance, if you see 80 p struggling with an API, that’s signifi different teams. But if they're all frc might be looking at a team-specific problem. Infrastructure engineers anc completely different friction points, data represents before making broad ¢

[&] Chapter 24 Turn Data Into Actionable Insights The gap between having data and knowing what to do with it is where many DevEx initiatives stall.

YOU'VE COLLECTED THE metrics, but now what? The goal isn’t to become a statistics expert, it’s to make informed decisions about improving the developer experience.

Even basic statistics can give you a good idea of the patterns of friction. You don’t need complex analyses to spot where developers are getting stuck or what tools they love using.

When you're diving into DevEx data, start with the basics.

Averages, medians, and frequency counts can reveal a lot. For instance, if your build times have a median of 8 minutes but an average of 15 minutes, that’s telling you some builds are taking much longer than others—definitely worth investigating. This can signal performance bottlenecks that need attention.

There are a few types of actionable insights you can get from these basic statistics: Performance bottlenecks emerge when your statistical measures don’t align. The gap betv the build time example points to inf?

problematic edge cases that are drag process. For example: «+ Test suite times with a median minutes - Investigate flaky tes « Code review approval times & median of 4 hours - Look for aj reviewer availability issues.

«Local development environmer average but 2 hours for 20 perc setup documentation or tooling Usage patterns show up in frequ time. A trend line of deployment frequ deploy less often on Mondays—spa workflows, meeting schedules, or eve patterns. For example: Internal tool usage plummeting - The new version might have features.

+ Slack mentions of “build failin Could indicate CI/CD resource c Friction points can become visib frequency counts. When you analy the most time or encounter the m bottlenecks. For example:

+ Survey data shows 70 percent of developers cite “waiting for code reviews” as their top frustration -» Examine reviewer workload distribution or approval workflows.

«API documentation accounts for 45 percent of all internal support requests ~ Invest in better docs, examples, or selfservice tooling.

+ You find that 60 percent of developers report spending more than 30 minutes daily on environment setup issues » Focus on containerization or automated environment provisioning.

Visualizations are your friend—they transform abstract numbers into patterns that people can quickly grasp. A histogram of build times might immediately show you have a “long tail” of problematic builds, while a trend line of deployment frequencies could reveal that teams deploy less often on Mondays or the end of (© the fiscal year. These visual patterns often spark the right questions: “Why do we see this dip here?” or “What changed when this metric improved?” Even better, visualizations make it easier to share insights with stakeholders who might get lost in raw numbers.

How LinkedIn made complex data simple.

LinkedIn’s Developer Insights Hub faced a classic challenge: How do you show comprehensive developer productivity metrics without overwhelming busy engineering leaders?

Their solution was progressive disclosure—starting simple and adding complexity only when needed. The main dashboard showed just essential information: Current metric values and recent changes. When managers wanted to investigate, a single click revealed historical trends and dimensional breakdowns.

This layered approach proved crt Instead of staring at “build times could drill down to discover. For specific to mobile developers in particular repository.

LinkedIn’s success came from p detail at the right time, turning ov clear path from problem identificati You can do much of the analysis best to partner with a data scientis scientist when: You're dealing with complex u: funnel analysis.

You want to predict future fric patterns.

You need to analyze unstructur responses at scale (though AI't this).

You're trying to establish co metrics (such as build times an You want to investigate tre differences.

Privacy and security are importa results and visualizations. The Kk developers while still getting meaning Rule of 5: Never show data for groups This prevents someone from figur:

developer is struggling with a particular API or deployment system.

Also, be extra careful with free-text comments in surveys—they can accidentally contain sensitive information.

# STEP 4

Decide Strategy and Priority YOU CAN'T SOLVE every DevEx problem at once, so you need a systematic way to decide and communicate your priorities. The data you've collected has revealed many developer experience. But with limi can’t address everything at once. Thi to evaluate your DevEx challenges us; decisions and create buy-in among ste Every item on your ever-growing but may not resonate with someone dive in and stack rank the list so you we caution against this. That ranking head, making it prone to errors and bi others—both for feedback and buy-in.

[&] Chapter 25 Focus Your DevEx Efforts Use RICE criteria to clarify decisions and create buy-in—now with real data.

AT SOME LEVEL, every challenge facing your developers is related to —or tightly integrated with—another challenge. For example, when someone says their build times are too slow, is it because the builds need to be rewritten to take advantage of build acceleration techniques such as parallelization or caching, or because the underlying architecture needs to be redesigned? If your test suite is too slow, is it because the tests need to be updated with performance in mind—because, for example, the test suite needs to Jrun only necessary tests—or because a large number of flaky tests leads to a test harness that resubmits failed tests several times, contributing to along test execution time (and much larger compute costs)?

It’s true that systems are interrelated, but it can be helpful to first think about the challenges independently, and then consider how those challenges relate to the system. This will help you evaluate challenges so you can prioritize work. Because you've collected data and done a listening tour, you should have a good feel for the top challenges facing your developers right now—whether it’s your first time doing this process or you're rev challenges.

But identifying these challenges is clarity around which challenges shoul resourcing. The RICE framework you now becomes your systemic evaluati your listening tour and metrics.

An important part of prioritizi understood this challenge well: “Peo; yes to the thing you've got to focus or at all. It means saying no to the hundr are. You have to pick carefully. I'm actt haven't done as the things I have dor 1,000 things.” This principle applies just as strong internal users. RICE helps you say no to evaluate the full picture—not just most interesting technical challenges.

Once the decision is made, you c: or all of the criteria used to make t] organization. We've found that sha behind the priorities can help win ov different. For example, they may be been given a lower priority, but then understand that the final product wil!

completed first.

Meet CloudTech: Your RICE framewo

To illustrate how this framework works in practice, we'll follow CloudTech, a mid-sized SaaS company whose DevEx team identified five top challenges: Manual deployments (halfday process requiring multiple people), slow build times (45+ minutes), flaky tests (30 percent failure rate), poor onboarding docs (2+ weeks to first commit), and inconsistent local environments. They are working with executive support, so they can choose from both large-scale and local efforts. In the chapters that follow, you'll see how they used the RICE framework to make tough prioritization decisions.

What's the frequency of impact? ( quarterly pain.) Does this affect high-leverage deve Use consistent units across all cal Chapter 26 mix “daily impacts” for some items affected” for others. This ensures a faj Use Relevant Criteria to Set Priority types of improvements.

f D | E . Impact assesses how significant or bevelo p er Xp erence developers’ daily experience. Questior Will developers immediately fe How significantly will this char When everything is a priority then nothing is a priority. + Does this remove a major con friction?

IN STEP 2, we introduced Quick RICE for rapid assessment of early opportunities. Now that you have more data and stakeholder When scoring impact, use a simple (© input, it’s time for a more comprehensive RICE analysis. Unlike the + 1 =Low impact: Minor improve quick version for identifying promising candidates, this systematic + 2 = Moderate impact: Noticeabls approach uses metrics to evaluate each component. + 3 = High impact: Major bottlen RICE can help you tease out projects that have a higher likelihood time savings.

of success, targeting those with high reach, high impact, and high confidence, while keeping effort low. Confidence reflects how certain y succeed as planned, and is typically e: 80% confident). Consider: Technical feasibility and knowr RICE Formula: (Reach x Impact x Confidence) + Effort = RICE score. . .

Team expertise and capacity.

Dependencies and potential blo Reach measures how many developers are affected and how . Past experience with similar ini often. This is your foundation for understanding true impact scale.

Possible questions to ask: Effort measures the total investme How many developers does this affect? months. Be sure to include:

«Development time.

+ Testing and deployment. Reach Impact . Documentation and training. (daily impacts] | [1-3scale] + Ongoing maintenance considerations.

Flaky 150 developers | Moderate, tests > *3testruns reduces CloudTech's RICE scoring for their top challenges. Flaky test | per day = 450 delays but resolution | daily impacts workRemember, CloudTech’s top challenges were manual SFiS deployments, slow build times, flaky tests, poor onboarding exist=2 docs, and inconsistent local environments. moat Confidence | great | pice Reach Impact (% confi(daily impacts) (Fscale) | denceot | PESO Sede: Pooron- | 24newhires | High, resuccess) months) =R*I"C/E boarding | peryear*5b duces time docs — estimated use | to first Manual | 150 developers | High, Clear 3 (1500*3 Onboard- | of docs/day * | commit deploy- | *2deploy- eliminates | technical | person- | *.85)/3 ingdocs | 3months (60 | by several ments | ments per half-day path months | =1275 overhaul | days) focused | weeks= Deploy- week /5days | bottleneck | proven onboarding 3impact ment inaworkweek | =3impact | tools period = score automa- | =300 daily score available 7.200 yearly tion impacts = 85% interactions confi- / 260 workdence ing days = 28 score daily impacts (rounded) Slow build | 160 developers | High, Requires | 8 (750 times — *5 builds per eliminates | archi- person- | 3*.65) Build time | day =750daily | 45+ minute | tectural months | /8=183 optimiza- | impacts wait times | changes, (rounded) tion =3impact | someunscore knowns = 65% confidence score I

© [&] Confidence | perry | Rice Reach Impact (% confi- Ea Sy (daily impacts) (1-3 scale) dence of i] ZRHC/E success) Inconsis- | 150 developers | Moderate, Contain- [2 [60% 2* tent local | affected, typ- | improves erization | person- | 8)/2= environ- ically once per | produc- approach | months | 120 ments day =150 daily tivity = is well— Local impacts 2impact underenviron- score stood ment and some standard- solutions ization exist = 80% confidence score Based on these RICE scores, CloudTech would prioritize manual deployments (1,275), then build times (183), local environments (120), flaky tests (75), and onboarding docs (53).

While RICE provides a solid foundation, it is typically used in product development, where resourcing and stakeholder buyin are assumed. DevEx initiatives benefit from asking additional questions.

A great way to address these limitations is to conduct a modified version of the “5 Whys.” But instead of asking, “Why?” ask, “What challenge should we tackle next?” And each time, focus on things that are important for resourcing, execution, or business needs. We also suggest you make notes about why you assess each challenge the way you did—this will come in handy when you discuss it with stakeholders and teams.

Look for business impact and s asking, “Is it easy for me to talk abo metrics that business leaders care abou High-impact problems naturally —50 developers losing 30 minut calculations. When presenting to les that demonstrate clear business understand: Developer hours saved, cc to-market improvements.

Equally important is considering, with or leverage existing work to maxin Initiatives that connect with ongoi often deliver greater impact through and established priorities.

For example, if the organization re observability infrastructure, DevEx this investment to solve visibility faster results at lower cost. Similar is reducing compliance-related fricti security initiatives can deliver dual t effort. Highlighting these to leaderst initiatives are integrated into the broa Think about collective vs. local ask is, “What challenge requires orgar fixes?” High-reach problems often require span multiple teams. These require a t and coordination across teams. Under

[&] organizational muscle versus team-specific approaches helps you match your approach to your scope of control.

Collective action candidates: + Architectural and process changes that benefit from coordinated investment.

«System-wide upgrades and security patching that get sidelined during team-level roadmap planning.

+ Local DevEx work that has outgrown its original scope and needs centralized support. For example, when an internal product team builds an exceptional CI/CD pipeline that others want to adopt, demand quickly exceeds capacity. It often doesn’t make sense for a product team to support the whole organization.

Local action candidates: + Improvements to automated testing practices.

+ Continuous integration workflows.

+ Trunk-based development.

The key is distinguishing which challenges require organizational muscle versus which benefit more from teamspecific approaches tailored to local workflows and needs.

Understanding what projects need local or collective action helps you match your approach to your scope of control, which we explore further in Step 6.

CloudTech'’s collective vs. local assessment.

Manual deployments: Collective—Needs central CI/CD platform investment.

- Build times: Collective and changes (collective) and team - Flaky tests: Collective and I each team can improve som team owns the solution.

-  Onboarding docs: Local—Inc their documentation.

- Local environments: Loca their own setups.

Consider timelines, urgency, and questions here include: “What challenge is best to tack to complete?” “Do we have the right skills i external expertise?” “Can we address this challenge v capabilities?” “Which challenges will get v problems will that create?” “How does this initiative align v business rhythm?” Seeing progress in three to si: maintaining momentum and demon: that can be implemented by realloca than requiring new headcount often f particularly when you're first starting

© [&] Timing also matters—launching a developer tooling overhaul during peak release season will likely fail, while the same initiative might thrive during a planned engineering investment period.

CloudTech’s timeline assessment.

Manual deployments: Medium (Medium speed)—3-4 months for basic automation.

Build times: Low (Slow)—Architectural changes needed, 6+ months.

Flaky tests: Low (Slow)—Requires deep investigation, 6+ months.

Onboarding docs: High (Fast)—Can improve significantly in 4-6 weeks (or faster with Al tools).

Local environments: High (Fast)—Docker standardization doable in 6-8 weeks.

Use constraints and risks. Great questions to ask here include: “What challenge should we tackle first because it represents a critical bottleneck in our development flow?” - “Do we have control over the key dependencies needed for success?” + “Can we implement this change with minimal disruption to existing workflows?” Constraints are the chokepoints limit system performance regardless of improvements elsewhere. For example, if every release requires a time-consuming manual security review, or if limited GPU capacity is restricting your team’s ability to develop and test Al solutions, addressing these constr multiple workflows.

Similarly, if AI code-generatio bottlenecks—like longer code review code quality concerns, or dependenc become performance chokepoints— may warrant prioritization.

When evaluating constraints, frequency and impact. A process | daily often creates more cumulatiy but quarterly bottleneck, even if complaints. Eliminating high-freque productivity more effectively than in enhancements that don't address valuable DevEx improvements of constraints rather than adding new ce CloudTech’s constraint assessment.

- Manual deployments: High deployment queue, limiting r - Build times: High—Develop 90-minute builds, slowing all - Flaky tests: Medium—Team: but releases still get delayed.

- Local environments: productivity but doesn’t bloc up.

- Onboarding docs: Low—On internal transfers, not ongoin

Don’t forget team and organizational factors. Ask yourself, “Which challenge allows us to strengthen our people and organization while solving technical problems?” Look for projects where team members can make meaningful contributions that showcase their expertise while creating opportunities for growth and recognition. The most successful initiatives align with teams’ professional development interests and incentives.

CloudTech’s team goals assessment.

CloudTech asked: “What aligns with our teams’ growth and incentives?” Manual deployments: High—Interesting DevOps work that requires specialized knowledge the team is excited about learning.

- Build times: Low—Requires deep architecture knowledge only a few team members have.

Flaky tests: High—Senior engineers excited to showcase debugging skills and testing expertise.

Onboarding docs: High—Gives newer team members meaningful contributions and ownership.

Local environments: Medium—Good learning opportunity but routine containerization work.

Don’t forget other considerations. The examples above aren’t comprehensive-you’ll want to include criteria specific to your organization. For example: - Remote workforce: “What challenge is best to tackle first because it disproportionately affects remote work?” «  Aladoption: “What frictionis A to address?” or “What challenge .  Compliance-heavy industries: most regulatory friction?” Your prioritization exercise can do d The same evaluation criteria tooling and automation can—and instrumentation and feedback loc identify high-priority developer fr evaluation framework, you've als measurement.

This creates a powerful two-way - Found a high-priority frict data? This is ared flag. You sh and start instrumenting the most-used CI pipeline has n that gap while you improve tl a targeted survey question to.

building instrumentation.

- Survey responses don’t 1 the system? In our exper productivity researchers h: discrepancies exist, self-repo points them to hidden pair adding targeted questions survey for more informatior deployments take forever bu you need better tools and bett

Limited resources? Your highest-friction areas deserve both better tools and better metrics. If you build tools for problems you can’t measure, it’s very difficult to show improvement, impact, and business value.

Try this: For your top three DevEx pain points, ask: “Can we measure improvements in this area?” If not, plan your measurement strategy at the same time as your tool improvements.

This approach creates a healthy cycle: Better measurements help you build better tools, and better tools let you collect more useful data. This systematic approach builds on the data you gathered in Step 3 and prepares you for stakeholder communications we cover in Step 5.

should do with a colleague—you st challenges emerge. If everything is F evaluate—you can’t operate in a we highest priority. If everything is Low, : Chapter 27 different viewpoints.

You can find a detailed rubric in th See the Bigger Picture: Use a Quick Rubric CloudTech’s completed analysis.

Let’s see how CloudTech’s RICE ana translates into their strategic rubri d DevEx criteri tli Avoid getting lost in the weeds by looking at the big picture. scores and Devix Criteria we outline NOW THAT YOU have your top DevEx challenges (from collecting Challenge RICE | Business | Collective data), your RICE scores (by quantifying reach, impact, confidence, score Value Action (© and effort), and your additional assessments (from asking “What Manual 1275 High Collecchallenge is best to tackle first?”), you're ready to look at the big deploy- (highest) tive picture. ments Create your rubric. Start with the criteria that matter most for Build 183 High Collecyour organization. Based on our analysis in Chapter 27, common times ve and DevEx prioritization criteria include: + RICE analysis Flaky 75 Medium | Collec. Can be mapped to business value. tests ve and «Requires collective action.

+ Aligns with timelines and rhythm of business. Onboard- | 53 (low- | Medium | Local . Isaconstraint. ingdocs | est) + Aligns with team goals. Local envi- | 120 Low Local + [Your context-specific questions here.] ronments — Once you've created and filled out your rubric—an exercise you

CloudTech’s decision: Start with manual deployments (high across most criteria, in particular business value and the highest RICE score) and onboarding docs (quick win while building deployment automation). Build times scored high on business value and RICE but low on timeline—they’ll tackle this after proving success with the first two initiatives.

Key insights from combining RICE with the DevEx criteria: RICE confirmed their intuition. Manual deployments had both the highest RICE score (1,275) and scored high across strategic criteria.

Timeline considerations shifted priorities. Even though build times had the second-highest RICE score (183), the rubric revealed timeline constraints that made (© it less suitable as an early initiative.

+ Quick wins became clearer. Onboarding docs, despite having the lowest RICE score (53), emerged as a valuable parallel track due to high timeline scoring and team alignment.

Make the most of your analysi scoring and strategic rubrics gives yot Use RICE scores for qua calculations, and detailed resou Use the rubric for strategic alignment, and big-picture deci When they conflict, consider w adjustment or whether strateg: team capacity) should override Remember that the goal isn’t r making informed decisions that bala organizational realities.

Having a clear strategy and wellbut it’s only half the battle. Even the DevEx roadmap will falter without stakeholder support. In the next che sell your DevEx strategy within you message to different audiences and bu drive lasting change.

# STEP 5

Sell Your Strategy A PERFECT DEVEX improvement plan won't matter if no one knows what to do—or why they should care. Now that you've established your improvement plan strategy and priorities, it’s time to focus on how you communicate these decisions to gain support and drive action across your organization.

Effective communications (whic] explain what sources of friction dev these pain points matters, what valt removing that friction, and what sp The best DevEx communications go fu capability through interactive worksh hands-on experiences that create lasti Many DevEx teams underestimat communications. While leading c Spotify invest in dedicated marketing for their DevEx initiatives—includ stakeholder enablement—smaller org results by having technical writers o this critical area.

[&] Chapter 28 Leverage Your Stakeholder Analysis for Effective Communication The relationships you've built and insights you've gathered during your listening tour will help you craft messages that resonate with each group.

REMEMBER THE STAKEHOLDER matrix you completed in Step 1?

Now is the time to pull it out again. That early identification work provides the foundation for your communication strategy.

Remember your stakeholders are more than just developers.

Many people assume that the audience for a DevEx comms plan is developers, but that assumption is often wrong. Developers benefit from these initiatives, but they aren’t the primary audience for your communication plans—at least not initially. DevEx improvement initiatives often require organization-wide support and resourcing, making your primary audience organizational leaders whose support you need and want.

Your Step 1 stakeholder analysis should have identified each group's interest level, familiarity with DevEx concepts, and general supportiveness (if it didn’t, please gob Use this information to shape and pr: and determine which stakeholders ne Tailor your approach based on Different stakeholders approaches, so you'll need to tailor you require A common mistake is sending ide —resulting in content that’s either t lacks sufficient detail for practitione content to all stakeholders, you ris} simultaneously overwhelming and i be left with unanswered implements may struggle to extract strategic value Instead, leverage the insights f create targeted communications. Fo implementation specifics and workf emphasize business outcomes and adjacent departments such as HR © relevant to their domains and expla them. This targeted approach ensur information that addresses their spe appropriate action.

Refine your stakeholder list w details. Review and expand your S include communication preferences: each group? What metrics matter m resonates with their priorities? This your comms so they resonate with all to executives.

The business case elements we explored in Part III provide the foundation for this positioning. We provide example tables in the Step 1 Workbook.

We often find it helpful to list key stakeholders and information in a table or a spreadsheet. This is handy for organization as well as identifying any information you may be missing for certain stakeholder groups. Your stakeholders—and the information you decide to collect—will differ. Here, you'll identify major stakeholders, their motivation (why they care), what support level they need (skeptical, neutral, enthusiastic), your engagement strategy (inform, convince, collaborate), their information needs, their engagement strategy, and their preferred communication channels. Here's a simple example: You will typically have three or four stakeholder groups, roughly grouped into leadership, engineering managers, and developers.

Depending on the size of your organization and how teams work together, you may also have an additional “Keep Informed” group with teams like Customer Support, Marketing, and Billing. These teams may have a strong reliance on the developer tools and want to be kept informed of what is happening and how it will impact their work.

To simplify and target messaging, avoid having too many groups.

With this table, you always have the information available to send targeted messages when necessary. See the Step 5 Workbook for materials you can use.

Identifying stakeholders also helps you identify specific groups you may want to work with early on in your DevEx improvement initiative. For example, if high-friction provisioning is a challenge you are tackling, there may be a team in one part of the org who has been experimenting with ways to them great partners from both a tech Meanwhile, teams working on legacy problem at all, and may only care abc the initiative impacts their own toolir Engagement Group Motivation strategy Support level eadership Skeptical Convince Engineering Neutral Collaborate managers 0 | Skeptical Inform, Collaborate Developers Your stakeholders need to know they should care. Don’t assume ever; faced by your organization as clearl the table with diverse backgrounds, s good, bad, or even possible in your sys also have preconceived solutions—fc assume that adopting AI tools will ¢ productivity challenges, without und Al or the specific friction points that n Take the time to clearly lay out the why they matter to each stakeholder

at first, especially with groups you don’t often work with. Make sure you understand why improving DevEx is important to each Audience Education stakeholder—this helps you explain it well, empathize, and learn . : . Developers “Our analysis “Thi more. If you can’t find that connection for someone, consider taking P , 4 found 40% of will them off your list or shifting the work that will likely affect them to build failures stem | time future cycles. from configura- and tion issues” nee Co wor Use the EMI framework for stakeholder communications.

When crafting DevEx communications, apply the EMI framework to ensure messages resonate with each stakeholder group: Engineering Tears are Al Leaders spending 15 hours | issu E = Educate: Address knowledge gaps specific to their role and weekly onavoid- | incr perspective. able technical deli 5 . . Cs debt” hy 2 M = Motivate: Connect DevEx improvements to their priorities } and pain points. HR Leaders “Engineers spend | “Im I = Inform: Provide actionable details relevant to their 20% of time syst 5 I waiting on builds duct Lyolyerent and fighting infra- | 16% Note that these components should be tailored based on each structure” inte stakeholder’s support level and information needs. Enthusiastic supporters need reinforcement and opportunities to champion the work, while skeptics require additional evidence and risk mitigation. Neutral stakeholders typically respond to clear value Finance Current ineffi- Thi . i cient systems has propositions and success stories. require extra 9m For example: infrastructure thre costing $450K clou annually” Applying EMI ensures you're not about what's happening, but educatin motivating them with benefits align This is particularly important to re:

about launches—resist the urge to send celebratory “We shipped it!” messages to everyone. Those celebrations belong with your team and immediate management chain, while other stakeholders need EMI-structured communications that focus on impact rather than achievement.

Think of your DevEx initiative like a product— and “sell” it to your stakeholders.

When communicating about your DevEx improvement initiative, adopt a product mindset to make your message more compelling. This approach helps you: Focus on solving specific problems rather than just implementing technology.

Clearly articulate value in terms stakeholders understand.

- Create a coherent narrative about your initiative’s purpose and benefits.

For “investors” (leaders who fund your work), you'll need to be able to briefly outline the business case, competitive landscape, and expected returns. For “customers” (developers and engineering managers), you'll need to emphasize how your solution addresses their specific pain points.

This product-based framing transforms abstract concepts like “improving developer experience” into concrete solutions that stakeholders can easily understand and support. For a more detailed approach to treating your DevEx tooling and automation ecosystem as a product, see the Third Practice: Make Technology Sustainable and Effective.

Chapter 29 Effective Messaging Takes Customization and Repetition Shape your message for each group—it boosts support and gets people on board.

WHEN YOU SHARE developers’ challenges and their relevance to (© your audience, you're not just informing them—you're inviting them to be key players in the solution. While some core messages will be consistent across stakeholder groups, tailor your approach by considering these questions: Does the tone of our message suit this specific group?

Is our level of technical detail appropriate, or should we simplify our language?

Do we need to provide concrete examples to illustrate the problems and potential improvements?

How will this impact their work directly?

What exactly are we asking from them—support, information, advocacy, or resources?

We suggest drafting a message for each group, then sharing with — key members to review and optimize tone, content, and distribution channels (e.g., email vs. internal posts Tell people what's going on—a We've all had emails or Slack messag or ignored—our inboxes are so full Your DevEx communications face th share important messages multiple tir developers.

For leadership communications, & concise deck shared during a meeting these materials will likely be forwarde on its own and is easily digestible at a When communicating with e developers, try sending an initial mx then enlist leaders to send reinforc This two-step approach not only er your message but also signals mana initiative. We consistently see notice and survey completion rates followin —proving that in DevEx communic isn’t redundant, it’s effective.

Give your DevEx initiative an ide DevEx initiative with a memorable an that energizes people. A simple, ca common reference point and can gen work. Alongside this branding, creat related to your DevEX initiatives an indicate success. This provides clarit they fit in the bigger picture.

You'll want more materials to help others confidently spread the word without always needing you. Additional materials such as workshops and detailed reference materials may be especially useful for leaders and other stakeholders, while developer groups may find technical runbooks and FAQ sessions useful.

Build capability, not just awareness. Effective DevEx communication goes beyond informing people—it builds their capability to understand, engage with, and champion your initiatives. Design your materials to move stakeholders through a three-stage progression: Understand. They grasp the big picture, value, why DevEx matters, and core terminology.

Try. They use what they've learned to engage with the ideas and actively look for ways to support and enable your work.

Activate. They mentor others, build capabilities in their teams, and provide recommendations for sustaining and improving DevEx initiatives.

This framework helps you create communications that generate lasting change rather than temporary awareness.

In one example, we supported HR partners with a detailed reference book and workshops. A whitepaper linked technical concepts (such as developer friction and platform engineering) to their domain—explaining how DevEx initiatives impact hiring, training, and retention. Since these technical details were probably new to some in HR, we offered interactive workshops where they could practice scenarios related to supporting engineering teams during DevEx changes. This hands-on approach helped HR partners confidently navigate the technical landscape of DevEx work.

How Snowflake rebuilt developer tri When Snowflake’s Engineering Syst mistrust—engineers believed “no they knew communication woul perceptions. Their solution: A co approach that emphasized both developers where they were.

Their strategy included weekly biweekly newsletters, quarterly s individual team all-hands meeting which had 40-50 percent participat they coordinated pushes from mul and Slack from the DevEx team, t engineering, and the CTO.

The key insight: The best way to a new solution is to meet them wh consistent messaging across multi; specific approaches—like weekly si —they successfully transformed or; built lasting trust through sustaine Prepare for challenging question: we've found useful in preparing our is a document listing a handful of q —typically ones that are defensive or “Aren't developers already doing thi these metrics, that’s not how *I* define

This technique, borrowed from product management, helps teams anticipate objections and develop thoughtful responses before they’re needed. Creating this document helps your team align on responses to difficult questions and prevents being caught off guard in important presentations or meetings. It also helps you improve your comms by anticipating questions and concerns.

When building your Rude FAQ, include your team’s candid responses but refine them into constructive, evidence-based answers that acknowledge the concern while redirecting to your initiative’s value. It’s meant only for the DevEx team as a way to prepare for questions you may get d and in some cases, it’s helpful to identi may have.

With your DevEx strategy « stakeholder support in place, you're changes. However, the approach yo your scope of influence within the o we explore how to drive DevEx impre you're working at the team level or ac

# STEP 6

Drive Change at (Your) Scale YOUR STRATEGY IS set, your priorities are clear, and you've communicated effectively with stakeholders. Now comes the crucial work of actually implementing chang how to match your approach to yo on where you can make an impact organizational inertia.

One of the most crucial factors to b to improve developer experience will approach to your scope of control. W] with organizational authority or an your team’s daily work, understandir you choose the right problems to tack to drive change.

can implement without requiring bre significant resources.

The principles of effective Dev regardless of scope. These princip!

Chapter 30 problems, balancing technical and cul impact. What changes is how you a; Ada pt Your App roac h to strategies you use to drive adoption a: explore how to execute DevEx impr Your S cope local levels. You'll learn how to: Choose projects that match you Build support and drive adopti By targeting areas within your scope of control, you can make impact levels.

faster. Don't waste time fighting organizational inertia, focus on where + Avoid common failure modes sy you can actually drive change. + Navigate the interplay betwe process changes, and cultural sl (© SCOPE OF CONTROL in DevEx work refers to the breadth of your «Leverage success to potentially ability to directly influence and implement improvements. At the global level, you might have formal authority, dedicated resources, Understanding these differences and a mandate to drive organization-wide changes—like rebuilding identifying problems to actually sc the CI platform or establishing new collaboration practices across working across an entire organizatio multiple teams. At the local level, you might be working within your team.

own team or a small group of teams, focusing on improvements you

Chapter 31 Drive Change With Global Scope of Control Global scope of control means you have organizational support and mandate, but success still depends on driving broad action.

THIS CHAPTERS for leaders like heads of DevEx or senior technical leaders who have both the official remit and resources to drive organization-wide improvements. You might have the job title and the leadership support, but you'll still need to work across different teams to create real impact. The data collection approaches you adopt from Step 3 will be particularly important at this scale to track progress.

The biggest challenges in global scope aren’t technical—they’re about choosing the right problems and driving sustainable change.

Even with organizational backing, success requires more than just building better tools. Take rewriting an internal CI system—you can create the most sophisticated platform imaginable, but if teams don’t adopt it or use it effectively, you haven't actually improved developer experience.

There are two critical ways that global DevEx initiatives typically fail. The first way is solvi perfect technical execution. This hapg Build solutions without valid: (which we covered previously— Assume they already know wha Try to solve everything at incremental value.

The second way is solving the righ failing at change management. This h Assume “If we build it, they will Underinvest in adoption strateg Focus purely on technical im; process changes.

Don't think about how to drive: Effective technical improvemen and cultural adoption to create how successful global DevEx imprc elements—technology, process, and rolling out an improved CI system. T might be flawless—faster builds, bett infrastructure—but that’s only the be; The technical foundation mu: developers. Unlike local improvemer team’s needs, global technical chan different scenarios. Your solution ne flexible enough to handle varied use For example, a new CI system th applications but can’t handle mobile

© [&] requirements won't achieve broad adoption. Here are some additional examples: + Modernized build infrastructure.

+ Improved test execution and reliability.

+ Better caching and parallelization.

+ Clear metrics and monitoring.

Two approaches to global solutions.

When building organization-wide tools, you can either create flexible primitives that handle every edge case, or build opinionated platforms that solve most common scenarios with less complexity. The best systems often combine both: Simple defaults for the 80 percent case, with underlying flexibility for teams with special requirements.

Process changes ensure solutions can be used. This is where many global initiatives stumble—they build great technical solutions but underinvest in making them accessible and adoptable.

Consider the example of a team that builds a new deployment platform to solve slow, unreliable releases. The platform works beautifully in demos, but teams struggle to configure it for their specific use cases, migration documentation is incomplete, and there’s no clear support process. The technical solution exists, but the original problem persists because adoption barriers weren't addressed. Process changes at global scale need to work for teams with different workflows, technologies, and constraints. For example: - Getting teams to integrate the new system into their existing workflows.

Establishing clear guidelines fo: + Creating processes for teams issues.

«+ Setting up support channels an + Defining migration paths for di: Cultural shifts are what make im] At global scale, cultural changes are more crucial. Youre not just chan about their work—you're trying to across the organization. For examp) implemented a policy where the per to fix it immediately. But without pr more stress rather than better practi consistent effort and clear demonstra + Building trust in the new syster + Getting teams to prioritize keep Fostering a culture where fast fi + Encouraging teams to contribu platform.

Having a clear technical found: cultural elements isn’t enough—yo to roll them out. Successful global succeed through a “big bang” appro prove value through focused pilots execution and strong relationships.

Start by building a coalition of th global initiative are crucial for buildir

[&] Rather than trying to convince everyone at once, focus on finding and enabling the people who already understand the problem and want to help solve it. For example, the mobile team spending three hours daily on build failures will become enthusiastic early adopters, while a small product team with 5-minute builds will probably show little interest. This focused approach helps you refine solutions with motivated partners before scaling more broadly: Share the identified problems and proposed solutions with potential stakeholders.

Find teams who are feeling the pain most acutely and with supportive leaders—they’ll be your best pilot candidates.

Connect with influential developers and tech leads who can become champions.

Build relationships with key leaders who can help remove organizational barriers.

Run focused pilots to prove value and refine approach. Pilots are your opportunity to validate assumptions and build compelling evidence for broader rollout. They're not just about testing technical solutions—they’re about learning how to drive adoption and support teams through change: Help teams design and run experiments with the new tools or processes.

Build quick prototypes to show what’s possible. Al tools can accelerate this prototyping phase.

Collect specific feedback about what works and what doesn’t.

Measure adoption and effectiveness of Al tools alongside traditional development metrics.

Document both successes and challenges openly.

Create initial templates and playbooks based on real usage.

Measure impact in ways that r and leadership.

Build momentum through ¢ community. As you expand beyond | proving the solution works to making a broader audience. This requires buil scale with adoption: Share concrete wins and learnir Create spaces for teams to sha one another.

Establish regular touchpoint: maintain alignment.

Make it easy for new team: onboarding, clear documentatic Celebrate and amplify teams wl Growing from pilot teams to 1 transition that many DevEx initiat scale requires more than just good t wins. You need robust feedback loo; can handle increasing adoption wh momentum.

Knowing when to make this transi but there's a reliable signal: Feedback getting useful new insights from yor ready to expand—but only if you'v feedback rather than waiting for it to:

Create clear paths for engagement at every level.

Regular check-ins with pilot teams to understand evolving needs.

Open channels for developers to report issues and request features.

Structured ways to gather feedback from tech leads and managers.

Periodic reviews with senior leadership to maintain alignment.

Community spaces where teams can help each other.

Regularly update playbooks and documentation based on team experiences.

Share metrics that demonstrate impact to both developers and leadership.

Identify patterns in team successes and struggles.

Look for opportunities to expand scope based on learned needs.

Keep iterating on all three elements: technical, process, and cultural.

Build systems that scale with adoption.

Automate common support requests and onboarding steps.

Create self-service resources for teams to get started.

Establish clear ownership and support models.

Plan for increased load on infrastructure and support channels.

- Document everything—from management approaches.

Integrate with Al development Motivate change through visibility a “Gaming the system” has a negat if sharing data can actually drive designed metrics can indirectly inflt generate energy toward organizatio When Dave Anderson was a Dire for improving platform error rates, challenge: He needed to drive chan over engineering roadmaps.

His initial approach—directly as error reduction—failed. These mar focus on their primary deliverab lacked visibility into the problem.

Dave's breakthrough came fic psychology. He created a monthly e - Listed every team’s error rate - Identified each organization - Highlighted the director or V - Was distributed directly to A Team) including the CEO.

“I warned all organizations abou before sending my first monthly r shared. “I still remember a direct

asking, ‘How much time do we have to fix this before the next report goes out?!” The results were dramatic. Leaders mobilized immediately to avoid appearing at the bottom of the list. Error rates plummeted week after week—all without Dave’s team writing a single line of code. The entire initiative consisted of a strategically designed email built with Outlook and Excel.

What this means for you: When economic arguments alone aren't compelling enough, consider using competitive dynamics. Create visibility around key metrics compared across teams or against industry benchmarks. Leaders respond powerfully to the prospect of public comparisons—whether against internal peers or external competitors. No one wants their team to rank last.

Chapter 32 Drive Change With Local Scope of Control Local scope of control means you can drive meaningful improvements without needing broad organizational support or resources.

THIS CHAPTER IS primarily for engineers, tech leads, and engineering managers who want to improve developer experience within their teams. The quick-wins approach from Step 2 is especially relevant for local-scope improvements.

Even if you have global scope, the strategies here are valuable.

The most effective global DevEx initiatives often use these same bottom-up tactics: Starting small, experimenting with willing teams, proving value through concrete results, and then scaling what works. Understanding how local improvements succeed can help you design better pilot programs and support grassroots innovation across your organization.

The biggest challenges in local scope aren’t about scale—they’re about picking the right battles and building credibility through results. You might not be able to rebuild the entire CI infrastructure, but you can significantly improve your team’s productivity through focused improvements to te development workflows.

There are two critical ways tl typically fail. Having limited scope significant improvements, but it ¢ strategic about where you focus your ¢ initiatives stumble either by taking or success too contained. Understanding avoid common pitfalls and maximize The first failure point is taking on local scope. This happens when team have authority to modify, take on ch cross-team coordination, build solu resources to maintain, or get stucl approval or support. These efforts « but quickly bog down in complexity team’s control.

The second failure point is keeping local. This happens when teams don’ how they did it, miss opportunities t problems, keep effective practices isol to build support for expanding suc these teams may solve their immed chance to multiply their impact ar struggle with issues they've already sc Local improvements still need tc and cultural changes to succeed. W a smaller scale, the fundamental prin

remain the same. Technical solutions alone won't stick, and process changes without supporting infrastructure will fade.

Let’s look at how these elements come together through the lens of a common local challenge: Improving your team’s test suite.

This example shows how even a focused, team-level improvement touches all three aspects of lasting change.

The technical foundation should focus on immediate team pain points. Start with improvements that your team can implement and maintain themselves. Unlike global initiatives that might rebuild entire systems, local improvements typically focus on enhancing existing tools and workflows. For example, one team discovered that 80 percent of their test failures came from three tests that depended on external network calls, so they mocked those dependencies and saw failure rates drop to under 5 percent. While you might not be able to replace the entire test framework, you can significantly improve how your team works with it. Some work the team could do includes: + Identify and fix flaky tests.

+ Improve test performance and reliability.

+ Apply better test organization and naming.

+ Uselocal tooling to help write and debug tests.

«Optimize workflows for Al-assisted development.

Process changes help the team adopt better practices. While technical improvements make better testing possible, process changes make it probable. These changes define how your team works together and establish shared expectations. For example, one team created a simple checklist: "Does this test have a clear name?

Does it test one thing? Can it run independently?” This reduced test review comments by 70 percent. The key is to create lightweight processes that make doing the right t consider are: Establish clear patterns for writ + Create guidelines for test covers + Setup code review practices tha + Make it easy to report and fix te: Cultural shifts ensure improven This is perhaps the most crucial ele Without cultural buy-in, technical in processes get bypassed. For example, « horror stories sharing session where | bad tests without judgment, leadin Cultural changes at the team level than org-wide shifts, but they still re example: + Build a shared understanding o: + Get the team to prioritize fixing + Create pride in maintaining a re «Make it safe to report and discu: However, having a strong foun and cultural elements isn't enough— to implement improvements withi improvements succeed by focusing or can solve, proving value quickly, and help other teams facing similar challe Start by building team alignmen global initiatives where you need | local improvements need deep unde

cc = your immediate team. This focused scope lets you have richer discussions, generate excitement around the problem—because it’s shared by the team—and move faster.

Have open discussions about pain points and their impact on daily work. Run a team retrospective focused specifically on development friction, or dedicate 15 minutes in your next team meeting to ask: “What slowed you down this week?” Get the team involved in prioritizing which problems to tackle first. Use dot voting in a team meeting or create a shared document where everyone can rank pain points by impact and effort.

Build a shared understanding of what success looks like.

Workshop this together—ask the team to write down what their ideal development day would look like, then identify the gaps.

Make sure everyone has a voice in shaping solutions.

Use multiple input channels: Capture individual perspectives through surveys or 1:1s first, then discuss collectively. Follow up with anyone who didn’t contribute to ensure you're not missing key viewpoints.

Create a safe space for concerns and alternative approaches.

Explicitly ask for devil's advocate perspectives in meetings, and consider anonymous feedback channels for sensitive topics.

Run small experiments as a team. The advantage of local scope is that everyone can participate in trying new approaches and providing immediate feedback. This collective experimentation helps build investment in solutions and catches issues early.

.

Start with lightweight changes that the team is excited to try.

Set clear timeframes and ge evaluation.

Gather feedback from differe: styles.

Use data to measure progress ar Document what works and wh: insights.

Be ready to adjust based on the Document successes and learn Good documentation isn’t just about it’s about capturing the team’s collecti This shared history helps your team e and creates richer resources for other Write down not just what approaches worked for your tea Keep track of different team insights.

Create practical guides that refl Collect metrics that demonstrat Build a story of collaborative i learn from.

Successfully improving DevEx 1 opportunities for broader impact.

problems effectively, other teams ne your primary focus might be helpin; successes can organically inspire an challenges.

Share learnings in ways that invite collaboration and adaptation. The key to spreading successful patterns isn't about prescribing exact solutions—it’s about sharing your team’s journey in ways that help other teams envision their own.

Create clear, practical documentation that tells your team’s story.

Package improvements to make experimentation easy.

Include the context of what didn’t work and why.

Be open about challenges and how your team overcame them.

Provide concrete examples that show real-world impact.

Build organic connections with other teams. The most effective way to spread improvements is through natural team-to-team relationships. These connections create spaces for mutual learning and adaptation.

(© Share your team’s story informally in engineering discussions.

Connect with other teams who express similar frustrations.

Offer to brainstorm how your solutions might adapt to their context.

«Create opportunities for teams . Learn from how others mod patterns.

Consider whether to advocate Sometimes local improvements 1 benefit from broader investment.

for organizational support often cor successes.

+ Collect stories of how the impre daily work.

+ Document how other teams ar patterns.

. Identify what additional organizational support.

+ Connect with leaders who see t!

+ Show how natural adoption ps support.

Chapter 33 Drive Change With Middle Ground Scope of Control Some DevEXx roles fall between global and local scope—you have the mandate but not the resources.

THIS IS A common situation, especially in organizations just starting to formalize developer experience work. You might have the job title and nominal executive support, but you're operating without dedicated resources or established authority. This is how many successful DevEx initiatives begin.

Working in this middle ground requires combining strategies from both scopes. While you have the organizational mandate of global scope, youll need to rely heavily on local-scope tactics to create impact. One DevEx lead started a monthly show-and-tell lunch where teams could demo a 5-minute improvement they’d made, leading to several teams adopting one another’s solutions.

+ Build strong relationships with teams who are already improving their developer experience.

«Help connect these scattered efforts into a more cohesive narrative.

Use your official role to improvements.

Create lightweight ways for tear Document patterns that ems efforts.

Turn this constraint into an limited resources can feel frustratin opportunities. For example, rather system, you can help teams compare collectively choose which improvemes You can spot patterns across might miss.

Your official role gives you licen: Teams may be more willing to v imposing solutions.

You can build evidence for concrete successes.

The patterns you discover off future global initiatives.

Some improvements work at any scc Some DevEx initiatives can be ef global or local scope. For exam; —the goal of increasing uninterr remains the same, but the executi control. The core principles stay cor Communicate the problem, run ex;

and share learnings. What changes is how you apply these principles: At global scope, you identify that developers across the organization spend too much time in meetings and lack focused development time. You might: Work with leadership to analyze meeting patterns across teams.

Create guidelines for meeting-free blocks of time.

Help teams design their own experiments for improving focus time.

Collect organization-wide data about productivity impacts.

Share successful patterns across the organization.

At local scope, your team recognizes they're spending too much time in meetings. You might: Establish “Focus Fridays” within your team.

Block out calendars for dedicated development time.

Review and reduce recurring meetings.

Collect feedback on what works for your team.

Document your approach to share with other interested teams.

In both cases, you're solving the same core problem, just at different scales and with different leverage points.

Understanding your scope of control helps you choose the right strategies for improving developer experience. While the core principles remain the same—focus on real problems, balance technical and cultural changes, mea them varies significantly based or resources.

The most effective organizations at all levels. Global initiatives pro practices across teams. Local impro points and often reveal patterns wort in between these scopes help connect strategies, turning limited resources strong relationships and emergent might discover that three different deployment issues in their own we another with parallelized builds, ar approval processes.

Build alliances and create info: scope, success often depends on creating informal influence networks authority. In one example, a #buildgrew from 3 frustrated developers with some solutions spreading to te requested help.

+ Partner with influential teams amplify your message.

Find natural allies—other team those already interested in Dev] + Create informal working grour around shared problems.

«Leverage existing relationship creating new formal processes.

Focus on solutions that demonstrate cross-team value.

Delivering value to several groups is critical with medium scope.

Here are some more things to think about: Choose initiatives that solve problems multiple teams are experiencing.

Share results that resonate across different contexts— highlight metrics and stories that other teams can relate to their own situations.

Create reusable assets (tools, processes, documentation) that teams can easily adopt.

Document your approach so other teams can experiment with modified versions.

Navigate organizational dynamics strategically. This can be the key to success. In one example, a leader recognized the company was focused on security compliance, and positioned faster automated testing as "reducing security risk through more frequent validation” rather than just "improving developer productivity.” Here are some additional strategies to consider: Work within existing approval processes and budget cycles rather than trying to change them.

Frame improvements in terms that align with current organizational priorities.

Be patient with adoption timelines—medium scope often means slower but more sustainable change.

Know when to escalate to leadership and when to work peerto-peer.

Building a DevEx team from the mid Ibotta’s “startup within a startup.” When Minh Pham and Titus Stone experience improvements at Ibotts team or dedicated budget—just grc 230-engineer organization needed t processes.

“We view it as a startup within “We believe it has a lot of value we're not fooling ourselves that our leadership, our investors, are going Their middle-scope approach c organizational influence: - Building coalition. They st engineers what they'd work time—overwhelmingly Dev!

them concrete evidence of de - Proving value incrementall internal search tool helped t technical wins to business about.

- Continual relationship man: updating our elevator pitct notes. Monthly check-ins w kept them aligned while builc This patient, relationship-dri earned them formal team status ar

constraint of limited authority into an advantage through demonstrated results and strong stakeholder relationships.22 No matter your scope, success comes from focusing on real problems and driving change thoughtfully. Whether you're rolling out organization-wide improvements or making your team’s daily work better, the key is matching your approach to your actual ability to implement change. And sometimes, that means starting small and letting success create opportuniti As you implement changes to imp: essential to track your progress and d work. Without clear evidence of imps can lose momentum and support. In how to evaluate your DevEx improver business value effectively to ensure growth.

# STEP 7

Evaluate Your Progress and Show Value YOUR DEVEX IMPROVEMENT initiatives are now underway, with changes being implemented at the appropriate scale for your role and organization. But how do y And how do you ensure stakehol improvements? This chapter will she progress and translate DevEx wins with business leaders.

Evaluation isn’t the final step ir critical checkpoint in a continuous evaluation allows you to assess your and make necessary adjustments to or metrics. It also gives you an ¢ stakeholder priorities and communi effectively.

Chapter 34 Analyze Your Data All the data in the world won't provide you with much value until you analyze it.

WHEN YOU BEGAN your DevEx improvement work, you identified metrics that were accessible, captured various aspects of developer experience, and would resonate with your stakeholders (Step 3).

(© As you reach your periodic checkpoints, it’s time to review these metrics—both to demonstrate impact and reassess your measurement strategy.

Choose the right analytical approaches for DevEx metrics.

Different metrics require different analytical techniques to reveal their true story. Here are key approaches to consider.

- Don’t go on “fishing expeditions"—write down your hypotheses first. Don't just slice and dice your data until you find something interesting—that’s fishing. Exploratory analysis is valuable but digging through data without a clear question increases the chance of finding spurious correlations. Start with testable ideas about what you expect to see and why. This keeps your analysis honest and defensible.

Think carefully before using using averages unless you ha (that is, your distribution is h on the ends when plotted on to calculate, averages can hid DevEx data is often subject example, an average build time some teams experience 20-hous experience 2-minute builds.

Report aggregates with pe These reveal the distribution organization, but only use the data: » p50 (median): Shows the tyj » p90: Highlights what most ¢ For example, a p90 build t percent of builds complete percent take longer.

» p99: Reveals your worst-cas Leverage cohort analysis for data by meaningful segment product areas, tool usage) to i are uneven or where specific ch Use time-series visualization f over time. Plot metrics over f trends, seasonal patterns, or co (releases, infrastructure change known events and interpret ti metrics can also be heavily af

Cc = holidays, major releases, and onboarding cycles can all create trends or spikes that can be misleading when looking at data.

Use correlation analysis to examine relationships. Examine relationships between metrics. Are faster build times correlated with higher deployment frequency? Do teams with better documentation also have fewer onboarding issues? Are teams using Al assistants showing improved code velocity?

How does Al-generated code correlate with review times or bug rates? And remember: Correlation doesn't equal causation—proving the direction of relationships requires more sophisticated methods.

Look for plausible explanations, not just patterns. A correlation isn’t useful if you can’t tell a reasonable story about why it exists. Use your domain knowledge and talk with developers to confirm whether a pattern makes sense.

Use variance and standard deviation to gauge consistency.

High variance in usage statistics suggests uneven implementation or adoption—and makes it difficult for teams to use existing data for predictions. High variance in system behavior like build times can indicate optimization gaps (like caching), making it difficult to plan sprints or estimate delivery timelines. Histograms can be a useful visualization to show this.

Before-and-after comparisons can communicate changes.

Calculate both absolute changes (e.g., 3 minutes faster) and percentage improvements (e.g. 30 percent reduction) to provide context.

Revisit and refine. Hypotheses evolve. Use your findings to sharpen your next questions and analyses and keep documenting what you're learn How Microsoft uses cohort analysis | drive targeted improvements.

Brian Houck, a senior principal ap: has found that cohort analysis is : patterns that would otherwise rer data. His discoveries show why lo metrics matters: Repo size can be important.

monorepos experience pull reques twice as long as those in smaller disappear when analyzing all reposi Unexpected language patterns C++ developers in Brian's dataset PR completion times than C# devel finding became valuable precise questions: Were slower build tools the inherent complexity of their C+: Seasonal effects hide in plain s: swings in active coding time ac to an unexpected culprit: Dayligl consistently affected developer pr annual averages or the most recent completely masked this recurring p These discoveries directly sl investments, helping teams dist problems and normal variations in

[&] Remember to define your unit of analysis. When calculating any DevEx metric, be explicit about what you're measuring. “90% of developers experienced build times under 8 minutes” tells a very different story than “90% of all builds completed in under 8 minutes.” The same principle applies whether you're looking at averages, percentiles, cohorts, or correlations—always clarify whether you're measuring per person, per event, per team, or per codebase.

This clarity helps you avoid misleading conclusions and ensures stakeholders interpret your data correctly.

Refresh analyses for your metrics. Return to your metrics plan and gather fresh data, whether through developer surveys or by analyzing system data collected since your last report. Compare your current performance against two important baselines: + Your initial baseline from when you started the initiative + Your performance at the last reporting period These comparisons help you identify improvements or regressions in developer experience and calculate the business value of those changes. Look for patterns in the data—are certain teams showing more improvement than others? Are some metrics moving faster than expected while others lag? These insights can guide your next steps.

When analyzing system metrics like build times or deployment frequency, consider both the central tendency (what’s typical) and the distribution (how experiences vary). For example, reducing your p90 build time from 15 minutes to 8 minutes might be more impactful than improving the average from 5 minutes to 4 minutes, as it addresses the worst experier affect productivity and satisfaction.

differences between teams using Al using traditional approaches—this ca potential friction points of Al adoptic initial rollout.

For survey data, pay attention to b distribution of responses. A flat averaj opinions where some developers ar frustrated. Segment your analysis tc target improvements more effectively Gather case studies about develo; part of the story. To gain a comple feedback about developers’ daily exr like: «What aspects of their work hav «Which processes remain difficu + How are Al tools affecting the; productivity?

+ Have communication pattern documentation more or «c differently?

Your organization-wide champ; insights they've gathered, or you cai piloting new initiatives. The most quantitative metrics with real de comprehensive narrative of progress.

Chapter 35 Prepare to Communicate Your Results Different audiences care about different aspects of developer experience.

WHEN SHARING YOUR data, keep in mind your stakeholders. Two (© main stakeholder groups are developers and leadership, so we cover some examples here.

For developer audiences: Focus on improvements that impact their daily work.

Time savings. Show how improved processes and feedback loops affect everyday tasks.

Reduced toil. Quantify how improvements in automation and tooling have eliminated frustrating manual work.

Improved focus time. Show how changes to meeting or calendaring practices have created more uninterrupted time for deep work.

When presenting these calculations to developers, connect metrics directly to their experience. Instead of simply reporting —_— “build times improved by 30%,” translate this to “30% faster builds mean you can stay in flow and get feec —and you'll save an average of 45 min For leadership audiences: Lea changes—and how they impact the bt Business Case, we identify five ways t things they care about and that imps use the same approach to communi leverage things that speak to them.

Tying improvements to business v you are in the journey. For example, s.

may be possible within the first fe improvements to revenue may take r development cycle. We discuss this ir here: Making money: Accelerated re between DevEx improvement can highlight faster time-to-m: deployment improvements to their business impact.

Saving money: Quantify dir reduced cloud spend from mo license costs from standardizat costs. These savings directly recurring costs, show how thes Recovering time and produc saved by reducing friction—e developers wait rather than savings across your developer value using fully loaded engine

cc = Correlations to business outcomes. Connect DevEx improvements to business metrics. Show how better build performance correlates with fewer production incidents, then multiply the incident reduction by your baseline average cost per incident.

Solving problems that keep them up at night. Make explicit connections between DevEx improvements and leaders’ priorities. For example, document improved security posture and better compliance outcomes. While these connections might be obvious to you, spell them out clearly for leadership.

Tie to company priorities. Show how DevEx supports current company initiatives. If your organization has a security push, demonstrate how increased automation builds security checks into every commit—simultaneously improving developer experience (less manual toil) and security posture (consistent enforcement).

Something to brag about. Provide leaders with concrete DevEx wins they can highlight in their quarterly reviews, board presentations, or industry conversations. For example, “Our team reduced build times by 40%, putting us among the top performers in our industry” or “We've automated 85% of our deployment process, enabling weekend releases without additional staffing.” These accomplishments give leaders tangible success stories that reflect well on their leadership while showcasing the value of their investment in DevEx.

Performance gaps. Illustrate how your improvements are moving the company closer to industry standards, closing the gap between your current state and what's possible.

When presenting these calculations to leaders, connect them to business goals and language. R: “Build times improved by 30%,” trar 45 minutes daily, recapturing 9,750 valued at $1.2M.” For maximum impact, package yo aligned with leadership priorities. Fo using a simple table: DevEx Initiative | Annual Value Value Type Build acceler- $3.3M Productivity ation recapture Cl/CD optimi- $1.2M Direct cost zation reduction Quality automa- | $1.32M Incident cost tion avoidance TOTAL IMPACT $5.8M Remember to customize your leadership audiences—CFOs will care ROI, while CTOs may focus on engin alongside financial benefits.

Refer to Part III for more o business case for continued invest: calculation examples, practical tem communication guides, see the Step 7

Evolution from manual to automated evaluation.

As your DevEx initiative matures, you'll naturally progress from manual analysis to more automated evaluation systems. This evolution follows a predictable pattern that mirrors product development.

Start with manual processes. In the early stages, expect to manually pull data, run analyses, craft reports, and update dashboards. This hands-on approach has advantages—it builds deep understanding of your metrics and helps you identify which data points actually matter to stakeholders.

Focus on value before automation. Like a startup finding product-market fit, prioritize delivering valuable insights before investing heavily in automation. Use these initial cycles to refine your metrics, visualization approaches, and reporting formats based on stakeholder feedback.

Incrementally automate high-value components.

Once you've established which metrics and reports consistently deliver value, begin automating their collection and presentation. Start with the most timeconsuming or frequently needed elements: Data collection scripts for commonly used system metrics.

Reusable report templates with standardized visualizations.

Scheduled data refreshes for critical dashboards.

. Automated distribution stakeholders.

+ Develop a comprehensive As your DevEx improvemer established, invest in creatir that integrates data sources provides self-service access stakeholder groups.

Remember that even mature some manual components, pa assessment and storytelling. Th everything, but to free up your tim.

you can focus on insight generation Use visualizations to improve impact. Effective data visualization t compelling stories that stakeholders designed visuals not only make your also help emphasize key improvemen missed in tables or text alone.

Most people, especially busy exec visual information faster than text.

or diagram can convey in seconds wi!

explain. For DevEX initiatives, where: metrics across different teams or s; become essential for demonstratin, stakeholder engagement.

The key to effective DevEx visualization lies in selecting the right format for your specific data and audience, then executing it with clarity and purpose. Your visuals should immediately answer stakeholders’ most pressing questions, such as: “Are we improving?” “Where should we focus next?” “Is this initiative delivering value?” These visualization formats are particularly effective for DevEx reporting: + Side-by-side workflow diagrams showing eliminated steps or simplified processes. These are particularly effective for demonstrating reduced complexity in developer workflows.

Use consistent colors and shapes, with clear annotations pointing out what’s been removed or improved.

+ Before/after charts highlighting key metrics. Bar or column charts work well for this purpose, using consistent scaling to ensure fair comparisons. Consider using color to highlight improvements.

- Annotated metric comparisons that make it easy to interpret direction and impact at a glance. Include visual cues like up/ down arrows, color coding (green for improvements, red for regressions), or simple icons to indicate whether changes are positive or negative. For example, show a decrease in build times with a downward arrow in green, while showing an increase in deployment frequency with an upward arrow in green.

- Sparklines or trendlines showing metric performance over time. These compact visualizations are especially valuable as your initiative matures and accumulates more reporting periods. They provide context beyond simple before/after comparisons.

Use layout strategies for maxim individual visualizations is just the st: these visuals in reports and dashboa impact and usefulness. A thoughtf stakeholders through your data st on what matters most. Consider tl designing your DevEx reports: + Establish a visual hierarch attention to the most import metrics and most significant i the top or beginning of your inherent tension so users can se + Create consistent dashboard grouped together and consister periods. This familiarity help: information they care about.

- Implement progressive disclc level summaries and providing detailed data. Executive sumn improvements, while linked sec can reveal team-specific data fo - Balance text and visuals to sug Key insights should be highligh forms, with the text explainir visuals.

+ Use white space effectively t and prevent visual overload. De difficult for stakeholders to ider

+ Create targeted views for different stakeholder groups that emphasize the metrics most relevant to their priorities. What an executive needs to see differs from what engineering managers need to see.

When creating visualizations, remember that the goal isn’t just to display data—it’s to answer key stakeholder questions within seconds, whether that’s “Are we improving?” or “Which areas need more attention?” or “What tradeoffs are developers having to make in their work?” Follow established best practices for clarity and impact. We include a visualization guide in the Step 7 Workbook to help you create compelling, accurate representations of your DevEx improvements.

(© The iterative nature of analysis and reporting.

Preparing data-driven DevEx reports is rarely a linear process.

You'll often find yourself moving between analysis and communication in multiple iterations: 1. Analyze your initial data based on your metrics plan.

2. Begin drafting your report or presentation.

3. Discover gaps or new questions that arise from your preliminary findings.

4. Return to your data for additional analysis or different visualization approaches.

5. Incorporate these new insights into your report.

6. Test the clarity of your message with a colleague.

7. Refine visualizations or explanations based on feedback.

This cyclical process is normal a improves both your understanding to communicate its significance effe iterations in your reporting schedu presentations to leadership.

cc = Chapter 36 Share Progress It's not enough to make progress in your DevEx improvement initiative, you also need to communicate that progress to stakeholders.

## TIME YOUR COMMUNICATIONS

strategically. Different stakeholders need updates at different cadences. We generally recommend the following cadences, though different ones may work better in your context. The key is to align with existing meetings and rhythm of business so you can take advantage of existing structures and processes.

Executive stakeholders. Twice yearly, focusing on ROI, strategic alignment, and 1-2 standout technical examples.

Technology leadership. Quarterly business reviews focusing on technology improvements and impact/value to their org, as well as appropriate comparisons (e.g., to their last report, and to other orgs that are similar).

Engineering managers. Monthly updates highlighting teamspecific benefits. You may also want to consider periodic reminders about available tools and resources for engineering managers.

Developers. Monthly updates highlighting improvements The that benefit them as a devel detailed data or dashboards the deeper. You may also want to about available tools and resour timing of major anno avoid competing with major prod: announcements, or holidays when sh: Integrate DevEx evaluation with maximum impact, align your Dev your organization's established busin ensures DevEx insights are available made and creates natural opportu requiring separate meetings or proces Quarterly planning cycles. Si DevEx evaluations 2-3 week: begins. This timing allows yout teams are determining priorit Prepare condensed summarie improvements have supported where further investment woul Annual budgeting process approaches, compile year-ove demonstrate ROI and business i investments have paid off ar potential returns from propos direct cost savings and product that finance teams can easily in Performance review cycles. P: with team-specific DevEx dat:

cc = © periods. This information helps them recognize team members who have contributed to DevEx improvements and identify areas where their teams might need additional support or training. For individual contributors, documented participation in DevEx initiatives can serve as concrete examples of impact beyond feature delivery.

Technology roadmap reviews. When technical leadership reviews technology roadmaps, ensure DevEx considerations are represented. Present data showing how developer experience friction points align with planned technical changes. This lets you highlight opportunities to address DevEx challenges as part of already-planned work rather than as separate initiatives.

Onboarding and training programs. Share targeted DevEx insights with teams responsible for engineer onboarding and training. This helps them focus on equipping new team members with skills and knowledge to navigate the most challenging aspects of your development environment.

By integrating DevEx evaluation into established organizational processes, you transform DevEx from a separate initiative into an embedded consideration in how the organization operates.

This approach reduces the perception of DevEx as competing for attention and instead positions it as a lens through which to view and enhance existing work.

Balance data with storytelling. While metrics provide credibility, stories create understanding and emotional connection.

For each key improvement: Identify representative user journeys that illustrate the before/after experience.

+ Collect specific developer testin life.

+ Create brief case studies of t benefited.

+ Use analogies that help nontechnical improvements.

For example, pair the statement 40%” with a story like: “The mobile of 2 days for code reviews, forcing between multiple tasks. Now they g within hours, allowing them to mai consistently within sprint boundaries Your developer surveys and ong are a great source for examples th: audience. (Pro tip: Keeping in close experimentation teams is a great v insights.) The attribution challenge: Measurin When you implement DevEx in factors in your organization may b including such things as net organizational restructuring, staffir improvements. This makes it diffic DevEx initiative X caused improve variables are in play.

Address attribution challenges t:

Acknowledging multiple factors. Identify and discuss other organizational changes that might influence your metrics.

Implementing targeted comparisons. Where possible, use control groups (teams using new processes vs. those following established methods).

Collecting specific feedback. Ask developers pointed questions about how your initiative directly affected their work: “How has the new CI pipeline changed your deployment confidence?” Presenting correlations carefully. Share data showing improvements while honestly addressing limitations: “After implementing X, we saw Y improvement. While we can’t attribute this solely to our initiative, developer feedback suggests a strong connection.” (0 Remember that stakeholders appreciate honesty about measurement limitations. Being transparent about the challenges of attributing a change demonstrates maturity in your DevEx approach and builds credibility for your findings.

© [&] Chapter 37 Navigate Conflicting Metrics Conflicting signals are normal in complex systems and offer valuable insights when approached thoughtfully.

AS YOU ANALYZE your DevEx data, youll likely encounter situations where different metrics appear to contradict each other.

Common conflicting patterns to watch for: Speed vs. quality tensions. Faster build times and higher commit frequency accompanied by increasing test failures or declining code review thoroughness.

Developer satisfaction misalignments. Improved developer satisfaction ratings alongside decreased output metrics.

Adoption vs. productivity paradoxes. High tool adoption rates but minimal productivity gains.

Short-term vs. long-term tradeoffs. Immediate productivity drops following infrastructure improvements that promise long-term gains.

AI adoption paradoxes. High AI tool usage but unclear productivity gains, or improved code generation speed alongside longer review cycles.

When you encounter these contrac to focus only on metrics that tell a pos Investigate the relationships bet connected metrics against each ot correlation. Is the increase in code su quality, or are they unrelated?

Segment your analysis. Break dow product area, or developer experienc resolve when you discover they affect Consider time horizons. Some im benefits in one metric while others : Track metrics over extended periods t determine if initial tradeoffs eventua the effects of deployment freeze win changes.

Engage developers in interpreta discuss the data with the developers Their contextual understanding oft moving in opposite directions.

Present the complete picture to st acknowledge tensions between metric what's causing them. This nuanced aj leads to more informed decision-maks For example, if you observe tha decreased build times but also redu discover through investigation tha certain test suites to speed up their to a need for more efficient testi fundamental problem with faster bu

suites for speed or implementing targeted testing would maintain quality while preserving the build time improvements.

By thoughtfully analyzing metric conflicts, you transform potential confusion into deeper insights about your development ecosystem and the complex interplay between different aspects of developer experience.

[&] Chapter 38 Learn and Improve Your goal is to continuously improve the DevEx in your organization by learning from what goes right, and what goes wrong.

MAINTAIN A RESULTS repository. Having a record of past performance—and actions—is one of the best ways to help learning.

Create a central location—whether a wiki, dashboard, or regular report—where stakeholders can track DevEx improvements over time. This historical record becomes invaluable for demonstrating sustained impact and securing continued investment in your initiatives.

By thoughtfully calculating and communicating the value of your DevEx improvements, you transform technical wins into organizational momentum that supports continued investment in developer experience.

If you create a dashboard, make sure there is the ability to look at not only current performance and trends over time, but also the state of the data at your established reporting timeframes. (e.g., “I may want to see today and how it compares to my starting baseline and the last report, but I probably also want to be able to see my performance status for the last four quarters.”) Turn evaluation into actionable i your own DevEx initiatives and e information they need to make in particularly valuable when evaluatir example, understanding not just wh assistants, but whether those tools experience and productivity.

As we've discussed, leaders an needs. A high-level view helps execu investments in DevEx improvement.

Engineering managers and dev granular data to diagnose specific fr targeted solutions.

Handle setbacks constructively.

Not every DevEx initiative or ex expected results. When metrics sho —or even regression—resist the ur these findings. Instead: shortfalls with defensiveness.

- Approach - Analyze what factors contri expectations and results.

- Engage developers direct perspective on what’s workin - Frame these insights as strengthens your next initiat:

[&] For example, if your build time improvements only achieved a 15 percent reduction against a target of 30 percent, don’t just report the miss—investigate why. Perhaps the initial baseline measurement didn't capture the full complexity of build scenarios, or maybe the solution addressed just one of several bottlenecks. These insights become the starting point for your next improvement cycle.

Balance new development with system maintenance. DevEx and platform teams can’t focus solely on solving problems with new features and innovations—they must explicitly carve out time for system maintenance, sometimes called keep-the-lights-on (KTLO) work. Marty Cagan of Silicon Valley Product Group estimates that traditional product teams need up to 30 percent of their time for maintenance, while platform teams often require up to 50 percent.3.

This higher burden reflects the critical nature and complexity of platform systems: When your build system or deployment pipeline breaks, it impacts every developer in the organization.

Maintenance work includes updating dependencies, monitoring performance, handling incidents, refactoring aging code, scaling systems, and updating documentation. The challenge is that this work is often invisible to stakeholders until something breaks.

Unlike new features that generate excitement, maintenance keeps things working at their current level.

maintenance as work that happens “when there's time,” reserve 40-50 percent of your team’s bandwidth for maintenance and operational work from the start. Use the remaining capacity for new initiatives. When communicating with stakeholders, frame maintenance as insurance against t risks—the cost of reactive maintena than proactive maintenance.

Evaluate your DevEx progress. T each initiative and gather feedback themselves and how they're being me Are the metrics capturing what Do the metrics align with busin Can you answer key stakeholde have?

Are there emerging friction poi you started?

Have team workflows or techn require adjusting your approact This feedback creates a virtuous informs not just what you improve ne entire process. Use these insights to: Update your initiative roa improvements based on impac needs. Sunset initiatives that ar or have been superseded by cha Refine your metrics fram approach should evolve as your new metrics that better captur to increase accuracy, and rem meaningful than anticipated.

Revisit your strategy. Periodic priorities and strategy) with a | real data. This might mean do

areas, pivoting to address newly discovered pain points, or realigning DevEX priorities with shifts in business strategy.

Communicate changes transparently. When you adjust course based on evaluation data, share both the what and the why with stakeholders. This builds credibility by demonstrating that your DevEx program is evidence-driven and responsive.

Teams that excel at DevEx consistently refine both their solutions and their measurement approaches based on what they learn, creating an adaptive system that becomes more effective over time.

Make learning systematic. Don't leave learning to chance.

Schedule dedicated retrospectives after completing major initiatives to document: What worked well in measurement.

What could be improved in you How stakeholder needs have ev Emerging DevEx challenges tha These insights feed directly bac developers) and Step 3 (data collectio cycle, ensuring that your DevEx effor than becoming static or disconnected When done effectively, this lear transforms DevEx from a series of iso capability that consistently deliver developers and the business.

Chapter 39 Evaluation Is Just One Step in a Virtuous Cycle Effective evaluation is the bridge that connects your current improvements to future initiatives.

BY MEASURING IMPACT, communicating value, and adapting based (© on what you learn, you create a sustainable cycle of DevEx improvement that builds momentum The cumulative effect of measured goes beyond individual metrics— developer experience is valued and c demonstrate repeated success, Devi as a cost center to a strategic adv organization's ability to deliver value.

Now that you've completed this ev begin again—armed with deeper insig stakeholder support. Return to Step 3 strategy based on what you've learne developers with fresh ears.

The journey to excellent developer with each cycle, you'll create more v your business.

# PART V

Evolving and Sustaining DevEx BUILDING A SUCCESSFUL developer experience initiative is just the beginning—the real challenge lies in making it sustainable and growing its impact over time. Unlike one-time projects that have clear endpoints, DevEx improvements require ongoing attention, evolution, and organizational commitment to deliver lasting value.

The most successful DevEx ini characteristics: They secure and pro scale, they create organizational struc change and adoption, and they with a product mindset that priorit Without these foundations, even the improvements can stagnate, lose adog burdens that ultimately hurt develope This part provides a practical | your DevEx efforts from promising organizational capabilities. Youll I initiative strategically, create change help teams embrace improvements, solutions, and develop metrics that mastering these practices, you'll ens continue delivering value long after tt

© [&]

## THE FIRST PRACTICE

Resource Your DevEx Initiative DevEx champions face a universal truth: You'll never have all the resources you want, but you can still deliver big impact.

“Leadership here just doesn’t get it.” “DevEx teams here are underfunded.” “The business doesn’t care about things outside of the core product.” We often hear technology leader: their lack of resourcing to improve de the hard truth: Like most internal initiatives, constantly feel underfunded. As we « investments in developer experience someone has to step up and drive the « The ROI calculations we explore i exercises—they’re critical weapons | resources. Rather than giving up bec funding, recognize that most success predictable journey: They start smal advocates working on borrowed time doors to formal funding, and eventua or organization-wide initiatives.

Chapter 40 Bootstrap Your Early Efforts Be prepared to start your DevEx improvement initiative with limited resources, like a startup.

MOST OF THE impressive developer experience initiatives you hear about today began with one or two people taking a calculated risk.

Like launching a new venture, there's no one-size-fits-all playbook for bootstrapping early developer experience projects to success. But through a combination of hard work, resourcefulness, strategic execution—and a bit of luck—you can build momentum and be successful. Here's how to approach those critical early stages.

Put in sweat equity. There’s no shortcut: In your earliest days, you'll need to find time outside of your core responsibilities to make progress. You can’t just ask others to do the work; you need to contribute yourself.

Leverage existing programs. If your company offers “20% time” (popularized by Google, where it led to products like AdSense), “Think Fridays” (a now-retired program at IBM that led to hundreds of patents), innovation days, or hackathons, use these opportunities strategically. They provide time to develop your ideas and partner with others while also gaining visibility in the organization.

Build a coalition of volunteers. D with most developers and frontline can contribute time, provide feedbacl Even small contributions from other the workload and strengthen your ini Focus on problems, not solution: specific vision or technical approach developer pain points—from develop rather than implementing a particul important as AI tools become availa adopt Al solutions simply because tt on whether they actually solve the fr are experiencing. Be willing to pivot developers you're serving.

Prioritize quick wins. With limit on making small bets that deliver x approach from Step 2 creates the 1 additional resources. Each success bu slightly larger effort.

Embrace learning and iteration.

succeed. Treat each attempt as a lea you better understand your organizati Wayne Gretzky famously said, “You 1 you don’t take.” From nights and weekends to fully f DoorDash’s DevEx journey Adam Rogal, now head of develope exemplifies this path.

Adam’s primary role at DoorDash was overseeing the existing internal developer platform. But he could see there was a growing need for better developer tooling and better ways to access those tools. Drawing from his experience at Uber, he had a vision for a unified interface for internal developer tooling— but recognized he couldn't secure the funding needed to tackle this overnight.

Instead of waiting for funding or permission, he rolled up his sleeves and invested nights and weekends to build a proof of concept for what has since become DoorDash’s highly successful (and fully funded) internal developer portal, DevConsole.

In reflecting on his journey, Adam shares, “Someone who wants to create one of these has to be a founder—somebody that is willing to invest every second of their free time into (© something like this. Because as I said, it is a startup within a startup.”

Chapter 41 Build a Dedicated Function As your DevEx improvement efforts gain traction, the next step is to carve out a place in your organization for it.

AS YOUR EARLY efforts gain traction, you'll eventually get the opportunity to establish a dedicated developer experience team.

This typically happens when your initial projects demonstrate (© clear value or when leadership recognizes emerging strategic needs around developer productivity. The advice in Part III, Making the Business Case, can help with this.

When pain points drive organizational change: Extend’s story Matthew Schreipel, head of experience at Extend, describes how their dedicated developer experience team was born: “Our build and test process completion times were out of control. The job of fixing this issue required a dedicated team that would have some ownership over every one of our services. From this need the platform division and the developer experience team was born.” When technical friction becom multiple teams, it often becom investment in specialized resources Developer experience teams t organizations. Sometimes they exis reporting directly to the CTO or VP o they operate as a specialized team infrastructure or platform organiza!

effective with the right decision depe: culture, and existing organizational st EliG) <<< Security Engine Infrastructure & Technolog

CTO

## “444

VP Engineering <<< Consumer Data Infrastructure Platform Engineering “<< Cloud Developer Infrastructure Experience goals, regardless of where they sit within the organization. Here ( Successful DevEx teams typically share similar missions and are some examples of real DevEx team charters from familiar companies: Slack: “Making the development experience seamless for all engineers.” Stripe: “Make software engineering easier at Stripe.” Google: “Make it easy for all developers to improve the world by creating fast, high-quality, and trustworthy experiences with the best technology from Google and the open source ecosystem.” Snyk: “Make Snyk a pleasure to develop within.” As the saying goes, there are only two hard things in computer science: cache invalidation, and naming things (and off-by-one errors). We've seen deve] names: Developer Acceleration at Sho; at Google, Engineering Thrive at Mic McKinsey, and more.

Rather than fixating on industry that resonates most with your leader organizational priorities. For exampl bringing up “engineering velocity” ir your team similarly positions your established business priorities.

There’s no magic answer to the teams of five developers dramatical times their size when their work pr and developers have the context they quickly. The difference isn’t just in systematically removing the barriers 1 While there’s no universal formulc three approaches can help you arrive + Delivery-based sizing. Calcul scope of what you need to d business requires. This method down push to solve specific pr function of time to deliver.

+ ROI-based sizing. Base headco on investment. This approac a strategic bet that isn't ob and leaders across the busine that investing in X enginee:

that investment in business value, your headcount request becomes more compelling.

Benchmark-based sizing. Compare against similar companies in your industry and stage. Organizations typically allocate about 10-20 percent of engineering headcount toward centralized developer productivity efforts, though actual numbers vary widely based on company maturity, industry sector, and In some cases, that percentag tools deliver more leverage.

Most successful teams combin benchmarks as a starting point whil delivery needs and ROI calculations.

Chapter 42 Developing Talent for DevEx Roles Building a successful DevEx function requires more than just securing resources—it demands the right talent with specialized skills.

DEVEX PROFESSIONALS NEED a unique blend of technical (© expertise, empathy, and communication abilities. Unlike traditional engineering roles focused on building customer-facing features, DevEx roles require a product-oriented mindset applied to internal users. The best candidates often come from diverse backgrounds— platform engineering, full-stack development, developer advocacy, or even product management.

Effective DevEx engineers and leaders typically demonstrate: Technical breadth and depth. Understanding a wide range of technologies (to enable supporting many developers) along with deep specialization in platforms and distributed systems. Specialization in tuning and serving data models is also important.

User empathy. The ability to understand developer pain points and prioritize effectively.

Data fluency. Skills to measur developer productivity metrics.

AI tool evaluation. Understang measure the effectiveness of Al impact on developer workflows Product thinking. Approachir same rigor as customer-facing Communication skills. Trans] different audiences, from engin This means you also need to find tl initiative. You can approach this in set Internal transfers. Look for ¢ interest in improving develog hack days, or contribute to inter individuals often thrive when g on DevEx full-time.

External hiring. When bringin candidates with previous platf engineering experience. Backgr advocacy can also translate wel Hybrid approaches. Many suc long-tenured employees who 1 with external hires who br specialized expertise.

Regardless of your approach, it’s talent density (that is, teams with n career and mid-career talent) is i DevEx teams. This is because of the

technologies they are responsible for, as well as the critical nature of systems that power the entire business.

Growing DevEx capabilities. Whether you're working with existing team members or new hires, developing it requires intentional focus.

Create learning opportunities through conference attendance, training programs, and engagement with the broader DevEx community.

Establish mentoring relationships between experienced DevEx practitioners and those new to the field.

Encourage cross-functional exposure by rotating team members through different parts of the engineering organization, whether through formal job rotations or close collaborations.

Develop business acumen by involving the team in ROI calculations and executive presentations.

Build community connections by participating in DevExfocused events, forums, and open-source projects.

Stay current with AI development trends by evaluating new Al coding tools, understanding their integration challenges, and measuring their real-world impact on developer productivity.

The most successful DevEx organizations invest in continuous learning. As the field evolves rapidly, staying current with emerging practices and technologies effectiveness.

Make sure there are career paths attract and retain DevEx talent, cre: opportunities.

+ Technical track. Moving senior engineer to principal/s developer productivity, platfo: AI infrastructure specializatio prevalent and important.

+ Leadership track. Growing fic director of developer experienc + Specialization paths. Creating in areas like metrics and automation, or developer educa Make these paths explicit, with « at each level. This helps team mr opportunities and signals organizatios valued discipline.

As your DevEx function ma development becomes increasingly nature of this work requires deliberate progression to build a sustainable cap

Chapter 43 Make Developer Experience Everyone's Job Empower your teams to improve DevEx whenever and wherever possible.

EVEN WITH A dedicated team, the space for DevEx improvements (© vastly exceeds what any centralized group can address. Each team has unique challenges that often can be solved only by the teams themselves.

The challenge is that in many organizations, teams don’t have the permission or authority to invest time in these improvements unless explicitly directed from leadership. By addressing this limitation, you can unlock a dramatically increased capacity for improving your organization’s developer experience and productivity.

Atlassian’s 10% time: Empowering teams to fix what sucks.

When Atlassian CTO Rajeev Rajan joined the company, he discovered a familiar problem: Teams knew what was broken but didn’t feel empowered to fix it. “When we spoke to our dev leads, we found that each team hz issues, but didn’t feel they had pern them.” The solution was elegantly simp] developers to use 10 percent of their that make their day job suck.” The results were immediate and: team improved their 48-hour deplo to 31 percent in one quarter. TI 24,000 lines of dead code. A cent: deployment frequency by 300 perce Rajan’s key insight: Developer jo teams need explicit permission to i aren’t feature work.

There are some proven practice constantly improve their DevEx. C practices: Establish clear time allocat leadership (like Atlassian’s 10 pi Identify DevEx champions wit with the central DevEx functi improvements.

Create visibility mechanisms team-level DevEx improvement work.

Develop shared measureme teams assess their own devel improvement opportunities.

Provide guidance on AI tool adoption that helps teams evaluate which AI development tools solve their specific problems versus creating new friction points.

Build knowledge-sharing channels where teams can exchange successful practices and solutions to common problems.

The ultimate goal isn’t building creating an organization where dev measured, and continuously imprc successful DevEx leaders recognize th: just from what their teams build, but broader engineering culture.

Chapter 44 Secure Budget at Different Organizational Stages As your DevEx improvement efforts scale, be sure that funds are available to support that growth.

ONE OF THE most persistent challenges in building a DevEx (© function is securing adequate funding. The approach you take should evolve as your organization grows and your DevEX initiative matures.

From startup to enterprise: Stage-appropriate strategies.

At startup scale (0-50 engineers), formal DevEx budgets are rare. Focus on leveraging existing tools and seeking time as products, pitching them to leadership just like you would pitch features to customers.

In growth-stage companies (50-200 engineers), begin with a modest tools budget before seeking headcount. Use early wins to build an ROI case while cultivating executive sponsors who understand DevEx value. Your first dedicated DevEx budget might be modest, but wi precedent.

For scale-ups (200-1000 en roadmaps with correspondir industry benchmarks to justif engineering budget on develop with tiered impact levels to choices.

At enterprise scale (1000+ er funding models that comt contributions from business companies dedicate 10-25 pe DevEx work and implement business units pay for DevEx groups should report key metr: demonstrate their value and im Protect your budget. Regardless of vulnerable during downturns. Consid Clearly distinguish between co and discretionary enhancemen Build a network of advocates at DevEx value.

Regularly publish internal cas highlighting ROI.

Leverage external validation t] and peer comparisons.

Organizations that maintain the; downturns typically recover faster an

having the data to show that these investments aren’t luxuries but essential drivers of resilience and competitive advantage.

Chapter 45 Making DevEx Stick Your DevEx improvement initiative will stall without ongoing effort.

IN THIS PART, we have provided you with everything you need to resource your DevEX initiative. However, this can all be boiled down to five principles that you must follow if you want your changes to stick: (© + Start small but think big. Most successful DevEx initiatives begin with bootstrapped efforts that demonstrate value before securing formal resources.

Evolve your approach as you s in the bootstrapping phase diff dedicated function or drive org: Balance central expertise witl most effective DevEx strategie teams with empowered local te: Align with business priorities terms that resonate with leads connection to business objectiv Measure and communicate im ROI of your DevEx investment: in terms that matter to differen By following the progression bootstrapped beginnings to dedicate wide adoption—you can build a sus practice that delivers lasting value to 3 and business.

## THE SECOND PRACTICE

Create Structures to Support Change GREAT DEVEX SOLUTIONS only mat them—change management is the : improvements stick. Identifying Dev] solutions is only half the journey. Eve improvements will falter without effe support their adoption and sustainab: Change management is just as work. Improvements won't stick unl repeat—which often means reshapir cultural norms along the way.

process for leading change, refined provides a proven roadmap for organ can be applied directly to developer ex Kotter’s framework provides a clea Chapter 46 1. Create a sense of urgency. H A Framework For DevEx Change DevEx improvements almost always involve cultural shifts, not just technical ones.

CULTURE CHANGE IS difficult to measure but critical to success.

This is particularly true when introducing new tools and AI development tools. For example, teams need to learn not just how to use new Al assistants, but when to trust Al-generated code, how to review it effectively, and how to maintain code quality standards. Creating shared language and goals accelerates adoption and reduces resistance to change.

When teams understand and use the same terminology around developer experience, it becomes easier to align efforts and track progress. Similarly, when goals are clear and shared across teams, people are more likely to embrace change because they understand how it connects to broader objectives. Many of these strategies build on the stakeholder communications we discuss in Step 5.

Follow a proven roadmap for organizational change. Successful DevEx change follows predictable patterns. John Kotter’s eight-step why DevEx improvements ca friction’s business impact—st experience slows delivery, is competitive disadvantages.

. Build a guiding coalition. Ass who can guide and coordinate technical leaders, engineering who understand both challenge . Form a strategic vision. Defin connect technical improvemer matter to leadership.

. Enlist a volunteer army. Get de participate in DevEx improv receiving them, showing im opportunities for meaningful c . Enable action by removing ba and cultural obstacles that p: better practices—eliminating tooling, and changing how tean . Generate short-term wins. ( improvements to maintain mx of DevEx work and energizin challenging changes.

—o 7. Sustain acceleration. Continue pushing for improvements after initial successes, using growing credibility to tackle more complex problems and systemic issues.

8. Institute change. Make new practices permanent by connecting them to organizational success and ensuring they become stronger than old habits through ongoing measurement, reinforcement, a The chapters that follow prov implementing each of these steps in helping you create lasting chan improvements.

[&] Chapter 47 Support Teams Through Change It's important to support teams through change—they're the ones who'll make or break your DevEx efforts.

ANY NEW TECH or process is disruptive, even when it’s meant to make things better in the long run. Teams need specific types of support to navigate these changes successfully and avoid sliding back into old habits. There are several practical ways to help developers embrace new ways of working.

Provide extra support during transition periods. Changing workflows creates temporary inefficiency before benefits emerge.

Offer extra support during these transition periods through dedicated office hours, specialized training sessions, and documented migration paths. Communicate clearly that things will likely get bumpier before they smooth out—this helps teams push through the initial friction.

Consider creating champions within teams or groups who receive additional training and can help their colleagues navigate changes, serving as day-to-day troubleshooters when issues arise.

This aligns with Kotter’s emphasis o —you need developers actively partic receiving end of tooling and proces important when rolling out AI deve need to develop new skills around p and using models, Al-generated cod assistance into their existing workflov Continue holding AMAs and | emerging challenges. As teams imple will emerge that weren't visible durir sessions create feedback loops that before they derail progress. If you large organization, local champions multiplies your reach while provic feedback. Developers often share chall that they might not surface in other s These local sessions are especially understand team-specific terminolo helping translate concerns into acti introducing AI tools, champions cs questions about when to use Al : approaches, and share practical tip: from these new tools. This iterative commitment to supporting teams rz change from above.

Create meaningful incentives fi embrace improvements. There are contributions to the DevEx init:

appropriate for your work and context. We've seen a few examples that work particularly well, such as: Organize hackathons with visibility and prizes to generate excitement around new tools or practices.

Tie DevEx improvement work to performance evaluations so teams know their (sometimes invisible) work is valued just as much as feature development.

Recognize non-technical contributions, like fixing or adding to documentation, removing friction from workflows, and being a local champion.

Arrange for leadership rec significant progress—this vit powerful and motivating.

Recognize effective AI tool improves code quality while helps establish cultural norms ¢

[&] Chapter 48 Guide Organizations Through Change Creating organizational change that lasts isn't easy, but you can make it easier by actively guiding it.

GUIDE ORGANIZATIONAL LEADERSHIP through the journey —their sustained support ensures resources and removes roadblocks. While teams focus on implementation details, leaders need different information and support to maintain commitment during the change process. Executives and managers want to see progress, understand challenges, and know when to expect returns on investment.

Communicate regularly with engineering managers and leaders about the work’s progress and challenges. Be transparent that improvement is not a linear journey—share the common pattern of a J-curve where teams might see quick wins from lowhanging fruit, then stall or even regress when hitting complexity and scale, before improving again after working through harder problems. Frame experimentation and failures as valuable learning opportunities that allow for faster adjustments. This transparency aligns with Kotter’s emphasis on g even when progress feels slow, con maintains momentum and shows st: working.

Share status updates and progres with each audience. Executive lead value creation, cost savings, risk advantages. (We cover this in more and engineering managers typicz oppor Translate your wins into terms that improvements, innovation we discuss in Step 5. Tailoring your n helps institute lasting change—Kotte: practices become embedded in orgar remaining temporary initiatives. The and 7 provides the data and feedback: Create visibility into long-term short-term wins. DevEx improveme significant value over time. Help st immediate gains and future payoffs strategy and roadmap. Create clear track progress on key metrics while next. This approach does double dx for upcoming improvements while work builds the foundation for tom celebrate quick wins along the way keep enthusiasm high when the bi horizon. These celebrations support K

acceleration—using early credibility to drive deeper organizational change.

[&] Chapter 49 Support Yourself Through Challenging Work Invest in your own sustainability—leading DevEx change is a marathon, not a sprint.

GUIDING TEAMS AND organizations through significant changes can be demanding and sometimes isolating. As the champion of better developer experiences, you need to maintain your own energy and perspective to be effective over the long haul. Here are some powerful strategies to sustain yourself through the challenging work of DevEx transformation.

Carve out time to learn about new technologies and industry trends. Staying current helps you anticipate future needs and ensures your DevEx strategy remains relevant. This is particularly important in the rapidly evolving AI development landscape, where new tools and best practices emerge frequently. It also helps you make better decisions regarding build vs. buy and gives you visibility into how other organizations execute their own DevEx work, including how they’re successfully integrating Al tools into their development workflows.

For example, seeing other organi guidelines can inspire and shortcut starting from scratch. Allocate regula conferences, or connecting with other this optional—it’s essential for effectiv Create a personal board of directc You'll need both technical and emot complex challenges. Identify mentc similar work who can act as your to provide advice, perspective, and e becomes particularly valuable during And don’t forget your champion earlier who do double duty. They not and troubleshoot hurdles, but they als the organization, giving you insight Building this supportive ecosysten the isolation that often comes witt Remember that leading change is ink research shows that transformation burn out before institutionalizing nev Practice what you preach b; sustainable pace. DevEx improve: sustainable engineering practices. M own workload thoughtfully and takir Demonstrating sustainable work pat changes you're trying to create.

Remember that effective self-c: boundaries—your physical and ment: effectiveness as a change leader. Mak

[&] food, and practices that ground you mentally, whether that’s meditation, time in nature, or whatever helps you recharge. Your DevEx work improves developers’ daily experience—you deserve the same.

Document and share your own learning journey. As you navigate the complexity of DevEx improvements, capture insights about what works and what doesn’t. Sharing these lessons helps others and creates an organizational memory that survives beyond any individual's tenure. (Be sure to check with your leadership or PR team to confirm what information can be shared publicly and if there are preferred outlets.) You'll find this documentation also strengthens your personal network as you connect with others facing similar challenges.

The process can be remarkably rewarding—whether you're directly mentoring someone on a similar path or indirectly helping countless others who discover and reference your shared experiences. This knowledge exchange creates a virtuous cycle that benefits both you and the broader DevEx community.

By thoughtfully addressing both technical challenges and change management needs, your DevEx initiatives stand a much better chance of creating lasting positive impact across your organization.

Investing in your own DevEx leadership.

Rose Nyte exemplifies the personal sustainability strategies outlined in this chapter. As a DevEx leader who has navigated multiple organizational cultures, she’s developed concrete approaches for supporting herself while championing better developer experiences.

Building a personal board of former executive coach with the trusted network a “board of director you and will tell you the truth abou you're in. She intentionally cultivat doing similar work across different multipliers” who actively connect he provides fresh perspectives and pr: who share her goal of making productive at work.

Continuous learning and stayi evaluates her learning source: conversations with her professior grounding and practical insights tk Her natural curiosity about people’ her knowledge and builds supportiv These strategies help Rose approach to the demanding work demonstrating how investing in directly strengthens your ability t engineering teams.

## THE THIRD PRACTICE

Make Technology Sustainable and Effective WHEN ORGANIZATIONS INVEST in developer experience, they often focus on technical capabilities while overlooking an important truth: The most powerful tools are use. This chapter explores three ess sustainable technology that deliver product mindset, implementing tho managing technical debt.

The difference between a transfor abandoned one isn’t just technical exc you approach the entire lifecycle fron By treating internal developers as trt their needs at the center, and bal innovation, you can create solutions t pain points but remain sustainable ov

Clear partnerships. You can with your customers—creating mind, running pilots with ther tools together.

Chapter 50 By thinking about DevEx improver Ado pt a Product Mindset you can identify clear value proposit: align with both your team’s goals and When measuring the success of y Every organization stumbles from time to time—here’s why. A 0 consider using the same metrics use ORGANIZATIONS OFTEN STUMBLE in their DevEx efforts for » Track monthly active users ( three key reasons. They build tools without truly understanding (DAU) to gauge adoption and re developer needs, they implement inflexible standards that hinder Measure customer satisfactio surveys to understand sentime: Monitor retention rates to see innovation, and they take shortcuts that create unsustainable (© technical debt. This chapter provides a framework for avoiding these pitfalls and building technology that truly enhances developer tools after initial adoption.

productivity and satisfaction. Use time-to-value metrics to s Rather than viewing tooling as “something we build for achieve their goals.

ourselves,” successful teams adopt a product mindset, grounded Apply feature usage analytics t in user needs and contextual analysis. This approach has several deliver the most value.

advantages: Track AI tool effectiveness 1 Accessible user research. Your customers (internal Al development features a developers) are relatively easy to find and observe since they productivity versus creating ne work at your own company. This makes collecting feedback i i . . These product-centric metrics p much simpler than if your customers were external. .

A Lo simple deployment counts, helping Tight feedback loops. Communication channels are more devel i tools. but h evelopers are using your tools, bu direct and targeted than they would be for external products, A —- gy real needs.

allowing for rapid iteration.

A cautionary tale: When tool-first thinking fails.

In 2020, James Russo joined Brex as a staff engineer on their platform team with a specific solution already in mind: An internal developer portal built using Spotify’s Backstage framework. Over the next two years, their team of six engineers invested substantial resources developing this portal. But despite their efforts, customary features such as the software catalog weren't resonating with developers.

Adoption remained stubbornly low—they never managed to get more than 20-30 percent of Brex’s developers to visit the platform weekly. When resource constraints tightened in late 2022, the team faced pressure to provide more value with fewer resources and to explicitly demonstrate that value.

(© Only after conducting their first developer experience survey did the problem become clear. “Our developers’ biggest pain point wasn't solvable via our developer portal. It was local development speed,” Russo shared. “At this point, it became clear to us that an internal developer portal wasn’t the right tool for the job, and we pivoted our focus to building local-first tools for iterating on changesets.” This story illustrates a common pitfall in DevEx initiatives.

Tool builders can become enamored with a particular solution before understanding the problem, whether that’s an internal developer portal or the latest AI coding assistant. The key is always starting with developer pain points rather than exciting new technologies.

Chapter 51 Use Product Management Principles to Build Better Solutions By using product management principles, you can solve real problems, < gain adoption, and create sustainable value for your organization.

PRODUCT MANAGEMENT INVOLVES several steps to help ensure a problem-based, user-centered approach to product development, while thinking holistically about the competitive landscape, adoption, and making measurable impact.

1. Understand your customers and their needs. This helps you not only empathize with the user, but identify the biggest problems they are facing. Talk directly to developers across different teams and roles (Step 1), and augment those discussions by collecting both self-report and system data from developers and their systems to identify patterns and priorities (Step 3). Use this information to define a product vision with solutions that demonstrate value.

2. Empathize with your stakeholders so you can better — understand their needs and communicate your vision and progress to them (Steps 1 and product vision to identify suc customers, sponsors, and addit; . Build a DevEx roadmap and insights you gathered stakeholders, and existing syst way to improve your chance: a quick win, so you can dem momentum (Step 2). Once you from your initial efforts and a can use evaluation criteria to product roadmap (Step 4).

. Prioritize ease of use in ever: DevEx tools like consumer proc interfaces, clear documentat Remember that developers ha tools—lower barriers to entry adoption rates. This is especial tools, where developers need | the tool, but how to prompt it generated code into their wo: for both initial onboarding ar consistent patterns that reduce . Create feedback loops to rema your users and the workflow so additional instrumentation (in in data), regular check-ins wi feedback and satisfaction data 3 and 4)

[&] 6. Continue to learn and discover as you build by experimenting, evaluating results, and iterating based on continued data collection and user feedback (Steps 2, 3, 4, and 7. Don’t forget release management. This includes technical best practices like versioning and backwards compatibility, deprecation policies, and migration support. This also includes continued communication with key stakeholders (Steps 1 and 5).

This approach ensures that your DevEx investments solve real problems, gain adoption, and create sustainable value for your organization. In the following chapters, we'll explore how to create standardized “golden paths” that reduce cognitive load while still allowing for innovation, and strategies for managing technical debt in your developer experience.

Apply product thinking to more than just automation and tooling. While this chapter focuses on treating your internal tools and platforms as a product, this represents just one application of product thinking to DevEx initiatives. The most successful organizations apply product management principles more broadly to their entire DevEx strategy—from platform tools and automation solutions to data and metrics.

Product thinking shifts the foc “collecting data” to “solving probler relationships with your developer ct projects. Because a data-driven apprc and because we have so much data pc our customers are internal users—it apply product thinking to data. This a . Developer needs drive y« instrumentation roadmap rat!

common formats (like dashboa + Solutions evolve continuous] changing requirements, provid DevEx team and your stakehold + Resources are allocated to areas . Adoption and satisfaction managed.

For a deeper exploration of solvi treating your DevEx metrics as a pros “Design Metrics That Evolve and Amp] how to apply product management iteration, and evolution of data.

[&] Chapter 52 Use Tooling Standardization to Drive Efficiency At some point, you're going to need to standardize to avoid chaos.

## STANDARDIZATION ACROSS DEVELOPMENT

delivers multiple benefits beyond simple consistency. By reducing environments the cognitive load for developers, they can focus on solving product problems rather than configuring tools or writing custom deployment scripts.

Support becomes more effective and efficient as platform teams develop deeper expertise with fewer tools rather than shallow knowledge across many versions. When teams use identical workflows and toolchains, teams can share solutions more easily, share information and debug problems more effectively, and developers who transfer teams accelerate their productivity.

Effective standardization should consider multiple layers in the development ecosystem. Tool standardization—from language choice to CI/CD pipelines to testing frameworks—creates a consistent foundation for daily work. Standardizing processes establishes shared methods for activities like code review, deployment, and incident managem: patterns, creating reusable architect machines) and project structures (suc!

faster and easier for teams to collabor: Standardization delivers the gr on common tasks performed by organization. After mapping your 1), focus on high-traffic areas—too developers will deliver the high Teams often prioritize the wrong standardizing pet projects or speci developers while neglecting daily testing, and deploying code that ev coding tools become more prevalent, Al-assisted development—including generated code and guidelines for wh approaches—can reduce cognitive lo across teams.

Prioritize areas where consistenc security, or compliance, and tasks be significantly reduced through au repetition.

Use standardization to create lev toolchain, you focus your investme standard tool benefits every team 1 20 different deployment tools, none resources get spread too thin.

[&] Remember: Standardization isn’t about control or cost-cutting.

It’s about creating exceptional experiences by concentrating your efforts where they’ll have the greatest impact.

Creating technology standardization is about managing expectations. Effective standardization requires a clear framework that balances organizational consistency with team flexibility. Most successful organizations implement a tiered approach. This creates clarity for development teams while allowing flexibility where it matters most. Most important, it establishes shared expectations about support levels and maintenance responsibilities across the organization.

Gold tier: The golden path.

The gold tier aligns with your organizations “golden path” (also called “paved path” or “happy path”) and includes the most commonly used tools, languages, and technologies. Teams choosing these technologies receive comprehensive support, including: - Zero maintenance burden. Platform teams handle all administration and infrastructure maintenance.

+ Fully automated CI/CD pipelines that “just work” without custom configuration.

- Managed database services with DBA support for optimization and scaling.

- Monitoring and logging for observability into their products.

- Pre-approval by security, legal, and compliance teams (although funding may be specific to their organization and licensing agreement).

This tier maximizes developer | infrastructure concerns, allowing te product development.

Silver tier: Supported alternativ Silver tier technologies have ac the organization but aren’t primary silver-tier technologies can expect: Partial support from platform tea Some responsibility for debuggin Contributing to shared solutions: Some responsibility for monitorir Pre-approval by security, lega (although funding may be speci licensing agreement).

This tier accommodates legitim: maintaining reasonable support effic Bronze tier: Approved experime: The bronze tier includes approve: Teams choosing bronze-tier options: - They own full responsibility maintenance.

+ No support is available from platf + They serve as the organiza technologies.

+ Pre-approval by security, legal, : any costs fully borne by the team.

+ Responsibility for all monitoring and logging.

«If the experiment fails, they are responsible for migrating any code, toolchains, and monitoring to an approved technology.

This tier enables innovation while maintaining governance guardrails.

Beyond the framework. When teams need technologies that don’t appear in any tier, they must provide: - Clear justification for why existing tiers can’t meet their requirements.

- Evidence of superior outcomes or unique capabilities.

- A sustainable operational plan.

- Commitment to security and compliance requirements.

- A clear expectation of support and work aligned with bronze tier technologies.

The power of Golden Paths: Google's approach to developer onboarding.

Instead of forcing new developers to navigate endless tool choices and YAML configurations, Google provides “Golden Paths”—complete templates that include everything a developer needs to build and deploy common services. A Golden Path might contain skeleton code, CI/CD pipelines, infrastructure templates, and monitoring setup—all preconfigured and ready to use.

Google outlines key principles behind effective Golden Paths: Reducing cognitive load through abstraction, providing clear opinionated methods for specific tasks, and lighting the complete path from develop: remaining optional for developers v The benefits are immediate: Fa: foundations across teams, easier del security policy implementation, ar costs.22 A critical component of star governance and evolution. Both tech monitored by a committee that reguls technology landscape. This cross-func technical leaders, security experts, : ensure the framework remains respo: evaluate usage patterns and support while keeping an eye on emerging tec current gaps or create new opportunit The committee establishes cle technology, defining the conditions be promoted, demoted, or retired. T!

adoption metrics, support burden, strategic alignment. Rather than m the committee relies on data and f using these technologies, creating a improvement.

When technologies need to be m completely, the committee develops a: timelines and migration paths. This the accumulation of technical debt frc outdated standards that no longer ser

Perhaps most valuably, the committee partners directly with teams using bronze-tier technologies to evaluate experimental outcomes. When experiments demonstrate exceptional value, the committee can shepherd them toward broader adoption and increased support. Conversely, when experiments fail to deliver anticipated benefits, the committee helps teams pivot gracefully to established gold or silver alternatives, preventing sunk-cost fallacies from prolonging unsuccessful approaches.

This governance mechanism transforms standardization from a static mandate into a dynamic, evolving framework that balances stability with innovation—preserving the benefits of consistency while remaining adaptable to both technological evolution and changing organizational needs.

Adobe's portfolio approach: Technology standardization that scales.

At Adobe, Dan Neff and Ken Anderson treat technology tiers like managing an investment portfolio rather than declaring winners and losers. “Gold technologies arent ‘winners,” Neff explains. “They’re where we concentrate resources because they serve the most teams with the greatest impact.” Think urban planning: Gold tier has utilities water, sewer, power—with comprehensive support. Bronze tier? You're tent camping—viable for the right team, but you handle everything yourself. Teams choose based on their needs and capacity: Critical services may choose gold tier for support and reliability, while experimental teams may opt for bronze tier.

The key insight: Effective standa —it’s about creating clear inves organizational capacity with team r Standardization isn’t a silver bul efficiency, a rigid approach can freeze Remember mainframes and COBC themselves into these technologies v faced massive technical debt later.

balance between standardization an now that Al is transforming everyth deployment.

Good experimentation works like development teams. It gives teams sp: existing limitations become major f dedicated spaces away from producti hackathons, or exploration sprints wl delivery pressure. The goal isn't rar investigation of technologies that mig For teams who want (or need core work, set up some basic guards productive. Define clear boundaries, t from the start. Don’t compromise on ¢ during experiments. Always docum experiment that teaches you somethir Large language models and AI toc why experimentation matters right actually make developers more produ improve your quality processes? Hox

code review time and quality? Which AI coding workflows actually reduce developer toil versus creating new types of friction? Will low-code platforms create maintenance headaches down the road?

You won't know without trying them in your environment and measuring their real impact on developer experience.

The tiered framework we discussed earlier gives experimental technologies a clear path to becoming standards. When an approach proves its value, your governance committee can move it up through the tiers, gradually increasing support as confidence grows.

Your scope of control matters organization-wide reach can cond experiments, while teams with nar: targeted experiments that solve spec compatible with standards. (We disc 6.) Match your experimentation amb authority to create a healthy, evolving

Technical debt is doubly relevant t identify which existing pain points to should build new solutions to avoid cr We can use technical debt to Chapter 53 improvement efforts. When a deve necessary due to technical debt, estin Deal with Technical Debt and multiply it by how frequent] . “re . bl d their fully loaded t in DevEX Initiatives probrem anc Theil uly foaded cos concrete business case for improvem turning what feels like cleanup work is investment.

Every technology decision comes with trade-offs, and sometimes the fastest path forward today creates extra work tomorrow. . .

Making the business case for technic Paying down technical debt requ Since debt reduction often appea WARD CUNNINGHAM COINED the term “technical debt” to explain (© the accumulated burden from shortcuts or incorrect decisions made when creating technology. Martin Fowler explains it with features, you need a strong busines: an example we're all probably familiar with: “Imagine I have a Measure technical debt’s imp confusing module structure in my code base. I need to add a new COStES feature. If the module structure was clear, then it would take me Track time spent on Ww four days to add the feature but with this cruft [poorly designed interventions. If 100 develor or overly complicated code], it takes me six days. The two day daily on deployment work: difference is the interest on the debt.”3¢ hours lost annually.

In the developer experience context, technical debt manifests in Measure error rates and recc multiple forms: Friction in everyday workflows, increased difficulty like pipeline failures, enviror updating codebases due to complexity or poor documentation, deployment rollbacks.

outdated tooling that requires workarounds just to function, and Survey developer satisfactic higher cognitive load from inconsistent environments and poorly points to identify hidden cost supported homegrown solutions.

Prioritize debt reduction. Focus on debt with the highest return: Developer impact multiplier. Target issues affecting the most developers most frequently.

risk. Address debt operational or security concerns.

Business creating significant Enablement potential. Prioritize improvements that will unlock new capabilities.

Demonstrate ROI. Frame debt reduction in business terms: Calculate productivity savings. 200 developers x 10 minutes saved x $75/hour x 230 working days = $575,000 annual productivity recapture.

Highlight risk reduction. Quantify how addressing debt reduces outages or security vulnerabilities.

Show enablement value. Estimate the business impact of faster deployments or improved quality.

Track and communicate before-and-after metrics to build momentum for future efforts.

By connecting DevEx improvements directly to business outcomes such as productivity, quality, and speed, you show that paying down technical debt isn’t just good engineering— it’s sound business strategy.

Use technical debt principles in your own DevEx tools. While some debt is inevitable, Fowler’s Technical Debt Quadrant helps us distinguish between types of debt that vary in their strategic value and risk, differentiating between prudent vs reckless risk, and deliberate vs. inadvertent debt.2s NCE “We don't have time for design”

## DELIBERATE

“What's Layering?” The most dangerous half for de —solutions rushed into production term implications or understanding creates a compounding maintenance productivity throughout your organiz In contrast, prudent-deliberate d choice. You might intentionally lau limited features to get early feedb: refactor certain components later. S: debt often emerges when building n better approaches during the buildi for DevEx teams tackling unsolved p haven't yet emerged. Rapidly evolving of this.

The critical difference is awareness—either making conscious decisions about trade-offs upfront or explicitly acknowledging them once discovered, then planning for improvements.

What makes technical debt especially significant in DevEx initiatives is its multiplicative impact. A slightly clunky deployment process might seem minor, but when hundreds of developers use it daily, small frictions compound into substantial productivity losses.

This means DevEx technical debt often carries a higher “interest rate” than product code debt—but : deliver outsized returns.

This compounding nature makes i and address technical debt as part of remember: Dwelling on how your deb brief retrospective to understand past your energy on strategic improvemen

Chapter 54 Bring It All Together: The Sustainable Technology Mindset Ultimately, your long-term success depends on adopting a sustainable technology mindset.

(© THROUGHOUT THIS PART, we've explored three interconnected approaches to making your developer experience sustainable: By adopting a product mindset, you create solutions that deliver genuine value by center: Through balanced standardizat while preserving space for inno And by actively managing tech frictions from compounding in These three strategies reinforce o identifies which standardization ef value, while governance processes undermining both standardization an As technology evolves—parti development tools—these principles By building sustainable practices nc experience that adapts to changin delivering efficiency, reliability, and se In the next chapter, we'll extend data and metrics initiatives.

## THE FOURTH PRACTICE

Design Metrics That Evolve and Amplify Impact CREATING A DASHBOARD isn’t enough. Your data has to solve a problem for your stakeholders. Think of your metrics as a product.

Like any product, they don’t need to | should serve their users and get bette: Internal metrics are different fro but treating them like a product help Solving real problems, delivering valu product-based approach elevates thet Step 3 into something more strategic : While an entire book could be wri on four essential pillars: Designing i ensuring quality and reliability, and : this will sound familiar from previo topics together shows how they worl metrics—and ultimately, your DevEX :

Chapter 55 Design Metrics for Your Stakeholders For metrics to be useful, start with the basics: Why you need them and who they're for.

FIRST UP—AND THIS is crucial—identify your customers and what they need. Yes, they're internal users, but think of them as customers. This mindset matters because it’s easy to lose sight of the core problems you're trying to solve with metrics. Sometimes you're drowning in data, other times you're starving for it.

We touched on this in Step 5 when we discussed strategy, but it’s worth repeating here: Write down who your stakeholders are.

When viewed through a product lens, your stakeholders may also be customers—for example, leadership may use data from aggregated dashboards to drive decisions, development teams may use detailed data to diagnose problems, and HR may use reports to inform hiring and training decisions. Writing down the groups who will be metrics customers helps you get feedback from your team and keeps you anchored as your initiative grows.

Don’t just guess what your customers need—do your homework!

You've probably already gathered friction points, but expand your r insights each group needs. For examp] For developers: Dig into specif pain points. What data wo efficiently?

For engineering managers: Exp them identify bottlenecks and § For leaders: Focus on their strat worried about costs, investm velocity?

These conversations often reveal s you might find leaders care more abot pure speed, or that managers need be dependencies. With these problems ir for each customer. For example: Leaders. They're often loo.

productivity, business value investment.

Engineering managers. They we and get actionable insights fron Developers. They want to be friction, have more time to fact: Our research shows that correlated with happiness.) Keep these goals high-level—they’ iterations. Check in with leadership (

© [&] and other stakeholders (they're the ones making improvements happen) to make sure everyone’s still aligned.

Remember: You're a customer too.

Here’s something people often miss: Your DevEx team is a key customer too! While mapping out stakeholders, add yourself to that list. You'll use these metrics regularly to: Guide where to focus your improvement efforts.

Justify investments in better instrumentation.

Make resourcing decisions.

Track the impact of your work.

Show the value of your DevEx initiatives.

In fact, you might be your own most active metrics user.

After all, you can’t improve what you can’t measure.

Before diving into solutions, review what you've learned. Take all the problems you've collected and group them into key themes.

Make sure every stakeholder’s needs are represented, and pay attention to where different groups have overlapping problems— these are often your biggest opportunities.

You should also scan the landscape. Look at what metrics and tools already exist, both inside and outside your organization. You might find that other teams have already solved similar problems, or that there are industry tools you can leverage. There’s no need to reinvent the wheel if good solutions al All of your goals should have su need to be measurable and tied dire mark the end of a project or phase, Sometimes you'll want exit criteria “mission accomplished” checkpoints.

real example about local build times: + High level goal: Reduce develop + Success criteria: Improve local months.

+ Supporting metric: Local build 1 Exit criteria: 90% of devs havel Each team measures their build tis against their baseline. Once you hit y focus elsewhere (unless things change Finally, make sure your met questions. If you want to improve | questions you want to answer. For ex: review process takes the most time: review process has the most delay?” that your customers can ask—they review, but they also require slightly d questions help your customers (reme they need.

Chapter 56 Use Metrics to Solve Your Stakeholders’ Problems Avoid a one-size-fits-all approach when designing dashboards.

YOUR SOLUTIONS WILL take different shapes for different audiences. The same data often needs different presentations for (© different users.

Leaders typically want high-level patterns that help with strategic decisions and resource allocation. For example, an engineering VP might spot increasing lead times across teams and task engineering managers with improving them.

Engineering managers and developers need more detail to drive action. When that VP asks about lead times, managers and their teams will dig into specific components —build times, integration tests, release processes—to find bottlenecks and plan improvements.

Design metrics that serve your stakeholders.

At LinkedIn, Max Kanat-Alexander experience dashboards that could stakeholders.

For engineering teams, the d level metrics that helped them ide improvements in their own workfl specific pain points and measure pr made.

For leadership stakeholders, the displayed to tell a different story— of developer experience investme: trends across teams and make infor to focus improvement efforts.

Their key insight: The same met audiences when presented in way problems and decision-making wanted actionable details about the needed strategic visibility into orga: But don’t limit yourself to dashboa include: Regular reports that highlight t Workshops to help teams under Training sessions on using met: Runbooks for common improve Templates for improvement pla

Watch how teams use your solutions and be ready to adapt.

Here's a real-world example: Say you notice teams struggling to use your dashboards effectively. Instead of just tweaking the Ul, dig deeper. Talk to the teams—maybe they understand the data but aren't sure how to act on it. That’s a different problem! You could test solutions such as creating improvement plan templates or starting a Community of Practice where teams share successful approaches.

network and developers at your c experiences like?” In these cases, det: interested in a general understand and what is possible. You probably ¢ Chapter 57 documenting and validating your a tool if others ask for comparisons or Fast Is Re lative to advocating for can’t be done.

Your Competition Benchmarking against industry stan While internal metrics provide criti improvements, external benchmar It's not enough to look inward to find the true markers of DevEx success .

that can inform your strategy and —you also need to look outward. : your developer experience comps helps you set appropriate targets ar may be significantly ahead or behis START CREATING A list of steps that developers take to do their work (© at competitor (or reference) companies. In this context, competitors benchmarks for peer and aspiration Where to find benchmarks.

DORA reports and State of De Stack Overflow and GitHub d Technology-specific reports f are organizations of a similar size, working under similar constraints (e.g., highly regulated industries, or an even narrower focus, such as finance), and similar technical characteristics (e.g., tech stack, amount of tech debt/legacy code, etc.).

In some cases, you may create lists for two competitors: One for direct comparisons (that is, those who are in the same industry and Developer experience comm whose DevEx is probably similar to or slightly better than yours), .

os . . Best practices.

and another for aspirational comparisons (those whose DevEx is c . Co ompare against organizatic much better than yours). These benchmarks will be particularly P 8 € i stack, and industry.

valuable when making your business case to stakeholders, which we .

. . Focus on 3-5 key metrics 1 discuss in Step 5. ; co . . cr . everything.

How can you get this information, since it’s outside of your .

Lo. j . Use benchmarks as guidance, organization and probably unpublished? Start by asking your ] Present external data with ap

When setting goals, consider both industry leaders and your starting point. If elite performers deploy multiple times daily but your industry typically deploys weekly, an intermediate goal of twice-weekly deployments might be more appropriate than immediately targeting daily deployments.

Present benchmarks with appropriate context. When sharing industry benchmarks with stakeholders, always include relevant context about the benchmark source, comparable organizations, and any methodological differences that might affect comparisons. And remember: Your organization’s unique context matters more than industry averages when determining what “good” looks like for your DevEx initiatives.

Remember: Your own trajectory matters most. While benchmarks can be interesting and useful for context, what's (© most important is your own progress. Are you getting better or worse? Focusing on your improvement trend—especially when starting out—provides more actionable insights and maintains team momentum better than chasing absolute numbers from industry.

With a clear picture of the friction points in your development process and the data to back up your findings, you're ready to build a measurement system that drives real improvement. In the next chapter, we'll explore how to choose the right metrics, ensure they're reliable and actionable, and adapt them as your needs evolve —starting simple and scaling smartly.

[&] Chapter 58 Start Simple and Scale Smartly Getting started with metrics doesn't have to be complicated.

START WITH METRICS that are easy to collect and provide clear value—things like developer satisfaction, PR cycle time, build success rates, or deployment frequency. These are common starting points because they're typically easy to instrument and map to problems developers face daily. Like the change management tools in the last chapter, your metrics must evolve to support ongoing improvement.

When you're just starting out, you'll likely offer both products (such as dashboards and tools) and services (like team enablement or training). That’s totally fine! Services can help you better understand team needs and identify which metrics matter most.

Just keep this split in mind as you design your metrics—some will help you deliver better services, while others will make your products more valuable.

Focus on problems, not data. When planning metrics, start with your problems, not the data you want to collect. Starting with this helps you avoid the common trap of building dashboards just because you can. Every metric should solve a specific challenge your team—and your customers—face.

Balance is key when choosing y data (such as PR stats) with hum surveys). Consider both team and remember that speed isn't everythi need different types of metrics to get t Watch out for metrics that can be consequences. Here’s a classic exan quickly developers respond to pull r their focused coding time to maintain a natural response to what you're sign The fix? Use balanced metrics th this case, also track time spent on fc becomes especially important with Al you might want to track both code review quality to ensure Al tools aren’ Using SPACE to balance your metrics One powerful way to ensure balan which we introduced in Chapter holistically about metrics across fivi Satisfaction: A developer’s process.

Performance: An outcome of Activity: The count of action Communication and colla systems talk to one another.

Efficiency and flow: Doing w interruptions.

You don’t need metrics from every dimension—three or four The goal is to be intentional but pr is typically enough. But considering all five helps you think metrics that give you the most bang | broadly and can unlock new ideas when you're stuck. Let's see there.

how SPACE could apply to code review: - 8: Developer satisfaction with the pull request process.

- P:Code review velocity and quality. Pro tip: Use this evaluation to smart your instrumentation efforts.

A: PRs per dev, reviews per PR.

If most of your development lifecyc C: PR discussions, merge time.

« E: Time PRs spend waiting for review. WELLS JEEVES (TE UD WROD GUE developer surveys (see Step 3 wor they serve double duty by: Evaluate your (prospective) metrics. First, look at the cost- + Guiding improvements. If st benefit tradeoff. Can you actually measure this thing without is your biggest productivity | spending a ton of time or money? Some metrics sound great in focus.

theory but are impractical to collect. For example, getting detailed - Prioritizing instrumentatic (© data about a developer's inner loop (local development) is typically local build as a priority, you ¢ hard and expensive, while PR data is usually readily available to collect objective data about through existing tools.

Next, assess where your data lives and how to get it. Some data might be sitting in your version-control system, ready to use. Other Eourcustomer SEW OTLEY data might require new tooling or surveys. For instance, while PR ies ley de metrics are usually just an API call away, understanding developer people discuss accuracy versus precisi . . . does this mean for DevEx metrics?

satisfaction often means running regular surveys.

Finally, make sure any metric you choose drives action. A metric Think of it like archery: Accuracy that doesn’t help you make decisions is just noise. Ask yourself: precision is hitting the same spot con: “If this number changes, will we know what to do about it?” The same applies to DevEx data. Yc For example, if AI tool usage increases but developer satisfaction build time measurements down to t decreases, you should have a clear plan for investigating whether the consistently off by 30-90 seconds, t1 tools need better training, different configuration, or different use side, you might have accurate measur cases.

[&] bit—say, only recorded to the nearest second—but they average out to the true build time.

Precision also reflects how detailed your data is. Say developers flag “slow builds” as a major pain point, but your instrumentation only gives you coarse time buckets like “under 1 minute” or “over 30 minutes.” That's accurate but low precision—you’ve identified a real issue and can start making improvements, but you won't be able to make detailed comparisons.

Here's the nuance: Consistently inaccurate data can still reveal valuable patterns over time—as long as the error is stable, you can often track relative changes and trends. But if the data is randomly inaccurate, it’s hard to trust or act on. Understanding these tradeoffs helps you decide when your data is “good enough”—and when it’s not.

Documentation isn’t exciting, but it’s crucial. Record how each metric is calculated, where the data comes from, and what assumptions you're making.

For example, do your PR cycle time calculations include weekends? What about time zones? These details matter when people start using your metrics to make decisions, and especially when comparing against any existing metrics or reports.

You'll probably find examples where different teams call differently calculated metrics by the same name, and others where they use different names to refer to the same metric calculation.

Keep your documentation where people can easily find it, and update it when things change.

Set up basic validation processes to catch obvious problems.

Start with simple automated checks that flag suspicious patterns.

«+ Identify reasonable bounds for your metrics. For example, PR completion times should never shouldn't jump from 2 minu investigation.

Look for unexpected gaps or sp you usually get 100 data points 10, something’s probably wron; Compare metrics across simile A’s build times are consistentl team’s, either there's a real pr measurement might be off.

You'll also want to create a regular: monthly or quarterly depending ont During these reviews: Sample a few metrics and tracet Verify that your automated che issues.

Look for any new edge cases yot When you find problems (and yo them. Document what went wrong, you're doing to fix it. Nothing kills hiding data quality issues.

Invest time in building trust wi just about data quality—it’s about ho metrics over time. Start by involvin, making sure everyone understands nc but why it matters to their goals.

Be transparent about how metric: and don’t hide problems when they ¢

tell the whole story, so provide context and combine quantitative data with qualitative feedback from teams.

Watch out for potential gaming of metrics—if teams feel pressured to hit certain numbers, they’ll find ways to do it that might not actually improve anything. Start small, gather feedback, and adjust your approach based on what you learn.

Most important, make sure teams know what actions they can take when metrics show problems.

The goal isn't perfection—it’s reliability you can trust for decision-making. Sometimes good er better than perfect data that takes for you understand and document the lin approach so others can make informe These principles—starting simple quality—form the foundation of effec there’s one more dimension to consic workflows in ways that require new m tackle that in the next chapter.

[&] Chapter 59 How Al Changes (and Doesn't Change) the Metrics You Need Al changes what developers do every day, so your metrics need to change too.

THE GOOD NEWS? The measurement fundamentals you just learned still apply. As Al tools become woven into daily development work, you're probably wondering: “Do I need to throw out everything I know about measuring developer experience?” The short answer is no—but the longer answer is more interesting.

The fundamentals still matter. The SPACE framework and DORA metrics remain relevant because developers still need fast builds, reliable deployments, good documentation, and strong collaboration—and Al often amplifies the pain of bad foundations rather than masking them. Flow and friction haven't gone anywhere: Developers still need focus, and slow pipelines, flaky tests, and unclear ownership still break it. And while AI shifts what developers do, it doesn’t change their need for clarity, autonomy, mastery, and purpose.

Applying SPACE to Al-Augmented D In Chapter 58, we introduced the SI balance your metrics across five di remains just as valuable when workflows—you just need to ask sli; Satisfaction: How do develo the tools improve or frustrate they satisfied with the qualit; Performance: Are outcon assistance? Track defect rate: and time-to-resolution for in Activity: What are the Al suggestion acceptance rates delegated to Al, and where Al debugging).

Communication: How does .

code reviews shifting from developers asking Al instead improving or declining?

Efficiency: Where does Al overhead? Measure workflo routine tasks, and frictio: validation effort.

Consider adding a sixth dime do developers trust Al-generate recommendations? This affects bot!

value teams ultimately derive from

AI doesn’t just speed up existing work—it changes workflows. Most importantly, collect th Developers aren't just writing code; they're reviewing, prompting, instrumentation typically involves r and steering AI. And here’s what most people miss: Most Al usage methods. Aggregate at the team involves reasoning about information rather than generating it. individuals, be transparent about wh Developers spend more time using Al to write summaries, compare and work with HR and legal partners ¢ alternatives, conduct smart searches, and synthesize research than boundaries. The goal is to improve de generating code. This means existing metrics that capture time surveillance.

spent coding or lines of code written miss the bulk of Al-augmented Your metrics product also needs work—the time spent crafting prompts, reviewing suggestions, and views that compare Al and non-Al making decisions based on Al synthesis. loops that reveal where AI adds the New metrics can help answer new, emerging questions. Track visualizations that track how Al affect prompting efficiency—how many attempts developers need before getting a useful AI suggestion. Measure validation effort—the time Use Al to build your Al metrics There's a helpful irony here: While to measure, it can also help you spent reviewing and correcting Al-generated code, which reveals whether AI truly saves time or just shifts where developers spend (© it. And monitor trust calibration—when developers trust Al too much (shipping bugs) versus too little (wasting time double- a checking correct code). These metrics reveal friction that traditional ee measures like commit frequency or lines changed simply can’t > Goniodlis ges hs ceded capture. + Create dashboard prototypes Al usage telemetry can reveal important patterns and changes > hoe saat i soll eo in workflows. Capture what types of work developers do themselves ates versus what they hand off to AI agents—this shows where Al > Build cit susan | is valuable and may reveal new system blockers. Deep insights levelling es also come from watching how AI reshapes team dynamics: Are i A What once required weeks of engineers asking Al instead of peers for help? Are code reviews Ri oo. Lo. i i A now be scaffolded in hours. Just shifting from syntax nitpicks to architecture discussions? Are new .

i generated code carefully—especiall developers getting up to speed faster because Al explains your . .

| feeds critical decisions. And lever internal codebase?

and boilerplate, while keeping human expertise focused on the measurement strategy and interpretation.

Mixed methods become even more important with Al Logs tell you what AI suggested and what got accepted, but only surveys and interviews tell you why. Your telemetry might show developers rejecting 80% of Al suggestions for authentication code —but you need to talk to developers to learn whether that’s because AT hallucinates security vulnerabilities, doesn’t understand your internal frameworks, or because developers don't trust it for security-critical work. The “what” reveals patterns; the “why” reveals the root cause and tells you what to fix.

The shift from output to outcomes becomes critical. AI makes it painfully obvious that lines of code was always a bad metric —but more importantly, it forces us to connect our metrics to what actually matters. Developer productivity isn’t the goal; faster customer value delivery is. That means measuring problem-solving speed (time from idea to working solution), breadth of exploration (how many approaches developers can test), and cognitive load (whether AI helps or overwhelms). These outcome-focused metrics tell you what actually moves the needle on business value, not just code volume.

Behind the scenes, your infrastructure needs to evolve—and not just for developer workflows. Traditional telemetry doesn’t capture Al interaction loops, so you need new instrumentation for prompting workflows, completions, and accept/reject events. These real-time metrics reveal patterns and friction that retrospective analysis can miss.

But don’t stop there—instrum Tracking what agents do reveals wk automation and which require hun how delegation to agents affects d the system: Does offloading routine t architecturally, or does it create b understanding of how things work?

Start by auditing your existing Ask: “Does this metric still capture wh important tasks, workflows, and fe miss?” Don’t throw everything out an —add data that fills important gaps questions.

Your metrics strategy should stakeholders will ask about AI adop the most value?” “Are we seeing qual are benefiting most?” Your metrics s operational velocity questions. Havir confidence in your Al implementatior make better decisions about where an The bottom line: AI changes whiz you measure it. You're still trying developer experience—the SPACE frar in the callout above. The fundamental new instruments to capture the new r

they provide. Without clear ownershi break without anyone noticing. Your Keep an eye on data quality and Check that metrics still align wi Chapter 60 + Handle questions and concerns Plan and prioritize improvemer Maintain Your Metrics . This doesn’t mean one person ds Li ke Any Prod uct needs to be responsible for the health of them as the product manager for yc Listen to your users and evolve.

remember? That means getting feed Your metrics system needs ongoing care and maintenance.

leaders, managers, and developers we!

TRACK VERSIONS AND changes religiously. Keep a changelog it to improve. Some ways to do this inc of what changed and why. When you update how a metric is + Regular check-ins with teams u (© calculated, document it. Your future self (and everyone else) will + Surveys about metric usefulnes thank you. + Watching which metrics actual For example, if you change how you measure PR review time to ones nobody uses.

exclude weekends, that’s a big deal—write it down! (Or better yet, + Looking for gaps where teams n create a new metric and give it a meaningful name so it’s easy to understand.) This helps teams understand why their numbers Sometimes you'll find metrics th: , : might look different and maintains trust in your metrics. but aren't actually helping anyone m: . a . : : ! : Think about versioning like this: Small tweaks get a minor them! Better to have fewer, more valu version bump (v1.1 to v1.2), while bigger changes that might affect full of numbers nobody uses.

historical comparisons get a major version update (v1.0 to v2.0).

This makes it easier to track changes over time and understand Measuring Linkedin’s metrics produ when metrics might not be directly comparable. Remember Max Kanat-Alexander’s Make ownership crystal clear. Someone needs to own these . — earlier example? Beyond designin metrics—both the technical implementation and the business value TE smell, tha Ak |

© product was actually working. Leadership frequently asked how they measured the success of their developer experience dashboards.

After trying different approaches, two metrics proved most valuable: Repeat engaged users. This included users who interact with a dashboard one day and return to interact again later.

If they come back, they got value from it. For this measure, the team required actual interaction—not just having the dashboard open in a tab.

Percentage of engaged teams. Since their dashboards showed team-level metrics, they tracked how many teams had at least one member actually click on their own team’s dashboard out of all possible teams—essentially their “market penetration.” These approaches helped them identify which metrics were truly valuable versus just dashboard noise.

Stay ahead of platform changes. Your development environment keeps changing—new tools, updated platforms, different processes. Your metrics need to keep up. Keep an eye on: New data sources becoming available (e.g., maybe that shiny new CI system has better build metrics).

Changes in how teams work (e.g. if everyone switches to trunk-based development, your PR metrics might need updates).

Tools being deprecated (e.g., got system goes away?).

This is where good relationships w pay off. They can give you a heads up the pipe, so you're not scrambling to t minute.

Remember to sunset. Not every When a metric stops being useful, re the problem it was tracking, or team challenges. In addition, having too nr having too few—it makes it harder for matters.

Before removing a metric, check if: Anyone is still using it for decisi It’s part of any regular reports o You need to keep historice comparison.

There’s a newer metric that bett The bottom line? Your DevEx met it thing. They need regular attention But with clear ownership, good feed] to evolve, they'll keep helping teams developer experience.

Final Thoughts IMPROVING DEVEX IS one of the most effective ways you can deliver greater value faster and more accurately than ever before. But to deliver that value, you need to get started—right now.

Y Filter Default levels v 208 Issues: F207 M1 53,537 hidden + Organizations with great DevEx can adapt faster to market > window. innerWidth - 100, clientY: 5.

window. innerHeight / 2, bubbles: true, nd cancelable: true bi; 08!

document.elementFromPoint (w i indow.innerWidth - 100, Jada Chapter 61 window. innerHeight / 2)?.dispatchEvent(clickEven ape 0s What Are You Waiting For? iy oft } niz for (let i = startPage; i 1m <= endPage; i++) { console. log( Requesting ad: You now have everything you need to transform your developer screenshot for page . . ${it..."); 1€] experience—and your business results. try { =~ const res = await ain fetch(“http://localhost:300 THROUGHOUT THIS BOOK, we've shown you that developer 1/ screenshot?page=${1} ); 18 experience isn’t just about making developers happy. It's about res-json()i tog(-P an systematically removing the friction that slows down your entire ${i} captured:", data); nil oe os . . . } catch (err) { : organizations ability to deliver value. Whether you're dealing with console.error( Failed ca Al tools that promise speed but create new bottlenecks, legacy oo sapture page ${i}:", oir systems that drain productivity, or growing technical debt that ) break; 1ap threatens your competitive position, the framework and tools in ces rat if (i < endPage) { the this book give you a clear path forward.

B LL. . console. log("Advancing to : be Improving DevEx has a multiplier effect. When you improve next page..."); i i . i turnPage(); developer experience, youre not just making one team more // Halt 3 seconds for ep . . Lo th t iti ; productive. You're creating a multiplier effect that compounds over © page rialody ron act time: Promise(resolve => Jer me: setTimeout (resolve, 3000)); h «Developers who work in low-friction environments attract y €.

other talented developers. Co ast console. log("Finished + Teams that ship reliably become the model for other teams to capt ring pages!"); follow. "oo Ww < » Promise {<pending>} nt.

[&] Acknowledgments A HUGE THANKS to the readers who really went above and beyond with detailed feedback that shaped this book in meaningful ways: C. Rich Wilson, Justin Reock, Keith Mann, Laura Tacho, Lita Cho, Max Kanat-Alexander, Mikhail Panchenko, Murali Suriar, and Rojin Vishkaie. You made this a much stronger book.

We are also grateful to our early readers and the many people who generously shared their time and insights through interviews and conversations. Your feedback, questions, and perspectives helped us refine our ideas and find clarity in complex topics. Thank you to: Alex Rasmussen, Alyss Noland, Andrew Cornwall, Andrew Flick, Ben Linsay, Brian Houck, C. Rich Wilson, Camille Fournier, Carmen Badea, Charles Sellers, Chris McEnery, Christian Bird, Greg Poirier, Ian Eslick, Jason Entenmann, Jeff Hodges, Jez Humble, Jordan West, Justin Reock, Keith Mann, Kelly Shortridge, Laura Tacho, Leif Walsh, Lita Cho, Margaret Price, Martin Fowler, Marty Cagan, Max Kanat-Alexander, Mikhail Panchenko, Murali Suriar, Nathen Harvey, Rob DeLine, Rojin Vishkae, Ronjin, Rose Nyte, Sam Pan, Sarah Drasner, Scott Andreas, Sean Gillespie, Sourabh Shirhatti, Tara Hernandez, Tom Hipwell, Trevor Eber], Xavier Velasquez, Zac Duncan and our anonymous readers Different Opposum, Different Seal, Impressive Goshawk, Supportive Upbeat Kookabura.

Nicole Forsgren To my co-author Abi Noda—than collaborator and for never being afrai just in case it made the book better (it and willingness to rethink everything To the wonderful people I've beer continue to learn from—thank you f showing me new ways to approach ole A heartfelt thank you to all the opened their doors and jumped on Zt —both the struggles and the succe vulnerable about what didn’t work, & did, truly shaped and informed this bc To the DevOps and DevEx commt conversations, insights, and shared e my thinking.

To all of our readers—thank you f us, for catching my silly mistakes, a I completely missed. I'm grateful to learning.

To Peter Economy, my editor—tha for helping shape this book into some made this book better, and I apologize that I'm sure will drive you crazy.

To my family—thank you for always being in my corner and supporting me in all the directions my career has taken me.

To Rachel Potvin, Ece Kamar, and Chris White—thank you for being incredible leaders and colleagues. I learned so much from you about leading teams, working through rapid technology changes, and strategy. Your influence shows up throughout this work.

To my brilliant colleagues Brian Houck, Eirini Kalliamvakou, and the SAINTES team—Carmen Badea, Christian Bird, Rob DeLine, Denae Ford Robinson, and Tom Zimmermann. I learned so much working with all of you.

To The Backchannel—y’all are the best. Thank you for all the great questions, new papers, and bananapants content that keeps me informed and entertained. You're so generous with your time and expertise, always providing answers and clarity when I need it.

Thank you for being an invaluable resource, sounding board, and most importantly, friends. You know who you are.

Special thanks to my dad, who always told me I just need to spin problems to look at them another way. That advice has been pretty handy in tech, where there’s always another angle to try—especially now with Al turning everything upside down. Sorry you missed the ride.

To Chris Cohen, my partner through late nights and working “vacations.” [Editorial note: He says I fail at vacations; he’s not wrong.] Thank you for your patience, encouragement, and for (rarely) complaining about all the typing interrupting things.

Thanks especially for the epic charcuterie boards, great drinks, and all the laughs.

And finally, to Diet Coke: This book would not have been possible without you. Some partnerships are just meant to be.

Abi Noda To Nicole Forsgren—thank you for bei: the opportunity to co-author this boc mad scientist, and your leadership an constantly inspired me.

To Laura Tacho and Justin Reocl passion, and deep expertise you bri productivity. Your thoughtful feedb shaping this book were invaluable.

To Margaret-Anne Storey and Mic jumping in headfirst on this journe experience” was even a thing. I've le: from the research we've pursued toget To Brian Houck and Max Kanat-Al spirits on the elusive quest to c Thank you for the countless conve importantly, encouragement.

To Azra Coburn, Gilad Turbahn, / thank you for being incredible custo: boards. It’s been a privilege to lea collaborate along the way.

To Isaac Noda and Iana Noda—tt curious about my projects, and for t needed laughs when I got too deep int To my dad—you always pushed writer, especially on the topic of deve were here to critique this book, but I ki