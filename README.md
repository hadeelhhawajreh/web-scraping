# web-scraping
Scrape a history of jordan  page and record which passages need citations 
+ ### Feature Tasks and Requirements
+ Scrape a Wikipedia page and record which passages need citations.
> E.g. History of Jordan has 3 “citation needed” cases, as of this writing.

+ Your web scraper should report the number of citations needed.
+ Your web scraper should identify those cases AND include the relevant passage.
Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.

> + Implementation 
* Count function  named **get_citations_needed_count**  takes in a url and returns an integer
* Report function  named **get_citations_needed_report**  takes in a url and returns a string
