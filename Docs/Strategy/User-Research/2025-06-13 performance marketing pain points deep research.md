# Performance Marketer Pain Points - Deep Research Findings

**Research Date:** June 13, 2025  
**Scope:** In-house performance marketers, US market, >$50k/month ad spend  
**Focus:** Google Ads and Meta Ads, complex funnels (SaaS, lead-gen, multi-step conversions)  
**Purpose:** Source material for Elly 3.0 automation opportunities - automating 90% of performance marketing work

---

## Pain Points & Automation Opportunities for In‑House Performance Marketers (>$50k/mo Ad Spend)

### Data & Attribution Challenges in Complex Funnels

#### SaaS Conversion Tracking & LTV
Standard analytics fall short for software/SaaS funnels. Most out-of-the-box conversion tools only log the initial signup or sale, missing downstream metrics like churn, upgrades, or lifetime value. Marketers end up optimizing to surface metrics (leads, clicks) instead of true ROI.

**Context:** B2B/B2C SaaS companies with recurring revenue (long customer lifecycles); in-house teams under pressure to prove revenue impact beyond the first purchase.

**Pain Point:** Inability to connect ad spend to real customer value. For example, a SaaS marketer noted that typical tracking "falls flat" for SaaS because it doesn't account for subscription cancellations or expansions. This means ROAS calculations are often wrong, leading to misallocated budget (e.g. overvaluing cheap leads that don't stick around).

**Time Impact:** High – Teams spend extra hours exporting data from payment platforms or CRMs to manually calculate metrics like CAC vs. LTV. Without automation, this is an ongoing, repetitive analysis each reporting cycle.

**Frustration Level:** Severe – Marketers are dissatisfied that they're "optimizing for vanity metrics" instead of what matters. Confidence in reported ROAS is low when internal finance data doesn't match ad platform conversions.

**Current Solutions:** Many build custom integrations. For instance, one SaaS team built an internal system syncing Google Ads with Stripe revenue via Segment and Google's Conversion API. This closed the loop on LTV, letting them optimize bids for high-LTV users (e.g. prioritizing leads with company email domains) rather than just volume. Others resort to offline conversion imports or third-party analytics to attribute revenue back to ads.

**Quote/Anecdote:** "Most conversion tracking tools…fall flat when it comes to SaaS. They only track the initial sale…leaving you optimizing for clicks and conversions instead of what really matters: LTV and ROI."

#### Long Sales Cycle Attribution Gaps
Conversions that occur months later often aren't captured. Google Ads has a 90-day conversion window, which is too short for industries like enterprise software or high-ticket B2B services. One PPC specialist noted for enterprise SaaS deals, the sales cycle "90% of the time [is] longer than 90 days," so attribution becomes impossible in Google's default setup.

**Context:** In-house marketers for enterprise/B2B products; $50k+ monthly spend generating leads that might close 4–12 months later (e.g. via sales team).

**Pain Point:** Lost credit for late conversions – Ads that ultimately drive revenue past the 3-month mark aren't counted in-platform. Marketers must rely on trust or manual tracking to know if those early leads eventually became customers. This makes it hard to optimize or justify ad spend, especially to finance teams.

**Time Impact:** Moderate – Teams often export lead data and later reconcile it with CRM opportunities and deals, a manual process that can take hours per month.

**Frustration Level:** High – Described as a "big annoyance" because marketers feel blind beyond 90 days, undermining confidence in reported ROI.

**Current Solutions:** Stop-gaps include extending attribution via CRMs (tracking lead creation to sale date) and offline conversion uploads for closed deals (if systems are set up to pass GCLIDs). Some teams use predictive LTV modeling to estimate long-term value within the ad platforms. Otherwise, they must wait and manually upload conversions once deals close, or use third-party attribution tools that allow longer look-back windows.

**Quote/Anecdote:** "If a client is selling enterprise solutions, the purchase time from the click is often longer than 90 days. [It] sort of makes attribution impossible…putting you in a position where you have to place enormous trust in the client."

#### Offline & Multi-Step Conversions (Leads to Sales)
Tracking offline outcomes of online leads is notoriously tricky. In funnels with form fills, phone calls, or multi-step sign-ups, the initial conversion online is just a starting point – the real goal (sale or revenue) happens later, often offline. Marketers struggle to tie ad clicks to these final outcomes.

**Context:** Lead-generation campaigns in industries like home services, healthcare, financial products, education enrollments, etc., as well as on-delivery payment ecommerce models.

**Pain Point:** Conversion data mismatch – Ad platforms might count a lead form or click-to-call as a "conversion," yet the marketing team needs to know if that lead actually resulted in revenue. This gap leads to overestimating ROAS in platform dashboards.

