# ResearchBot

ResearchBot is an automated workflow designed to provide sophisticated business and financial insights by crawling and analyzing Google Alerts RSS feeds. It features a locally-hosted web interface for managing monitored companies, configuring analysis parameters, and viewing multi-level summaries of news articles and financial data.

## Key Features

*   **Multi-Level Summarization:** AI-generated three-tiered summaries for each article (single sentence, bullet points, narrative).
*   **Hierarchical Prompting:** AI analysis guided by a global project prompt, company-specific prompt, and RSS feed content.
*   **Local Web Application:** A user-friendly interface for managing companies, editing narratives (text or JSON), and viewing analysis results.
*   **Data-Driven Insights:** Compares new information against user-defined narratives to identify trends, contradictions, and strategic alignments.
*   **Stock Price Visualization:** Displays 12-month stock price data for monitored companies.
*   **Robust Backend:** A FastAPI application handling data processing, API endpoints, authentication, and scheduled tasks.
*   **Modern Frontend:** A React web application providing a dynamic user interface.

## Getting Started

To set up and run the ResearchBot, you will need to configure both the server and the application components.

### Server Setup

For detailed instructions on setting up the backend server, including database configuration, dependencies, and running the application, please refer to the [Server Project Setup Guide](Documentation/Server/1.0%20Project%20Setup.md).

### Application Setup

For detailed instructions on setting up the frontend application, including project creation, dependencies, and running the development server, please refer to the [Application Project Setup Guide](Documentation/Front/1.0%20Project%20Setup.md).

## Project Structure and Documentation

This project is meticulously documented to provide a clear understanding of its architecture and implementation details.

### Frontend (Application) Documentation

*   **Component Structure:** Learn about the organization and purpose of React components in the [Component Structure Guide](Documentation/Front/2.0%20Component%20Structure.md).
*   **Routing:** Understand how navigation is handled within the application in the [Routing Guide](Documentation/Front/3.0%20Routing.md).
*   **API Integration:** Details on how the frontend interacts with the backend API can be found in the [API Integration Guide](Documentation/Front/4.0%20API%20Integration.md).
*   **Styling:** Recommendations and guidelines for styling the application are in the [Styling Guide](Documentation/Front/5.0%20Styling.md).
*   **Authentication Components:** Implementation details for core authentication components like `AuthContext` and `PrivateRoute` are in the [Authentication Components Guide](Documentation/Front/6.0%20Authentication%20Components.md).
*   **User Interaction and Forms:** Design details for key user interaction components and forms are in the [User Interaction and Forms Guide](Documentation/Front/7.0%20User%20Interaction%20and%20Forms.md).
*   **Advanced UI Features:** Learn about the design for more complex UI features in the [Advanced UI Features Guide](Documentation/Front/8.0%20Advanced%20UI%20Features.md).

### Backend (Server) Documentation

*   **Database Setup:** Information on setting up the MongoDB database connection and defining data models is in the [Database Setup Guide](Documentation/Server/2.0%20Database%20Setup.md).
*   **RSS Feed Crawler:** Details on the implementation of the RSS feed crawler can be found in the [RSS Feed Crawler Guide](Documentation/Server/3.0%20RSS%20Feed%20Crawler.md).
*   **Web Scraper:** Learn about the web scraper and content extractor in the [Web Scraper Guide](Documentation/Server/4.0%20Web%20Scraper.md).
*   **AI Summarization:** Details on the AI summarization and analysis component are in the [AI Summarization Guide](Documentation/Server/5.0%20AI%20Summarization.md).
*   **API Endpoints:** A comprehensive overview of the REST API endpoints is in the [API Guide](Documentation/Server/6.0%20API.md).
*   **Task Scheduler:** Information on setting up the task scheduler using APScheduler is in the [Task Scheduler Guide](Documentation/Server/7.0%20Task%20Scheduler.md).
*   **Authentication:** Details on the JWT-based authentication system are in the [Authentication Guide](Documentation/Server/8.0%20Authentication.md).
*   **User Management:** Information on API endpoints for user registration and profile management is in the [User Management Guide](Documentation/Server/9.0%20User%20Management.md).
*   **Global Prompt Management:** Learn about the API for managing user-specific global project prompts in the [Global Prompt Management Guide](Documentation/Server/10.0%20Global%20Prompt%20Management.md).
*   **Stock Data Service:** Details on fetching historical stock data are in the [Stock Data Service Guide](Documentation/Server/11.0%20Stock%20Data%20Service.md).
*   **Error Handling Strategy:** Learn about the centralized error handling strategy for the FastAPI server in the [Error Handling Strategy Guide](Documentation/Server/12.0%20Error%20Handling%20Strategy.md).

## Project Overview and Gap Analysis

For a comprehensive understanding of the project's goals, scope, functional, and non-functional requirements, please refer to the [Project Requirements Document](Documentation/requirements.md).

To understand the identified gaps in the project planning documentation for both the Server (Backend) and the Application (Frontend), please refer to the [Project Documentation Gap Analysis](Documentation/gaps.md).