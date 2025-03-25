from urllib.parse import urlparse, urlunparse

PARAMS_TO_REMOVE = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "fbclid", "gclid"]

def clean_url(url):
    parsed_url = urlparse(url)
    query_params = parsed_url.query.split("&")

    cleaned_params = [param for param in query_params if not any(p in param for p in PARAMS_TO_REMOVE)]
    cleaned_query = "&".join(cleaned_params)

    return urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, cleaned_query, parsed_url.fragment))
