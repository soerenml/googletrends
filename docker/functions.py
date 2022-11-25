def interest_over_time(
    search_term: str,
    start_time: str,
    end_time: str
):
    """Extract top trends from Google Trends
    Args:
        search_term: term of interest
        start_time: start time
        end_time: end time
    Returns:
        df: pd.DataFrame
    """
    import pandas as pd
    from pytrends.request import TrendReq

    pytrends = TrendReq(hl='en-US', tz=360)

    pytrends.build_payload(
        [search_term],
        cat=0,
        timeframe=f'{start_time} {end_time}',
        geo='',
        gprop=''
        )

    df = pytrends.interest_over_time()
    return df
