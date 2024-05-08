from urllib.parse import quote_plus, urljoin, quote

BASE_URL = "https://www.wattpad.com"
def build_story_search_query(query: str, mature: bool = True, limit: int = 15) -> str:
    """
    Build a search query for Wattpad.
    :param query: The query to search for.
    :param mature: Whether to include mature content.
    :param limit: The number of results to return.
    :return: The search query url.
    """
    return urljoin(
        BASE_URL,
        f"v4/search/stories?query={quote_plus(query)}&mature={str(mature).lower()}&limit={limit}&fields="
        + quote(
            "stories(id,title,voteCount,readCount,commentCount,description,mature,completed,cover,url,numParts,"
            "isPaywalled,paidModel,length,language(id),user(name),lastPublishedPart(createDate),promoted,sponsor(name,"
            "avatar),tags,tracking(clickUrl,impressionUrl,thirdParty(impressionUrls,clickUrls)),contest(endDate,"
            "ctaLabel,ctaURL)),total,tags,nextUrlstories(id,title,voteCount,readCount,commentCount,description,mature,"
            "completed,cover,url,numParts,isPaywalled,paidModel,length,language(id),user(name),lastPublishedPart("
            "createDate),promoted,sponsor(name,avatar),tags,tracking(clickUrl,impressionUrl,thirdParty(impressionUrls,"
            "clickUrls)),contest(endDate,ctaLabel,ctaURL)),total,tags,nextUrl"
        )
    )

def build_user_search_query(query: str, limit: int = 15, offset: int=0) -> str:
    """
    Build a search query for Wattpad.
    :param query: The query to search for.
    :param limit: The number of results to return.
    :param offset: The offset of the results. ie next page. used for pagination
    :return: The search query url.
    """
    return urljoin(
        BASE_URL,
        f"v4/search/users?query={quote_plus(query)}&limit={limit}&offset={offset}&fields="
        + quote("username,name,avatar,description,numLists,numFollowers,numStoriesPublished,badges,following")
    )


def build_browse_topics(language: int = 0) -> str:
    """
    Build a query to browse topics on Wattpad.
    :param language: The language (index) to browse in. 0 is all languages. 1 is English. Don't know the rest.
    :return: The search query url.
    """
    return urljoin(BASE_URL, f"v5/browse/topics?language={language}&fields=" + quote("topics(name,categoryID,CbrowseURL,tagURL)"))
