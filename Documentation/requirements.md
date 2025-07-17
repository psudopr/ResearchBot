# Project Requirements: ResearchBot

**Time Spend:** 1'38" (prep for initial commit)

**Document Version:** 1.0

**Date:** July 15, 2025

---

## Executive Summary

ResearchBot is a Python-based automated workflow designed to provide sophisticated business and financial insights. By crawling and analyzing Google Alerts RSS feeds, the application will deliver multi-level summaries of news articles and financial data. A key feature is the hierarchical prompting system that aligns AI analysis with user-defined narratives, first consulting a global prompt, then a company-specific prompt, and finally the news content itself.

The system will feature a locally-hosted web interface for managing monitored companies, configuring analysis parameters, and viewing results. Users can input and refine their analytical narratives, which the AI uses to compare new information, identifying trends, contradictions, and strategic alignments. Phase 1 includes a localhost web application for daily updates, stock price visualization, and data management via a local MongoDB database. The ultimate goal is to provide actionable intelligence comparable to a senior-level business consultant, enabling informed marketing, communication, and financial decisions.

---

## Table of Contents

1.  [Introduction](#1-introduction)
2.  [Project Overview](#2-project-overview)
3.  [Functional Requirements](#3-functional-requirements)
4.  [Non-Functional Requirements](#4-non-functional-requirements)
5.  [Constraints](#5-constraints)
6.  [Assumptions](#6-assumptions)
7.  [Dependencies](#7-dependencies)
8.  [Open Issues](#8-open-issues)
9.  [Future Considerations](#9-future-considerations)

---

## 1. Introduction

### 1.1 Purpose of this Document

This document outlines the requirements for **ResearchBot**. It serves as a comprehensive guide for all stakeholders, ensuring a shared understanding of the project's goals, scope, and functionalities.

### 1.2 Project Scope

The project involves developing a **Python-based automated workflow** that leverages the Google CLI to crawl and analyze Google Alerts RSS feeds. The core functionality includes:

- **Configurable Crawling:** Users can set the crawling frequency (e.g., daily, 2-4 times per day).
- **Multi-Level Summarization:** The AI will generate three tiers of summaries for each article:
  1.  A single compound sentence.
  2.  Supporting bullet points.
  3.  A narrative summary (up to 250 words) indicating alignment with the user's prompt.
- **Hierarchical Prompting:** The AI's analysis will follow a structured hierarchy:
  1.  Global Project Prompt
  2.  Company-Specific Prompt
  3.  RSS Feed Content
- **Local Web Application:** A localhost web interface will allow users to manage monitored companies, edit narratives via text input or JSON upload, and view analysis results.
- **Data-Driven Insights:** The system will compare new information against user-defined narratives to identify trends, contradictions, and strategic alignments.
- **Phase 1 Deliverables:**
  - A homepage listing all monitored companies.
  - Detailed company pages for configuration and analysis.
  - 12-month stock price data visualization.
  - A "global summary" co-authored by the user and AI.
  - A list of analyzed articles with summaries.
  - Local **MongoDB** for data storage and retrieval.
- **Phase 2 and Beyond:** Email updates and interactive UI elements are planned for future phases.

### 1.3 Target Audience

The application is **invite-only**, targeting individual investors and marketing professionals with high financial acumen. It will operate exclusively in a localhost environment.

### 1.4 Definitions and Acronyms

_(This section will be populated as project-specific terms are identified.)_

---

## 2. Project Overview

### 2.1 Project Goals and Objectives

The primary goal is to synthesize information rapidly, enabling users to make informed marketing and financial decisions. The sole KPI for success will be **stock returns** resulting from the research provided.

### 2.2 Business Context

This is a **hobby project** with no broader business implications.

### 2.3 Stakeholders

- Developer(s)
- Initial user group (investors and marketing professionals)

---

## 3. Functional Requirements

### 3.1 User Stories / Use Cases

**User Story 1: Add/Manage Monitored Companies**

- As a user, I want to add a company by name/stock symbol or by providing a Google Alerts RSS feed URL.
- As a user, I want to see a list of all monitored companies on the homepage.
- As a user, I want to be notified if no new information is available from a feed.

**User Story 2: Configure Company Monitoring**

- As a user, I want to access a detailed configuration page for each company.
- As a user, I want to input or upload a JSON file with my narrative for a company.
- As a user, I want to specify the RSS feed URL and analysis frequency for each company.

**User Story 3: View Company Analysis and Insights**

- As a user, I want to see the last 12 months of stock price data.
- As a user, I want to view a "global summary" and a list of analyzed articles.
- As a user, I want to see structured summaries for each article and mark them as "read."

**User Story 4: Refine AI Guidance and Prompts**

- As a user, I want to set a global project prompt via text input or JSON upload.
- As a user, I want to edit the company-specific narrative and AI instructions.
- As a user, I want to ask the AI to summarize and update my prompts.

**User Story 5: Handle Crawling and Summarization Errors**

- As a user, I want to see clear error messages for failed crawls.
- As a user, I want to be able to manually re-run a failed crawl.

### 3.2 System Features

- **Company Management:** Add, list, and view details for monitored companies.
- **Google Alerts Integration:** Store and crawl Google Alerts RSS feeds.
- **Data Storage (MongoDB):** Store company configurations, analysis results, and crawl status.
- **Website Information Summarization:** Extract content and generate multi-level summaries.
- **User Narrative and Prompt Management:** Manage global and company-specific prompts.
- **News Analysis and Comparison:** Compare new information against user narratives.
- **Website Display (Phase 1):** Display stock data, summaries, and user input sections.
- **Error Handling:** Provide clear error messages and a manual re-crawl option.

---

## 4. Non-Functional Requirements

### 4.1 Performance

- Performance metrics are not strictly defined for Phase 1.
- The application will use the **Google CLI** for processing and summarization.

### 4.2 Security

- **User Authentication:** Basic user authentication is required.

### 4.3 Usability

- The UI should follow modern design best practices.
- The display will be static (no animations).
- Users are assumed to be technically proficient.

### 4.4 Reliability

- The application must provide an option to **re-run the previous job** in case of an error.

### 4.5 Maintainability

- **Code Standards:** Adhere to PEP 8 for Python and a consistent style guide for the frontend.
- **Documentation:** Maintain a comprehensive `README.md`, docstrings, and architecture notes.
- **Ease of Setup:** Use virtual environments and consider Docker for containerization.
- **Modularity:** Design the application with a clear separation of concerns.
- **Logging/Debugging:** Implement structured logging and error tracing.
- **Version Control:** Use Git with a simple branching strategy and descriptive commit messages.

### 4.6 Environmental Requirements

- **Operating System:** Windows 11
- **Browser:** Latest version of Chrome
- **Software:** Latest stable versions of Python, Node.js, MongoDB, etc.
- **AI Processing:** All AI processing will be done in the cloud.
- **Internet Access:** Required for all workflow components.

---

## 5. Constraints

### 5.1 Technical Constraints

- **Frontend:** HTML, CSS, JavaScript served by a Node.js server.
- **Backend:** Python for all logic, automation, and database interactions.
- **Web Server:** Node.js
- **Task Scheduling:** APScheduler or a native OS scheduler.
- **Database:** MongoDB
- **Integrations:** No third-party SaaS integrations.

### 5.2 Business Constraints

- **Budget:** Prioritize first-party development to minimize costs.
- **Timeline:** Fluid and not material.

### 5.3 Regulatory Constraints

- None.

---

## 6. Assumptions

- Google Alerts RSS feeds are stable and accessible.
- Websites are generally crawlable without significant anti-scraping measures.
- The cloud AI service is reliable and cost-effective.
- A reliable source for stock data is available.
- Users are technically proficient enough for local setup.
- The Google CLI can interact with Google Alerts as needed.
- Consistent internet connectivity is available.

---

## 7. Dependencies

- Google Alerts
- Cloud AI Service (e.g., Gemini API)
- Stock Data API
- MongoDB
- Python
- Node.js
- Web Browser (Chrome)
- Operating System (Windows 11 / macOS)
- Internet Connectivity
- Google CLI

---

## 8. Open Issues

- No issues have been identified at this time.

---

## 9. Future Considerations

- **Period-over-Period Comparison:** Analyze trends over user-defined timeframes.
- **AI-Driven Narrative Refinement:** Allow the AI to propose updates to the user's narrative.
- **Email Updates (Phase 2):** Implement email notification functionality.
- **Interactive Results Display:** Add filtering, sorting, and drill-down capabilities.
- **AI Podcast:** Generate audio summaries using text-to-voice models.