**Time Impact:** High – Marketers spend significant time manually reconciling leads with sales. This involves exporting leads from ad platforms, matching them to CRM or point-of-sale records, and calculating true conversion rates and ROAS.

**Frustration Level:** Severe – There's both data anxiety (never being sure if the ads are actually profitable) and annoyance at "wasted" conversions. Low-quality leads "waste your team's time and resources" and frustrate stakeholders expecting better lead-to-sale ratios.

**Current Solutions:** Offline Conversion Tracking (OCT) is the ideal, but not easy: it requires capturing lead info (or a click ID) and later uploading actual outcomes. Many teams use call tracking software (e.g. CallRail, WhatConverts) to tie phone calls to campaigns.

**Quote/Anecdote:** "We set up local ad campaigns… Now our 'conversions' look high on the digital end, but revenue doesn't reflect that because many people never actually came in and purchased. Aside from asking every customer how they found us…how the hell do you track CAC?"

---

### Repetitive Tasks and Time-Consuming Workflows

#### Manual Offline Conversion Uploads
Uploading offline conversion data is labor-intensive without automation. One in-house specialist shared that they upload 15–25 offline conversions to Google Ads every single day, calling it "a major hassle" and wishing they could do it weekly. They estimated automating this would save "a couple hours a day".

**Context:** Mid-sized company with a custom CRM (no out-of-the-box integration to Google Ads). Likely a lead-gen business with dozens of daily lead updates that need to be fed back into the ad platform.

**Pain Point:** Daily data janitorial work – pulling conversion data from internal systems and formatting/importing it into Google Ads. It's tedious and prone to error.

**Time Impact:** Very High – ~2 hours per day (10+ hours per week) can be consumed just preparing and uploading offline conversion files.

**Frustration Level:** Severe – This repetitive task is seen as a drag on productivity. The user was adamant that while they'd "love to do it weekly" to save time, they fear even a 1% performance drop if data isn't updated daily.

**Current Solutions:** Partial automations are used, though often brittle. Some teams set up Zapier or scripts to push conversions from a Google Sheet into Google Ads on a schedule.

**Quote/Anecdote:** "Currently uploading 15 to 25 offline conversions to Google Ads each day. It's a major hassle and…saving a couple hours a day would be amazing."

#### Reporting & Data Collation Overload
Performance marketers spend an inordinate amount of time building reports by hand. In one case, an in-house marketer said one full day each week was devoted to just assembling weekly reports for one business unit.

**Context:** Both in-house teams (especially at mid-to-large companies with siloed data systems) face this challenge when aggregating metrics from Google Ads, Facebook Ads, analytics platforms, call tracking and CRM exports.

**Pain Point:** Manual, repetitive reporting workflows – Every week or month, marketers must perform the same multi-step routine: log into multiple platforms, export CSVs or screenshots, update Excel/Sheets or PowerPoint templates, double-check numbers, and write insights.

**Time Impact:** Extremely High – Many report spending 4–8+ hours per week on routine reporting. That's 10–20% of their work hours lost to copy-pasting and formatting.

**Frustration Level:** High – This is one of the most universally cited pain points. One in-house team was so frustrated that they hired a full-time data analyst to take over the reporting pipeline.

**Current Solutions:** Common approaches include building live dashboards in Data Studio/Looker Studio or Power BI that pull directly from ad platforms. Using marketing data integration services (Supermetrics, Funnel.io, etc.) is also popular.

**Quote/Anecdote:** "We ended up outsourcing [reporting] because it's menial work – before that, it would take about a day each week to get the reporting together."

#### Navigating Ads Platforms & Data Extraction
Even day-to-day analysis in native ad platforms can be slow and tedious. One marketer confessed that finding the right data in Google Ads and analyzing it "consumes a significant portion" of the day, often more than it should.

**Context:** In-house marketers managing large campaigns with lots of segments (dozens of campaigns, hundreds of ad groups/keywords).

**Pain Point:** Cumbersome interfaces and siloed data views – performing analysis requires too many manual steps. Multi-platform comparison is even worse (comparing Google vs. Facebook requires exporting both).

**Time Impact:** Moderate – This can eat up 30–60+ minutes each day just in routine checks. Over a week, several hours might be lost in UI navigation overhead.

**Frustration Level:** Moderate – While not as demoralizing as reporting grunt work, this is a constant friction that "it's more time-consuming than it should be".

**Current Solutions:** Many create their own workarounds. Some use Google's official add-ons or APIs. Others build custom dashboards so they rarely have to poke around in the raw interface.

