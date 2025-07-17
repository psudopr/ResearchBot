from apscheduler.schedulers.background import BackgroundScheduler
from app.services.rss_crawler import crawl_rss_feed
from app.services.web_scraper import scrape_dynamic_content
from app.services.ai_service import summarize_text

scheduler = BackgroundScheduler()

def run_analysis_job(company_id: str, rss_feed_url: str, user_narrative: str, global_prompt: str):
    """The main job that runs the analysis for a company."""
    print(f"Running analysis for company {company_id}")
    articles = crawl_rss_feed(rss_feed_url)
    for article in articles:
        # This is a placeholder for the actual implementation.
        # You will need to check if the article has already been processed
        # before scraping and summarizing.
        content = scrape_dynamic_content(article.link)
        if content:
            summary = summarize_text(content, user_narrative, global_prompt)
            # Save the summary to the database
            print(summary)

def schedule_jobs(db):
    """Schedules the analysis jobs for all companies in the database."""
    companies = db.companies.find()
    for company in companies:
        scheduler.add_job(
            run_analysis_job,
            'interval',
            hours=company['analysis_frequency'],
            args=[company['_id'], company['rss_feed_url'], company['user_narrative'], ""], # Add global prompt
            id=str(company['_id'])
        )
    scheduler.start()