**Quote/Anecdote:** "Navigating through Google Ads to locate the right data, and then analyzing it, tends to consume a significant portion of my day… I enjoy the analytical process, but it often requires custom scripts to manage efficiently."

#### Repetitive Campaign Management Tasks
Certain PPC management tasks are done over and over, and marketers are eager to automate them. A ten-year PPC veteran noted that a lot of their workflow could be templatized – from campaign creation to routine optimizations.

**Context:** In-house teams managing large accounts or many products, and small teams that don't have junior staff to hand off repetitive chores to.

**Pain Point:** Tedious, error-prone workflow – things like setting up similar campaigns across multiple locations or duplicating a successful ad group structure requires lots of manual copying/pasting without automation.

**Time Impact:** High – Optimizing keywords and ads at scale can consume hours each week. Campaign setup can be even more – building out a full structure for a new product launch might take days if done manually.

**Frustration Level:** High – Many PPC managers find this work boring and beneath their strategic potential.

**Current Solutions:** Marketers use platform features like automated rules and Smart Bidding to alleviate some burden. Some subscribe to SaaS tools or utilize Google Ads Scripts.

**Quote/Anecdote:** "I've built tools for personal use cases (e.g. auto campaign creation from briefs, optimization workflows for keywords, search terms, ad copy, bids & budget, etc.)… I'd like to address pain points not covered by existing offerings on the market."

---

### Decision Bottlenecks and External Pressures

#### Limited Transparency in New "Black Box" Campaigns
The push toward automated campaign types (like Google's Performance Max) has created a knowledge gap. Nearly half of PPC experts (49%) say the "loss of insights and data" due to highly automated campaigns has made campaign management harder.

**Context:** Any performance marketer using Google's AI-driven products (PMax, Smart Shopping, Meta Advantage+ campaigns, etc.).

**Pain Point:** Data opacity and control loss – Marketers thrive on data, and now they're flying partially blind. It's frustrating not to see which creative or audience is failing.

**Time Impact:** Moderate – Teams spend extra time devising workarounds, like running "experiment" campaigns to glean insights.

**Frustration Level:** Moderate to High – It's a love-hate relationship: they enjoy better performance in some cases, but hate the lack of clarity.

**Current Solutions:** Marketers are adopting mix-and-match strategies: using automated campaigns for broad efficiency but supplementing them with manual campaigns in specific areas where they need insight.

**Statistic:** 49% of PPC experts find campaign management harder in the last two years due to "loss of insights and data" from automated campaign types.

#### Stakeholder Communication & Approval Bottlenecks
In-house marketers often face decision bottlenecks due to managers, executives, or clients who may not fully grasp digital performance nuances.

**Context:** In-house teams often report to marketing directors or CMOs who demand frequent updates, or to CEOs/CFOs who care about every dollar.

**Pain Point:** Decision and approval delays – e.g. needing sign-off to increase budget or launch new creative can bottleneck swift action. Additionally, constant updates are expected.

**Time Impact:** High (but hidden) – The time spent on emails, calls, and meetings to keep everyone calm and informed can rival the time spent actually managing campaigns.

**Frustration Level:** High – This can be very stressful. PPC managers joke about clients/bosses "making my hair turn gray" when they overreact to minor issues.

**Current Solutions:** Education and transparency are the main workarounds. Many in-house marketers create simplified dashboards for stakeholders to self-serve basic stats.

**Quotes:** "Optimizing campaigns is the easiest part of my day. Clients freaking out constantly…because a campaign's CPC went up $0.63 today is the hardest."

---

## Research Sources & Methodology

The insights above were synthesized from a range of industry discussions and reports, including:

- **Reddit Forums:** First-hand accounts on Reddit's PPC forums (r/PPC, r/digital_marketing) from in-house marketers and consultants
- **Industry Surveys:** PPCsurvey 2024 results on in-house team challenges
- **Marketing Tool Blogs:** Data integration and call tracking limitations (Funnel.io, WhatConverts.com)
- **Case Studies:** Agency case studies and real-world anecdotes

**Key Statistics:**
- 49% of PPC experts find campaign management harder due to "loss of insights and data" from automated campaign types
- 40% of in-house teams find constant platform changes challenging
- Performance marketers report spending 4-8+ hours per week on routine reporting (10-20% of work hours)
- Some teams spend up to 2 hours daily on manual offline conversion uploads

Each pain point includes specific context about company scenarios, challenges, impact levels, frustration levels, and current workarounds - providing a foundation for prioritizing which problems an AI-driven platform like Elly 3.0 could solve first. 